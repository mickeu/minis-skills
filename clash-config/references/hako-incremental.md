# Hako 相对 mihomo v1.19.31 的配置增量

> 来源：`bind/hako/` 目录下非测试 `.go` 文件（约 130+ 个）。版本基线：mihomo v1.19.31（`UPSTREAM_VERSION` 文件确认），上游基线 `v1.19.31`。Hako HEAD `7ea70d15`（2026-09-24）。Hako（`github.com/TokenPLS/Hako`）是 mihomo 的独立 fork，`bind/hako` 为 Hako 独有目录，是相对 mihomo 的全部增量代码。
>
> 本文只摘录**配置项 / 配置行为**层面的增量，不含纯运行时诊断、UI 路由、IPC 细节。所有结论均来自源码注释与函数体，未在代码中找到明确佐证的项标注「推断」。
>
> **v1.19.31 更新要点**：上游新增 `stack: mips` tun 栈、EasyTier 出站、ZeroTier `identity-secret`、SSH 字段改用 kebab-case（`private-key`/`private-key-passphrase`）、REALITY ML-KEM 后量子密钥交换、DomainMap 简洁数据结构（规则集性能提升）。Hako 新增 mDNS 发现、macOS 连接归属解析、网络重置、代理目录预连接等 Apple 平台特化能力。

Hako 的核心设计哲学（贯穿 `config_deviations.go`、`config_pipeline.go`、`validate.go`）：**「任何上游 mihomo 配置都必须能在 Apple 平台启动；不支持的字段被容忍并剥离（tolerate + strip），只在少数会改变 DNS/选路语义的情况才拒绝」**。因此 Hako 对 mihomo 的增量绝大多数是**改写默认值 / 强制值 / 剥离字段**，而非新增 YAML schema 字段。

---

## 一、config_deviations 机制（偏差登记表）

Hako 用一张 `deviationRules` 表显式记录「内核做了与配置请求不同的事」。每条规则（`deviationRule`）字段：

| 字段 | 含义 |
|---|---|
| `field` | YAML 点路径（如 `tun.stack`），或 `rules` + `ruleKind` 表示规则扫描类 |
| `category` | `stripped`（剥离）/ `forced`（强制改写）/ `unavailable`（平台无此能力） |
| `effective` | 内核实际行为 |
| `reason` / `mechanism` | 面向读者的理由 / 面向开发者的机制引用 |
| `source` | 引证：Apple 文档/SDK 头、mihomo 源码行、本仓库文件 |
| `recoverable` | 仅编辑配置能否恢复该行为 |
| `alternative` | 在本平台获得该行为的另一途径 |
| `applies` | 平台策略函数（决定本配置文件是否产生该偏差） |
| `upstreamDefault` | 仅对强制规则：mihomo `DefaultRawConfig` 的原值 |
| `forcedValue` | 强制规则写入的常量标量（`"true"`/`"0"`/`"gvisor"`…） |
| `defaultOnly` | 仅在用户未显式写时改默认值（显式值总被尊重） |
| `honouredBy` | `"expansion"` 表示字段本身被忽略但其意图通过改写实现 |
| `withheld` | 凭据字段，报告里渲染为 `set (value withheld)` |
| `ruleScan` / `ruleKind` | 由扫描 rules 列表发出（如 UID 规则） |

登记表在 `config_deviations.go:223` 的 `var deviationRules`，共约 48 条字段规则 + UID 规则扫描条目。运行时 `collectConfigDeviations` 读取用户**实际写出的合并 YAML**（而非解析后的 RawConfig，以区分零值与未写），逐条匹配并产出 `configDeviation` 列表，经 `publishDeviations` 发布（带文档 SHA-256 身份），可经 Clash API 查询。

三类别的语义边界（`config_deviations.go:14-30`）：
- `stripped`：字段解析了，本内核移除它（可争论、可复议的决定）
- `forced`：字段解析了，本内核用不同值覆盖它
- `unavailable`：本平台无此设施，无论如何都无法兑现

---

## 二、Hako 改写/强制的默认值与字段值

下表为 Hako 相对 mihomo 默认行为**主动改写**的项。`强制值` 列为 `forcedValue`/`forcedValue` 等价标量；`仅默认` 表示 `defaultOnly`（用户显式写则尊重）。`适用` 列为 `applies` 策略简述。

### 2.1 通用配置（非 tun）

