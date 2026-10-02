# 入站监听（listeners）

来源：`Hako/docs/config.yaml` 1976-2812 行

监听类型与出站协议基本对应，字段大体一致。监听特有字段见下文。

## 通用字段（所有监听共享）

```yaml
- name: <name>            # 监听名称（规则里用 INBOUND 类型引用）
  type: <type>            # 监听类型
  port: <port>            # 端口，支持 ports 格式如 "200,302 or 200,204,401-429,501-503"
  listen: 0.0.0.0         # 监听地址，默认 0.0.0.0
  routing-mark: 0         # 监听 socket 的 routing-mark，仅 Linux
  rule: sub-rule-name1    # 指定子规则集（默认用 rules，未找到则直接用 rules）
  proxy: proxy            # 不为空则直接交由指定 proxy 处理（必须合法否则出错）
  udp: true               # 默认 true
  users: []               # 用户列表，不填遵从全局 authentication，填则忽略全局；空数组跳过验证
```

### TLS 配置（所有支持加密的监听共享）

```yaml
  certificate: ./server.crt    # PEM 内容或路径
  private-key: ./server.key    # PEM 内容或路径
  client-auth-type: ""         # ""/request/require-any/verify-if-given/require-and-verify
  client-auth-cert: string     # 客户端认证证书（verify-if-given/require-and-verify 时必填）
  ech-key: |                   # ECH 密钥（mihomo generate ech-keypair <域名>）
    -----BEGIN ECH KEYS-----
    ...
    -----END ECH KEYS-----
```

### 加密替换方案（可替代 certificate + private-key）

- **shadow-tls**：
```yaml
  shadow-tls:
    enable: true
    version: 3         # v1/v2/v3
    password: "password"  # v2 专用
    users:              # v3 专用
      - name: shadow-tls-user
        password: shadow-tls-password
    handshake:
      dest: www.example.com:443
      proxy: ""
```
- **res-tls**：
```yaml
  res-tls:
    enable: true
    dest: www.example.com:443
    password: restls-password
    restls-script: ""
    min-record-len: 0
    proxy: ""
    rate-limit: 0      # fallback 转发限速 bit/s，0=不限速
```
- **jls-config**：
```yaml
  jls-config:
    enable: true
    users:
      - username: jls-user
        password: jls-password
    dest: www.example.com:443
    sni: www.example.com   # 留空从 dest 推导
    alpn: [h2, http/1.1]
    proxy: ""
    rate-limit: 0          # fallback 限速 bit/s
```
- **reality-config**：
```yaml
  reality-config:
    dest: test.com:443
    private-key: jNXHt1yRo0vDuchQlIP6Z0ZvjT3KtzVI-T4E7RoLJS0  # mihomo generate reality-keypair
    short-id:
      - 0123456789abcdef
    server-names:
      - test.com
    limit-fallback-upload:       # 回落限速（不建议，是特征）
      after-bytes: 0
      bytes-per-sec: 0
      burst-bytes-per-sec: 0
    limit-fallback-download:
      after-bytes: 0
      bytes-per-sec: 0
      burst-bytes-per-sec: 0
```

**注意**：`allow-insecure: false` 时，vless/trojan/anytls 监听至少需要填 `certificate+private-key` 或 `shadow-tls` 或 `res-tls` 或 `jls-config` 或 `reality-config` 之一。

## 基础监听

### socks5

```yaml
- name: socks5-in-1
  type: socks
  port: 10808
  listen: 0.0.0.0
  udp: true
  users:
    - username: aaa
      password: aaa
```

### http

```yaml
- name: http-in-1
  type: http
  port: 10809
  listen: 0.0.0.0
  users:
    - username: aaa
      password: aaa
```

### mixed

```yaml
- name: mixed-in-1
  type: mixed           # HTTP(S) + SOCKS 混合
  port: 10810
  listen: 0.0.0.0
  udp: true
```

### redir

```yaml
- name: redir-in-1
  type: redir
  port: 10811
  listen: 0.0.0.0
```

