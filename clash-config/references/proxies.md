# 出站协议配置（proxies）

来源：`Hako/docs/config.yaml` + `adapter/outbound/` 各协议源码（v1.19.31，HEAD `7ea70d15`）。字段"必填"以 config.yaml 中未注释的字段为准（示例显式填写），实际必填性需对照 `adapter/outbound/` 各协议 ParseConfig。

## 通用字段（几乎所有协议共用）

| 字段 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `name` / `type` / `server` / `port` | — | 必填 | 节点名、协议类型、服务器地址、端口 |
| `udp` | bool | false | 支持 UDP |
| `tls` | bool | false | 启用 TLS（vmess/vless/trojan/ss/gost 等） |
| `sni` / `servername` | string | — | SNI；vmess 的 `servername` 优先于 `ws-opts.headers.Host` |
| `alpn` | list | — | ALPN 列表，如 `[h2, http/1.1]`；xhttp 默认仅 h2，h3 需 `alpn: [h3]` |
| `skip-cert-verify` | bool | false | 跳过证书校验 |
| `name-cert-verify` | string | — | 仅修改证书 DNSName 校验目标，不修改 SNI |
| `fingerprint` | string | — | SSL Pinning 指纹（`openssl x509 -noout -fingerprint -sha256 -inform pem -in yourcert.pem`） |
| `client-fingerprint` | string | — | chrome/firefox/safari/ios/random/none；仅 TLS transport 的 vless/vmess/trojan |
| `certificate` / `private-key` | string | — | mTLS 客户端证书/私钥，需同时填写 |
| `ip-version` | string | dual | dual/ipv4/ipv6/ipv4-prefer/ipv6-prefer；ipv4-prefer 对 TCP 需 `tcp-concurrent` 生效 |
| `dialer-proxy` | string | — | 链式代理（通过指定 proxy 发出连接） |
| `interface-name` / `routing-mark` | — | — | 出口网卡 / Linux fwmark |
| `ech-opts` | object | — | ECH：`enable` / `config`（base64，空则 DNS 解析 `dig +short TYPE65`）/ `query-server-name` |
| `shadow-tls-opts` | object | — | 需 `tls:true`；用 servername 作 SNI；`version`(1/2/3，默认2) / `password` |
| `restls-opts` | object | — | 需 `tls:true`；`password` / `version-hint`(tls12/tls13) / `restls-script` |
| `jls-opts` | object | — | 需 `tls:true`；`username` / `password` |
| `reality-opts` | object | — | `public-key`(必填) / `short-id` / `support-x25519mlkem768` |
| `ws-opts` | object | — | `path` / `headers` / `max-early-data` / `early-data-header-name` / `v2ray-http-upgrade` / `v2ray-http-upgrade-fast-open` |
| `grpc-opts` | object | — | `grpc-service-name`(必填) / `grpc-user-agent` / `ping-interval`(默认0关闭) / `max-connections`(默认1) / `min-streams` / `max-streams` |
| `ip-stack` | object | — | wireguard/openvpn/zerotier/masque/easytier 用；`mode`(auto/gvisor/mips) / `congestion-controller`(cubic/reno/bbr/bbr3) |
| `smux` | object | — | `enabled` / `protocol`(smux/yamux/h2mux) / `max-connections` / `min-streams` / `max-streams` / `padding`(需 sing-box server ≥1.3-beta9) / `statistic` / `only-tcp` |
| `remote-dns-resolve` | bool | false | 强制 DNS 远程解析；`dns` 字段仅此时生效 |

---

## 1. SOCKS5 (`type: socks5`)

```yaml
- name: "socks"
  type: socks5
  server: server
  port: 443
  # username: username
  # password: password
  # tls: true
  # fingerprint: xxxx
  # certificate: ./client.crt   # mTLS，需与 private-key 同时填
  # private-key: ./client.key
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # udp: true
  # ip-version: ipv6
```

## 2. HTTP (`type: http`)

```yaml
- name: "http"
  type: http
  server: server
  port: 443
  # username: username
  # password: password
  # tls: true              # https
  # sni: custom.com
  # skip-cert-verify: true
  # fingerprint: xxxx
  # certificate: ./client.crt
  # private-key: ./client.key
  # ip-version: dual
```

## 3. Snell (`type: snell`)

`psk` 必填。`version` 支持 1/2/3/4/5，UDP 仅 3/4/5 支持，`reuse` 仅 v4/5。`obfs-opts.mode` 可选 `http`/`tls`/`shadow-tls`/`restls`/`jls`。

```yaml
- name: "snell"
  type: snell
  server: server
  port: 44046
  psk: yourpsk
  # version: 4
  # udp: true
  # reuse: false
  # client-fingerprint: chrome
  # obfs-opts:
  #   mode: http           # http/tls/shadow-tls/restls/jls
  #   host: bing.com
  #   password: "shadow_tls_password"   # shadow-tls / restls
  #   version: 2           # shadow-tls 1/2/3
  #   alpn: ["h2","http/1.1"]
  #   version-hint: tls13  # restls
  #   username: jls-user   # jls
```

## 4. Shadowsocks (`type: ss`)

**cipher 支持**：aes-128/192/256-gcm、aes-128/192/256-cfb、aes-128/192/256-ctr、rc4-md5、chacha20-ietf、xchacha20、chacha20-ietf-poly1305、xchacha20-ietf-poly1305、2022-blake3-aes-128-gcm、2022-blake3-aes-256-gcm、2022-blake3-chacha20-poly1305

```yaml
- name: "ss1"
  type: ss
  server: server
  port: 443
  cipher: chacha20-ietf-poly1305
  password: "password"
  # udp: true
  # udp-over-tcp: false
  # ip-version: dual
  # dialer-proxy: gost-relay-hop     # 链式
  # smux:
  #   enabled: true
  #   protocol: smux                   # smux/yamux/h2mux
  #   max-connections: 4               # 与 max-streams 冲突
  #   min-streams: 4                   # 与 max-streams 冲突
  #   max-streams: 0                   # 与 max-connections/min-streams 冲突
  #   padding: false                   # 需 sing-box server ≥1.3-beta9
  #   statistic: false
  #   only-tcp: false
```

