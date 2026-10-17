# Surge iOS 5.102.0 (3871)：Tailscale / WireGuard 入站

收录日期：2026-10-14。状态：TestFlight 公告确认功能；本文未进行双机真机验收。

## 官方公告确认

入站连接与普通请求一样经过 Surge 规则和策略，并显示在请求列表。

### Tailscale
- `accept-incoming = true`：其他 tailnet 设备可以通过本机 tailnet 地址访问本机，包括 Surge HTTP/SOCKS5 代理和本机其他服务。
- `advertise-exit-node = true`：宣告本机为出口节点；选择它的其他设备通过本机 Surge 规则访问互联网。
- `advertise-routes = 192.168.1.0/24, ...`：宣告指定子网路由。
- 出口节点和子网路由需要在 Tailscale 管理后台批准。
- Surge 不会对这些 Tailscale 入站连接应用 Tailscale 访问控制策略；应使用 Surge 的 `SRC-IP` 等规则限制来源及目的地。

### WireGuard
- `accept-incoming = true`：允许对端通过已有隧道发起到本机的连接。
- `listen-port = 51820`：Surge 可以作为 WireGuard 服务端监听客户端连接。
- Peer 可以省略 `endpoint`；Surge 在客户端连接时学习地址，并跟随地址变化更新。
- 客户端可以把 Surge 的隧道地址作为 DNS 服务器，由 Surge 回答查询。

## 使用场景与边界

### 远端手机借用 Surge 出网
A 手机运行新版 Surge 内置 Tailscale，开启入站；B 设备加入可互通的 tailnet。
- 显式代理：B 的支持代理的应用连接 A 的 tailnet 地址及 HTTP/SOCKS5 端口；必须另行配置监听、端口、认证，不能假定默认端口已对远端开放。
- 系统流量：A 宣告出口节点并获后台批准，B 在 Tailscale 中选择 A 作为出口。实际转发受 A 的 Surge 规则、节点能力及可用网络影响。
- 两端使用 Surge 时，B 使用内置 Tailscale policy；流量必须匹配到该策略，不能仅写一个节点就假定全部流量经过它。

### 远程控制另一台手机的 Surge
远程控制是既有 External Controller / HTTP API 能力；3871 提供新的 Tailscale 入站可达通道，不是手机系统远控。
- 被控 A 需开启控制接口、设置认证并配置可达监听。
- 控制 B 需通过 Tailscale 路由访问 A 的 tailnet 地址及控制端口，可使用 Surge iOS 远程控制器等客户端。
- 公告未单独给出控制器经此通道的完整例子；实际监听映射、规则及双机连接需真机验证，不宣称已经跑通。
- 可以管理 Surge（策略、请求、配置等），不等于操作手机屏幕或控制其他 App。

### 网络条件
- Tailscale：通常无需自有公网 IP、端口映射或同一局域网；两端仍需互联网及可用的控制/中继服务。优先直连，不能直连时可使用 DERP，中继会影响速度和延迟。
- 原生 WireGuard：没有自动的 Tailscale 打洞/DERP 能力；服务端必须具有客户端可达的 endpoint，或已有可用隧道。不能将“不需要公网、不同局域网也能连接”无条件套用到 WireGuard。
- iOS：独立 Tailscale App 与 Surge 的系统 VPN 接管通常不能同时运行。B 可以只运行 Tailscale 使用 A 的出口，或只运行 Surge 内置 Tailscale；不要推荐独立 Tailscale VPN 与 Surge VPN 同时接管。
- 本次未验证锁屏、系统暂停、切网后的持续服务能力；不把手机视为保证全天在线的服务器。

## 访问控制纠错

`SRC-IP,100.64.0.0/10,PROXY` 只是让该来源范围匹配某出站策略，并非白名单：未匹配的其他来源仍会继续匹配后续规则；也不能区分 tailnet 内哪些设备获准访问哪些服务。

应根据实际 tailnet 地址、目标与端口设计明确允许和拒绝规则，并审查顺序，避免影响本机流量。不要直接复制一条宽泛的 SRC-IP 策略规则当成安全限制。控制器必须另设强认证；`0.0.0.0` 是全 IPv4 接口监听，可能同时向局域网开放，不是仅 Tailscale 专用监听。

## 实战排查记录（2026-10-17 双机真机验收通过）

**场景**：另一台 iPhone（B）通过 Tailscale 借用本机 Surge（5.102.0 3871）作为 exit node 出网，走 Surge 自动分流。

**本机 Surge 配置**：
```
[Proxy]
我的Tailnet = tailscale, section-name=ts-net
[Tailscale ts-net]
interactive-login = true
hostname = surge-iphone
accept-incoming = true
advertise-exit-node = true
dns-server = 223.5.5.5, 119.29.29.29
```
- Surge App 的 Tailscale 策略编辑器用 Apple ID 交互登录（与 B 同一 Apple ID → 自动同 tailnet）。
- 管理后台 `console.tailscale.com/admin/machines` → surge-iphone → Edit route settings → 勾选 "Use as exit node" → Save。注意：带感叹号的 "Exit Node" 标签 = 待批准，必须手动批准。

**关键坑（DNS 解析失败）**：
- 现象：B 设出口节点后 Safari 所有网页"找不到服务器"，但 QQ 等 IP 直连能通 → 判断为 DNS 问题。
- 根因：B 开启 Tailscale DNS（DNS 发到 100.100.100.100），Surge 作为 exit node **不监听 100.100.100.100**，DNS 查询无人应答。
- 解决：**在 B 手机 Tailscale App → Settings → DNS Settings 关闭 "Use Tailscale DNS Settings"** 即可。关闭后 B 的 DNS 走普通流量经 Surge 转发，解析成功。
- Surge 侧 `dns-server` 对 B 的 Tailscale DNS 虚拟地址无效；真正解决靠关闭 B 的 Tailscale DNS。
- "Detect MagicDNS hostnames" 开关灰色打不开：只有 Wi-Fi/Cellular 的 VPN On Demand 设为 "Do Nothing" 才可开，Always 模式下不可用，不影响。
- 主配置被 iCloud 托管为只读，App 无法编辑 [Proxy]（提示"分离段配置只读"），改文件 + reload 生效。

## 参考资料（来源）

- 原文：用户于 2026-10-14 提供的 Surge 5.102.0 (3871) TestFlight 英文公告，标题 Incoming Connections for Tailscale and WireGuard。
- 官方频道：https://t.me/SurgeTestFlightFeed （用户提供频道名；未提供具体消息 URL）。
- 官方手册：https://manual.nssurge.com/ （公告指引 Tailscale / WireGuard 页面；本次未独立同步最新版页面）。
- 官方远程管理指南：https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/remote-management.md
- 官方入口：https://nssurge.com/
- 版本校验：公告明确 5.102.0 (3871)；发布日期未独立核验，2026-10-14 为收录日期。
