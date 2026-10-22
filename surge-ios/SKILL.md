---
name: surge-ios
description: 通过同机 Surge External Controller 检查和控制 Surge iOS，处理策略与节点、规则、DNS、连接、模块、脚本及代理诊断。涉及 Surge 专有命令或配置时使用；优先 Minis surge-cli，HTTP API 按需回退。
compatibility: Surge iOS with external-controller-access enabled; Python 3
metadata:
  upstream: Surge for macOS 6.11.0 (12570), bundled Skill synchronized and adapted for Minis
  controller_protocol: 27
  source: /Applications/Surge.app/Contents/Resources/Skills/surge/
---

# Surge for Minis

## 1. 确认入口与授权范围

使用 `/usr/local/bin/surge-cli`，默认连接 `127.0.0.1:6170`，优先 `--raw` 读取 JSON。

密码仅从 `--password-stdin`、`SURGE_CLI_PASSWORD` 或安全交互提示读取，不写入命令参数、文件、日志或回复。可用以下命令安全检查：

```sh
[ -n "$SURGE_CLI_PASSWORD" ] && echo set || echo missing
```

缺失时提供 [设置 SURGE_CLI_PASSWORD](minis://settings/environments?create_key=SURGE_CLI_PASSWORD&create_value=&create_note=Surge%20External%20Controller%20password)，不要让用户在聊天中发送密码。

## 2. 检查相关状态，防止误判 Suspend

实际依赖 Surge 联网、代理、DNS、脚本或 API 的任务，先检查当前实例；意外 EOF 或超时后重新检查，不沿用历史状态。纯文档阅读不需连接：

```sh
surge-cli --raw status
surge-cli --raw environment
```

- Controller/HTTP API 能响应，不等于引擎在正常处理流量。留意 Suspend、停止或引擎异常，但不假设每个版本都有同名暂停字段。
- 输出不足以确认时，标为未确认，请用户查看 Surge 界面的 Suspend 与 VPN/引擎状态；EOF/超时本身不能证明已暂停，也不能证明节点、凭据或目标服务故障。
- 不为排障擅自恢复、重启、换模式或换实例。授权恢复后重读状态，再重试原操作；仍失败再查路由、DNS、节点和目标服务。

## 3. 按任务查阅与操作

基础网络知识不代替 Surge 专有语义。不得照搬其他代理客户端的规则、代理参数或策略组语法；不确定时查对应官方正文，不猜字段、命令或版本能力。

| 任务 | 参考入口 |
|---|---|
| 命令、响应字段、环境 key-path | [command-reference.md](references/command-reference.md)，只读相关节 |
| Profile、模块、代理协议、策略组、DNS/MITM/脚本配置 | [manual-index.md](references/manual-index.md)，定位对应官方手册正文 |
| 路由解释、临时规则、DNS、性能、Tailscale/WireGuard | [diagnostics.md](references/diagnostics.md) |
| 临时 verbose、实时日志解析、Packet Capture 与 PCAP 导出边界 | [diagnostics.md](references/diagnostics.md#实时日志与临时-verbose) |
| 本地模块落盘、发现、HTTP API 启用与验证 | [http-api.md](references/http-api.md#本地模块安装与启用) |
| IP Rewrite / reflect、本机开发服务回环及反射抓包判读 | [ip-rewrite-loopback.md](references/ip-rewrite-loopback.md) |
| Controller 不可用、明确要求 `/v1/*`、指标或未配置节点测试 | [http-api.md](references/http-api.md) |
| 平台限制、Unknown command、协议版本异常 | [platform-compatibility.md](references/platform-compatibility.md) |
| 安装、认证传输和客户端协议 | [controller-cli.md](references/controller-cli.md) |

切换策略、模块或功能前确认目标存在，按需读取相关列表，不把全量 `dump policy`/日志/Profile 当每次任务的前置流程。只做最小授权变更，变更后重读相关状态；需要端到端证明时再做真实请求。

### 运行时操作不附加 reload

`reload` 不是 CLI/HTTP API 写操作后的通用"保存/提交"步骤。区分三类操作：

- **即时运行时操作**：如 `set-log-level`、`set` 环境 key-path、`feature set`、模式/策略选择、临时规则、抓包开关及 DNS flush。按各命令语义执行后重读相关状态；不要为了"确保生效"再追加 reload。即时生效不等于持久化，各字段的持久化与重载后保留行为须分别核实。
- **自身安排配置加载的操作**：如模块 enable/disable、Profile 切换。等待操作完成并复核，不重复 reload；这些操作本身也可能扰动正在进行的运行时诊断。
- **直接修改活动配置文件**：只有确需让文件变更生效且影响已获授权时才 reload；不能将文件修改流程照搬到运行时 API 操作。

运行时测试先记录原状态，只恢复本次改动；不拿 reload/restart 当清理或恢复原状的快捷方式。重载可能重新应用配置并改变临时状态，必要时还会自动升级为完整引擎重启，破坏连接、缓存或诊断现场；但不得反向宣称所有运行时字段都会被 reload 清空。确需重载时先结束/清理本次诊断，重载完成后重新核实并建立所需测试状态。

环境 key-path 的 null 值须保护 shell 引号，例如：

```sh
surge-cli --raw set 'AutoPolicyGroupOverride.Streaming=<nil>'
```

`<nil>` / `(null)` 的接口语义、ProxyMode 数值和组选择字段以命令参考为准；上例是写操作，不是检查命令。

## 4. 保留影响边界

- 临时 `set-log-level verbose` 应在模块/配置变更完成后设置；诊断期间不要 `reload`（会恢复配置中的等级），也不要切换模块触发重载。结束或失败时恢复原日志等级，不固定恢复成 `notify`。IP 层流量没有常规日志不能证明未处理，按诊断参考转 Packet Capture。
- `dump profile` 可能含节点、订阅和凭据；仅在确有必要时读取，进程内脱敏，不原样输出、记录或打包。
- `reload` 与 `restart-engine` 不等价：Protocol ≥24 的完整重启会关闭活动连接、清除缓存和临时规则，须明确授权这些影响；`stop` 会关闭 Surge，须用户明确要求。
- 临时规则立即生效、优先于 Profile 规则。`rule temp flush` 清空所有临时规则，不能用于默认清理本次测试；保留用户已有项。
- `http probe` 会发真实 HEAD 请求，DNS/节点/带宽测试也可能产生实际流量；仅按任务需要执行。加密 benchmark 是 Surge 所在设备的本地加密性能，不是网络带宽。
- `watch`、`diagnostics`、带宽和加密测试可能持续输出 JSON Lines，按对应 `hasMore=false` 或结束载荷处理，不能拿首帧当最终结果。
- Minis `--check <path>` / `-c <path>` 会把明确指定的 UTF-8 Profile 上传到 `https://services.nssurge.com/v1/config/validate`，不是 Mac 本地解析器。不得自动上传当前 Profile；先告知上传，含凭据/私有信息时使用脱敏副本并确认范围。
- HTTP 默认同机 `127.0.0.1:6171`，密钥仅从 `SURGE_HTTP_API_KEY` 获取；`metrics` 是受 X-Key 保护的 `/v1/metrics`。远端凭据传输与危险操作按 HTTP 参考执行。
- 未配置节点优先考虑 HTTP 参考中的 `policy-descriptor`，不必改/重载 Profile；描述符可能含密码/PSK，只从权限受限文件或 stdin 读取，不进参数、日志或回复。

## 5. 交付与维护

报告实际命中/状态、做了什么、相关验证与尚未确认之处。规则推演不冒充端到端联网成功；只有版本快照时不冒充当前版本实测。

上游更新与验收见 [SOURCE.md](references/SOURCE.md)：默认暂存并审阅差异，明确应用后才更新活动文件；不自动打包。`scripts/acceptance.sh` 默认离线；`--controller` 查询实例，`--network` 还上传合成无秘密 Profile 并发 DNS 请求，仅按变更需要执行。

按需加载参考，保留官方命令主体与本地适配层；不以缩短行数为目标删除专有知识。

**Surge 规则集改动 → 必须同步 MRS 到 Clash 仓库**（2026-10-04 用户要求）：自建规则集（Direct_Supplement/Proxy_Supplement/Advertising_Supplement/Gemini/Apple_All/Apple_Services/AppleIntelligence/Telegram_All/Video_RESOURCE 等）增删域名后，除 ChinaMax_All.list 外，必须用 `mihomo1190 convert-ruleset domain|ipcidr text <源> <目标.mrs>` 重新转换 MRS 并推送到 mickeu/Clash（覆写脚本通过同名 URL 自动跟随新版）。ChinaMax 例外：用 blackmatrix7 的 ChinaMax_Classical.yaml 拆分转换（domain + ipcidr 两个 MRS），不转换 Surge 版 list。Hako 需用户手动重新应用覆写脚本才生效。

## 6. 本机环境补充（Minis 实测沉淀）

以下为本机长期维护 Surge 沉淀的环境专属知识，上游文档未覆盖；本地完整实测坑位菜谱另见 [pitfalls-and-cookbook.md](references/pitfalls-and-cookbook.md)。

### 修改配置文件（nssurge 挂载目录）

Surge iOS 配置文件通过挂载目录暴露给 iSH：`/var/minis/mounts/nssurge/`（含 `.Default.conf` 等），当前生效配置用 `surge-cli profile current` 查看。工作流：

```sh
surge-cli profile current      # 1. 确认当前配置文件名
# 2. file_read/file_edit 编辑 /var/minis/mounts/nssurge/<当前配置>.conf
surge-cli reload                # 3. 改完必须 reload 才生效
surge-cli --raw status           # 4. 验证
```

- `surge-cli set <key-path>=<value>` 可单改配置项，立即生效；App 内置编辑器保存自动重载。
- reload 返回 `success` 即成功；失败读 stderr，多为语法/值错误。
- 改错回退：改回原内容再 reload，或 `surge-cli profile switch <name>` 切备份配置。

### 远程规则集维护（mickeu/surge）

**核心规则：所有能加进规则集文件的域名，一律加入对应规则集文件（如 `Gemini.list`、`Direct_Supplement.list`），不写死进 Rule.dconf。** Rule.dconf 只通过 `RULE-SET` 引用远程规则集。

- blackmatrix7 漏域名 → 拉下来补进同名规则集，Rule.dconf 引用切到 mickeu/surge 版本。
- 引用 URL 优先 GitHub raw（jsdelivr CDN 缓存可能滞后）。
- 包含密码/证书的配置文件（Proxy.dconf / mitm-ca.dconf / 主配置.conf）只能推 config-backup 私库。
- 验证：`surge-cli --raw rule match <domain>` 看是否命中对应规则集；加载状态看 `external-resource list` 的 ready 字段，不要用 `/v1/rules`。

**⚠️ 规则集缓存不对称（2026-09-19 实测）**：新建规则集文件（全新 URL）→ reload 后立即拉取生效；修改已有规则集文件（URL 不变）→ reload **不刷新缓存**，`ready=true` 但 `updatedAt` 不变，`?v=` 参数无效。不要只看 ready=true 判定生效，必须 `rule match` 验证实际命中的规则集 URL；唯一可靠刷新是 Surge App 内手动「更新外部资源」或等刷新周期。实务影响：往规则集补域名无法替代"删除 Rule.dconf 原生规则"——缓存刷新前会落到后面规则集走错策略。

### 网址不通的标准处理流程（端到端自动化）

用户反馈某网址打不开，**禁止只口头劝或用 `rule temp add` 糊弄**。走全套：
1. `surge-cli rule match <域名>` + `dns lookup` + `http probe` 连真机检测，不要求用户贴配置。
2. 判定：REJECT=被广告/规则集拦；DIRECT 连不上=直连被墙；PROXY 连不上=节点或 DNS 投毒（加 DoH）。
3. **修规则集不修 Rule.dconf**：误杀走代理→`Ad_Whitelist.list`；需直连→`Direct_Supplement.list`；需强制代理→`Proxy_Supplement.list`。推 mickeu/surge。
4. 同步 MRS 到 mickeu/Clash：自建规则集（ChinaMax_All 例外）改后用 `/tmp/mihomo1190 convert-ruleset domain text <源> <目标.mrs>` 重转。⚠️ 规则集用 Surge 原生 `//` 行内注释，mihomo 不认，**转换前先 `sed 's| //.*||'` 剥离行内注释**，否则整行被判非法 domain 产 0 字节。
5. 推 mickeu/surge + mickeu/Clash；纯增删域名一般不用改 Hako 覆写脚本。
6. 生效：`surge-cli external-resource update <key>`（key 从 `external-resource list` 取；先 curl raw 确认 CDN 已传播再 update，CDN 删内容有延迟）+ `surge-cli reload`；`rule match` 验证命中、`http probe` 验证连通。
7. 清理本次误加的临时规则（`rule temp remove`）。
⚠️ 临时规则只作验证，**不是最终修复**（重启/清缓存即失，且策略名须严格匹配你的组 `PROXY` 非 `Proxy`）。

### 防 DNS 泄露配置（2026-08-29 / 09-10 实测）

**核心三防线**（参考 Beatrice Surge Config 三道防线，已实测）：
1. `dns-server = system` + `use-local-host-item-for-proxy = false` —— DNS 跟网络走，代理域名不在本地解析
2. 所有含 IP 规则的 RULE-SET 加 `no-resolve` —— 代理域名不做本地 DNS 解析
3. `FINAL,<兜底策略>,dns-failed` —— DNS 失败就拒绝，不漏到本地

**关闭 IPv6**：`ipv6 = false, ipv6-vif = disabled`

**DoH 加密（蜂窝/WiFi 不泄露的关键，2026-09-10 实测）**：
- `encrypted-dns-server = https://1.1.1.1/dns-query, https://8.8.8.8/dns-query`
- ⚠️ 端点必须是 `/dns-query`（RFC8484）；`/resolve` 是 JSON API，收 RFC8484 二进制 → 400，DoH 静默失效
- `encrypted-dns-follow-outbound-mode = true`（DoH 走代理；直连 443 被运营商阻断）
- 必须保留 `dns-server = system` 作 fallback（纯 DoH 零明文做不到，代理挂掉时兜底）
- 删除 SSID 覆盖里的 `encrypted-dns-server=off`（否则 WiFi 下退回明文）
- 验证：`surge-cli dump dns` 看查询服务器是否 DoH 端点；browserleaks.com/dns 复测
- 配置只进 config-backup 私库，不进公开仓库

### 远程脚本更新工作流

1. 本地改脚本（`/tmp/surge-repo/Scripts/...` 或先写本地文件）→ `node --check` 验证语法
2. `git commit + push` 到 mickeu/surge（credential.helper 已配好）
3. `surge-cli reload` = 强制重新下载远程脚本，立即生效（不用等 script-update-interval）
4. 验证：`surge-cli --raw script list` 看脚本已加载；`external-resource list` 的 updatedAt = reload 时间
5. script-update-interval=86400 只作兜底，日常更新靠 reload

### 节点连通性测试（v6 坑）

- `/v1/policies/test`（HTTP API）**只对支持 IPv6 的节点生效**——Snell 日本/新加坡可测；Trojan/Hysteria2 等订阅节点单测返回空，**不要用它判断节点死活**。
- 判断组/节点可用性用组测速 `POST /v1/policy_groups/test`（body: `{"group_name":"X"}`），返回 `{"available":[...]}`；必须**串行**调用（并发限制导致部分组返回空）。
- `script evaluate <path> event <timeout>` 要单独跑，连发会让 controller 卡死；脚本 JS 语法错误静默输出空——先 `node --check`。
- 断线自动重连脚本：`mickeu/surge → Scripts/AutoReconnect/auto-reconnect.js`（叶子 select 组 + 组测速 + 切候选）。

### 抓包查看 header/body（surge-dump 工具，2026-10-22 实测）

用 surge-cli 控制抓包并查看完整请求/响应 header 与 body。封装脚本：`scripts/surge-dump.py`（复制自 workspace/surge-dump/，用法见脚本 docstring）。

**工作流**：
1. 开抓包：`surge-dump.py capture on --time 600`（等价于 `surge-cli set ReplicaSessionParameters.timeLimit=600` + `surge-cli feature set capture on`）。⚠️ 抓包默认窗口只有 **180 秒**，超时自动关闭，status 里 capture 会变回 Off。
2. 列记录：`surge-dump.py list --keyword <kw>`（等价于 `surge-cli --raw dump recent`）。
3. 看详情：`surge-dump.py show <id>` 输出完整 requestHeader / request body / responseHeader / response body / 连接 notes。
4. 存 body：`surge-dump.py body <id> request|response -o file`。

**关键技术点（实测踩坑）**：
- `surge-cli --raw dump recent` 每条记录含 `requestHeader`、`responseHeader`、`URL`、`method`、`status`、`streamHasRequestBody`、`streamHasResponseBody`、`replicaDirectoryPath`、`notes` 等——**header 在这里直接能看**。
- body 走 `surge-cli retrieve-data <id> request|response`，但返回的是**原始二进制**（`8字节小端长度 + \r\n + body`），官方 surge-cli 会因 `json.loads` 遇非 UTF-8 抛 `UnicodeDecodeError` 崩溃。surge-dump.py 用**直连 Controller socket** 读原始字节并解析长度前缀。
- body 解压按 header 的 `content-encoding` 判断（gzip/deflate）；gzip 魔数 `\x1f\x8b` 已验证可正确解压。
- `SURGE_CLI_REMOTE` 是本机实际 Controller 地址（本机非 127.0.0.1:6170），直连脚本必须读该环境变量，不要写死 localhost。
- 无 body 的请求（GET 无 body）`streamHasRequestBody=false`，show 会提示无 body。
- 实测抓包能穿过 MITM（httpbin 的 POST 请求体/响应体均完整抓到，含自定义 header）。

### 模块测试与管理（本地 & 远程，2026-10-22 整理）

本机 24 个本地模块之外，用户实际启用的大多为**远程模块**（Installed Modules，用 URL 安装）。两者测试管理流程基本一致，差异集中在「写模块」和「刷新生效」。

**本地模块**：`.sgmodule` 直接写进 `iCloud/Surge/Documents/Module/`，Surge 自动发现，按 `#!name=` 识别。

**远程模块**：`.sgmodule` 在 GitHub 仓库（mickeu/surge）维护并推送，Surge 通过订阅 URL 加载。⚠️ 远程模块文件本身**不在** `external-resource list` 里（外部资源只有 ruleset/script/policy-group），CLI 无法直接强制重拉模块文件本体；修改仓库推送后，需在 Surge App「模块」页手动更新该模块，或等待模块自动更新周期。

| 环节 | 本地模块 | 远程模块 |
|---|---|---|
| 写模块 | 写 `.sgmodule` 到 `iCloud/Surge/Documents/Module/` | 在 mickeu/surge 仓库改 `.sgmodule` → git push |
| 刷新生效 | Surge 自动发现，无需刷新 | 仓库推送后，在 Surge App「模块」页手动更新该模块（或等自动更新周期） |
| 语法自检 | `surge-cli --check <文件>`（可对仓库本地副本执行） | 同左；⚠️ 会把模块当完整配置检查，正常模块也报 "Rules must end with FINAL"，忽略；真正语法错误能准确定位到行 |
| 启用/停用 | `surge-cli module enable "<#!name>"` / `disable`，或 HTTP API `POST /v1/modules` | 同左；两种都能读到模块列表；启用后 Surge 自动重载配置 |
| 确认已生效 | `profile diff`：对比启用模块前后的配置 | 同左 |
| 调试规则 | `rule match` / `explain` | 同左 |
| 调试脚本 | `script evaluate`，用 `$argument` 传入真实 body | 同左 |
| 调试重写和 MitM | 开抓包 → `dump recent` 看 `modified` 字段 → `retrieve-data` 对比改写前后 body | 同左（iPhone 上也可以） |
| 看报错 | `log memory` / `log watch`、`script-log` | 同左 |

**方案选择**：优先 surge-cli。启用停用两种方案都能做，但调试需要的 `rule explain`、`script evaluate`、`retrieve-data`、`log` 只有 surge-cli 方便直接用。HTTP API 适合没有 surge-cli 的地方（如快捷指令）；本机 `http-api-tls = false`，HTTP API 明文传输，只适合在局域网或 tailnet 里用。

### 模块命名约定（2026-08-25 用户明确）

为用户制作的 Surge/Egern 模块，统一 `#!author=mickeu` 且 `#!category=mickeu`，新模块必须带上。