### tproxy

```yaml
- name: tproxy-in-1
  type: tproxy
  port: 10812
  listen: 0.0.0.0
  udp: true
```

### shadowsocks

```yaml
- name: shadowsocks-in-1
  type: shadowsocks
  port: 10813
  listen: 0.0.0.0
  password: vlmpIPSyHH6f4S8WVPdRIHIlzmB+GIRfoH3aNJ/t9Gg=
  cipher: 2022-blake3-aes-256-gcm
  # simple-obfs:
  #   mode: http
  #   host: example.com
```

### tunnel（端口转发）

```yaml
- name: tunnel-in-1
  type: tunnel
  port: 10816
  listen: 0.0.0.0
  network: [tcp, udp]
  target: target.com
```

## 协议监听

### trojan

```yaml
- name: trojan-in-1
  type: trojan
  port: 10819
  listen: 0.0.0.0
  users:
    - username: 1
      password: 9d0cb9d0-964f-4ef6-897d-6c6b3ccf9e68
  certificate: ./server.crt
  private-key: ./server.key
  ws-path: "/"                  # 非空则开启 websocket
  grpc-service-name: "GunService"  # 非空则开启 grpc
  ss-option:                    # trojan-go 风格的 shadowsocks
    enabled: false
    method: aes-128-gcm         # aes-128-gcm/aes-256-gcm/chacha20-ietf-poly1305
    password: "example"
  allow-insecure: false         # 允许不开 TLS（仅 nginx/caddy 前置时用）
```

### vless

```yaml
- name: vless-in-1
  type: vless
  port: 10817
  listen: 0.0.0.0
  users:
    - username: 1
      uuid: 9d0cb9d0-964f-4ef6-897d-6c6b3ccf9e68
      flow: xtls-rprx-vision
  ws-path: "/"
  grpc-service-name: "GunService"
  xhttp-config:                 # xhttp 传输层
    path: "/"
    host: ""
    mode: auto                  # stream-one / stream-up / packet-up
    no-sse-header: false
    x-padding-bytes: "100-1000"
    x-padding-obfs-mode: false
    x-padding-key: x_padding
    x-padding-header: Referer
    x-padding-placement: queryInHeader  # queryInHeader/cookie/header/query
    x-padding-method: repeat-x          # repeat-x/tokenish
    uplink-http-method: POST            # POST/PUT/PATCH/DELETE
    session-placement: path             # path/query/cookie/header
    session-key: ""
    session-table: ""                   # ""/uuid/ALPHABET/Alphabet/BASE36/Base62/HEX/alphabet/base36/hex/number
    session-length: "16-32"             # 起始不可为0，id空间须>21亿
    seq-placement: path
    seq-key: ""
    uplink-data-placement: body         # body/cookie/header
    uplink-data-key: ""
    uplink-chunk-size: 0
    sc-max-buffered-posts: 30
    sc-stream-up-server-secs: "20-80"
    sc-max-each-post-bytes: 1000000
  decryption: "mlkem768x25519plus.native/xorpub/random.600s/0s.(padding).(X25519).(ML-KEM)..."
  allow-insecure: false
```

**vless decryption 说明**：
- 原生外观 / 只 XOR 公钥 / 全随机数
- `600s` 每次随机取 50%-100%（即 `300-600s`）
- `/` 只能选一个，后面 base64 至少一个，可无限串联
- 生成命令：`mihomo generate vless-x25519`、`mihomo generate vless-mlkem768`
- Padding 仅作用于 1-RTT，默认值 `"100-111-1111.75-0-111.50-0-3333"`
- 双端可设不同 padding，按 len/gap 顺序串联，第一个需概率 100% 且至少 35 字节

### anytls

```yaml
- name: anytls-in-1
  type: anytls
  port: 10818
  listen: 0.0.0.0
  users:
    username1: password1
    username2: password2
  certificate: ./server.crt
  private-key: ./server.key
  allow-insecure: false
  padding-scheme: ""            # https://github.com/anytls/anytls-go/blob/main/docs/protocol.md#cmdupdatepaddingscheme
```

