#!/bin/bash
# vision-read.sh — Minis 视觉兜底链
# 顺序：小浣熊 Sn DeepSeek V4 1 Flash → apple-vision OCR
# 注：不用日日新（sensenova/kimi-k3）做视觉——2026-10-29 用户强制，日日新视觉经常失败
# 小浣熊（Xiaoxiong OpenAI）全系支持视觉，且请求体约 1MB 上限，图片在 make_json 中压缩后发送
# 用法：vision-read.sh <图片路径> [问题]
# 环境变量 FORCE_ENGINE 可强制指定引擎：xhx / 任意值（触发OCR兜底）
set -u
# 小浣熊视觉模型（Xiaoxiong OpenAI）
XHX="2527D111-C53C-4FEF-9F6C-DA804DCF6841/sn-deepseek-v4-1-flash"
IMG="${1:?用法: vision-read.sh <图片路径> [问题]}"
[ -f "$IMG" ] || { echo "错误: 图片不存在: $IMG" >&2; exit 2; }
Q="${2:-请描述这张图片的内容，逐条列出形状、颜色、文字等关键信息}"

make_json() { python3 - "$IMG" "$Q" <<'PY'
import base64, json, sys, io
path, q = sys.argv[1], sys.argv[2]
b64 = None
try:
    from PIL import Image
    img = Image.open(path).convert('RGB')
    w = 900
    h = int(img.height * w / img.width)
    img = img.resize((w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=75)
    b64 = base64.b64encode(buf.getvalue()).decode()
    mime = 'image/jpeg'
except Exception:
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = 'image/png'
json.dump({"messages":[{"role":"user","content":[
    {"type":"text","text":q},
    {"type":"image_url","image_url":{"url":f"data:{mime};base64,{b64}"}}]}]},
    open('/tmp/vision_input.json','w'), ensure_ascii=False)
PY
}

ask() {
    local model="$1" label="$2"
    make_json || return 1
    local out text
    out=$(timeout 90 minis-model-use run --model "$model" --input /tmp/vision_input.json 2>&1) || return 1
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
        xhx|raccoon) ENGINES=( "$XHX" ); LABELS=( "Sn DeepSeek V4 1 Flash (小浣熊)" );;
        *) echo "[vision-read] 未知引擎 $FORCE_ENGINE，跳过" >&2; ENGINES=();;
    esac
else
    ENGINES=( "$XHX" )
    LABELS=( "Sn DeepSeek V4 1 Flash (小浣熊)" )
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