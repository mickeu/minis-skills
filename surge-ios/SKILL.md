---
name: surge-ios
description: 通过同机 Surge External Controller 检查和控制 Surge iOS，处理策略与节点、规则、DNS、连接、模块、脚本及代理诊断。涉及 Surge 专有命令或配置时使用；优先 Minis surge-cli，HTTP API 按需回退。
compatibility: Surge iOS with external-controller-access enabled; Python 3
metadata:
  upstream: Surge for macOS 6.9.0 (12250), bundled Skill synchronized and adapted for Minis
  controller_protocol: 25
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
| Controller 不可用、明确要求 `/v1/*`、指标或未配置节点测试 | [http-api.md](references/http-api.md) |
| 平台限制、Unknown command、协议版本异常 | [platform-compatibility.md](references/platform-compatibility.md) |
| 安装、认证传输和客户端协议 | [controller-cli.md](references/controller-cli.md) |

切换策略、模块或功能前确认目标存在，按需读取相关列表，不把全量 `dump policy`/日志/Profile 当每次任务的前置流程。只做最小授权变更，变更后重读相关状态；需要端到端证明时再做真实请求。

环境 key-path 的 null 值须保护 shell 引号，例如：

```sh
surge-cli --raw set 'AutoPolicyGroupOverride.Streaming=<nil>'
```

`<nil>` / `(null)` 的接口语义、ProxyMode 数值和组选择字段以命令参考为准；上例是写操作，不是检查命令。

## 4. 保留影响边界

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

### 模块命名约定（2026-08-25 用户明确）

为用户制作的 Surge/Egern 模块，统一 `#!author=mickeu` 且 `#!category=mickeu`，新模块必须带上。