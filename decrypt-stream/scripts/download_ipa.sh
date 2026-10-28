#!/bin/sh
# decrypt.stream 脱壳 IPA 下载辅助脚本
# 用法:
#   download_ipa.sh <bundle_id> [region] [输出路径]
#   默认 region=us，输出到当前目录 <bundle_id>_decrypted.ipa
# 示例:
#   download_ipa.sh ph.telegra.Telegraph
#   download_ipa.sh com.ss.iphone.ugc.tiktok.pro us /tmp/tiktok.ipa
set -e

BID="${1:?用法: download_ipa.sh <bundle_id> [region] [输出路径]}"
REGION="${2:-us}"
OUT="${3:-${BID}_decrypted.ipa}"

UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"

echo "下载 https://decrypt.stream/api/v1/download/${BID}?region=${REGION}"
echo "输出: ${OUT}"
curl -L -A "$UA" \
  "https://decrypt.stream/api/v1/download/${BID}?region=${REGION}" \
  -o "${OUT}"

echo "完成:"
ls -lh "${OUT}"
shasum -a 256 "${OUT}"