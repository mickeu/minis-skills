# 官方 MetaCubeX Wiki 参考（虚空终端 Docs / 最新特性增量）

> 本文件是对 `clash-config` 技能库其余 references 的**补充参考**，聚焦官方 Wiki 记录的最新 mihomo 特性与字段增量。
> 技能库主体（proxies/listeners/providers/config-structure）基于 Hako 源码（mihomo v1.19.31/32 fork）提取；本文件以 **官方 Wiki（基于最新 mihomo 分支）** 为准，两者冲突时以 Wiki 为准（Wiki 更新更快）。

## 参考资料（来源）

- 官方 Wiki 站：https://wiki.metacubex.one
- 文档源仓库：`MetaCubeX/Meta-Docs`（GitHub）
- 核对的 HEAD：`c47fd7212afc3f0e6afe9c7cb18591ba55e5e79b`（2026-10-03，`docs: mips as default IP stack, add tun congestion-controller (#226)`）
- 本地完整克隆：`/var/minis/workspace/metacubex-docs/`（95 个中文 .md，含 api/config/example/groups/handbook/startup）
- 上游 mihomo 最新稳定版：v1.19.32（2026-09-30，GitHub releases）。Wiki 的 example 分 Alpha（开发版）与 Meta（稳定版）两个分支
- 调研/核对日期：2026-10-20

## 全局配置增量（较 v1.19.31 技能库多出的字段）

```yaml
# TCP Keep Alive（移动端省电）
keep-alive-interval: 15   # Keep Alive 包间隔（秒）
keep-alive-idle: 15       # Keep Alive 最大空闲时间
disable-keep-alive: false  # 禁用 TCP Keep Alive（Android 强制 true）

# 统一延迟：计算 RTT 消除不同类型节点握手带来的延迟差异
unified-delay: true

# TCP 并发：用 dns 解析出的所有 IP 并发连接，取第一个成功
tcp-concurrent: true

# GeoData 数据模式
geodata-mode: true          # true=dat，false=mmdb（默认 false）
geodata-loader: memconservative  # standard / memconservative（默认，小内存优化）

# 自定义外部资源下载 UA（默认 clash.meta）
global-ua: clash.meta

# ETag 支持（外部资源增量下载）
etag-support: true

# geox-url 额外支持 asn 源
geox-url:
  asn: "https://github.com/xishang0128/geoip/releases/download/latest/GeoLite2-ASN.mmdb"
```

**客户端指纹**：全局 `client-fingerprint` 已弃用，直接写在 proxy 的 `client-fingerprint`。

## NTP（新增顶级配置段）

```yaml
ntp:
  enable: true
  write-to-system: true    # 同步系统时间（需 root）
  server: time.apple.com
  port: 123
  interval: 30             # 分钟
  dialer-proxy: DIRECT     # 可选；默认直接连接不经路由规则
```

## 实验性配置（新增两个字段）

```yaml
experimental:
  quic-go-disable-gso: false
  quic-go-disable-ecn: false   # 禁用 ECN
  dialer-ip4p-convert: false   # 启用 IP4P 地址转换
```

## DNS 服务器附加参数（`#` 语法）

对发往公网的 DNS 服务器，用 `#` 附加参数、`&` 连接多个参数：

```yaml
dns:
  nameserver:
    - 'https://8.8.8.8/dns-query#proxy&ecs=1.1.1.1/24&ecs-override=true'
```

| 参数 | 说明 |
|---|---|
| `#代理名` | 指定代理/策略组连接；`#RULES` 等价 `respect-rules` |
| `h3` | 强制 HTTP/3（与 `prefer-h3` 不冲突） |
| `skip-cert-verify` | 跳过 TLS 证书验证 |
| `name-cert-verify` | 仅修改证书 DNSName 校验目标，不改 SNI |
| `ecs` | 指定 DNS 查询 subnet 地址 |
| `ecs-override` | 强制覆盖 subnet |
| `disable-ipv4` | 丢弃 A 回应 |
| `disable-ipv6` | 丢弃 AAAA 回应 |
| `disable-qtype-<int>` | 丢弃特定类型回应，如 `disable-qtype-65` 屏蔽 HTTPS(TYPE65) |

