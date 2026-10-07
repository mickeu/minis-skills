---
name: Egern
description: Egern 网络工具知识库（中英双语完整官方文档 38 页）。涵盖代理协议（15种）、规则系统（20+规则类型）、7种策略组（select/auto_test/smart/fallback/load_balance/external/conditional）、DNS、URL/Header/Body重写、HTTP抓包、5种脚本类型、模块系统、小组件DSL、JavaScript API、URL Scheme、FAQ、完整配置示例等。来源：egernapp.com/docs/ + doc.egernapp.com/zh-CN/docs/ 官方完整版
source_url: https://doc.egernapp.com/zh-CN/docs/intro（中文）+ https://egernapp.com/docs/intro（英文）
license: Proprietary
last_sync: 2026-10-01
---
# Egern 知识库

## 语言约定（2026-08-31 用户明确，全局适用）
- **所有分析、说明、回复一律使用简体中文**（含技术分析、配置解释、报错定位等）。
- 配置/脚本/命令里的技术名词（英文标识符、域名、参数名）保持原样，说明性文字用中文。
- 涉及设备/App 界面语言按"跟系统语言走"处理，不算配置问题。
- 本条与 GLOBAL.md「语言约定」一致，为通用回复规则，适用所有任务与技能。

> 当前版本：**v2.21.0（788）**（TestFlight，2026-09-18）
> 价格：$5.99 买断（App Store），Pro 内购可选
> 📁 **完整官方文档（中英双语 38 页/275KB）已保存至 `/var/minis/skills/egern/docs/`**

# Egern 完整知识库

> 来源：egernapp.com/docs/ + doc.egernapp.com/zh-CN/docs/ 官方完整版（38页）
> 当前版本：**v2.21.0（788）**（TestFlight，2026-09-18）
> 价格：$5.99 买断（App Store），Pro 内购可选

### 📌 文档来源与更新检查（2026-10-01 确认）
- **中文文档站**：`https://doc.egernapp.com/zh-CN/docs/`（Docusaurus），入口页 `.../zh-CN/docs/intro`
- **英文文档站**：`https://egernapp.com/docs/`，入口页 `.../docs/intro`
- **页面清单**：`https://doc.egernapp.com/sitemap.xml`（英文，所有 loc 指向 egernapp.com）和 `https://doc.egernapp.com/zh-CN/sitemap.xml`（中文）
- 无公开 GitHub 仓库，检查更新 = 抓 sitemap 对比技能库 `docs/` 文件列表 + 核对官网最新版本号/更新日志
- 首页/根路径是 App Store 落地页，不直接显示版本信息

---

# 版本历史

## v2.21.0（788）— TestFlight（2026-09-18）

### 新功能

- **虚拟接口回流地址设置页**：填入 IPv4 地址后，设备可通过这些地址访问运行在本机上的服务。为依赖 StosVPN 约定（10.7.0.1）的 App 提供支持，开启后隧道会自动切换为纯 IPv4。
- **连接详情新增「代理服务器」一栏**：显示本次连接实际握手的代理地址与端口，并标注其归属地（地理位置）。
- **通知历史的来源筛选改为多选**：可同时保留多个来源，也可一键隐藏被拦截的通知；筛选条件会被记住，下次进入时保持不变。
- **DNS 的 `proxy_nameservers` 可直接填写上游分组名**：只填一个分组时，代理域名解析会走该分组并被缓存，在 DNS 页面以你自己起的名字显示健康状态。
- **gRPC 传输按线路复用同一条 HTTP/2 连接**：握手只做一次，避免并行下载时多条连接各自占用窗口缓冲的问题。

### 改进

- **大幅减少 App 在 iPhone 备份中占用的空间**：抓包记录、缓存、编译后的规则和 GeoIP 数据库不再写入 iCloud 备份，这些内容重启后都会自动重建。
- **被拦截的通知现在也会显示时间**，拦截状态改用铃铛图标标注在时间旁边，列表不再出现没有时间的行。

### 修复

- 修复对没有 SNI 的连接进行 HTTPS 解密时，按目标 IP 签发的证书不被客户端接受的问题。

---

## v2.21.0（785）— TestFlight（2026-08-03）

### 新功能

- **脚本运行时长不再限制**：超时时间可设为任意秒数，设为0或-1表示不限时，长时间运行的定时任务也可正常执行

### 修复

- 修复部分 REALITY 节点无法正常连接的问题
- 修复开启「排除路由 0.0.0.0/31」后切换网络，系统与 App 仍判定为蜂窝网络的问题
- 修复图标集点击「更新」后仍显示旧图标，需手动清理缓存才能更新的问题
- 修复通过 HTTP 本地代理访问 IPv6 地址（如 `https://[2400::1]:9999`）时，目标地址可能解析错误的问题

---

## v2.20.0（780）— App Store 发布（2026-07-24）

### 新功能

- **Snell 代理协议**（v1–v5）：支持连接复用池、obfs 混淆与 ShadowTLS，可解析 Clash（`type: snell`）与 Surge 配置
- **SSH 出站代理**：支持密码/私钥认证与 host key 校验
- **SOCKS5 over TLS** 协议
- **VMess / VLESS 新增 gRPC（Gun）传输**，针对高延迟链路优化下载速度
- **Trojan、AnyTLS、HTTPS 新增 REALITY 支持**，含 X25519MLKEM768 抗量子密钥交换，可从分享链接与 Clash 订阅导入
- **服务器证书 SHA-256 指纹固定**，支持 Trojan、AnyTLS、HTTPS、Hysteria2、TUIC 及 VMess（HTTP/2、TLS、WSS）
- **所有策略组类型均可直接挂载订阅链接**：静态节点与订阅节点写在同一组即可，无需再单独建外部策略组
- **负载均衡新增轮询（Round-Robin）算法**
- **节点级 IP 版本策略（`ip_version`）**：域名服务器可选双栈、仅 IPv4 / 仅 IPv6、IPv4 / IPv6 优先
- **策略切换时关闭连接**：策略组选中节点变化时自动关闭仍在使用旧节点的连接
- **监听端口规则**：可按本地 HTTP/SOCKS 代理端口分流
- **DNS over TCP** 支持，可通过 `tcp://` 配置上游
- **配置历史**：每次编辑、更新或覆盖前自动保存快照，可预览并一键恢复
- **全新「存储」页面**：完整展示缓存、日志、流量记录、GeoIP 数据库、脚本数据等占用情况
- **通知历史**：所有通知自动记录（含被屏蔽或已自动消失的），可在「设置 → 通知」中查看
- **连接列表深度链接**：详情页支持实时刷新，`egern:///connections` 与 `egern:///connections/<连接ID>`
- **连接详情可查看 IP 信息**及命中的 MITM 规则与所属模块
- **小组件新增 SVG 矢量图渲染**支持
- **支持将 MITM CA 证书安装到其他设备**

### 改进

- **Smart 策略组**记住真实连接中的失败：测速正常但实际不可用的节点自动降权，故障切换后立即重新测速
- Hysteria2 支持 TCP Fast Open；AnyTLS 支持跳过 TLS 证书验证
- 无网络（如飞行模式）时立即拒绝请求，不再反复重试导致发热耗电
- 提升脚本并发发起 HTTP 请求的能力，突破 WebView 每主机约 6 条连接的限制
- 配置错误提示直接指出出错字段与原因，不再只显示不准确的行号
- 日志支持搜索；DNS 转发规则集可预览 YAML 与原始文本；长按模块可自定义图标
- 复用的 HTTP 连接也会显示策略、规则和 IP 信息；流量改用二进制单位（KiB/MiB）显示

### 修复

- 修复部分代理协议下上传大文件卡住，以及节点域名对应多个 IP 时无法回退到可用 IP 的问题
- 修复配置改动及手动更新资源后不立即生效的问题
- 修复 DNS 劫持误将非 DNS 的 UDP 流量（如 SNTP）当作 DNS 处理的问题
- 修复逻辑规则（AND/OR/NOT）包含不支持的子规则时匹配所有流量的问题，此类规则现在会被整体忽略
- 修复 Hysteria2 跳过证书验证不生效、Hysteria2 / TUIC 测速偶发误判失败、HTTP 类节点延迟偏高的问题
- 修复 Clash 订阅中 VLESS `encryption: none` 节点被丢弃、VLESS / VMess 链接被错误识别的问题
- 修复 INI `#!arguments` 裸键被丢弃、YAML 模块参数替换无法处理数字字段占位符的问题
- 修复切换网络后 IPv6 可用性未及时更新的问题
- 修复连接页协议、策略与失败筛选不准确的问题
- 修复更新间隔、超时等字段填入超大数值时被静默忽略，YAML 配置甚至整体解析错乱的问题
- 修复对域名节点查看 IP 信息时绕过代理 DNS、延迟标签文字截断、键盘弹出时切后台再返回后编辑器底部出现空白的问题

---

# Egern 完整配置示例大全

## 代理协议 (Proxies)

```yaml
shadowsocks:
  name: "my-ss"
  method: "aes-256-gcm"
  password: "mypassword"
  server: "1.2.3.4"
  port: 8388
  tfo: true
  udp_relay: false
  obfs: "http"
  obfs_host: "example.com"
  obfs_uri: "/path"

snell:
  name: "my-snell"
  server: "1.2.3.4"
  port: 8388
  psk: "mypassword"
  version: 4
  udp_relay: true
  obfs: "http"
  obfs_host: "example.com"

trojan:
  name: "my-trojan"
  server: "trojan.example.com"
  port: 443
  password: "trojanpass"
  sni: "trojan.example.com"
  skip_tls_verify: true
  udp_relay: true

anytls:
  name: "my-anytls"
  server: "anytls.example.com"
  port: 443
  password: "mypassword"
  sni: "anytls.example.com"
  udp_relay: true

hysteria2:
  name: "my-hysteria2"
  server: "hysteria.example.com"
  port: 443
  auth: "my_auth_token"
  sni: "hysteria.example.com"
  obfs: "salamander"
  obfs_password: "myobfspass"
  skip_tls_verify: true
  bandwidth: 100

tuic:
  name: "my-tuic"
  server: "tuic.example.com"
  port: 443
  uuid: "22222222-2222-2222-2222-222222222222"
  password: "tuicpass"
  udp_relay_mode: "native"
  alpn: ["h3"]

socks5:
  name: "my-socks5"
  server: "1.2.3.4"
  port: 1080
  username: "user"
  password: "pass"

socks5_tls:
  name: "my-socks5-tls"
  server: "1.2.3.4"
  port: 443
  sni: "example.com"

ssh:
  name: "my-ssh"
  server: "1.2.3.4"
  port: 22
  username: "root"
  private_key: "base64key"
  private_key_password: "passphrase"

http:
  name: "my-http"
  server: "1.2.3.4"
  port: 443
  username: "user"
  password: "pass"

https:
  name: "my-https"
  server: "1.2.3.4"
  port: 443
  username: "user"
  password: "pass"

vmess:
  name: "my-vmess"
  server: "127.0.0.1"
  port: 443
  user_id: "uuid"
  security: "auto"
  transport:
    wss:
      path: "/ws"
      sni: "www.bing.com"

vless:
  name: "my-vless"
  server: "127.0.0.1"
  port: 443
  user_id: "uuid"
  transport:
    wss:
      path: "/ws"
      sni: "www.bing.com"

wireguard:
  name: "my-wireguard"
  server: "engage.cloudflareclient.com"
  port: 2408
  private_key: "base64_private_key"
  peer_public_key: "base64_public_key"
  local_ipv4: "172.16.0.2/32"
  reserved: [1, 2, 3]
```

