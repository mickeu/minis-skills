---
name: Shadowrocket 小火箭
description: Shadowrocket（小火箭）完整知识库。涵盖官方说明、配置格式、规则系统、节点管理、DNS、HTTPS解密、脚本模块、URL Scheme、故障排查等。当用户询问 Shadowrocket 配置、规则、使用教程、分流、代理分组、懒人配置、小火箭相关问题时触发。来源：LOWERTOP/Shadowrocket 使用手册（⭐4143）、dlisin/shadowrocket-config、Johnshall/Shadowrocket-ADBlock-Rules-Forever（⭐28445）、NodeMaven 指南、Hiddify 教程、Wikipedia 等。
source_url: https://github.com/LOWERTOP/Shadowrocket
source_repo: https://github.com/LOWERTOP/Shadowrocket
license: MIT
last_sync: 2026-09-26
---
# Shadowrocket（小火箭）完整知识库

> Shadowrocket 是 Shadow Launch Technology Limited 开发的 iOS 规则代理客户端，昵称"小火箭"。仅 iOS/iPadOS/Apple TV，**无官方 Android/Windows 版本**。
> App Store ID: `932747118` | 官方 Telegram：[@ShadowrocketApp](https://t.me/ShadowrocketApp) | [@ShadowrocketNews](https://t.me/ShadowrocketNews)

---

## 📋 目录

1. [软件概述](#1-软件概述)
2. [安装与购买](#2-安装与购买)
3. [快速上手](#3-快速上手)
4. [节点管理](#4-节点管理)
5. [配置与规则](#5-配置与规则)
6. [全局路由](#6-全局路由)
7. [DNS 配置](#7-dns-配置)
8. [代理分组](#8-代理分组)
9. [HTTPS 解密](#9-https-解密)
10. [脚本与模块](#10-脚本与模块)
11. [高级特性](#11-高级特性)
12. [URL Schemes](#12-url-schemes)
13. [故障排查](#13-故障排查)
14. [配置文件格式参考](#14-配置文件格式参考)
15. [规则集与社区资源](#15-规则集与社区资源)
16. [参考链接](#16-参考链接)
17. [更新历史](#17-更新历史)

---

## 1. 软件概述

Shadowrocket 是一款基于规则的代理客户端，通过本地 VPN 隧道捕获设备流量，根据配置文件规则进行分流。

### 核心能力
- 支持协议：**29种** — Shadowsocks、SSR、VMess、VLESS、Trojan、Hysteria、Hysteria2、TUIC、Juicity、AnyTLS、SOCKS5、SOCKS5 over TLS、HTTP、HTTPS、HTTP2、HTTP3、Relay、SSH、WireGuard、OpenConnect、TrustTunnel、MASQUE、Snell、Mieru、Brook、Lua、**Sudoku**（v2.2.92+） + **Tailscale**（全局隧道模组 v2.2.89+）
- 规则匹配：域名（精确/后缀/关键字）、CIDR IP 范围、GeoIP、IP-ASN、进程（App 分流）
- 功能：URL 重写、HTTPS 解密、脚本、模块、代理分组、多级转发
- 网络：IPv6、UDP 转发、DNS over HTTPS/TLS/QUIC、TUN 模式
- 数据：流量统计、延迟测试、iCloud 同步

### 连接原理
```
设备 → Shadowrocket（本地 VPN） → 配置文件路由判断 → 代理服务器 / 直连
```

---

## 2. 安装与购买

- **App Store**：仅非中国大陆区 Apple ID（美区/港区等）可搜索下载
- **价格**：$2.99 USD（美区）
- **支持设备**：iPhone / iPad / Apple TV / 兼容 Mac
- **系统要求**：iOS 13.0+

> ⚠️ 不要登录 iCloud，仅登录 App Store。`shadowrockets.app`、`shadowrocket.vip` 等非官方网站。

---

## 3. 快速上手

### 3.1 一键导入订阅
1. 服务商后台 → 一键导入到 Shadowrocket → 自动跳转
2. 或复制订阅链接 → 打开 Shadowrocket → 自动弹出"添加订阅"

### 3.2 手动添加订阅
1. 首页右上角 `+` → 类型改为 `Subscribe`
2. 粘贴 URL、备注名称 → 完成
3. 点击节点列表中的节点，选中后点击顶部开关连接

### 3.3 建议开头的设置
- **设置 → 服务器订阅** → 开启「打开时更新」「自动后台更新」（间隔 6-12 小时）
- **全局路由** → 选择 `Config`（配置模式）

---

## 4. 节点管理

### 4.1 添加节点
- **扫码添加**：首页右上角扫码图标
- **手动输入**：首页 `+` → 选择协议类型 → 填写地址/端口/密码
- **URL 导入**：复制 `ss://` / `vmess://` 等链接，打开 App 自动识别

### 4.2 协议类型（29种，含Sudoku/Tailscale）

官方手册完整列表（首页 → 右上角 `+` → 类型 可查看当前版本支持的协议）：

| 协议 | 说明 |
|------|------|
| **Shadowsocks** | ss:// 格式，支持 AEAD 加密、obfs http/tls |
| **ShadowsocksR** | SSR 协议 |
| **VMess** | V2Ray 核心，支持 TCP/WS/gRPC/XTLS |
| **VLESS** | Xray 轻量协议，支持 Reality、XTLS Vision、WebSocket、gRPC |
| **Trojan** | HTTPS 伪装协议 |
| **Hysteria** | 基于 QUIC 的协议（v1） |
| **Hysteria2** | 新一代 QUIC 协议，支持 obfs、端口跳跃 |
| **TUIC** | 基于 QUIC 的隧道协议 |
| **Juicity** | 基于 QUIC 的多路复用协议 |
| **AnyTLS** | TLS 隧道协议 |
| **SOCKS5** | 标准 SOCKS5 代理 |
| **SOCKS5 over TLS** | 加密 SOCKS5 隧道 |
| **HTTP / HTTPS** | 标准 HTTP 代理 |
| **HTTP2** | HTTP/2 代理 |
| **HTTP3** | HTTP/3 (QUIC) 代理 |
| **Relay** | 中继代理（代理链） |
| **SSH** | SSH 隧道转发 |
| **WireGuard** | L3 VPN 协议，支持自定义 DNS/MTU/Keepalive |
| **Tailscale** | 全局隧道模组（v2.2.89+），支持 auth key、exit node、DERP 中继、自定义控制服务器 |
| **OpenConnect** | Cisco AnyConnect SSL VPN |
| **TrustTunnel** | 信任隧道协议 |
| **MASQUE** | HTTP/3 隧道协议 |
| **Snell** | Surge 兼容的轻量代理协议（支持 v1-v5） |
| **Mieru** | 基于 UDP 的代理协议 |
| **Brook** | 简单 UDP/TCP 代理 |
| **Lua** | 脚本化自定义协议 |
| **Sudoku** | 新增代理协议（v2.2.92+），数据转发路径深度优化，减少内存分配与拷贝 |
| **Subscribe（订阅）** | 订阅链接，聚合管理多个节点 |

### 4.3 订阅更新
- **打开时更新**：每次打开 App 自动拉取
- **自动后台更新**：按设定间隔（6/12/24h）后台更新
- **手动更新**：节点列表下拉刷新

### 4.4 节点排序
- 节点列表右上角圆形按钮 → 批量延迟测试
- 按延迟排序 / 按名称排序 / 手动拖动排序
- 测速不反映实际下载速度，仅代表连通性

### 4.5 节点筛选与整理
- 订阅节点可通过关键词过滤
- 长按节点 → 分享 / 复制 / 删除
- 节点前方圆点为选中状态

---

## 5. 配置与规则

### 5.1 配置文件基础
配置文件决定了流量如何分流。内置 `default.conf` 满足基本需求，可导入第三方配置。

### 5.2 导入配置
1. 底部 **配置** 页 → 右上角 `+`
2. 输入 URL → 下载
3. 点击配置文件 → **使用配置** / **编译配置**

### 5.3 编辑配置
- **编辑纯文本**：直接用文本模式修改配置文件
- **编辑配置**：GUI 方式编辑各参数
- **编译配置**：拉取所有远程资源（规则集、脚本等）后编译生效
- **预览配置**：编译后预览最终规则列表
- **更新配置**：重新拉取远程资源

### 5.4 配置文件参数

#### [General] 通用参数
```ini
[General]
bypass-system = true                    # 绕过系统代理
bypass-tun = 10.0.0.0/8,172.16.0.0/12  # 绕过 TUN 的网段
dns-server = 8.8.8.8, 1.1.1.1          # DNS 服务器
ipv6 = true                             # 启用 IPv6
skip-proxy = 192.168.0.0/16, 10.0.0.0/8  # 不走代理的网段
tcp-connection = false                  # 全局 TCP 连接
```

#### [Rule] 规则
```ini
[Rule]
# 规则语法：DOMAIN-KEYWORD,域名关键字,策略
# 优先级从上到下
DOMAIN-SUFFIX,google.com,Proxy
DOMAIN-KEYWORD,adservice,Reject
IP-CIDR,10.0.0.0/8,DIRECT
GEOIP,CN,DIRECT
FINAL,Proxy
```

### 5.5 规则类型
| 类型 | 示例 | 说明 |
|------|------|------|
| DOMAIN | `DOMAIN,example.com` | 精确域名匹配 |
| DOMAIN-SUFFIX | `DOMAIN-SUFFIX,google.com` | 域名后缀匹配 |
| DOMAIN-KEYWORD | `DOMAIN-KEYWORD,google` | 域名关键字匹配 |
| IP-CIDR | `IP-CIDR,10.0.0.0/8` | IP 段匹配（直连前解析） |
| IP-CIDR6 | `IP-CIDR6,::1/128` | IPv6 段匹配 |
| GEOIP | `GEOIP,CN` | GeoIP 国家匹配 |
| DST-PORT | `DST-PORT,80` | 目标端口匹配 |
| SRC-PORT | `SRC-PORT,8080` | 源端口匹配 |
| PROCESS | `PROCESS,WeChat` | 进程名匹配（仅限 iOS） |
| AND | `AND,((DOMAIN,google.com),(DST-PORT,443))` | 多条件与逻辑 |
| OR | `OR,((DOMAIN,google.com),(DOMAIN,youtube.com))` | 多条件或逻辑 |
| NOT | `NOT,((DOMAIN,google.com))` | 条件取反 |

### 5.6 规则策略
| 策略 | 说明 |
|------|------|
| Proxy | 通过代理服务器转发 |
| DIRECT | 直连 |
| Reject | 拒绝连接（拦截广告跟踪器） |
| 代理分组名 | 转发到指定代理分组 |

### 5.7 规则优先级
规则从上至下依次匹配，命中即停。推荐顺序：
1. 广告拦截（Reject）
2. 局域网/内网（DIRECT）
3. 国内域名（DIRECT）
4. 国外域名（Proxy）
5. FINAL 兜底规则

### 5.8 APP分流
Shadowrocket 支持按 App 进程名称分流。在规则中使用 `PROCESS,AppName`。注意 App 需要接入系统 Network Extension 框架才能被识别。

---

## 6. 全局路由

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **Proxy**（代理） | 所有流量走代理 | 测试节点是否可用 |
| **Direct**（直连） | 所有流量直连 | 关闭代理 |
| **Config**（配置） | 按配置文件规则分流 | ⭐ 日常推荐 |
| **Scene**（场景） | 按 WiFi/蜂窝自动切换不同配置 | 多个网络环境 |

### 场景模式
底部「场景」功能可根据连接的 Wi-Fi SSID 或蜂窝网络自动切换配置文件和全局路由模式。
- 添加场景 → 选择触发条件（SSID/蜂窝）
- 绑定对应的配置文件和全局路由
- 连接指定 WiFi 时自动切换

---

## 7. DNS 配置

### 7.1 DNS 模式
- **系统默认 DNS**：使用系统 DNS
- **自定义 DNS**：在设置中配置
- **DNS over HTTPS**：`https://dns.alidns.com/dns-query`
- **DNS over TLS**：`tls://dns.alidns.com`
- **DNS over QUIC**：`quic://dns.alidns.com`

### 7.2 DNS-over-PROXY
DNS 查询走代理通道，避免 DNS 污染。在配置文件中：
```ini
dns-server = https://doh.pub/dns-query
```

### 7.3 DNS 新特性（v2.2.92+）
- **直连域名专属 DNS 路由**：支持为直连流量配置独立的 DNS 路由
- **DNS over TCP**：支持通过 TCP 传输 DNS 查询
- **DNSCrypt 上游**：新增 DNSCrypt 协议作为 DNS 上游服务器
- **CNAME 与 Host 规则多服务器**：在 CNAME 重写和 Host 规则中支持配置多个 DNS 服务器
- **隧道解析优化**：支持通过 DNS 隧道解析 QUIC 端点，HTTP/3 升级时复用 HTTP/2 地址

### 7.4 no-resolve 的作用
在 IP 规则前添加 `no-resolve` 参数，避免不必要的 DNS 解析：
```ini
IP-CIDR,0.0.0.0/8,DIRECT,no-resolve
```

---

## 8. 代理分组

### 8.1 分组类型
| 类型 | 说明 |
|------|------|
| select | 手动选择，可从分组中手动选一个策略 |
| url-test | 自动测速，按周期和结果自动切换延迟最低的节点 |
| fallback | 故障转移，节点不可用时自动切换到其他可用节点 |
| load-balance | 负载均衡，不同规则的请求使用不同节点，相同域名固定同一节点 |
| random | 随机分配，每次请求随机使用节点，相同域名可能不同节点 |
| ssid | 按 WiFi SSID 切换节点 |

### 8.2 分组参数（v2.2.92+）
- **独立 Ping 延迟自动排序**：策略组支持独立的 Ping 延迟自动排序选项，可按 Ping 延迟自动排列节点顺序

### 8.3 示例
```ruby
香港节点 = select,HK-01,HK-02,HK-03,policy-select-name=HK-01
自动选择 = url-test,HK-01,HK-02,HK-03,url=http://www.gstatic.com/generate_204,interval=600,tolerance=100,timeout=5
自动回退 = fallback,HK-01,HK-02,HK-03,url=http://www.gstatic.com/generate_204,interval=600
```

---

## 9. HTTPS 解密

HTTPS 解密用于抓包调试或审查流量。

### 9.1 开启步骤
1. 配置 → HTTPS 解密 → 开启
2. 生成 CA 证书 → 安装描述文件
3. 设置 → 通用 → 关于本机 → 证书信任设置 → 信任该证书

### 9.2 排除域名
在 `HTTPS_DECRYPTION` 段配置不解密的域名：
```ini
[HttpsDecryption]
host-name = *.apple.com
host-name = *.icloud.com
```

> ⚠️ HTTPS 解密涉及隐私安全，仅建议调试时使用。

---

## 10. 脚本与模块

### 10.1 脚本
Shadowrocket 支持 JavaScript 脚本对 HTTP 请求进行修改。
- 脚本类型：request（请求）、response（响应）、cron（定时）
- 脚本操作：修改请求头、响应体、URL 重写等

### 10.2 模块
模块是配置文件的扩展包，可以添加额外功能。
- 模块格式：`.module` / `.sgmodule`
- 导入：配置 → 模块 → 右上角 `+` → 填写 URL → 下载
- 模块内容：可包含规则、脚本、重写、MitM 等

### 10.3 查看远程资源
- 配置页面显示远程规则集/脚本的下载状态
- ✅ 下载成功 / ❎ 下载失败
- 点击重新拉取（需重新编译才生效）

---

## 11. 高级特性

### 11.1 TUN 模式
控制进出设备的全部流量，包括非 HTTP 应用。
- 配置 → 隧道 → 开启
- 兼容模式：解决某些应用的网络连接问题
- 启用条件：设备支持 Network Extension

### 11.2 前置代理
多级转发代理链：
```
应用 → 前置代理 → 主代理 → 目标服务器
```
适用于需要通过跳板机访问的场景。

### 11.3 代理共享
开启后将设备上的代理提供给局域网其他设备使用。
- 配置 → 代理共享 → 开启
- 同一局域网下其他设备设置代理为本机 IP:端口

### 11.4 UDP 转发
- 设置 → 开启 UDP 转发
- 适用于游戏、通话等 UDP 应用

### 11.5 禁用 STUN
开启后防止 WebRTC 等应用泄露真实 IP。

### 11.6 Tailscale 支持（v2.2.89+）
Shadowrocket 自 v2.2.89 (3314) 起内置 Tailscale 全局隧道模组。

- **启用位置**：配置 → Tailscale，开启全局隧道
- **规则策略**：`TAILSCALE` — 通过 Tailscale 隧道转发流量
  - 示例：`DOMAIN-WILDCARD,tail*.ts.net,TAILSCALE`
  - 示例：`DOMAIN-SUFFIX,ts.net,TAILSCALE`
- **认证密钥**：支持可复用/临时 auth key，免登录加入 tailnet
- **控制服务器**：支持自定义控制服务器 URL（默认 `https://controlplane.tailscale.com`）
- **出口节点**：可选启用 exit node，将所有互联网流量通过 Tailscale 设备转发
- **DERP 中继**：支持强制通过 DERP 中继转发，禁用 UDP 直连通道
- **注意**：TUN 旁路路由 `tun-excluded-routes` 若包含 `100.64.0.0/10` 可能影响 Tailscale 连通性

#### v2.2.92 升级
- **TS2021 登录流程**：登录机制升级至 Tailscale TS2021
- **子网网段路由**：支持子网网段路由（subnet routing）
- **自动出口节点**：支持自动出口节点（auto exit node）
- **低功耗按需暂停隧道**：引入低功耗模式，按需暂停隧道以省电
- **DERP 自定义 TLS**：遵循自定义 DERP TLS 验证设置
- **Disco 密钥宣告**：宣告 disco 密钥以优化直连
- **耗电修复**：解决 VPN 断开后仍然刷新设备的耗电问题

### 11.7 GEOIP 数据库
- 内置 GeoIP 数据库用于国家/地区路由
- 可配置 MaxMind 账号密钥在线更新
- 支持自定义 `.mmdb` 数据库

### 11.8 自动切换节点
基于 URL 连通性检测自动切换到可用节点。

### 11.9 温和策略机制
当节点的连通性测试结果不佳时，自动降低其排序或暂停使用。

### 11.10 iCloud 自动同步
配置文件和节点数据跨设备同步。
> 注意：场景和分组不属于 iCloud 同步范围，需手动备份。

---

## 12. URL Schemes

Shadowrocket 支持的 URL Scheme，可用于快捷指令或外部调用：

| Scheme | 说明 |
|--------|------|
| `shadowrocket://` | 打开 App |
| `shadowrocket://connect` | 快速连接 |
| `shadowrocket://disconnect` | 断开连接 |
| `shadowrocket://import/{URL}` | 导入订阅/节点 |
| `shadowrocket://install/{URL}` | 安装配置 |
| `shadowrocket://open/{URL}` | 打开链接 |
| `shadowrocket://config` | 打开配置页 |
| `shadowrocket://log` | 打开日志页 |
| `shadowrocket://setting` | 打开设置页 |
| `shadowrocket://http-proxy` | 设置 HTTP 代理 |
| `shadowrocket://global-routing/{proxy,direct,config,scene}` | 切换路由模式 |

---

## 13. 故障排查

### 13.1 连接成功但无法访问
1. 检查 DNS 设置（尝试更换 DNS）
2. 检查全局路由模式（建议 Config）
3. 检查 IPv6 开关
4. 切换其他节点测试
5. 检查是否有规则冲突

### 13.2 一键测速全部失败
1. 确认本机网络正常
2. 检查测速 URL 是否可用
3. 更新远程节点列表

### 13.3 微信转圈/图片打不开
- 微信使用自有协议，部分节点无法代理
- 尝试开启 TUN 模式
- 或使用兼容模式

### 13.4 模块消失/失效
- 模块文件存储在 iCloud 云盘 `Shadowrocket/Modules/`
- 如果 iCloud 本地缓存被清理，模块文件显示为未下载状态
- 等待自动下载或在 iCloud 中手动触发下载
- 有些模块需安装相关描述文件才能生效

### 13.5 VPN 自动断开
- 检查是否开启了「低数据模式」
- 检查系统 VPN 权限是否被撤销
- 某些 iOS 版本可能有限制
- 「按需求连接」配置不当也可能导致断开

### 13.6 检测代理
某些网站（如 Netflix、OpenAI）会检测代理 IP。
- 尝试切换节点（不同 IP）
- 使用住宅 IP 而非机房 IP
- 关闭 UDP 转发

### 13.7 编译原因
当提示需要编译配置时，说明有远程资源未下载完成。
- 编译会自动拉取所有远程规则集和脚本
- 打断编译会导致配置处于中间状态

### 13.8 订阅异常
- **节点旗帜错误**：GeoIP 数据库过旧，更新 GEOIP
- **节点感叹号**：节点连接异常，检查节点信息是否过期
- **节点用不了**：检查订阅链接是否已过期或变更

---

## 14. 配置文件格式参考

Shadowrocket 配置格式兼容 Surge，采用 `ini` 风格。

### 14.1 完整结构
```ini
#!MANAGED-CONFIG https://example.com/config.conf  # 远程托管配置

[General]
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 17.0.0.0/8
bypass-tun = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.168.0.0/16, 198.18.0.0/15, 224.0.0.0/4
dns-server = 8.8.8.8, 1.1.1.1, 223.5.5.5
ipv6 = true

[Proxy]
# 节点定义
🇭🇰HK-01 = ss, example.com, 443, encrypt-method=chacha20-ietf-poly1305, password=xxx
🇯🇵JP-01 = ss, example.jp, 8443, encrypt-method=aes-256-gcm, password=yyy

[Proxy Group]
Auto = url-test, 🇭🇰HK-01, 🇯🇵JP-01, url=http://www.gstatic.com/generate_204, interval=600, timeout=5
Proxy = select, 🇭🇰HK-01, 🇯🇵JP-01, Auto

[Rule]
# 广告拦截
RULE-SET,https://example.com/reject.list,Reject
# 国内直连
RULE-SET,https://example.com/direct.list,DIRECT
# 代理
RULE-SET,https://example.com/proxy.list,Proxy
# 兜底
FINAL,Proxy,dns-fail=true

[URL Rewrite]
^https?://(www.)?example.com http://new-example.com 302

[MITM]
hostname = *.example.com, *.test.com
ca-passphrase = xxx
ca-p12 = MIIK...
```

### 14.2 隐式参数
- `dns-fail=true`：当 DNS 解析失败时匹配该规则
- `no-resolve`：跳过 DNS 解析
- `force-remote-dns`：强制使用远程 DNS

### 14.3 配置指令
- `#!MANAGED-CONFIG`：远程托管配置
- `#!INCLUDE`：导入其他配置文件

---

## 15. 规则集与社区资源

### 15.1 内置配置
- `default.conf`：官方内置默认配置

### 15.2 社区热门规则集

| 名称 | ⭐ | 说明 | 地址 |
|------|---|------|------|
| Johnshall | 28K+ | 多类型规则，含去广告版、回国版 | [GitHub](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) |
| blackmatrix7 | 30K+ | iOS 规则脚本集 | [GitHub](https://github.com/blackmatrix7/ios_rule_script) |
| Lazy Config | - | LOWERTOP 懒人配置（含策略组） | `https://lowertop.github.io/Shadowrocket/lazy_group.conf` |
| itdog | - | 允许域名列表 | [GitHub](https://github.com/itdoginfo/allow-domains) |

### 15.3 Johnshall 规则类型
- `lazy.conf` / `lazy_group.conf`：懒人配置（带策略组）
- `sr_ad_only.conf`：仅广告过滤
- `sr_backcn.conf`：回国专用
- `sr_cnip.conf`：仅国内 IP 直连
- `sr_direct_banad.conf`：直连 + 去广告
- `sr_proxy_banad.conf`：代理 + 去广告
- `sr_top500_*`：Top 500 网站优化规则

---

## 16. 参考链接

### 官方
- App Store：`https://apps.apple.com/us/app/shadowrocket/id932747118`
- Telegram 群组：[@ShadowrocketApp](https://t.me/ShadowrocketApp)
- Telegram 频道：[@ShadowrocketNews](https://t.me/ShadowrocketNews)（更新日志发布渠道）

### 频道消息缓存
- TGStat 频道页：[tgstat.com/channel/@ShadowrocketNews](https://tgstat.com/channel/@ShadowrocketNews)（最近 ~240 条消息可读，更早的消息不缓存）
- 单条消息页：`https://tgstat.com/channel/@ShadowrocketNews/<消息ID>`（每条消息独立可访问）

### 社区手册
- LOWERTOP 使用手册（⭐4143）：[GitHub](https://github.com/LOWERTOP/Shadowrocket)
- 手册 HTML版：<https://lowertop.github.io/Shadowrocket/>

### 规则集
- Johnshall（⭐28K+）：[GitHub](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever)
- blackmatrix7（⭐30K+）：[GitHub](https://github.com/blackmatrix7/ios_rule_script)
- dlisin 配置：[GitHub](https://github.com/dlisin/shadowrocket-config)
- Lazy Config：`https://lowertop.github.io/Shadowrocket/lazy_group.conf`

### 配置格式参考
- Surge 手册（兼容）：<https://manual.nssurge.com>
- dlisin shadowrocket.conf：`https://raw.githubusercontent.com/dlisin/shadowrocket-config/master/shadowrocket.conf`

### 翻译版
- [Google Translate 英文版手册](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=https://github.com/LOWERTOP/Shadowrocket/wiki)

---

## 17. 更新历史

> 📁 完整更新日志（241 条消息，覆盖 2026-03-28 至 2026-09-07，从 tgstat.com 抓取）：`docs/changelog.txt`
> 数据来源：[@ShadowrocketNews](https://t.me/ShadowrocketNews) Telegram 官方频道，通过 [tgstat.com](https://tgstat.com/channel/@ShadowrocketNews) 缓存页面获取。

### v2.2.92

#### 新增特性
- **Sudoku 代理协议**：新增支持，数据转发路径深度优化以减少内存分配与拷贝
- **DNS 增强**：直连域名专属 DNS 路由、DNS over TCP、新增 DNSCrypt 上游支持、CNAME 与 Host 规则支持多服务器配置
- **Tailscale 升级**：登录升级至 TS2021 流程，支持子网网段路由与自动出口节点，引入低功耗按需暂停隧道功能
- **Clash 订阅导入**：支持在 Clash 订阅中导入 SSH 代理与 packetaddr 配置
- **macOS 菜单栏**：为 macOS 版添加菜单栏路由切换与服务器快捷控制面板
- **策略组 Ping 排序**：策略组支持独立的 Ping 延迟自动排序选项

#### 优化
- **Transport**：支持 KCP 背压控制，增强 WireGuard 混淆安全性，增强 Hysteria 数据包保护，恢复 QUIC 上传吞吐性能

#### 修复
- **VPN**：修复启动挂起问题并保持本地网络互联（AirDrop 等），防止过期连通性测试意外重置 VPN 状态
- **DNS**：优化隧道解析逻辑，支持通过 DNS 隧道解析 QUIC 端点，HTTP/3 升级时复用 HTTP/2 地址
- **Tailscale**：宣告 disco 密钥优化直连，遵循自定义 DERP TLS 验证设置，解决 VPN 断开后仍刷新设备的耗电问题
- **Rule**：修复远程规则刷新与配置导出时带引号重写参数被丢弃问题，保护已编译策略组排序与状态更新
- **System**：脚本环境支持 WebKit 作用域全局变量与 fetch 代理扩展；采用墓碑（Tombstone）清单的 iCloud 同步机制避免配置回滚；解决 WKWebView 与 JavaScriptCore 退出时的释放崩溃；限制代理流缓冲区大小防止内存暴涨

---

> 📁 本知识库附带完整文档存储：`/var/minis/skills/shadowrocket/` 下的文档子目录包含各来源原始资料。
> 配置文件示例位于 `configs/` 子目录。