**注意**：
- `fallback-filter.geosite` 已废弃，改用 `nameserver-policy`
- 默认 DNS 服务器 `default-nameserver` 必须为纯 IP（可为加密 DNS）
- `fake-ip-filter-mode: rule` 时 fake-ip-filter 支持 `RULE-SET`/`GEOSITE`/`DOMAIN*`/`MATCH`（行为必须 domain/classical）

## 策略组新增字段

```yaml
proxy-groups:
  - name: proxy
    type: select
    timeout: 5000              # 健康检查超时（ms）
    max-failed-times: 5        # 最大失败次数，超过强制健康检查
    expected-status: 204       # 期望状态码，支持 200/302、400-503、200/302/400-503
    exclude-filter: "美|日"     # 排除节点（正则）
    exclude-type: "Shadowsocks|Http"  # 按类型排除（| 分隔，不支持正则）
    include-all: false         # 引入所有 proxies + providers（不含策略组）
    include-all-proxies: false # 引入所有出站代理
    include-all-providers: false  # 引入所有代理集合（会使 use 失效）
    hidden: true               # API 返回 hidden 状态（配合前端隐藏）
    icon: xxx                  # API 返回的图标 URL
```

⚠️ 策略组里的 `interface-name` / `routing-mark` **已弃用**，请写在代理节点上。优先级：代理节点 > 代理策略 > 全局。

## 代理节点增量

### 通用：smux brutal

```yaml
proxies:
  - name: ss
    type: ss
    smux:
      enabled: true
      protocol: smux          # smux / yamux / h2mux（默认 h2mux）
      max-connections: 4
      min-streams: 4
      max-streams: 0
      statistic: false
      only-tcp: false
      padding: true
      brutal-opts:            # TCP Brutal 拥塞控制
        enabled: true
        up: 50                # Mbps
        down: 100
```

### TLS 层新选项（tls.md）

```yaml
proxies:
  - name: x
    type: vless
    tls: true
    sni: example.com
    client-fingerprint: chrome   # chrome/firefox/safari/ios/android/edge/360/qq/random
    reality-opts:
      public-key: xxxx
      short-id: xxxx
      support-x25519mlkem768: true   # 支持 X25519-MLKEM768 密钥交换
    ech-opts:
      enable: true
      config: base64_encoded_config   # 空则走 DNS 解析 ECH 参数
      query-server-name: xxx.com      # 可选，指定 DNS 解析域名
    shadow-tls-opts:                  # 需 tls:true，SNI 复用 sni/servername
      version: 3                      # v1/v2/v3，默认 v2
      password: shadow-tls-password
    restls-opts:
      password: restls-password
      version-hint: tls13             # tls12 / tls13
    jls-opts:
      username: jls-user
      password: jls-password
    tlsmirror-opts:                   # 仅 VMess 支持
      primary-key: BASE64_32字节密钥
      ...
```

- `fingerprint` = 证书 SHA256 指纹；`name-cert-verify` 仅改证书 DNSName 校验目标不改 SNI
- `certificate` + `private-key` = 开启 mTLS
- v1.19.18+ 起 `certificate`/`private-key`/`ech-key` 本地文件支持自动重载
- `tlsmirror-opts` 是 VMess 专有的 TLS 载体镜像（tlsmirror），含 `explicit-nonce-ciphersuites`、`transport-layer-padding`、`connection-enrolment`、`sequence-watermarking-enabled`、`embedded-traffic-generator.steps` 等复杂字段，详见 Wiki `config/proxies/tls.md`

### 新传输层 xhttp-opts（仅 VLESS）

```yaml
proxies:
  - name: x
    type: vless
    network: xhttp
    alpn: [h3]                # h3 需 alpn:[h3]；http/1.1 模式设 alpn:[http/1.1]
    xhttp-opts:
      path: "/"
      host: xxx.com
      mode: auto              # auto / stream-one / stream-up / packet-up
      headers: {}
      no-grpc-header: false   # stream-up/one 上行是否伪装 gRPC
      # 填充混淆、会话 ID、序列号、上下行分离等详见 Wiki transport.md
```

- `xhttp-opts` 内含大量字段：`x-padding-obfs-mode`/`x-padding-placement`/`x-padding-key`/`session-placement`/`session-key`/`seq-placement`/`uplink-data-placement`/`uplink-chunk-size`/`reuse-settings`（XMUX）/`download-settings` 等，字段众多，用到时查 Wiki `config/proxies/transport.md`
- `mekya-opts`：仅 VMess 的 Mekya 传输层（`url`/`max-write-delay`/`h2-pool-size`/`kcp` 等）
- gRPC 传输层新增 `grpc-opts.ping-interval`、`max-connections`、`min-streams`、`max-streams`

