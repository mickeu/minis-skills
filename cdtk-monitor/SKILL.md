---
name: cdtk-monitor
description: "coredevice-toolkit 一键健康监测：自动检查配对文件与 Surge 回环前置条件，一键读取电池真实健康（循环/容量/健康度）、扫描系统崩溃日志、统计进程数与已安装应用，支持文本与 JSON 输出。当用户提到「一键监测」「电池监测」「崩溃监测」「cdtk-monitor」「运行体检」「设备健康状况」时使用。触发词：cdtk-monitor, 一键监测, 电池监测, 崩溃监测, 设备体检, iOS 健康监测。"
compatibility: "iOS 18.0+, Bash (BusyBox 兼容), 依赖 coredevice-toolkit 已安装"
---

# cdtk-monitor 一键健康监测

基于 `coredevice-toolkit` 的一键化封装脚本，把「检查前置条件 → 电池诊断 → 崩溃扫描 → 进程/应用统计」整合为单条命令，适合日常设备体检或面板化输出。

---

## 一、前置条件

本技能依赖 `coredevice-toolkit` 已正确安装并可用：

1. **Surge 回环反射**已配置（`10.7.0.1 = reflect`，Local Device Loopback 模块）；
2. **配对文件**已就位：`/var/minis/workspace/cdtk/*.plist` 或 `CDTK_PAIRING_FILE` 指定；
3. **cdtk CLI** 已注册：`cdtk-diag`、`cdtk-crash`、`cdtk-ctrl`、`cdtk-install` 在 `/usr/local/bin/`；
4. 安装：`sh /var/minis/skills/coredevice-toolkit/scripts/setup.sh`。

---

## 二、用法

```bash
# 完整监测（电池 + 崩溃 + 进程/应用）
bash /var/minis/skills/cdtk-monitor/scripts/cdtk-monitor.sh

# 只监测电池
bash /var/minis/skills/cdtk-monitor/scripts/cdtk-monitor.sh --battery

# 只扫描崩溃
bash /var/minis/skills/cdtk-monitor/scripts/cdtk-monitor.sh --crash

# 只看进程/应用
bash /var/minis/skills/cdtk-monitor/scripts/cdtk-monitor.sh --apps

# JSON 输出（供脚本/面板解析）
bash /var/minis/skills/cdtk-monitor/scripts/cdtk-monitor.sh --json
```

### 输出示例（文本模式）

```
========================================
🔧 步骤 1/4：检查前置条件...
✅ 配对文件: /var/minis/workspace/cdtk/pairing.plist
✅ Surge 回环反射: 10.7.0.1:49152 可连通
✅ cdtk CLI 依赖检查完成

🔧 步骤 2/4：读取电池真实健康数据...
  • 真实充放电循环:   1353 次
  • 出厂设计容量:     3254 mAh
  • 当前实际物理容量: 2559 mAh (相对出厂: 78.6%)
  • 当前剩余电量:     75%
  • 当前电芯电压:     4.232 V
  • 充电状态:         ⚡ 正在充电

🔧 步骤 3/4：扫描最近崩溃日志...
✅ 发现 23 份系统崩溃日志
最近崩溃:
  • xp_amp_app_usage_dnu-2026-10-19-121600.ips
  • Turrit.cpu_resource-2026-10-19-142317.ips

🔧 步骤 4/4：统计系统进程与已安装应用...
✅ 系统进程: 483 个
✅ 已安装应用: 46 个
✨ 监测完成！
```

### JSON 输出示例

```json
{ "pairing_file":"/var/minis/workspace/cdtk/pairing.plist", "loopback":"ok",
  "battery_cycle":"1353", "battery_design":"3254", "battery_capacity":"2559",
  "battery_health":"78.6%", "battery_voltage":"4.240",
  "crash_count":"23", "crash_1":"...ips", "crash_2":"...ips",
  "process_count":"485", "app_count":"46" }
```

---

## 三、关键实现说明

- **前置检查**：自动发现配对文件（`CDTK_PAIRING_FILE` 优先 → 目录扫描兜底）、`nc` 探测 `10.7.0.1:49152` 回环连通性、校验 cdtk CLI 是否存在。
- **连续调用防冲突**：完整模式下命令间 `sleep 3`，避免 pmd-pytcp 协议栈 ARP Cache 竞态（`ARP Cache.start() called while a worker is still running`）。
- **BusyBox 兼容**：文本解析使用 `sed`/`awk`，**不用** `grep -P`（iSH/BusyBox 不支持 Perl 正则）。
- **超时保护**：每个 cdtk 子命令 `timeout 60`，防止偶发阻塞挂死。
- **安全**：脚本只读监测，不修改任何设备数据；配对文件仍遵循 coredevice-toolkit 的隔离与权限规范。

---

## 四、实测记录（2026-10-19，iOS 27.0 / 24A437）

- 电池：循环 1353 次 / 设计 3254 mAh / 实际 2559 mAh / 健康 78.6% / 电压 4.232V
- 崩溃：23 份（含 `Turrit.cpu_resource`、`xp_amp_app_usage_dnu` 等）
- 进程：483~485 个；已安装应用：46 个
- 完整模式 + JSON 模式均实测通过。

---

## 参考资料（来源）

- 上游技能：`coredevice-toolkit`（OpenMinis/MinisSkills 官方，作者 mickeu）——本机安装于 `/var/minis/skills/coredevice-toolkit/`，含配对指南、Surge 回环配置、cdtk CLI 全家桶。
- 实战调研与真机验证：2026-10-18~19，Minis on iPhone（iOS 27.0）。