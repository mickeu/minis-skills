---
name: sing-box 知识库
description: sing-box 官方文档全量中文镜像（168 个文件）+ 配置生成与排查能力，覆盖全部协议、路由、DNS、TUN、出站类型与示例配置。当用户提到「sing-box」「singbox」时触发。
---
# sing-box 知识库技能

> sing-box 官方文档全量中文镜像 + 配置生成与排查能力。

## 来源
- **官方文档**：https://sing-box.sagernet.org/zh/ （mkdocs-material 站点）
- **源仓库**：https://github.com/SagerNet/sing-box （`testing` 分支 `docs/` 目录，i18n suffix 模式：`xxx.zh.md` 为中文版）
- **扒取方式**：从仓库 `mkdocs.yml` 的 nav 提取全部 .md 路径 → 生成 `xxx.zh.md` raw URL → minis-browser-use 批量 fetch → 存入 `docs/` 目录（缺失中文的页面 fallback 到英文版）
- **首次扒取**：2026-08-31，共 147 个文件
- **全量更新**：2026-09-29，共 168 个文件（直接 git clone 仓库 docs/ 目录同步，5 新增 + 40 更新）

## 目录结构
```
/var/minis/skills/sing-box/
├── SKILL.md            ← 本文件
├── docs/               ← 全量文档（168 个 .md，中文为主 + 英文独有页面）
│   ├── index.zh.md                          开始
│   ├── changelog.md                         更新日志（英文，唯一来源）
│   ├── migration.zh.md                      迁移指南（字段废弃/迁移，排查必读）
│   ├── deprecated.zh.md                     废弃功能列表
│   ├── configuration_index.zh.md            配置引言（顶级结构）
│   ├── configuration_dns_index.zh.md        DNS
│   ├── configuration_dns_server_*.zh.md     DNS 服务器各类型
│   ├── configuration_dns_rule.zh.md         DNS 规则
│   ├── configuration_dns_rule_action.zh.md DNS 规则动作
│   ├── configuration_route_index.zh.md     路由
│   ├── configuration_route_rule.zh.md       路由规则
│   ├── configuration_route_rule_action.zh.md 路由规则动作
│   ├── configuration_rule-set_*.zh.md       规则集
│   ├── configuration_shared_*.zh.md         通用字段（拨号/TLS/HTTP客户端/传输层等）
│   ├── configuration_inbound_*.zh.md        入站
│   ├── configuration_outbound_*.zh.md       出站（各代理协议）
│   ├── configuration_endpoint_*.zh.md       端点
│   ├── configuration_service_*.zh.md        服务
│   ├── configuration_experimental_*.zh.md   实验性
│   ├── configuration_endpoint_masque-*.zh.md  MASQUE 端点（1.15.0+）
│   ├── configuration_inbound_tailcat.zh.md  Tailcat 入站（1.15.0+）
│   ├── configuration_outbound_tailcat.zh.md Tailcat 出站（1.15.0+）
│   ├── clients_*.md                         客户端文档（英文）
│   └── manual_*.md                          手动配置文档（英文）
└── scripts/
    ├── batch_fetch.sh   ← 批量扒取脚本（从 mkdocs.yml nav 生成 URL 并 fetch）
    └── gen_config.py    ← 配置生成器（订阅→sing-box 配置，参照 Surge 分流）
```

## 自动更新规则（用户偏好，2026-08-31 明确）

**当用户发来 sing-box 相关内容（配置、报错、截图、文档链接、订阅等），自动执行：**
1. 先查 `migration.zh.md` 和 `deprecated.zh.md`，确认当前版本字段是否废弃——sing-box 在 1.8→1.16 持续迁移，旧字段报错极常见
2. 扒取的文档可能滞后，优先信文档里的"Changes in 1.x.0"标记 + 用户实际版本的报错
3. 若用户提到的字段/行为在本地文档找不到，或文档明显过期，重新跑 `batch_fetch.sh` 更新文档（见下方"更新文档"）

## 更新文档（重新同步）

```bash
# 方法一：直接 git clone 仓库 docs/ 目录（推荐，最快最可靠）
cd /var/minis/workspace && git clone --depth 1 https://github.com/SagerNet/sing-box.git sing-box-src
# 然后按 SKILL.md 的命名约定同步（路径 / → _ 扁平化）
cd sing-box-src/docs && for f in $(find . -name '*.zh.md'); do
  flat=$(echo "${f#./}" | sed 's|/|_|g'); cp "$f" "/var/minis/skills/sing-box/docs/$flat"; done
# 英文独有页面也复制
cp changelog.md clients/*.md clients/*/*.md manual/*/*.md manual/*/*/*.md sponsors.md /var/minis/skills/sing-box/docs/
# 清理克隆
rm -rf /var/minis/workspace/sing-box-src

# 方法二：批量扒取脚本（备用）
minis-browser-use fetch --url "https://raw.githubusercontent.com/SagerNet/sing-box/testing/mkdocs.yml"
bash /var/minis/skills/sing-box/scripts/batch_fetch.sh
```

## 当前已知版本与关键字段状态（2026-09-29 更新）

最新稳定版：**1.14.2**（2026-09-24）。testing 分支最新预发布：**1.15.0-alpha.9**。
用户 iOS 版 sing-box = **1.14.2**（2026-09-29 更新安装）。

