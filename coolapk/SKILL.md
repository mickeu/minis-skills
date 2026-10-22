---
name: coolapk
description: 酷安社区搜索工具 — 搜索帖子、用户、应用、话题，浏览首页动态/热榜/板块/二手，查看用户资料。CLI 直调（coolapk），比 MCP Server 更省 token。触发词：酷安、coolapk、酷安搜索、酷安热榜、看酷安、数码社区。
---

# 酷安社区搜索工具

通过 `coolapk` CLI 搜索酷安社区内容，获取帖子、用户、话题、应用信息。所有命令输出精简 JSON（自动排除空值字段），适合直接解析。

## 环境（已在本机配置好）

- Python 包 `coolapk-mcp` 已 pip 安装，CLI 命令 `coolapk` / `coolapk-mcp` 全局可用。
- 已从酷安 APK（16.4.0 / versionCode 2607021）提取并缓存 `libauth.so` blob 到 `~/.coolapk-mcp/auth_blob.bin`，v3 token 可直接生成。
- 已把 `token_v3.py` 的版本常量更新为 16.4.0 / 2607021（与提取 blob 的 APK 一致）。
- 设备码已改为**随机生成**（原默认设备码是 qiuyurs/coolApkAPI 的共享硬编码值，被酷安风控标记为"设备登录账号过多"导致 -415）。
- 配置文件：`~/.coolapk-mcp/config.json`（device_code / uid / username / token）。

## 使用方式

### 搜索

```bash
# 搜索帖子（默认）
coolapk search "关键词"

# 搜索用户
coolapk search "用户名" --type user

# 搜索话题
coolapk search "话题" --type feedTopic

# 搜索应用
coolapk search "应用名" --type app

# 翻页
coolapk search "关键词" --page 2
```

### 帖子详情

```bash
# 查看帖子详情 + 回复
coolapk feed <帖子ID>

# 只要详情不要回复
coolapk feed <帖子ID> --no-replies

# 指定回复页码
coolapk feed <帖子ID> --reply-page 2
```

> ⚠️ **已知限制**：帖子详情接口 `/v6/feed/detail` 风控很严，本环境会返回 `{"error":"当前访问需要验证码","code":-1}`。这是酷安服务端 IP/环境级风控（上游 README 也承认此问题），搜索、列表、用户动态、热榜、话题等读接口通常可用。需要正文时，优先从搜索结果/用户动态列表里取 `content` 字段，或改用 `coolapk user <UID> --feeds` 拿公开帖。

### 用户

```bash
# 用户资料
coolapk user <UID>

# 用户帖子列表
coolapk user <UID> --feeds
coolapk user <UID> --feeds --page 2
```

### 首页 / 热榜 / 板块

```bash
# 首页推荐动态（默认）
coolapk home

# 热门
coolapk home --tab hot

# 最新
coolapk home --tab latest

# 热榜板块
coolapk hot

# 列出所有板块
coolapk boards

# 浏览指定板块（板块ID/page_name/url）
coolapk board <board_id> [--page N]

# 二手交易（1005=苹果等品牌ID）
coolapk secondhand [--brand <品牌ID>] [--page N]
```

### 话题

```bash
# 话题详情
coolapk topic "话题名"

# 话题下的帖子
coolapk topic "话题名" --feeds
```

### 私信 / 通知（读）

```bash
# 通知未读计数
coolapk notify

# 指定类型通知
coolapk notify comment
coolapk notify atMeMeFeed
coolapk notify feedLike

# 私信会话列表
coolapk message list

# 与某人的聊天记录
coolapk message chat <ukey>
```

### 交互（需先登录，本机默认未登录）

```bash
# 登录（传入 Cookie）
coolapk login --cookie "uid=xxx;username=xxx;token=xxx"

# 查看登录状态
coolapk login --status

# 点赞/取消赞
coolapk like <帖子ID>
coolapk unlike <帖子ID>

# 回复
coolapk reply <帖子ID> -m "回复内容"

# 关注/取消关注
coolapk follow <UID>
coolapk unfollow <UID>

# 发帖
coolapk post -m "帖子正文" [--pic <图片URL>]

# 上传图片
coolapk upload <文件路径>
```

## 注意事项

- 搜索和浏览**不需要登录**；点赞、回复、关注、发帖等写操作需要先 `login`。
- 所有输出为精简 JSON，自动排除空值字段。
- 若命令偶发 `SystemError: error return without exception set`（pydantic_core 冷启动导入失败，iSH 模拟环境下的已知不稳定），**重试一次即可**。
- 设备码保存在 `~/.coolapk-mcp/config.json`，不要用共享默认值（会被风控 -415）。
- 请合理使用接口频率，遵守酷安用户协议与当地法规。仅作个人/研究向信息检索。

## 参考资料（来源）

- 上游仓库：https://github.com/Lniosy/coolapk-mcp （MIT License，v0.1.0，coolapk-mcp）
- 本项目自带 `.claude/skills/coolapk.md` 与 `clawhub/SKILL.md`，本 SKILL.md 在两者基础上针对 Minis 环境补充了安装配置与已知限制。
- Token 算法来源：https://github.com/qiuyurs/coolApkAPI （coolapk_token.py + docs/TOKEN_ALGORITHM.md）
- 安装日期：2026-10-23。版本常量已随提取 blob 的 APK 更新为 16.4.0 / versionCode 2607021。
- 已知限制：`/v6/feed/detail` 接口在本环境返回验证码（-1），上游 README 已承认（原话：部分环境会稳定返回 `err_request_captcha_v2`）。