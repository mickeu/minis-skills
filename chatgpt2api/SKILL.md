# ChatGPT2API 知识库

> 来源：https://github.com/basketikun/chatgpt2api
> 作者：basketikun · 5975 star · 1592 fork · MIT 协议
> 版本：v1.8.0 · 创建 2026-04-19 · 最后更新 2026-08-24
> 完整源码已经克隆到同目录 `repo/`

**核心定位**：对 ChatGPT 官网能力（图片生成、编辑、文本、搜索）的**纯协议逆向封装**，暴露 OpenAI 兼容的 API / 代理，自带网页画图工作台、号池管理、多账号导入，支持 Docker 自托管。

## ⚠️ 重要前提与风险声明

- 本项目是官方没做成接口放开前的「白嫖」逆向方案，**有账号被限/封禁风险**（官方条款禁止）。
- 作者明确声明：仅供个人学习、技术研究与非商业交流，**严禁商业用途、批量滥用、二次倒卖**。
- 不要用自己重要的、高价值的官方账号来测试。
- 本项目主要面向**图片生成/编辑**场景（GPT-Image-2），文本/搜索是附带能力，不是通用聊天代理。

## 1. 快速部署

### 普通 Docker（推荐）
```bash
git clone git@github.com:basketikun/chatgpt2api.git
cd chatgpt2api
docker compose up -d
```
- 启动前在 `config.json` 设 `auth-key`，或在 `docker-compose.yml` 用 `CHATGPT2API_AUTH_KEY` 覆盖
- Web 面板：`http://localhost:3000`
- API 地址：`http://localhost:3000/v1`
- 数据目录：`./data`

### WARP + FlareSolverr（上游易被 Cloudflare 拦截时）
```bash
cp .env.example .env
docker compose -f docker-compose.warp.yml up -d --build
```
- 启动 `warp-proxy`(SOCKS5) → `privoxy`(转HTTP) → `flaresolverr`(刷CF clearance) → `init-config` → `app`
- 默认只接管上游 OpenAI/ChatGPT 请求，账号邮箱、CPA 等辅助链路不强制走代理

### 本地开发
```bash
uv sync && uv run main.py        # 后端 (Python 3.13)
cd web && bun install && bun run dev   # 前端
```

### 升级
```bash
docker pull ghcr.io/basketikun/chatgpt2api:latest
docker-compose down && docker-compose up -d
```
> 持久化关键项：`config.json`、`.env`、`data/`，升级迁移务必保留。

## 2. 存储后端（STORAGE_BACKEND）
| 值 | 说明 |
|---|---|
| `json` | 本地 JSON 文件（默认） |
| `sqlite` | 本地 SQLite |
| `postgres` | 外部 PostgreSQL，需 `DATABASE_URL` |
| `git` | Git 私有仓库同步，需 `GIT_REPO_URL` + `GIT_TOKEN` |

## 3. API 接口（全部需请求头 `Authorization: Bearer <auth-key>`）

所有 AI 调用都要带 auth-key。注意官方标准端口文档写 8000，Docker 默认 3000。

### GET /v1/models
返回图片模型：`gpt-image-2`、`codex-gpt-image-2`、`auto`、`gpt-5`、`gpt-5-1`、`gpt-5-2`、`gpt-5-3`、`gpt-5-3-mini`、`gpt-5-mini`

### POST /v1/images/generations（文生图）
```bash
curl http://localhost:8000/v1/images/generations \
  -H "Content-Type: application/json" -H "Authorization: Bearer <auth-key>" \
  -d '{"model":"gpt-image-2","prompt":"一只漂浮在太空里的猫","n":1,"response_format":"b64_json"}'
```
| 字段 | 说明 |
|---|---|
| `model` | 推荐 `gpt-image-2` |
| `prompt` | 提示词 |
| `n` | 生成数量，后端限制 1-4 |
| `response_format` | 默认 `b64_json` |

### POST /v1/images/edits（图编辑，支持多图）
文件上传（multipart）：
```bash
curl http://localhost:8000/v1/images/edits \
  -H "Authorization: Bearer <auth-key>" \
  -F "model=gpt-image-2" -F "prompt=改成赛博朋克夜景" -F "n=1" -F "image=@./input.png"
```
JSON 传图 URL（可多张）：
```bash
-d '{"model":"gpt-image-2","prompt":"...","images":[{"image_url":"https://example.com/input.png"}]}'
```

### POST /v1/chat/completions（文本+搜索+图片，非完整通用代理）
- 搜索：传 `web_search` / `web_search_preview` / `web_search_preview_2025_03_11` tools 或 `web_search_options`
- 文本链路默认 60 秒缓存 + 流式回放 + in-flight 合并，可用 `chat_completion_cache` 关闭
- `stream` 支持但仍在测试