## 策略组 (Policy Groups)

```yaml
policy_groups:
  - select:
      name: "手动选择"
      policies: [节点1, 节点2, DIRECT, REJECT]
      flatten: true
      filter: "(?i)香港|HK"
      icon: "globe"

  - auto_test:
      name: "自动选择"
      policies: [节点1, 节点2]
      interval: 600
      tolerance: 100
      timeout: 5

  - smart:
      name: "智能选优"
      policies: [HK Premium, HK Standard, 日本节点]
      priorities:
        "^HK Premium$": 0.8
        "(?i)HK": 0.9
        "JP|日本": 1.2

  - fallback:
      name: "故障转移"
      policies: [主节点, 备用节点1, 备用节点2]
      interval: 600
      timeout: 5

  - load_balance:
      name: "负载均衡"
      policies: [节点1, 节点2, 节点3]
      algorithm: "round_robin"

  - external:
      name: "机场订阅"
      type: auto_test
      urls:
        - "https://provider1.com/subscribe"
        - "https://provider2.com/subscribe"
      filter: "(?i)香港|日本|HK|JP"
      update_interval: 86400

  - conditional:
      name: "网络环境"
      rules:
        - ssid: { match: "Home-*", policy: DIRECT }
        - bssid: { match: "aa:bb:cc:*", policy: 香港节点 }
        - cellular: { match: "LTE", policy: 自动选择 }
      default_policy: 手动选择
```

## 规则 (Rules)

```yaml
rules:
  - domain: { match: "www.google.com", policy: Proxy }
  - domain_suffix: { match: "google.com", policy: Proxy }
  - domain_keyword: { match: "google", policy: Proxy }
  - domain_regex: { match: "^ads?\\.", policy: REJECT }
  - domain_wildcard: { match: "*.google.*", policy: Proxy }
  - geoip: { match: CN, policy: DIRECT, no_resolve: true }
  - ip_cidr: { match: "192.168.0.0/16", policy: DIRECT }
  - ip_cidr6: { match: "::1/128", policy: DIRECT }
  - asn: { match: "AS13335", policy: Proxy }
  - url_regex: { match: "^https://.*\\.google\\.com/", policy: Proxy }
  - user_agent: { match: "*Chrome*", policy: Proxy }
  - dest_port: { match: "80,443,8000-9000", policy: Proxy }
  - protocol: { match: udp, policy: DIRECT }
  - rule_set: { match: "https://example.com/rules.yaml", policy: Proxy, update_interval: 86400 }
  - ssid: { match: "Home-WiFi", policy: DIRECT }
  - bssid: { match: "aa:bb:cc:dd:ee:ff", policy: Proxy }
  - cellular: { match: "LTE", policy: 自动选择 }
  - and:
      match:
        - domain_suffix: { match: "example.com" }
        - dest_port: { match: "443" }
      policy: Proxy
  - default: { policy: DIRECT }
```

## DNS 配置

```yaml
dns:
  bootstrap:
    - system
    - 223.5.5.5
  upstreams:
    google:
      - https://8.8.8.8/dns-query
    adguard:
      - quic://dns.adguard-dns.com
  forward:
    - domain: { match: "internal.example.com", value: "192.168.1.1" }
    - domain_suffix: { match: "cn", value: bootstrap }
    - domain_regex: { match: "^ad\\..*", value: reject }
    - domain_wildcard: { match: "*", value: google }
  hosts:
    "*.google.com": "142.250.80.46"
  proxy_nameservers:
    - tls://dns.google
  block_ips:
    - 0.0.0.0
    - 127.0.0.1
```

## 脚本 (Scriptings)

```yaml
scriptings:
  - http_request:
      name: "修改请求头"
      match: "^https://api\\.example\\.com/"
      script_url: "https://example.com/scripts/modify-header.js"
      timeout: 30
      body_required: true

  - http_response:
      name: "解析响应"
      match: "^https://api\\.example\\.com/data"
      script_url: "https://example.com/scripts/parse-response.js"
      body_required: true

  - schedule:
      name: "每日签到"
      cron: "0 8 * * *"
      script_url: "https://example.com/scripts/daily-checkin.js"

  - generic:
      name: "server-status"
      script_url: "https://example.com/scripts/server-status.js"

  - network:
      name: "网络切换通知"
      script_url: "https://example.com/scripts/network-change.js"
      timeout: 30
```

## 小组件 (Widgets)

```javascript
export default async function (ctx) {
  return {
    type: 'widget',
    children: [
      {
        type: 'text',
        text: 'Hello, Widget!',
        font: { size: 'title2', weight: 'bold' },
        textColor: '#FFFFFF',
      }
    ],
    backgroundColor: '#2D6A4F',
    padding: 16,
  };
}
```

### 小组件 DSL 组件

```json
{
  "type": "widget",
  "children": [
    { "type": "text", "text": "标题", "font": { "size": "title" } },
    { "type": "stack", "direction": "row", "children": [
        { "type": "text", "text": "标签" },
        { "type": "spacer" },
        { "type": "text", "text": "值" }
    ]},
    { "type": "date", "date": "2024-01-01T00:00:00Z" },
    { "type": "image", "image": "globe" }
  ],
  "backgroundColor": "#1A1A2E",
  "gap": 8,
  "padding": 16,
  "refreshAfter": "2024-01-01T01:00:00Z"
}
```

## URL 重写

```yaml
url_rewrites:
  - match: "(.*google)\\.cn"
    location: "$1.com"
    status_code: 307
  - match: "^https://ads\\.example\\.com"
    location: "http://reject-dict/"
```

## HTTP 头部重写

```yaml
header_rewrites:
  - add:
      match: "^https://example\\.com"
      name: "X-Custom-Header"
      value: "custom-value"
      type: request
  - delete:
      match: ".*"
      name: "X-Tracking-Id"
      type: request
```

## HTTP 消息体重写

```yaml
body_rewrites:
  - response_regex:
      match: "^https://api\\.example\\.com/data"
      find: '"status":\s*"pending"'
      replace: '"status": "completed"'
  - response_jq:
      match: "^https://api\\.example\\.com/config"
      filter: '.settings.theme = "dark"'
```

## HTTP 抓包

```yaml
http_captures:
  - "*.example.com"
  - "test.com"
```

## 模块

```yaml
modules:
  - name: "广告过滤"
    url: "https://example.com/adblock.yaml"
    enabled: true
    update_interval: 86400
    compat_arguments:
      API_KEY: "your_api_key"
    env:
      REFRESH_INTERVAL: "300"
```
---

# 官方文档完整内容

## Configuration Proxies

