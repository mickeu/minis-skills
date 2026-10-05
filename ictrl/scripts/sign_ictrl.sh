#!/bin/bash
# iCTRL UITests-Runner 一键重签名脚本（zsign）
# 保留 PlugIns/*.xctest —— 这是大多数签名工具不处理的部分
#
# 用法:
#   sign_ictrl.sh <输入.ipa> <证书.p12> <证书密码> [描述文件.mobileprovision] [输出.ipa]
# 不传描述文件时自动使用 IPA 内嵌的 embedded.mobileprovision
set -e
ZSIGN="$(command -v zsign || echo /usr/local/bin/zsign)"
INPUT="$1"; CERT="$2"; PASS="$3"; PROV="$4"; OUTPUT="$5"
if [ -z "$INPUT" ] || [ -z "$CERT" ]; then
  echo "用法: $0 <input.ipa> <cert.p12> <password> [profile.mobileprovision] [output.ipa]" >&2
  exit 1
fi
OUTPUT="${OUTPUT:-${INPUT%.ipa}-signed.ipa}"
ARGS=(-k "$CERT" -p "$PASS")
[ -n "$PROV" ] && ARGS+=(-m "$PROV")
ARGS+=(-o "$OUTPUT" "$INPUT")
echo ">>> zsign 重签名: $INPUT"
echo ">>> 输出: $OUTPUT"
"$ZSIGN" "${ARGS[@]}"
echo ">>> 验证 xctest 是否保留..."
unzip -l "$OUTPUT" | rg -q 'PlugIns/.*\.xctest/' && echo "✅ xctest bundle 已保留并签名" || { echo "❌ xctest bundle 丢失！"; exit 1; }
echo ">>> 签名完成: $OUTPUT"
