# 固定单域名 Reader 网关（可选）

## 何时需要

Muse 云电脑若按最终公网目标域名逐站审核，即使通过 MCP 仍会弹窗。解决办法不是关闭审核，而是把目标抓取移到 Muse 之外：

```text
Muse MCP → 用户自己的固定 Worker 域名 → 目标网站
```

Muse 只看见一个固定域名。此功能可选；没有审核困扰时不要增加复杂度。

## Cloudflare Worker

1. 在 Cloudflare Workers 创建 Worker。
2. 使用 `../assets/reader-worker.js` 作为代码。
3. 设置 Secret：`GATEWAY_TOKEN`，使用随机 32 字节以上密钥。
4. 绑定用户自己的固定域名，例如 `reader.example.com`。
5. 不要使用 Skill 作者或其他人的域名/token。

Worker 接口：

- `POST /search`：`{"query":"...","count":10}`
- `POST /fetch`：`{"url":"https://..."}`
- `POST /download`：`{"url":"https://..."}`，返回文件流
- Header：`Authorization: Bearer <GATEWAY_TOKEN>`

## 修改 Muse MCP

让 Muse 服务端：

- 从 600 权限文件读取 `READER_GATEWAY_TOKEN` 并注入 systemd；
- web_search/fetch_page/download_file 只调用固定网关；
- 网关失败时明确返回错误，不直连、不调用内置浏览器；
- 异步下载也经过 `/download`；
- 审计只记录 `gateway <固定域名>/<path> ok=True|False`；
- AGENTS.md 禁止智能体通过 shell/python 绕过网关联网，用户单次明确要求除外。

## 验收顺序

1. 未带 token 请求应返回 401。
2. 从非 Muse 侧测试一次 search、fetch、download。
3. Muse 侧各测试一次；观察审核只出现固定网关域名。
4. 再测试两个不同目标网站；不得出现目标域名审核。
5. 检查审计无目标 URL、搜索引擎域名和 token。
6. 推荐并发 4～6 做小型压力测试。

## 限制

- Worker HTTP 抓取不是完整浏览器；
- 免费搜索源可能不稳定或质量有限；
- 大文件受 Worker/上游连接限制；
- Worker、域名和 Secret 由每位用户自行维护；
- 不承诺绕过网站的登录、验证码、付费墙或反爬措施。