**plugin 类型**：

| plugin | plugin-opts |
|---|---|
| `obfs` | `mode`(tls/http) / `host` |
| `v2ray-plugin` | `mode`(websocket，暂无 QUIC) / `tls` / `fingerprint` / `certificate` / `private-key` / `ech-opts` / `skip-cert-verify` / `name-cert-verify` / `host` / `path` / `mux` / `headers` / `v2ray-http-upgrade` / `v2ray-http-upgrade-fast-open` |
| `shadow-tls` | `host` / `password` / `version`(1/2/3) / `alpn` |
| `gost-plugin` | `mode`(websocket) / `tls` / `fingerprint` / `certificate` / `private-key` / `skip-cert-verify` / `name-cert-verify` / `host` / `path` / `mux` / `headers` |
| `jls` | `host` / `username` / `password` / `alpn` |
| `restls` | `host`(须 TLS1.2/1.3 服务器) / `password` / `version-hint`(tls12/tls13) / `restls-script` |
| `kcptun` | 见下 |

```yaml
  # kcptun 插件（KCP 传输）
  - name: "ss-kcptun"
    type: ss
    server: [YOUR_SERVER_IP]
    port: 443
    cipher: chacha20-ietf-poly1305
    password: [YOUR_SS_PASSWORD]
    plugin: kcptun
    plugin-opts:
      key: it's a secrect
      crypt: aes              # aes/aes-128/aes-128-gcm/aes-192/salsa20/blowfish/twofish/cast5/3des/tea/xtea/xor/none/null
      mode: fast              # fast3/fast2/fast/normal/manual
      conn: 1                 # UDP 连接数
      autoexpire: 0           # 单连接自动过期秒，0 禁用
      scavengettl: 600        # 过期连接存活秒
      mtu: 1350               # UDP 包 MTU
      ratelimit: 0            # 上行 bytes/s，0 禁用
      sndwnd: 128             # 发送窗口（包数）
      rcvwnd: 512             # 接收窗口（包数）
      datashard: 10           # RS 纠删码数据分片
      parityshard: 3          # RS 纠删码校验分片
      dscp: 0                 # DSCP(6bit)
      nocomp: false
      acknodelay: false
      nodelay: 0
      interval: 50
      resend: 0
      sockbuf: 4194304        # 每 socket 缓冲字节
      smuxver: 1              # smux 版本 1/2
      smuxbuf: 4194304        # 总 demux 缓冲
      framesize: 8192         # smux 最大帧
      streambuf: 2097152      # 每流缓冲（smux v2+）
      keepalive: 10           # 心跳间隔秒
```

## 5. GOST Relay (`type: gost-relay`)

动态模式：relay 连接上层代理请求的目标；通过 `dialer-proxy` 承载 ss/vmess/vless/trojan。forward 模式：relay 服务端选转发目标。

```yaml
- name: "gost-relay-hop"
  type: gost-relay
  server: relay.example.com
  port: 443
  udp: true
  tls: true
  # forward: true            # forward 模式（服务端选转发目标）
  # mux: true                # relay+mtls（需 tls:true）
  # sni: relay.example.com
  # username: user
  # password: pass
  # client-fingerprint: chrome
  # fingerprint: xxxx
  # certificate: ./client.crt
  # private-key: ./client.key
  # skip-cert-verify: true
  # name-cert-verify: example.com

# 用法：目标节点通过 dialer-proxy 指向它
- name: "ss6-gost-relay"
  type: ss
  server: 127.0.0.1          # relay 服务端本地监听的地址
  port: 12345
  cipher: chacha20-ietf-poly1305
  password: "password"
  udp: true
  dialer-proxy: gost-relay-hop
```

## 6. VMess (`type: vmess`)

**cipher**：auto/aes-128-gcm/chacha20-poly1305/none。`network`：ws/mkcp/mekya/h2/http/grpc。

```yaml
- name: "vmess"
  type: vmess
  server: server
  port: 443
  uuid: uuid
  alterId: 32
  cipher: auto
  # network: ws              # ws/mkcp/mekya/h2/http/grpc
  # tls: true
  # servername: example.com  # 优先于 ws-opts.headers.Host
  # fingerprint: xxxx
  # client-fingerprint: chrome
  # certificate: ./client.crt
  # private-key: ./client.key
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # udp: true
  # ip-version: dual
  # ech-opts: { enable: true, config: "...", query-server-name: "xxx.com" }
  # reality-opts: { public-key: xxx, short-id: xxx, support-x25519mlkem768: false }
  # shadow-tls-opts: { version: 3, password: "shadow-tls-password" }
  # restls-opts: { password: "restls-password", version-hint: tls13, restls-script: "" }
  # jls-opts: { username: jls-user, password: jls-password }
  # ws-opts:
  #   path: /path
  #   headers: { Host: v2ray.com }
  #   max-early-data: 2048
  #   early-data-header-name: Sec-WebSocket-Protocol
  #   v2ray-http-upgrade: false
  #   v2ray-http-upgrade-fast-open: false
  # grpc-opts:
  #   grpc-service-name: "example"
  #   grpc-user-agent: "grpc-go/1.36.0"
  #   ping-interval: 0
  #   max-connections: 1
  #   min-streams: 0
  #   max-streams: 0
  # h2-opts: { host: [http.example.com, http-alt.example.com], path: / }
  # http-opts: { method: GET, path: ['/', '/video'], headers: { Connection: [keep-alive] } }
  # mkcp-opts:
  #   mtu: 1350
  #   tti: 50                     # 传输时间间隔 ms
  #   uplink-capacity: 5          # MB/s
  #   downlink-capacity: 20
  #   congestion: false
  #   write-buffer: 2097152
  #   read-buffer: 2097152
  #   seed: ""                    # AES-GCM 认证种子，空用默认
  #   header: ""                  # none/srtp/utp/wechat-video/dtls/wireguard
  # mekya-opts:
  #   url: https://server:443/mekya
  #   max-write-delay: 80         # 首包后最大聚合等待 ms
  #   max-request-size: 96000     # 单次 HTTP 请求最大负载字节
  #   polling-interval-initial: 200
  #   h2-pool-size: 8             # HTTP/2 连接池
  #   kcp: { mtu: 1350, tti: 15, uplink-capacity: 40, downlink-capacity: 2000, congestion: false, write-buffer: 67108864, read-buffer: 67108864, seed: "", header: "" }
  # tlsmirror-opts:               # 需 tls:true，载体复用 servername/alpn/cert 等
  #   primary-key: MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=   # 32字节 base64
  #   explicit-nonce-ciphersuites: [156, 157, 158, 159]
  #   defer-instance-derived-write-time: { base-nanoseconds: 0, uniform-random-multiplier-nanoseconds: 0 }
  #   transport-layer-padding: { enabled: false }
  #   connection-enrolment: { primary-egress-outbound: "" }   # mihomo 保持空
  #   sequence-watermarking-enabled: false
  #   embedded-traffic-generator:
  #     steps:
  #       - host: example.com
  #         path: /
  #         method: GET
  #         connection-ready: true
  #         connection-recall-exit: true
  #         h2-do-not-wait-for-download-finish: false
  #         wait-time: { base-nanoseconds: 1000000000 }
  #         next-step: [ { weight: 1, goto-location: 0 } ]
```