### POST /v1/responses（Responses API 兼容，图片生成工具调用）
```bash
-d '{"model":"gpt-5","input":"生成未来城市","tools":[{"type":"image_generation"}]}'
```
- tools 支持 `image_generation`、`web_search` 等

### /v1/complete（文本补全与流式输出）已实现

## 4. 核心功能

### 在线画图工作台
- 生成、编辑、组图编辑；2k/4k（Codex 链路）
- 模型选择、参考图上传、历史回看/删除/清空、服务端 URL 缓存、进度追踪、超时续轮询、懒加载+滚动位置记忆

### 号池管理
- 自动刷新邮箱/类型/额度/恢复时间、轮询可用账号、剔除失效 Token、限流自动刷新
- 密码重登恢复异常账号、全局代理（HTTP/HTTPS/SOCKS5/SOCKS5H）
- 批量刷新/导出/编辑/清理、账号级代理
- **4 种导入方式**：本地 CPA JSON、远程 CPA 服务器、sub2api 服务器、access_token
- Pro 号约每天 1000 张额度，不再按无限处理

### Codex 画图逆向
- 仅 Plus/Team/Pro 订阅可用，别名 `codex-gpt-image-2`
- 同账号同时拥有官网 + Codex 两份生图额度（可自行映射回 gpt-image-2）

### 可编辑文件
- AI 生成**可编辑 PPT**、**可编辑 PSD** 文件

### 社区/生态
- 可接入 Cherry Studio、New API 等客户端/上游
- 社区：LinuxDO（linux.do）

## 5. 关键配置项（config.json）
| 项 | 默认 | 说明 |
|---|---|---|
| `auth-key` | chatgpt2api | 认证密钥（务必改） |
| `refresh_account_interval_minute` | 5 | 账号刷新间隔 |
| `image_parallel_generation` | true | 多图并行生成 |
| `image_account_concurrency` | 3 | 单账号并发 |
| `image_poll_timeout_secs` | 120 | 图片轮询超时 |
| `image_settle_enabled` | false | 二次确认；关闭跳过等待直接返回 |
| `image_check_before_hit_enabled` | false | 先check再hit |
| `chat_completion_cache.*` | — | 文本缓存/去重/流式回放 |
| `image_timeout_retry_secs` | 30 | 超时换账号重试等 |
| `default_upstream_model_name` | gpt-5-5 | 默认上游模型；支持 `-standard/-extended/-max` 后缀覆盖思考强度 |
| `default_thinking_effort` | auto | 默认思考强度 |
| `base_url` | "" | 生成图片 URL 用 |
| `proxy` / `proxy_runtime` | — | 全局代理 / 稳定代理运行时 |
| `ai_review` | off | AI 内容审核 |
| `backup` | off | 云 R2 备份 |
| `third_party_apps.infinite_canvas` | canvas.best | 无限画布跳转 |

### 环境变量（.env.example）
- `CHATGPT2API_AUTH_KEY` 必填
- `CHATGPT2API_BASE_URL`
- `STORAGE_BACKEND`、`DATABASE_URL`
- `GIT_REPO_URL`、`GIT_TOKEN`、`GIT_BRANCH`、`GIT_FILE_PATH`
- WARP/Privoxy/FlareSolverr 端口与 `CHATGPT2API_*` clearance 系列

## 6. 上游 Conversation SSE 协议要点
流式返回协议，`data:` 可能是 JSON payload、协议标记或结束标记，需按序消费：
- `"v1"` = 协议版本；`[DONE]` = 流结束；JSON=事件/patch；非 JSON=raw 事件
- 关键事件 type：`resume_conversation_token`、`input_message`、`message_marker`、`title_generation`、`server_ste_metadata`
- patch 结构：`p`(路径) + `o`(add/append/replace/patch) + `v`(值) + `c`(游标)
- 图片异步任务 type 通常为 `image_gen`
- `resume_conversation_token.token` 不应暴露给下游

## 7. 目录结构速览（repo/）
- `main.py` 入口 · `api/` OpenAI 兼容路由 · `services/` 业务逻辑
- `services/protocol/` OpenAI v1 各接口协议实现 + Anthropic 骨架（未完成）
- `services/storage/` json/sqlite/postgres/git 存储
- `services/` 含 account/cpa/sub2api/image/proxy/oauth/editable_file/backup 等服务
- `utils/` sentinel/PoW/turnstile/pkce 等逆向算法 · `web/` 前端(bun) · `scripts/` 运维脚本

## 8. 状态/规划
- ✅ 已实现：generations/edits/chat/responses/models@v1、多图并行、进度追踪、Cherry Studio/New API 接入、CPA+sub2api 导入、Password 重登、Docker 多架构镜像
- ⚠️ 完善中：高级 Token 调度、非 Docker 平台部署文档
- ❌ 未实现：图片尺寸参数、rt_token 刷新、Anthropic 协议