## TUN 配置更新

- **默认 stack 已改为 `mips`**（mihomo 自研 IP 协议栈），可用 `system/gvisor/mixed/mips`
- 新增 `congestion-controller`：`cubic`/`reno`/`bbr`/`bbr3`，默认 `cubic`，仅 `mips` 栈生效
- 新增 `inet6-address` 指定 TUN 的 IPv6 地址（需顶层 `ipv6: true`；无系统 IPv6 时自动禁用，可设 `SKIP_SYSTEM_IPV6_CHECK=1` 强制）
- 旧写法 `inet4-route-address`/`inet6-route-address`/`inet4-route-exclude-address`/`inet6-route-exclude-address` 即将废弃，用 `route-address`/`route-exclude-address`

```yaml
tun:
  enable: true
  stack: mips               # 默认 mips
  congestion-controller: bbr   # cubic/reno/bbr/bbr3，仅 mips
  inet6-address: [fdfe:dcba:9876::1/126]
```

## Sniffer 注意

`override-destination` **默认值为 true**（Wiki 示例值），配置时注意显式设置。

## 预置出站：PASS-RULE

内置出站除 `DIRECT/REJECT/REJECT-DROP/PASS/COMPATIBLE` 外，新增 **`PASS-RULE`**：
- `PASS`：视为已命中出站并跳过当前规则分支；在 SUB-RULE 中命中则**跳出子规则**回到主规则
- `PASS-RULE`：与 PASS 类似，但命中后**不跳出子规则**，仅跳过当前规则分支继续向后匹配

## 语法手册速记（handbook/syntax.md）

- 注释：`#` 必须在行头或前方有空格才视为注释
- 域名通配符（fake-ip-filter / force-domain 等处，**不同于** `DOMAIN-WILDCARD` 规则）：
  - `*`：一次匹配一级域名（`*.baidu.com` 不匹配 `123.tieba.baidu.com`）
  - `+`：前缀匹配多级（`+.baidu.com` 匹配 `baidu.com` 及所有子域）
  - `.`：前缀匹配多级但不含根域（`.baidu.com` 不匹配 `baidu.com`）
- 端口范围：`114-514/810-1919,65530`（`-` 范围，`/` 或 `,` 分隔多段）
- YAML 锚点 `&` / 别名 `*` / 合并 `<<` 可用于 provider 配置复用；重复键不合并

## API 速记（api/index.md，外部控制器 RESTful）

| 端点 | 方法 | 说明 |
|---|---|---|
| `/configs` | GET/PUT/PATCH | 获取/重载/更新配置（PUT 带 `?force=true`，PATCH 如 `{"mixed-port":7890}`） |
| `/configs/geo`、`/upgrade/geo` | POST | 更新 GEO 数据库 |
| `/restart` | POST | 重启内核 |
| `/upgrade` | POST | 更新内核（`?channel=`、`?force=true`） |
| `/upgrade/ui` | POST | 更新面板（需配置 external-ui） |
| `/cache/fakeip/flush`、`/cache/dns/flush` | POST | 清 fakeip / DNS 缓存 |
| `/logs` | GET/WS | 实时日志；`?format=structured` 输出结构化日志 |
| `/traffic` | GET/WS | `up/down` 字节/秒，`upTotal/downTotal` 累计字节 |
| `/proxies`、`/proxies/:name` | GET/PUT/DELETE | 查代理/策略组、选节点、清 fixed |
| `/proxies/:name/delay` | GET | 延迟测试，`?url=&timeout=`、`?expected=200/204` |
| `/group`、`/group/:name/delay` | GET | 策略组信息与延迟 |
| `/providers/proxies`、`/providers/rules` | GET/PUT | 代理集合 / 规则集合 |
| `/rules` | GET/PATCH | 规则列表；`/rules/disable` PATCH `{"0":false,"1":true}` 临时禁用规则 |
| `/connections` | GET/WS/DELETE | 连接列表（`?interval=`）、关闭连接 |

⚠️ `?expected=` 支持范围写法（如 `200/204`、`200-299`）。