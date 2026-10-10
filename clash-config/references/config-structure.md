# Hako 内核完整 YAML 配置结构参考

> 基于 ProjectClash/Clash-Legacy（原 TokenPLS/Hako）源码（mihomo 分支内核）提取。源文件：`config/config.go`、`config/initial.go`、`config/utils.go`、`adapter/parser.go`、`adapter/outboundgroup/*.go`、`adapter/provider/parser.go`、`rules/parser.go`、`rules/provider/parse.go`、`listener/parse.go`、`listener/inbound/*.go`、`docs/config.yaml`。
>
> 约定：YAML 字段名来自 struct tag（`yaml:"xxx"`）或 structure decoder tag（`group:"xxx"` / `provider:"xxx"` / `inbound:"xxx"`）。默认值来自 `DefaultRawConfig()` 函数及 parser 初始化逻辑。

---

## 一、顶层全局参数（RawConfig struct）

定义于 `config/config.go` → `RawConfig`。

### 1.1 入站端口

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `port` | `int` | `0`（未设置） | HTTP(S) 代理服务器端口 |
| `socks-port` | `int` | `0` | SOCKS5 代理端口 |
| `redir-port` | `int` | `0` | 透明代理端口（Linux/macOS redir） |
| `tproxy-port` | `int` | `0` | 透明代理端口（Linux TProxy TCP+UDP） |
| `mixed-port` | `int` | `0` | HTTP(S)+SOCKS 混合代理端口 |
| `ss-config` | `string` | `""` | Shadowsocks 入站配置 URL（`ss://...`） |
| `vmess-config` | `string` | `""` | Vmess 入站配置 URL（`vmess://...`） |
| `inbound-tfo` | `bool` | `false` | 入站连接 TCP Fast Open |
| `inbound-mptcp` | `bool` | `false` | 入站连接 Multipath TCP |

### 1.2 认证与 LAN 控制

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `allow-lan` | `bool` | `false` | 是否允许局域网连接 |
| `bind-address` | `string` | `"*"` | 绑定 IP 地址，`*` 表示所有地址；仅当 `allow-lan: true` 生效 |
| `authentication` | `[]string` | `[]` | HTTP/SOCKS 入口认证用户名密码，格式 `"user:pass"` |
| `skip-auth-prefixes` | `[]netip.Prefix` | `nil` | 跳过认证的 IP 段（CIDR） |
| `lan-allowed-ips` | `[]netip.Prefix` | `["0.0.0.0/0","::/0"]` | 允许连接的 IP 白名单（仅 `allow-lan: true`） |
| `lan-disallowed-ips` | `[]netip.Prefix` | `nil` | 禁止连接的 IP 黑名单（优先级高于白名单） |

### 1.3 核心运行参数

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `mode` | `T.TunnelMode` | `rule` | 运行模式，可选 `rule` / `global` / `direct` |
| `log-level` | `log.LogLevel` | `info` | 日志级别，可选 `silent` / `error` / `warning` / `info` / `debug` |
| `ipv6` | `bool` | `true` | IPv6 总开关，关闭则阻断所有 IPv6 链接并屏蔽 DNS AAAA |
| `unified-delay` | `bool` | `false` | 统一延迟计算方式（去掉握手时间） |
| `tcp-concurrent` | `bool` | `false` | TCP 并发连接所有 IP，使用最快握手的 TCP |
| `interface-name` | `string` | `""` | 出口网卡名 |
| `routing-mark` | `int` | `0` | Linux fwmark |
| `find-process-mode` | `process.FindProcessMode` | `strict` | 进程匹配模式，可选 `always` / `strict` / `off` |
| `global-client-fingerprint` | `string` | `""` | **已移除**，仅打印警告；请在 proxy 上直接设置 `client-fingerprint` |
| `global-ua` | `string` | `"clash.meta/<version>"` | 全局 User-Agent |
| `etag-support` | `bool` | `true` | 是否支持 ETag（provider 下载缓存） |
| `keep-alive-idle` | `int` | `0` | TCP keep-alive idle 时间（秒） |
| `keep-alive-interval` | `int` | `0` | TCP keep-alive interval 时间（秒） |
| `disable-keep-alive` | `bool` | `false` | 禁用 TCP keep-alive（Android 端强制为 true） |

### 1.4 外部控制器（Controller）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `external-controller` | `string` | `""` | RESTful API 监听地址 |
| `external-controller-tls` | `string` | `""` | RESTful API HTTPS 监听地址（需配置 `tls` 段） |
| `external-controller-unix` | `string` | `""` | RESTful API Unix socket 监听地址（不验证 secret） |
| `external-controller-pipe` | `string` | `""` | RESTful API Windows named pipe 监听地址（不验证 secret） |
| `external-controller-routing-mark` | `int` | `0` | 为 controller 监听 socket 设置 routing-mark（仅 Linux） |
| `external-controller-cors` | `RawCors` | 见下 | RESTful API CORS 配置 |
| `secret` | `string` | `""` | API 认证密钥（`Authorization: Bearer ${secret}`） |
| `external-ui` | `string` | `""` | Web UI 目录路径 |
| `external-ui-name` | `string` | `""` | Web UI 名称（须为本地名） |
| `external-ui-url` | `string` | `"https://github.com/MetaCubeX/metacubexd/archive/refs/heads/gh-pages.zip"` | Web UI 下载 URL（zip/tgz） |
| `external-doh-server` | `string` | `""` | 在 RESTful API 端口上开启 DOH 服务器路径（不验证 secret） |

#### external-controller-cors（RawCors）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `allow-origins` | `[]string` | `["*"]` | 允许的 CORS 来源 |
| `allow-private-network` | `bool` | `true` | 是否允许私有网络访问 |

### 1.5 GeoData 配置

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `geox-url` | `RawGeoXUrl` | 见下 | 自定义 GeoData 下载 URL |
| `geo-auto-update` | `bool` | `false` | 是否自动更新 GeoData |
| `geo-update-interval` | `int` | `24` | 更新间隔（小时） |
| `geodata-mode` | `bool` | `geodata.GeodataMode()`（编译期决定） | 是否使用 dat 格式 GeoData |
| `geodata-loader` | `string` | `"memconservative"` | GeoData 加载器，可选 `standard` / `memconservative` |
| `geosite-matcher` | `string` | `""`（内部默认 `succinct`） | GeoSite 匹配器实现，可选 `succinct` / `mph` |

#### geox-url（RawGeoXUrl）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `geoip` | `string` | `"https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.dat"` | GeoIP dat URL |
| `mmdb` | `string` | `"https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geoip.metadb"` | MMDB URL |
| `asn` | `string` | `"https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/GeoLite2-ASN.mmdb"` | ASN MMDB URL |
| `geosite` | `string` | `"https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/geosite.dat"` | GeoSite dat URL |

### 1.6 顶层子段映射

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `proxies` | `[]map[string]any` | `[]` | 代理节点列表 |
| `proxy-groups` | `[]map[string]any` | `[]` | 策略组列表 |
| `rules` | `[]string` | `[]` | 规则列表 |
| `sub-rules` | `map[string][]string` | `nil` | 子规则集 |
| `proxy-providers` | `map[string]map[string]any` | `nil` | 代理订阅 |
| `rule-providers` | `map[string]map[string]any` | `nil` | 规则订阅 |
| `listeners` | `[]map[string]any` | `nil` | 入站监听列表 |
| `hosts` | `map[string]any` | `{}` | 自定义 hosts |
| `dns` | `RawDNS` | 见 DNS 段 | DNS 配置 |
| `ntp` | `RawNTP` | 见 NTP 段 | NTP 配置 |
| `tun` | `RawTun` | 见 tun 段 | TUN 配置 |
| `tuic-server` | `RawTuicServer` | 见 tuic-server 段 | TUIC 入站服务器 |
| `iptables` | `RawIPTables` | 见 iptables 段 | iptables 配置 |
| `experimental` | `RawExperimental` | 见 experimental 段 | 实验性配置 |
| `profile` | `RawProfile` | 见 profile 段 | 存储配置 |
| `geox-url` | `RawGeoXUrl` | 见上 | GeoData URL |
| `sniffer` | `RawSniffer` | 见 sniffer 段 | 嗅探配置 |
| `tls` | `RawTLS` | 见 tls 段 | 全局 TLS 配置 |
| `tunnels` | `[]LC.Tunnel` | `nil` | 隧道配置 |
| `clash-for-android` | `RawClashForAndroid` | 零值 | Android 专用配置 |

