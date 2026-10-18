---
name: workbuddy2api-panel
description: 腾讯 CodeBuddy（小浣熊）账号池 OpenAI 兼容网关 workbuddy2api-panel 的完整知识库。涵盖多账号池调度、熔断冷却、会话粘性、定时任务（签到/活跃/旅行/保活）、成长任务一键完成（17/18）、Web 管理面板、部署方式、API 端点与上游接口。是 linguo2625469/workbuddy2api-panel（Sliverkiss/workbuddy2api 增强分支）的逆向/运维参考。当用户提到 workbuddy2api、CodeBuddy 网关、小浣熊 API 网关、成长任务一键完成、多账号池、连登兑换抽奖时使用。
---

# workbuddy2api-panel 知识库

## 概述

把腾讯 CodeBuddy（小浣熊，copilot.tencent.com）账号变成 **OpenAI 兼容 API** 的自托管多账号网关，附 Web 管理面板。非官方网关，仅限自用账号。

- 上游：Sliverkiss/workbuddy2api（**已删库**），本项目已同步至上游删库前最后一次提交 `ea8b1e5`，此后独立演进。
- 技术栈：Go 1.22+，单文件二进制（前端 go:embed 进二进制），或 Docker/GHCR 镜像。
- 默认监听 `:7863`，面板 `http://<host>:7863/panel/`。
- 授权协议 MIT。⚠️ 仅限自用（签到/保活/个人工具），禁止批量注册小号、转售接口、收费分发。auths/ 存明文 accessToken/refreshToken，注意安全。

## 核心能力

| 能力 | 说明 |
|---|---|
| OAuth 一键登录 | `login.sh` 设备授权流程，或面板「添加账号」浏览器内 OAuth，凭证落盘 auths/ 热加载 |
| 多账号池 | 快过期积分加权 + 成本分层 + 加权随机选号，Top-5 候选 + 防惊群 |
| 熔断与冷却 | 429 软冷却 600s 起指数退避（封顶 `soft_rate_max`）、404 固定 60s、402 硬冷却至次日 04:00、连续失败熔断、在途租约限流 |
| 会话粘性 | 同 conversation_id 绑定同账号，TTL 滚动续期，失败自动解绑，可镜像 Redis |
| 定时任务 | 签到（09/21 点）、活跃上报（10 点）、猫猫旅行（09/21）、token 保活（22 点），四类独立开关 |
| 流式+非流式 | 出站强制 stream:true，SSE 帧白名单重建，非流式本地聚合 |
| 推理兼容 | DeepSeek 思维链注入（thinking.type=enabled）、reasoning_content 回填、effort 档位自动降级 |
| 系统提示词体系 | 网关自有提示词替换客户端 system（默认 custom），消灭 system 来源内容误报；passthrough 遇拦截自动降级 |
| 指纹脱敏 | 出站请求体黑名单指纹字段清洗（可关闭） |
| 可观测 | 每请求一行表格日志，/healthz 带 service 身份标识可接负载均衡 |
| Web 面板 | 账号运维/用量积分分析/模型档位条件查询/在线热改配置/运行日志（IP·UA·时间区间）/任务中心 |

## 成长任务一键完成（17/18）

官方「成长计划」18 个成长任务中 17 个可面板一键纯 API 完成，无需安装客户端。任务计分走 `/v2/report` 行为上报，不同任务认不同客户端指纹（CLI/桌面/web）。上报 200 ≠ 计分，面板执行后轮询任务进度，达标自动调 Web 域领奖接口。

### 任务覆盖与一键方式