### 1.15.0-alpha 重大变更（2026-08-31 后新增）
- **MASQUE Client/Server 端点**（1.15.0-alpha.7）：HTTP CONNECT-IP 代理，支持 HTTP/1.1/2/3
- **HTTP 代理重写**（1.15.0-alpha.7）：HTTP/2、HTTP/3、CONNECT-UDP 支持；HTTP outbound 默认 HTTP/2 自动降级 HTTP/1.1；`version` 选项启用 HTTP/3
- **证书钉扎**（1.15.0-alpha.7）：`certificate_sha256` / `client_certificate_sha256` 完整证书哈希钉扎
- **Tailcat 入站/出站**（1.15.0-alpha.5）：Tailscale 数据面（DERP bootstrap + NAT 穿透）
- **新路由规则项**（1.15.0-alpha.8）：`dns_server_address` / `dns_search_domain`
- **TUN stack 重写**（1.15.0-alpha.3）：自有 TCP/IP stack，`stack` 参数废弃，1.17.0 移除
- **NaiveProxy 更新**（1.15.0-alpha.9）：154.0.8037.49-2
- **DERP service 增强**：`verify_client_inbound` / `verify_client_key` 选项

### 1.14.0 重大变更（仍有效，直接影响配置编写）
- **`download_detour`（remote rule-set）已废弃** → 改用顶级 `http_clients` + route 的 `default_http_client` + rule-set 的 `http_client`
- **DNS fakeip 顶层 `fakeip` 字段废弃** → fakeip 作为独立 DNS server 类型（`type: "fakeip"`）
- **DNS legacy server（`address` 字段）废弃** → 用新 `type` 格式（https/local/udp/tls/quic/...）
- **`https` DNS server 默认走"空直连出站"** → 不配 detour 会报 `detour to an empty direct outbound makes no sense`，必须用 `http_clients` 或拨号字段 detour 指定真实出站
- **DNS outbound（`type: "dns"`）已移除** → DNS 由路由层 `protocol: "dns"` 规则 + 默认处理，不再需要独立 dns outbound
- **route rule 的 `action` 必填**（`route`/`reject`/`sniff`/等），旧 `outbound` 字段废弃移到 rule action
- **`geosite`/`geoip` route 字段废弃** → 改用 rule-set（`geoip-cn`、`geosite-cn` 等）
- **inbound 顶层 `sniff` 字段废弃** → sniff 由路由 rule action 处理

### 规则集来源（sing-box 最优选择）
- **MetaCubeX/meta-rules-dat `sing` 分支 .srs**：`https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/sing/geo/geosite/{name}.srs` 和 `.../geo/geoip/{name}.srs`
- 二进制格式，sing-box 原生优化，比 blackmatrix7 .list 快
- 常用：category-ads-all / cn / geolocation-cn / geolocation-!cn / gfw / apple / apple@cn / apple-intelligence / openai / anthropic / google / telegram / youtube / netflix / disney / spotify / tiktok / bilibili / microsoft / category-games / blizzard / category-media-cn / tld-cn / private / geoip-cn / geoip-telegram
- sing-box 官方 sing-geosite/sing-geoip 现只发 `.db`（对应已废弃 geosite/geoip 字段，不能用）

## 排查 sing-box 报错的固定流程

1. **先看报错类型**：`Failed to start service` / `FATAL` / 迁移期 `deprecated`
2. **查本地文档**：grep `docs/` 找对应配置段，看 "Changes in 1.x.0" 标记确认字段是否废弃
3. **查 migration.zh.md**：有完整的"旧→新"对照
4. **用 musl 二进制校验**：`/tmp/sing-box-1.13.21-linux-arm64-musl/sing-box check -c config.json`（注意：本地二进制是 1.13，1.14 特有校验它查不出，以用户实际 iOS 版为准）
5. **修完重跑 check**，再给用户导入

## 配置生成器（gen_config.py）

`scripts/gen_config.py` 把订阅解析成 sing-box 完整配置，参照用户 Surge 配置的分流设计：
- 节点解析：hysteria2 / trojan(ws) / vless(reality+ws) / vmess(ws)
- DNS 防泄露：国内域名→国内 DoH 直连，代理域名→境外 DoH 经 PROXY，广告拒答，其余 FakeIP
- 策略组对齐 Surge：PROXY + AIGC/Telegram/YouTube/Netflix/... 共 13 个 selector + 地区 urltest 组
- 规则集全用 MetaCubeX .srs，顺序对齐 Surge Rule.dconf

**已适配 1.14+ 的改动**（2026-09-29）：
- ✅ rule-set 的 `download_detour` 改为顶级 `http_clients`（detour 指向 PROXY）+ `default_http_client`
- ✅ DNS https server 仍用 `detour` 字段（DNS server 的 dial 字段，1.14+ 仍有效）
- ⚠️ 1.15.0-alpha 新增 MASQUE/Tailcat/HTTP3 等能力，gen_config.py 暂未覆盖（需升级才能用）

## 注意事项
- 本地 iSH 的 sing-box 二进制是 **1.13.21 musl arm64**（`/tmp/sing-box-1.13.21-linux-arm64-musl/sing-box`），仅用于 check 校验，不用于运行
- 用户 iOS sing-box 是 **1.14.2**（2026-09-29 更新）
- 1.15.0-alpha 功能需升级 iOS 版才能使用（MASQUE/Tailcat/HTTP3/TUN stack 重写）
- shell 的 DNS 解析 raw.githubusercontent.com 经常失败，优先用浏览器 fetch 或直接 git clone
- 文档目录结构已从扁平命名升级为仓库原始嵌套路径（2026-09-29），但技能库保持扁平化命名兼容
