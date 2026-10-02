#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 mkdocs.yml 的 nav 提取所有 .md 文件路径，生成 sing-box 中文文档 raw URL。
中文版文件名规则（i18n suffix 模式）：xxx.md -> xxx.zh.md
输出 URL 清单到 /tmp/sb_raw_urls.txt（每行一个 URL），用于 minis-browser-use 批量下载。
"""
import re

yml = open("/var/minis/browser/1788148002_mkdocs.yml", encoding="utf-8").read()

# 提取 nav 里所有形如  configuration/xxx/yyy.md 的路径（- 后面或冒号后的 .md）
paths = re.findall(r"([\w\-/]+\.md)", yml)
# 去重保序
seen = set()
md_paths = []
for p in paths:
    if p not in seen:
        seen.add(p)
        md_paths.append(p)

print(f"nav 中 .md 文件数: {len(md_paths)}")

BASE = "https://raw.githubusercontent.com/SagerNet/sing-box/testing/docs"
# 中文版：xxx.md -> xxx.zh.md
urls = []
for p in md_paths:
    # index.md 这种顶层也加 .zh
    zh = p[:-3] + ".zh.md"
    urls.append(f"{BASE}/{zh}")

# 保存
with open("/tmp/sb_raw_urls.txt", "w") as f:
    for u in urls:
        f.write(u + "\n")

# 同时保存预期本地文件名（去掉前缀，保留相对路径，/ 换 _）
with open("/tmp/sb_local_names.txt", "w") as f:
    for p in md_paths:
        # 用相对路径做本地文件名：configuration/dns/index.md -> configuration_dns_index.zh.md
        local = p.replace("/", "_")[:-3] + ".zh.md"
        f.write(local + "\n")

print(f"生成 {len(urls)} 个 raw URL，保存到 /tmp/sb_raw_urls.txt")
print("前5个示例:")
for u in urls[:5]:
    print(" ", u)
