#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram 频道网页预览抓取工具（纯标准库，E2B 云沙箱 / 本地均可运行）

用途：抓取 @SurgeTestFlightFeed 等频道的公告原文（用于维护 surge-knowledge changelog）
原理：Telegram 网页预览 https://t.me/s/<channel> 渲染最近 ~20 条消息，
      data-post 属性定位消息，`?before=<post_id>` 向前翻页。

用法：
  # 按关键词搜索（如版本号），最多翻 3 页，输出 JSON 到 stdout
  python3 tg_channel_fetch.py --channel SurgeTestFlight --keywords "3871,3870" --pages 3

  # 抓取指定 post 的完整原文
  python3 tg_channel_fetch.py --channel SurgeTestFlight --posts "SurgeTestFlight/1798,SurgeTestFlight/1794"

  # 列出最近 N 条消息（post/日期/文本前 80 字符）
  python3 tg_channel_fetch.py --channel SurgeTestFlight --list --pages 1

输出：JSON 数组，每项 {post, date, text}

关键坑（务必记住）：
  1. data-post 属性后面还有 data-view 等属性，正则必须用 data-post="..." 后接 [^>]*>，
     不能直接写 data-post="...">。
  2. 消息块之间可能跳号（转发频道），翻页用最后一个 post id 作 ?before 参数。
  3. 本地 iSH 访问 t.me 会被 Surge 拦截（302 turrit://），必须经 E2B 云沙箱
     换美国出口运行。E2B 派单命令：
       python3 /var/minis/skills/e2b-cloud-ops/scripts/e2b-run.py \
         --file <本脚本> --cmd "python3 /home/user/tg_channel_fetch.py --channel ..."
     （e2b-run.py 上传到 /home/user/，不是 /tmp）
  4. 文本清理：<br> 转 \n，去 <b>/<i>/<a> 等标签，html.unescape 反转义。
"""
import argparse
import html
import json
import re
import urllib.request

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


def fetch_page(channel, before=None):
    url = f"https://t.me/s/{channel}"
    if before:
        url += f"?before={before}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def clean_text(raw):
    text = re.sub(r"<br\s*/?>", "\n", raw)
    text = re.sub(r"</?(b|i|u|strong|em)>", "", text)
    text = re.sub(r"<a[^>]*>", "", text)
    text = re.sub(r"</a>", "", text)
    text = re.sub(r"<code[^>]*>", "`", text)
    text = re.sub(r"</code>", "`", text)
    text = re.sub(r"<pre[^>]*>", "\n```\n", text)
    text = re.sub(r"</pre>", "\n```\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_page(body):
    """按 data-post 切块解析，避免跨块误配。返回 [(post, date, text)]"""
    posts = list(re.finditer(r'data-post="(SurgeTestFlight/\d+)"', body))
    results = []
    for i, m in enumerate(posts):
        start = m.start()
        end = posts[i + 1].start() if i + 1 < len(posts) else len(body)
        chunk = body[start:end]
        t = re.search(r'<time datetime="([^"]+)"', chunk)
        txtm = re.search(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', chunk, re.S)
        text = clean_text(txtm.group(1)) if txtm else ""
        results.append((m.group(1), t.group(1) if t else "", text))
    return results


def main():
    ap = argparse.ArgumentParser(description="Telegram 频道网页预览抓取")
    ap.add_argument("--channel", default="SurgeTestFlight")
    ap.add_argument("--keywords", help="逗号分隔关键词，命中任意即保留")
    ap.add_argument("--posts", help="逗号分隔指定 post（如 SurgeTestFlight/1798）")
    ap.add_argument("--list", action="store_true", help="列出最近消息摘要")
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--out", help="输出 JSON 到文件（默认 stdout）")
    args = ap.parse_args()

    all_msgs, before = [], None
    for _ in range(max(1, args.pages)):
        msgs = parse_page(fetch_page(args.channel, before))
        if not msgs:
            break
        all_msgs.extend(msgs)
        before = msgs[-1][0].split("/")[-1]
        if len(msgs) < 20:
            break

    # 去重
    seen, uniq = set(), []
    for m in all_msgs:
        if m[0] not in seen:
            seen.add(m[0])
            uniq.append(m)

    if args.list:
        for post, date, text in uniq:
            print(f"{post} | {date} | {text[:80]}")
        return

    if args.posts:
        wanted = {p.strip() for p in args.posts.split(",") if p.strip()}
        targets = [{"post": p, "date": d, "text": t} for p, d, t in uniq if p in wanted]
    elif args.keywords:
        kws = [k.strip() for k in args.keywords.split(",") if k.strip()]
        targets = [{"post": p, "date": d, "text": t} for p, d, t in uniq
                   if any(k in t for k in kws)]
    else:
        targets = [{"post": p, "date": d, "text": t} for p, d, t in uniq]

    out = json.dumps(targets, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"已写入 {args.out}，共 {len(targets)} 条")
    else:
        print(out)


if __name__ == "__main__":
    main()