## 7. VLESS (`type: vless`)

`network`：tcp/grpc/ws/xhttp。reality 时 `client-fingerprint` 不可为空。

```yaml
- name: "vless-tcp"
  type: vless
  server: server
  port: 443
  uuid: uuid
  network: tcp
  servername: example.com      # AKA SNI
  # tls: true
  # udp: true
  # flow: xtls-rprx-vision     # vision / xtls-rprx-origin / xtls-rprx-direct
  # client-fingerprint: chrome # reality 时不可为空
  # encryption: "mlkem768x25519plus.native/xorpub/random.1rtt/0rtt.(padding len).(padding gap).(X25519).(ML-KEM)..."
  # alpn: [h2]                 # xhttp 默认仅 h2
  # ech-opts / reality-opts / shadow-tls-opts / restls-opts / jls-opts: 同上
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # certificate: ./client.crt
  # private-key: ./client.key
  # fingerprint: xxxx
  # ws-opts / grpc-opts / xhttp-opts: 见下
```

**xhttp-opts**（`network: xhttp`）：

```yaml
  xhttp-opts:
    path: "/"
    host: xxx.com
    # mode: stream-one         # stream-one/stream-up/packet-up
    # headers: { X-Forwarded-For: "" }
    # no-grpc-header: false
    # x-padding-bytes: "100-1000"
    # x-padding-obfs-mode: false
    # x-padding-key: x_padding
    # x-padding-header: Referer
    # x-padding-placement: queryInHeader   # queryInHeader/cookie/header/query
    # x-padding-method: repeat-x           # repeat-x/tokenish
    # uplink-http-method: POST             # POST/PUT/PATCH/DELETE
    # session-placement: path              # path/query/cookie/header
    # session-key: ""
    # seq-placement: path
    # seq-key: ""
    # uplink-data-placement: body          # body/cookie/header
    # uplink-data-key: ""
    # uplink-chunk-size: 0                 # 非 body 时生效
    # sc-max-each-post-bytes: 1000000
    # sc-min-posts-interval-ms: 30
    # reuse-settings:                      # aka XMUX
    #   max-concurrency: "16-32"
    #   max-connections: "0"
    #   c-max-reuse-times: "0"
    #   h-max-request-times: "600-900"
    #   h-max-reusable-secs: "1800-3000"
    #   h-keep-alive-period: 0
    # download-settings:                   # 下载通道独立配置
    #   path: "/"
    #   host: xxx.com
    #   headers: { X-Forwarded-For: "" }
    #   reuse-settings: { max-concurrency: "16-32", max-connections: "0", c-max-reuse-times: "0", h-max-request-times: "600-900", h-max-reusable-secs: "1800-3000", h-keep-alive-period: 0 }
    #   # proxy part: server/port/tls/alpn/ech-opts/shadow-tls-opts/restls-opts/jls-opts/reality-opts/skip-cert-verify/name-cert-verify/fingerprint/certificate/private-key/servername/client-fingerprint
```

**vless encryption**：native/xorpub 的 XTLS Vision 可 Splice。只使用 1-RTT 模式（服务端 ticket 秒数非零则 0-RTT 复用）。`/` 分隔多选，后面 base64 至少一个无限串联。用 `mihomo generate vless-x25519` / `mihomo generate vless-mlkem768` 生成，替换值时去掉括号。Padding 仅 1-RTT，双端默认 `"100-111-1111.75-0-111.50-0-3333"`；第一个 padding 需概率 100% 且至少 35 字节。

## 8. Trojan (`type: trojan`)

`network`：tcp/grpc/ws。`flow`：xtls-rprx-origin/xtls-rprx-direct。

```yaml
- name: "trojan"
  type: trojan
  server: server
  port: 443
  password: yourpsk
  # network: grpc              # tcp/grpc/ws
  # sni: example.com           # aka server name
  # alpn: [h2, http/1.1]
  # udp: true
  # flow: xtls-rprx-direct     # xtls-rprx-origin / xtls-rprx-direct
  # flow-show: true
  # client-fingerprint: random # chrome/firefox/safari/random/none
  # fingerprint: xxxx
  # certificate: ./client.crt
  # private-key: ./client.key
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # ss-opts:                   # like trojan-go's shadowsocks
  #   enabled: false
  #   method: aes-128-gcm      # aes-128-gcm/aes-256-gcm/chacha20-ietf-poly1305
  #   password: "example"
  # ech-opts / reality-opts / shadow-tls-opts / restls-opts / jls-opts / ws-opts / grpc-opts: 同上
```

