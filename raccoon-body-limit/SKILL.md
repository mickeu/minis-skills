# 小浣熊请求体限制（1MB）排查与精简

## 触发词
小浣熊报错、-1005、网络连接已中断、413、请求体过大、精简对话、小浣熊模型用不了、小浣熊限流、小浣熊断连

## 背景与根因
用户通过「小浣熊 OpenAI 反代（多账号轮询）」模块在 Minis 里使用小浣熊模型时，偶发 `NSURLErrorDomain -1005 网络连接已中断`（目标 `https://xiaohuanxiong.com/v1/chat/completions`）。

**根因（2026-10-23 抓包实锤）**：不是限流、不是免费版限制、不是多账号轮询、不是登录态失效。而是 Minis 的 agent 循环调用模型时带上**完整系统提示 + GLOBAL.md + 工具定义 + 对话历史**，请求体高达 **~1.4MB**，小浣熊上游网关（火山云 WAF `volcwaf.com` + litellm）对超大请求体**直接断连**（不返回任何 HTTP 状态），客户端最终报 `-1005`。简短请求（几百字节）完全正常。

## 判断方法
1. **别用 iSH 里 curl 直测**——会因 Surge fake-ip + MITM 证书不受信任返回 HTTP 000/self-signed 假象，不代表真实断网。要用 `surge-cli http probe` 或 Surge evaluate 脚本里的 `$httpClient`。
2. **抓包定位**：用 `/var/minis/skills/surge-ios/scripts/surge-dump.py` 抓 `xiaohuanxiong` 请求。特征：失败请求 `content-length` 巨大（>1MB）、Status 卡在 **Active**、Response Header 为空；正常请求 `content-length` 很小（几百字节）且 HTTP 200。
3. **上游连通性自检**：`surge-cli script evaluate /var/minis/workspace/raccoon-diag.js generic 90`（非流式）、`raccoon-stream-diag.js`（流式 SSE）、`raccoon-health.js`（多账号 token 体检）。全部正常则确认是请求体大小问题。

## 解决方案
### 已做修复（mickeu/surge commit 182df34）
- `Scripts/raccoon-openai-multi.js` 的 `chat/completions` 分支加了 **1MB 请求体保护**：读取 `Content-Length`/body 长度，超 1MB 返回 `errResp(413, "请求体过大…")`，不再默默断连。
- `RaccoonOpenAI-Multi.sgmodule` 脚本 URL `?v=6 → ?v=7`（强制刷新 Surge 缓存）。
- **用户需在 Surge App 重装/更新「Xiaoxiong OpenAI 反代（多账号轮询）」模块**才能拉到 v7 新脚本。

### 用户侧精简方法（核心）
1. **用小浣熊时开新会话**——清空历史，请求体最小。
2. **只做简短问答**（翻译、改写、简单总结），不跑需要反复调用工具的多步 agent 任务。
3. **复杂/长任务换其他模型**：云知声（GLM-5.3/DeepSeek V4/Mimo）、strrx1 日日新、自建中转 kcne。
4. **避免整段塞长文**，单次请求控制在几十万字符以内；长文先让模型读摘要或分段处理。
5. 对话一长就新开会话，别在旧会话一直聊。

口诀：**简短用浣熊，长任务换模型。**

## 可复用工具（workspace）
- `/var/minis/workspace/raccoon-diag.js`：非流式上游诊断
- `/var/minis/workspace/raccoon-stream-diag.js`：流式 SSE 透传诊断
- `/var/minis/workspace/raccoon-health.js`：多账号 token 批量体检
- `/var/minis/skills/surge-ios/scripts/surge-dump.py`：抓包（capture on/off、list --keyword、show <id>）
- 精简指南全文：`/var/minis/workspace/小浣熊精简请求体指南.md`

## 参考资料（来源）
- 抓包实测（2026-10-23）：失败请求 `content-length: 1426081`（~1.4MB）卡 Active；成功请求 `content-length: 494` HTTP 200
- 修复推送：mickeu/surge commit `182df34`（v7）
- 上游模块：LinkPass888/Surge `小浣熊OpenAI反代.sgmodule` → `js/raccoon-openai.js`
- 本技能创建日期：2026-10-23