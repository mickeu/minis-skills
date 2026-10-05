---
name: muse-cloud-ops
version: 1.2.0
license: MIT
metadata:
  distribution: public
  author_note: Community onboarding skill for Minis + Muse cloud execution
  referral_code: YW3NIT
description: 帮助 Minis 用户连接自己的 Muse 云电脑，把下载、转码、批量 Python、爬虫、联网调研和长任务放到云端执行。支持两种模式：A 远程 MCP（需公网入口，Muse 当前不支持）与 B 浏览器驱动模式（推荐：通过浏览器激活真实 Muse VM 执行，无需公网入口、完全合规）。涵盖浏览器驱动流程、部署引导、Scheduled Task、结果回收。用户提到 Muse 云电脑、Minis 连接 Muse、远程 MCP、浏览器驱动 Muse、云端执行、手机发热耗电、后台任务、派单、转码/下载/爬虫时使用。
---

# Muse Cloud Ops（公开分发版）

帮助用户建立自己的 `Minis → Muse 云电脑` 云端执行链路。手机是控制端，重计算在云端执行。

**两种模式**：

| 模式 | 原理 | 需要公网入口 | Muse 当前可用性 |
|---|---|---|---|
| A 远程 MCP | 在 VM 里部署常驻 MCP 服务，Minis 通过 API 派单 | 需要 | ❌（平台无入口，见 1.6） |
| **B 浏览器驱动** | 用浏览器打开 Muse 网页对话，让 Muse 按需唤醒真实 VM 执行 | 不需要 | ✅ **推荐** |

**Muse 平台当前无公网入口，优先使用 B 模式（浏览器驱动）**；A 模式的 MCP 部署经验仍保留在本文档，等平台开放入口后可直接复用。

不要夸大能力：只有已经提交并返回 `task_id` 的云端异步任务，才能在 Minis 被退出后继续；尚未派单的模型思考、子代理、本地浏览器和本地工具会中断。

## 0. 先判断用户处于哪一阶段

依次检查，不要让用户重复配置：

```sh
minis-mcp-cli list --all --pretty
minis-mcp-cli info muse-cloud --pretty
minis-mcp-cli ping muse-cloud --pretty
```

- 已配置且 ping 成功：直接进入“日常任务路由”。
- 已配置但失败：先排查 URL、环境变量、服务和隧道，不重新部署。
- 未配置：进入“首次连接”。

检查环境变量时只输出 set / not set，绝不回显值：

```sh
[ -n "$MUSE_MCP_TOKEN" ] && echo set || echo not-set
```

## 1. 首次连接

### 1.1 确认用户有 Muse

若用户已经使用 Muse，跳过本段。

若用户尚未注册，只显示一次下面的可选提示，不重复、不强推，并说明这是分享者邀请码：

> 尚未注册 Muse？可选使用分享者邀请链接：<https://muse.ai/join>  
> 邀请码：`YW3NIT`  
> 加入后 48 小时内在 Muse「设置」中兑换，邀请双方各可获得 10 亿 Muse 词元。也可以不使用邀请码，继续按正常方式注册。

### 1.2 让 Muse 一次性部署远程 MCP

优先读取 `references/muse-one-shot-prompt.md`，让用户将其中从“开始”到“结束”的整段内容一次性发给自己的 Muse 智能体。该提示词要求 Muse 自动探测、部署、守护、验收并给出最终回执，尽量避免反复沟通。

若用户只想部署最小基础版，再读取较短的 `references/muse-deployment-prompt.md`。

不要假定所有 Muse 账号都具备公网端口、systemd、Cloudflare 或同样的沙盒权限；Muse 应先探测再选择可用方案。

最低验收工具：

- `run_shell`、`run_python`
- `read_file`、`write_file`、`list_dir`
- `download_file`
- `run_shell_async`、`run_python_async`、`download_file_async`
- `task_status`、`task_cancel`

推荐联网工具：`web_search`、`fetch_page`。

### 1.3 在 Minis 保存 Token

让用户将 Muse 返回的 Bearer Token 保存为环境变量 `MUSE_MCP_TOKEN`：