## 9. 注册机（已从 v1.7 移除，本技能库有 v1.6 全量存档）

> ⚠️ **状态**：v1.7 起作者移除了注册功能（防滥用导致 GitHub 账号被制裁）。当前官方版本（v1.8.0）**已无注册机**，只能通过 CPA/sub2api/access_token 导入现成账号。
> ✅ **但本技能库已从 git 历史 v1.6.0 tag 完整提取注册机全部代码**，存档在 `register/` 子目录，可单独研究/复用。

### 存档文件（register/）
| 文件 | 作用 |
|---|---|
| `backend/register.py` | /api/register 系列 API 路由（get/update/start/stop/reset/outlook-pool/reset/events SSE） |
| `backend/register_service.py` | 注册调度线程 + 号池合并 + 统计（total/quota/available 三种模式） |
| `backend/openai_register.py` | **核心注册逻辑**（652 行）：PKCE/OTP/sentinel 逆向 |
| `backend/mail_provider.py` | 邮箱提供商抽象（76KB） |
| `frontend/page.tsx`、`register-card.tsx` | 前端注册工作台 |
| `test/` | 注册代理/邮箱代理测试 |

### 注册核心流程（openai_register.py → PlatformRegistrar.register）
1. **创建邮箱** → `create_mailbox`（用邮箱 provider 生成一次性地址）
2. **platform authorize** → `_platform_authorize`（PKCE code_challenge，auth.openai.com）
3. **注册用户** → `_register_user`（提交邮箱+随机密码）
4. **发送 OTP** → `_send_otp`
5. **等验证码** → `wait_for_code`（轮询邮箱取 6 位码）
6. **校验 OTP** → `_validate_otp`
7. **创建账号资料** → `_create_account`（随机姓名+生日，带 `openai-sentinel-token`）
8. **换 token** → `request_platform_oauth_token`（code_verifier 换平台 token）

### 关键逆向点
- OAuth client：`app_2SKx67EdpoN0G6j64rFvigXD`，endpoint 走 `auth.openai.com` + `platform.openai.com`
- PKCE 用 code_challenge/code_verifier，`_generate_pkce()`
- 请求头带 `openai-sentinel-token`（`build_sentinel_token`）+ `oai-device-id`
- Cloudflare 拦截时走 **FlareSolverr clearance 刷新**（`_refresh_cloudflare_clearance`）
- 反爬 trace headers（`openai-sentinel-token`、`oai-did` 等）

### 邮箱提供商（mail_provider.py，13 种）
CloudflareTempMail · DDGMailᔌ · CloudMailGen · TempMailLol · DuckMail · GptMail · MoEmail · Inbucket · YydsMail · OutlookToken 池（含 outlook_token 邮箱池，支持 Outlook/Hotmail 收验证码）
- 随机邮箱名/随机域名，按 provider 轮换
- 邮箱 API 也可走注册代理 (`api_use_register_proxy`)

### 调度模式（register_service.py）
- `mode=total`：注册到指定总数
- `mode=quota`：冲到指定配额
- `mode=available`：保持指定可用账号数（`check_interval` 间隔巡检）
- 多线程（`threads`）+ 账号池合并（按邮箱去重）+ 限流自动刷新 + 失败统计

### 注册机当前可行性与警告（重要）
- **这段代码是 2026-06/07 的逆向快照**。OpenAI 注册链路（Auth0/sentinel/验证码/风控）随时在变，**存代码不等于还能用**，真用前必须逐一测端点返回。
- 注册成功极大依赖**邮箱域名不被 OpenAI 拉黑** —— 代码里直接提示「邮箱域名很可能因滥用被封禁，请更换邮箱域名」。
- 批量注册 = 账号大量封禁风险 + 违法 OpenAI ToS，**建议只用少量测试号验证流程可行性**，不要上量。

## 版本演进要点
- v1.6 Pro 号不再按无限额度（约 1000 张/天）
- v1.5 新增 WARP/Privoxy/FlareSolverr 清障、outlook_token 邮箱池、web 搜索兼容接口
- v1.4 新增可编辑 PSD/PPT 逆向、账号异步刷新密码重登、图片并行+超时换账号
- v1.3 新增 ChatGPT 搜索接口逆向 + Skills
- v1.2 基线：Web 面板、画图、号池、注册机、图片管理、日志、设置；Codex 链路生图 2k/4k
- v1.7 移除注册功能（防滥用导致 GitHub 封禁账号）

> ⚠️ v1.7 起**移除了注册机功能**，改用 CPA / sub2api / 账号导入。