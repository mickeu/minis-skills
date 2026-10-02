---
name: Surge iOS 控制器
description: 通过同一台 iPhone 上的 Surge External Controller 远程控制 Surge。支持：surge-cli 全部命令（状态/策略/规则/模块/DNS/GeoIP/流量/日志/脚本/性能）、配置文件读写、规则解释与诊断、HTTP API 回退。需要开启 external-controller-access 和 http-api。
compatibility: Surge iOS with external-controller-access enabled; Python 3
metadata:
  upstream: Surge for macOS 6.9.0 (12100), bundled Skill synchronized and adapted for Minis
  controller_protocol: 23
  source: /Applications/Surge.app/Contents/Resources/Skills/surge/
---

# Surge for Minis

使用 `/usr/local/bin/surge-cli` 连接同机 Surge External Controller。默认地址为 `127.0.0.1:6170`；除非用户明确指定其他实例，不要连接外部主机。优先使用 `--raw` 获取 JSON。

## 认证

密码只从以下来源读取，禁止写进参数、文件、日志或回复：

1. `--password-stdin`
2. `SURGE_CLI_PASSWORD`
3. 交互式安全提示

先安全检查变量是否存在：

```sh
[ -n "$SURGE_CLI_PASSWORD" ] && echo set || echo missing
```

