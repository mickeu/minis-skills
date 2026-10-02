---
name: Clash / Mihomo 配置参考
description: >
  Mihomo / Hako / Clash Meta 内核完整 YAML 配置参考。涵盖全局配置、DNS、规则语法（含逻辑规则）、
  策略组、27 种出站协议（vmess/vless/trojan/shadowsocks/gost-relay/hysteria/hysteria2/tuic/shadowquic/
  trusttunnel/anytls/mieru/sudoku/wireguard/tailscale/zerotier/easytier/openvpn/masque/ssr/ssh/snell/rematch/dns/direct）、
  18 种入站监听（listeners）、节点订阅（proxy-providers，含 override-expr yq v4 表达式覆写）、
  规则订阅（rule-providers）、TUN（system/gvisor/mixed/mips 四种 stack）、Sniffer、tunnels、hosts、
  **Hako 覆写脚本（Override Script，JSContext main(config)）**、完整配置模板与常见坑。
  基于 TokenPLS/Hako 源码（mihomo v1.19.31 fork，Hako HEAD `7ea70d15`，上游基线 v1.19.31）的 docs/config.yaml
  与 config/config.go 结构定义提取，字段类型与默认值对照 Go struct。
  当用户提到 mihomo、Clash Meta、Hako、Clash 配置、YAML 配置格式、DNS 配置、fake-ip、规则、
  RULE-SET、GEOSITE、策略组、url-test、proxy-groups、proxy-providers、订阅、override、override-expr、
  覆写脚本、override-script、preprocess-script、main(config)、JSContext、过滤非法节点、
  vmess、vless、reality、xtls、hysteria2、tuic、trusttunnel、anytls、mieru、sudoku、wireguard、
  openvpn、masque、listeners、TUN、Sniffer、gost-relay、dialer-proxy、smux、mrs 等代理内核配置时触发。
source_url: https://github.com/TokenPLS/Hako
license: GPL-3.0
last_sync: 2026-09-24
---
# clash-config

## 触发条件

当用户询问 Clash / Mihomo / Hako 配置、YAML 配置格式、DNS 配置、规则语法、策略组、节点订阅（proxy-providers）、规则订阅（rule-providers）、出站协议字段（vmess/vless/trojan/shadowsocks/reality/tuic/hysteria2/trusttunnel/anytls/mieru/sudoku 等）、入站监听（listeners）、TUN、Sniffer 等 mihomo 内核配置相关内容时触发。

## 概述

- **配置格式**：YAML，单文件
- **内核关系**：Hako = MetaCubeX/mihomo v1.19.31 的独立 fork，配置格式与 mihomo 完全兼容，Hako 额外增加了 Apple 平台特化配置（见 `references/hako-incremental.md`）
- **客户端**：Hako 客户端（App Store id6794257189）、FlClash（Flutter，用 mihomo 内核）均用此配置格式
- **规则集格式**：YAML / text / MRS（二进制），mihomo 用 `.mrs` 格式（区别于 Clash 的 `.list`/`.yaml`）
- **配置文件参考**：`Hako/docs/config.yaml`（2812 行带中文注释的完整参考）

## 数据来源

所有来源已逐一 clone 并核对 git HEAD（2026-09-24）。

| 来源 | 核对的 HEAD commit | 内容 | 本地路径 |
|---|---|---|---|
| **TokenPLS/Hako** | `7ea70d15` 2026-09-24 | 内核源码 = mihomo v1.19.31 fork | `/var/minis/workspace/Hako` |
| ├─ `docs/config.yaml` | — | 完整配置参考（2855 行带中文注释） | 技能库主要素材 |
| ├─ `bind/hako/` | — | Apple 绑定层，121 个非测试 .go | 增量配置参考 |
| ├─ `adapter/outbound/` | — | 30+ 出站协议配置字段 | 协议字段参考 |
| └─ `config/config.go` | — | 配置结构体定义（约 2200 行） | 字段类型/默认值 |
| **TokenPLS/Hako-Client** | `62aa2f2` 2026-09-24 | Apple 客户端源码（纯 Swift） | `/var/minis/workspace/Hako-Client` |
| ├─ `Dependencies.lock.json` | — | 依赖版本锁定（kernel `7ea70d15` 与 Hako HEAD 一致 ✅） | 版本追溯 |
| └─ `apple/` | — | HakoClient（应用+扩展）/ HakoClientKit / HakoClientUI / HakoMacClient | 四模块结构 |
| **TokenPLS/Hako-Adapter** | `6a47cf9` 2026-09-24 | Swift 数据包桥接 | `/var/minis/workspace/Hako-Adapter` |
| └─ `Sources/HakoAdapter/` | — | `PacketFlowBridge.swift` + `ProviderLifecycle.swift` | Swift 5.9，iOS15+/macOS13+/tvOS17+ |
| **MetaCubeX/mihomo**（上游） | ✅ 已恢复 | 上游基线 v1.19.31，commit `ab405bad` | 直接 clone 可用 |
| **chen08209/FlClash** | `c7be7023` 2026-09-17 | Flutter 客户端（mihomo 内核） | `/var/minis/workspace/FlClash` |
| **SagerNet/sing-box** | `ac87080d` 2026-09-21 | 独立 JSON 配置体系（不在此技能库） | `/var/minis/workspace/sing-box` |
| **clash.md**（官网） | — | 发行主体 **OmniWide Media Limited**，legal@omniwide.media | https://clash.md |
| ├─ `/terms` | Last updated 18 Aug | 补充条款：Apple Standard EULA、lawful use、自带代理、责任限制 | 不收集代理数据 |
| └─ `/privacy` | Last updated 21 | 收集不到 app/VPN 数据，profile 本地存储，支持 iCloud 备份 | 同上 |

