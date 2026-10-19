#!/bin/bash
# ============================================================
# cdtk-monitor.sh — coredevice-toolkit 一键健康监测
#
# 功能：
#   1. 检查前置条件（配对文件 / Surge 回环 / 依赖）
#   2. 自动拉起诊断，输出汇总报告：
#      - 电池真实健康（循环/容量/健康度）
#      - 最近崩溃日志
#      - 系统进程总数
#      - 已安装应用数
#
# 用法：
#   bash cdtk-monitor.sh              # 完整监测
#   bash cdtk-monitor.sh --battery    # 只看电池
#   bash cdtk-monitor.sh --crash      # 只看崩溃
#   bash cdtk-monitor.sh --apps       # 只看进程/应用
#   bash cdtk-monitor.sh --json       # 输出 JSON 汇总（给脚本/面板用）
# ============================================================

set -uo pipefail

# ---------- 配置 ----------
PAIRING_DIR="${CDTK_PAIRING_DIR:-/var/minis/workspace/cdtk}"
LOOPBACK_IP="10.7.0.1"
RSD_PORT="49152"
CDTK_BIN="/usr/local/bin"
ONLY_BATTERY=0
ONLY_CRASH=0
ONLY_APPS=0
OUTPUT_JSON=0

# ---------- 参数解析 ----------
for arg in "$@"; do
    case "$arg" in
        --battery) ONLY_BATTERY=1 ;;
        --crash)   ONLY_CRASH=1 ;;
        --apps)    ONLY_APPS=1 ;;
        --json)    OUTPUT_JSON=1 ;;
        -h|--help)
            echo "用法: bash cdtk-monitor.sh [--battery|--crash|--apps] [--json]"
            exit 0 ;;
    esac
done

# ---------- 颜色（非 JSON 时） ----------
if [ "$OUTPUT_JSON" -eq 0 ]; then
    C_G="\033[32m"; C_R="\033[31m"; C_Y="\033[33m"; C_B="\033[34m"; C_N="\033[0m"
else
    C_G=""; C_R=""; C_Y=""; C_B=""; C_N=""
fi

ok()   { [ "$OUTPUT_JSON" -eq 0 ] && echo -e "${C_G}✅ $1${C_N}"; }
warn() { [ "$OUTPUT_JSON" -eq 0 ] && echo -e "${C_Y}⚠️  $1${C_N}"; }
err()  { [ "$OUTPUT_JSON" -eq 0 ] && echo -e "${C_R}❌ $1${C_N}"; }
info() { [ "$OUTPUT_JSON" -eq 0 ] && echo -e "${C_B}🔧 $1${C_N}"; }

# ---------- JSON 输出初始化 ----------
JSON_RESULT=""
jpush() { # jpush key value
    if [ -n "$JSON_RESULT" ]; then JSON_RESULT="$JSON_RESULT, "; fi
    JSON_RESULT="$JSON_RESULT\"$1\":\"$2\""
}

# ---------- 1. 前置检查 ----------
check_preflight() {
    [ "$OUTPUT_JSON" -eq 0 ] && echo "========================================"
    info "步骤 1/4：检查前置条件..."

    # 1a. 配对文件
    PAIRING_FILE=""
    if [ -n "${CDTK_PAIRING_FILE:-}" ] && [ -f "$CDTK_PAIRING_FILE" ]; then
        PAIRING_FILE="$CDTK_PAIRING_FILE"
    else
        for f in "$PAIRING_DIR"/*.plist; do
            [ -f "$f" ] && PAIRING_FILE="$f" && break
        done
    fi

    if [ -z "$PAIRING_FILE" ]; then
        err "未找到配对文件！请将 pairing.plist 放入 $PAIRING_DIR"
        err "获取方法：StikPair 生成后导出，或用 CDTK_PAIRING_FILE 指定路径。"
        [ "$OUTPUT_JSON" -eq 1 ] && echo "{\"status\":\"error\",\"error\":\"no_pairing_file\"}"
        exit 1
    fi
    ok "配对文件: $PAIRING_FILE"
    jpush "pairing_file" "$PAIRING_FILE"

    # 1b. Surge 回环端口
    if command -v nc >/dev/null 2>&1; then
        if nc -z -w 3 "$LOOPBACK_IP" "$RSD_PORT" 2>/dev/null; then
            ok "Surge 回环反射: $LOOPBACK_IP:$RSD_PORT 可连通"
            jpush "loopback" "ok"
        else
            warn "回环端口 $LOOPBACK_IP:$RSD_PORT 不通（Surge 回环可能未开启）"
            jpush "loopback" "fail"
        fi
    fi

    # 1c. 依赖
    for bin in cdtk-diag cdtk-crash cdtk-ctrl cdtk-install; do
        if [ ! -x "$CDTK_BIN/$bin" ]; then
            warn "缺少 $bin，请先运行 setup.sh"
            jpush "missing_bin" "$bin"
        fi
    done
    ok "cdtk CLI 依赖检查完成"
}

# ---------- 2. 电池诊断 ----------
run_battery() {
    [ "$OUTPUT_JSON" -eq 0 ] && echo ""
    info "步骤 2/4：读取电池真实健康数据..."
    local out
    out=$(cd "$PAIRING_DIR" && timeout 60 "$CDTK_BIN/cdtk-diag" hw 2>&1)
    local rc=$?
    if [ $rc -ne 0 ]; then
        err "电池诊断失败: $(echo "$out" | tail -3)"
        jpush "battery" "failed"
        return 1
    fi

    [ "$OUTPUT_JSON" -eq 0 ] && echo "$out"

    # 解析关键字段（兼容 BusyBox，不用 grep -P）
    local cycle cap design health voltage
    cycle=$(echo "$out" | sed -n 's/.*真实充放电循环:[[:space:]]*\([0-9][0-9]*\).*/\1/p' | head -1)
    design=$(echo "$out" | sed -n 's/.*出厂设计容量:[[:space:]]*\([0-9][0-9]*\).*/\1/p' | head -1)
    cap=$(echo "$out" | sed -n 's/.*当前实际物理容量:[[:space:]]*\([0-9][0-9]*\).*/\1/p' | head -1)
    health=$(echo "$out" | sed -n 's/.*相对出厂:[[:space:]]*\([0-9][0-9.]*%\).*/\1/p' | head -1)
    voltage=$(echo "$out" | sed -n 's/.*当前电芯电压:[[:space:]]*\([0-9][0-9.]*\).*/\1/p' | head -1)
    jpush "battery_cycle" "${cycle:-N/A}"
    jpush "battery_design" "${design:-N/A}"
    jpush "battery_capacity" "${cap:-N/A}"
    jpush "battery_health" "${health:-N/A}"
    jpush "battery_voltage" "${voltage:-N/A}"
    return 0
}