| 字段/行为 | 类型 | mihomo 默认 | Hako 强制值 | 适用 | 说明 | 源码位置 |
|---|---|---|---|---|---|---|
| `dns.enable` | forced | false | **true** | 包隧道（NE） | 包隧道总捕获 53；dns.enable=false 时所有劫持查询 SERVFAIL，隧道能起却解析不了。显式写不被覆盖但 `repairApplePacketTunnelDNS` 仍会置 true | `config_pipeline.go:918` repairApplePacketTunnelDNS；`config_deviations.go:382` |
| `profile.store-fake-ip` | forced(defaultOnly) | false | **true** | NE | fake-ip 映射落盘以跨 NE 重启存活；显式 true/false 总被尊重 | `config_pipeline.go:204` applyStoreFakeIPDefault；`config_deviations.go:395` |
| `unified-delay` | forced(defaultOnly) | false | **true** | NE | 探测报告第二次可比 RTT；显式值总被尊重 | `config_pipeline.go:219` applyUnifiedDelayDefault；`config_deviations.go:409` |
| `find-process-mode` | forced | strict | **off** | iOS（无 processPath 能力） | 应用扩展无法枚举其他进程；规则保留但元数据为空。macOS 包隧道保留配置值（mihomo 自查 socket 表） | `override.go:50`；`config_pipeline.go:688`；`config_deviations.go:424` |
| `geodata-loader` | forced | standard | **memconservative** | `memoryConservativeGeodata`（iOS/tvOS 包隧道） | 测得 geosite 编译峰值 72.7 MiB，超 50 MiB 预算；macOS 保留原值 | `config_pipeline.go:252`；`override.go:60`；`config_deviations.go:708` |
| `geo-auto-update` | forced | true | **false** | 全平台 | geo 数据由 App 预下载并喂给内核 | `override.go:24`；`config_pipeline.go:269`；`config_deviations.go:698` |
| `geo-update-interval` | unavailable | — | 未用（无周期下载器） | 全平台 | 仅调度已关闭的 geo-auto-update | `config_deviations.go:720` |
| `GeoXUrl`(geoip/mmdb/asn/geosite) | forced | mihomo 下载 URL | **`hako-ne-disabled://prestage-required`** | NE | 内核不从网络拉 geo；App 预置。非网络 URL，预检即失败 | `config_pipeline.go:269-275` |
| `ntp.write-to-system` | forced | false | **false** | NE | 仅系统自身可设设备时钟；settimeofday 需 super-user | `config_pipeline.go:757`；`override.go` overrideForNetworkExtension；`config_deviations.go:340` |
| `redir-port` | forced | 0（默认） | **0**（显式清零） | NE | 需 /dev/pf + root | `config_pipeline.go:624`；`override.go:106` |
| `tproxy-port` | unavailable | 0 | 不开（上游非 Linux 自报不支持） | 全平台 | 透明代理为 Linux 专属 | `config_pipeline.go:624`；`config_deviations.go:226` |
| `routing-mark` | unavailable | 0 | 不设（Darwin 无 SO_MARK） | NE | Linux socket 选项 | `config_pipeline.go:691`；`config_deviations.go:340` |
| `interface-name` | stripped | "" | 移除（NE 用 socket hook + IP_BOUND_IF 绑定物理口） | NE | 上游 dialer 在有 socket hook 时忽略 interfaceName | `config_pipeline.go:689`；`config_deviations.go:368` |
| `iptables.enable` | forced | false | **false** | NE | Linux 转发面 | `config_pipeline.go:751`；`override.go:115` |
| `external-controller-routing-mark` | forced | 0 | **0** | NE | Darwin 无 SO_MARK | `config_pipeline.go:753` |
| `external-controller-pipe` | unavailable | "" | 不开 | 全平台 | Windows 命名管道 | `config_pipeline.go:754`；`config_deviations.go:262` |
| `dns.listen-routing-mark` | forced | 0 | **0** | NE | Darwin 无 SO_MARK；`dns.listen` 本身被尊重 | `config_pipeline.go:756`；`override.go:110` |
| `allow-lan` | stripped | false | 未许可时清为 false | NE 且 `!allowLanPermitted` | 暴露设备到局域网是持机者的决定，不由订阅代决；App 许可后下次 reload 起尊重配置值 | `config_pipeline.go:601`；`config_deviations.go:271` |

### 2.2 tun 家族（包隧道下强制）