| 任务 | 奖励 | 一键完成方式 |
|---|---|---|
| first_buddy | +300c +8e | 解锁上报 → 同意协议 → 领养第一只 Buddy |
| create_canvas | +300c +5e | 设计画布创建事件组（Ardot 遥测） |
| chat_5 | +100c | 对话活跃上报 ×5（自动补足差额） |
| Model_chat_GLM5.2 | +100c +5e | glm-5.2 真实对话一次 |
| RichMeow_Chat | +100c +5e +UR | Buddy 桌面端对话事件链（6 事件，含成功回执） |
| Buddy_App | +100c +5e | Buddy 应用「发现→进入→授权」事件链 |
| Buddy_App_QQ | +50c +5e | 企鹅教师助手进入事件链（与上共用） |
| automation_1 | +100c +5e | 定时任务创建成功事件 |
| Library_read | +100c +5e | 资料库阅读点击（web 域上报） |
| template_5 | +100c +5e | 模板使用事件组 ×5 |
| playbook_prompt | +100c +5e | 灵感案例「做同款」发送事件 |
| expert_5 | +100c +5e | 真实专家召唤+使用链 ×5 |
| Expert_team_use_3 | +100c +5e | 专家团召唤+使用链 ×3 |
| Hp_Appearance | +100c +5e | 主题设置 + 皮肤生效事件 |
| Expert_lighthouse | +100c +5e | 轻量云专家召唤+使用链（真实对话 requestId，可免费领一个月轻量服务器） |
| skill_1 | +100c +5e | 真实对话 + 技能加载事件（skill_info） |
| automation_1 | +100c +5e | 定时任务创建成功事件 |

全新账号一键全做完 ≈ **+1950 credits +78 能量**，仅数个任务涉及真实对话（Model_chat_GLM5.2 一条、expert_5/Expert_team_use_3/skill_1 各数条 fast-model 短对话），其余全为行为事件上报，零对话消耗。

**不可自动的 1 个**：`Expert_Philanthropy`（需真实捐款，服务端校验捐赠回执，实测无法绕过）。

**幂等**：行为事件按天幂等，重复点「一键完成」不重复扣资源，已达标任务自动跳过。

### 关键实现（internal/panel/autotask.go）

- 指纹分三类：
  - CLI 指纹：www.codebuddy.cn
  - 桌面指纹：copilot.tencent.com + WorkBuddy/5.5.6 UA + workbuddy-desktop 事件族
  - web 指纹：www.workbuddy.cn + x-client-platform: web
- 专家类任务需要真实专家 id + 真实对话回执（internal/upstream/streak.go 之外的 expert 序列）。
- 事件链构造在 internal/upstream/desktop.go（桌面事件族）。
- 已知难点：`skill_1` 疑似要求真实 Skill 工具调用；`Expert_lighthouse` 需真实连接器授权——README 说可一键，代码注释标「仍未破解/不做」，实际以代码为准。

## 定时任务（schedule）

- `checkin_hours` [9,21]：签到，末尾自动跑**连登管家**（兑换已解锁档位 + 抽完抽奖次数）
- `activity_hours` [10]：活跃上报（点亮连登/解锁领养 + streak 自检）
- `travel_hours` [9,21]：猫猫旅行
- `keepalive_hours` [22]：token 保活
- `blackcat_hours` [23]：黑猫
- `growth_hours` [1]：成长任务
- `balance_refresh_minutes` 5：周期查余额更新池，冷却账号余额恢复自动解冻

连登档位 7/14/28 天兑换后发积分/能量/补签卡/抽奖次数，抽奖次数只能从兑换获得。

## 上游 API 端点（逆向实测）

### growth 域任务（internal/upstream/tasks.go）
- `GET  {webBase}/v2/activity/growth/tasks` — 全量任务列表（含 progress/accept_status）
- `POST {webBase}/v2/activity/growth/tasks/accept` body `{"task_codes":[...]}` — not_accepted → accepted
- `POST {webBase}/activity/growth/tasks/<task_code>/claim` — 完成态领奖（注意是单路径，不是 reward/claim；`/v2/activity/growth/tasks/reward/claim` 不存在）
  - 领奖需带 `Referer: https://www.workbuddy.cn/profile/growth-center`
  - 小程序口径：叠加 `X-Client-Platform: miniprogram` 头，列表是默认口径的超集（按 task_code 去重）

### billing 域（internal/upstream/client.go）
- 签到：`POST {billingBase}/billing/meter/daily-checkin`（global 首选，fallback `/v2/billing/meter/daily-checkin`）
- 已签到幂等识别：响应含「已签到」/「already」关键词即视为 IsAlreadyCheckin，不判失败
- 活跃上报：`POST {billingBase}/v2/report`（一条上报同时点亮 growth 连登 + 解锁 first_buddy 前置）