Proxies | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Configuration for proxies, supporting the following protocols:
Shadowsocks
,
Snell
,
Trojan
,
AnyTLS
,
Hysteria2
,
TUIC
,
SOCKS5
,
SOCKS5 over TLS
,
SSH
,
HTTP
,
HTTPS
,
Vmess
,
Vless
,
WireGuard
. All optional fields of type
bool
default to
false
.
Shadowsocks
​
name
(string), Required
The proxy name, which must be globally unique.
method
(string), Required
Encryption method.
AEAD-2022:
2022-blake3-aes-128-gcm
,
2022-blake3-aes-256-gcm
,
2022-blake3-chacha20-poly1305
AEAD:
chacha20-poly1305
,
aes-256-gcm
,
aes-128-gcm
Stream:
none
,
table
,
rc4
,
rc4-md5
,
aes-128-cfb
,
aes-192-cfb
,
aes-256-cfb
,
aes-128-ctr
,
aes-192-ctr
,
aes-256-ctr
,
bf-cfb
,
camellia-128-cfb
,
camellia-192-cfb
,
camellia-256-cfb
,
cast5-cfb
,
des-cfb
,
idea-cfb
,
rc2-cfb
,
seed-cfb
,
salsa20
,
chacha20
,
chacha20-ietf
password
(string), Required
The password. Shadowsocks 2022 uses a Base64-encoded key.
server
(string), Required
The server address, which can be an IP or domain name.
port
(integer), Required
The server port.
udp_port
(integer), Optional
Dedicated UDP port. Used when the server listens on different ports for TCP and UDP.
tfo
(bool), Optional
Whether to enable TCP Fast Open.
udp_relay
(bool), Optional
Whether to enable UDP relay.
obfs
(string), Optional
Obfuscation method. Possible values:
http
,
tls
.
obfs_host
(string), Optional
The hostname used for obfuscation.
obfs_uri
(string), Optional
The URI path used for obfuscation.
block_quic
(bool), Optional
Whether to block the QUIC protocol. When set to
true
, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global
block_quic
. When not set, the policy group and global settings are used in order; if none are set, Shadowsocks defaults to
false
(allow QUIC).
shadow_tls
(object), Optional
ShadowTLS transport configuration. See
ShadowTLS
for details.
prev_hop
(string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
ip_version
(string), Optional
IP version strategy applied when
server
is a domain that requires DNS resolution; it has no effect on an IP-literal
server
. One of
dual_stack
(default),
v4_only
,
v6_only
,
v4_prefer
,
v6_prefer
.
Configuration Example
​
shadowsocks
:
name
:
"my-ss"
method
:
"aes-256-gcm"
password
:
"mypassword"
server
:
"1.2.3.4"
port
:
8388
tfo
:
true
udp_relay
:
false
obfs
:
"http"
obfs_host
:
"example.com"
obfs_uri
:

---

## Configuration Policy Groups

# Policy Groups
Policy groups are used to organize and manage multiple proxy nodes, determining which node to use based on different selection strategies. Policy groups can contain proxy servers, other policy groups, or built-in policies.
Supported policy group types: select (manual selection), auto_test (automatic latency test), smart (smart selection), fallback (failover), load_balance (load balancing), external (external resource), conditional (conditional selection).
Built-in policies: DIRECT (direct connection), REJECT (reject connection).
## Common Fields
The following fields are common to all policy group types (except conditional):
- **name** (string, required): Policy group name, must be globally unique.
- **policies** (string array, required): List of sub-policies. Can be proxy server names, other policy group names, or built-in policies (DIRECT, REJECT).
- **flatten** (bool, optional): Expand all proxy nodes from nested policy groups. When set to true, nodes within sub-policy groups are fully expanded rather than showing only the policy group name. Often used in conjunction with filter.
- **filter** (string, optional): A regular expression filter that retains only nodes whose names match. Commonly used with flatten to filter specific nodes from subscriptions, e.g., (?i)香港|HK.
- **block_quic** (bool, optional): Block the QUIC protocol. Takes priority over the global block_quic, but is overridden by the proxy's own block_quic setting.
- **icon** (string, optional): Icon, supports SF Symbols names or icon URLs.
- **hidden** (bool, optional): Whether to hide this policy group in the UI.
- **prev_hop** (string, optional): Previous hop proxy, used to build proxy chains. Traffic path: local device → previous hop proxy → current node → destination.
- **latency_test_url** (string, optional): Per-group latency test / health check URL. Takes precedence over the global settings.
## Manual Selection (select)
The user manually selects which sub-policy to use. Uses only the common fields, no additional fields.
## Auto Test (auto_test)
Periodically tests the latency of all sub-policies and automatically selects the node with the lowest latency.
Additional fields:
- **interval** (integer, optional): Latency test interval in seconds, default 600. Set to 0 or negative to disable.
- **tolerance** (integer, optional): Switch tolerance in milliseconds, default 100. A switch occurs only when the new node's latency is faster than the current node by more than this value.
- **timeout** (integer, optional): Timeout for a single node's latency test in seconds, default 5, maximum 60.
## Smart Selection (smart)
Continuously learns the health of each candidate node across probe rounds and picks the most robust one based on a combined score of latency, jitter, and reliability. Runtime failures are also fed back to the health profile so subsequent selections automatically avoid recently unstable nodes.
**Differences from auto_test:**
- Not misled by single-round noise — abnormal samples are smoothed out by EWMA
- Avoids "low latency but unstable" nodes — success rate is part of the ranking
- Switches with hysteresis — a candidate must be sufficiently cheaper than the current node and the minimum dwell time must have elapsed
- Adaptive probe cadence — the probe interval lengthens when stable and shortens after a switch or failure
Additional fields:
- **priorities** (object, optional): Sub-policy priority coefficients. Keys are regular expressions matched against sub-policy names; values are coefficients multiplied onto the candidate's health score:
1 lowers priority, 0 always picks this candidate first.
## Fallback (fallback)
Tries sub-policies in order and selects the first available node. When a higher-priority node becomes available again, it automatically switches back.
Additional fields:
- **interval** (integer, optional): Health check interval in seconds, default 600.
- **timeout** (integer, optional): Timeout for a single node's health check in seconds, default 5, maximum 60.
## Load Balance (load_balance)
Distributes traffic across multiple sub-policies. By default, connections to the same domain/IP are assigned to the same node (hash mode).
Additional fields:
- **algorithm** (string, optional): Load balancing algorithm. `hash` (default) — hash by destination; `round_robin` — rotation.
## External Resource (external)
Loads a list of proxy nodes from a remote URL, supporting airport subscription links.
Additional fields:
- **type** (string, required): Selection strategy: select, auto_test, smart, fallback, load_balance.
- **urls** (string array, required): List of subscription URLs.
- **filter** (string, optional): Regex filter for node names.
- **update_interval** (integer, optional): Subscription update interval in seconds, default 86400 (24 hours).
## Conditional Selection (conditional)
Automatically selects a sub-policy based on the current network environment (Wi-Fi SSID, BSSID, cellular network type). Rules are matched in order.
- **rules** (array, required): List of matching rules. Three rule types:
- `ssid` - Wi-Fi name matching, supports glob wildcards
- `bssid` - Wi-Fi router MAC address matching, supports glob wildcards
- `cellular` - Cellular network type matching
- **default_policy** (string, required): Default policy when no rule matches.

---

## Configuration Rules

Rules | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Egern supports multiple types of rules that can be used to control the proxy behavior of network traffic and to block certain traffic. Rules are matched in the order they appear in the configuration; once a rule matches, subsequent rules are no longer evaluated.
Supported Rules
​
Domain Rules
​
Type
Name
Description
domain
Exact Domain Match
Matches the domain exactly
domain_suffix
Domain Suffix Match
Matches domains by suffix, automatically handling subdomain boundaries (e.g.,
google.com
matches
www.google.com
but not
fakegoogle.com
)
domain_keyword
Domain Keyword Match
Matches domains containing the specified keyword
domain_regex
Domain Regex Match
Matches domains using regular expressions
domain_wildcard
Domain Wildcard Match
Matches domains using glob patterns, case-insensitive (e.g.,
*.google.*
)
IP Rules
​
Type
Name
Description
geoip
GeoIP Match
Matches IP addresses based on ISO 3166-1 alpha-2 country/region codes (e.g.,
CN
,
US
)
ip_cidr
IPv4 Range Match
Matches the specified IPv4 CIDR range
ip_cidr6
IPv6 Range Match
Matches the specified IPv6 CIDR range
asn
ASN Match
Matches ASN numbers or organization names (e.g.,
13335
,
AS13335
,
Telegram Messenger Inc
)
Other Rules
​
Type
Name
Description
url_regex
URL Regex Match
Matches the full URL using regular expressions (HTTP/HTTPS traffic only)
user_agent
User-Agent Match
Matches the User-Agent header using glob patterns, case-insensitive (HTTP/HTTPS traffic only)
dest_port
Destination Port Match
Matches the destination port; supports single ports, ranges, and mixed formats (e.g.,
80,443,8000-9000
)
protocol
Protocol Match
Matches the protocol type:
tcp
,
udp
,
http
,
https
,
quic
,
stun
rule_set
Rule Set
References a local or remote rule set file, allowing multiple rules to be bundled for reuse
Network Environment Rules
​
Type
Name
Description
ssid
Wi-Fi SSID Match
Matches the current Wi-Fi name using glob patterns, case-insensitive
bssid
Wi-Fi BSSID Match
Matches the MAC address of the current Wi-Fi access point using glob patterns
cellular
Cellular Network Match
Matches the cellular network type using glob patterns (e.g.,
NR
,
LTE
,
WCDMA
)
Logical Rules
​
Type
Name
Description
and
Logical AND
Matches when all sub-conditions are satisfied
or
Logical OR
Matches when any sub-condition is satisfied
not
Logical NOT
Matches when the sub-condition is not satisfied
Default Rule
​
Type
Name
Description
default
Default Rule
A fallback rule that matches all traffic not matched by any other rule
Rule Fields
​
match
(string), required
The value to match.
policy
(string), required
The policy name. Determines how matched traffic should be handled.
DIRECT
means direct connection,
REJECT
means the connection is refused. You can also use the name of a proxy server or policy group.
name
(string), optional
The rule name, used for logging and debugging.
no_resolve
(bool), optional
Applicable only to IP-based rules (geoip, ip_cidr, ip_cidr6, asn). When set to
true
, the rule only matches already-resolved IP addresses and will not trigger DNS resolution.
disabled
(bool), optional
Whether to disable this rule.
Configuration Example
​
rules
:
-
domain
:
match
:
www.google.com
policy
:
Proxy
-
domain_keyword
:
match
:
google
policy
:
Proxy
-
domain_suffix
:
match
:
google.com
policy
:
Proxy
-
domain_regex
:
match
:
"^ads?\\."
policy
:

---

## Configuration Dns

DNS | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Egern's DNS subsystem supports multiple protocols (UDP, DoT, DoH, DoQ, DoH3) and lets you route different domains to different upstream DNS groups via Forward rules. Egern has two internal resolution paths:
Default DNS
: resolves domain names for user traffic. Goes through Forward rules and falls back to Bootstrap on no-match. Connections to upstreams follow the proxy rules.
Proxy DNS
: used by proxy servers to resolve destination domains. Connections to upstreams are forced to be direct, avoiding a DNS → proxy → DNS dependency loop. When
proxy_nameservers
is configured, every proxy-DNS query is forced through that list (
Forward rules are bypassed
); when unset, the proxy DNS shares the Forward rules with the default DNS and falls back to Bootstrap on no-match.
Resolution Flow
​
Each query goes through these stages in order:
Hosts
: if a local mapping matches, return the IP directly, or continue resolving the mapped domain as an alias.
Forward
: rules are evaluated in order; the first matching rule selects the upstream. SSID/BSSID/Cellular rules depend on current network state, and the matching cache is cleared when the network changes. The proxy DNS skips this stage entirely when
proxy_nameservers
is configured — every query goes straight to that list.
Default upstream
: used when no Forward rule matches — the default DNS falls back to Bootstrap; the proxy DNS also falls back to Bootstrap when
proxy_nameservers
is not configured.
Block IPs
: records in the response matching
block_ips
are filtered out; if all records are filtered, the resolution is treated as failed.
Bootstrap (Startup DNS)
​
bootstrap
configures the DNS servers used during startup. It only supports plain UDP (port 53) and never goes through proxy rules — traffic is always direct. It serves two purposes:
Resolve the hostnames of encrypted DNS servers in
upstreams
(
tls://
,
https://
, etc.).
Act as the final DNS fallback (see "Resolution Flow" above).
Supported values:
An IP or
IP:port
, e.g.
1.1.1.1
,
8.8.8.8:53
.
The special value
system
, which merges in system DNS servers (the ones provisioned by Wi-Fi/cellular).
If unset or unparsable, Egern automatically falls back to the system DNS servers.
dns
:
bootstrap
:
-
system
# merge system DNS
-
223.5.5.5
# plus a custom server
Upstreams (DNS Server Groups)
​
Defines named groups of encrypted DNS servers, referenced by Forward rules via the group name. Servers within a group race in parallel; the fastest response wins.
Supported server formats:
Format
Protocol
Default Port
1.1.1.1
or
1.1.1.1:53
Plain UDP
53
udp://1.1.1.1
Plain UDP
53
tls://1.1.1.1
DNS over TLS
853
https://8.8.8.8/dns-query
DNS over HTTPS
443
quic://dns.adguard-dns.com
DNS over QUIC
853
h3://dns.example.com/dns-query
DNS over HTTP/3
443
bootstrap
Expands to all Bootstrap servers
—
system
Expands to all system DNS servers
—
A Forward rule's
value
may reference a group name from
upstreams
. The default DNS always honors Forward rules, so it can use any of these groups; the proxy DNS only reaches them via Forward when
proxy_nameservers
is unset (Forward is skipped once
proxy_nameservers
is configured).
dns
:
upstreams
:
google
:
-
https
:
//8.8.8.8/dns
-
query
-
https
:
//8.8.4.4/dns
-
query
adguard
:
-
quic
:
//dns.adguard
-
dns.com
Forward (DNS Forwarding Rules)
​
Rules are evaluated in declaration order; the first matching rule routes the query to its upstream. The default DNS always uses these rules; the proxy DNS only goes through Forward when
proxy_nameservers
is unset (otherwise it bypasses Forward and goes straight to
proxy_nameservers
).
Supported match types:
Type
Description
domain
Exact match on the full domain
domain_keyword
Substring match on the domain
domain_suffix
Suffix match aligned on
.
boundaries:
match: cn
matches
cn
and
example.cn
, but not
examplecn
domain_wildcard
Glob pattern (
*
/
?
), case-insensitive. e.g.
*.google.com
domain_regex
PCRE2 regex,
find
-style — any substring hit counts
proxy_rule_set
Reference to a precompiled remote rule set
ssid
Glob match against the current Wi-Fi SSID
bssid
Glob match against the current Wi-Fi BSSID
cellular
Glob match against the current cellular radio type, e.g.
LTE
,
NR
Fields per rule:
match
(string), required
The match condition; semantics depend on the rule type.
value
(string), required
The target upstream. May be:
A group name defined in
upstreams
.
A single DNS server address, e.g.
tls://1.1.1.1
(an implicit upstream — equivalent to a group containing just that one address).
The special value
bootstrap
— use the Bootstrap DNS.
The special value
system
— use the system DNS.
The special value

---

## Configuration Url Rewrites

# URL Rewriting
The URL rewriting feature supports three modes:
- **Redirect mode**: Returns an HTTP 3xx redirect response. The client is aware of the redirect and initiates a new request.
- **Header mode**: Directly modifies the request URI and Host header, transparently forwarding the request to the new address without the client's awareness.
- **Reject mode**: Directly returns a specific response body to block the request, commonly used for ad filtering.
> Rewriting the URL of HTTPS requests requires configuring MITM and installing a CA certificate.
## Fields
- **match** (string, required): A regular expression for URL matching, which matches the full request URL (including protocol, hostname, path, and query parameters). Capture groups are supported.
- **location** (string, required): The redirect target URL. Supports referencing capture groups with $1, $2, etc. Special values for reject mode:
- `http://reject/` — returns a 404 empty response
- `http://reject-200/` — returns a 200 empty response
- `http://reject-dict/` — returns an empty JSON object {}
- `http://reject-array/` — returns an empty JSON array []
- `http://reject-img/` — returns a 1×1 transparent GIF
- `http://reject-video/` — returns an empty MP4
- **status_code** (integer, optional): The HTTP redirect status code (301, 302, 307, 308). When omitted, header mode is used.
- **disabled** (bool, optional): Whether to disable this rule.
## Examples
```yaml
url_rewrites:
# Redirect mode: returns a 307 redirect response
- match: "(.*google)\\.cn"
location: "$1.com"
status_code: 307
# Redirect mode: returns a 301 permanent redirect
- match: "^https://old\\.example\\.com/(.*)$"
location: "https://new.example.com/$1"
status_code: 301
# Header mode: transparent forwarding, client unaware
- match: "^https://api\\.example\\.com/v1/(.*)$"
location: "https://api.example.com/v2/$1"
# Reject mode: block ad requests, return an empty JSON object
- match: "^https://ads\\.example\\.com"
location: "http://reject-dict/"
```

---

## Configuration Header Rewrites

# HTTP Header Rewriting
The HTTP header rewriting feature allows users to add, replace, or delete headers in HTTP requests or responses that match specific URLs. MITM decryption is required to modify HTTPS traffic.
## Adding Header Information
If the header already exists, it will be replaced; if it does not exist, it will be added.
- **match** (string, required): A regular expression for URL matching.
- **name** (string, required): The name of the header to add.
- **value** (string, required): The value of the header to add.
- **type** (string, optional): Applies to request or response. Defaults to request.
- **disabled** (bool, optional): Whether to disable this rule.
## Replacing Header Information
Semantically intended for replacing the value of an existing header. The actual behavior is the same as add: if the header exists, it will be replaced; if it does not exist, it will be added.
- **match** (string, required): A regular expression for URL matching.
- **name** (string, required): The name of the header to replace.
- **value** (string, required): The new value of the header.
- **type** (string, optional): Applies to request or response. Defaults to request.
- **disabled** (bool, optional): Whether to disable this rule.
## Deleting Header Information
- **match** (string, required): A regular expression for URL matching.
- **name** (string, required): The name of the header to delete.
- **type** (string, optional): Applies to request or response. Defaults to request.
- **disabled** (bool, optional): Whether to disable this rule.

---

## Configuration Body Rewrites

# HTTP Message Body Rewriting
Message body rewriting allows users to modify the body of HTTP requests or responses that match specific URLs. It supports two methods: regex replacement and jq filters. MITM decryption is required to modify HTTPS traffic.
## Regex Replacement
Uses regular expressions to find and replace text content in the message body.
### Request Body Regex
- **match** (string, required): A regular expression for URL matching.
- **find** (string, required): The regex pattern to find in the body.
- **replace** (string, required): The replacement text.
- **disabled** (bool, optional): Whether to disable this rule.
### Response Body Regex
- **match** (string, required): A regular expression for URL matching.
- **find** (string, required): The regex pattern to find in the body.
- **replace** (string, required): The replacement text.
- **disabled** (bool, optional): Whether to disable this rule.
## jq Filter
Use jq expressions to process JSON-formatted message bodies, suitable for making structured modifications to JSON data.
### Request Body jq Filter (request_jq)
- **match** (string, required): A regular expression for URL matching.
- **filter** (string, required): The jq filter expression.
- **disabled** (bool, optional): Whether to disable this rule.
### Response Body jq Filter (response_jq)
- **match** (string, required): A regular expression for URL matching.
- **filter** (string, required): The jq filter expression.
- **disabled** (bool, optional): Whether to disable this rule.

---

## Configuration Scriptings

Scripting | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Egern allows users to flexibly control network request/response handling, scheduled tasks, network change events, and manually triggered generic scripts by writing JavaScript scripts.
Script Types
​
The
scriptings
configuration includes five types of scripts:
Type
Description
http_request
HTTP request script, executed before sending the request
http_response
HTTP response script, executed after receiving the response
schedule
Scheduled script, executed at intervals based on a cron expression
generic
Generic script, manually triggered
network
Network change script, executed when the network environment changes
HTTP Request/Response Scripts
​
name
(string), required
The name of the script.
match
(string), required
A regular expression for URL matching.
script_url
(string), required
The URL of the script file, which can be a local path or a remote link.
env
(object), optional
Environment variables (key-value pairs) passed to the script, accessible via
ctx.env
. See
for details.
update_interval
(integer), optional
The update interval for the script file in seconds. Defaults to 86400 (24 hours).
max_size
(integer), optional
The maximum request/response body size to process in bytes. Bodies exceeding this size will not be passed to the script. Defaults to 1048576 (1MB).
timeout
(integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
body_required
(boolean), optional
Whether the request/response body is needed. Defaults to
false
. Set to
true
if you need to read or modify the body.
binary_body
(boolean), optional
Whether to handle the request/response body in binary mode. Defaults to
false
. Set to
true
when processing binary content such as images.
disabled
(boolean), optional
Whether to disable this script.
Scheduled Scripts
​
Execute scripts at scheduled intervals based on cron expressions, suitable for scenarios such as scheduled check-ins and data synchronization.
Supports the standard 5-field format (minute, hour, day, month, weekday) and the 6-field format (second, minute, hour, day, month, weekday).
name
(string), required
The name of the script.
cron
(string), required
A cron expression (e.g.,
0 8 * * *
means every day at 8:00 AM).
script_url
(string), required
The URL of the script file, which can be a local path or a remote link.
env
(object), optional
Environment variables (key-value pairs) passed to the script, accessible via
ctx.env
. See
for details.
update_interval
(integer), optional
The update interval for the script file in seconds. Defaults to 86400.
timeout
(integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
disabled
(boolean), optional
Whether to disable this script.
Generic Scripts
​
Manually triggered scripts, primarily used as associated scripts for
.
name
(string), required
The name of the script.
script_url
(string), required
The URL of the script file.
env
(object), optional
Environment variables (key-value pairs) passed to the script, accessible via
ctx.env
. See
for details.
update_interval
(integer), optional
The update interval for the script file in seconds. Defaults to 86400.
timeout
(integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
disabled
(boolean), optional
Whether to disable this script.
Network Change Scripts
​
Execute scripts when the network environment changes, such as Wi-Fi switching, cellular network connection, VPN status changes, and similar scenarios. Can be used for automatically switching proxy nodes, sending notifications, and more.
name
(string), required
The name of the script.
script_url
(string), required
The URL of the script file.
env
(object), optional
Environment variables (key-value pairs) passed to the script, accessible via
ctx.env
. See
for details.
update_interval
(integer), optional
The update interval for the script file in seconds. Defaults to 86400.
timeout
(integer), optional
The script execution timeout in seconds. Defaults to 10 seconds, with a maximum of 600 seconds.
disabled
(boolean), optional
Whether to disable this script.
Configuration Example
​
scriptings
:
-
http_request
:
name
:
"Modify Request Headers"
match
:
"^https://api\\.example\\.com/"
script_url
:
"https://example.com/scripts/modify-header.js"
env
:
TOKEN
:
"my-secret-token"
timeout
:
30
body_required
:
true
-
http_response
:
name
:
"Parse Response"
match
:
"^https://api\\.example\\.com/data"
script_url
:
"https://example.com/scripts/parse-response.js"
body_required
:
true
max_size
:
2097152
-
schedule
:
name
:
"Daily Check-in"
cron
:
"0 8 * * *"
script_url

---

## Configuration Modules

Modules | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
In Egern, modules are preset configuration snippets that allow users to conveniently enable or disable a specific set of network processing rules. Modules cover a wide range of functionality and can include rules, URL rewrites, header rewrites, body rewrites, Map Local, scripts, MITM, HTTP captures, and widgets. When a module is enabled, its configuration is merged into Egern's main configuration.
Module Reference Configuration
​
Referencing modules in the main configuration file:
name
(string), optional
The display name of the module, overriding the name defined within the module file. When not set, the
name
field from the module file or the URL is used.
url
(string), required
The address of the module file, which can be a local file path or a remote URL.
compat_arguments
(object), optional
Arguments passed to the module, used to override the default argument values defined in the module file. Arguments are substituted as variables when the module is parsed. See
Argument Substitution
for the placeholder syntax and rules.
env
(object), optional
Environment variables (key-value pairs) passed to scripts and widgets in the module. Module-level env has the highest priority and overrides variables with the same key in widgets and scripts. See
for details.
update_interval
(integer), optional
When the module file is a remote URL, this parameter specifies the update interval (in seconds) for the module. The default value is 86400 (24 hours).
enabled
(boolean), optional
Controls whether the module is enabled. The default value is
true
.
Configuration Example
​
modules
:
-
name
:
"Ad Blocking"
url
:
"https://example.com/adblock.yaml"
enabled
:
true
update_interval
:
86400
-
url
:
"https://example.com/custom.yaml"
compat_arguments
:
API_KEY
:
"your_api_key"
REGION
:
"cn"
env
:
REFRESH_INTERVAL
:
"300"
Module File Format
​
A module file itself is a YAML-formatted file containing metadata and configuration content.
Metadata Fields
​
name
(string), optional
Module name.
description
(string), optional
Module description.
author
(string), optional
Module author.
homepage
(string), optional
Module homepage URL.
manual
(string), optional
Usage instructions URL.
icon
(string), optional
Module icon, supporting SF Symbols names or URLs.
open_url
(string), optional
URL to open the settings page.
compat_arguments
(object), optional
Default values for module arguments. See
Argument Substitution
for how to reference them with placeholders.
compat_arguments_desc
(string), optional
Documentation for module arguments.
env_schema
(object), optional
Declares the available environment variables for the module and their types. Egern will automatically generate corresponding UI controls on the module settings page. Keys are environment variable names, and values are descriptor objects with the following fields:
name
(string), optional — Display name shown in the UI. Falls back to the key name if not set.
description
(string), optional — Descriptive text displayed below the control.
default_value
(string), optional — Default value, shown as placeholder text in the input field. Not written to env unless the user explicitly sets a value.
options
(array), optional — List of allowed values.
["true", "false"]
generates a Toggle switch.
Other values generate a Picker.
When not set, a TextField is generated.
env_schema
:
TITLE
:
name
:
Title
description
:
The title text to display
default_value
:
"Default Title"
ENABLE_FEATURE
:
name
:
Enable Feature
options
:
-
"true"
-
"false"
THEME
:
name
:
Theme
options
:
-
light
-
dark
-
auto
Configuration Content Fields
​
A module file can contain the following configuration items, which are merged with the main configuration:
dns
(object), optional
DNS configuration.
rules
(array), optional
Rule list.
url_rewrites
(array), optional
URL rewrite list.
header_rewrites
(array), optional
Header rewrite list.
body_rewrites
(array), optional
Body rewrite list.
map_locals
(array), optional
Map Local list.
scriptings
(array), optional
Script list.
mitm
(object), optional
MITM configuration.
http_captures
(array), optional
HTTP capture hostname list.
widgets
(array), optional
Widget
list.
bypass_tunnel_proxy
(array), optional
List of domains that bypass the tunnel proxy.
real_ip_domains
(array), optional
List of domains that use real IP addresses (instead of Fake IP).
Configuration Example
​
name
:
"Ad Blocking Module"
description

---

## Configuration Widgets

Widgets | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Egern supports iOS Widgets, allowing users to display custom content on the Home Screen and Lock Screen. Widgets are rendered from a JSON-based DSL description generated by JavaScript scripts.
Using Widgets from Modules
​
The simplest way is to install a module that includes widgets — no coding required.
Steps
​
Go to
Tools
→
, tap
+
in the top-right corner to add a module
Enter the module URL and save
Open the
Analytics
tab at the bottom, tap the top-left button to enter the
Widget Gallery
— widgets provided by the module will automatically appear in the "Module Widgets" section
If the module requires parameters (e.g. API Key), go back to the module edit page and add the corresponding key-value pairs in the
Env
section
Adding to the iOS Home Screen
​
Long-press an empty area on the Home Screen, tap
+
in the top-left corner
Search for
Egern
and select a widget size
After adding, long-press the widget →
Edit Widget
, then select the widget name to display
Building Your Own Widget
​
To create your own widget, you first need a
generic type
script, then create a widget that references it.
1. Create a Script
​
Go to
Tools
→
Scripts
, tap
+
:
Field
Value
Name
e.g.
my-widget
Type
Select
generic
File Location
Select
Local
, enter a filename like
my-widget.js
Tap
Edit File
and write the following minimal script:
export
default
async
function
(
ctx
)
{
return
{
type
:
'widget'
,
children
:
[
{
type
:
'text'
,
text
:
'Hello, Widget!'
,
font
:
{
size
:
'title2'
,
weight
:
'bold'
}
,
textColor
:
'#FFFFFF'
,
}
,
]
,
backgroundColor
:
'#2D6A4F'
,
padding
:
16
,
}
;
}
Save the script.
2. Create a Widget
​
In the
Analytics
tab, tap the top-left button to enter the
Widget Gallery
, then tap
+
:
Field
Value
Name
e.g.
My Widget
Script Name
Select the
my-widget
script you just created
After saving, the widget will appear in the gallery and run automatically.
Widget Configuration
​
Define widgets in the
widgets
field of the main configuration file:
name
(string), required
The widget name, must be unique.
script_name
(string), optional
The name of an associated generic script. Defaults to using a script with the same name as the widget.
env
(object), optional
Environment variables (key-value pairs) passed to the script. See
for details.
Configuration Example
​
scriptings
:
-
generic
:
name
:
"weather-widget"
script_url
:
"https://example.com/scripts/weather.js"
timeout
:
20
-
generic
:
name
:
"net-status-script"
script_url
:
"https://example.com/scripts/net-status.js"
timeout
:
20
widgets
:
# name matches script name, no need to set script_name
-
name
:
"weather-widget"
env
:
CITY
:
"Shanghai"
UNIT

---

## Configuration Http Captures

# HTTP Captures
In Egern, the http_captures configuration allows you to define specific domain wildcard patterns whose HTTP requests and responses will be recorded by the application. This is particularly useful for debugging and inspecting HTTP interactions for specific domains. Glob wildcards are supported (e.g., *.example.com).
> Capturing HTTPS traffic requires configuring MITM and installing a CA certificate.
## Simple Format (String Array)
Directly specify the list of hostnames to capture:
```yaml
http_captures:
- "*.example.com"
- "test.com"
```
## Structured Format (With Exclusions)
You can specify both included and excluded hostnames:
```yaml
http_captures:
includes:
- "*.example.com"
- "test.com"
excludes:
- "*.internal.example.com"
```
Using the exclusion list allows you to exclude specific subdomains when capturing a broad range of domains.

---

## Configuration Env

Environment Variables | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Egern supports configuring environment variables (env) for scripts, widgets, and modules. Environment variables are passed as key-value pairs and can be accessed via
ctx.env
in scripts, allowing the same script to be flexibly configured for different scenarios without modifying the code.
Basic Usage
​
Defining in Scripts
​
All five script types support the
env
field:
scriptings
:
-
generic
:
name
:
"my-script"
script_url
:
"https://example.com/scripts/my-script.js"
env
:
API_KEY
:
"your_api_key"
API_URL
:
"https://api.example.com"
-
http_request
:
name
:
"modify-header"
match
:
"^https://api\\.example\\.com/"
script_url
:
"https://example.com/scripts/modify-header.js"
env
:
TOKEN
:
"my-secret-token"
-
schedule
:
name
:
"daily-checkin"
cron
:
"0 8 * * *"
script_url
:
"https://example.com/scripts/checkin.js"
env
:
USERNAME
:
"user123"
Defining in Widgets
​
widgets
:
-
name
:
"weather-widget"
env
:
CITY
:
"Shanghai"
UNIT
:
"celsius"
Defining in Module References
​
modules
:
-
url
:
"https://example.com/module.yaml"
enabled
:
true
env
:
API_KEY
:
"your_api_key"
REGION
:
"cn"
Accessing in Scripts
​
Environment variables are accessible in scripts via
ctx.env
as key-value pairs:
export
default
async
function
(
ctx
)
{
const
apiKey
=
ctx
.
env
.
API_KEY
;
const
apiUrl
=
ctx
.
env
.
API_URL
;
const
resp
=
await
ctx
.
http
.
get
(
apiUrl
+
'/data'
,
{
headers
:
{
'Authorization'
:
'Bearer '
+
apiKey
}
}
)
;
const
data
=
await
resp
.
json
(
)
;
console
.
log
(
data
)
;
}
Priority and Merging
​
When the same key exists at multiple levels, the priority from highest to lowest is:
Module > Widget > Script
Module-level env overrides widget-level variables with the same key, and widget-level env overrides script-level variables with the same key.
Merging Example
​
Given the following configuration:
scriptings
:
-
generic
:
name
:
"my-widget"
script_url
:
"https://example.com/scripts/widget.js"
env
:

---

## Configuration Example

Configuration Example | Egern
Egern
Configuration Example
HTTP Header Rewriting
HTTP Message Body Rewriting
Configuration Example
Configuration Example
You can configure Egern's parameters in the
Profile.yaml
file.
Here is an example of a
Profile.yaml
file:
---
# Content of automatic update configuration. Default value is empty
auto_update
:
url
:
http
:
//example.com/
interval
:
86400
# Whether to enable IPv6. Default value is false
ipv6
:
false
# HTTP proxy port number. Default value is 3080
http_port
:
3080
# SOCKS proxy port number. Default value is 3090
socks_port
:
3090
# Allow external connections to access the proxy on the device through Wi-Fi. Default value is false
allow_external_connections
:
false
# Virtual interface only mode. Default value is false
vif_only
:
false
# Globally block the QUIC protocol, forcing TCP connections. Default value is false
# Priority: proxy > policy group > global. The proxy's own block_quic takes
# the highest priority, followed by the policy group's, then this global setting.
# If none are set, the protocol default is used (TCP-based protocols block by default,
# UDP-based protocols allow by default).
block_quic
:
false
# Close connections that are still using the old node when a policy group's
# selected node changes (manual switch, automatic latency-test switch, failover,
# or selection fallback after a subscription update), so traffic immediately
# reconnects through the new node. Default value is false
close_connections_on_policy_change
:
false
# List of domains that bypass the tunnel proxy. Default value is an empty array
bypass_tunnel_proxy
:
-
"*.local"
-
"192.168.0.0/16"
# List of domains that use real IP (not Fake IP). Default value is an empty array
real_ip_domains
:
-
"*.lan"
-
"*.push.apple.com"
# Hide VPN icon. Default value is false
hide_vpn_icon
:
false
# List of addresses for DNS hijacking. Default value is an empty array
hijack_dns
:
-
'*'
# Specify a custom GeoIP database URL. Default value is empty
geoip_db_url
:
null
# Specify a custom ASN database URL. Default value is empty
asn_db_url
:
null
# Custom proxy latency test URL. Default value is empty
proxy_latency_test_url
:
null
# Custom direct latency test URL. Default value is empty
direct_latency_test_url
:
null
# Compatible routing mode. Default value is false
compat_route
:
false
# Include all network traffic. Default value is false
include_all_networks
:
false
# Include APNs traffic (requires include_all_networks to be enabled). Default value is false
include_apns
:
false
# Include cellular network service traffic (requires include_all_networks to be enabled). Default value is false
include_cellular_services
:
false
# Include local network traffic (requires include_all_networks to be enabled). Default value is false
include_local_networks
:
false
# Routes included in the virtual interface. Default value is an empty array
vif_included_routes
:
-
192.168.0.1/32
# Routes excluded from the virtual interface. Default value is an empty array
vif_excluded_routes
:
-
192.168.0.1/32
dns
:
bootstrap
:
-
system
# Use the system's default DNS configuration as bootstrap
upstreams
:
google
:
-
https
:
//8.8.8.8/dns
-
query
-
https
:
//8.8.4.4/dns
-
query
forward
:
-
domain_suffix
:
match
:
"cn"
value
:
bootstrap
-
wildcard
:
match
:
'*.cn'
value
:
bootstrap
-
proxy_rule_set
:
match
:
https
:
//github.com/ACL4SSR/ACL4SSR/raw/master/Clash/ChinaDomain.list
value
:
bootstrap
-
regex
:
match
:
^ad\..
*|^ads\..*
value
:
reject
-
wildcard
:
match
:
'*'
value

---

## Javascript-Api

JavaScript API Reference | Egern
Egern
Egern scripts use
export default
to export an async function. The
ctx
object is injected at runtime.
export
default
async
function
(
ctx
)
{
// ...
}
Five script types are supported:
Request
,
Response
,
Schedule
,
Generic
, and
Network
.
ctx
​
ctx.script
​
Script information.
Property
Type
Description
ctx.script.name
string
Script name
ctx.env
​
Object<string, string>
— Environment variable key-value pairs. See
for details.
export
default
async
function
(
ctx
)
{
const
apiKey
=
ctx
.
env
.
API_KEY
;
const
apiUrl
=
ctx
.
env
.
API_URL
;
}
ctx.app
​
Application information.
Property
Type
Description
ctx.app.version
string
App version
ctx.app.language
string
System language
ctx.device
​
Device network environment information.
Property
Type
Description
ctx.device.cellular.carrier
string | null
Cellular carrier
ctx.device.cellular.radio
string | null
Cellular radio technology
ctx.device.wifi.ssid
string | null
Wi-Fi name
ctx.device.wifi.bssid
string | null
Wi-Fi BSSID
ctx.device.ipv4.address
string | null
IPv4 address
ctx.device.ipv4.gateway
string | null
IPv4 gateway
ctx.device.ipv4.interface
string | null
Network interface
ctx.device.ipv6.address
string | null
IPv6 address
ctx.device.ipv6.interface
string | null
Network interface
ctx.device.dnsServers
string[]
DNS server list
ctx.cron
​
string | undefined
— Only available in schedule scripts. The cron expression.
ctx.widgetFamily
​
string | undefined
— Only available in generic scripts. The widget size family.
Possible values:
systemSmall
,
systemMedium
,
systemLarge
,
systemExtraLarge
,
accessoryCircular
,
accessoryRectangular
,
accessoryInline
.
ctx.request
​
Object | undefined
— Only available in request/response scripts.
Property/Method
Type
Description
method
string
HTTP method
url
string
Request URL
headers
Headers
Request headers
body
ReadableStream | null
Request body stream
json()
Promise<any>
Parse as JSON
text()
Promise<string>
Parse as text
arrayBuffer()
Promise<ArrayBuffer>
Parse as ArrayBuffer
blob()
Promise<Blob>
Parse as Blob
formData()
Promise<FormData>
Parse as FormData
Note: The body can only be consumed once (consistent with Fetch API behavior).
ctx.response
​
Object | undefined
— Only available in response scripts.
Property/Method
Type
Description
status
number
Status code
headers
Headers
Response headers
body
ReadableStream | null
Response body stream
json()
Promise<any>
Parse as JSON
text()
Promise<string>
Parse as text
arrayBuffer()

---

## Url-Scheme

URL Scheme | Egern
Egern
All URL Schemes support the
x-success
parameter for callback after the operation completes. For example:
egern:/start?x-success=myapp://callback
Start Egern VPN
egern:/start
Stop Egern VPN
egern:/stop
Add Configuration Profile
egern:/profiles/new?name=name&url=url
Parameter Description:
url
(required): The URL of the configuration file
name
(optional): Name of the configuration
Add Proxy Server
egern:/proxies/new
Add Policy Group
egern:/policy_groups/new?type=type&external_type=external_type&name=name&policy=policy&url=url
Parameter Description:
type
(optional): Policy group type, defaults to
external
external_type
(optional): External policy group type, defaults to
auto_test
name
(optional): Name of the policy group
policy
(optional): Policy
url
(optional): The URL of the policy
Add Subscription
egern:/subscriptions/new?url=url
Parameter Description:
url
(optional): The URL of the subscription
Add Rule
egern:/rules/new?type=domain&match=match&policy=DIRECT
Parameter Description:
type
(optional): Type of rule (e.g.,
domain
or
domain_keyword
), defaults to
rule_set
match
(optional): Matching item (e.g., a specific domain like
example.com
)
policy
(optional): Policy (e.g.,
DIRECT
or
PROXY
)
Add Module
egern:/modules/new?name=name&url=url
Parameter Description:
url
(required): The URL of the module file
name
(optional): Module name
Egern as a Proxy Tool
Copyright © 2026 Egern, LLC. All rights reserved.

---

## Faq

Frequently Asked Questions | Egern
Egern
The Relationship Between Rules, Proxies, and Policy Groups in Egern
​
1. Rules Determine Policies
​
are conditions used to match network requests. When a network request is made, Egern will match them sequentially according to the rules.
Each rule specifies a
policy
, which can be a
proxy name
,
policy group name
, or
DIRECT
and
REJECT
.
2. Policies
​
A
policy
can be a single
proxy
or a
policy group
.
Once a rule is matched, if the policy is a proxy name, the traffic will be forwarded through the specified proxy server.
If the policy is a policy group name, Egern will select an appropriate proxy server based on the type and configuration of the policy group.
3. Sub-policies of Policy Groups
​
A
policy group
can contain multiple
proxies
or
other policy groups
, forming a hierarchical structure.
For example, the policy group
Manual Selection
may include
VmessProxy
and
ShadowsocksProxy
, allowing users to manually choose which proxy to use.
In nested policy groups, the policy matched by a rule may need to go through several layers of policy groups before determining the final proxy server.
4. Traffic Handling Process
​
Request Initiation
: A user's network request needs to be processed.
Rule Matching
: Egern matches the configured rules from top to bottom and finds the first rule that meets the condition.
Policy Determination
: Based on the
policy
of the matched rule, the appropriate policy is determined.
Policy Parsing
:
If the policy is
DIRECT
, the connection is made directly without using a proxy.
If the policy is
REJECT
, the connection is blocked.
If the policy is a proxy name, that proxy server is used.
If the policy is a policy group, the appropriate proxy server is selected according to the policy group's type and configuration.
Request Forwarding
: The network request is processed and forwarded through the determined proxy server.
How to Add a Rule Set
​
Egern currently supports Surge rule sets. Go to Tools -> Rules -> + -> Select the rule-set type, then add the Surge rule set URL.
How to Add a Module
​
Egern currently supports Surge modules. You can add a Surge module URL under Tools -> Modules.
Egern as HTTP traffic sniffer
The Relationship Between Rules, Proxies, and Policy Groups in Egern
1. Rules Determine Policies
2. Policies
3. Sub-policies of Policy Groups
4. Traffic Handling Process
How to Add a Rule Set
How to Add a Module
Copyright © 2026 Egern, LLC. All rights reserved.

---

## Intro

Introduction | Egern
Egern
Egern is a feature-rich and powerful network tool designed for proxying, intercepting, and modifying network traffic.
Key features include:
Detailed logging of TCP, UDP, DNS, and HTTP network traffic.
Support for a wide range of rule types: domain name, domain keyword, domain suffix, domain regex, geo-location, IPv4/IPv6 CIDR, URL regex, rule sets, and default rules.
Flexible policy group options: selection, auto-testing, fallback, load balancing, and external policies.
Support for various proxy protocols: HTTP, SOCKS5, Shadowsocks, Trojan, Hysteria2, Vless, and Vmess.
URL rewriting functionality, giving you greater freedom to customize network requests.
Highly customizable request and response header rewriting capabilities.
Flexible request and response content rewriting options.
Customize request and response data manipulation with JavaScript scripting.
Support for local HTTP proxy servers and local SOCKS5 proxy servers, catering to various network needs.
DNS forwarding rules can proxy traffic to servers that support DoH, DoT, and DoQ protocols.
Sync configuration across devices via iCloud, ensuring your network settings stay consistent wherever you are.
Egern is your essential network management tool, helping you efficiently control and debug various network environments. Whether you’re a network security expert, a developer, or a user interested in network management, Egern will become an indispensable tool for you. Come experience the powerful features of Egern and create your own custom network environment!
Module Conversion
App Store
Configuration Example
Copyright © 2026 Egern, LLC. All rights reserved.

---

---

# 中文文档完整内容

## configuration_body_rewrites

找不到页面 | Egern
Egern
找不到页面
我们找不到您要找的页面。
请联系原始链接来源网站的所有者，并告知他们链接已损坏。

---

## 合并系统 DNS

DNS | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
DNS
DNS
Egern 的 DNS 子系统支持多种协议（UDP、DoT、DoH、DoQ、DoH3），并允许通过 Forward 规则把不同域名分发到不同的上游 DNS 组。Egern 内部存在两条解析路径：
默认 DNS
：处理用户流量的域名解析，按 Forward 规则匹配上游，未命中回退到 Bootstrap；连接上游时遵循代理规则。
代理 DNS
：代理服务器解析目标域名时使用，连接上游时强制直连，避免 DNS → 代理 → DNS 的循环依赖。配置 
proxy_nameservers
 后，所有代理 DNS 查询强制走该列表（
绕过 Forward 规则
）；未配置时与默认 DNS 共用 Forward 规则，未命中回退到 Bootstrap。
解析流程
​
每次域名查询依次经过以下阶段：
Hosts
：命中本地映射时直接返回（IP）或将映射后的域名作为别名继续解析。
Forward
：按配置顺序匹配规则，第一条命中规则决定上游 DNS。SSID/BSSID/Cellular 类规则依赖当前网络状态，网络变化时匹配缓存会被清空。代理 DNS 在配置了 
proxy_nameservers
 时跳过此阶段，所有查询直接走该列表。
默认上游
：所有 Forward 规则均未命中时使用——默认 DNS 回退到 Bootstrap；代理 DNS 在未配置 
proxy_nameservers
 时也回退到 Bootstrap。
Block IPs
：响应中匹配 
block_ips
 的记录被过滤；全部被过滤时视为解析失败。
Bootstrap（启动 DNS）
​
bootstrap
 配置启动阶段使用的 DNS 服务器，仅支持传统 UDP 协议（端口 53），且不遵循代理规则——流量直连。它有两个用途：
解析 
upstreams
 中加密 DNS 服务器（
tls://
、
https://
 等）的主机名。
作为最终的 DNS 回退（详见上文「解析流程」）。
支持的值：
IP 或 
IP:port
，例如 
1.1.1.1
、
8.8.8.8:53
。
特殊值 
system
：合并系统 DNS 服务器（即 Wi-Fi/蜂窝网络下发的 DNS）。
未配置或解析失败时，自动使用系统 DNS 服务器。
dns
:
bootstrap
:
-
 system        
# 合并系统 DNS
-
 223.5.5.5     
# 同时加上自定义服务器
Upstreams（DNS 服务器组）
​

---

## 同一脚本，不同环境变量，显示不同城市天气

环境变量 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
环境变量
环境变量
Egern 支持为脚本、小组件和模块配置环境变量（env）。环境变量以键值对形式传递，脚本中可通过 
ctx.env
 访问，使得同一脚本在不同场景下可以灵活配置而无需修改代码。
基本用法
​
在脚本中定 义
​
所有五种脚本类型均支持 
env
 字段：
scriptings
:
-
generic
:
name
:
&quot;my-script&quot;
script_url
:
&quot;https://example.com/scripts/my-script.js&quot;
env
:
API_KEY
:
&quot;your_api_key&quot;
API_URL
:
&quot;https://api.example.com&quot;
-
http_request
:
name
:
&quot;modify-header&quot;
match
:
&quot;^https://api\\.example\\.com/&quot;
script_url
:
&quot;https://example.com/scripts/modify-header.js&quot;
env
:
TOKEN
:
&quot;my-secret-token&quot;
-
schedule
:
name
:
&quot;daily-checkin&quot;
cron
:
&quot;0 8 * * *&quot;
script_url
:
&quot;https://example.com/scripts/checkin.js&quot;
env
:
USERNAME
:

---

## 自动更新配置的内容。默认值是空

示例 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
示例
示例
您可以在 Profile.yaml 文件中配置 Egern 的参数。
下面是一个 Profile.yaml 文件的示例：
---
# 自动更新配置的内容。默认值是空
auto_update
:
url
:
 http
:
//example.com/
interval
:
86400
# 是否启用 IPv6。默认值是 false
ipv6
:
false
# HTTP 代理端口号。默认值是 3080
http_port
:
3080
# SOCKS 代理端口号。默认值是 3090
socks_port
:
3090
# 允许外部连接通过 Wi-Fi 访问设备上的代理。默认值是 false
allow_external_connections
:
false
# 仅虚拟网接口模式。默认值是 false
vif_only
:
false
# 全局阻止 QUIC 协议，强制使用 TCP 连接。默认值是 false
# 优先级：代理 &gt; 策略组 &gt; 全局。代理自身的 block_quic 优先级最高，
# 其次是策略组的 block_quic，最后是此全局设置。
# 若三者均未设置，则使用协议默认值（TCP 类协议默认阻止，UDP 类协议默认放行）。
block_quic
:
false
# 策略组选中节点变化时（手动切换、自动测速切换、故障转移、订阅更新后选中项回退），
# 关闭仍在使用旧节点的连接，使流量立即通过新节点重连。默认值是 false
close_connections_on_policy_change
:
false
# 绕过隧道代理的域名列表。默认值是空数组
bypass_tunnel_proxy
:
-
&quot;*.local&quot;
-
&quot;192.168.0.0/16&quot;
# 使用真实 IP 的域名列表（不使用 Fake IP）。默认值是空数组
real_ip_domains
:
-
&quot;*.lan&quot;
-
&quot;*.push.apple.com&quot;
# 隐藏 VPN 图标。默认值是 false
hide_vpn_icon

---

## configuration_header_rewrites

找不到页面 | Egern
Egern
找不到页面
我们找不到您要找的页面。
请联系原始链接来源网站的所有者，并告知他们链接已损坏。

---

## configuration_http_captures

找不到页面 | Egern
Egern
找不到页面
我们找不到您要找的页面。
请联系原始链接来源网站的所有者，并告知他们链接已损坏。

---

## 字符串默认值

模块 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
模块
模块
在 Egern 中，模块是预设定的配置片段，用户可以方便地启用或禁用一组特定的网络处理规则。模块的功能覆盖范围广泛，可以包含规则、URL 重写、头部重写、主体重写、Map Local、脚本、MITM、HTTP 抓取和小组件等。当启用模块后，模块内的配置将会被合并到 Egern 的主配置中。
模块引用配置
​
在主配置文件中引用模块：
name
 (string), 可选
模块显示名称，覆盖模块文件内定义的名称。未设置时使用模块文件中的 
name
 字段或 URL。
url
 (string), 必填
模块文件的地址，可以是本地文件路径或远程链接。
compat_arguments
 (object), 可选
传递给模块的参数，用于覆盖模块文件中定义的默认参数值。参数会在模块解析时进行变量替换。详见 
参数替换
。
env
 (object), 可选
传递给模块中脚本和小组件的环境变量（键值对）。模块级别的 env 优先级最高，会覆盖小组件和脚本中的同名变量。详见 
环境变量
。
update_interval
 (integer), 可选
当模块文件是远程链接时，此参数指定模块的更新间隔（秒）。默认值为 86400（24 小时）。
enabled
 (boolean), 可选
控制模块是否启用。默认值为 
true
。
示例
​
modules
:
-
name
:
&quot;广告过滤&quot;
url
:
&quot;https://example.com/adblock.yaml&quot;
enabled
:
true
update_interval
:
86400
-
url
:
&quot;https://example.com/custom.yaml&quot;
compat_arguments
:
API_KEY
:
&quot;your_api_key&quot;
REGION
:
&quot;cn&quot;
env
:
REFRESH_INTERVAL

---

## configuration_policy_groups

找不到页面 | Egern
Egern
找不到页面
我们找不到您要找的页面。
请联系原始链接来源网站的所有者，并告知他们链接已损坏。

---

## 使用内联私钥认证（PEM/OpenSSH 格式）……

代理 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
代理
代理
代理的配置，支持协议 
Shadowsocks
，
Snell
，
Trojan
，
AnyTLS
，
Hysteria2
，
TUIC
，
SOCKS5
，
SOCKS5 over TLS
，
SSH
，
HTTP
，
HTTPS
，
Vmess
，
Vless
，
WireGuard
。所有字段中 
bool
 类型的可选值默认为 
false
。
Shadowsocks
​
name
 (string), 必填
代理名称，需在全局唯一。
method
 (string), 必填
加密方式。
AEAD-2022：
2022-blake3-aes-128-gcm
, 
2022-blake3-aes-256-gcm
, 
2022-blake3-chacha20-poly1305
AEAD：
chacha20-poly1305
, 
aes-256-gcm
, 
aes-128-gcm
Stream：
none
, 
table
, 
rc4
, 
rc4-md5
, 

---

## configuration_rules

规则 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
规则
规则
Egern 支持多种类型的规则，可以用于控制网络流量的代理行为，同时可以用于阻止某些流量。规则按照配置顺序依次匹配，匹配成功后不再继续匹配后续规则。
支持的规则
​
域名规则
​
类型
名称
说明
domain
域名完全匹配
完全匹配域名
domain_suffix
域名后缀匹配
匹配域名后缀，自动处理子域名边界（如 
google.com
 匹配 
www.google.com
 但不匹配 
fakegoogle.com
）
domain_keyword
域名关键词匹配
匹配含有指定关键词的域名
domain_regex
域名正则匹配
通过正则表达式匹配域名
domain_wildcard
域名通配符匹配
使用 glob 模式匹配域名，大小写不敏感（如 
*.google.*
）
IP 规则
​
类型
名称
说明
geoip
GeoIP 匹配
根据 ISO 3166-1 alpha-2 国家/地区代码匹配 IP 地址（如 
CN
、
US
）
ip_cidr
IPv4 范围匹配
匹配指定 IPv4 CIDR 范围
ip_cidr6
IPv6 范围匹配
匹配指定 IPv6 CIDR 范围
asn
ASN 匹配
匹配 ASN 编号或组织名称（如 
13335
、
AS13335
、
Telegram Messenger Inc
）
其他规则
​
类型
名称

---

## configuration_scriptings

脚本 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
脚本
脚本
Egern 允许用户通过编写 JavaScript 脚本来灵活地控制网络请求/响应的处理、定时任务、网络变化事件以及手动触发的通用脚本。
脚本类型
​
scriptings
 配置包含五种类型的脚本：
类型
说明
http_request
HTTP 请求脚本，在发送请求前执行
http_response
HTTP 响应脚本，在收到响应后执行
schedule
定时脚本，按 cron 表达式定时执行
generic
通用脚本，手动触发执行
network
网络变化脚本，在网络环境变化时执行
HTTP 请求/响应脚本
​
name
 (string), 必填
脚本名称。
match
 (string), 必填
URL 匹配正则表达式。
script_url
 (string), 必填
脚本文件的 URL，可以是本地路径或远程链接。
env
 (object), 可选
传递给脚本的环境变量（键值对），在脚本中可通过 
ctx.env
 访问。详见 
环境变量
。
update_interval
 (integer), 可选
脚本文件更新间隔（秒），默认 86400（24 小时）。
max_size
 (integer), 可选
最大处理的请求/响应体大小（字节），超过此大小不传递给脚本，默认 1048576 (1MB)。
timeout
 (integer), 可选
脚本执行超时时间（秒），默认 10 秒，最大 600 秒。
body_required
 (boolean), 可选
是否需要请求/响应体，默认 
false
。如需读取或修改 body 需设为 
true
。
binary_body
 (boolean), 可选
是否以二进制方式处理请求/响应体，默认 
false
。处理图片等二进制内容时需设为 
true
。
disabled
 (boolean), 可选
是否禁用此脚本。
定时脚本

---

## URL 重写

# URL 重写
URL 重写功能支持三种模式：
- **重定向模式**：返回 HTTP 3xx 重定向响应，客户端会感知到重定向并发起新请求。
- **Header 模式**：直接修改请求的 URI 和 Host 头，透明地将请求转发到新地址，客户端无感知。
- **Reject 模式**：直接返回特定响应体来拦截请求，常用于广告过滤。
> 重写 HTTPS 请求的 URL 需要配置 MITM 并安装 CA 证书。
## 字段
- **match** (string, 必填): URL 匹配正则表达式，匹配完整请求 URL（含协议、主机名、路径和查询参数）。支持捕获组。
- **location** (string, 必填): 重定向目标 URL，支持使用 $1、$2 等引用捕获组。特殊值：
  - `http://reject/` — 返回 404 空响应
  - `http://reject-200/` — 返回 200 空响应
  - `http://reject-dict/` — 返回空 JSON 对象 {}
  - `http://reject-array/` — 返回空 JSON 数组 []
  - `http://reject-img/` — 返回 1×1 透明 GIF
  - `http://reject-video/` — 返回空 MP4
- **status_code** (integer, 可选): HTTP 重定向状态码（301/302/307/308）。省略时使用 header 模式。
- **disabled** (bool, 可选): 是否禁用此规则。

---

## name 与脚本同名，无需设置 script_name

小组件 | Egern
Egern
示例
代理
策略组
规则
模块
DNS
HTTP 抓包
URL 重写
HTTP 头部重写
HTTP 消息体重写
脚本
小组件
环境变量
参考
小组件
小组件
Egern 支持 iOS 小组件（Widget），允许用户在主屏幕和锁定屏幕上显示自定义内容。小组件通过 JavaScript 脚本生成 JSON 格式的 DSL 描述，由 Egern 渲染为原生小组件视图。
使用模块中的小组件
​
最简单的方式是安装包含  小组件的模块，无需编写任何代码。
步骤
​
进入 
工具
 → 
模块
，点击右上角 
+
 添加模块
填入模块 URL，保存
打开底部 
分析
 标签页，点击左上角按钮进入 
小组件画廊
，模块提供的小组件会自动出现在「模块小组件」区域
如果模块需要参数（如 API Key），回到模块编辑页面，在 
Env
 区域添加对应的键值对
添加到 iOS 主屏幕
​
长按主屏幕空白处，点击左上角 
+
Egern
，选择小组件尺寸
添加后长按小组件 → 
编辑小组件
，选择要显示的小组件名称
自建小组件
​
如果你想创建自己的小组件，需要先有一个 
generic 类型
的脚本，然后创建小组件关联它。
1. 创建脚本
​
进入 
工具
 → 
脚本
，点击 
+
：
字段
填写内容
名称
例如 
my-widget
类型
选择 
generic
文件位置
选 
本地
，填写文件名如 
my-widget.js
点击 
编辑文件
，写入以下最简脚本：
export

---

## example_http-traffic-sniffer

Egern 作为 HTTP 流量抓取工具 | Egern
Egern
参考
Egern 作为 HTTP 流量抓取工具
Egern 作为代理工具
Egern 作为 HTTP 流量抓取工具
Egern 作为 HTTP 流量抓取工具
Egern 可用于捕获和分析网络传输中 HTTP 请求和响应数据的工具，能够帮助诊断网络应用问题、监控数据传输，以及进行网络安全分析。
根证书
​
点击 
工具
 -&gt; 
证书
 -&gt; 
生成新证书
 -&gt; 
安装新证书
开启全局 MITM
​
点击 
全部连接
 -&gt; 
...
 -&gt; 
开启全局 MITM
开启 HTTP 全局抓包
​
点击 
全部连接
 -&gt; 
...
 -&gt; 
开启 HTTP 全局抓包
Egern 作为代理工具
根证书
开启全局 MITM
开启 HTTP 全局抓包

---

## example_proxy

Egern 作为代理工具 | Egern
Egern
参考
Egern 作为 HTTP 流量抓取工具
Egern 作为代理工具
Egern 作为代理工具
Egern 作为代理工具
Egern 可作为代理工具代理网络流量，以下列子说明了如何添加代理服务器和使用远程代理订阅。
使用代理服务器
​
添加 Shadowsocks 代理服务器
​
点击 
工具
 -&gt; 
代理
 -&gt; 
+
，填入
名称
，
服务器
，
端口
，
方法
和
密码
，点击保存。
添加代理服务器到策略组中
​
点击 
策略组
 -&gt; 
Proxy
 -&gt; 
ss
 -&gt; 
保存
。
使用远程代理的订阅地址
​
修改 Proxy 为外部策略组
​
点击 
策略组
 -&gt; 
Proxy
 -&gt; 
类型
 -&gt; 
外部的
 -&gt; 
添加新的 URL
，填入远程代理的 URL 地址，点击 
保存
。
Egern 作为 HTTP 流量抓取工具
使用代理服务器
添加 Shadowsocks 代理服务器
添加代理服务器到策略组中
使用远程代理的订阅地址
修改 Proxy 为外部策略组

---

## faq

| Egern
Egern
参考
 常见问题
如何从官网购买 Egern Pro
​
通过支付宝或微信可以在 
https://egernapp.com/payment
 购买 Egern Pro，购买后会收到一封授权邮件，邮件中包含了授权码和激活链接。
一键激活
​
在授权邮件中点击激活链接即可激活 Egern Pro，此链接永久有效。
也可以通过手动在 Egern 中输入授权码激活 Egern Pro
​
打开 Egern，在左上角点击升级到专业版
点击恢复购买 → 通过邮箱恢复
输入邮箱和授权码
官网购买的 Egern Pro 设备限制数量
​
每个授权支持最多 3 个 iCloud 账号，设备数量不限。
在 Egern 中规则、代理与策略组的关系
​
1. 规则决定策略
​
规则
 是用于匹配网络请求的条件。当网络请求发出时，Egern 会根据规则的顺序逐一匹配。
每条规则都指定了一个 
策略（policy）
，这个策略可以是一个 
代理名称
、
策略组名称
 或者 
DIRECT
 和 
REJECT
。
2. 策略
​
策略
 可以是单个 
代理
，也可以是一个 
策略组
。
当规则匹配后，如果策略是一个代理名称，流量将通过指定的代理服务器转发。
如果策略是一个策略组名称，Egern 将根据策略组的类型和配置，选择合适的代理服务器。
3. 策略组的子策略
​
策略组
 可以包含多个 
代理
 或 
其他策略组
，形成一个层级结构。
例如，策略组 
手动选择
 包含 
VmessProxy
 和 
ShadowsocksProxy
，用户可以手动选择使用哪个代理。
在嵌套的策略组中，规则匹配的策略可能需要经过多个策略组的选择，最终确定具体的代理服务器。
4. 流量处理流程
​
请求发出
：用户的网络请求需要被处理。
规则匹配
：Egern 从上到下匹配配置的规则，找到第一个符合条件的规则。
确定策略
：根据匹配规则的 
policy
，确定使用的策略。
策略解析
：
如果策略是 
DIRECT
，直接连接，不使用代理。
如果策略是 
REJECT

---

## intro

| Egern
Egern
参考
 介绍
Egern 是一款功能丰富且强大的网络工具，专为代理、拦截和修改网络流量而设计。
主要特点包括：
详细记录 TCP、UDP、DNS 和 HTTP 网络流量。
支持丰富的规则类型：域名、域名关键词、域名后缀、域名正则表达式、地理位置、IPv4/IPv6 CIDR、URL 正则表达式、规则集以及默认规则。
提供灵活的策略组选项：选择、自动测试、故障切换、负载均衡和外部策略。
支持多种代理协议：HTTP、SOCKS5、Shadowsocks、Trojan、Hysteria2、Vless 和 Vmess。
URL 重写功能，让您更自由地定制网络请求。
高度可定制的请求和响应头部重写功能。
灵活的请求和响应内容重写能力。
通过 JavaScript 脚本为您提供自定义请求和响应数据的操作。
支持本地 HTTP 代理服务器和本地 SOCKS5 代理服务器，满足各种网络需求。
DNS 转发规则可将流量代理至支持 DoH、DoT 和 DoQ 协议的服务器。
通过 iCloud 实现跨设备配置信息同步，让您的网络设置随时随地保持一致。
Egern 作为您的网络管理利器，帮助您轻松应对各种网络环境，实现高效网络控制和调试。无论您是网络安全专家、开发者还是对网络管理感兴趣的用户，Egern 都将成为您不可或缺的工具。快来体验 Egern 的强大功能，打造专属的网络环境吧！
模块转换
App Store
示例

---

## javascript-api

参考 | Egern
Egern
参考
参考
参考
Egern 脚本使用 
export default
 导出一个 async 函数，运行时会将 
ctx
 对象注入该函数。
export
default
async
function
(
ctx
)
{
// ...
}
支持五种脚本类型：
Request
、
Response
、
Schedule
、
Generic
 和 
Network
。
ctx
​
ctx.script
​
脚本信息。
属性
类型
说明
ctx.script.name
string
脚本名称
ctx.env
​
Object&lt;string, string&gt;
 — 环境变量键值对。详见 
环境变量
。
export
default
async
function
(
ctx
)
{
const
 apiKey 
=
 ctx
.
env
.
API_KEY
;
const
 apiUrl 
=
 ctx
.
env
.
API_URL
;
}
ctx.app
​
应用信息。
属性
类型

---

## url-scheme

| Egern
Egern
参考
所有 URL Scheme 均支持 
x-success
 参数，用于操作完成后的回调。例如：
egern:/start?x-success=myapp://callback
启动 Egern VPN
egern:/start
停止 Egern VPN
egern:/stop
添加配置文件
egern:/profiles/new?name=name&amp;url=url
参数说明：
url
（必填）：配置文件的 URL
name
（可选）：配置名称
添加代理服务器
egern:/proxies/new
添加策略组
egern:/policy_groups/new?type=type&amp;external_type=external_type&amp;name=name&amp;policy=policy&amp;url=url
参数说明：
type
（可选）：策略组类型，默认为 
external
external_type
（可选）：外部策略组类型，默认为 
auto_test
name
（可选）：策略组名称
policy
（可选）：策略
url
（可选）：策略的 URL
添加订阅
egern:/subscriptions/new?url=url
参数说明：
url
（可选）：订阅的 URL
添加规则
egern:/rules/new?type=domain&amp;match=match&amp;policy=DIRECT
参数说明：
type
（可选）：规则类型（如 
domain
 或 
domain_keyword
），默认为 
rule_set
match
（可选）：匹配项（如具体域名 
example.com
）
policy
（可选）：策略（如 
DIRECT
 或 
PROXY
）
添加模块
egern:/modules/new?name=name&amp;url=url
参数说明：
url
（必填）：模块文件的 URL
name
（可选）：模块名称
Egern 作为代理工具

---

---

## 实战：与 Surge 共用规则集 + 两个关键排查案例（2026-10-06）

### 1. 与 Surge 共用同一套规则集
Egern 的 `rule_set` **原生支持 Surge 规则集**（官方文档明确 "Egern currently supports Surge rule sets"），可直接引用 mickeu/surge 的 .list URL，实现与 Surge 完全同源的分流规则：
- 境外代理：`Proxy_Supplement.list`（mickeu/surge）+ `Global_All.list`（blackmatrix7）
- 苹果/国内：`Apple_All`、`Direct_Supplement` 等
- 流媒体：用 `_All` 版（`GlobalMedia_All.list`，不要用纯 IP 的 `GlobalMedia.list`）
- 国内：`ChinaMax_All.list` 一条（不要用已删除的 `ChinaMax_Domain.list` + 纯 IP 的 `ChinaMax.list`）

⚠️ 检测类网站（browserleaks.com 等）必须确认在代理规则集里，且该规则集位于「国内直连」（geoip CN）之前——否则会落到 geoip CN 被误判为国内 IP → 真实 IP 泄露。

### 2. Telegram fallback 精准测速（对应 Surge 的 fallback + test-url）
Egern 支持组级测速 URL（`latency_test_url`），无需像 Surge 那样给节点加 test-url：
```yaml
- fallback:
    name: Telegram
    policies: [🇯🇵日本, 🇸🇬新加坡, BPD, 美国节点, 香港节点]
    flatten: true
    interval: 120
    latency_test_url: https://telegram.org
```

### 3. 排查案例：网站全挂（网易/Minis 模型/快捷指令分享）＝ DNS 上游直连国外 DoH
- 现象：国内国外网站全不通，DNS 解析超时
- 根因：`DNS上游直连` 规则把 `1.1.1.1/8.8.8.8` 强制 `DIRECT`；国内直连 Cloudflare IP 常被墙 → 境外 DoH 全部超时 → 所有域名解析失败
- 修复：从该规则移除 CF IP 段，只保留 Lan.list 直连；1.1.1.1 DoH 请求落到默认规则走 PROXY 即可达

### 4. 排查案例：BrowserLeaks 显示本地真实 IP，但 DNS 未泄露
- 现象：BrowserLeaks DNS Leak Test 页面 `Your IP Address` 显示联通/电信真实 IP，DNS 测试服务器显示境外（正常）
- 根因：访问 browserleaks.com 的流量被「国内直连」误判（geoip CN / ChinaMax_All 内误收录段），实际走了 DIRECT
- 修复：在「境外代理」规则加入 `Proxy_Supplement.list`（browserleaks.com 在其中），且确保它在「国内直连」之前命中 PROXY

### 参考资料（来源）
- 本次实战基于用户 Egern 配置定版「被🐶追的猫.yaml」，config-backup commit `4178edf`（2026-10-06）
- mickeu/surge 规则集仓库：https://github.com/mickeu/surge （Rulesets/ 目录）
- blackmatrix7 规则集：https://github.com/blackmatrix7/ios_rule_script

## 实战：油价小组件背景改造——纯白/纯黑 + 卡片描边立体感（2026-10-08）

### 需求与结论
用户希望油价组件背景借鉴 IBL3ND 版（白底 + 卡片描边立体感），但**保留自己的纯白/纯黑配色**。已修改 `mickeu/Egern/实时油价.js` 并推送（commit `62026b9`）。

### 关键实现
- **背景字段**：沿用 `backgroundGradient`（`{type:'linear', colors:[C.bg,C.bg], ...}` 两端同色=纯色），**不要改成 `backgroundColor`**——注释说明这是实测后确保覆盖 Egern 默认背景的写法
- **背景色**：`bg: { light:'#FFFFFF', dark:'#000000' }`（纯白/纯黑，IBL3ND 是白/`#1C1C1E`）
- **立体感**：卡片加 `borderWidth: 0.5 + borderColor`（IBL3ND 同款 `#E0E0E0`/`#3A3A3C`），同时浅色下卡片色从纯白改为微灰 `#F5F5F7`，与纯白背景形成层次对比

### 借鉴 IBL3ND 版时的配色映射
| 项 | IBL3ND | 本组件最终值 |
|---|---|---|
| 页面背景 | `#FFFFFF` / `#1C1C1E` | `#FFFFFF` / `#000000`（保留纯黑） |
| 卡片背景 | `#F5F5F7` / `#2C2C2E` | `#F5F5F7` / `#2C2C2E`（同款） |
| 卡片描边 | `#E0E0E0` / `#3A3A3C`，宽 0.5 | 同款 |

### 参考资料（来源）
- 修改后脚本：https://raw.githubusercontent.com/mickeu/Egern/main/实时油价.js
- IBL3ND 参考脚本：https://raw.githubusercontent.com/IBL3ND/module/refs/heads/main/Oil_Widget.JS
- 本组件原始出处：https://raw.githubusercontent.com/jnlaoshu/MySelf/master/Egern/Widget/GasPrice.js
- 数据中心(DCH)脚本：https://raw.githubusercontent.com/mickeu/Egern/main/数据中心.js