下列在 `underPacketTunnel`（NE 且 packetTunnel）下生效，源自 `override.go:155` overrideTunForIOS 与 `config_pipeline.go` normalizeRawNetworkExtensionSurfaces。

| 字段 | 类型 | mihomo 默认 | Hako 强制值 | 说明 | 源码位置 |
|---|---|---|---|---|---|
| `tun.enable` | forced | false | **true** | 包隧道必为 tun（`ensureTunEnabled`） | `override.go:148`；`config_deviations.go:458` |
| `tun.device` | forced | "" | **`hako-packet-flow`** | NE 交付 NEPacketTunnelFlow，非 utun 描述符 | `override.go:186`；`config_deviations.go:469` |
| `tun.stack` | forced | mixed | **gvisor**（仅 IncludeAllNetworks 时） | 系统/mixed 栈在 IncludeAllNetworks 下内核丢弃重注入包，仅 gvisor 可承载 | `override.go:192`；`config_deviations.go:444` |
| `tun.mtu` | forced | 1500(推断) | **启动选定值**（默认 4064，范围 1280–9000） | App 与内核须共用一个 MTU，启动时一次选定 | `override.go:197`；`tun.go:17` |
| `tun.auto-route` | forced | true | **false** | 路由由 NEPacketTunnelNetworkSettings 安装，非内核 | `override.go:199`；`config_deviations.go:480` |
| `tun.auto-detect-interface` | forced | true | **false** | 扩展自决出口接口 | `override.go:200`；`config_deviations.go:492` |
| `tun.gso` | forced | false | **false** | 桥接描述符无可协商 offload 的驱动 | `override.go:202`；`config_deviations.go:503` |
| `tun.gso-max-size` | forced | 65536(推断) | **0** | 随 gso | `override.go:203`；`config_deviations.go:514` |
| `tun.recvmsgx` | forced | true(推断) | **false** | 批量 utun-fd 读路径在 SOCK_DGRAM 桥上用普通 readv | `override.go:205`；`config_deviations.go:525` |
| `tun.sendmsgx` | forced | true(推断) | **false** | 同上写路径 | `override.go:206`；`config_deviations.go:536` |
| `tun.disable-icmp-forwarding` | forced | false | **true** | 无特权 raw socket；内核自答 ping（延迟为本机而非路由） | `override.go:208`；`config_deviations.go:547` |
| `tun.dns-hijack` | forced | ["0.0.0.0:53"](默认) | **`["0.0.0.0:53"]`** | 捕获隧道内全部 DNS 查询；已写「全劫持」则不算偏差 | `override.go:213`；`config_deviations.go:558` |

### 2.3 tun 路由过滤族（剥离，stripped）

下列在 `underPacketTunnel` 下被 `normalizeRawNetworkExtensionSurfaces` 清空（`config_pipeline.go:700-718`），属 `deviationStripped`，理由统一为 `tunAutoRouteFilter`（NE 不装核心侧主机路由，过滤无对象）：

`tun.include-interface`、`tun.exclude-interface`、`tun.include-uid`、`tun.include-uid-range`、`tun.exclude-uid`、`tun.exclude-uid-range`、`tun.exclude-src-port`、`tun.exclude-src-port-range`、`tun.exclude-dst-port`、`tun.exclude-dst-port-range`、`tun.include-mac-address`、`tun.exclude-mac-address`（`config_deviations.go:568-687`）

### 2.4 Linux/Android 专属（unavailable，接受并忽略）

`tun.auto-redirect`、`tun.auto-redirect-input-mark`、`tun.auto-redirect-output-mark`、`tun.auto-redirect-iproute2-fallback-rule-index`、`tun.iproute2-table-index`、`tun.iproute2-rule-index`、`iptables`、`tun.include-package`、`tun.exclude-package`、`tun.include-android-user`、`clash-for-android`（`config_deviations.go:728-816`）。这些在 `normalizeRawNetworkExtensionSurfaces` 中被清零（`config_pipeline.go:695-699`）。

### 2.5 route-address-set（unavailable + honouredBy=expansion）

`tun.route-address-set` 与 `tun.route-exclude-address-set`：字段本身是 Linux nftables 设施（Apple 无），但**意图被兑现**——`FinalizeForIOS` 的 `expandRouteSet` 在内核启动前把命名规则集的地址读出并写入 `route-address` / `route-exclude-address`（`config_finalize.go:74-77, 269`）。因此 `Category=unavailable` 且 `honouredBy="expansion"`，客户端不应让用户删除。