缺失时提供：[设置 SURGE_CLI_PASSWORD](minis://settings/environments?create_key=SURGE_CLI_PASSWORD&create_value=&create_note=Surge%20External%20Controller%20password)，不要让用户在聊天中发送密码。

## 操作原则

- 先读取与任务相关的状态，变更后立即重复读取验证。
- 修改前通常检查 `status`、`environment` 和相关策略或功能；只做最小变更。
- `dump profile` 可能包含节点地址、订阅 URL 等敏感信息，仅在确有必要时使用，不原样输出、记录或打包。
- 切换策略、模块或功能前先确认目标存在。
- `stop` 会关闭 Surge，仅在用户明确要求时执行。
- 对 `watch`、`diagnostics`、带宽测试和 `benchmark encryption` 持续读取 JSON Lines，遵循 `hasMore=false` 或命令结束载荷。

常用基线：

```sh
surge-cli --raw status
surge-cli --raw environment
surge-cli --raw dump policy
```

环境 key-path 可批量设置；`<nil>` 和 `(null)` 表示 null：

```sh
surge-cli --raw set ProxyMode=2
surge-cli --raw set ProxyGroupSelection.Proxy=HK
surge-cli --raw set AutoPolicyGroupOverride.Streaming=<nil>
```

## 修改配置文件（直接编辑 .conf）

Surge iOS 配置文件通过用户挂载目录暴露给 iSH：`/var/minis/mounts/nssurge/`（含多个 .conf：.Default.conf、`被🐶追的猫.conf`、`极速机场.conf` 等）。当前生效配置可用 `surge-cli profile current` 查看。

### 标准工作流（编辑 → reload → 验证）

```sh
# 1. 确认当前生效的配置文件名
surge-cli profile current

# 2. 编辑对应 .conf（file_read → file_edit/file_write，或用 sed 批量改）
#    路径：/var/minis/mounts/nssurge/<当前配置>.conf

# 3. 改完必须 reload 才生效
surge-cli reload

# 4. 验证改动已生效（status / 具体 dump）
surge-cli --raw status
```

直接编辑 .conf 文件后 **必须运行 `surge-cli reload` 才生效**（不是自动检测）。

三种修改方式对比：

1. **直接编辑 .conf 文件**（`file_edit`/`file_write`/`sed`，路径 `/var/minis/mounts/nssurge/`）— 最灵活，可改任意文本内容，**改完必须 `surge-cli reload`**
2. `surge-cli set <key-path>=<value>` — 改单个配置项，持久化写入，立即生效
3. Surge App 内置编辑器 — 手动改，保存自动重载

注意事项：
- reload 返回 `success` 即成功；失败时读 stderr 的错误信息，多为语法/值错误，改文件后重试
- 涉及多条配置修改时统一一次 reload，不要每条改一次
- 改错想回退：改回原内容再 reload，或 `surge-cli profile switch <name>` 切到备份配置

备注（2026-08-15 用户确认）：8月14日晚 http-api、external-controller 等配置都是直接编辑 .conf 文件完成的，不是 surge-cli set。

## 常见诊断

### 路由与 DNS

```sh
surge-cli --raw rule match example.com
surge-cli --raw rule explain https://example.com
surge-cli --raw dns trace example.com
surge-cli --raw geoip 1.1.1.1
```

- `rule match`：快速查看命中规则和最终策略。
- `rule explain`：查看完整策略组决策路径；回答“为什么这样走”时优先使用。
- `http probe <url> [policy]` 会发送真实 HEAD 请求，只在需要端到端验证时使用。

调试路由时优先使用会在 Surge 停止后失效的临时规则，而不是改 Profile：

```sh
surge-cli rule temp add "DOMAIN-SUFFIX,example.com,Proxy"
surge-cli rule temp list
surge-cli rule temp flush
```

### 性能与隧道

```sh
surge-cli --raw dump performance
surge-cli --raw dump rule-usage
surge-cli --raw benchmark rule-matching
surge-cli --raw benchmark encryption 25
```

### 节点连通性测试（v6 坑）

- `/v1/policies/test`（HTTP API）**只对支持 IPv6 的节点生效**——Snell 日本/新加坡可测；Trojan/Hysteria2 等订阅节点（不支持 v6）单测返回空，**不要用它判断节点死活**（假"不通"）。
- 判断组/节点可用性用组测速 `POST /v1/policy_groups/test`（body: `{"group_name":"X"}`），返回 `{"available":[...]}`，对 select 组 = 当前选中策略的可用性（含=可用，空=不可用），对所有协议正确。
- 组测速必须**串行**调用（Surge 单测速任务并发限制，并行会导致部分组返回空）。
- evaluate 测试 `script evaluate <path> event <timeout>` 要单独跑，连发会让 controller 卡死；脚本 JS 语法错误会静默输出空——先 `node --check`。
- 断线自动重连脚本：`mickeu/surge → Scripts/AutoReconnect/auto-reconnect.js`（叶子 select 组 + 组测速 + 切候选；Telegram 组因 MTProto v6 只允许切日本/新加坡）。

### 远程规则集维护工作流（新增域名规则必须走规则集，不写死 Rule.dconf）

**核心规则：所有能加进规则集文件的域名，一律加入对应规则集文件（如 `Gemini.list`、`Direct_Supplement.list`），不写死进 Rule.dconf。** Rule.dconf 只通过 `RULE-SET` 引用远程规则集。

- **如果 blackmatrix7 的规则集漏了域名**：把 blackmatrix7 的规则集拉下来，补全，保存到自己仓库 `mickeu/surge` 的**同名规则集文件**，Rule.dconf 里的引用 URL 改成 `mickeu/surge` 版本。Rule.dconf 不再指向 blackmatrix7 远程。
- 规则集用 `# NAME/AUTHOR/UPDATED/DOMAIN/.../TOTAL` 头注释，mickeu 补充的域名用 `# > 以下为 mickeu 补充` 分段标注，并更新 TOTAL 计数。
- 引用 URL 优先用 GitHub raw（不要用 jsdelivr，除非 GitHub raw 拉取失败，因为 jsdelivr CDN 缓存可能滞后）。
- 改完 `git commit + push` 到 mickeu/surge（用 credential.helper，见 GLOBAL.md"GitHub 推送认证"）。
- **包含密码/证书的配置文件（Proxy.dconf / mitm-ca.dconf / 主配置.conf）只能推 config-backup 私库**（`/var/minis/shared/config-backup/Surge/config/`），不能推公开仓库。
- 生效：Surge 需刷新规则集（`surge-cli reload` 或 Surge 界面重载），验证用 `surge-cli --raw rule match <domain>` 看域名是否命中对应规则集，或 `dump recent` 抓真实连接看 rule/policy。
- 验证规则集加载状态用 `surge-cli --raw external-resource list | grep -A2 Gemini` 看 ready 字段，不要用 `/v1/rules`（不展开规则集内容）。

**⚠️ 规则集缓存不对称（2026-09-19 实测，重要）**

- **新建规则集文件（全新 URL）→ `surge-cli reload` 后立即拉取生效**。
- **修改已有规则集文件（URL 不变）→ `surge-cli reload` 不刷新缓存**，`ready=true` 但 `updatedAt` 不变，规则内容还是旧的。`?v=` 参数实测无效。
- **不要只看 `ready=true` 判定生效**，必须用 `surge-cli --raw rule match <domain>` 验证实际命中的规则集 URL。`updatedAt` 时间戳不变 = 用的旧缓存。
- 唯一可靠刷新方式：Surge App 内手动「更新外部资源」，或等自身刷新周期。`surge-cli` 与 HTTP API 均无刷新外部资源的端点（`/v1/external_resources/update` 等实测连接失败）。
- **实务影响**：往规则集里补域名，无法替代"删除 Rule.dconf 原生规则"——原生规则一旦删掉，在缓存刷新前会落到后面的规则集（如 Global_All）走错策略。若原策略必须立即生效，保留原生规则或改用新规则集文件名。

### 远程脚本更新工作流（改脚本后立即生效）

1. 本地改脚本（`/tmp/surge-repo/Scripts/...` 或先写本地文件）→ `node --check` 验证语法
2. `git commit + push` 到 mickeu/surge（用 `https://x-access-token:${GITHUB_TOKEN}@github.com/mickeu/surge.git`）
3. `surge-cli reload` **= 强制重新下载远程脚本，立即生效**（不用等 script-update-interval）
4. 验证：`surge-cli --raw script list` 看脚本已加载；`external-resource list` 的 updatedAt 时间戳 = reload 时间
5. script-update-interval=86400 只作兜底自动更新，日常更新靠 reload

`benchmark encryption` 测量 Surge 所在设备的本地加密性能，不是网络带宽。

排查 Tailscale/WireGuard 时，先从 `dump policy` 找到 `lineHash`，再读取运行时状态：

```sh
surge-cli --raw proxy-runtime-status <line-hash>
```

优先检查握手、底层策略、Tailscale 会话、Exit Node、DERP 和 peer path，不要先做宽泛日志搜索。

### VMNET（macOS only）

Protocol 23 新增：

```sh
surge-cli --raw vmnet status
surge-cli --raw vmnet arp
surge-cli --raw vmnet ndp
surge-cli --raw vmnet ra
```

用于排查 macOS Enhanced/Gateway Mode 的接口、ARP/NDP 邻居和 IPv6 RA 接管。Surge iOS 返回 `Unsupported command` 属正常平台限制。

## 兼容性与回退

- `rule`、`dns`、`http probe`、`security ban` 需要 Controller Protocol ≥20。
- `geoip`、性能/规则使用/虚拟 IP dump、规则匹配 benchmark 需要 ≥22。
- `vmnet` 需要 ≥23，且仅限 macOS。
- 遇到 `Unknown command` 或能力异常时，先运行 `surge-cli --raw version` 核对 Surge、Core、平台和 Controller Protocol。
- iSH 不支持官方 macOS 本地 Profile 解析器，因此不能使用 `--check <path>`。

Controller 不可用或任务明确要求 `/v1/*` 时，读取 `references/http-api.md` 并使用 `scripts/surge_ios.py`。HTTP API 默认 `127.0.0.1:6171`，密钥仅从 `SURGE_HTTP_API_KEY` 获取；停止引擎必须使用脚本的危险操作确认参数。

## 参考与维护

按需读取，不要一次加载全部：

- 完整命令、响应字段和环境 key-path：`references/command-reference.md`
- Controller 协议、安装与认证：`references/controller-cli.md`
- HTTP API 回退：`references/http-api.md`
- Profile、模块和代理语法：`references/manual-index.md`
- 实测坑位与命令菜谱（外部资源更新/$event 崩溃/MITM CA 方案/测速）：`references/pitfalls-and-cookbook.md`
- 官方上游同步、版本和发布流程：`references/SOURCE.md`

安装或改动后运行只读验收：

```sh
/var/minis/skills/surge/scripts/acceptance.sh
```

## 模块命名约定（2026-08-25 用户明确）
为用户制作的 Surge/Egern 模块，统一 `#!author=mickeu` 且 `#!category=mickeu`。新模块必须带上。