### hysteria2

```yaml
- name: hysteria2-in-1
  type: hysteria2
  port: 10820
  listen: 0.0.0.0
  users:
    00000000-0000-0000-0000-000000000000: PASSWORD_0
    00000000-0000-0000-0000-000000000001: PASSWORD_1
  certificate: ./server.crt
  private-key: ./server.key
  up: "30 Mbps"         # 不写单位默认 Mbps
  down: "200 Mbps"
  obfs: salamander      # salamander / gecko
  obfs-password: yourpassword
  obfs-min-packet-size: 512    # 仅 Gecko
  obfs-max-packet-size: 1200   # 仅 Gecko
  bbr-profile: ""       # standard / conservative / aggressive
  max-idle-time: 15000
  alpn:
    - h3
  ignore-client-bandwidth: false
  masquerade: file:///var/www   # 认证失败时伪装（file/http/https）
  masquerade: http://127.0.0.1:8080
  realm-opts:
    enable: true
    server-url: https://realm.hy2.io
    token: public
    realm-id: my-cabin-1f3a8c2e9b
    stun-servers:
      - stun.nextcloud.com:3478
      - stun.sip.us:3478
      - global.stun.twilio.com:3478
    proxy: DIRECT         # server-url 走哪个代理
    skip-cert-verify: false
    name-cert-verify: example.com
```

**up/down 均不写或为 0 则使用 BBR 流控**。

### hysteria2-realm（realm 服务器）

```yaml
- name: hysteria2-realm-in-1
  type: hysteria2-realm
  port: 10820
  listen: 0.0.0.0
  token: public                         # Bearer 令牌
  max-realms: 65536                     # 最大 realm 数，0=无限
  max-realms-per-ip: 4                  # 每 IP 最大 realm 数
  trusted-proxy-header: ""              # 读取真实客户端 IP 的 header，如 X-Forwarded-For
  realm-name-pattern: "^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$"
  certificate: ./server.crt             # 配了走 HTTPS，不配走明文 HTTP
  private-key: ./server.key
  alpn: ["h2", "http/1.1"]
```

### trusttunnel

```yaml
- name: trusttunnel-in-1
  type: trusttunnel
  port: 10821
  listen: 0.0.0.0
  users:
    - username: 1
      password: 9d0cb9d0-964f-4ef6-897d-6c6b3ccf9e68
  certificate: ./server.crt
  private-key: ./server.key
  network: ["tcp", "udp"]      # http2+http3
  congestion-controller: bbr  # bbr / cubic / new_reno
  bbr-profile: ""              # standard / conservative / aggressive
```

### shadowquic

```yaml
- name: shadowquic-in-1
  type: shadowquic
  port: 10822
  listen: 0.0.0.0
  users:
    - username: username
      password: password
  jls-upstream:                  # JLS 上游（未认证连接转发到该 QUIC 伪装上游）
    addr: www.example.com:443
    sni: example.com
    proxy: proxy
    rate-limit: 0
  alpn:
    - h3
  quic-versions: [v1]            # v1/v2
  zero-rtt: true
  congestion-controller: bbr     # cubic / new_reno / bbr
  up: 100 Mbps
  down: 100 Mbps
  ignore-client-bandwidth: false
  cwnd: 10                       # 默认 32
  bbr-profile: ""                # standard / conservative / aggressive
  max-idle-time: 30000
  max-datagram-frame-size: 1400
  recv-window-conn: 0
  recv-window: 0
  disable-mtu-discovery: false
```

### mieru

```yaml
- name: mieru-in-1
  type: mieru
  port: 10818
  listen: 0.0.0.0
  transport: TCP                  # TCP / UDP
  users:
    username1: password1
    username2: password2
  traffic-pattern: ""             # base64 字符串，微调网络行为
  user-hint-is-mandatory: false   # 客户端不发送用户提示则拒绝
```

