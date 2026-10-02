#!/bin/bash
# 批量下载 sing-box 中文文档 raw markdown 到技能库
# 输入：/tmp/sb_raw_urls.txt (URL) + /tmp/sb_local_names.txt (本地文件名)
SK="/var/minis/skills/sing-box/docs"
mkdir -p "$SK"

total=$(wc -l < /tmp/sb_raw_urls.txt)
i=0
fail=0
while IFS= read -r url; do
    i=$((i+1))
    local_name=$(sed -n "${i}p" /tmp/sb_local_names.txt)
    # fetch（输出 JSON，提取 fetched_path）
    out=$(minis-browser-use fetch --url "$url" 2>&1)
    fpath=$(echo "$out" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['fetched_path'])" 2>/dev/null)
    if [ -n "$fpath" ] && [ -f "$fpath" ]; then
        cp "$fpath" "$SK/$local_name"
        printf "\r[%d/%d] OK %s" "$i" "$total" "$local_name"
    else
        fail=$((fail+1))
        printf "\r[%d/%d] FAIL %s\n" "$i" "$total" "$url"
    fi
done < /tmp/sb_raw_urls.txt

echo ""
echo "=== 完成：成功 $((total-fail))/$total，失败 $fail ==="
echo "技能库目录：$SK"
ls "$SK" | wc -l
