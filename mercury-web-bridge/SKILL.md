# Mercury 网页版桥接（mercury-web-bridge）

在 Minis 对话框里直接使用 chat.inceptionlabs.ai 网页版的免费 Mercury 3 能力，无需注册 API Key。

## 触发场景
- 用户说「问 Mercury」「用 Mercury 回答」「Mercury：xxx」「让 Mercury 写代码」等
- 任何需要调用 Inception 网页版免费额度的场景

## 原理（重要）
- `chat.inceptionlabs.ai` 部署在 Vercel，有 **Vercel Security Checkpoint**，只放行真实浏览器（JS Proof-of-Work 挑战）。curl、Surge `$httpClient`、服务器转发全部 429。
- **Minis 内置浏览器是唯一能通过挑战的客户端**。
- 因此「反代」= 用 Minis 内置浏览器作为执行引擎：在浏览器会话里 `fetch('/api/session')` 拿匿名 token → `fetch('/api/chat')` 发送消息 → 解析 SSE 流（`text-delta`）得到回答。
- 关键接口：
  - `GET /api/session` → `{"ok":true,"token":"..."}`（每 ~78 秒刷新）
  - `POST /api/chat` 需要 header `x-session-token`，body 用 Vercel AI SDK parts 格式（不传 model 字段，模型由后端按模式固定为 Mercury 3）。
- 请求体关键字段：`reasoningEffort`（instant/low/medium/high）、`webSearchEnabled`、`timezone`、`language`、`id`、`messages:[{role, parts:[{type:"text",text}], id}]`、`trigger:"submit-message"`。
- 响应是 SSE：`data: {"type":"text-delta","delta":"..."}` 累加即完整回答。

## 使用步骤（Agent 操作）

### 方式 A：直接驱动浏览器（最简单，不依赖 HTTP 服务）
1. 确保有一个浏览器 tab 打开在 `https://chat.inceptionlabs.ai`（必要时 `minis-browser-use navigate`）。
2. 用 `minis-browser-use execute_js --script "$(cat /var/minis/skills/mercury-web-bridge/scripts/bridge.js)"` 执行桥接 JS。
   - 需要把消息写进 JS：修改 `bridge.js` 里的 `payload` 变量，或参考 `bridge_server.py` 的 `build_bridge_js()` 动态生成。
3. 解析返回的 `data.text`（JSON：`{ok,status,reasoning,answer}`），把 `answer` 返回给用户。

### 方式 B：本地 OpenAI 兼容桥接服务（可编程调用）
1. 启动服务：`python3 -u /var/minis/skills/mercury-web-bridge/scripts/bridge_server.py 18080 > /tmp/mercury_bridge.log 2>&1 &`
2. 调用：
   ```bash
   curl -s -X POST http://127.0.0.1:18080/v1/chat/completions \
     -H 'Content-Type: application/json' \
     -d '{"model":"mercury-3","reasoning_effort":"low","messages":[{"role":"user","content":"你好"}]}'
   ```
   返回标准 OpenAI `chat.completion` JSON，`choices[0].message.content` 即回答。
3. 支持多轮对话（messages 里带历史即可）、`reasoning_effort` 四档、`web_search`。
4. 服务假设浏览器 tab 已在 chat.inceptionlabs.ai；`ensure_chat_page()` 会自动导航。

## 注意事项
- **依赖内置浏览器 tab 保持打开**在 chat.inceptionlabs.ai；Minis 重启后需重新导航一次（会自动过挑战）。
- 网页版免费额度有匿名限流，个人使用没问题，批量滥用可能被封 IP。
- 网页版可能有 ToS 限制自动化调用，仅限个人自用。
- 若浏览器 tab 被占用/关闭，`execute_js` 会失败，先 `navigate` 到 chat.inceptionlabs.ai。
- `execute_js` 返回的 `data.text` 末尾可能混入 `tab_id: 0`，解析 JSON 时用 `json.JSONDecoder().raw_decode()` 忽略尾部。

## Minis 自定义 provider 接入（已实测）
把桥接服务配置成 Minis 的一个模型 provider，让 Minis 的 Agent Loop 直接路由到 Mercury 3，不经过 agent 中转、不消耗 Minis 自家模型额度。

前置：桥接服务已运行在 `http://127.0.0.1:18080/v1`，且 Minis 主进程能访问 iSH 的 localhost（实测内置浏览器能打开 `http://127.0.0.1:18080/`）。

配置命令（均触发用户确认，用 minis-config）：
1. 添加 provider：
   ```bash
   cat > /tmp/p.json <<'EOF'
   {"customBaseURL":"http://127.0.0.1:18080/v1","providerType":"openAI",
    "imageEndpointMode":"auto","isEnabled":true,"label":"Mercury Bridge (网页版免费)",
    "hasVoiceModels":false,"credentialType":"apiKey","appendV1Suffix":false}
   EOF
   minis-config add providers --file /tmp/p.json
   ```
2. 设置占位 API Key（bridge_server 不校验）：
   `minis-config set providers.<UUID>.apiKey "bridge-noauth"`
3. 手动添加模型（models 需要 instance_id）：
   ```bash
   cat > /tmp/m.json <<'EOF'
   {"model_id":"mercury-3","provider_id":"<UUID>","instance_id":"<UUID>",
    "display_name":"Mercury 3 (网页版免费)","provider_label":"Mercury Bridge (网页版免费)",
    "provider_type":"openAI","is_custom":true}
   EOF
   minis-config add models --file /tmp/m.json
   ```