### 2.6 每代理 egress override（stripped）

`stripOutboundEgressOverrides`（`config_pipeline.go:1136`）删除每代理 `interface-name`/`routing-mark` 出口覆盖（NWPathMonitor 管物理出口，不改变选代理），配置仍启动。

---

## 三、Hako 新增/强化的校验限制（validate.go / config_pipeline.go）

Hako 的校验原则：**只拒绝会改变 DNS/选路语义或上游自身也拒绝的配置；其余容忍+剥离+告警**。

| 限制 | 类型 | 触发 | 源码位置 |
|---|---|---|---|
| `dns.nameserver` 在 iOS 必须显式设置 | 拒绝 | NE 且无显式 nameserver（防止回落到硬编码 114/8.8） | `validate.go:462` validateDNSForIOS |
| `proxy-groups[].filter` / `exclude-filter` 必须为合法 regexp2 | 拒绝 | 解析失败 | `config_pipeline.go:1187` validateRawProxyGroupRegexForIOS |
| `proxy-provider` health-check.interval 的时长单位 | 拒绝 | 单位不可解析 | `config_pipeline.go:1234` validateProxyProviderHealthCheck |
| geo 数据文件必须预置（GeoIP/GeoSite/ASN） | 拒绝 | 规则引用但本地无文件 | `config_pipeline.go:1286` validateGeodataFilesForIOS / requirePrestagedFile |
| 配置输入上限 4 MiB / JSON 上限 16 MiB | 拒绝 | 超长 | `config_limits.go` |
| hysteria `up`/`down` 速率可被 `StringToBps` 解析 | 拒绝（转发上游自身拒绝） | 解析得 0 | `validate.go:755` upstreamRefusedOutboundOption |
| hysteria2 `ports` / `hop-interval` 可被 `NewUnsignedRange` 解析 | 拒绝（转发上游拒绝） | 解析失败 | `validate.go:770` |
| xhttp-opts `sc-max-each-post-bytes` / `sc-min-posts-interval-ms` 可被 `xhttp.ParseRange` 解析且 Max>0 | 拒绝（转发上游拒绝） | — | `validate.go:816`（仅这两个，经实测驱动 mihomo 确认到达 config.Parse） |
| grpc-opts `ping-interval` 时长单位 | 拒绝（不可表示） | — | `validate.go:836` unrepresentableOutboundOption |
| `SetupOptions.TunMTU` 必须为 0 或 1280–9000 | 拒绝 | — | `tun.go:24` validateTunMTU |
| `SetupOptions.RuntimeProfile` 枚举校验 | 拒绝 | 非四个合法值 | `runtime_profile.go:67` normalizeRuntimeProfile |
| `SetupOptions.SystemDNSServerLines` 每行须为合法地址 | 拒绝 | — | `setup.go:181` |

> 注：Hako **不再**拒绝 `tun.route-address-set`、嵌套 `dns:#fragment`、`dhcp://`/`system://` 解析器 scheme、远程 provider 未预下载等——这些曾经被拒，现改为「容忍+剥离/告警」，理由是上游 mihomo 接受它们或剥离比拒绝更安全（见 `validate.go` 各处长注释）。

---

## 四、Apple 平台特化配置行为

### 4.1 RuntimeProfile（运行时档位）

`SetupOptions.RuntimeProfile`（`runtime_profile.go`，启动期、不可热改）四档，决定能力矩阵 `appleRuntimePolicy`：

| 档位 | networkExtension | packetTunnel | trustedProcessMetadata | memoryConservativeGeodata | compiledGeoSiteOnly/GeoIPOnly | requirePacketTunnelDNS | repairPacketTunnelDNS | bindsUnixControlSocket | useSystemDNS |
|---|---|---|---|---|---|---|---|---|---|
| `iosPacketTunnel`（默认/空） | 取传入 | true | false | true | (NE 时) true | (NE 时) true | (NE 时) true | true | false |
| `macosPacketTunnel` | (NE 时) true | true | false | false | false | (NE 时) true | (NE 时) true | true | false |
| `macosApplication` | false | false | true | false | false | false | false | true | true |
| `tvosPacketTunnel` | 取传入 | true | false | true | (NE 时) true | (NE 时) true | (NE 时) true | **false** | false |