### sudoku

```yaml
- name: sudoku-in-1
  type: sudoku
  port: 8443                      # 仅支持单端口
  listen: 0.0.0.0
  key: "<server_key>"             # sudoku ED25519 公钥或任意 uuid
  aead-method: chacha20-poly1305  # chacha20-poly1305 / aes-128-gcm / none（不建议）
  padding-min: 1                  # 最小填充率 0-100
  padding-max: 15                 # 最大填充率，必须 >= padding-min
  table-type: prefer_ascii        # prefer_ascii / prefer_entropy / up_ascii_down_entropy / up_entropy_down_ascii
  custom-table: xpxvvpvv          # 自定义字节布局，需含2个x、2个p、4个v；仅对 entropy 方向生效
  custom-tables: ["xpxvvpvv", "vxpvxvvp"]  # 多表轮换，非空覆盖 custom-table
  handshake-timeout: 5            # 秒
  enable-pure-downlink: false     # false=带宽优化下行；true=纯 Sudoku 下行
  httpmask:
    disable: false
    mode: legacy                  # legacy / stream / poll / auto / ws
    path-root: ""                 # HTTP 隧道一级路径前缀
  fallback: "127.0.0.1:80"        # 可连接请求的回落转发
```

## 旧式入口（等价于 listener）

```yaml
# shadowsocks / vmess 入口
ss-config: ss://2022-blake3-aes-256-gcm:vlmpIPSyHH6f4S8WVPdRIHIlzmB+GIRfoH3aNJ/t9Gg=@:23456
vmess-config: vmess://1:9d0cb9d0-964f-4ef6-897d-6c6b3ccf9e68@:12345

# tuic 服务器入口
tuic-server:
  enable: true
  listen: 127.0.0.1:10443
  token: [TOKEN]                  # tuicV4
  users:                          # tuicV5
    00000000-0000-0000-0000-000000000000: PASSWORD_0
  certificate: ./server.crt
  private-key: ./server.key
  congestion-controller: bbr
  bbr-profile: ""
  max-idle-time: 15000
  authentication-timeout: 1000
  alpn:
    - h3
  max-udp-relay-packet-size: 1500
```

## tun 监听（高级用户）

仅供高级用户使用，普通用户用顶层 `tun`。

```yaml
- name: tun-in-1
  type: tun
  stack: system                   # gvisor / mixed / mips
  dns-hijack:
    - 0.0.0.0:53
  auto-detect-interface: false
  auto-route: false
  mtu: 9000
  inet4-address:                  # 必须手动设置
    - 198.19.0.1/30
  inet6-address:                  # 必须手动设置
    - "fdfe:dcba:9877::1/126"
  strict-route: true
  inet4-route-address:
    - 0.0.0.0/1
    - 128.0.0.0/1
  inet6-route-address:
    - "::/1"
    - "8000::/1"
```

## 监听类型速查表

| 类型 | 端口 | 说明 |
|---|---|---|
| `socks` | 支持 ports | SOCKS5 |
| `http` | 支持 ports | HTTP 代理 |
| `mixed` | 支持 ports | HTTP(S)+SOCKS 混合 |
| `redir` | 支持 ports | 透明代理 TCP |
| `tproxy` | 支持 ports | TProxy TCP+UDP |
| `shadowsocks` | 支持 ports | SS |
| `trojan` | 支持 ports | Trojan |
| `vless` | 支持 ports | VLESS |
| `anytls` | 支持 ports | AnyTLS |
| `hysteria2` | 支持 ports | Hysteria2 |
| `hysteria2-realm` | 支持 ports | Hysteria2 realm 服务 |
| `trusttunnel` | 支持 ports | TrustTunnel |
| `shadowquic` | 支持 ports | ShadowQUIC |
| `mieru` | 支持 ports | Mieru |
| `sudoku` | **仅单端口** | Sudoku |
| `tunnel` | 支持 ports | 端口转发 |
| `tun` | 无端口 | TUN 设备 |
