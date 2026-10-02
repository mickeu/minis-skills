#!/bin/bash
# vision-read.sh — Minis 视觉兜底链
# 顺序：Kimi K3(日日新1→2→3) → apple-vision OCR
# 注：sensenova-6.8/6.7 在 token.sensenova.cn 上视觉不可用（2026-08-19 实测确认）
#    - content 数组 image_url → 400 "Unexpected item type"
#    - 顶层 images 字段 → 200 但图片不进视觉通道
# 2026-09-23：视觉模型从 Gemini 3 Flash 换成 Kimi K3（日日新新视觉模型，原生视觉力）
# 用法：vision-read.sh <图片路径> [问题]
# 环境变量 FORCE_ENGINE 可强制指定引擎：kimi / kimi1 / kimi2 / kimi3 / 任意值（触发OCR兜底）
set -u
# 日日新三个账号的 provider ID
P1="514FB615-1DEA-4595-8B4D-8A7228107131"
P2="5C26A146-BF51-4B05-B62B-38FEDFD0E9FB"
P3="5E0E4A8B-3EDF-4787-BEC1-B267B368E1D2"
IMG="${1:?用法: vision-read.sh <图片路径> [问题]}"
[ -f "$IMG" ] || { echo "错误: 图片不存在: $IMG" >&2; exit 2; }
Q="${2:-请描述这张图片的内容，逐条列出形状、颜色、文字等关键信息}"

make_json() { python3 - "$IMG" "$Q" <<'PY'
import base64, json, sys
with open(sys.argv[1],'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
json.dump({"messages":[{"role":"user","content":[
    {"type":"text","text":sys.argv[2]},
    {"type":"image_url","image_url":{"url":"data:image/png;base64,"+b64}}]}]},
    open('/tmp/vision_input.json','w'), ensure_ascii=False)
PY
}

ask() {
    local model="$1" label="$2"
    make_json || return 1
    local out text
    out=$(timeout 60 minis-model-use run --model "$model" --input /tmp/vision_input.json 2>&1) || return 1
    text=$(printf '%s' "$out" | python3 -c "import json,sys
try:
    d=json.load(sys.stdin)
    if not d.get('ok'): sys.exit(1)
    t=(d.get('data') or {}).get('output_text','').strip()
    if t: print(t)
    else: sys.exit(1)
except Exception: sys.exit(1)") || return 1
    echo "[vision-read] 引擎=$label"
    echo "$text"
}

declare -a ENGINES LABELS
if [ -n "${FORCE_ENGINE:-}" ]; then
    case "$FORCE_ENGINE" in
        kimi|kimi1) ENGINES=( "$P1/kimi-k3" ); LABELS=( "Kimi K3 (日日新1)" );;
        kimi2)      ENGINES=( "$P2/kimi-k3" ); LABELS=( "Kimi K3 (日日新2)" );;
        kimi3)      ENGINES=( "$P3/kimi-k3" ); LABELS=( "Kimi K3 (日日新3)" );;
        *) echo "[vision-read] 未知引擎 $FORCE_ENGINE，跳过" >&2; ENGINES=();;
    esac
else
    ENGINES=( "$P1/kimi-k3" "$P2/kimi-k3" "$P3/kimi-k3" )
    LABELS=( "Kimi K3 (日日新1)" "Kimi K3 (日日新2)" "Kimi K3 (日日新3)" )
fi

i=0
for e in "${ENGINES[@]}"; do
    echo "[vision-read] 尝试引擎: ${LABELS[$i]} ..." >&2
    if ask "$e" "${LABELS[$i]}"; then exit 0; fi
    echo "[vision-read] ${LABELS[$i]} 失败，切换下一个" >&2
    i=$((i+1))
done

echo "[vision-read] 视觉模型全部不可用，回退 apple-vision OCR" >&2
apple-vision ocr "$IMG" --lang zh-Hans,en --level accurate -q 2>&1 | head -c 3000
exit 0