---

## 二、DNS 段（RawDNS struct）

定义于 `config/config.go` → `RawDNS`。默认值来自 `DefaultRawConfig().DNS`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用内置 DNS，关闭则使用系统 DNS |
| `prefer-h3` | `bool` | `false` | DoH 是否支持 HTTP/3，将并发尝试 |
| `ipv6` | `bool` | `false` | 是否返回 AAAA 记录，`false` 返回空结果 |
| `ipv6-timeout` | `uint` | `100` | 双栈并发时等待 AAAA 的时间（ms） |
| `use-hosts` | `bool` | `true` | 是否查询自定义 hosts |
| `use-system-hosts` | `bool` | `true` | 是否查询系统 hosts |
| `respect-rules` | `bool` | `false` | nameserver/fallback/nameserver-policy 连接是否遵守 rules 规则；开启时 `proxy-server-nameserver` 不能为空 |
| `nameserver` | `[]string` | `["https://doh.pub/dns-query","tls://223.5.5.5:853"]` | 主 DNS 服务器列表 |
| `fallback` | `[]string` | `nil` | 备用 DNS，当 nameserver 解析 IP 非 CN 时使用 |
| `fallback-filter` | `RawFallbackFilter` | 见下 | fallback 使用条件 |
| `fallback-lazy-query` | `bool` | `false` | 为 `true` 时先判断 nameserver 结果是否满足 fallback-filter 再发查询 |
| `listen` | `string` | `""` | DNS 服务器监听地址（如 `0.0.0.0:53`） |
| `listen-routing-mark` | `int` | `0` | DNS 监听 socket 的 routing-mark（仅 Linux） |
| `enhanced-mode` | `C.DNSMode` | `fake-ip`（`DNSMapping` 即 `redir-host`） | DNS 增强模式，可选 `fake-ip` / `redir-host` |
| `fake-ip-range` | `string` | `"198.18.0.1/16"` | fake-ip IPv4 池（必须是 IPv4 前缀） |
| `fake-ip-range6` | `string` | `""` | fake-ip IPv6 池（必须是 IPv6 前缀） |
| `fake-ip-filter` | `[]string` | `["dns.msftnsci.com","www.msftnsci.com","www.msftconnecttest.com"]` | 不使用 fake-ip 的域名列表；`fake-ip-filter-mode: rule` 时为规则列表 |
| `fake-ip-filter-mode` | `C.FilterMode` | `blacklist` | fake-ip-filter 匹配模式，可选 `blacklist` / `whitelist` / `rule` |
| `fake-ip-ttl` | `int` | `1` | fake-ip 查询返回的 TTL |
| `default-nameserver` | `[]string` | `["114.114.114.114","223.5.5.5","8.8.8.8","1.0.0.1"]` | 用于解析其他 DNS 服务器域名的 DNS，必须为纯 IP |
| `cache-algorithm` | `string` | `""` | DNS 缓存算法，可选 `arc` / `lru` |
| `cache-max-size` | `int` | `0` | DNS 缓存最大大小 |
| `nameserver-policy` | `*orderedmap.OrderedMap[string, any]` | `nil` | 按域名指定 DNS 服务器，key 支持 `geosite:xxx` / `rule-set:xxx` / `+.domain.com` / 逗号分隔多 key |
| `proxy-server-nameserver` | `[]string` | `nil` | 专用于节点域名解析的 DNS；`respect-rules: true` 时必填 |
| `proxy-server-nameserver-policy` | `*orderedmap.OrderedMap[string, any]` | `nil` | 节点域名解析策略，格式同 nameserver-policy；仅当 proxy-server-nameserver 非空时生效 |
| `direct-nameserver` | `[]string` | `nil` | 专用于 direct 出口域名解析的 DNS |
| `direct-nameserver-follow-policy` | `bool` | `false` | direct-nameserver 是否遵循 nameserver-policy |

### fallback-filter（RawFallbackFilter）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `geoip` | `bool` | `true` | 是否使用 GeoIP 判断 |
| `geoip-code` | `string` | `"CN"` | GeoIP 国家代码 |
| `ipcidr` | `[]string` | `[]` | 匹配此 CIDR 时使用 fallback |
| `domain` | `[]string` | `nil` | 匹配这些域名直接使用 fallback |
| `geosite` | `[]string` | `[]` | 匹配这些 geosite 直接使用 fallback（**已废弃**，请用 nameserver-policy） |

### DNS 服务器 URL 格式（parseNameServer 支持的 scheme）

| scheme | 说明 | 默认端口 |
|---|---|---|
| `udp://` | 普通 UDP DNS | 53 |
| `tcp://` | TCP DNS | 53 |
| `tls://` | DNS over TLS (DoT) | 853 |
| `https://` / `http://` | DNS over HTTPS (DoH) | 443 / 80 |
| `quic://` | DNS over QUIC (DoQ) | 853 |
| `system://` | 系统 DNS | — |
| `dhcp://` | DHCP DNS | — |
| `ts://` / `tailscale://` | Tailscale DNS | — |
| `rcode://` | 返回指定 RCODE（`success`/`format_error`/`server_failure`/`name_error`/`not_implemented`/`refused`） | — |

- URL fragment（`#` 后）支持参数：`#h3=true`（强制 HTTP/3）、`#ProxyName`（指定代理/网卡）、`#RULES`（等同 respect-rules）
- 纯 IP 地址（如 `8.8.8.8`）自动加 `udp://` 前缀

---

## 三、tun 段（RawTun struct）

定义于 `config/config.go` → `RawTun`。默认值来自 `DefaultRawConfig().Tun`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用 TUN |
| `device` | `string` | `""` | TUN 设备名 |
| `stack` | `C.TUNStack` | `gvisor` | TUN 协议栈，可选 `system` / `gvisor` / `mixed` / `mips` |
| `dns-hijack` | `[]string` | `["0.0.0.0:53"]` | 劫持的 DNS 地址 |
| `auto-route` | `bool` | `true` | 自动配置路由表 |
| `auto-detect-interface` | `bool` | `true` | 自动识别出口网卡 |
| `mtu` | `uint32` | `0`（内部默认 9000） | 最大传输单元 |
| `gso` | `bool` | `false` | 通用分段卸载（仅 Linux） |
| `gso-max-size` | `uint32` | `0` | GSO 包最大大小 |
| `inet4-address` | （已移除 yaml tag） | 内部从 fake-ip-range 推导 `/30` | IPv4 地址段 |
| `inet6-address` | `[]netip.Prefix` | `["fdfe:dcba:9876::1/126"]` | IPv6 地址段 |
| `iproute2-table-index` | `int` | `0` | iproute2 表索引 |
| `iproute2-rule-index` | `int` | `0` | iproute2 规则索引 |
| `auto-redirect` | `bool` | `false` | 自动配置 iptables 重定向 TCP（仅 Linux） |
| `auto-redirect-input-mark` | `uint32` | `0` | auto-redirect input mark |
| `auto-redirect-output-mark` | `uint32` | `0` | auto-redirect output mark |
| `auto-redirect-iproute2-fallback-rule-index` | `int` | `0` | auto-redirect iproute2 fallback 规则索引 |
| `loopback-address` | `[]netip.Addr` | `nil` | 环回地址 |
| `strict-route` | `bool` | `false` | 将所有连接路由到 tun 防止泄漏 |
| `route-address` | `[]netip.Prefix` | `nil` | 自定义路由（替代默认路由） |
| `route-address-set` | `[]string` | `nil` | 将规则集 IP CIDR 添加到防火墙（仅 Linux nftables，需 auto-route+auto-redirect） |
| `route-exclude-address` | `[]netip.Prefix` | `nil` | 排除路由的地址 |
| `route-exclude-address-set` | `[]string` | `nil` | 排除规则集 IP CIDR 添加到防火墙 |
| `include-interface` | `[]string` | `nil` | 限制被路由的接口 |
| `exclude-interface` | `[]string` | `nil` | 排除路由的接口 |
| `include-uid` | `[]uint32` | `nil` | 限制路由的 UID（仅 Linux） |
| `include-uid-range` | `[]string` | `nil` | 限制路由的 UID 范围（如 `1000:9999`） |
| `exclude-uid` | `[]uint32` | `nil` | 排除路由的 UID |
| `exclude-uid-range` | `[]string` | `nil` | 排除路由的 UID 范围 |
| `exclude-src-port` | `[]uint16` | `nil` | 排除的源端口 |
| `exclude-src-port-range` | `[]string` | `nil` | 排除的源端口范围 |
| `exclude-dst-port` | `[]uint16` | `nil` | 排除的目标端口 |
| `exclude-dst-port-range` | `[]string` | `nil` | 排除的目标端口范围 |
| `include-android-user` | `[]int` | `nil` | 限制路由的 Android 用户（仅 Android） |
| `include-package` | `[]string` | `nil` | 限制路由的 Android 包名（仅 Android） |
| `exclude-package` | `[]string` | `nil` | 排除路由的 Android 包名 |
| `include-mac-address` | `[]string` | `nil` | 限制路由的 MAC 地址 |
| `exclude-mac-address` | `[]string` | `nil` | 排除路由的 MAC 地址 |
| `endpoint-independent-nat` | `bool` | `false` | 启用独立于端点的 NAT |
| `udp-timeout` | `int64` | `0` | UDP 超时（秒） |
| `icmp-timeout` | `int64` | `0` | ICMP 超时（秒） |
| `disable-icmp-forwarding` | `bool` | `false` | 禁用 ICMP 转发 |
| `file-descriptor` | `int` | `0` | TUN 文件描述符 |
| `inet4-route-address` | `[]netip.Prefix` | `nil` | 自定义 IPv4 路由（旧写法） |
| `inet6-route-address` | `[]netip.Prefix` | `nil` | 自定义 IPv6 路由（旧写法） |
| `inet4-route-exclude-address` | `[]netip.Prefix` | `nil` | 排除的 IPv4 路由 |
| `inet6-route-exclude-address` | `[]netip.Prefix` | `nil` | 排除的 IPv6 路由 |
| `recvmsgx` | `bool` | `true` | darwin: 使用 RecvMsgX |
| `sendmsgx` | `bool` | `false` | darwin: 使用 SendMsgX（默认关闭，多线程下载可能冻结） |

