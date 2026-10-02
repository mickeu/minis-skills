---
name: Beatrice Surge 配置参考
description: BeatriceArchive 的 Surge 配置架构与防泄露设计参考。当用户提到 DNS 泄露修复、Surge 配置优化、fake-ip 防泄露、Beatrice 配置、VIF 接管模式时触发。包含两个仓库的完整源码。
source:
  - repo: https://github.com/BeatriceArchive/Beatrice-Surge-Config
    desc: Surge iOS 配置壳（General/Proxy Group/Rule 模板 + 校验器）
    cloned: 2026-08-29
  - repo: https://github.com/BeatriceArchive/Beatrice-Surge-Modules
    desc: Surge 模块与脚本（系统托管设置、基础面板、B站签到）
    cloned: 2026-08-29
license: Beatrice Personal Use License v1.0（个人使用允许，禁止再分发/改名/换皮）
---

# Beatrice Surge 配置参考

## 来源

- **Config 仓库**：https://github.com/BeatriceArchive/Beatrice-Surge-Config
- **Modules 仓库**：https://github.com/BeatriceArchive/Beatrice-Surge-Modules
- **扒取时间**：2026-08-29
- **本地路径**：`/var/minis/skills/beatrice-surge-config/repo/`

## 仓库一：Beatrice-Surge-Config

### 文件结构
```
Beatrice-Surge.conf       # 配置模板（无 [Proxy]，纯 General+Group+Rule）
scripts/validate-config.mjs  # 零依赖静态校验器
.github/workflows/validate.yml  # CI 自动校验
.editorconfig
README.md
```

### 核心 DNS 防泄露设计（3 道防线）

#### 防线1：DNS 上游不硬编码
```ini
dns-server = system
use-local-host-item-for-proxy = false
```
- `dns-server = system`：DNS 跟着网络走，不钉死在国内服务器
- `use-local-host-item-for-proxy = false`：代理连接不用本地 hosts/DNS，由代理端解析

#### 防线2：IP 规则全加 no-resolve
所有 IP-CIDR / GEOIP / RULE-SET(IP) 规则都带 `no-resolve`：
```ini
RULE-SET,https://ruleset.skk.moe/List/ip/ai.conf,🤖 AI服务,no-resolve
RULE-SET,https://ruleset.skk.moe/List/ip/china_ip.conf,DIRECT,no-resolve
GEOIP,CN,DIRECT,no-resolve
```
- 代理域名不在本地做 DNS 解析 → DNS 查询不经过国内运营商 → 不泄露

#### 防线3：FINAL 加 dns-failed
```ini
FINAL,🌐 兜底策略,dns-failed
```
- 兜底策略如果 DNS 解析失败就拒绝，不让 DNS 查询漏到本地

### 其他安全设置
```ini
compatibility-mode = 3        # 纯 VIF 虚拟网卡接管
ipv6 = false                   # 关闭 IPv6 防泄露
ipv6-vif = disabled
wifi-assist = false            # 关闭 WiFi 助手
all-hybrid = false             # 关闭混合网络
udp-priority = true
udp-policy-not-supported-behaviour = reject  # UDP 不支持时拒绝，防泄露
allow-wifi-access = false      # 关闭局域网代理共享
allow-hotspot-access = false
proxy-restricted-to-lan = true
include-all-networks = true    # 全网络 VIF 接管
include-local-networks = false
include-apns = false
include-cellular-services = false
icmp-forwarding = false        # 不转发 ICMP，防 ping 指纹
```

### 策略组架构
- 5 个核心组：🚀 手动切换 / 🤖 AI服务 / 🌍 国外流媒体 / 🍎 苹果服务 / 🌐 兜底策略
- 5 个隐藏地区组：🇭🇰港 / 🇯🇵日 / 🇸🇬新 / 🇺🇸美 / 🇹🇼台
- 地区组用 `fallback, REJECT` fail-closed，无匹配节点时拒绝而非直连
- 地区组用 `policy-regex-filter` + `evaluate-before-use` 自动匹配节点名
- 手动切换/AI/流媒体组**不含 DIRECT**（防意外直连）
- 苹果服务/兜底策略**保留 DIRECT**（允许直连）

### 规则顺序
1. LAN/System 直连
2. AI 服务（DeepSeek/Apple Intelligence/skk.moe ai 规则集）
3. Apple 服务
4. 国际流媒体（YouTube/Netflix/Disney+/Spotify/TikTok/Prime Video）
5. Bilibili（走手动切换，不走流媒体组）
6. 中国域名直连（.cn + skk.moe domestic）
7. IP 规则（AI IP / 中国 IP / GEOIP CN）全带 no-resolve
8. FINAL 兜底 + dns-failed

### 规则集来源
使用 Sukka 的规则集 `ruleset.skk.moe`（非 blackmatrix7）

### 校验器（validate-config.mjs）
零依赖 Node.js 脚本，检查：
- 公开模板只有 [General]/[Proxy Group]/[Rule] 三个段
- [Proxy] 不得进入公开仓库
- General 19 条基线完全冻结（逐行精确匹配）
- 5 核心 + 5 地区组，顺序固定
- 地区 regex 正向/反向边界测试
- 手动切换/AI/流媒体组不含 DIRECT
- 无 Smart 组、无 MATCH、只有一条 FINAL
- 外部 RULE-SET 必须 HTTPS
- 无代理凭据/节点声明

## 仓库二：Beatrice-Surge-Modules

### 模块列表
1. **Beatrice-Surge-System.sgmodule** — 系统托管设置覆盖（VIF/IPv6/UDP/安全），category 无
2. **Betty-Basic-Panel.sgmodule** — 基础面板（网络/出口IP/DNS/延迟/流媒体/AI可达性/流量/IP风险），category=🩺 网络工具
3. **Betty-Bilibili-Cookie.sgmodule** — B站 Cookie 获取（二维码登录，无 MITM）
4. **Betty-Bilibili-Daily.sgmodule** — B站每日签到（cron 08:00 + 面板手动，大会员+10经验，投币逐枚补足）

### 面板脚本特点
- Betty-Basic-Panel.js（63KB）：汇总网络信息面板，参数 YS=1&RISK=1
- Betty-Bilibili-Cookie.js（19KB）：官方二维码登录流程
- Betty-Bilibili-Daily.js（20KB）：每日任务（登录/观看/分享/投币/大会员经验）

## 与用户当前配置的差异（2026-08-29 DNS 泄露检测）

| 项目 | 用户当前 | Beatrice | 修复建议 |
|------|---------|----------|---------|
| DNS 上游 | 119.29.29.29 + 223.5.5.5 + 国内DoH | system | 改为 system 或加境外DoH |
| 代理本地解析 | 未设置 | use-local-host-item-for-proxy=false | 加上 |
| IPv6 | true | false | 关闭 |
| IP 规则 | 无 no-resolve | 全 no-resolve | 全加 |
| FINAL | 无 dns-failed | dns-failed | 加上 |
| compatibility-mode | 注释掉 | 3 | 开启 |
| icmp-forwarding | 未设置 | false | 加上 |

## 重新配置用户配置时的原则
1. 保留用户现有节点（[Proxy] 段不动）
2. 保留用户现有策略组结构（但可借鉴 fail-closed 设计）
3. 重点改 [General] 的 DNS 和网络行为设置
4. IP 规则全加 no-resolve
5. FINAL 加 dns-failed
6. IPv6 关闭
7. 保留用户现有规则集（blackmatrix7 或 skk.moe），不强制更换
