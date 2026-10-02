# Mihomo-Script-Rules 知识库

> 来源：https://github.com/zzzhhe999/Mihomo-Script-Rules
> 作者：zzzhhe999 · 16 star · 创建 2026-07-14 · 最后更新 2026-09-08
> 用途：Mihomo (Clash Meta) 订阅预处理脚本 + 自托管二进制规则集，面向 Bettbox 深度优化
> ⚠️ 维护状态：作者已宣布**暂停维护**（学业压力），推荐改用 [MyClash](https://github.com/AIsouler/MyClash)

## 1. 项目概述

为 **Bettbox（Mihomo 内核 / QuickJS 引擎）** 深度优化的 JavaScript 订阅预处理脚本（`Mihomo-Script-Rules.js`），同时自托管两个二进制规则集（`anti-ad.mrs` 广告拦截、`fakeip-filter.mrs` Fake-IP 过滤）。脚本接管机场原始订阅，自动执行节点重命名、无效节点过滤、精细化策略组分流、智能 DNS 配置。

**纯 JS 单文件方案**（无静态 YAML 配置）：所有分流规则集以 **.mrs 二进制**形式经 jsdelivr CDN 下发，客户端每 12h 自动拉取更新。

## 2. 脚本与规则集链接

**脚本主链接：**
```
https://raw.githubusercontent.com/zzzhhe999/Mihomo-Script-Rules/refs/heads/main/Mihomo-Script-Rules.js
```
**脚本 CDN 镜像：**
```
https://fastly.jsdelivr.net/gh/zzzhhe999/Mihomo-Script-Rules@main/Mihomo-Script-Rules.js
```
**广告拦截规则集（anti-ad.mrs）：**
```
https://raw.githubusercontent.com/zzzhhe999/Mihomo-Script-Rules/refs/heads/main/anti-ad.mrs
```
**Fake-IP 过滤规则集（fakeip-filter.mrs）：**
```
https://raw.githubusercontent.com/zzzhhe999/Mihomo-Script-Rules/refs/heads/main/fakeip-filter.mrs
```
> CDN 镜像同理：`https://fastly.jsdelivr.net/gh/zzzhhe999/Mihomo-Script-Rules@main/anti-ad.mrs` 等。

### 2.1 快速上手（Bettbox）
1. APP → 底部 **更多** → **脚本** 功能入口 → 右下角 **+** → **通过 URL 导入**
2. 粘贴脚本链接（建议 CDN 镜像）→ 命名 → 保存
3. 在 **脚本** 功能页打开该脚本的 **开关**
4. 回到 **代理** 页选择该脚本生成的配置，即可选择节点及策略组

## 3. 支持的服务/应用（17 个独立策略组）

| 服务 | 策略组 | 规则来源 | 特殊处理 |
|---|---|---|---|
| AI 服务 | `AI` | `rule-set:ai` | ChatGPT、Claude 等 |
| YouTube | `YouTube` | `rule-set:youtube` | — |
| FCM 推送 | `FCM` | `rule-set:googlefcm` | Android 推送 |
| Google | `Google` | `rule-set:google` + `rule-set:google_ip` | 域名+IP 双匹配 |
| GitHub | `GitHub` | `rule-set:github` | — |
| Microsoft | `Microsoft` | `rule-set:microsoft` | — |
| Apple | `Apple` | `rule-set:apple` | — |
| Telegram | `Telegram` | `rule-set:telegram` + `rule-set:telegram_ip` | 域名+IP 双匹配 |
| Cloudflare | `Cloudflare` | `rule-set:cloudflare` + `rule-set:cloudflare_ip` | 域名+IP 双匹配 |
| Steam | `Steam` | `rule-set:steam` + `rule-set:steam_asn` | 域名+ASN 双匹配 |
| X | `X` | `rule-set:twitter` + `rule-set:twitter_ip` | 域名+IP 双匹配 |
| Instagram | `Instagram` | `rule-set:instagram` | — |
| Spotify | `Spotify` | `rule-set:spotify` | — |
| TikTok | `TikTok` | `rule-set:tiktok` | — |
| Netflix | `Netflix` | `rule-set:netflix` + `rule-set:netflix_ip` | 域名+IP 双匹配 |
| Emby | `Emby` | `rule-set:emby` + `DOMAIN-SUFFIX,mb3admin.com` + `DOMAIN-KEYWORD,emby` | 多重匹配 |
| 广告拦截 | `AdBlock` | `rule-set:antiad` | 仅 REJECT / DIRECT |

> 服务策略组默认提供 `Default`（跟随默认出口）、`Direct`、`Auto`、`Balance` 及地区组选项；`AdBlock` 仅提供 `REJECT`（拦截）与 `DIRECT`（放行）。
> 规则集均以 **RULE-SET（.mrs）** 形式下发，主数据源 [appshubcc/bett-rules](https://github.com/appshubcc/bett-rules)（经 jsdelivr CDN，含 path-in-bundle）

## 4. 支持的国家/地区（16 个 + Others 兜底 + 2 个倍率组）

🇭🇰 HK · 🇯🇵 JP · 🇺🇸 US · 🇸🇬 SG · 🇹🇼 TW · 🇰🇷 KR · 🇬🇧 UK · 🇩🇪 DE · 🇫🇷 FR · 🇨🇦 CA · 🇦🇺 AU · 🇮🇳 IN · 🇹🇷 TR · 🇧🇷 BR · 🇦🇷 AR · 🇷🇺 RU

另有两个倍率分组：`Low-Rate`（节点名含 低倍/省流/0.0x~0.5x 等标记）、`High-Rate`（含 2倍/3倍率/2x/×2 等标记）。
每个地区（含倍率组）自动生成三层策略组：**手动选择节点 → Auto（自动测速） → Balance（负载均衡）**

## 5. 核心特性

### 5.1 节点智能归类与统一命名
- 根据节点名关键词（中文、英文、国旗 Emoji）自动识别国家/地区
- 自动剥离机场广告、联系方式、流量信息（50+ 条过滤正则）
- 倍率自动识别：低倍率（0.0x~0.5x）、高倍率（2x+）
- 统一格式：普通 `🇭🇰 HK 01`、低倍率 `🇯🇵 JP 02 0.5x`、高倍率 `🇺🇸 US 03 2x`
- 无法识别地区的节点保留原名追加序号（如 `示例节点 #01`），归入 `Others`

### 5.2 低质节点过滤
内置 `excludeFilter` 正则，过滤包含以下关键词的节点：
`群|返利|循环|官[网址]|客服|网站|网址|获取|订阅|流量|到期|机场|下次|备用|过期|已用|联系|邮箱|工单|通知|防止|国内|地址|频道|无法|说明|使用|提示|特别|访问|教程|关注|更新|作者|加入|超时|收藏|福利|邀请|好友|选择|剩余|公益|发布|通路|登录|禁止|定时|渠道|牢记|永久|余额|阁下|本站|刷新|导航|⚠️|@|Expire|https?:\/\/|www\.|\.com(?:$|[^a-zA-Z0-9])`

### 5.3 策略组分流
- 每个地区 3 层：手动选择 → Auto（测速间隔 180s，容忍度 50ms，3 次失败切换）→ Balance（sticky-sessions 同域名固定节点）
- 功能组：`Default`（默认出口，含全部组选项）、`Auto`、`Balance`、`QUIC`、`Direct`（含 5 个内置直连节点）
- GLOBAL 组包含所有功能组和地区组

### 5.4 DNS 防污染
```
国内域名 → 阿里 DNS / DNSPod (DoH) → 直连
国外域名 → Google DNS / Cloudflare (DoH) → 代理
```
- **Fake-IP 模式**（ARC 缓存），`fake-ip-filter` 由 `rule-set:private`、`rule-set:fakeip_filter`、`rule-set:geolocation-cn` 及 `geosite:connectivity-check` 构成，国内域名直接返回真实 IP，跳过 Fake-IP 映射
- `nameserver-policy` 精准分流：`rule-set:geolocation-!cn` 走国外 DNS；`rule-set:private`/`cn`/`geolocation-cn`/`apple_cn`/`cloudflare_cn`/`games_cn` 走国内 DNS
- **节点 DNS 感知**：自动提取代理节点 `server` 域名，与用户自定义的 `nameserver-policy` / `proxy-server-nameserver-policy` 交叉匹配后注入 `proxy-server-nameserver-policy`；无匹配时全部节点域名指向私有 DNS
- **Hosts 映射直达**：用户 `hosts` 中与节点 `server` 匹配的映射直接改写节点 server 字段，同时注入默认 hosts
- **纯净默认解析**：默认 `nameserver` 仅保留 Google + Cloudflare DoH，防 GFW 抢答污染

### 5.5 AdBlock（广告拦截）
- 自托管 `anti-ad.mrs` 规则集，源头 [anti-AD](https://github.com/privacy-protection-tools/anti-AD)
- 经 jsdelivr CDN 分发，每 12h 自动更新，默认 REJECT 可切 DIRECT
- 策略组 `AdBlock` 仅提供 `REJECT` / `DIRECT` 两个出口

### 5.6 自动补全客户端指纹
对 vmess/vless/trojan/anytls 协议自动补全 `client-fingerprint: chrome`。Hysteria2 用独立 `fingerprint` 字段，TUIC 不涉及 TLS 指纹，不支持 uTLS。

### 5.7 QUIC 管控
```js
'AND,((NETWORK,udp),(DST-PORT,443),(RULE-SET,private_ip,no-resolve)),Direct',
'AND,((NETWORK,udp),(DST-PORT,443),(OR,((RULE-SET,geolocation-cn),(RULE-SET,cn_ip,no-resolve)))),Direct',
'AND,((NETWORK,udp),(DST-PORT,443)),QUIC'
```
- 私有 IP / 国内 QUIC（匹配 geolocation-cn / cn_ip）→ Direct
- 境外 QUIC → QUIC 策略组（Default 代理 / REJECT 阻断）
- 注意：QUIC 走 UDP 443，Windows 必须开 TUN 模式才能劫持（系统代理只处理 TCP）

### 5.8 双栈 & TUN 模式
注入 5 个直连节点：Dual Stack / IPv4 Only / IPv6 Only / IPv4 Preferred / IPv6 Preferred

### 5.9 规则自动更新
所有分流规则集每 **12 小时**自动更新（经 jsdelivr CDN 分发，实际生效最长约 24h）。来源：
- [appshubcc/bett-rules](https://github.com/appshubcc/bett-rules)：主数据源，规则集按 `geo/geosite/*.mrs`、`geo/geoip/*.mrs`、`asn/*.mrs` 路径组织（含 path-in-bundle，可打包进内核内置 geo 数据）
- 本仓库自托管（GitHub Actions 每日同步）：`fakeip-filter.mrs`（Fake-IP 过滤，源头 [ShellCrash](https://github.com/juewuy/ShellCrash)）、`anti-ad.mrs`（广告拦截，源头 [anti-AD](https://github.com/privacy-protection-tools/anti-AD)）

### 5.10 防御性架构
- 每处外部输入显式类型校验（typeof / Array.isArray / == null）
- 主流程 try/catch 包裹，异常返回最小可用配置（空代理+空规则），不断连
- 不可变配置合并（浅拷贝 `{ ...config }`），不污染原始 config
- 严格 ES2020 子集，不用 `??=` / `String.replaceAll` / `Array.at`，兼容 QuickJS

### 5.11 dialer-proxy 修复
节点重命名后自动检查所有 dialer-proxy 字段：指向已改名→改写新名称；指向存活未改名→不变；指向被过滤移除→删除字段；检测到重名节点时输出日志警告

### 5.12 其他
- Sniffer 域名嗅探（HTTP/TLS/QUIC，跳过 mijia / push.apple.com / .lan / .local）
- NTP 每 30 分钟阿里 NTP 同步
- Hosts 硬编码防 DNS 污染（cn.bing.com 重定向 global.bing.com，屏蔽哔哩哔哩 PCDN）
- 节点图标（Qure 图标集）
- 测速 URL 国内外分流（国外 Cloudflare / 国内华为）
- unified-delay + TCP 并发

## 6. 项目文件结构（2026-09-08）

| 文件 | 说明 |
|---|---|
| `Mihomo-Script-Rules.js` | 主脚本（约 1000 行），全部逻辑所在 |
| `anti-ad.mrs` | 广告拦截二进制规则集（源头 anti-AD），由 Actions 每日同步 |
| `fakeip-filter.mrs` | Fake-IP 过滤二进制规则集（源头 ShellCrash），由 Actions 每日同步 |
| `Test/` | Node.js 测试套件：冒烟测试 + ES2020 兼容性检查（espree）+ QuickJS 引擎验证（quickjs-emscripten），`npm test` 可本地运行，CI 亦运行 |
| `.github/workflows/` | `release.yml` 发布 · `rule-check.yml` 规则校验 · `lint.yml` 代码风格 · `sync-antiad.yml` 同步 anti-ad · `sync-fakeip.yml` 同步 fakeip-filter |
| `README.md` / `LICENSE` | 文档 / MIT 许可证 |

## 7. 客户端兼容性

| 客户端 | 兼容性 | 备注 |
|---|---|---|
| Bettbox | 完美 | QuickJS 引擎，强烈推荐 |
| FlClash | 较好 | 原生支持 JS 预处理 |
| Clash Verge Rev | 可用 | boa_engine，print() 可能不兼容 |
| Clash Nyanpasu | 可用 | 同上需验证 |
| Stash / Shadowrocket | 不兼容 | 项目为纯脚本方案，无静态配置可用，建议 sub-store 中转或改用 MyClash |
| Surge / Quantumult X | 不兼容 | 同上 |
| **Clash Apple (Hako)** | **未列出** | Hako 是 mihomo 内核，JS 预处理是客户端功能，大概率不支持脚本模式 |

> 原静态纯配置已从仓库移除，本项目不再提供"不支持 JS 的客户端"的静态配置方案。

## 8. 个性化定制

脚本开头定义所有可配置常量，直接编辑即可生效：
- `Compatible_With_Bettbox`：声明兼容 Bettbox，用于客户端展示规则开关
- `ruleOptionsEnable`：17 个服务策略组开关
- `regionDefinitionsEnable`：16 地区 + Low-Rate/High-Rate 开关
- `excludeFilterEnable`：杂质节点过滤开关（默认 true）
- `quicEnable`：QUIC 管控开关（默认 true）
- `excludeFilter`：自定义过滤正则
- `BETT` / `ZZZ`：规则集 CDN 地址常量（bett-rules / 本仓库自托管规则集）

## 9. 与用户现有配置的对比参考

用户现有 Clash 配置（mickeu/Clash）特征：
- 规则集：blackmatrix7（.yaml 格式）vs 本项目 bett-rules（.mrs 二进制，加载更快）
- 地区组：5 个（日/港/新/美/其他）vs 本项目 16 个 + Others + 倍率组
- 服务分流：基础分组 vs 本项目 17 个独立服务组
- DNS：fake-ip-filter + nameserver-policy + fallback（国内为主）vs 本项目 nameserver 默认只留境外 DoH 防 GFW 抢答
- QUIC 管控：无 vs 本项目有独立策略组
- 广告拦截：无 vs 本项目集成 anti-ad.mrs

**可参考借鉴的点：** QUIC 管控思路、.mrs 规则集格式、nameserver 默认只用境外 DoH 防 GFW 抢答、client-fingerprint 自动补全