4. 新建模型组（add groups 的 entries 不保存，需单独 append entry_id）：
   - `minis-config add groups '{"name":"Mercury (网页版桥接)","strategy":"fallback","fallback_strategy":"limited"}'`
   - `minis-config set groups.<组ID>.entries.append "<UUID>/mercury-3"`
5. **必须重启 Minis**：模型列表是运行时缓存的，不重启 `minis-model-use` 搜不到新模型。
6. 验证：`minis-model-use run --model "Mercury Bridge (网页版免费)/mercury-3" --prompt "你好"`。

## 作为子代理使用（推荐）
把 Mercury 3 配成子代理，让 Minis 的 agent 能委派「纯分析/写代码」任务给它，且 token 计入 Minis 用量统计。

1. 创建自定义子代理（minis-config，触发确认）：
   ```bash
   minis-config add subagents '{"name":"Mercury 分析助手",
     "description":"使用 Mercury 3 进行纯分析/写作/代码生成，不执行工具",
     "instructions":"你是基于 Mercury 3 的子代理，擅长分析/写作/代码生成。不要调用任何工具，直接根据任务简报中的材料输出高质量结果。用简体中文，先结论后依据。",
     "model_group":"Mercury (网页版桥接)"}'
   ```
2. 父代理用 `subagent_task` 委派，`agent` 参数传子代理 name（如「Mercury 分析助手」）。实测成功用 Mercury 3 生成代码。
3. **需要工具的任务**：父代理（U2 flash）先用 shell 等工具获取材料（读配置/跑命令），再把材料+分析要求写进 task，委派给 Mercury 子代理做分析/写代码。
4. 子代理走 Minis 模型通道，Mercury 3 的 token 会出现在 Minis「用量」面板（按模型能看到「Mercury 3 (网页版免费)」的消耗）。
5. **边界**：Mercury 3 桥接不支持工具调用，子代理自己不能跑命令；材料必须由父代理先取好。

## 实战踩坑记录（2026-10-22，均已修复）
1. **Vercel Security Checkpoint**：curl / Surge `$httpClient` / 服务器转发一律 429；只有真实浏览器能过 JS 挑战。Minis 内置浏览器是唯一过挑战的客户端。
2. **`list_tabs` 输出是 JSON**：URL 里的 `\/` 和 `\n` 是转义。必须先 `json.loads` 取 `data.text` 再正则匹配 tab，否则 `[^\n]*` 会吞掉转义的 `\n` 误匹配到错误 tab。
3. **`execute_js` 返回的 `data.text` 末尾混入 `tab_id: N`**：解析用 `json.JSONDecoder().raw_decode()` 忽略尾部。
4. **iSH `ARG_MAX` = 128KB**：`minis-browser-use execute_js --script "$(cat js)"` 把完整 JS 当命令行参数，Minis 传入的整段历史会让 JS 超限报 `Argument list too long`。修复：`build_bridge_js` 智能截断（消息数 15→1、每条 8000→200 字符逐步压缩到 JS ≤ 90KB）。
5. **developer/tool 角色导致网页版 API 500**：网页版只认 `user`/`assistant`。修复：非 user/assistant 角色统一映射为 user。
6. **Minis agent loop 用流式调用**：bridge_server 必须支持 OpenAI 兼容 SSE（`_send_stream`），且发送 `data: [DONE]` 后必须 `close_connection=True` 关闭连接，否则客户端 readline 卡死、触发模型组 fallback 自动切回 U2 flash。
7. **浏览器 fetch 本地 http 被 mixed content 阻止**：https 页面里 `fetch('http://127.0.0.1:18080/')` 报 `TypeError: Load failed`。无法用「HTTP body 传消息给浏览器」绕开 ARG_MAX，只能截断。
8. **Surge 模块做不了这个反代**：Surge 过不了 Vercel 挑战（429）、不能当 HTTP 服务器、也访问不到 iSH 的 localhost。Surge 最多做一个可选网络加速规则（`Mercury-Web-Accel.sgmodule`），非必需。
9. **小浣熊思路（workbuddy2api-panel 式独立 HTTP 网关）不适用**：那种方式上游没有 Vercel 挑战所以能纯 HTTP 反代；Inception 网页版有挑战，必须依赖真实浏览器执行层。

## Token 统计
- 网页免费版接口**不返回 `usage` 字段**，拿不到精确 token 数。
- 需要看消耗时只能**估算**：`token ≈ ceil(字符数 / 4)`（英文约 4 字符/token，中文通常更高）。
- 想精确统计必须走官方 API（注册 platform.inceptionlabs.ai，响应带 `usage`）。
- 可在 bridge_server 的 `Handler` 里加一行：`estimated = math.ceil(len(answer) / 4)` 打印到 stderr 日志。

## 文件
- `scripts/bridge.js` —— 单次桥接 JS（硬编码 payload，简单测试用）
- `scripts/bridge_server.py` —— 本地 OpenAI 兼容 HTTP 服务（推荐，支持流式/多轮/角色映射/智能截断）
- `scripts/start_bridge.sh` —— 一键启动桥接服务
- 开发副本：`/var/minis/workspace/mercury-test/`

## 参考资料
- 网页版：https://chat.inceptionlabs.ai/
- 官方文档：https://docs.inceptionlabs.ai/llms-full.txt
- 调研日期：2026-10-22