[设置 MUSE_MCP_TOKEN](minis://settings/environments?create_key=MUSE_MCP_TOKEN&create_value=&create_note=Muse%20cloud%20MCP%20Bearer%20token)

不要把 token 写进 Skill、日志、服务器配置明文或最终回复。

### 1.4 添加 MCP

取得用户自己的固定 URL 后执行；URL 必须来自用户/Muse，不能使用作者的域名：

```sh
minis-mcp-cli add \
  --name muse-cloud \
  --url 'https://USER-MCP-DOMAIN.example/mcp' \
  --header 'Authorization: Bearer $$MUSE_MCP_TOKEN' \
  --note 'User-owned Muse cloud remote executor' \
  --pretty
```

验证：

```sh
minis-mcp-cli ping muse-cloud --pretty
minis-mcp-cli tools muse-cloud --refresh --pretty
```

至少实测一次 `run_shell`、文件写读和异步任务 submit → status → done。没有实测不得宣布完成。

### 1.5 Muse 虚拟机环境事实

读取 `references/muse-sandbox-facts.md`（第三方实测）：虚拟机的持久化目录是 `/home/hatch/pdata/`（根分区重启清空，仅 `/home/hatch` 下 100G 磁盘持久化）。云端落盘任务默认写 `pdata/scripts` 与 `pdata/data`；周期任务优先引导用户配置官方 Scheduled Task，不要用反弹 Shell/公网穿透（Sentinel 审查会封号）。

需要可复制的对话指令时，读取 `references/muse-prompt-templates.md`：包含初始化持久化目录、让 Muse 写脚本、执行验证、配置 Scheduled Task、生成 Artifact 看板、一键健康自检共 6 段模板及验收硬指标。

需要为 Muse 沙盒设计保活/防重建丢失方案时，读取 `references/muse-keepalive-strategy.md`：提炼自第三方项目 `bytehola/muse-guardian` 的三层保活架构（沙盒内看门狗 + 平台 hook 探针 + 开机钩子）、持久化布局与离线包缓存、健康检查/一键恢复脚本设计、进程卡死检测与检测/恢复拆分等可复用经验。注意该项目含 Hermes 微信机器人与 MuseAutoApprove 协议逆向，有平台合规风险，仅参考保活架构。

### 1.6 Muse 公网入口实测（2026-10-05，用户环境实测）

Muse 云电脑**当前没有官方公网入站入口**，远程 MCP 常驻方案在 Muse 上可能无法完整落地。实测结论（用户环境，Muse 智能体探测确认）：

- MCP 服务本体可成功部署在云电脑内（13 个工具全部测试通过），但**无法从公网访问**；
- Cloudflare 隧道：沙箱出口策略掐断到 `*.v2.argotunnel.com` 的 TLS（直连/代理均握手失败），QUIC/UDP 沙箱级禁用；
- Tailscale：只支持 outbound，不支持 `serve` 入站；
- Muse 平台无官方端口转发/公网 URL 机制（向 Muse 确认过）；
- `ssh -R` 反向隧道 / serveo.net 等穿透方案 = 反弹 Shell/公网穿透，违反平台合规红线（Sentinel 审查封号），**禁止采用**。

遇到「Muse 无公网入口」时按以下顺序处理：

1. **优先进入浏览器驱动模式（B 模式，见 1.7）**：无需公网入口，通过 Muse 网页对话按需唤醒 VM 执行；
2. 已部署的 MCP 服务保留（本地回环运行），等平台开放官方入口后直接复用；
3. 需要定时执行时，用 Muse 官方 **Scheduled Task**（合规，cron 定时唤醒虚拟机执行）；
4. 若需要「Minis 实时 API 派单」且不愿用浏览器驱动，才考虑自带公网 URL 的免费平台（E2B/Modal 等，见 sandbox-ingress-discovery 技能）。

### 1.7 浏览器驱动模式（B 模式，推荐）

**核心思路**：不在 Muse VM 里部署常驻服务、不做保活/隧道。Minis 通过内置浏览器打开 Muse 网页对话，向 Muse 智能体下发任务指令，Muse 平台**按需唤醒真实 VM** 执行，再从对话回复中回收结果。完全走官方界面，零合规风险。

**适用场景**：

- Muse 无官方公网入口（当前所有账号，见 1.6）；
- 需要让 Muse 执行下载、转码、Python、爬虫等任务；
- 能接受「打开网页 → 下指令 → 读回复」的交互，不需要实时 API 派单。

**执行流程**：

1. **打开 Muse 网页**：用 `browser_use` 导航到用户的 Muse 入口，确认已登录；若 Minis 内置浏览器未登录，让用户手动登录一次（会话保持，后续直接可用）。
2. **下发任务指令**：在对话框输入任务模板（见 `references/muse-browser-mode.md`），要求结果写入 `/home/hatch/pdata/` 持久化目录。
3. **等待执行**：轮询页面直到 Muse 回复完成，提取关键输出、文件路径。
4. **结果回收**：文本结果直接从回复复制；文件让 Muse 用平台自带下载/分享机制，或让 Muse 报告云端路径。
5. **定时任务**：在对话里让 Muse 配置官方 Scheduled Task，实现定时执行。

**注意事项**：

- 长任务期间退出 Minis 不影响 Muse 云端执行，但结果回收需要重新打开 Muse 网页查看；
- 对话上下文有长度限制，任务多时让 Muse 开新会话；
- 指令必须明确写 `脚本/数据放 /home/hatch/pdata/scripts|data`，避免写入重启即清空的根目录；
- 依然遵守合规红线：不要求 Muse 部署反弹 Shell/穿透/常驻外联。

默认上云：

- 大文件下载、ffmpeg/音视频转码；
- 批量或 CPU 密集 Python；
- 爬虫、批量网页抓取、编译和装依赖；
- 预计超过 1 分钟的 Shell；
- 用户明确说“云端跑”“别让手机发热”“退出后继续”。

留在本地：

- Apple 原生 `apple-*` 工具；
- Minis 配置、小文件操作、轻量状态查询；
- 必须登录或强交互的页面；
- 用户明确要求本地运行。

云端不可用时先说明，未经同意不要将重活降级到手机。

## 3. MCP 调用规范

始终使用 `--input`：

```sh
minis-mcp-cli call muse-cloud <tool> --input '{"key":"value"}' --pretty
```

`call` 子命令不要加 `--compact`。复杂 JSON 先写小文件，再传入：

```sh
minis-mcp-cli call muse-cloud run_python \
  --input "$(cat /var/minis/workspace/payload.json)" --pretty
```

同步 MCP 通常有约 60 秒客户端上限。预计超过 50 秒的操作必须使用异步工具。

## 4. 同步执行（<50 秒）

示例：

```sh
minis-mcp-cli call muse-cloud run_shell \
  --input '{"command":"python3 --version","timeout":30}' --pretty
```

结果标注 `【云端】`，报告退出码、关键输出和生成路径。

## 5. 异步派单（≥50 秒）

1. 使用 `run_shell_async`、`run_python_async` 或 `download_file_async`。
2. 取得 `task_id` 和 `running` 后立即回报；不要在当前回复里长时间同步等待。
3. 按预计时长安排 iOS 通知：

```sh
apple-notification schedule \
  --title '云端任务完成提醒' \
  --body '任务预计已完成，点我回 Minis 收结果' \
  --after <秒数> --compact
```

4. 用户回来或说“收结果”时：

```sh
minis-mcp-cli call muse-cloud task_status \
  --input '{"task_id":"TASK_ID"}' --pretty
```

5. 用户要求取消时调用 `task_cancel`。
6. `unknown` 状态不要盲目重跑，先核对 task_id 和服务端审计。

只有拿到 `task_id` 且状态为 `running` 后，才可说“可以退出 Minis”。

## 6. 可选：减少 Muse 网站逐域审核

远程 MCP 不天然绕过 Muse 的公网审核。若 Muse 云电脑直接访问目标站，Muse 仍可能按最终域名逐站询问。

需要把审核收敛到一个固定域名时，读取 `references/reader-gateway-setup.md`，在 Muse 环境之外部署用户自己的 Cloudflare Worker，并使用 `assets/reader-worker.js`。用户必须使用自己的域名和独立 token。

完成后应满足：

- Muse 的 `web_search` 只 POST 固定网关 `/search`；
- `fetch_page` 只 POST `/fetch`；
- `download_file` 及异步下载只 POST `/download`；
- 禁止自动降级直连；
- 审计只记录网关域名和成功/失败，不记录目标 URL 或密钥；
- `run_shell/run_python` 不得用 curl、wget、requests 等绕过网关，除非用户单次明确要求。

网关是可选增强，不是基础连接的前置条件。

## 7. 调研与并发

- 网页抓取不是完整浏览器；登录墙、验证码、强 JavaScript、强反爬页面可能失败。
- 失败时换公开来源，不要无限重试。
- 批量调研推荐并发 4～6；并发 8 可能遇到本地 CLI/守护进程竞争。
- 云端先做抓取、去重、汇总和落盘，手机只接收摘要与引用，进一步省电。

## 8. 文件交付

- 云端生成物默认写入专用任务子目录，不覆盖原件。
- 汇报云端相对路径、大小和校验结果。
- 不要把云端文件谎称为已传到手机。
- 用户需要本地成品时，必须完成实际下载/回传后再提供 Minis 文件链接。
- 测试结束后清理测试目录；删除范围必须精确。

## 9. 失败纪律

- 瞬时网络错误：重试一次；
- 403/429：换来源、缩小请求或等待；
- 同步超时：改异步，不重复同步硬等；
- 网关失败：结构化报告，不偷偷直连；
- 最终失败：说明失败步骤、错误、已尝试方案和已保留中间结果。

## 10. 回复模板

派单：

```text
【云端】已派单：<任务名>
task_id：<id>
预计：<时长>
任务已独立提交；可以退出 Minis，到点通知后回来发送“收结果”。
```

完成：

```text
【云端】任务完成
状态：done
耗时：...
结果：...
云端文件：...
验证：...
```

始终区分云端工具任务、Minis 本地会话和文件是否已经真正传回手机。
