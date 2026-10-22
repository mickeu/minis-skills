#!/usr/bin/env python3
import os, sys, glob, smtplib, re, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate, make_msgid
from email.header import Header

DIARY_DIR = "/var/minis/shared/diaries"
os.makedirs(DIARY_DIR, exist_ok=True)

def get_env_or_first(*keys):
    for k in keys:
        v = os.environ.get(k)
        if v:
            return v.strip()
    return None

def get_smtp_config():
    # Support multiple common email providers
    user = get_env_or_first("DIARY_SMTP_USER", "MAIL_163_USER", "SMTP_USER", "EMAIL_USER")
    pwd = get_env_or_first("DIARY_SMTP_PASS", "MAIL_163_AUTH", "SMTP_PASS", "EMAIL_PASS")
    host = get_env_or_first("DIARY_SMTP_HOST", "SMTP_HOST")
    port = get_env_or_first("DIARY_SMTP_PORT", "SMTP_PORT")
    to_mail = get_env_or_first("DIARY_TO_EMAIL", "TARGET_EMAIL", "MAIL_TO")
    if not to_mail:
        raise ValueError("未配置收件人邮箱，请在 Minis 环境变量中设置 DIARY_TO_EMAIL")
    sender_name = get_env_or_first("DIARY_SENDER_NAME") or "AI伴侣"

    if not host and user:
        if "@163.com" in user:
            host, port = "smtp.163.com", 465
        elif "@qq.com" in user:
            host, port = "smtp.qq.com", 465
        elif "@gmail.com" in user:
            host, port = "smtp.gmail.com", 587
        elif "@outlook.com" in user or "@hotmail.com" in user:
            host, port = "smtp.office365.com", 587

    port = int(port) if port else 465
    return {
        "user": user,
        "pass": pwd,
        "host": host,
        "port": port,
        "to": to_mail,
        "name": sender_name
    }

def cmd_list():
    files = sorted(glob.glob(os.path.join(DIARY_DIR, "*.md")), reverse=True)
    if not files:
        print("📖 日记本还是空的哦，快写下第一篇吧～")
        return
    print(f"📖 【伴侣日记本】（共 {len(files)} 篇）")
    for f in files:
        b = os.path.basename(f)
        size = os.path.getsize(f)
        print(f"  - 📄 {b} ({size} 字节) -> minis://shared/diaries/{b}")

def cmd_read(date_str=None):
    if not date_str:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    target = os.path.join(DIARY_DIR, f"{date_str}.md")
    if not os.path.exists(target):
        print(f"❌ 未找到 {date_str} 的日记文件：{target}")
        sys.exit(1)
    with open(target, "r", encoding="utf-8") as f:
        print(f.read())

def render_html_letter(title, md_content, sender_name):
    # Basic markdown parsing to clean HTML
    paragraphs = []
    for line in md_content.splitlines():
        line = line.strip()
        if not line:
            paragraphs.append("<div style='height: 12px;'></div>")
        elif line.startswith("#### "):
            paragraphs.append(f"<h4 style='color:#e67e22;margin:16px 0 6px 0;font-size:16px;'>{line[5:]}</h4>")
        elif line.startswith("### "):
            paragraphs.append(f"<h3 style='color:#d35400;margin:18px 0 8px 0;font-size:18px;'>{line[4:]}</h3>")
        elif line.startswith("## "):
            paragraphs.append(f"<h2 style='color:#2c3e50;margin:20px 0 10px 0;font-size:20px;'>{line[3:]}</h2>")
        elif line.startswith("> "):
            paragraphs.append(f"<blockquote style='border-left:3px solid #f39c12;padding:6px 12px;background:#fef9e7;color:#7f8c8d;margin:8px 0;border-radius:4px;'>{line[2:]}</blockquote>")
        elif line.startswith("- "):
            paragraphs.append(f"<li style='margin-left:20px;color:#34495e;line-height:1.7;'>{line[2:]}</li>")
        else:
            paragraphs.append(f"<p style='color:#2c3e50;line-height:1.8;margin:6px 0;font-size:15px;'>{line}</p>")

    body_html = "\n".join(paragraphs)
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="margin:0;padding:24px 12px;background:#f5f0ea;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <div style="max-width:600px;margin:0 auto;background:#fffdf9;border-radius:16px;box-shadow:0 8px 24px rgba(0,0,0,0.06);border:1px solid #efe8dc;overflow:hidden;">
    <div style="background:linear-gradient(135deg,#ffecd2 0%,#fcb69f 100%);padding:28px 24px 20px 24px;border-bottom:1px solid #f2d6c9;">
      <span style="display:inline-block;padding:4px 10px;background:rgba(255,255,255,0.7);border-radius:20px;font-size:12px;color:#e67e22;font-weight:600;margin-bottom:8px;">💌 伴侣日记来信</span>
      <h1 style="margin:0;color:#2d3436;font-size:22px;font-weight:700;">{title}</h1>
    </div>
    <div style="padding:28px 24px 32px 24px;">
      {body_html}
    </div>
    <div style="background:#faf6f0;padding:16px 24px;text-align:center;border-top:1px solid #efe8dc;font-size:12px;color:#a4b0be;">
      ✨ 由 Minis 贴身 AI 伴侣亲笔撰写并寄出 · 完全随心，温暖常在
    </div>
  </div>
</body>
</html>"""

def cmd_mail(date_str=None):
    cfg = get_smtp_config()
    if not cfg["user"] or not cfg["pass"]:
        print("❌ 错误：未配置发信邮箱凭据！")
        print("请在环境变量或 Settings -> Environments 中设置：")
        print("  - MAIL_163_USER (发信账号)")
        print("  - MAIL_163_AUTH (发信授权码/密码)")
        print("  - DIARY_TO_EMAIL (收件人邮箱，默认支持 target 传参)")
        sys.exit(1)

    if not date_str:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    target = os.path.join(DIARY_DIR, f"{date_str}.md")
    if not os.path.exists(target):
        print(f"❌ 未找到 {date_str} 的日记：{target}")
        sys.exit(1)

    with open(target, "r", encoding="utf-8") as f:
        content = f.read()

    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else f"{date_str} 的心情日记"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(f"💌 {cfg['name']}的日记信件：{title}", "utf-8")
    msg["From"] = formataddr((cfg["name"], cfg["user"]))
    msg["To"] = formataddr(("亲爱的你", cfg["to"]))
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=cfg["user"].split("@")[-1])

    msg.attach(MIMEText(content, "plain", "utf-8"))
    html = render_html_letter(title, content, cfg["name"])
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        if cfg["port"] == 465:
            server = smtplib.SMTP_SSL(cfg["host"], cfg["port"], timeout=15)
        else:
            server = smtplib.SMTP(cfg["host"], cfg["port"], timeout=15)
            server.starttls()
        server.login(cfg["user"], cfg["pass"])
        server.sendmail(cfg["user"], [cfg["to"]], msg.as_string())
        server.quit()
        print(f"✅ 成功寄送日记信件至：{cfg['to']}")
    except Exception as e:
        print(f"❌ 邮件投递失败：{type(e).__name__}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
        print("Usage: diary-engine <list|read|mail> [date YYYY-MM-DD]")
        sys.exit(0)
    action = sys.argv[1]
    arg = sys.argv[2] if len(sys.argv) > 2 else None
    if action == "list":
        cmd_list()
    elif action == "read":
        cmd_read(arg)
    elif action == "mail":
        cmd_mail(arg)
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
