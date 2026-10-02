# 一次性发给 Muse 的完整提示词

将下方从“开始”到“结束”整段复制给自己的 Muse 智能体。无需预先修改；Muse 应先探测环境并完成能自动完成的全部步骤，只把确实需要用户提供的域名、平台授权或外部网关值列为待办。

--- 开始 ---

请为我一次性部署并验收一套供 iPhone Minis 使用的“云端执行 MCP”。目标是：Minis 只负责下达任务和收结果，下载、转码、Python、爬虫、编译和长任务在这台 Muse 云电脑执行；长任务提交成功后，即使退出 Minis 也能继续。

请直接执行，不要只给教程。先探测当前权限、系统、端口、公网入口、systemd/等效守护能力和现有服务；复用安全且可用的已有组件，不破坏其他项目。只有涉及外部账号登录、购买、域名授权或无法推断的值时才向我提问。

## A. 部署远程 MCP

1. 使用 MCP Streamable HTTP，提供 `/mcp` 和轻量 `/health`。
2. 服务只监听回环地址或受控内网端口，通过当前环境可用的固定 HTTPS 域名、隧道或反向代理暴露；优先固定地址。若当前只能临时 URL，明确说明轮换限制，并把更换固定入口列为待办。
3. 使用独立高强度 Bearer Token。Token 只在最终回执中显示一次；服务器保存为权限 600 的文件或 Secret，禁止写入代码、普通日志、审计和 shell 历史。
4. 工作目录限定在专用 workspace。阻止路径穿越、任意私网探测、危险递归删除和明显破坏性命令。
5. 配置开机自启、崩溃重启和每 15 分钟健康检查；脚本必须幂等，不重复生成 token、不覆盖用户文件。

## B. 工具清单

必须实现并注册：

- `run_shell(command, timeout)`
- `run_python(script, timeout)`
- `read_file(path, max_bytes)`
- `write_file(path, content, mode)`
- `list_dir(path)`
- `download_file(url, dest, max_bytes)`
- `run_shell_async(command, timeout)`
- `run_python_async(script, timeout)`
- `download_file_async(url, dest, max_bytes)`
- `task_status(task_id)`
- `task_cancel(task_id)`

可选联网工具：

- `web_search(query, count)`
- `fetch_page(url, max_chars)`

## C. 60 秒同步契约与异步任务

1. Minis 客户端的单次 MCP 请求可能在约 60 秒被终止。所有同步工具必须在 50 秒内成功或结构化失败，不能拖满 60 秒。
2. 预计超过 50 秒的任务必须使用异步工具；异步提交应在数秒内返回随机 `task_id` 和 `running`。
3. `task_status` 返回 `running/done/failed/cancelled/unknown`；完成时包含 stdout、stderr、exit_code、timed_out 或文件路径/大小。
4. `task_cancel` 必须终止整个进程组，约 1 秒内生效且不留孤儿进程。
5. 服务重启后，对提交中或运行中但无法确认的旧任务标记 `unknown`，禁止自动重跑，避免重复下载、计算或写入。
6. 任务元数据和结果文件权限至少为 600，并设置合理清理周期。

## D. 公网搜索、抓取和下载

先判断 Muse 环境是否会按最终目标域名触发逐站审核：

- 如果没有外部固定网关：基础 MCP 可以先完成；明确提示直接公网访问可能触发逐域审核。不要谎称“走 MCP 就零弹窗”。
- 如果系统中已经配置 `READER_GATEWAY_URL` 与 `READER_GATEWAY_TOKEN`：
  - `web_search` 只 POST `${READER_GATEWAY_URL}/search`
  - `fetch_page` 只 POST `${READER_GATEWAY_URL}/fetch`
  - 同步和异步下载只 POST `${READER_GATEWAY_URL}/download`
  - 网关 Token 从 600 权限文件/环境变量读取；失败时结构化报错，不直连、不调用 Muse 内置浏览器。
  - 审计只记录网关主机、路径和成功失败，不记录目标 URL、搜索词、正文或 token。
  - 禁止智能体借 `run_shell/run_python` 使用 curl、wget、requests、urlopen 绕过网关，除非我在某一次任务中明确要求。
- 如果没有 Reader 网关，请在最终回执说明：可以使用 Skill 附带的 Cloudflare Worker 模板稍后启用，不要擅自登录我的 Cloudflare 或索取 Google 会话。

## E. 审计与失败行为

1. 审计记录：时间、工具、状态、耗时和必要的非敏感摘要。
2. 不记录 token、完整命令中的秘密、目标 URL、网页正文或用户文件内容。
3. 瞬时网络错误最多自动重试一次；403/429 快速返回，不无限重试。
4. 最终失败必须明确说明失败步骤、错误和已尝试方案，不静默结束。
5. 不安装来源不明或无许可的服务；新增依赖和配置应可审计、可回滚。

## F. Minis 配置交付

完成后给我以下内容：

1. 固定 MCP URL（含 `/mcp`）；
2. Bearer Token（仅这一次）；
3. 推荐环境变量名：`MUSE_MCP_TOKEN`；
4. Minis 配置命令，必须使用环境变量引用，不把 token 写死：

```sh
minis-mcp-cli add \
  --name muse-cloud \
  --url 'https://你的固定域名/mcp' \
  --header 'Authorization: Bearer $$MUSE_MCP_TOKEN' \
  --note 'User-owned Muse cloud remote executor' \
  --pretty
```

5. 工具列表和参数；
6. 工作目录、服务名、日志位置、健康检查和恢复方式；
7. 如果有尚未完成的外部步骤，给出最短待办清单，不要把已完成步骤重新交给我。

## G. 必须实际验收

按顺序执行并报告证据：

1. `/health`；
2. MCP initialize；
3. tools/list；
4. `run_shell`：输出主机名和 Python 版本；
5. write_file → read_file → list_dir；
6. 异步任务：提交一个约 20 秒任务，立即得到 task_id，先查 running，再查 done 和完整结果；
7. 取消测试：提交一个 60 秒任务，调用 task_cancel，确认约 1 秒内 cancelled，且没有孤儿进程；
8. 未带 Bearer Token 的请求必须返回 401；
9. 若已接 Reader 网关：只测试 1 次 search、1 次 fetch、1 次小文件 download；网络审计必须只出现固定网关域名，不得出现搜索引擎或目标域名。

测试文件完成后精确清理。不要删除无关文件。

## H. 最终回执格式

请用以下结构一次性回报：

- 状态：已完成 / 部分完成
- MCP URL
- 一次性 Token
- 工具数量与名称
- 服务与开机自启状态
- 工作目录
- 验收结果表
- Reader 网关状态：已启用 / 未启用及原因
- 仍需我完成的事项（没有则写“无”）
- 回滚方式

不要把“服务能启动”当作“全链路完成”；只有以上验收通过后才能宣布部署成功。

--- 结束 ---