## 9. Hysteria v1 (`type: hysteria`)

`protocol` 支持 udp/wechat-video/faketcp。`ports` 端口范围如 `1000,2000-3000,5000`（`port` 不可省略）。

```yaml
- name: "hysteria"
  type: hysteria
  server: server.com
  port: 443
  # ports: 1000,2000-3000,5000
  auth-str: yourpassword
  protocol: udp               # udp/wechat-video/faketcp
  up: "30 Mbps"               # 不写单位默认 Mbps
  down: "200 Mbps"
  # obfs: obfs_str
  # alpn: [h3]
  # sni: server.com
  # ech-opts: { enable: true, config: "...", query-server-name: "xxx.com" }
  # skip-cert-verify: false
  # name-cert-verify: example.com
  # recv-window-conn: 12582912
  # recv-window: 52428800
  # disable-mtu-discovery: false
  # fingerprint: xxxx
  # certificate: ./client.crt
  # private-key: ./client.key
  # fast-open: true            # TCP 快速打开
```

## 10. Hysteria2 (`type: hysteria2`)

```yaml
- name: "hysteria2"
  type: hysteria2
  server: server.com
  port: 443
  password: yourpassword
  # ports: 1000,2000-3000,5000
  # hop-interval: 15           # 支持 "15-30" 随机范围，仅一个范围不允许逗号
  # up: "30 Mbps"              # 不写或 0 则用 BBR 流控
  # down: "200 Mbps"
  # bbr-profile: standard      # standard/conservative/aggressive
  # obfs: salamander           # salamander / gecko
  # obfs-password: yourpassword
  # obfs-min-packet-size: 512  # 仅 Gecko
  # obfs-max-packet-size: 1200 # 仅 Gecko
  # sni: server.com
  # alpn: [h3]
  # ech-opts: { enable: true, config: "...", query-server-name: "xxx.com" }
  # skip-cert-verify: false
  # name-cert-verify: example.com
  # fingerprint: xxxx
  # certificate: ./client.crt
  # private-key: ./client.key
  # handshake-timeout: 30      # 秒；0 仅用外层超时
  # realm-opts:
  #   enable: true             # 必须手动开启
  #   server-url: https://realm.hy2.io
  #   token: public
  #   realm-id: my-cabin-1f3a8c2e9b
  #   stun-servers:
  #     - stun.nextcloud.com:3478
  #     - stun.sip.us:3478
  #     - global.stun.twilio.com:3478
  #   # 针对 server-url 的 TLS：sni / skip-cert-verify / name-cert-verify / fingerprint / certificate / private-key / alpn
  ### quic-go 特殊配置，不要随意修改 ###
  # initial-stream-receive-window: 8388608
  # max-stream-receive-window: 8388608
  # initial-connection-receive-window: 20971520
  # max-connection-receive-window: 20971520
```

## 11. WireGuard (`type: wireguard`)

```yaml
- name: "wg"
  type: wireguard
  server: 162.159.192.1
  port: 2480
  ip: 172.16.0.2
  ipv6: fd01:5ca1:ab1e:80fa:ab85:6eea:213f:f4a5
  public-key: Cr8hWlKvtDt7nrvf+f0brNQQzabAqrjfBvas9pmowjo=
  # pre-shared-key: 31aIhAPwktDGpH4JDhA8GNvjFXEf/a6+UaQRyOAiyfM=
  private-key: eCtXsJZ27+4PbhDkHnB923tkUn2Gj59wZw5wFA75MnU=
  udp: true
  reserved: "U4An"             # 也支持数组 [209,98,59]
  # persistent-keepalive: 0
  # ip-stack:
  #   mode: auto               # auto/gvisor/mips
  #   congestion-controller: cubic   # cubic/reno/bbr/bbr3；gVisor 忽略
  # dialer-proxy: "ss1"
  # remote-dns-resolve: true   # 强制 DNS 远程解析
  # dns: [1.1.1.1, 8.8.8.8]    # 仅 remote-dns-resolve 为 true 生效
  # refresh-server-ip-interval: 60   # 重新解析 server ip 间隔秒，0 仅首次解析（家宽 ddns 用）
  # peers:                     # 非空时顶层 server/port/public-key/pre-shared-key 被忽略，private-key 保留且仅顶层
  #   - server: 162.159.192.1
  #     port: 2480
  #     public-key: Cr8hWlKvtDt7nrvf+f0brNQQzabAqrjfBvas9pmowjo=
  #     allowed-ips: ['0.0.0.0/0']
  #     reserved: [209,98,59]
  # amnezia-wg-option:
  #   version: 2               # 仅 v3 用 v3 实现，其余 legacy
  #   jc: 5                    # AmneziaWG v1.0+
  #   jmin: 500
  #   jmax: 501
  #   s1: 30                   # v1.0+
  #   s2: 40                   # v1.0+
  #   s3: 50                   # v1.5+
  #   s4: 8                    # v1.5+
  #   h1: 123456               # v1.0/v1.5 仅单值；v2+ 支持范围
  #   h2: 67543
  #   h3: 123123
  #   h4: 32345
  #   i1: <b 0xf6ab3267fa><b 0xf6ab><t><r 10>   # v1.5+
  #   i2: <b 0xf6ab3267fa><r 100>                # v1.5+
  #   i3: ""                 # v1.5+
  #   i4: ""                 # v1.5+
  #   i5: ""                 # v1.5+
  #   j1: <b 0xffffffff><c><b 0xf6ab><t><r 10>  # v1.5 only（v2+ 移除）
  #   j2: <c><b 0xf6ab><t><wt 1000>              # v1.5 only
  #   j3: <t><b 0xf6ab><c><r 10>                 # v1.5 only
  #   itime: 60              # v1.5 only
  #   header-protection-key: >-                    # v3+
  #     MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=
  #   content-padding-addition: 0-32               # v3+
  #   rekey-after-time: 120                        # v3+
  #   rekey-timeout: 5                             # v3+
  #   reject-after-time: 180                       # v3+
  #   keepalive-timeout: 10                        # v3+
  #   max-handshake-attempts: 18                   # v3+
  #   random-trailers: true                        # v3.1+
  #   disable-cookies: true                        # v3.1+
```