- macOS 包隧道**保留** `find-process-mode`、`geodata-loader` 配置值（mihomo 自查 socket 表，无 50 MiB 墙）
- tvOS 继承 iOS 行为，唯一已测差异：第三方进程无法绑 AF_UNIX（`bindsUnixControlSocket=false`），故 tvOS 不开绑定自有 unix 控制套接字
- `macosApplication`（容器 App 预检）`trustedProcessMetadata=true`，接受所有规则类型以验证而非预剥离
- `inheritsIOSPacketTunnelBehavior()`：iOS 与 tvOS 共用行为（暂无实测分裂）

### 4.2 内存预算与 GC 调度

| 行为 | 值/机制 | 源码 |
|---|---|---|
| NE jetsam 预算 | **50 MiB**（`neJetsamBudgetBytes`，非 Apple 文档声明，为本仓库实测） | `memory_ne_pacing.go:34` |
| GOMEMLIMIT（GC pacing） | 预算的 **3/4** = 37.5 MiB（留给 cgo/ObjC）；仅 iOS 族+NE 下默认武装，显式 `MemoryLimit`/`ReloadSetupOptions.SoftMemoryLimit` 总优先 | `memory_ne_pacing.go:36, 70` |
| 内存压力阈值机 | 三态滞后（normal/armed/triggered），trigger 阈值 = 预算 − 5 MiB；**默认仅报告**（`MemoryPressureShed=false`），与 sing-box 默认即 shed 相反 | `memory_threshold.go` |
| reload 内存守卫 | reload 前判余量；估算「再建一核」成本 = `oneCore × 2.0`（+ provider 增长 × 6.0），超余量则拒绝并让 App 重启扩展 | `reload_memory_guard.go` |

### 4.3 NAT64 合成

`installPhysicalAddressTransform`（`nat64.go`）在物理路径无 IPv4 但有 IPv6 时，通过系统 `getaddrinfo`（RFC 7050 发现的 NAT64 前缀）把 IPv4 字面量合成 IPv6 目的地址。校验 `validateNAT64Synthesis` 拒绝回环/链路本地/非 RFC 6052 嵌入的合成结果（防恶意网络重定向）。

### 4.4 SystemDNS 替换

`SetupOptions.SystemDNSServerLines` 携带 App 在隧道 DNS 设置生效前读到的系统解析器；`substituteSystemResolvers` 把配置中每个 `system://`/`dhcp://` 条目就地替换为这些解析器（issue #21：否则 system:// 在隧道内只解析到隧道自身地址）。落在隧道自身范围的行被忽略并告警。

### 4.5 geodata 预编译

`compiledGeoSiteOnly`/`compiledGeoIPOnly`（iOS/tvOS 包隧道）：内核只读 App 预编译的 geosite/geoip 制品，不从源编译（编译峰值 72.7 MiB / 130 MiB，超 50 MiB）。`geodata.SetCompiledGeoSiteOnly` 为进程级开关。`validateGeodataFilesForIOS` 要求规则引用的 geo 文件已预置；`geodata.MarkGeoSiteVerified` 跳过 mihomo 自带的昂贵全量 CN matcher 校验。

### 4.6 IncludeAllNetworks

`SetupOptions.IncludeAllNetworks`（启动期）反映 `NETunnelProviderProtocol.includeAllNetworks`。开启时 system/mixed 栈因内核丢弃重注入包而失效，故 `overrideTunForIOS` 把栈移到 gvisor 并报告；`include_all_networks.go` 同时告知 sing-tun 该设置，使 override 未捕获的栈在 Start 失败而非静默运行。

### 4.7 证书存储

`SetupOptions.CertificateStore`（`system`/`mozilla`/`chrome`/`none`）为进程级选项（mihomo 全进程单一证书池）。选非 system 可避免每次校验都向 trustd 走 XPC，但会丢掉平台信任的非 bundle 根（含 MDM 企业根），故为显式选择而非默认。

---

## 五、新增的协议/出站/监听类型

### 5.1 Hako 新增的是「深链导入注册表」本身，不是新协议（`proxy_import.go:190`）