### 三个 base（按 realm 路由）
- chatBase：copilot.tencent.com 系（chat 域）
- billingBase：codebuddy.cn 系（billing/checkin/report）
- webBase：www.workbuddy.cn 系（web 域领奖）
- global realm 的多路径 fallback：先无 `/v2` 前缀，ErrNotFound 时换有 `/v2` 前缀

## API 端点（网关对外）

- `GET  /v1/models` — 模型列表（含 supported_efforts / default_effort / 积分倍率 / 输入输出上限）
- `GET  /status` — 账号状态汇总 + 每账号详情（disabled 透出 disabled_reason）
- `POST /v1/chat/completions` — 流式/非流式聊天
- `GET  /healthz` — 健康检查（无可用账号返回 503）
- `GET  /panel/` — Web 管理面板
- `/panel/api/*` — 面板后端接口

## 部署

- **Docker Compose（推荐）**：`git clone` → `cp config.example.json config.json` → `docker compose up -d --build` → 打开面板添加账号。
- **单文件**：`go build -trimpath -ldflags="-s -w" -o wb2api ./cmd/server`，首次运行自动生成 config.json（含随机 api_key），`./wb2api.exe -config config.json`。
- **GHCR 镜像**：`ghcr.io/linguo2625469/workbuddy2api-panel:latest`，挂载 `./auths`、`./data`、`./config.json`。
- **源码运行**：`go run ./cmd/server -config config.json`。
- 构建全部二进制：`cmd/server`（wb2api）、`cmd/signin`、`cmd/login`、`cmd/credit`。

## 配置关键项（config.json）

- `listen`（默认 :7863）、`api_key`（留空自动生成随机）
- `auth_dir` ./auths、`state_file` ./data/state.json
- `cooldown.soft_rate` / `soft_rate_max`
- `schedule.*` 各类任务开关与小时
- `upstream.user_agent` / `client_version` / `cli_version` / `client_name` / `device_token` / `device_token_file`（默认 5.5.4/2.137.1）
- `features.sanitize_blacklist_fingerprints`
- `prompt.mode`（custom/passthrough）、`prompt.file`
- `upstash.url` / `token`（Redis 镜像，可选）
- `pool.*`（max_in_flight、breaker、degrade、idle_weight、prefer_expiring、expiring_soon=168h、credit_floor=100）
- `session_sticky.*`（enabled、ttl=30m）
- 环境变量可覆盖部分配置（见 README「环境变量覆盖」）

## 与 mickeu 小浣熊 Surge 模块的关系

- 本项目的「签到」「活跃上报」「多账号池」能力与 `mickeu/surge` 的 `RaccoonOpenAI-Multi.sgmodule`（`Scripts/raccoon-openai-multi.js`）功能重叠、生态相同（CodeBuddy/小浣熊账号）。
- 现有 Surge 模块**没有**「成长任务一键完成」「连登兑换抽奖」「猫猫旅行」「活跃 streak 自检」——若需扩展，可借鉴 `internal/panel/autotask.go` + `internal/upstream/{report,tasks,desktop,streak}.go` 的事件链构造与 task_code。
- 本项目是完整 Go 服务端，Surge 脚本是轻量客户端身份头方案，两者取舍：服务端功能全但需部署；Surge 模块轻量但能力受限。
- 相关 Surge 模块维护备忘见 `surge-ios` 技能的 pitfalls-and-cookbook.md「小浣熊多账号模块维护备忘」。

## 参考资料（来源）

- 仓库：https://github.com/linguo2625469/workbuddy2api-panel
- 上游（已删除）：https://github.com/Sliverkiss/workbuddy2api ，本项目同步至删库前最后提交 `ea8b1e5`
- 本分支最新基线：commit `6b31db6d045e985042620c819c3a938002e7b0b1`（2026-10-12，Merge PR #152）
- 调研/归档日期：2026-10-19
- 关键源码文件：`internal/panel/autotask.go`、`internal/upstream/{tasks,report,client,desktop,streak,travel,payload,sse}.go`、`cmd/server/main.go`、`config.example.json`
- 本地克隆：`/var/minis/workspace/workbuddy2api-panel/`