## 12. Tailscale (`type: tailscale`)

**注**：目标不在 Tailscale 路由内时连接直接报错，不会回退直连；访问公网需配 `exit-node` 或接受覆盖目标网段的 subnet routes。

```yaml
- name: "tailscale"
  type: tailscale
  # hostname: mihomo               # Tailscale 设备名，默认由 tsnet 处理
  # auth-key: tskey-auth-xxxx      # 可选；不填首次启动输出交互式登录 URL
  # control-url: https://controlplane.tailscale.com   # 自定义 Headscale/Tailscale control
  # state-dir: ./tailscale         # tsnet 状态目录，默认 tailscale
  # ephemeral: false               # 作为 ephemeral node 登录
  udp: true
  # accept-routes: true            # 接受 Tailnet 中发布的 subnet routes
  # exit-node: 100.64.0.1          # 指定 exit node，支持 auto:any
  # exit-node-allow-lan-access: true
  # dialer-proxy: "ss1"            # 控制面/DERP/STUN 连接走指定 proxy
  # interface-name: "WLAN"
  # routing-mark: 6666
  # ip-version: ipv4-prefer
```

## 13. ZeroTier (`type: zerotier`)

```yaml
- name: "zerotier"
  type: zerotier
  network: "0123456789abcdef"     # 16 位 network ID
  # state-dir: ./zerotier-node     # 持久节点状态和默认身份；默认由 network 和出站名派生隔离目录
  # identity-secret: "0123456789:0:pub-key:priv-key" # 完整 identity.secret 内容；覆盖 state-dir 中的身份，不会写入磁盘
  # planet: ./planet               # 私有 planet 文件，替换内置 Earth planet
  # mtu: 1400                      # 本地 MTU 覆盖，不能超过 controller MTU
  # physical-mtu: 1432             # ZeroTier UDP payload MTU（510-10324，默认 1432）
  # ip-stack: { mode: auto, congestion-controller: cubic }
  # primary-port: 0                # 主 UDP 端口，0 自动选
  # secondary-port: 0              # 次 UDP 端口，0 自动选，-1 禁用
  # tcp-fallback-mode: auto        # auto(UDP失败后relay)/force(仅relay)/disable(关relay)
  # tcp-fallback-relay: 204.80.128.1:443
  # remote-trace-target: "0123456789"   # 接收全局诊断 trace 的 node ID
  # remote-trace-level: 0            # 0 normal / 10 verbose / 15 rules / 20 debug / 30 insane
  # low-bandwidth: false             # 减少后台流量和配置刷新频率
  # encrypted-hello: false           # protocol-13 扩展加密外发 HELLO 包
  # orbit:                           # 联邦 root worlds (moons)
  #   - world: "0123456789abcdef"    # 16 位 moon world ID
  #     seed: "0123456789"           # 10 位 moon root node ID
  udp: true
  # remote-dns-resolve: true         # 通过 ZeroTier 用 controller 提供的 DNS 解析
  # dns: [10.147.17.1]               # 覆盖 controller 提供的 DNS
  # dialer-proxy: "ss1"              # 承载 ZeroTier wire 流量
  # interface-name: "WLAN"
  # routing-mark: 6666
  # ip-version: ipv4-prefer
```

## 14. EasyTier (`type: easytier`)