---

## 四、sniffer 段（RawSniffer struct）

定义于 `config/config.go` → `RawSniffer`。默认值来自 `DefaultRawConfig().Sniffer`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用域名嗅探 |
| `override-destination` | `bool` | `true` | 是否使用嗅探结果作为实际访问目标；全局配置，优先级低于 `sniff` 子项 |
| `sniffing` | `[]string` | `nil` | 需要嗅探的协议名列表（**已废弃**，若配置 `sniff` 则此项无效） |
| `force-domain` | `[]string` | `[]` | 强制对此域名进行嗅探 |
| `skip-src-address` | `[]string` | `nil` | 对来源 IP 跳过嗅探（支持 CIDR / `geoip:` / `rule-set:`） |
| `skip-dst-address` | `[]string` | `nil` | 对目标 IP 跳过嗅探 |
| `skip-domain` | `[]string` | `[]` | 对嗅探结果进行跳过 |
| `port-whitelist` | `[]string` | `[]` | 仅对白名单中的端口进行嗅探（**已废弃**，若配置 `sniff` 则无效） |
| `force-dns-mapping` | `bool` | `true` | 对 redir-host 类型识别的流量进行强制嗅探 |
| `parse-pure-ip` | `bool` | `true` | 对所有未获取到域名的流量进行强制嗅探 |
| `sniff` | `map[string]RawSniffingConfig` | `{}` | 按协议配置嗅探，key 为协议名（`TLS` / `HTTP` / `QUIC`） |

### sniff 子项（RawSniffingConfig）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `ports` | `[]string` | `nil` | 该协议需要嗅探的端口；TLS/QUIC 默认 443，HTTP 默认 80 |
| `override-destination` | `*bool` | `nil`（继承全局） | 可覆盖 `sniffer.override-destination` |

---

## 五、profile 段（RawProfile struct）

定义于 `config/config.go` → `RawProfile`。默认值来自 `DefaultRawConfig().Profile`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `store-selected` | `bool` | `true` | 存储 select 选择记录 |
| `store-fake-ip` | `bool` | `false`（Hako 内部覆盖为 `true` 以持久化 fake-ip 映射） | 持久化 fake-ip |

> 注：`store-fake-ip` 有特殊处理。`RawProfile.UnmarshalYAML` 会记录 `StoreFakeIPSet` 字段标记文档是否显式声明了 `store-fake-ip`，Hako 在 iOS Network Extension 场景下会据此区分"未声明"与"显式 false"，从而默认开启持久化。`StoreFakeIPSet` 的 yaml tag 为 `"-"`（不暴露）。

---

## 六、tls 段（RawTLS struct）

定义于 `config/config.go` → `RawTLS`。无默认值（零值）。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `certificate` | `string` | `""` | 证书 PEM 格式或路径 |
| `private-key` | `string` | `""` | 证书私钥 PEM 格式或路径 |
| `client-auth-type` | `string` | `""` | mTLS 类型，可选 `""` / `request` / `require-any` / `verify-if-given` / `require-and-verify` |
| `client-auth-cert` | `string` | `""` | 客户端证书 PEM 格式或路径 |
| `ech-key` | `string` | `""` | ECH 密钥（`mihomo generate ech-keypair` 生成） |
| `custom-certifactes` | `[]string` | `nil` | 自定义信任证书 PEM 列表 |

---

## 七、ntp 段（RawNTP struct）

定义于 `config/config.go` → `RawNTP`。默认值来自 `DefaultRawConfig().NTP`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用 NTP |
| `server` | `string` | `"time.apple.com"` | NTP 服务器 |
| `port` | `int` | `123` | NTP 端口 |
| `interval` | `int` | `30` | 同步间隔（分钟） |
| `dialer-proxy` | `string` | `""` | NTP 连接使用的代理 |
| `write-to-system` | `bool` | `false` | 是否写入系统时间 |

---

## 八、iptables 段（RawIPTables struct）

定义于 `config/config.go` → `RawIPTables`。默认值来自 `DefaultRawConfig().IPTables`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用 iptables |
| `inbound-interface` | `string` | `"lo"` | 入站接口 |
| `bypass` | `[]string` | `[]` | 旁路地址 |
| `dns-redirect` | `bool` | `true` | 是否重定向 DNS |

---

## 九、experimental 段（RawExperimental struct）

定义于 `config/config.go` → `RawExperimental`。默认值来自 `DefaultRawConfig().Experimental`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `fingerprints` | `[]string` | `nil` | 全局 TLS 指纹列表 |
| `quic-go-disable-gso` | `bool` | `false` | 禁用 quic-go GSO（仅 Linux） |
| `quic-go-disable-ecn` | `bool` | `true` | 禁用 quic-go ECN（默认开启，因平台兼容性） |
| `dialer-ip4p-convert` | `bool` | `false` | 启用 IP4P 转换 |

---

## 十、tuic-server 段（RawTuicServer struct）

定义于 `config/config.go` → `RawTuicServer`。默认值来自 `DefaultRawConfig().TuicServer`。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用 TUIC 入站 |
| `listen` | `string` | `""` | 监听地址 |
| `token` | `[]string` | `nil` | tuicV4 token |
| `users` | `map[string]string` | `nil` | tuicV5 用户（`uuid:password`） |
| `certificate` | `string` | `""` | 证书 |
| `private-key` | `string` | `""` | 私钥 |
| `congestion-controller` | `string` | `""` | 拥塞控制（如 `bbr`） |
| `max-idle-time` | `int` | `15000` | 最大空闲时间（ms） |
| `authentication-timeout` | `int` | `1000` | 认证超时（ms） |
| `alpn` | `[]string` | `["h3"]` | ALPN |
| `max-udp-relay-packet-size` | `int` | `1500` | 最大 UDP 中继包大小 |
| `cwnd` | `int` | `0` | 拥塞窗口 |

---

## 十一、tunnels 段

