#!/usr/bin/env python3
"""
Gmail IMAP 访问脚本 — 使用 Python 内置 imaplib
前置条件：
  1. 在 Google 账号开启两步验证
  2. 生成应用专用密码：https://myaccount.google.com/apppasswords
  3. 将密码填入下方或设为环境变量 GMAIL_APP_PASSWORD
"""

import imaplib
import email
import os
import sys
from email.header import decode_header

# ============ 配置 ============
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
EMAIL = os.environ.get("GMAIL_EMAIL")
PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

if not EMAIL or not PASSWORD:
    print("⚠️  请设置环境变量：")
    print("    export GMAIL_EMAIL='your.email@gmail.com'")
    print("    export GMAIL_APP_PASSWORD='你的16位应用专用密码'")
    print("")
    print("  也可在 Settings → Environment Variables 中永久设置：")
    print("    - GMAIL_EMAIL")
    print("    - GMAIL_APP_PASSWORD")
    sys.exit(1)


def decode_str(s):
    """解码邮件标题/发件人"""
    if not s:
        return ""
    parts = decode_header(s)
    result = []
    for content, charset in parts:
        if isinstance(content, bytes):
            try:
                result.append(content.decode(charset or "utf-8", errors="replace"))
            except (LookupError, UnicodeDecodeError):
                result.append(content.decode("utf-8", errors="replace"))
        else:
            result.append(content)
    return " ".join(result)


def get_email_body(msg):
    """提取邮件正文（优先纯文本）"""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = str(part.get("Content-Disposition", ""))
            if content_type == "text/plain" and "attachment" not in disposition:
                try:
                    return part.get_payload(decode=True).decode("utf-8", errors="replace")
                except:
                    return part.get_payload(decode=True).decode("gbk", errors="replace")
    else:
        try:
            return msg.get_payload(decode=True).decode("utf-8", errors="replace")
        except:
            return msg.get_payload(decode=True).decode("gbk", errors="replace")
    return "[无法解析的邮件内容]"


def list_inbox(max_emails=10):
    """列出收件箱最近的邮件"""
    print(f"📥 连接 {IMAP_SERVER}:{IMAP_PORT} ...")
    conn = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    conn.login(EMAIL, PASSWORD)
    conn.select("INBOX")

    status, msg_ids = conn.search(None, "ALL")
    if status != "OK":
        print("❌ 搜索失败")
        return

    ids = msg_ids[0].split()
    recent = ids[-max_emails:]  # 取最新的 N 封

    print(f"\n{'='*60}")
    print(f"📬 收件箱共 {len(ids)} 封邮件，显示最近 {len(recent)} 封：")
    print(f"{'='*60}\n")

    for i, mid in enumerate(reversed(recent), 1):
        status, data = conn.fetch(mid, "(RFC822)")
        if status != "OK":
            continue
        msg = email.message_from_bytes(data[0][1])

        subject = decode_str(msg["Subject"]) or "(无主题)"
        sender = decode_str(msg["From"]) or "(未知发件人)"
        date = msg["Date"] or "(未知日期)"

        print(f"── [{i}] ────────────────────────────────")
        print(f"  发件人: {sender}")
        print(f"  主题:   {subject}")
        print(f"  日期:   {date}")
        print(f"  {'─'*40}")

    conn.logout()


def search_emails(keyword="通知", max_results=5):
    """搜索含关键字的邮件"""
    print(f"🔍 搜索关键字: '{keyword}' ...")
    conn = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    conn.login(EMAIL, PASSWORD)
    conn.select("INBOX")

    status, msg_ids = conn.search(None, f'BODY "{keyword}"')
    if status != "OK":
        print("❌ 搜索失败")
        return

    ids = msg_ids[0].split()
    if not ids:
        print("  未找到匹配邮件")
        conn.logout()
        return

    recent = ids[-max_results:]
    print(f"\n📬 找到 {len(ids)} 封匹配邮件，显示最近 {len(recent)} 封：\n")

    for i, mid in enumerate(reversed(recent), 1):
        status, data = conn.fetch(mid, "(RFC822)")
        if status != "OK":
            continue
        msg = email.message_from_bytes(data[0][1])

        subject = decode_str(msg["Subject"])
        sender = decode_str(msg["From"])
        date = msg["Date"]
        body_preview = get_email_body(msg)[:200]

        print(f"── [{i}] ────────────────────────────────")
        print(f"  发件人: {sender}")
        print(f"  主题:   {subject}")
        print(f"  日期:   {date}")
        print(f"  预览:   {body_preview}...")
        print(f"  {'─'*40}")

    conn.logout()


def read_email_by_index(idx=1):
    """按序号（1=最新）读取邮件全文"""
    print(f"📥 连接 {IMAP_SERVER}:{IMAP_PORT} ...")
    conn = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    conn.login(EMAIL, PASSWORD)
    conn.select("INBOX")

    status, msg_ids = conn.search(None, "ALL")
    if status != "OK":
        print("❌ 搜索失败")
        return

    ids = msg_ids[0].split()
    if idx < 1 or idx > len(ids):
        print(f"❌ 序号超出范围（1 ~ {len(ids)})")
        conn.logout()
        return

    # idx 从 1 开始，最新的是最后一个
    mid = ids[-idx]
    status, data = conn.fetch(mid, "(RFC822)")
    if status != "OK":
        print("❌ 读取失败")
        conn.logout()
        return

    msg = email.message_from_bytes(data[0][1])

    subject = decode_str(msg["Subject"]) or "(无主题)"
    sender = decode_str(msg["From"]) or "(未知发件人)"
    date = msg["Date"] or "(未知日期)"
    to = decode_str(msg["To"]) or ""

    print(f"\n{'='*60}")
    print(f"📩 第 {idx} 封邮件（最新）")
    print(f"{'='*60}")
    print(f"  发件人: {sender}")
    print(f"  收件人: {to}")
    print(f"  主题:   {subject}")
    print(f"  日期:   {date}")
    print(f"{'='*60}\n")

    body = get_email_body(msg)
    print(body[:3000])  # 正文前 3000 字符
    if len(body) > 3000:
        print(f"\n...（全文共 {len(body)} 字符，已截断）")

    conn.logout()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 /var/minis/skills/gmail-imap/scripts/gmail_imap.py <命令> [参数]")
        print("")
        print("  命令:")
        print("    list [数量]        列出最近邮件")
        print("    read [序号]         读取邮件全文（序号 1=最新）")
        print("    search <词> [数量]  搜索邮件")
        print("")
        print("  示例:")
        print("    python3 gmail_imap.py list 5")
        print("    python3 gmail_imap.py read 1")
        print("    python3 gmail_imap.py search 发票 3")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "list":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        list_inbox(count)
    elif cmd == "read":
        idx = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        read_email_by_index(idx)
    elif cmd == "search":
        keyword = sys.argv[2] if len(sys.argv) > 2 else "通知"
        count = int(sys.argv[3]) if len(sys.argv) > 3 else 5
        search_emails(keyword, count)
    else:
        print(f"❌ 未知命令: {cmd}")