mesh VPN overlay 协议，基于 [easytier/easytier](https://github.com/easytier/easytier)。overlay 仅支持 IPv4；`ip-version` 只影响底层 peer 连接，不启用 overlay IPv6。

```yaml
- name: "easytier"
  type: easytier
  network-name: example            # 网络名称
  network-secret: secret            # 网络密钥
  # hostname: mihomo               # 节点主机名
  # ipv4: 10.144.0.1/24            # 指定 overlay IPv4
  # dhcp: true                     # ipv4 为空时默认开启，否则实例没有 overlay IPv4
  peers:                           # 可配置多个入口；默认不隐式连接 public.easytier.top；无 listeners 时至少填一个
    - tcp://192.0.2.10:11010
    - udp://192.0.2.11:11010
    # - "tcp://relay.example.com:11010?peer-public-key=base64-x25519-pub-key" # 锁定共享节点公钥，防中间人
  # secure-mode: true              # Noise E2EE；配置 local-*-key 或 peer URI 中的 peer-public-key 时自动开启
  # local-private-key: "base64-x25519-priv-key" # 固定本机身份，避免每次启动更换公钥
  # local-public-key: "base64-x25519-pub-key"  # 通常可由私钥派生
  # listeners: ["tcp://0.0.0.0:11010"]          # 本地监听地址
  # no-listener: true               # 默认 true，listeners 为空
  # mapped-listeners: ["tcp://203.0.113.10:11010"] # 对外映射地址
  # exit-nodes: ["10.144.0.1"]     # 指定出口节点
  # proxy-networks: ["10.0.0.0/24"] # 代理网络 CIDR
  # instance-name: mihomo-easytier  # 实例名
  # state-dir: ./easytier           # 默认 easytier/<name>，持久化 instance_id
  udp: true                        # 是否支持 UDP 转发
  # accept-dns: false              # 接受 EasyTier 网络 DNS
  # enable-exit-node: false        # 作为出口节点
  # enable-encryption: true         # 启用加密
  # encryption-algorithm: aes-gcm  # 加密算法
  # private-mode: false             # 私有网络模式
  # latency-first: false           # 延迟优先路由
  # disable-p2p: false              # 禁用 P2P
  # enable-kcp-proxy: false        # KCP 代理
  # disable-kcp-input: false        # 禁止 KCP 入站
  # enable-quic-proxy: false        # QUIC 代理
  # disable-quic-input: false       # 禁止 QUIC 入站
  # mtu: 1380
  # tld-dns-zone: et.net.           # EasyTier 顶层 DNS 域
  # dialer-proxy: "ss1"             # 承载 EasyTier peer 流量
  # interface-name: "WLAN"
  # routing-mark: 6666
  # ip-version: ipv4-prefer
```

| 字段 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `network-name` | string | — | 网络名称 |
| `network-secret` | string | — | 网络密钥 |
| `hostname` | string | — | 节点主机名 |
| `ipv4` | string | — | 指定 overlay IPv4 地址/CIDR |
| `dhcp` | bool | true（ipv4 为空时） | 自动获取 overlay IPv4 |
| `peers` | []string | — | peer 入口地址列表，至少一个 |
| `listeners` | []string | — | 本地监听地址 |
| `no-listener` | *bool | true | 不监听，listeners 为空时默认 true |
| `mapped-listeners` | []string | — | 对外映射地址（NAT 穿透） |
| `exit-nodes` | []string | — | 指定出口节点 IP 列表 |
| `proxy-networks` | []string | — | 代理网络 CIDR |
| `instance-name` | string | 出站 name | 实例名 |
| `state-dir` | string | `easytier/<name>` | 持久化 instance_id |
| `udp` | bool | false | 支持 UDP 转发 |
| `accept-dns` | *bool | false | 接受 EasyTier 网络 DNS |
| `enable-exit-node` | *bool | false | 作为出口节点 |
| `enable-encryption` | *bool | false | 启用加密 |
| `encryption-algorithm` | string | — | 加密算法（如 aes-gcm） |
| `private-mode` | *bool | false | 私有网络模式 |
| `latency-first` | *bool | false | 延迟优先路由 |
| `disable-p2p` | *bool | false | 禁用 P2P |
| `enable-kcp-proxy` | *bool | false | KCP 代理 |
| `disable-kcp-input` | *bool | false | 禁止 KCP 入站 |
| `enable-quic-proxy` | *bool | false | QUIC 代理 |
| `disable-quic-input` | *bool | false | 禁止 QUIC 入站 |
| `mtu` | int | 1380 | MTU |
| `tld-dns-zone` | string | — | 顶层 DNS 域 |
| `secure-mode` | *bool | false | Noise E2EE 加密 |
| `local-private-key` | string | — | X25519 私钥（base64），固定身份 |
| `local-public-key` | string | — | X25519 公钥（base64），通常由私钥派生 |

DNS 集成：在 DNS nameserver 中使用 `et://easytier` 可解析 EasyTier overlay 的 A/PTR 记录，建议放在 `nameserver-policy`。

## 15. OpenVPN (`type: openvpn`)

```yaml
- name: "openvpn"
  type: openvpn
  server: vpn.example.com
  port: 1194
  proto: udp                     # udp/tcp，默认 udp
  # dev: tun                     # 目前仅支持 tun
  # cipher: AES-128-GCM          # AES-128/192/256-GCM、AES-128/192/256-CBC、CHACHA20-POLY1305；AES-CBC 按 AES-128-CBC 处理
  # data-ciphers: [AES-256-GCM, AES-128-GCM]   # 发送 IV_CIPHERS，与服务端 push 取交集取首个
  # data-ciphers-fallback: AES-128-CBC         # 协商失败回退 cipher
  # auth: SHA256                 # MD5/SHA1/SHA256/SHA384/SHA512；AEAD cipher 忽略 auth
  # comp-lzo: "no"               # yes/no/adaptive
  # username: "user"             # auth-user-pass 模式（与 cert+key 二选一）
  # password: "pass"
  ca: |                          # 从 .ovpn 复制 <ca></ca> 内容，不含标签
    -----BEGIN CERTIFICATE-----
    MIIB...example
    -----END CERTIFICATE-----
  # cert: |                      # <cert></cert> 内容（auth-user-pass 时可省略 cert/key）
  #   -----BEGIN CERTIFICATE-----
  #   MIIB...example
  #   -----END CERTIFICATE-----
  # key: |                       # <key></key> 内容
  #   -----BEGIN PRIVATE KEY-----
  #   MIIE...example
  #   -----END PRIVATE KEY-----
  # tls-auth: |                  # <tls-auth></tls-auth> 内容；与 tls-crypt 互斥
  #   -----BEGIN OpenVPN Static key V1-----
  #   00000000000000000000000000000000
  #   ...
  #   -----END OpenVPN Static key V1-----
  # key-direction: "1"           # "1"/"0"；空为双向 bidirectional
  # tls-crypt: |                 # <tls-crypt></tls-crypt> 内容；与 tls-auth/tls-crypt-v2 互斥
  #   -----BEGIN OpenVPN Static key V1-----
  #   00000000000000000000000000000000
  #   -----END OpenVPN Static key V1-----
  # tls-crypt-v2: |              # <tls-crypt-v2></tls-crypt-v2>；独立客户端密钥（PEM 含 256 字节密钥+wrapped key）；与 tls-auth/tls-crypt 互斥
  #   -----BEGIN OpenVPN tls-crypt-v2 client key-----
  #   AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8...
  #   -----END OpenVPN tls-crypt-v2 client key-----
  # peer-info:                   # 透传给服务端的 peer-info，追加在内置 IV_VER/IV_PROTO/IV_CIPHERS 之后
  #   IV_HWADDR: "52:54:00:ff:72:87"
  #   UV_DEVICE_ID: "laptop-001"
  # ping: 10                     # 默认 0
  # ping-restart: 60             # 默认 0
  # tran-window: 3600            # 旧 data key rekey 后保留秒；0 立即过期，应与服务端 --tran-window 对齐
  # handshake-timeout: 30        # 秒；0 仅用外层超时
  # mtu: 1500
  udp: true
  # ip-stack: { mode: auto, congestion-controller: cubic }
  # dialer-proxy: "ss1"
  # remote-dns-resolve: true
  # dns: [1.1.1.1, 8.8.8.8]
```

## 16. MASQUE (`type: masque`)

3 种变体：标准 QUIC、`h3-l4proxy`（不支持 udp，须 false）、`h2`。

```yaml
- name: "masque"
  type: masque
  server: 162.159.198.1
  port: 443
  private-key: MHcCAQEEILI1eOtnbEIh89Fj4yNDuFR6UjayCKI3NdLl3DhetimWoAoGCCqGSM49AwEHoUQDQgAEgyXrE8v+hHsHy3ewSb3WcRjYgCrM9T9hiE0Uv6k2DZ1+4kefrDT9v1Q/8wdRigTf6t6gGNUV8W+IUMdrfUt+9g==
  public-key: MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEIaU7MToJm9NKp8YfGxR6r+/h4mcG7SxI8tsW8OR1A5tv/zCzVbCRRh2t87/kxnP6lAy0lkr7qYwu+ox+k3dr6w==
  ip: 172.16.0.2
  ipv6: 2606:4700:110:84c0:163a:4914:a0ad:3342
  mtu: 1280
  udp: true
  # network: h3-l4proxy          # h3-l4proxy / h2
  # ip-stack: { mode: auto, congestion-controller: cubic }
  # dialer-proxy: "ss1"
  # remote-dns-resolve: true
  # dns: [1.1.1.1, 8.8.8.8]
  # congestion-controller: bbr   # 默认不开启
  # handshake-timeout: 30
```

## 17. TUIC (`type: tuic`)

**tuicV4 必须填 `token`（不可同时填 uuid+password）；tuicV5 必须填 `uuid`+`password`（不可同时填 token）**。

```yaml
- name: tuic
  type: tuic
  server: www.example.com
  port: 10443
  token: TOKEN                    # tuicV4
  uuid: 00000000-0000-0000-0000-000000000001   # tuicV5
  password: PASSWORD_1            # tuicV5
  # ip: 127.0.0.1                 # 覆盖 server 的 DNS 解析结果
  # heartbeat-interval: 10000     # ms
  # alpn: [h3]
  disable-sni: true
  reduce-rtt: true
  request-timeout: 8000           # ms
  udp-relay-mode: native          # native/quic，默认 native
  # congestion-controller: bbr    # cubic/new_reno/bbr，默认 cubic
  # cwnd: 10                      # 默认 32
  # bbr-profile: standard         # standard/conservative/aggressive
  # max-udp-relay-packet-size: 1500
  # fast-open: true
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # max-open-streams: 20          # 默认 100，过多影响性能
  # sni: example.com
  # ech-opts: { enable: true, config: "...", query-server-name: "xxx.com" }
  ### meta 和 sing-box 私有扩展，开启后 udp-relay-mode 失效；与原版 tuic 不兼容！！！
  # udp-over-stream: false
  # udp-over-stream-version: 1
```

## 18. ShadowQUIC (`type: shadowquic`)

```yaml
- name: shadowquic
  type: shadowquic
  server: www.example.com
  port: 10443
  username: username
  password: password
  # sni: example.com
  # alpn: [h3]
  # quic-versions: [v1]           # v1/v2，默认 v1
  # udp-over-stream: false
  # zero-rtt: false               # 官方 server 0-RTT 可能在 JLS 认证完成前读取用户状态（影响 v0.3.11）；不通/断联时服务端关闭
  # keep-alive-interval: 10000    # ms
  # congestion-controller: bbr    # cubic/new_reno/bbr，默认 cubic
  # up: 100 Mbps                  # mihomo 私有 brutal 协商；客户端上行速度；不支持时回退 congestion-controller
  # down: 100 Mbps                # 客户端下行速度，受 listener up 上限
  # cwnd: 10                      # 默认 32
  # bbr-profile: standard
  # max-datagram-frame-size: 1400
  # max-open-streams: 1024
  # recv-window-conn: 0
  # recv-window: 0
  # disable-mtu-discovery: false
```

## 19. ShadowsocksR (`type: ssr`)

**cipher**：ss 中所有流加密。**obfs**：plain/http_simple/http_post/random_head/tls1.2_ticket_auth/tls1.2_ticket_fastauth。**protocol**：origin/auth_sha1_v4/auth_aes128_md5/auth_aes128_sha1/auth_chain_a/auth_chain_b。

```yaml
- name: "ssr"
  type: ssr
  server: server
  port: 443
  cipher: chacha20-ietf
  password: "password"
  obfs: tls1.2_ticket_auth
  protocol: auth_sha1_v4
  # obfs-param: domain.tld
  # protocol-param: "#"
  # udp: true
```

## 20. SSH (`type: ssh`)

```yaml
- name: "ssh-out"
  type: ssh
  server: 127.0.0.1
  port: 22
  username: root
  password: password
  privateKey: path / private-key: path # 私钥路径（v1.19.31+ 推荐 private-key）
```

## 21. Mieru (`type: mieru`)

```yaml
- name: mieru
  type: mieru
  server: 1.2.3.4
  port: 2999
  # port-range: 2090-2099         # 不可同时填写 port 和 port-range
  transport: TCP                  # TCP / UDP
  udp: true                       # UDP over TCP
  username: user
  password: password
  # multiplexing: MULTIPLEXING_LOW   # MULTIPLEXING_OFF/LOW/MIDDLE/HIGH，默认 LOW
  # handshake-mode: HANDSHAKE_STANDARD  # HANDSHAKE_NO_WAIT(0-RTT) / HANDSHAKE_STANDARD
  # traffic-pattern: ""               # base64 字符串，微调网络行为
```

## 22. Sudoku (`type: sudoku`)

```yaml
- name: sudoku
  type: sudoku
  server: server_ip/domain
  port: 443
  key: "<client_key>"             # ED25519 密钥对私钥，否则填与服务端相同的 uuid
  aead-method: chacha20-poly1305  # chacha20-poly1305 / aes-128-gcm / none（不建议，无 AEAD 保护）
  padding-min: 2                  # 最小填充率 0-100
  padding-max: 7                  # 最大填充率 0-100，必须 >= padding-min
  table-type: prefer_ascii        # prefer_ascii / prefer_entropy / up_ascii_down_entropy / up_entropy_down_ascii
  # custom-table: xpxvvpvv        # 自定义字节布局，须含 2x/2p/4v；只对 entropy 方向生效
  # custom-tables: ["xpxvvpvv", "vxpvxvvp"]   # 非空覆盖 custom-table
  # multiplex: off                # off(默认) / auto(仅复用 HTTPMask 底层连接) / on(TCP 或 HTTPMask 上启用单会话多目标 mux)
  httpmask:
    disable: false                # true 禁用所有 HTTP 伪装/隧道
    mode: legacy                  # legacy(默认) / stream(split-stream) / poll / auto(先stream再poll) / ws(WebSocket 隧道)
    # tls: true                   # 按需开启 HTTPS/WSS
    # host: ""                    # 覆盖 Host/SNI（example.com 或 example.com:443）；仅 stream/poll/auto/ws 生效
    # path-root: ""               # HTTP 隧道端点一级路径前缀（双方一致），如 "aabbcc" => /aabbcc/session 等
    # multiplex: off              # 兼容旧配置，设置时优先于顶层 multiplex
  enable-pure-downlink: false     # false=带宽优化下行；true=纯 Sudoku 下行
```

## 23. AnyTLS (`type: anytls`)

```yaml
- name: anytls
  type: anytls
  server: 1.2.3.4
  port: 443
  password: "<your password>"
  udp: true
  # client-fingerprint: chrome
  # client-metadata: ""           # 客户端元数据，可能被服务端统计区别对待，v1.19.30 起默认不发送
  # idle-session-check-interval: 30   # 秒
  # idle-session-timeout: 30          # 秒
  # min-idle-session: 0
  # sni: "example.com"
  # alpn: [h2, http/1.1]
  # skip-cert-verify: true
  # name-cert-verify: example.com
  # shadow-tls-opts / restls-opts / jls-opts: 用 sni 作 SNI，见通用字段
```

## 24. TrustTunnel (`type: trusttunnel`)

```yaml
- name: trusttunnel
  type: trusttunnel
  server: 1.2.3.4
  port: 443
  username: username
  password: password
  udp: true
  health-check: true
  # client-fingerprint: chrome
  # sni: "example.com"
  # alpn: [h2]
  # skip-cert-verify: true
  # name-cert-verify: example.com
  ### quic options
  # quic: true                    # 默认 false
  # congestion-controller: bbr
  # bbr-profile: standard         # standard/conservative/aggressive
  ### reuse options
  # max-connections: 8            # 与 max-streams 冲突
  # min-streams: 5                # 与 max-streams 冲突
  # max-streams: 0                # 与 max-connections/min-streams 冲突
```

## 25. DNS 出站 (`type: dns`)

请求劫持到内部 dns 模块，所有请求均在内部处理。**无其他配置字段**。

```yaml
- name: "dns-out"
  type: dns
```

## 26. Rematch (`type: rematch`)

```yaml
- name: "rematch"
  type: rematch
  target-rematch-name: "rematch1"   # 覆盖原始 metadata 中的 rematch-name（可用 REMATCH-NAME 规则匹配）
  target-sub-rule: "sub-rule1"      # 直接用指定 sub-rule 匹配；名字不存在或为空回退主 rules
```

## 27. Direct (`type: direct`)

自定义 interface-name 和 fwmark 的直连节点。

```yaml
- name: en1-direct
  type: direct
  interface-name: en1
  routing-mark: 6667
```

---

## 协议索引汇总

| # | 协议 | type 值 | 变体 |
|---|---|---|---|
| 1 | SOCKS5 | `socks5` | — |
| 2 | HTTP | `http` | — |
| 3 | Snell | `snell` | 4 obfs（http/tls/shadow-tls/restls/jls） |
| 4 | Shadowsocks | `ss` | 7 plugin（obfs/v2ray-plugin/shadow-tls/gost-plugin/jls/restls/kcptun）+ smux + dialer-proxy |
| 5 | GOST Relay | `gost-relay` | dynamic / forward |
| 6 | VMess | `vmess` | ws / mkcp / mekya / h2 / http / grpc + tlsmirror |
| 7 | VLESS | `vless` | tcp / vision / encryption / reality-vision / reality-grpc / ws / xhttp |
| 8 | Trojan | `trojan` | tcp / grpc / ws / xtls + ss-opts |
| 9 | Hysteria v1 | `hysteria` | — |
| 10 | Hysteria2 | `hysteria2` | realm-opts |
| 11 | WireGuard | `wireguard` | peers / AmneziaWG |
| 12 | Tailscale | `tailscale` | exit-node |
| 13 | ZeroTier | `zerotier` | orbit / identity-secret |
| 14 | EasyTier | `easytier` | mesh overlay / Noise E2EE / exit-nodes |
| 15 | OpenVPN | `openvpn` | tls-auth / tls-crypt / tls-crypt-v2 |
| 16 | MASQUE | `masque` | quic / h3-l4proxy / h2 |
| 17 | TUIC | `tuic` | V4 / V5 |
| 18 | ShadowQUIC | `shadowquic` | — |
| 19 | ShadowsocksR | `ssr` | — |
| 20 | SSH | `ssh` | private-key / private-key-passphrase |
| 21 | Mieru | `mieru` | — |
| 22 | Sudoku | `sudoku` | httpmask |
| 23 | AnyTLS | `anytls` | — |
| 24 | TrustTunnel | `trusttunnel` | — |
| 25 | DNS 出站 | `dns` | — |
| 26 | Rematch | `rematch` | — |
| 27 | Direct | `direct` | — |

## 内置特殊代理（自动创建，无需在 proxies 声明）

| 名称 | 说明 |
|---|---|
| `DIRECT` | 直连 |
| `REJECT` | 拒绝 |
| `REJECT-DROP` | 拒绝（丢弃） |
| `COMPATIBLE` | 兼容代理 |
| `PASS` | 透传（不处理） |
| `PASS-RULE` | 透传规则 |
| `GLOBAL` | 全局选择组（自动创建） |
