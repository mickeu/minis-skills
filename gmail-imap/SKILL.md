---
name: gmail-imap
description: >
  通过 Python IMAP 访问 Gmail 邮箱。当用户提到"Gmail"、"谷歌邮箱"、"域名邮箱"、"查邮件"、"收邮件"、"看邮件"、
  "搜邮件"、"邮箱"、"收件箱"、"未读邮件"时触发。使用 IMAP 协议 + 应用专用密码，
  支持列出收件箱、搜索邮件、读取邮件全文。依赖两个环境变量：GMAIL_EMAIL（邮箱地址）、
  GMAIL_APP_PASSWORD（Google 应用专用密码）。
source_url: https://github.com/OpenMinis/MinisSkills/pull/75
source_repo: https://github.com/OpenMinis/MinisSkills
license: MIT
last_sync: 2026-07-26
---

# Gmail IMAP 技能

通过 Python 内置 `imaplib` 访问 Gmail 收件箱，零外部依赖。

## 前置条件

用户需要在 Google 账号完成以下两步：

1. **开启两步验证** → https://myaccount.google.com/security/signinoptions/two-step-verification
2. **生成应用专用密码** → https://myaccount.google.com/apppasswords（名称填 "Minis"）

## 环境变量

| 变量名 | 说明 |
|-------|------|
| `GMAIL_EMAIL` | Gmail 邮箱地址，如 `example@gmail.com` |
| `GMAIL_APP_PASSWORD` | 16 位应用专用密码（含空格） |

检查是否设置：
```bash
[ -n "$GMAIL_EMAIL" ] && echo "email ok" || echo "email missing"
[ -n "$GMAIL_APP_PASSWORD" ] && echo "password ok" || echo "password missing"
```

如未设置，提供链接让用户去 Settings 中配置：
- [设置 GMAIL_EMAIL](minis://settings/environments?create_key=GMAIL_EMAIL&create_value=)
- [设置 GMAIL_APP_PASSWORD](minis://settings/environments?create_key=GMAIL_APP_PASSWORD&create_value=)

## 脚本路径

资源脚本位于 `scripts/gmail_imap.py`。

## 可用命令

```bash
# 列出收件箱最新邮件（默认 10 封）
python3 /var/minis/skills/gmail-imap/scripts/gmail_imap.py list [数量]

# 搜索含有关键字的邮件
python3 /var/minis/skills/gmail-imap/scripts/gmail_imap.py search <关键词> [结果数]

# 读取指定邮件全文（序号 1=最新）
python3 /var/minis/skills/gmail-imap/scripts/gmail_imap.py read [序号]
```

## 工作流程

1. 检查 `$GMAIL_EMAIL` 和 `$GMAIL_APP_PASSWORD` 是否已设置
2. 如未设置：提醒用户并给出设置链接
3. 如已设置：直接运行脚本执行用户请求的操作
4. 用户明确要求时，可保存邮件内容到 workspace

## 示例

```
user: 帮我看看 Gmail 收件箱
action: 检查环境变量 → 运行 list → 展示结果

user: 搜一下 Gmail 里关于 FlutterFlow 的邮件
action: 运行 search FlutterFlow → 展示匹配邮件

user: 帮我读一下最新那封邮件
action: 运行 read 1 → 展示邮件全文
```

## 来源与更新

- 来源仓库：https://github.com/OpenMinis/MinisSkills
- 来源链接：https://github.com/OpenMinis/MinisSkills/pull/75
- 许可证：MIT
- 最后同步：2026-07-26
- 检查更新命令：
  ```bash
  curl -sL "https://api.github.com/repos/OpenMinis/MinisSkills/pulls/75" | grep -o '"updated_at": "[^"]*"' | head -1
  ```