`[]LC.Tunnel`，支持两种写法：

**单行格式**：`tcp/udp,127.0.0.1:6553,114.114.114.114:53,proxy`

**YAML 格式**：

| YAML 字段 | Go 类型 | 说明 |
|---|---|---|
| `network` | `[]string` | 协议，`tcp` / `udp` |
| `address` | `string` | 监听地址 |
| `target` | `string` | 目标地址 |
| `proxy` | `string` | 使用的代理（可为空） |

---

## 十二、hosts 段

`map[string]any`，类似 `/etc/hosts`，仅支持配置单个 IP 或域名别名。

- `'*.mihomo.dev': 127.0.0.1` — 通配域名
- `test.com: [1.1.1.1, 2.2.2.2]` — 多 IP
- `home.lan: lan` — 特殊字段，加入本地所有网卡地址
- `baidu.com: google.com` — 域名别名（仅允许一个）

---

## 十三、rules 段（规则语法）

规则格式：`TYPE,PAYLOAD,TARGET(,params...)`，或 `MATCH,TARGET`。

### 支持的规则类型（来自 `rules/parser.go`）

| 规则类型 | Payload | 说明 | 支持参数 |
|---|---|---|---|
| `DOMAIN` | 精确域名 | 完全匹配域名 | — |
| `DOMAIN-SUFFIX` | 域名后缀 | 匹配域名后缀 | — |
| `DOMAIN-KEYWORD` | 关键词 | 匹配域名中包含的关键词 | — |
| `DOMAIN-REGEX` | 正则表达式 | 正则匹配域名（payload 可含逗号） | — |
| `DOMAIN-WILDCARD` | 通配符 | 通配符匹配域名（如 `test.*.mihomo.com`） | — |
| `GEOSITE` | 分类名 | GeoSite 匹配 | — |
| `GEOIP` | 国家代码 | GeoIP 匹配 | `src` / `no-resolve` |
| `SRC-GEOIP` | 国家代码 | 源 IP GeoIP 匹配 | — |
| `IP-ASN` | ASN 号 | IP ASN 匹配 | `src` / `no-resolve` |
| `SRC-IP-ASN` | ASN 号 | 源 IP ASN 匹配 | — |
| `IP-CIDR` | CIDR | IPv4 CIDR 匹配 | `src` / `no-resolve` |
| `IP-CIDR6` | CIDR | IPv6 CIDR 匹配 | `src` / `no-resolve` |
| `SRC-IP-CIDR` | CIDR | 源 IP CIDR 匹配 | — |
| `IP-SUFFIX` | IP 后缀 | IP 后缀匹配 | `src` / `no-resolve` |
| `SRC-IP-SUFFIX` | IP 后缀 | 源 IP 后缀匹配 | — |
| `SRC-PORT` | 端口/范围 | 源端口匹配 | — |
| `DST-PORT` | 端口/范围 | 目标端口匹配 | — |
| `IN-PORT` | 端口/范围 | 入站端口匹配 | — |
| `DSCP` | DSCP 值 | DSCP 标记匹配 | — |
| `PROCESS-NAME` | 进程名 | 进程名匹配 | — |
| `PROCESS-PATH` | 进程路径 | 进程路径匹配 | — |
| `PROCESS-NAME-REGEX` | 正则 | 进程名正则匹配 | — |
| `PROCESS-PATH-REGEX` | 正则 | 进程路径正则匹配 | — |
| `PROCESS-NAME-WILDCARD` | 通配符 | 进程名通配符匹配 | — |
| `PROCESS-PATH-WILDCARD` | 通配符 | 进程路径通配符匹配 | — |
| `NETWORK` | `tcp`/`udp` | 网络类型匹配 | — |
| `UID` | UID | UID 匹配（Linux） | — |
| `SOURCE-APP-SIGNING-ID` | 签名 ID | iOS 源 App 签名 ID | — |
| `SOURCE-APP-TEAM-ID` | Team ID | iOS 源 App Team ID | — |
| `IN-TYPE` | 入站类型 | 入站类型匹配 | — |
| `IN-USER` | 用户名 | 入站用户匹配 | — |
| `IN-NAME` | 入站名 | 入站名称匹配 | — |
| `REMATCH-NAME` | rematch 名称 | Rematch 名称匹配 | — |
| `SUB-RULE` | 逻辑表达式 | 子规则集（payload 为逻辑规则） | — |
| `AND` | 逻辑表达式 | AND 逻辑规则（payload 可含逗号） | — |
| `OR` | 逻辑表达式 | OR 逻辑规则（payload 可含逗号） | — |
| `NOT` | 逻辑表达式 | NOT 逻辑规则（payload 可含逗号） | — |
| `RULE-SET` | 规则集名 | 引用 rule-provider | `src` / `no-resolve` |
| `MATCH` | 无 | 全匹配（无 payload，直接跟 target） | — |

### 规则参数

| 参数 | 说明 |
|---|---|
| `src` | 匹配源 IP（隐含 `no-resolve`） |
| `no-resolve` | 不解析 DNS，仅匹配 IP 类型规则 |

### 逻辑规则语法

- `AND,((DOMAIN,google.com),(NETWORK,TCP)),PROXY`
- `OR,((NETWORK,TCP),(NETWORK,UDP)),PROXY`
- `NOT,((DOMAIN,google.com)),DIRECT`
- `SUB-RULE,(OR,((NETWORK,TCP),(NETWORK,UDP))),sub-rule-name1`

### sub-rules 段

`map[string][]string`，定义子规则集，配合 `SUB-RULE` 使用：

```yaml
sub-rules:
  sub-rule-name1:
    - DOMAIN,google.com,ss1
    - DOMAIN,baidu.com,DIRECT
```

---

## 十四、rule-providers 段

定义于 `rules/provider/parse.go` → `ruleProviderSchema`。使用 `provider` tag。

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `type` | `string` | —（必填） | 类型，可选 `http` / `file` / `inline` |
| `behavior` | `string` | —（必填） | 行为类型，可选 `domain` / `ipcidr` / `classical` |
| `path` | `string` | `""` | 本地存储路径（默认存 Home Dir rules 文件夹） |
| `url` | `string` | `""` | 下载 URL（`type: http` 时） |
| `proxy` | `string` | `""` | 下载使用的代理 |
| `format` | `string` | `""` | 格式，可选 `yaml` / `text` / `mrs`（mrs 仅支持 domain/ipcidr） |
| `interval` | `int` | `0` | 更新间隔（秒） |
| `size-limit` | `int64` | `0` | 限制下载文件最大大小（字节），0 为不限 |
| `payload` | `[]string` | `nil` | 内联规则内容（`type: inline` 时） |
| `header` | `map[string][]string` | `nil` | 自定义 HTTP 请求头（`type: http` 时） |
| `path-in-bundle` | `string` | `""` | BundleMRS.7z 中的路径，本地文件不存在时从 bundle 解压 |

### rule-provider 示例

```yaml
rule-providers:
  rule1:
    behavior: classical
    interval: 259200
    path: /path/to/save/file.yaml
    type: http
    url: "url"
    proxy: DIRECT
    # size-limit: 10240
  rule3:
    type: http
    url: "url"
    format: mrs
    behavior: domain
    path: /path/to/save/file.mrs
    # path-in-bundle: "geo/geosite/cn.mrs"
  rule4:
    type: inline
    behavior: domain
    payload:
      - '.blogger.com'
      - '*.*.microsoft.com'
```

---

## 十五、proxy-groups 段

通用字段来自 `outboundgroup.GroupCommonOption`（`group` tag），各类型特有字段来自对应 Option struct。

