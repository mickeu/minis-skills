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

## 文件
- `scripts/bridge.js` —— 单次桥接 JS（硬编码 payload，简单测试用）
- `scripts/bridge_server.py` —— 本地 OpenAI 兼容 HTTP 服务（推荐）
- 开发副本：`/var/minis/workspace/mercury-test/`

## 参考资料
- 网页版：https://chat.inceptionlabs.ai/
- 官方文档：https://docs.inceptionlabs.ai/llms-full.txt
- 调研日期：2026-10-22