**⚠️ 交叉验证结论（已核对上游 ac017cd，见文末「交叉验证」节）**：masque / trusttunnel / mihomo 上游 v1.19.30 **早已同时具备 outbound 实现与 parser 注册**，不是 Hako 增补。真正的增量是 Hako 独有文件 `bind/hako/proxy_import.go`（约 4500 行）——**代理深链导入这一整套功能上游完全没有**，其 scheme 顺序刻意对齐 Shadowrocket 2.2.90 的 `supportsSchemes` 输出以便单次精确比对。

| Scheme | CanonicalType | 状态 | 上游是否已有该协议 |
|---|---|---|---|
| `masque` | **masque** | supported | ✅ 上游 `adapter/outbound/masque.go` + `adapter/parser.go` |
| `tt` | **trusttunnel** | supported | ✅ 上游 `trusttunnel.go` + `parser.go`（Hako 经深链 TLV payload 解码，`proxy_import.go:4338`） |
| `mierus` | **mieru** | supported | ✅ 上游 `mieru.go` + `parser.go` + `common/convert/converter.go`；仅 `mieru` 裸 scheme 被标 coreUnsupported |
| `hysteria2+realm`/`hy2+realm` | hysteria2 | supported | ✅ 上游 converter 的 +realm 后缀变体 |

> vmess/trojan/ss/ssr/snell/vless/hysteria/hysteria2/tuic/wireguard/ssh/anytls 亦全为上游已有类型。**Hako 对 `adapter/outbound/` 的改动量为 +0/-0（零行改动）**，唯一新增文件是 `physical_packet.go`（Apple 包隧道的物理包处理）+ 4 个 test 文件；无任何出站目录被删除。

**协议增量的正确表述**：Hako 不新增、不修改任何代理协议实现；它新增的是**导入能力**（把外部深链/订阅粘贴进 App 并物化进内核配置）与**配置语义改造**（下文第一、二节）。

### 5.2 proxy_share 本地混合监听器

`proxy_share.go`：Hako 在扩展进程内自开的**带认证 mixed HTTP/SOCKS5 监听器**，绑 0.0.0.0/::，端口范围 1024–65535，凭据为 SOCKS5 用户名/密码。这是 `config_deviations.go` 中「NE 能开监听套接字」的事实依据（证伪了旧有「NE 不能开监听」的墙）。Apple 立场为 TN3120 的「不建议」而非「不能」。允许的前缀为常见私网/链路本地段。

---

## 六、其他配置行为增量

| 行为 | 说明 | 源码 |
|---|---|---|
| provider 键名规范化 | `canonicalizeProviderDefinitionKeys`：provider 定义顶层键统一小写（`Path`→`path`，已存在小写键则保留小写） | `config_pipeline.go:145` |
| FinalizeForIOS http→file 改写 | `FinalizeForIOS` 把 http provider 物化为 type:file（App 预下载），并展开 route-address-set | `config_finalize.go:30` |
| 偏差报告 API | Start/Reload 后可查 `publishedDeviationReport`（含文档 SHA-256 与序号），CheckConfig 不发布 | `config_deviations.go` publishDeviations |
| `upstream_defaults.go` | 导出 mihomo `DefaultRawConfig()` 的标量默认（反射读 yaml tag，3 层，枚举按名），供客户端在隧道未起时得知「内核无人说话时的行为」 | `upstream_defaults.go` |
| `yaml_json.go` YamlToJSON | 保序 YAML→JSON（含 nameserver-policy 等首匹配段），4 MiB/16 MiB 上限，拒自引用锚/billion laughs/重复键 | `yaml_json.go` |
| gVisor TCP 窗口调参 | App-Group 文件 `hako-gvisor-tcp-buffer-bytes` 可越界调 `tun.GVisorTCPBufferBytes`（基准 20 KiB，生产默认不写） | `setup.go:139` |
| `PlatformConfigIntent` | 导出 tun 重启指纹（仅源控字段，固定 Hako 字段如 stack/MTU/bridge fd/DNS hijack 故意缺席） | `config_api.go:15` |

---

## 我不确定的地方

以下为从代码**推断**而非注释/文档明确确认的点。原 8 项中 3 项（masque 等协议归属、`tun.mtu` 默认、`ntp.write-to-system` 默认）已通过上游 ac017cd 对照核实并移除，见下一节。