### 通用字段（GroupCommonOption）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `name` | `string` | —（必填） | 策略组名称 |
| `type` | `string` | —（必填） | 类型，可选 `select` / `url-test` / `fallback` / `load-balance` |
| `proxies` | `[]string` | `nil` | 包含的代理列表 |
| `use` | `[]string` | `nil` | 引用的 proxy-provider 列表 |
| `url` | `string` | `""`（默认 `https://www.gstatic.com/generate_204`） | 健康检查 URL |
| `interval` | `int` | `0`（select/relay 不需要；其他默认 `300`） | 健康检查间隔（秒） |
| `timeout` | `int` | `0`（内部默认 `5000` ms） | 测试超时（ms） |
| `max-failed-times` | `int` | `0`（内部默认 `5`） | 最大失败次数，超过后激活健康检查 |
| `empty-fallback` | `string` | `"COMPATIBLE"` | 组为空时的回退代理（不支持填代理组） |
| `lazy` | `bool` | `true` | 是否懒加载健康检查 |
| `disable-udp` | `bool` | `false` | 是否禁用 UDP |
| `filter` | `string` | `""` | 正则表达式过滤节点名（多规则用 `` ` `` 分隔） |
| `exclude-filter` | `string` | `""` | 正则排除节点名 |
| `exclude-type` | `string` | `""` | 排除的代理类型（`|` 分隔） |
| `expected-status` | `string` | `""`（内部默认 `"*"`） | 期望的 HTTP 状态码 |
| `include-all` | `bool` | `false` | 包含所有代理和 provider（等同 include-all-proxies + include-all-providers） |
| `include-all-proxies` | `bool` | `false` | 包含所有代理（proxies 段） |
| `include-all-providers` | `bool` | `false` | 包含所有 proxy-provider |
| `hidden` | `bool` | `false` | 是否在 UI 中隐藏 |
| `icon` | `string` | `""` | 图标 URL |

> **已移除字段**：`routing-mark`、`interface-name`、`dialer-proxy`（仅打印警告，应直接在 proxy 上设置）
> **已移除类型**：`relay`（应使用 `dialer-proxy` 代替）

### select 特有字段（SelectorOption）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `default-selected` | `string` | `""` | 默认选择的节点（空或不存在时选第一个） |

### url-test 特有字段（URLTestOption）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `tolerance` | `uint16` | `0` | 延迟容差（ms） |

### fallback 特有字段（FallbackOption）

无额外字段（`FallbackOption` 为空 struct）。

### load-balance 特有字段（LoadBalanceOption）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `strategy` | `string` | `""`（默认 `round-robin`） | 负载均衡策略，可选 `round-robin` / `consistent-hashing` / `sticky-sessions` |

### proxy-groups 示例

```yaml
proxy-groups:
  - name: "auto"
    type: url-test
    proxies: [ss1, ss2, vmess1]
    # tolerance: 150
    # lazy: true
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  - name: "fallback-auto"
    type: fallback
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  - name: "load-balance"
    type: load-balance
    proxies: [ss1, ss2, vmess1]
    # strategy: consistent-hashing
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  - name: Proxy
    type: select
    proxies: [ss1, ss2, vmess1, auto]
    # default-selected: ss1

  - name: UseProvider
    type: select
    filter: "HK|TW"
    use: [provider1]
    proxies: [Proxy, DIRECT]
```

---

## 十六、proxy-providers 段

定义于 `adapter/provider/parser.go` → `proxyProviderSchema`（`provider` tag）。

### 主字段（proxyProviderSchema）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `type` | `string` | —（必填） | 类型，可选 `http` / `file` / `inline` |
| `path` | `string` | `""` | 本地存储路径（默认存 Home Dir proxies 文件夹，文件名为 url md5） |
| `url` | `string` | `""` | 下载 URL |
| `proxy` | `string` | `""` | 下载使用的代理 |
| `interval` | `int` | `0` | 更新间隔（秒） |
| `filter` | `string` | `""` | 正则过滤节点名 |
| `exclude-filter` | `string` | `""` | 正则排除节点名 |
| `exclude-type` | `string` | `""` | 排除的代理类型 |
| `dialer-proxy` | `string` | `""` | dialer-proxy |
| `size-limit` | `int64` | `0` | 限制下载文件大小（字节） |
| `payload` | `[]map[string]any` | `nil` | 内联节点内容（`type: inline` 时） |
| `age-secret-key` | `string` | `""` | age 加密配置的解密密钥 |
| `health-check` | `healthCheckSchema` | 见下 | 健康检查配置 |
| `override` | `overrideSchema` | 见下 | 覆写节点配置 |
| `header` | `map[string][]string` | `nil` | 自定义 HTTP 请求头 |

### health-check 子项（healthCheckSchema）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `enable` | `bool` | `false` | 是否启用健康检查 |
| `url` | `string` | `""` | 健康检查 URL |
| `interval` | `int` | `0`（启用时默认 `300`） | 检查间隔（秒） |
| `timeout` | `int` | `0` | 测试超时（ms） |
| `lazy` | `bool` | `true` | 是否懒加载 |
| `expected-status` | `string` | `""` | 期望 HTTP 状态码 |

### override 子项（overrideSchema）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `tfo` | `*bool` | `nil` | 覆写 TFO |
| `mptcp` | `*bool` | `nil` | 覆写 MPTCP |
| `udp` | `*bool` | `nil` | 覆写 UDP |
| `udp-over-tcp` | `*bool` | `nil` | 覆写 UDP over TCP |
| `up` | `*string` | `nil` | 覆写上传带宽 |
| `down` | `*string` | `nil` | 覆写下带宽 |
| `dialer-proxy` | `*string` | `nil` | 覆写 dialer-proxy |
| `skip-cert-verify` | `*bool` | `nil` | 覆写跳过证书验证 |
| `name-cert-verify` | `*string` | `nil` | 覆写证书 DNSName 校验目标 |
| `interface-name` | `*string` | `nil` | 覆写出口网卡 |
| `routing-mark` | `*int` | `nil` | 覆写 routing-mark |
| `ip-version` | `*string` | `nil` | 覆写 IP 版本 |
| `additional-prefix` | `*string` | `nil` | 节点名前缀 |
| `additional-suffix` | `*string` | `nil` | 节点名后缀 |
| `proxy-name` | `[]overrideProxyNameSchema` | `nil` | 节点名正则替换，每项含 `pattern`（正则）和 `target`（替换内容） |
| `override-expr` | `[]OverrideExpr` | `nil` | yq v4 风格的表达式覆盖，按顺序执行 |

### proxy-provider 示例

```yaml
proxy-providers:
  provider1:
    type: http
    url: "url"
    interval: 3600
    path: ./provider1.yaml
    proxy: DIRECT
    # size-limit: 10240
    # age-secret-key: AGE-SECRET-KEY-...
    header:
      User-Agent:
        - "mihomo/1.18.3"
    health-check:
      enable: true
      interval: 600
      url: https://cp.cloudflare.com/generate_204
    override:
      skip-cert-verify: true
      udp: true
      # additional-prefix: "[provider1]"
      # proxy-name:
      #   - pattern: "test"
      #     target: "TEST"

  provider2:
    type: inline
    dialer-proxy: proxy
    payload:
      - name: "ss1"
        type: ss
        server: server
        port: 443
        cipher: chacha20-ietf-poly1305
        password: "password"

  test:
    type: file
    path: /test.yaml
    health-check:
      enable: true
      interval: 36000
      url: https://cp.cloudflare.com/generate_204
