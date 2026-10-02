# 发给 Muse 的远程 MCP 部署提示词

将下面提示词发给你自己的 Muse 智能体。它应先探测权限，再按环境选择方案，不能照搬别人域名或密钥。

---

请在我的 Muse 云电脑上部署一个供 Minis 使用的远程 MCP 服务。

## 目标

让 iPhone 上的 Minis 把下载、转码、Python、爬虫和长任务交给这台云电脑执行。长任务在 Minis 退出后仍能继续，并支持状态查询、取消和结果回收。

## 协议和公网入口

- 使用 MCP Streamable HTTP；
- 服务监听本机回环地址和独立端口；
- 通过当前环境可用的固定公网隧道或反向代理暴露 `/mcp`；
- 必须使用 Bearer Token 鉴权；
- 优先固定域名；若只能临时 URL，要明确说明会轮换；
- 配置开机自启和定期健康检查。

## 工具

至少提供：

- run_shell、run_python
- read_file、write_file、list_dir
- download_file
- run_shell_async、run_python_async、download_file_async
- task_status、task_cancel

推荐提供 web_search、fetch_page。

## 安全和执行契约

- 工作目录限制在专用 workspace；
- 路径穿越、危险删除和明显破坏性命令必须阻止；
- token 存 600 权限文件，不写入日志；
- 同步工具最坏返回时间必须低于 60 秒，预计超过 50 秒的任务必须走异步；
- 异步提交立即返回 task_id；
- task_status 返回 running/done/failed/cancelled/unknown 和完整结果；
- task_cancel 必须终止整个进程组，不留孤儿进程；
- 服务重启时不盲目接管或重跑状态不明的任务；
- 审计只记录工具名、时间、成功失败和必要摘要，不记录密钥或敏感正文。

## 交付

完成后给我：

1. 固定 MCP URL；
2. 一次性 Bearer Token；
3. 工具列表与参数；
4. systemd/守护和巡检状态；
5. Minis 配置示例，token 使用 `$$MUSE_MCP_TOKEN` 引用；
6. 实测证据：initialize、tools/list、run_shell、文件写读、异步 submit → status → done、cancel。

不要代我登录其他私人账号，不要把任何凭据写在代码或日志里。

---