1. **`tun.gso-max-size` / `tun.recvmsgx` / `tun.sendmsgx` 的 mihomo 默认**：Hako 强制为 0/false；上游 `RawTun` 结构体确有这三个字段（`config.go:281` 区块，含 `omitempty`），但 `DefaultRawConfig` 未逐一点名其值，表中标「(推断)」仍是推断。
2. **`profile.store-fake-ip` 与 `unified-delay` 的 defaultOnly 行为**：代码明确「显式值总被尊重」，但「显式 false」是否真不被覆盖取决于 `configExplicitlySetsUnifiedDelay` 的 `*bool` 探针能否区分显式 false 与缺省——代码逻辑显示能（`probe.UnifiedDelay != nil`），未在运行时实测。
3. **50 MiB jetsam 预算**：`memory_ne_pacing.go` 注释自承「no Apple document states a memory ceiling」，该数为仓库实测而非 Apple 声明；不同 iOS 版本/设备可能不同。
4. **`dns.enable` 强制**：`repairApplePacketTunnelDNS` 无条件在 NE 置 true（即便用户写 false），但 `config_deviations.go:382` 把它记为 `forced` 且未标 `defaultOnly`——二者是否完全一致需对照运行时；代码行为倾向「NE 下总是 true」。
5. **`external-controller` 等 RESTful API 的处置**：`override.go` 注释称「carried and inert」（携带但不消费），与 mihomo 行为有别，未核实是否真有绑定自有 unix 套接字服务它。

## 交叉验证记录（2026-09-22）

方法：`TokenPLS/Hako` 完整克隆（4285 commits / 5 tags）可访问上游基线 commit `ac017cdd246ce8bd547653d927e7bf77d7ee73d5`（「fix: initialize DNS before NTP (#3103)」），用 `git ls-tree` / `git grep` / `git show <commit>:<file>` 逐一对照。**MetaCubeX/mihomo 主仓库现已不可用作验证源**——该 org 下同名仓库已被替换为一个 Python Pydantic 库（描述：*A simple Python Pydantic model for Honkai: Star Rail parsed data*，MIT License，与内核无关），org 其余仓库（`meta-rules-dat`/`metacubexd`/`mipstack`/`subconverter`/`utls`/`sing-quic` 等）仍在。

| 待验证项 | 结论 | 证据 |
|---|---|---|
| masque/trusttunnel/mieru 是否上游无 | **否，上游三者俱有** | ac017cd 下 `adapter/outbound/masque.go`、`trusttunnel.go`、`mieru.go`，且 `adapter/parser.go` 均有注册、`common/convert/converter.go` 有 mieru 转换 |
| Hako 是否改动过协议实现 | **零改动** | `git diff --numstat ac017cd HEAD -- adapter/outbound/{masque,mieru,trusttunnel,anytls,tlsmirror,jls,restls,ech,shadowtls}/` 全部 +0/-0 |
| Hako 在 outbound 层唯一新增文件 | `physical_packet.go` | 上游 outbound 39 文件 → Hako 45 文件，差集仅 `physical_packet.go` + 4 个 test |
| 被删除的出站协议 | **无** | 差集为空 |
| `tun.mtu` 上游默认 | **0（未设置）**，非 1500 | ac017cd `config.go:1686` 仅 `MTU: rawTun.MTU` 透传，`DefaultRawConfig` 无 MTU 项 |
| `gso`/`gso-max-size`/`loopback-address`/`udp-timeout`/`disable-icmp-forwarding`/`recvmsgx`/`sendmsgx` 是否 Hako 新字段 | **否，上游均有** | ac017cd `config.go:281` 区块全部存在（均带 `omitempty`） |
| `ntp.write-to-system` 上游默认 | **false** | ac017cd `config.go:533-539`：`Enable:false, WriteToSystem:false, Server:"time.apple.com", Port:123, Interval:30` |
| `defaultOnly` 是否借用上游概念 | **否，Hako 自有字段** | 仅见于 `bind/hako/config_deviations.go:168`（含专属注释「enforcement fires ONLY when the reader did not write the field」）+ 其 test 文件；上游 mihomo 的同名字段属 `component/dns/fallback.go` 的 DNS fallback-filter 机制，二者同名但无关 |

**验证命令速查**：

```bash
git ls-tree --name-only ac017cdd adapter/outbound/          # 上游文件清单
git grep -oE '"(masque|trusttunnel|mieru)"' ac017cdd -- '*.go'   # 上游是否注册该协议
git show ac017cdd:config/config.go | grep -A6 'type RawNTP'   # 上游结构体字段
git diff --numstat ac017cdd HEAD -- adapter/outbound/         # Hako 协议层改动量
```