```

---

## 十七、listeners 段（入站监听）

定义于 `listener/parse.go` → `ParseListener`。每个 listener 为一个 map，通用字段来自 `inbound.BaseOption`。

### 通用字段（BaseOption，`inbound` tag）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `name` | `string` | —（必填） | 监听名称 |
| `listen` | `string` | `"0.0.0.0"` | 监听 IP |
| `port` | `string` | —（必填） | 监听端口，支持 ports 格式（如 `200,302` 或 `200,204,401-429,501-503`） |
| `rule` | `string` | `""` | 使用的 sub-rule 名称（默认用 rules） |
| `proxy` | `string` | `""` | 直接将流量交由指定 proxy 处理 |
| `routing-mark` | `int` | `0` | 监听 socket 的 routing-mark（仅 Linux） |

### 支持的 listener 类型（来自 `listener/parse.go`）

| type | 说明 | 特有字段 |
|---|---|---|
| `socks` | SOCKS5 入站 | `users`, `udp`(默认true), `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `reality-config` |
| `http` | HTTP 入站 | `users`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `reality-config` |
| `mixed` | HTTP+SOCKS 混合入站 | `users`, `udp`(默认true), `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `reality-config` |
| `redir` | 透明代理入站（Linux redir） | 无额外字段 |
| `tproxy` | TProxy 入站（Linux） | `udp`(默认true) |
| `tunnel` | 隧道入站 | `network`(`[]string`，必填), `target`(string，必填) |
| `tun` | TUN 入站（高级用户） | 同顶层 tun 段字段 |
| `shadowsocks` | Shadowsocks 入站 | `password`, `cipher`, `udp`(默认true), `mux-option`, `shadow-tls`, `res-tls`, `jls-config`, `kcp-tun`, `simple-obfs` |
| `snell` | Snell 入站 | `psk`, `version`, `udp`(默认true), `obfs-opts`, `shadow-tls`, `res-tls`, `jls-config` |
| `vmess` | Vmess 入站 | `users`(`[{username,uuid,alterId}]`), `ws-path`, `grpc-service-name`, `mekya-config`, `mkcp-config`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `jls-config`, `shadow-tls`, `res-tls`, `reality-config`, `tlsmirror-config` |
| `vless` | Vless 入站 | `users`(`[{username,uuid,flow}]`), `decryption`, `ws-path`, `xhttp-config`, `grpc-service-name`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `allow-insecure`, `shadow-tls`, `res-tls`, `jls-config`, `reality-config` |
| `trojan` | Trojan 入站 | `users`(`[{username,password}]`), `ws-path`, `grpc-service-name`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `allow-insecure`, `shadow-tls`, `res-tls`, `jls-config`, `reality-config`, `mux-option`, `ss-option` |
| `tuic` | TUIC 入站 | `token`, `users`(map), `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `congestion-controller`(默认bbr), `max-idle-time`(默认15000), `authentication-timeout`(默认1000), `alpn`(默认["h3"]), `max-udp-relay-packet-size`(默认1500), `cwnd` |
| `shadowquic` | ShadowQUIC 入站 | `users`(`[{username,password}]`), `jls-upstream`, `alpn`(默认["h3"]), `quic-versions`, `zero-rtt`(默认true), `congestion-controller`(默认bbr), `up`, `down`, `ignore-client-bandwidth`, `max-idle-time`(默认30000), `max-datagram-frame-size`(默认1400), `recv-window-conn`, `recv-window`, `disable-mtu-discovery`, `cwnd` |
| `anytls` | AnyTLS 入站 | `users`(map), `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `shadow-tls`, `res-tls`, `jls-config`, `allow-insecure`, `padding-scheme` |
| `mieru` | Mieru 入站 | `transport`(`"TCP"`/`"UDP"`), `users`(map), `traffic-pattern`, `user-hint-is-mandatory` |
| `sudoku` | Sudoku 入站 | `key`, `aead-method`, `padding-min`, `padding-max`, `table-type`, `custom-table`, `custom-tables`, `handshake-timeout`, `enable-pure-downlink`, `disable-http-mask`, `http-mask-mode`, `httpmask`(对象) |
| `trusttunnel` | TrustTunnel 入站 | `users`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `network`, `congestion-controller`, `cwnd`, `bbr-profile` |
| `hysteria2` | Hysteria2 入站 | `users`(map), `obfs`, `obfs-password`, `obfs-min-packet-size`, `obfs-max-packet-size`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `max-idle-time`, `alpn`, `up`, `down`, `masquerade`, `bbr-profile`, `ignore-client-bandwidth`, `realm-opts` |
| `hysteria2-realm` | Hysteria2 Realm 服务器 | `token`, `max-realms`, `max-realms-per-ip`, `trusted-proxy-header`, `realm-name-pattern`, `certificate`, `private-key`, `client-auth-type`, `client-auth-cert`, `ech-key`, `alpn` |

### users 通用格式

**列表格式**（AuthUsers）：
```yaml
users:
  - username: aaa
    password: aaa
```

**Map 格式**（部分类型如 tuic/hysteria2/anytls/mieru）：
```yaml
users:
  00000000-0000-0000-0000-000000000000: PASSWORD_0
```

### listeners 示例

```yaml
listeners:
  - name: socks5-in-1
    type: socks
    port: 10808
    # listen: 0.0.0.0
    # udp: true
    # users: []
    # certificate / private-key / client-auth-type / client-auth-cert / ech-key

  - name: http-in-1
    type: http
    port: 10809

  - name: mixed-in-1
    type: mixed
    port: 10810

  - name: redir-in-1
    type: redir
    port: 10811

  - name: tproxy-in-1
    type: tproxy
    port: 10812

  - name: shadowsocks-in-1
    type: shadowsocks
    port: 10813
    password: vlmpIPSyHH6f4S8WVPdRIHIlzmB+GIRfoH3aNJ/t9Gg=
    cipher: 2022-blake3-aes-256-gcm

  - name: tunnel-in-1
    type: tunnel
    port: 10816
    network: [tcp, udp]
    target: target.com

  - name: vmess-in-1
    type: vmess
    port: 10814
    users:
      - username: 1
        uuid: 9d0cb9d0-964f-4ef6-897d-6c6b3ccf9e68
        alterId: 1

  - name: tun-in-1
    type: tun
    stack: system
    dns-hijack:
      - 0.0.0.0:53
    inet4-address:
      - 198.19.0.1/30
    inet6-address:
      - "fdfe:dcba:9877::1/126"
```

---

## 十八、proxies 段（代理节点类型）

定义于 `adapter/parser.go` → `ParseProxy`。支持的 type：

| type | 说明 |
|---|---|
| `ss` | Shadowsocks |
| `ssr` | ShadowsocksR |
| `socks5` | SOCKS5 |
| `http` | HTTP/HTTPS |
| `vmess` | VMess |
| `vless` | VLESS |
| `snell` | Snell |
| `trojan` | Trojan |
| `hysteria` | Hysteria v1 |
| `hysteria2` | Hysteria v2 |
| `wireguard` | WireGuard |
| `tuic` | TUIC |
| `shadowquic` | ShadowQUIC |
| `gost-relay` | GOST Relay |
| `direct` | DIRECT（自定义 interface/routing-mark） |
| `dns` | DNS 出站（劫持到内部 DNS） |
| `reject` | REJECT |
| `rematch` | Rematch（重匹配） |
| `ssh` | SSH |
| `mieru` | Mieru |
| `anytls` | AnyTLS |
| `sudoku` | Sudoku |
| `masque` | MASQUE |
| `trusttunnel` | TrustTunnel |
| `openvpn` | OpenVPN |
| `tailscale` | Tailscale |
| `zerotier` | ZeroTier |

### 内置特殊代理（自动创建）

| 名称 | 说明 |
|---|---|
| `DIRECT` | 直连 |
| `REJECT` | 拒绝 |
| `REJECT-DROP` | 拒绝（丢弃） |
| `COMPATIBLE` | 兼容代理 |
| `PASS` | 透传（不处理） |
| `PASS-RULE` | 透传规则 |
| `GLOBAL` | 全局选择组（自动创建） |

### proxy 通用字段（BasicOption）

所有代理均支持通过 `smux` 字段启用多路复用：

| YAML 字段 | 说明 |
|---|---|
| `smux.enabled` | 是否启用 |
| `smux.protocol` | `smux` / `yamux` / `h2mux` |
| `smux.max-connections` | 最大连接数（与 max-streams 冲突） |
| `smux.min-streams` | 最小流数（与 max-streams 冲突） |
| `smux.max-streams` | 最大流数（与 max-connections 冲突） |
| `smux.padding` | 启用填充 |
| `smux.statistic` | 是否在面板中显示底层连接 |
| `smux.only-tcp` | 仅对 TCP 生效 |

### 通用 TLS/网络字段（多协议共用）

| YAML 字段 | 说明 |
|---|---|
| `server` / `port` | 服务器地址和端口 |
| `udp` | 是否支持 UDP |
| `tls` | 是否启用 TLS |
| `sni` / `servername` | SNI |
| `alpn` | ALPN 列表 |
| `skip-cert-verify` | 跳过证书验证 |
| `name-cert-verify` | 证书 DNSName 校验目标 |
| `fingerprint` | TLS 指纹（SSL Pinning） |
| `client-fingerprint` | 客户端指纹（`chrome`/`firefox`/`safari`/`ios`/`random`/`none`） |
| `certificate` / `private-key` | mTLS 客户端证书和私钥 |
| `ech-opts` | ECH 配置（`enable`, `config`, `query-server-name`） |
| `dialer-proxy` | 链式代理 |
| `interface-name` | 出口网卡 |
| `routing-mark` | Linux fwmark |
| `ip-version` | IP 版本（`dual`/`ipv4`/`ipv6`/`ipv4-prefer`/`ipv6-prefer`） |
| `network` | 传输层（`tcp`/`ws`/`h2`/`grpc`/`mkcp`/`mekya`/`xhttp`） |

---

## 十九、clash-for-android 段（RawClashForAndroid）

| YAML 字段 | Go 类型 | 默认值 | 说明 |
|---|---|---|---|
| `append-system-dns` | `bool` | `false` | 是否追加系统 DNS |
| `ui-subtitle-pattern` | `string` | `""` | UI 副标题正则 |

---

## 二十、常量枚举值汇总

### TunnelMode（`mode`）
- `global` → `Global`
- `rule` → `Rule`（默认）
- `direct` → `Direct`

### TUNStack（`tun.stack`）
- `gvisor` → `TunGvisor`（默认）
- `system` → `TunSystem`
- `mixed` → `TunMixed`
- `mips` → `TunMips`（v1.19.31+ 新增）

### DNSMode（`dns.enhanced-mode`）
- `fake-ip` → `DNSFakeIP`
- `redir-host` → `DNSMapping`（默认）

### FilterMode（`dns.fake-ip-filter-mode`）
- `blacklist` → `FilterBlackList`（默认）
- `whitelist` → `FilterWhiteList`
- `rule` → `FilterRule`

### FindProcessMode（`find-process-mode`）
- `strict` → `FindProcessStrict`（默认）
- `always` → `FindProcessAlways`
- `off` → `FindProcessOff`

### LogLevel（`log-level`）
- `silent` / `error` / `warning` / `info`（默认）/ `debug`

### Proxy Provider 类型（`proxy-providers.*.type`）
- `http` / `file` / `inline`

### Rule Provider 类型（`rule-providers.*.type`）
- `http` / `file` / `inline`

### Rule Provider behavior（`rule-providers.*.behavior`）
- `domain` / `ipcidr` / `classical`

### Rule Provider format（`rule-providers.*.format`）
- `yaml` / `text` / `mrs`

### Proxy Group 类型（`proxy-groups.*.type`）
- `select` / `url-test` / `fallback` / `load-balance`（`relay` 已移除）

---

## 二十一、完整配置示例参考

以下为 `docs/config.yaml` 的完整结构示例（已精简注释，保留所有字段）：

```yaml
# ===== 入站端口 =====
mixed-port: 10801
# port: 7890
# socks-port: 7891
# redir-port: 7892
# tproxy-port: 7893