**⚠️ 上游仓库已恢复**：README 明确声明 Hako 基于 [mihomo v1.19.31](https://github.com/MetaCubeX/mihomo/tree/v1.19.31)，上游基线 commit `ab405bad5beeeac8b003bb01f60f134f6df54471`。旧基线 v1.19.30 (`ac017cdd`) 仍在历史中可查。

**版本锁定**（`Hako-Client/Dependencies.lock.json`）：

```
kernel:   7ea70d15bf8b67257928efe45c12f16d4ffc9f61   (TokenPLS/Hako)
adapter:  01b6f728973857b3c553a56ea1aeef24669c1128   (TokenPLS/Hako-Adapter)
gomobile: github.com/sagernet/gomobile@v0.1.13
上游基线: mihomo v1.19.31 @ ab405bad5beeeac8b003bb01f60f134f6df54471
许可证:   GPL-3.0
```

**三仓库架构**：Hako（内核，Go）+ Hako-Adapter（数据包桥接，Swift）+ Hako-Client（应用，Swift）
官网 https://clash.md ，App Store id6794257189

### 配置文件结构总览（顶级字段）

```yaml
# ── 网络入口 ──
mixed-port: 10801          # HTTP(S)+SOCKS 混合端口（推荐）
port: 7890                 # HTTP(S) 端口
socks-port: 7891           # SOCKS5 端口
redir-port: 7892           # 透明代理（TCP）
tproxy-port: 7893          # TProxy（TCP+UDP，Linux）
allow-lan: true            # 允许局域网
bind-address: "*"
authentication: []         # HTTP/SOCKS 认证
skip-auth-prefixes: []     # 跳过认证网段
lan-allowed-ips: []        # LAN 白名单
lan-disallowed-ips: []     # LAN 黑名单（优先于白名单）

# ── 运行模式 ──
mode: rule                 # rule / global / direct
find-process-mode: strict  # always / strict / off
log-level: debug           # silent/error/warning/info/debug
ipv6: true
interface-name: en0        # 出口网卡

# ── GeoData ──
geox-url:                  # 自定义 GeoIP/GeoSite/MMDB 下载源
geo-auto-update: false
geo-update-interval: 24    # 小时
geosite-matcher: succinct  # succinct（默认）/ mph

# ── API 控制 ──
external-controller: 0.0.0.0:9093
external-controller-tls: 0.0.0.0:9443
external-controller-unix: mihomo.sock     # Unix socket（不验 secret）
external-controller-pipe: \\.\pipe\mihomo # Windows 命名管道（不验 secret）
external-controller-routing-mark: 0       # 仅 Linux
secret: ""                                 # Bearer 认证
external-controller-cors:                  # CORS 配置
  allow-origins: ["*"]
  allow-private-network: true
external-doh-server: /dns-query           # 在 API 端口开 DOH（不验 secret）

# ── Web UI ──
external-ui: /path/to/ui
external-ui-name: xd
external-ui-url: "https://..."            # 支持 zip/tgz 下载

# ── TLS ──
tls:
  certificate: string    # PEM 内容或路径
  private-key: string
  client-auth-type: ""   # ""/request/require-any/verify-if-given/require-and-verify
  client-auth-cert: string
  ech-key: ""            # ECH 密钥（mihomo generate ech-keypair <域名> 生成）
  custom-certifactes: [] # 自定义 CA 证书

# ── 其他 ──
hosts: {}                # 类似 /etc/hosts，仅支持单个 IP 或别名
tunnels: []              # 隧道转发（固定端口转发）
sniffer: {}              # 协议嗅探
profile:                 # 状态持久化
  store-selected: false  # 存储 select 选择记录
  store-fake-ip: true    # 持久化 fake-ip
tun: {}                  # TUN 配置
dns: {}                  # DNS 配置
proxies: []              # 出站节点列表
proxy-groups: []         # 策略组
proxy-providers: {}      # 节点订阅
rule-providers: {}       # 规则订阅
sub-rules: {}            # 子规则集
rules: []                # 路由规则
listeners: []            # 入站监听
experimental: {}         # 实验性配置
routing-mark: 0          # fwmark，仅 Linux
```

## 全局配置详解

### 端口与网络

| 字段 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `mixed-port` | int | - | HTTP(S)+SOCKS 混合端口，推荐用这个替代 port+socks-port |
| `port` | int | 7890 | HTTP(S) 代理端口 |
| `socks-port` | int | 7891 | SOCKS5 代理端口 |
| `redir-port` | int | 7892 | 透明代理 TCP 端口 |
| `tproxy-port` | int | 7893 | TProxy 端口（TCP+UDP，仅 Linux） |
| `allow-lan` | bool | false | 允许局域网访问 |
| `bind-address` | string | `*` | 绑定 IP，仅 allow-lan=true 时生效 |
| `authentication` | list | - | HTTP/SOCKS 认证，格式 `"user:pass"` |
| `skip-auth-prefixes` | list | - | 跳过认证的网段 |
| `lan-allowed-ips` | list | `["0.0.0.0/0","::/0"]` | LAN 白名单 |
| `lan-disallowed-ips` | list | `[]` | LAN 黑名单，优先级高于白名单 |

### 运行模式

| 字段 | 值 | 说明 |
|---|---|---|
| `mode` | `rule` / `global` / `direct` | 路由模式 |
| `find-process-mode` | `always` / `strict` / `off` | 进程名匹配；`strict` 由内核判断，`always` 强制，`off` 关闭（路由器推荐） |
| `log-level` | `silent`/`error`/`warning`/`info`/`debug` | 日志级别 |
| `ipv6` | bool | IPv6 总开关，关闭则阻断所有 IPv6 和 AAAA 查询 |

### GeoData 管理

```yaml
geox-url:
  geoip: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat"
  geosite: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat"
  mmdb: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.metadb"
geo-auto-update: false
geo-update-interval: 24    # 小时
geosite-matcher: succinct  # succinct（默认）或 mph（V2Ray 实现）
```

### Web UI

```yaml
external-ui: /path/to/ui          # 本地 UI 目录
external-ui-name: xd              # UI 名称
external-ui-url: "https://..."    # 支持 zip/tgz 下载
external-controller: 0.0.0.0:9093 # UI 访问地址 http://<host>:<port>/ui
```

### tunnels（隧道转发）

```yaml
tunnels:
  - tcp/udp,127.0.0.1:6553,114.114.114.114:53,proxy   # 单行格式
  - tcp,127.0.0.1:6666,rds.mysql.com:3306,vpn
  - network: [tcp, udp]   # 完整格式
    address: 127.0.0.1:7777
    target: target.com
    proxy: proxy
```

### experimental

```yaml
experimental:
  quic-go-disable-gso: true  # 禁用 quic-go GSO（仅 Linux，解决兼容问题）
```

## DNS 配置

```yaml
dns:
  enable: false                # 关闭则使用系统 DNS
  cache-algorithm: arc         # DNS 缓存算法（lru / arc）
  cache-max-size: 0            # DNS 缓存最大条目数，0=不限制
  listen: 0.0.0.0:53           # DNS 监听地址
  listen-routing-mark: 0       # DNS 监听 socket 的 fwmark（仅 Linux）
  prefer-h3: false             # DoH 支持 HTTP/3，并发尝试
  ipv6: false                  # false 返回 AAAA 空结果
  ipv6-timeout: 100            # 双栈并发时等待 AAAA 的超时（ms），默认 100
  use-hosts: true              # 使用 hosts 文件，默认 true
  use-system-hosts: true       # 使用系统 hosts 文件，默认 true
  respect-rules: false         # DNS 请求遵循 rules；开启后 proxy-server-nameserver 不能为空
```

### DNS 服务器分级

```yaml
dns:
  # 用于解析其他 DNS 服务器域名的（只能用纯 IP，可加密）
  default-nameserver:
    - 114.114.114.114
    - 8.8.8.8
    - tls://1.12.12.12:853
    - tls://223.5.5.5:853
    - system               # 从系统配置追加 DNS

  # 主要 DNS，影响所有直连
  nameserver:
    - 114.114.114.114      # 默认值
    - 8.8.8.8               # 默认值
    - tls://223.5.5.5:853   # DNS over TLS
    - https://doh.pub/dns-query                    # DNS over HTTPS
    - https://dns.alidns.com/dns-query#h3=true     # 强制 HTTP/3
    - https://mozilla.cloudflare-dns.com/dns-query#DNS&h3=true  # 指定策略组+H3
    - dhcp://en0            # 从 DHCP 获取
    - quic://dns.adguard.com:784                    # DNS over QUIC
    - ts://tailscale        # 使用指定 Tailscale 出站的 DNS
    - et://easytier        # EasyTier overlay DNS（仅解析 A/PTR，建议放在 nameserver-policy）
    - '8.8.8.8#RULES'      # 该服务器遵循 rules 规则（等价 respect-rules 但仅单个）
    - '8.8.8.8#en0'        # 指定该 DNS 服务器出口网卡

  # 降级 DNS（nameserver 解析结果非 CN 时使用）
  fallback:
    - tcp://1.1.1.1
    - 'tcp://1.1.1.1#ProxyGroupName'  # 指定代理查询，优先于网卡指定

  # 专用于节点域名解析
  proxy-server-nameserver:
    - https://doh.pub/dns-query
  proxy-server-nameserver-policy:      # 格式同 nameserver-policy
    'www.yournode.com': '114.114.114.114'

  # 专用于 direct 出口域名解析
  direct-nameserver:
    - system://
  direct-nameserver-follow-policy: false
```

### fallback-filter（降级判断条件）

```yaml
dns:
  fallback-filter:
    geoip: true              # 是否用 geoip 判断
    geoip-code: CN           # 解析结果 IP 为 CN 时用 nameserver 结果
    ipcidr:                  # 匹配时用 fallback 结果
      - 240.0.0.0/4
      - 0.0.0.0/32
      - 127.0.0.1/32
      - 100.64.0.0/10
    domain:                  # 匹配时直接用 fallback
      - '+.google.com'
      - '+.youtube.com'
  fallback-lazy-query: false  # true 则先判断 nameserver 结果是否满足 filter 再查询
```

### nameserver-policy（按域名分流）

```yaml
dns:
  nameserver-policy:
    "geosite:cn,private,apple":
      - https://doh.pub/dns-query
      - https://dns.alidns.com/dns-query
    "geosite:category-ads-all": rcode://success
    "www.baidu.com,+.google.cn": [223.5.5.5, https://dns.alidns.com/dns-query]
    "rule-set:global,dns": 8.8.8.8   # 支持 rule-provider（behavior 必须 domain/classical）
```

### fake-ip 模式

```yaml
dns:
  enhanced-mode: fake-ip     # fake-ip 或 redir-host
  fake-ip-range: 198.18.0.1/16
  fake-ip-range6: fdfe:dcba:9876::1/64
  fake-ip-ttl: 1             # fake-ip TTL，非必要勿改
  fake-ip-filter:
    - '*.lan'
    - localhost.ptlogin2.qq.com
    - rule-set:fakeip-filter   # rule-provider（behavior domain/classical）
    - geosite:fakeip-filter    # geosite 分类
    # 当 fake-ip-filter-mode: rule 时启用规则模式
    - RULE-SET,reject-domain,fake-ip
    - DOMAIN,www.baidu.com,real-ip
    - DOMAIN-SUFFIX,qq.com,real-ip
    - DOMAIN-SUFFIX,jd.com,fake-ip
    - MATCH,fake-ip           # 最后一条 fake-ip 或 real-ip
  fake-ip-filter-mode: blacklist  # blacklist / whitelist / rule
```

### 其他 DNS 字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `respect-rules` | bool | nameserver/fallback/nameserver-policy 的连接是否遵守 rules |
| `use-hosts` | bool | 是否查询 hosts |
| `use-system-hosts` | bool | 是否使用系统 hosts |

## 规则配置

### 规则语法

格式：`<类型>,<参数>,<目标>`

```yaml
rules:
  - RULE-SET,rule1,REJECT            # 引用 rule-provider
  - IP-ASN,1,PROXY                    # IP 自治系统号
  - DOMAIN-REGEX,^abc,DIRECT          # 域名正则
  - DOMAIN-SUFFIX,baidu.com,DIRECT    # 域名后缀
  - DOMAIN-KEYWORD,google,ss1         # 域名关键词
  - DOMAIN-WILDCARD,test.*.mihomo.com,ss1  # 域名通配
  - DOMAIN,www.example.com,PROXY      # 精确域名
  - IP-CIDR,1.1.1.1/32,ss1            # IPv4 CIDR
  - IP-CIDR6,2409::/64,DIRECT         # IPv6 CIDR
  - GEOSITE,category-ads-all,REJECT   # GeoSite 分类
  - GEOIP,private,DIRECT              # GeoIP 分类
  - PROCESS-NAME,WeChat,DIRECT        # 进程名
  - PROCESS-PATH,/path/to/app,PROXY   # 进程路径
  - DST-PORT,443,PROXY                # 目标端口
  - SRC-IP-CIDR,192.168.1.0/24,DIRECT # 源 IP
  - SRC-PORT,50000,REJECT             # 源端口
  - NETWORK,UDP,DIRECT                # 网络类型（tcp/udp）
  - UID,1000,DIRECT                   # 用户 ID（Linux）
  - IN-NAME,socks-in-1,PROXY          # 入站名称
  - IN-TYPE,socks,PROXY               # 入站类型
  - IN-USER,user1,PROXY               # 入站用户名
  - IN-PORT,10808,DIRECT              # 入站端口
  - DSCP,46,PROXY                     # DSCP 值
  - REMATCH-NAME,rematch1,PROXY       # rematch 名称
  - AND,((DOMAIN,example.com),(NETWORK,TCP)),PROXY  # 逻辑与
  - OR,((NETWORK,TCP),(NETWORK,UDP)),PROXY          # 逻辑或
  - NOT,((DOMAIN,example.com)),DIRECT                # 逻辑非
  - SUB-RULE,(OR,((NETWORK,TCP),(NETWORK,UDP))),sub-rule-name1  # 子规则
  - MATCH,PROXY                       # 兜底规则（必须放最后）
```

目标（出口）可用：`PROXY`（全局）、`DIRECT`、`REJECT`、节点名、策略组名。

### 常用规则类型速查

源码支持 **38 种**规则类型（`rules/parser.go` 的 case 分支，commit `7ea70d15`）。

**⚠️ 常见错误类型**：`OS`、`INBOUND`、`SCRIPT` 不是 mihomo 规则类型。操作系统用 `SOURCE-APP-*`（iOS），入站用 `IN-NAME`/`IN-TYPE`/`IN-USER`，脚本用 `REMATCH-NAME` 或 rule-provider。

| 类型 | 参数 | 说明 |
|---|---|---|
| `DOMAIN` | 精确域名 | 精确匹配 |
| `DOMAIN-SUFFIX` | 域名 | 后缀匹配，含自身 |
| `DOMAIN-KEYWORD` | 关键词 | 关键词包含 |
| `DOMAIN-REGEX` | 正则 | 正则匹配（性能较差） |
| `DOMAIN-WILDCARD` | `*.example.com` | 通配符匹配 |
| `GEOSITE` | 分类名 | GeoSite 分类匹配 |
| `GEOIP` | 分类名 / 国家代码 | GeoIP 分类匹配 |
| `SRC-GEOIP` | 分类名 | 源 GeoIP 匹配 |
| `IP-CIDR` / `IP-CIDR6` | `1.1.1.1/32` / `2409::/64` | IPv4 / IPv6 网段 |
| `IP-SUFFIX` | `1.1.1.1/32` | IP 后缀（不做掩码规范化） |
| `IP-ASN` | ASN 号 | 自治系统号 |
| `SRC-IP-CIDR` | 网段 | 源 IP 网段 |
| `SRC-IP-SUFFIX` | IP 段 | 源 IP 后缀 |
| `SRC-IP-ASN` | ASN 号 | 源 ASN |
| `SRC-PORT` / `DST-PORT` | 端口 | 源 / 目标端口 |
| `IN-PORT` | 端口 | 入站端口 |
| `IN-TYPE` | `socks`/`http`/... | 入站类型 |
| `IN-USER` | 用户名 | 入站用户名 |
| `IN-NAME` | 入站名 | 入站名称（监听 name） |
| `PROCESS-NAME` | 进程名 | 进程名（仅本地进程可用） |
| `PROCESS-PATH` | 进程路径 | 进程路径 |
| `PROCESS-NAME-REGEX` / `PROCESS-PATH-REGEX` | 正则 | 进程名 / 路径正则 |
| `PROCESS-NAME-WILDCARD` / `PROCESS-PATH-WILDCARD` | 通配符 | 进程名 / 路径通配 |
| `SOURCE-APP-SIGNING-ID` | 签名 ID | iOS 源 App 签名 ID |
| `SOURCE-APP-TEAM-ID` | Team ID | iOS 源 App Team ID |
| `NETWORK` | `tcp` / `udp` | 网络类型 |
| `UID` | UID 号 | 用户 ID（Linux） |
| `DSCP` | DSCP 值 | DSCP 标记 |
| `REMATCH-NAME` | rematch 名 | 配合 `type: rematch` 出站 |
| `RULE-SET` | provider 名 | 引用 rule-provider |
| `AND` / `OR` / `NOT` | `((类型,参数),(...))` | 逻辑与 / 或 / 非 |
| `SUB-RULE` | 逻辑表达式 | 引用 `sub-rules` 子规则集 |
| `MATCH` | - | 兜底，必须放最后 |

**逻辑规则语法**：`AND,((NETWORK,TCP),(DOMAIN,example.com)),PROXY` —— 每对 `(类型,参数)` 为一项，外层括号包裹所有项；payload 可含逗号。`SUB-RULE` 的 payload 是逻辑表达式，最后一项为 `sub-rules` 的名称。

### rule-providers（规则订阅）

```yaml
rule-providers:
  rule1:
    behavior: classical      # domain / ipcidr / classical（classical=域名+网段）
    interval: 259200         # 更新间隔（秒）
    path: /path/to/save/file.yaml
    type: http               # http / file / inline
    url: "url"
    proxy: DIRECT
    size-limit: 10240        # 下载文件大小限制（KB），0=不限制

  rule2:
    behavior: classical
    type: file
    path: /test.yaml

  rule3:                     # MRS 二进制格式
    type: http
    url: "url"
    format: mrs              # yaml / text / mrs
    behavior: domain         # mrs 仅支持 domain 和 ipcidr
    path: /path/to/save/file.mrs
    path-in-bundle: "geo/geosite/cn.mrs"  # 从 BundleMRS.7z 解压

  rule4:                     # 内联规则
    type: inline
    behavior: domain
    payload:
      - '.blogger.com'
      - '*.*.microsoft.com'
```

**MRS 格式转换**（mihomo 命令行）：
```sh
mihomo convert-ruleset domain yaml XXX.yaml XXX.mrs
mihomo convert-ruleset domain text XXX.text XXX.mrs
mihomo convert-ruleset domain mrs XXX.mrs XXX.text
mihomo convert-ruleset ipcidr yaml XXX.yaml XXX.mrs
```

### sub-rules（子规则集）

```yaml
# 定义子规则集
sub-rules:
  sub-rule-name1:
    - DOMAIN,google.com,ss1
    - DOMAIN,baidu.com,DIRECT
  sub-rule-name2:
    - IP-CIDR,1.1.1.1/32,REJECT
    - IP-CIDR,8.8.8.8/32,ss1
    - DOMAIN,dns.alidns.com,REJECT

# 在 rules 中用 SUB-RULE 引用（分叉匹配）
rules:
  - SUB-RULE,(OR,((NETWORK,TCP),(NETWORK,UDP))),sub-rule-name1
  - SUB-RULE,(AND,((NETWORK,UDP))),sub-rule-name2
```

子规则用逻辑表达式 `(OR,...)` / `(AND,...)` / `(NETWORK,TCP)` 组合条件。

## 策略组（proxy-groups）

```yaml
proxy-groups:
  # url-test：按延迟选最优
  - name: "auto"
    type: url-test
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300            # 健康检查间隔（秒）
    tolerance: 150           # 延迟容忍度（ms），最优节点延迟+tolerance 内视为可用
    lazy: true               # 延迟检查
    expected-status: 204     # 期望状态码，不符则视为不可用

  # fallback：按顺序选第一个可用
  - name: "fallback-auto"
    type: fallback
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  # load-balance：负载均衡
  - name: "load-balance"
    type: load-balance
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300
    strategy: consistent-hashing  # round-robin / consistent-hashing / sticky-sessions

  # select：手动选择
  - name: Proxy
    type: select
    proxies: [ss1, ss2, vmess1, auto, DIRECT, REJECT]
    disable-udp: true        # 禁用 UDP
    default-selected: ss1    # 默认选择节点（空或不存在则选第一个）

  # 引用 proxy-provider（订阅）
  - name: UseProvider
    type: select
    filter: "HK|TW"          # 正则过滤节点名
    use: [provider1]         # 引用 provider 名称
    proxies: [Proxy, DIRECT]
    empty-fallback: COMPATIBLE  # 组为空时的回退（只支持 proxy 名称，不支持代理组）
```

### 策略组类型

| 类型 | 说明 | 特有字段 |
|---|---|---|
| `select` | 手动选择 | `default-selected`, `disable-udp`, `filter`, `use`, `empty-fallback` |
| `url-test` | 延迟测试选优 | `url`, `interval`, `tolerance`, `lazy`, `expected-status` |
| `fallback` | 顺序降级 | `url`, `interval`, `expected-status`, `lazy` |
| `load-balance` | 负载均衡 | `strategy`（round-robin/consistent-hashing/sticky-sessions） |
| `relay` | 中继链 | 按顺序转发，无需健康检查字段 |

### 代理组常见命名约定

| 组名 | 用途 |
|---|---|
| `🌍 全球直连` / `DIRECT` | 直连 |
| `🚀 节点选择` / `Proxy` | 总选择组（包含所有其他组） |
| `🤖 自动选择` / `auto` | url-test 自动选优 |
| `🔯 故障转移` / `fallback` | fallback 自动降级 |
| `🛑 全局拦截` / `REJECT` | 全局拒绝 |

## 导航

| 主题 | 文件 |
|---|---|
| 出站协议（26 种，YAML 字段 + 示例） | [references/proxies.md](references/proxies.md) |
| 入站监听 listeners（18 种） | [references/listeners.md](references/listeners.md) |
| 节点订阅 proxy-providers（含 override-expr yq v4 覆写） | [references/providers.md](references/providers.md) |
| 配置结构定义（RawConfig struct，源码级字段类型与默认值，22 章节） | [references/config-structure.md](references/config-structure.md) |
| Hako 相对 mihomo 的配置增量（48 条偏差规则 + Apple 特化 + 交叉验证记录） | [references/hako-incremental.md](references/hako-incremental.md) |
| **Hako 覆写脚本**（Override Script，JSContext main(config)，过滤非法节点范例 + JSContext 正则坑） | [references/override-script.md](references/override-script.md) |
| **远程更新流程**（更新本技能库时执行） | 见文末「远程更新流程」 |
| TUN 配置 | 见下方 |
| Sniffer 配置 | 见下方 |
| 常用配置模板 | 见下方 |
| 配置文件常见坑 | 见下方 |

规则类型共 **38 种**（含 `AND`/`OR`/`NOT`/`SUB-RULE` 逻辑规则），见「规则配置」章节。

## TUN 配置

```yaml
tun:
  enable: false
  stack: system              # system / gvisor / mixed / mips（gvisor 兼容性最好，mixed 性能最好）
  device:                    # 虚拟网卡名（默认自动生成）
  dns-hijack:
    - 0.0.0.0:53             # DNS 劫持（仅 UDP）
    - any:53                 # 任意地址
  auto-detect-interface: true  # 自动识别出口网卡
  auto-route: true             # 配置路由表
  mtu: 9000                    # 最大传输单元
  gso: false                   # 通用分段卸载，仅 Linux
  gso-max-size: 65536
  auto-redirect: false         # 自动配置 iptables 重定向 TCP，仅 Linux
  auto-redirect-input-mark: 0  # iptables input mark（仅 Linux）
  auto-redirect-output-mark: 0 # iptables output mark（仅 Linux）
  auto-redirect-iproute2-fallback-rule-index: 0  # iproute2 兜底规则索引（仅 Linux）
  iproute2-table-index: 0      # iproute2 路由表索引（仅 Linux）
  iproute2-rule-index: 0       # iproute2 规则索引（仅 Linux）
  loopback-address: []         # 环回地址
  udp-timeout: 0               # UDP 连接超时（秒），0=使用默认值
  icmp-timeout: 0              # ICMP 连接超时（秒）
  strict-route: true           # 防止泄漏，但设备无法被其他设备访问
  disable-icmp-forwarding: true  # 禁用 ICMP 转发
  route-address-set: []        # 从规则集添加防火墙规则，仅 Linux + nftables
  route-exclude-address-set: []
  route-exclude-address:       # 排除路由（配合 auto-route）
    - 192.168.0.0/16
  route-address:               # 自定义路由（启用 auto-route 时）
    - 0.0.0.0/1
    - 128.0.0.0/1
    - "::/1"
    - "8000::/1"
  endpoint-independent-nat: false  # 独立于端点的 NAT
  include-interface: []        # 限制路由的接口（与 exclude-interface 冲突）
  exclude-interface: []        # 排除路由的接口
  include-uid: []              # UID 规则，仅 Linux + auto-route
  include-uid-range: []        # UID 范围
  exclude-uid: []
  exclude-uid-range: []
  include-mac-address: []
  exclude-mac-address: []
  # Android 专属（需 auto-route）
  include-android-user: []
  include-package: []
  exclude-package: []
```

**Apple 平台注意**：Hako 客户端使用 Network Extension（NEPacketTunnelProvider），不使用 tun 配置。tun 仅用于桌面端（FlClash 等）。

## Sniffer 配置（协议嗅探）

```yaml
sniffer:
  enable: false
  force-dns-mapping: false   # 对 redir-host 流量强制嗅探
  parse-pure-ip: false       # 对所有未获取域名的流量强制嗅探
  override-destination: false # 用嗅探结果作为实际访问目标
  sniff:
    QUIC:
      ports: [443]
    TLS:
      ports: [443, 8443]
    HTTP:
      ports: [80, 8080-8880]
      override-destination: true
  force-domain:
    - +.v2ex.com             # 强制嗅探这些域名
  skip-src-address: []       # 跳过嗅探的源 IP
  skip-dst-address: []       # 跳过嗅探的目标 IP
  skip-domain: []            # 跳过嗅探结果的域名
  # 以下已废弃，sniff 配置时生效
  sniffing: [tls, http]
  port-whitelist: ["80", "443", "8000-9999"]
```

## 常用配置模板

### 最小可用配置（仅 HTTP/SOCKS 代理）

```yaml
mixed-port: 7890
allow-lan: false
mode: rule
log-level: info
proxies:
  - name: "node1"
    type: ss
    server: 1.2.3.4
    port: 8388
    cipher: aes-256-gcm
    password: "password"
proxy-groups:
  - name: PROXY
    type: select
    proxies: [node1, DIRECT]
rules:
  - MATCH,PROXY
```

### DNS 推荐配置（fake-ip + 分流）

```yaml
dns:
  enable: true
  listen: 127.0.0.1:553
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  fake-ip-filter:
    - '*.lan'
    - localhost.ptlogin2.qq.com
    - geosite:private
    - geosite:cn
  default-nameserver:
    - 114.114.114.114
    - 223.5.5.5
  nameserver:
    - https://doh.pub/dns-query
    - https://dns.alidns.com/dns-query
  fallback:
    - https://1.1.1.1/dns-query
    - https://dns.google/dns-query
  fallback-filter:
    geoip: true
    geoip-code: CN
    ipcidr:
      - 240.0.0.0/4
  nameserver-policy:
    "+.internal.crop.com": 10.0.0.1
    "geosite:cn,private,apple":
      - https://doh.pub/dns-query
  respect-rules: false
```

### 订阅 + 策略组推荐配置

```yaml
proxy-providers:
  my-sub:
    type: http
    url: "https://example.com/subscribe?sub=1"
    interval: 86400
    path: ./providers/my-sub.yaml
    proxy: DIRECT
    header:
      User-Agent:
        - "Clash/1.0.0"
    health-check:
      enable: true
      interval: 600
      url: https://cp.cloudflare.com/generate_204
    override:
      udp: true
      skip-cert-verify: true
    filter:
      include: "^(?!.*日本|JP).*"   # 排除日本节点
      exclude: "^直连"

proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - 🤖 自动选择
      - 🌍 全球直连
      - 🛑 全局拦截
      - my-sub
    default-selected: 🤖 自动选择
  - name: 🤖 自动选择
    type: url-test
    use: [my-sub]
    url: https://cp.cloudflare.com/generate_204
    interval: 300
    tolerance: 100
  - name: 🌍 全球直连
    type: select
    proxies: [DIRECT, 🚀 节点选择]
  - name: 🛑 全局拦截
    type: select
    proxies: [REJECT, 🚀 节点选择]
  - name: 🌐 自动选择
    type: select
    proxies: [🌍 全球直连, 🤖 自动选择, 🚀 节点选择]

rules:
  - GEOSITE,private,DIRECT
  - GEOSITE,category-ads-all,REJECT
  - GEOSITE,category-ads,REJECT
  - MATCH,🌐 自动选择
```

## 配置文件常见坑

1. **`mode: global` 时 rules 无效** —— 全局模式忽略所有规则
2. **`fake-ip-filter` 默认 blacklist 模式** —— 匹配成功的域名不走 fake-ip（用真实 IP）
3. **`fake-ip-filter-mode: whitelist`** —— 反过来，只有匹配成功才用 fake-ip
4. **`fallback-filter.geoip: true`** —— 依赖 GeoIP 库判断，库不准则 fallback 不生效
5. **`respect-rules: true`** —— 不建议开，DNS 服务器域名本身需要先解析，容易死循环
6. **`dns.default-nameserver` 只能用纯 IP** —— 不能用域名，且必须加密 DNS 支持
7. **`listeners` 里的 `tun`** —— 仅供高级用户，普通用户用顶层 `tun`
8. **`proxy-providers` 的 `path`** —— 默认只能存 mihomo Home Dir，需 `SAFE_PATHS` 环境变量扩展
9. **`proxy-groups` 的 `use` 字段** —— 引用 provider，不是节点列表
10. **`rules` 里 `RULE-SET` 的参数** —— 是 `rule-providers` 的 key 名，不是文件路径

---

## 远程更新流程

用户说「更新 Clash 技能库」/「同步 clash 配置」/「拉取 mihomo 更新」时，**执行本节，不要凭记忆重写**。所有来源都在 GitHub 远程拉取。

### 1. 拉取来源

```bash
cd /var/minis/workspace
# 主来源：完整克隆（必须带完整历史，上游基线 commit 只在历史里）
rm -rf Hako && git clone https://github.com/TokenPLS/Hako.git
git -C Hako rev-list --count HEAD && git -C Hako tag

# 客户端与桥接（可浅克隆）
git clone --depth 1 https://github.com/TokenPLS/Hako-Client.git
git clone --depth 1 https://github.com/TokenPLS/Hako-Adapter.git
```

上游基线 commit `ab405bad`（v1.19.31），也可从 Hako 仓库历史访问。旧基线 `ac017cdd`（v1.19.30）仍在历史中。

### 2. 核对版本

```bash
cd /var/minis/workspace/Hako
git rev-list --count HEAD                                    # commit 数（完整克隆可见，浅克隆受限）
git tag | grep -E '^v1\.19\.30'                              # Hako SDK tag
git show --no-patch --oneline ab405bad   # v1.19.31 上游基线，应为 "feat: support `stack: mips` in tun configuration"
git show --no-patch --oneline ac017cdd   # v1.19.30 旧基线（仍在历史中），应为 "fix: initialize DNS before NTP (#3103)"
git -C ../Hako-Client cat Dependencies.lock.json             # kernel/adapter 锁定 commit
```

对照本文件 front matter 的 `last_sync` 与「数据来源」表；有变化就更新那两处的 HEAD commit 与日期。

### 3. 提取素材

| 文件 | 命令 | 产出章节 |
|---|---|---|
| 出站协议清单 | `git ls-tree --name-only HEAD adapter/outbound/ \| grep '\.go$'` | proxies.md 协议数 |
| 结构体字段 | `sed -n '/type RawConfig struct/,/^}/p' config/config.go \| grep 'yaml:'` | config-structure.md |
| 默认值 | `grep -A40 'DefaultRawConfig' config/config.go` | 默认值列 |
| 规则类型 | `grep -oE '"[A-Z][A-Z0-9-]+"' rules/parser.go \| sort -u` | 规则配置（38 种） |
| Hako 增量 | `git diff --name-only ab405bad HEAD -- bind/hako/` | hako-incremental.md |
| 协议层改动 | `git diff --numstat ab405bad HEAD -- adapter/outbound/` | 判断协议是否被改 |
| 配置参考 | `wc -l docs/config.yaml`（2026-09-24 为 2855 行） | 行数引用 |

上游对照统一用 `git show ab405bad:<path>`、`git grep <pattern> ab405bad -- '*.go'`、`git ls-tree --name-only ab405bad <dir>/`。

### 4. 同步到技能库

```bash
# 技能库路径
ls -la /var/minis/skills/clash-config/ /var/minis/skills/clash-config/references/
```

更新顺序：

1. 重抓 `references/` 下 6 个文件（proxies / listeners / providers / config-structure / hako-incremental / override-script）
2. 回改 SKILL.md：front matter `last_sync` → 概述 → 数据来源表 HEAD commit
3. **数字必须同步**：front matter description、导航表、概述里的计数要一致——2026-09-24 为 27 种出站协议 / 18 种入站监听 / 38 种规则类型
4. 跑第 8 节「常见坑」的核对清单，尤其验证新增/删除的协议与字段

### 5. 已知陷阱

- **`adapter/outbound/` 目录数 ≠ 协议数**：目录数含 `base.go`/`util*.go`/`*_stub.go`/`*_test.go` 与已废弃实现，实际可用协议少于此数
- **`docs/config.yaml` 里的类型可能多于内核支持**：以 `adapter/outbound/*.go` + `adapter/parser.go` 为准
- **`git clone MetaCubeX/mihomo` 必失败**：仓库被替换，见第 1 节
- **上游 tag**：Hako tag 为 `v1.19.30-hako.1` / `v1.19.30-hako.2` / `v1.19.31-hako.1`
- **默认值要看 `config.go` 的 `DefaultRawConfig`**，不要从 `docs/config.yaml` 的示例反推——文档里写的是推荐值不是内核默认（例：`tun.mtu` 上游默认为 0，文档示例写的是 1500 量级）
- **协议层几乎不动**：Hako 对 `adapter/outbound/` 历史零改动，唯一新增 `physical_packet.go`；写增量时不要把已有协议误判为 Hako 新增
- **`bind/hako/` 才是 Hako 独有层**：`upstream_defaults.go` 会导出上游 `DefaultRawConfig`，可直接用来回答「上游默认值是什么」，比反查文档可靠

### 6. 交付前检查

- [ ] `git rev-list --count HEAD` 与文档记录的 commit 数对得上，或已更新
- [ ] `ab405bad` 仍可 `git show` 到，说明上游基线 v1.19.31 没丢
- [ ] SKILL.md front matter `last_sync` 已是当天
- [ ] 4 个数字（协议/监听/规则/偏差）在 3 处一致
- [ ] 「我不确定的地方」里的推断项已尽量用上游对照消除（能验证就别留推断）