# ---------- 3. 崩溃日志 ----------
run_crash() {
    [ "$OUTPUT_JSON" -eq 0 ] && echo ""
    info "步骤 3/4：扫描最近崩溃日志..."
    local out
    out=$(cd "$PAIRING_DIR" && timeout 60 "$CDTK_BIN/cdtk-crash" list 2>&1)
    local rc=$?
    if [ $rc -ne 0 ]; then
        err "崩溃扫描失败: $(echo "$out" | tail -3)"
        jpush "crash_count" "failed"
        return 1
    fi

    local count
    count=$(echo "$out" | sed -n 's/.*发现[[:space:]]*\([0-9][0-9]*\)[[:space:]]*份系统崩溃日志.*/\1/p' | head -1)
    [ -z "$count" ] && count=$(echo "$out" | sed -n 's/.*共[[:space:]]*\([0-9][0-9]*\)[[:space:]]*份.*/\1/p' | head -1)
    [ -z "$count" ] && count="?"
    ok "发现 $count 份系统崩溃日志"
    jpush "crash_count" "$count"

    # 提取最近几条文件名
    local recent
    recent=$(echo "$out" | awk '/Crash\(崩溃\)/ {print $NF}' | head -5)
    if [ -n "$recent" ]; then
        [ "$OUTPUT_JSON" -eq 0 ] && echo "最近崩溃:"
        local i=0
        while IFS= read -r f; do
            [ "$OUTPUT_JSON" -eq 0 ] && echo "  • $f"
            i=$((i+1))
            jpush "crash_$i" "$f"
        done <<< "$recent"
    fi
    return 0
}

# ---------- 4. 进程 & 应用 ----------
run_apps() {
    [ "$OUTPUT_JSON" -eq 0 ] && echo ""
    info "步骤 4/4：统计系统进程与已安装应用..."

    # 进程数
    local procs_out
    procs_out=$(cd "$PAIRING_DIR" && timeout 60 "$CDTK_BIN/cdtk-ctrl" procs 2>&1)
    local proc_count
    proc_count=$(echo "$procs_out" | sed -n 's/.*当前系统共运行[[:space:]]*\([0-9][0-9]*\)[[:space:]]*个进程.*/\1/p' | head -1)
    [ -z "$proc_count" ] && proc_count="?"
    ok "系统进程: $proc_count 个"
    jpush "process_count" "$proc_count"

    # 已安装应用数
    local apps_out apps_count
    apps_out=$(cd "$PAIRING_DIR" && timeout 60 "$CDTK_BIN/cdtk-install" list 2>&1)
    apps_count=$(echo "$apps_out" | sed -n 's/.*共查询到[[:space:]]*\([0-9][0-9]*\)[[:space:]]*个已安装应用.*/\1/p' | head -1)
    [ -z "$apps_count" ] && apps_count="?"
    ok "已安装应用: $apps_count 个"
    jpush "app_count" "$apps_count"
    return 0
}

# ---------- 主流程 ----------
main() {
    check_preflight

    if [ "$ONLY_BATTERY" -eq 1 ]; then
        run_battery
    elif [ "$ONLY_CRASH" -eq 1 ]; then
        run_crash
    elif [ "$ONLY_APPS" -eq 1 ]; then
        run_apps
    else
        # 完整监测，命令之间留时间让协议栈清理
        run_battery
        sleep 3
        run_crash
        sleep 3
        run_apps
    fi

    [ "$OUTPUT_JSON" -eq 0 ] && echo ""
    [ "$OUTPUT_JSON" -eq 0 ] && echo "========================================"
    [ "$OUTPUT_JSON" -eq 0 ] && echo -e "${C_G}✨ 监测完成！${C_N}"

    if [ "$OUTPUT_JSON" -eq 1 ]; then
        echo "{ $JSON_RESULT }"
    fi
}

main "$@"