allow-lan: true
bind-address: "*"
authentication:
  - "username:password"
skip-auth-prefixes:
  - 127.0.0.1/8
  - ::1/128
lan-allowed-ips:
  - 0.0.0.0/0
  - ::/0
lan-disallowed-ips:
  - 192.168.0.3/32

find-process-mode: strict
mode: rule

geox-url:
  geoip: "https://.../geoip.dat"
  geosite: "https://.../geosite.dat"
  mmdb: "https://.../geoip.metadb"
  asn: "https://.../GeoLite2-ASN.mmdb"
geo-auto-update: false
geo-update-interval: 24
# geodata-mode: true
# geodata-loader: memconservative
# geosite-matcher: succinct

log-level: debug
ipv6: true
# unified-delay: false
# tcp-concurrent: false
# interface-name: en0
# routing-mark: 6666
# global-ua: clash.meta/1.x
# etag-support: true
# keep-alive-idle: 15
# keep-alive-interval: 15
# disable-keep-alive: false

# ===== TLS =====
tls:
  certificate: string
  private-key: string
  # client-auth-type: ""
  # client-auth-cert: string
  # ech-key: |
  custom-certifactes:
    - |

# ===== 外部控制器 =====
external-controller: 0.0.0.0:9093
# external-controller-tls: 0.0.0.0:9443
# secret: "123456"
external-controller-cors:
  allow-origins:
    - "*"
  allow-private-network: true
# external-controller-unix: mihomo.sock
# external-controller-pipe: \\.\pipe\mihomo
# external-controller-routing-mark: 0
external-ui: /path/to/ui/folder/
external-ui-name: xd
external-ui-url: "https://.../gh-pages.zip"
# external-doh-server: /dns-query

# ===== Experimental =====
experimental:
  # quic-go-disable-gso: true
  # quic-go-disable-ecn: true
  # dialer-ip4p-convert: false
  # fingerprints: []

# ===== Hosts =====
hosts:
  '*.mihomo.dev': 127.0.0.1
  'home.lan': lan

# ===== Profile =====
profile:
  store-selected: false
  store-fake-ip: true

# ===== Tun =====
tun:
  enable: false
  stack: system  # gvisor/mixed/mips
  dns-hijack:
    - 0.0.0.0:53
  # auto-route: true
  # auto-detect-interface: true
  # mtu: 9000
  # gso: false
  # gso-max-size: 65536
  # auto-redirect: false
  # strict-route: true
  # route-address: [...]
  # route-address-set: [...]
  # route-exclude-address-set: [...]
  # include-interface: [...]
  # exclude-interface: [...]
  # include-uid: [...]
  # exclude-uid: [...]
  # include-android-user: [...]
  # include-package: [...]
  # exclude-package: [...]
  # endpoint-independent-nat: false
  # disable-icmp-forwarding: true

# ===== Sniffer =====
sniffer:
  enable: false
  # force-dns-mapping: false
  # parse-pure-ip: false
  override-destination: false
  sniff:
    QUIC: {}
    TLS: {}
    HTTP:
      ports: [80, 8080-8880]
      override-destination: true
  force-domain:
    - +.v2ex.com
  # skip-src-address: [...]
  # skip-dst-address: [...]
  # skip-domain: [...]
  # sniffing: [tls, http]  # 已废弃
  # port-whitelist: ["80", "443"]  # 已废弃

# ===== Tunnels =====
tunnels:
  - tcp/udp,127.0.0.1:6553,114.114.114.114:53,proxy
  - network: [tcp, udp]
    address: 127.0.0.1:7777
    target: target.com
    proxy: proxy

# ===== DNS =====
dns:
  cache-algorithm: arc
  enable: false
  prefer-h3: false
  listen: 0.0.0.0:53
  ipv6: false
  ipv6-timeout: 300
  default-nameserver:
    - 114.114.114.114
    - 8.8.8.8
    - system
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  # fake-ip-range6: fdfe:dcba:9876::1/64
  fake-ip-filter:
    - '*.lan'
    - localhost.ptlogin2.qq.com
    - rule-set:fakeip-filter
    - geosite:fakeip-filter
  fake-ip-filter-mode: blacklist
  fake-ip-ttl: 1
  # use-hosts: true
  # use-system-hosts: true
  respect-rules: false
  nameserver:
    - 114.114.114.114
    - https://doh.pub/dns-query
    - https://dns.alidns.com/dns-query#h3=true
    - dhcp://en0
    - quic://dns.adguard.com:784
  # fallback: [...]
  # proxy-server-nameserver: [...]
  # proxy-server-nameserver-policy: {...}
  # direct-nameserver: [...]
  # direct-nameserver-follow-policy: false
  # fallback-filter:
  #   geoip: true
  #   geoip-code: CN
  #   ipcidr: [...]
  #   domain: [...]
  #   geosite: [...]  # 已废弃
  # fallback-lazy-query: false
  nameserver-policy:
    "geosite:cn,private,apple":
      - https://doh.pub/dns-query
    "geosite:category-ads-all": rcode://success
    "www.baidu.com,+.google.cn": [223.5.5.5]

# ===== Proxies =====
proxies:
  - name: "ss1"
    type: ss
    server: server
    port: 443
    cipher: chacha20-ietf-poly1305
    password: "password"
    # udp: true
    # ip-version: dual
    # smux: { enabled: false, protocol: smux }
    # plugin: obfs/v2ray-plugin/shadow-tls/gost-plugin/restls/jls/kcptun
    # plugin-opts: {...}
    # dialer-proxy: gost-relay-hop

  - name: "vmess"
    type: vmess
    server: server
    port: 443
    uuid: uuid
    alterId: 32
    cipher: auto
    # network: ws/h2/grpc/mkcp/mekya/xhttp
    # tls: true
    # client-fingerprint: chrome
    # ws-opts: { path, headers, max-early-data, ... }
    # grpc-opts: { grpc-service-name, grpc-user-agent, ping-interval, max-connections, min-streams, max-streams }
    # reality-opts: { public-key, short-id, support-x25519mlkem768 }
    # ech-opts: { enable, config, query-server-name }
    # shadow-tls-opts / restls-opts / jls-opts / tlsmirror-opts

  - name: "vless"
    type: vless
    server: server
    port: 443
    uuid: uuid
    # flow: xtls-rprx-vision
    # encryption: "mlkem768x25519plus.native/..."
    # network: tcp/ws/grpc/xhttp
    # reality-opts: {...}
    # xhttp-opts: { path, host, mode, ... }

  - name: "trojan"
    type: trojan
    server: server
    port: 443
    password: yourpsk
    # flow: xtls-rprx-direct
    # ss-opts: { enabled, method, password }
    # ws-opts / grpc-opts

  - name: "hysteria2"
    type: hysteria2
    server: server.com
    port: 443
    password: yourpassword
    # up: "30 Mbps"
    # down: "200 Mbps"
    # obfs: salamander
    # obfs-password: xxx
    # realm-opts: { enable, server-url, token, realm-id, stun-servers }
    # handshake-timeout: 30

  - name: "wireguard"
    type: wireguard
    server: 162.159.192.1
    port: 2480
    ip: 172.16.0.2
    ipv6: fd01:...
    public-key: xxx
    private-key: xxx
    udp: true
    # peers: [...]
    # amnezia-wg-option: {...}

  - name: "tuic"
    type: tuic
    server: www.example.com
    port: 10443
    token: TOKEN  # v4
    # uuid/password: v5
    # udp-relay-mode: native
    # congestion-controller: bbr

  - name: "anytls"
    type: anytls
    server: 1.2.3.4
    port: 443
    password: xxx
    udp: true

  - name: "dns-out"
    type: dns

  - name: "rematch"
    type: rematch
    target-rematch-name: "rematch1"
    target-sub-rule: "sub-rule1"

# ===== Proxy Groups =====
proxy-groups:
  - name: "auto"
    type: url-test
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300
    # tolerance: 150

  - name: "fallback-auto"
    type: fallback
    proxies: [ss1, ss2, vmess1]
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  - name: "load-balance"
    type: load-balance
    proxies: [ss1, ss2, vmess1]
    # strategy: consistent-hashing
    url: "https://cp.cloudflare.com/generate_204"
    interval: 300

  - name: "Proxy"
    type: select
    proxies: [ss1, ss2, auto]

  - name: "UseProvider"
    type: select
    filter: "HK|TW"
    use: [provider1]
    proxies: [Proxy, DIRECT]

# ===== Proxy Providers =====
proxy-providers:
  provider1:
    type: http
    url: "url"
    interval: 3600
    path: ./provider1.yaml
    proxy: DIRECT
    header:
      User-Agent: ["mihomo/1.18.3"]
    health-check:
      enable: true
      interval: 600
      url: https://cp.cloudflare.com/generate_204
    override:
      skip-cert-verify: true
      udp: true
  provider2:
    type: inline
    payload: [...]
  test:
    type: file
    path: /test.yaml

# ===== Rule Providers =====
rule-providers:
  rule1:
    behavior: classical
    interval: 259200
    path: /path/to/save/file.yaml
    type: http
    url: "url"
    proxy: DIRECT
  rule3:
    type: http
    url: "url"
    format: mrs
    behavior: domain
    path: /path/to/save/file.mrs
  rule4:
    type: inline
    behavior: domain
    payload: ['.blogger.com', '*.*.microsoft.com']

# ===== Rules =====
rules:
  - RULE-SET,rule1,REJECT
  - IP-ASN,1,PROXY
  - DOMAIN-REGEX,^abc,DIRECT
  - DOMAIN-SUFFIX,baidu.com,DIRECT
  - DOMAIN-KEYWORD,google,ss1
  - DOMAIN-WILDCARD,test.*.mihomo.com,ss1
  - IP-CIDR,1.1.1.1/32,ss1
  - IP-CIDR6,2409::/64,DIRECT
  - SUB-RULE,(OR,((NETWORK,TCP),(NETWORK,UDP))),sub-rule-name1
  - MATCH,DIRECT

# ===== Sub Rules =====
sub-rules:
  sub-rule-name1:
    - DOMAIN,google.com,ss1
    - DOMAIN,baidu.com,DIRECT

# ===== Listeners =====
listeners:
  - name: socks5-in-1
    type: socks
    port: 10808
  - name: http-in-1
    type: http
    port: 10809
  - name: mixed-in-1
    type: mixed
    port: 10810
  - name: tunnel-in-1
    type: tunnel
    port: 10816
    network: [tcp, udp]
    target: target.com
  - name: tun-in-1
    type: tun
    stack: system
    dns-hijack: [0.0.0.0:53]
    inet4-address: [198.19.0.1/30]
    inet6-address: ["fdfe:dcba:9877::1/126"]

# ===== TUIC Server =====
# tuic-server:
#   enable: true
#   listen: 127.0.0.1:10443
#   certificate: ./server.crt
#   private-key: ./server.key

# ===== NTP =====
# ntp:
#   enable: true
#   server: time.apple.com
#   port: 123
#   interval: 30

# ===== iptables =====
# iptables:
#   enable: true
#   inbound-interface: lo
#   dns-redirect: true
```

---

## 附：源码文件索引

| 文件 | 说明 |
|---|---|
| `config/config.go` | 核心配置结构定义（RawConfig 及所有 Raw* 子结构），解析逻辑（ParseRawConfig / parseDNS / parseTun / parseSniffer 等），默认值（DefaultRawConfig） |
| `config/initial.go` | 初始化函数（创建配置目录和初始 config.yaml） |
| `config/utils.go` | DAG 排序（proxyGroupsDagSort），dialer-proxy 循环检测，IPv6 检测 |
| `adapter/parser.go` | 全局代理类型注册（ParseProxy switch），smux 处理 |
| `adapter/outboundgroup/groupbase.go` | GroupBase / GroupBaseOption，filter/exclude-filter/exclude-type 实现 |
| `adapter/outboundgroup/parser.go` | GroupCommonOption（通用字段），ParseProxyGroup（类型分发），默认值逻辑 |
| `adapter/outboundgroup/selector.go` | SelectorOption（`default-selected`） |
| `adapter/outboundgroup/urltest.go` | URLTestOption（`tolerance`） |
| `adapter/outboundgroup/fallback.go` | FallbackOption（空） |
| `adapter/outboundgroup/loadbalance.go` | LoadBalanceOption（`strategy`） |
| `adapter/provider/parser.go` | proxyProviderSchema / healthCheckSchema，ParseProxyProvider |
| `adapter/provider/override.go` | overrideSchema / overrideProxyNameSchema / OverrideExpr |
| `rules/parser.go` | 全局规则类型注册（ParseRule switch） |
| `rules/common/base.go` | ParseRulePayload（规则行解析），参数常量（`no-resolve` / `src`） |
| `rules/provider/parse.go` | ruleProviderSchema，ParseRuleProvider |
| `listener/parse.go` | 全局 listener 类型注册（ParseListener switch） |
| `listener/inbound/base.go` | BaseOption（通用字段） |
| `listener/inbound/*.go` | 各类型 Option struct（SocksOption / HTTPOption / MixedOption / 等） |
| `dns/resolver.go` | NameServer struct |
| `dns/policy.go` | DNS Policy 实现 |
| `constant/dns.go` | DNSMode / FilterMode 枚举 |
| `constant/tun.go` | TUNStack 枚举 |
| `constant/adapters.go` | DefaultTestURL 常量 |
| `component/process/find_process_mode.go` | FindProcessMode 枚举 |
| `tunnel/mode.go` | TunnelMode 枚举（Global/Rule/Direct） |
| `docs/config.yaml` | 官方完整配置参考示例（2811 行） |
