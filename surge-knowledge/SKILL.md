---
name: Surge 完整知识库
description: Surge 官方手册（2026 重编写版）。涵盖原理指南、Profile 格式、规则系统（域名/IP/HTTP/进程/协议/逻辑/脚本规则集等）、16+ 种代理协议（HTTP/SOCKS5/Snell/Shadowsocks/VMess/Trojan/TUIC/Hysteria2/AnyTLS/SSH/WireGuard/Tailscale 等）、策略组（Select/URL-Test/Fallback/Load-Balance/Smart/Subnet）、DNS（DoH/DoH3/DoQ/DoT/本地映射/fake-IP）、HTTP 处理（MITM/URL 重写/Header/Body/Map-Local）、脚本（9 种类型 + JS API）、设备网络功能（VIF/网关/DHCP/端口转发/Ponte/Snell 服务器/MTProto）、工具 API（Dashboard/CLI/HTTP API/URL Scheme/信息面板）。来源：manual.nssurge.com 官方重编写版
source_url: https://manual.nssurge.com/ + https://kb.nssurge.com/surge-knowledge-base/zh/
license: Proprietary
last_sync: 2026-10-01
---
# Surge 官方手册（重编写版）

> 来源：https://manual.nssurge.com/（手册）+ https://kb.nssurge.com/surge-knowledge-base/（知识库）
> 同步时间：2026-10-01

### 📁 本地文档镜像（docs/，2026-10-01 全量同步）
- **docs/manual/**：官方手册全部 86 页的 `.md` 源文件（文件名 `manual_<路径下划线化>.md`），来源 `https://manual.nssurge.com/<路径>.md`（官网支持 `.md` 直出）
- **docs/kb-zh-clean/**：中文知识库 32 篇（文件名 `<分类>_<标题>.md`），来源 `https://kb.nssurge.com/surge-knowledge-base/zh/<路径>.md`
- **docs/kb-en/**：英文知识库 32 篇，来源 `https://kb.nssurge.com/surge-knowledge-base/<路径>.md`（英文 KB URL 不含 /en/）
- **文档索引**：KB 站点提供 `https://kb.nssurge.com/llms.txt`，含中英全部文章链接；页面 URL 追加 `.md` 即得 Markdown 源
- **更新检查**：抓 `https://manual.nssurge.com/SUMMARY.md`（HonKit 目录）对比 docs/manual/ 文件列表；抓 `kb.nssurge.com/llms.txt` 对比 KB 篇目；内容级对比直接抓 `.md` 与本地 diff

---

## Getting Started / How Surge Works

# How Surge Works


Surge has four core jobs: capture traffic, resolve names, choose an outbound policy, and optionally inspect or modify HTTP traffic. This page walks through the life of a request and the components involved.


## The Request Lifecycle


### Traffic Takeover


Surge can receive traffic in three ways:


- System proxy settings: apps that honor the system HTTP/SOCKS proxy configuration send requests to Surge's proxy ports.

- Local proxy ports: any app or device can be pointed at Surge's HTTP or SOCKS5 listener directly, including other devices on the LAN.

- Surge VIF: a virtual network interface that captures raw TCP, UDP, and ICMP traffic from apps that do not honor proxy settings.


On Surge iOS, the VIF is part of the VPN-based takeover and is enabled by default. On Surge Mac, it is enabled by turning on Enhanced Mode. Surge Mac can additionally act as a layer-3 gateway for other devices; see Gateway Mode.


### DNS Resolution


Surge has its own DNS client instead of relying on the system resolver. This enables concurrent queries to multiple servers, encrypted DNS, local DNS mapping, per-domain DNS server assignment, and fake-IP handling on the VIF. See DNS Overview.


### Rule Matching


Rules answer "which traffic is this?" Each request is matched against the `[Rule]` section from top to bottom; the first matched rule wins. Rules can match domains, IP ranges, GeoIP, processes, protocols, source attributes, and more, and the list must end with a `FINAL` rule. See Rules Overview.


### Policy Execution


Policies answer "what should Surge do with it?" The matched rule returns a policy: a built-in policy such as `DIRECT` or `REJECT`, a proxy policy defined in `[Proxy]`, or a policy group. Policy groups let you write rules against a stable group name while switching the actual proxy manually or automatically.


### HTTP Processing (Optional)


After a policy is selected, HTTP requests and responses can be rewritten, mapped to local data, or processed by scripts. HTTPS traffic must match the MITM hostname list before Surge can see the decrypted content. See HTTP Processing.


## Components


### Surge Proxy Server


The core of Surge: a full-featured HTTP/SOCKS5 proxy server optimized for macOS and iOS. All captured traffic ultimately flows through it for rule matching and policy execution.


### Surge Virtual Network Interface (Surge VIF)


Some apps do not obey system proxy settings (such as Mail.app) because they use raw TCP sockets. The VIF captures this traffic at the IP layer and feeds it into the proxy engine. It handles only TCP, UDP, and ICMP; ICMP cannot be proxied, so the VIF answers it directly.


This is the architecture of Surge iOS:


### Surge Dashboard


A graphical interface for reviewing requests, inspecting the DNS cache, and analyzing traffic. The Dashboard app ships with Surge Mac and can connect to the local instance or to a remote Surge iOS/Mac instance over the network or USB when `external-controller-access` is configured. See Dashboard.


### surge-cli


A command-line tool bundled with Surge Mac for controlling and diagnosing local or remote Surge instances, checking profiles, and running tests. See CLI.


## Where to Go Next


- Build a minimal profile: Quick Start

- Understand the profile file itself: Profile Format

- See what differs between platforms: Platform Differences

---
## Getting Started / Quick Start

# Quick Start


Surge is controlled by a profile: a plain-text file that describes how traffic is captured, how requests are matched, and which outbound policy is used. This page builds a minimal working profile.


Most setups only need four sections:


[General]
dns-server = system, 1.1.1.1, 8.8.8.8

[Proxy]
ProxyA = https, proxy.example.com, 443, username, password

[Proxy Group]
Proxy = select, ProxyA, DIRECT

[Rule]
DOMAIN-SUFFIX,example.com,Proxy
GEOIP,CN,DIRECT
FINAL,Proxy
## How to Read This Profile


- `[General]` contains global options such as DNS servers, testing URLs, and takeover behavior. This example uses the system DNS servers plus 1.1.1.1 and 8.8.8.8, queried concurrently.

- `[Proxy]` defines outbound policies. `ProxyA` forwards traffic to an HTTPS proxy server; a policy can also connect directly or use any other supported protocol.

- `[Proxy Group]` lets you choose among multiple policies. The `select` group named `Proxy` is switched manually in the app UI between `ProxyA` and the built-in `DIRECT` policy.

- `[Rule]` matches requests from top to bottom; the first matched rule decides the policy. Here, `example.com` and its subdomains go through the `Proxy` group, destinations with a Chinese GeoIP result connect directly, and everything else falls to the `FINAL` rule.


Load the profile, start Surge, and check the request list in the UI or Dashboard to confirm traffic is being captured and matched as expected.


## Where to Go Next


- To understand the profile file format, read Profile Format.

- To write matching logic, read Rules Overview.

- To configure proxy servers, read Policies Overview.

- To choose among proxies automatically, read Policy Groups.

- To customize DNS behavior, read DNS Server and Local DNS Mapping.

- To modify HTTP requests and responses, read HTTP Processing and Scripting.

---
## Getting Started / Platform Differences

# Platform Differences


Surge Mac and Surge iOS share the same core engine and profile format, and most options behave identically. This page consolidates the differences: features exclusive to one platform and where each is documented.


Surge tvOS is included with the Surge iOS app and generally behaves like Surge iOS; features marked iOS-only usually apply to tvOS as well unless noted on the feature's page.


## Surge Mac Only


[TABLE]


|
Feature |
 Notes |
 Documentation |
 |


|
 Enhanced Mode toggle |
 The VIF must be enabled manually on Mac; on iOS it is part of the VPN takeover and enabled by default. |
 Enhanced Mode |
 |

|
 Gateway Mode |
 Operate as a layer-3 gateway handling traffic for other LAN devices. |
 Gateway Mode |
 |

|
 DHCP server |
 Provide DHCP service for gateway-managed devices, with the `[DHCP]` section for lease tuning. |
 DHCP |
 |

|
 Built-in Snell server |
 Accept incoming Snell v1/v6 proxy connections via `[Snell Server]`. |
 Snell Server |
 |

|
 Ponte server role |
 Any Surge device can act as a Ponte client, but only Surge Mac can serve as the Ponte server (home network access point). |
 Surge Ponte |
 |

|
 External Proxy Program |
 Launch and manage an external proxy executable as a policy. Surge iOS treats `external` policies as REJECT. |
 External Proxy Program |
 |

|
 PROCESS-NAME rule |
 Match traffic by the originating process. Surge iOS ignores these rules. |
 Process Rules |
 |

|
 MAC-ADDRESS rule |
 Match LAN client devices by MAC address. |
 Source and Port Rules |
 |

|
 surge-cli |
 Command-line tool for controlling local and remote instances. |
 CLI |
 |

|
 Surge Dashboard app |
 The Dashboard app ships with Surge Mac; it can also connect to remote Surge iOS instances over network or USB. |
 Dashboard |
 |

|
 Mac-only `[General]` keys |
 `http-listen`, `socks5-listen`, `read-etc-hosts`, `set-system-socks-proxy`, `subnet-exp-wifi-always-match`. |
 General Section |
 |


[/TABLE]
### Metered Network Mode


Surge Mac can restrict which applications and processes may access the Internet, which is useful on metered connections such as a phone hotspot. The allowed application list is configured in the Surge Mac interface. The mode can be turned on automatically for specific networks with the `cellular-mode` parameter in Subnet Settings.


## Surge iOS Only


[TABLE]


|
Feature |
 Notes |
 Documentation |
 |


|
 Works on cellular |
 Surge iOS runs as a Network Extension VPN, so all functions work on Wi-Fi and cellular networks alike. |
 How Surge Works |
 |

|
 `compatibility-mode` |
 Selects the takeover mode (proxy takeover, VIF takeover, or combinations) to work around app-specific issues. |
 General Section |
 |

|
 CELLULAR policy family |
 `CELLULAR`, `CELLULAR-ONLY`, `HYBRID`, `NO-HYBRID` built-in policies for controlling interface usage. |
 Built-in Policies |
 |

|
 `hybrid` policy parameter |
 Set up proxy connections over Wi-Fi and cellular simultaneously. |
 Policy Parameters |
 |

|
 CELLULAR-RADIO / CELLULAR-CARRIER rules |
 Match by radio access technology or carrier (also available on tvOS). |
 Protocol and Network Rules |
 |

|
 Cellular Fallback subnet setting |
 Per-network override of Wi-Fi Assist / All-Hybrid behavior. |
 Subnet Settings |
 |

|
 Information Panel |
 Show custom panels in the app main view, backed by scripts. |
 Information Panel |
 |

|
 URL scheme start/stop actions |
 `start`, `stop`, and `toggle` URL scheme actions are iOS-only. |
 URL Scheme |
 |

|
 iOS-only `[General]` keys |
 `allow-wifi-access`, `allow-hotspot-access`, `wifi-access-http-port`, `wifi-access-socks5-port`, `wifi-access-http-auth`, `wifi-assist`, `all-hybrid`, `hide-vpn-icon`, `include-all-networks`, `include-local-networks`, `include-apns`, `include-cellular-services`, `auto-suspend`. |
 General Section |
 |


[/TABLE]
Platform-specific keys are simply ignored on the other platform, so a single profile can be shared between Surge Mac and Surge iOS. To restrict individual profile lines to one platform, use line requirement expressions such as `#!MACOS-ONLY`.

---
## Profile / Format

# Profile Format


The profile is the source of truth for Surge behavior. Most profile content can be adjusted in the user interface, but advanced or experimental features may still require manual editing.


Surge profiles use an INI-like format. Content is divided into sections such as `[General]`, `[Proxy]`, `[Proxy Group]`, and `[Rule]`.


[General]
loglevel = notify

[Proxy]
ProxyA = http, 1.2.3.4, 80

[Rule]
DOMAIN-SUFFIX,example.com,ProxyA
FINAL,DIRECT
Each section has its own syntax. Sections like `[General]` and `[MITM]` use `key = value` lines, and line order usually does not matter. In ordered sections such as `[Rule]`, line order is part of the behavior.


## Sections


Surge recognizes the following section names. Content in unrecognized sections is preserved as-is when the profile is saved, without errors.


[TABLE]


|
Section |
 Purpose |
 |


|
 `[General]` |
 Global settings |
 |

|
 `[Proxy]` |
 Proxy policies |
 |

|
 `[Proxy Group]` |
 Policy groups |
 |

|
 `[Rule]` |
 Rules |
 |

|
 `[Host]` |
 Local DNS mapping |
 |

|
 `[URL Rewrite]` |
 URL Rewrite |
 |

|
 `[Header Rewrite]` |
 Header Rewrite |
 |

|
 `[Body Rewrite]` |
 Body Rewrite |
 |

|
 `[Map Local]` |
 Map Local |
 |

|
 `[MITM]` |
 HTTPS decryption |
 |

|
 `[Keystore]` |
 Certificates and private keys |
 |

|
 `[SSID Setting]` |
 Subnet settings |
 |

|
 `[Script]` |
 Scripting |
 |

|
 `[Panel]` |
 Information panels |
 |

|
 `[Ponte]` |
 Surge Ponte |
 |

|
 `[Port Forwarding]` |
 Port forwarding |
 |

|
 `[Testing]` |
 Throughput testing |
 |

|
 `[DHCP]` |
 DHCP server (Mac gateway mode) |
 |

|
 `[Snell Server]` |
 Built-in Snell server |
 |

|
 `[MTProto]` |
 Built-in MTProto server |
 |

|
 `[WireGuard <name>]` |
 WireGuard policy configuration |
 |

|
 `[Tailscale <name>]` |
 Tailscale policy configuration |
 |

|
 `[Ruleset <name>]` |
 Inline rule sets |
 |


[/TABLE]
## Comments


Comment lines start with `#`, `;`, or `//`. Inline comments are also supported.


# This is a comment line.
; This is a comment line.
// This is a comment line.
```
dns-server = 8.8.8.8 // This is an inline comment.
dns-server = 8.8.8.8 # This is an inline comment.
dns-server = 8.8.8.8 ; This is an inline comment.

```

When using inline comments, there must be at least one space before the delimiter.


## Quoted Values iOS 5.21.0+ Mac 6.8.0+


Inside a double-quoted profile value, use `\"` for a literal double quote and `\\` for a literal backslash. This allows values containing quotes or backslashes to be saved and reloaded without changing their contents.


example = "a quoted value: \"text\"; path: C:\\Proxy"
## Profile Types


Profiles are divided into three categories:


- Normal profile: created manually or used by default.

- Managed profile: usually provided by an enterprise administrator or service provider. A managed profile cannot be modified locally because it can be updated remotely. To make changes, first create a copy to turn it into a normal profile.

- Enterprise profile: Enterprise version only. It cannot be modified, viewed, or copied.


## Detached Profile Section


To support complex setups, Surge can split one or more sections into another file with the `#!include` statement.


Main.conf


[Proxy]
#!include Proxy.dconf
The referenced file must contain the corresponding section declaration. The file can contain one section, multiple sections, or a complete profile.


Proxy.dconf


[Proxy]
ProxyA = http, 1.2.3.4, 80
This is useful when you want to:


- Reference the `[Proxy]`, `[Proxy Group]`, and `[Rule]` sections of a managed profile while writing other sections yourself. This keeps proxy-related content updated without affecting local UI-managed settings.

- Share sections across multiple profiles. For example, when using Surge on both iOS and macOS, `[Proxy]`, `[Proxy Group]`, and `[Rule]` are often the same, while `[General]` may be different. You can create `iOS.conf` and `macOS.conf`, then place the shared sections in another file.


[Proxy]
#!include Forwarding.dconf

[Proxy Group]
#!include Forwarding.dconf

[Rule]
#!include Forwarding.dconf
This way, adjusting `[General]` on iOS does not affect macOS, and you do not need to maintain two copies of the same routing configuration.


Additional notes:


- After modifying the profile in the UI, Surge writes the section back to the corresponding detached profile according to the include statement. If the included file contains other unused sections, only the used section is modified.

- If a managed profile is referenced, the referenced section cannot be edited locally, but other sections remain editable.

- A filename suffix is not required. If the file is a complete profile, you can continue using `.conf`. If it is not a complete profile, use another suffix to avoid showing it in the profile list.

- Starting from Surge iOS 4.12.0 and Surge Mac 4.5.0, one section can include multiple detached profiles. That section is marked read-only and cannot be edited in the UI.


  [Proxy]
  #!include A.dconf, B.dconf


### `#include`/`#!include` 语法与用法模式（当前版本）

**CLI/API 实测：`#!include`（带感叹号）有效，`#include`（无感叹号）无效**。3821 TestFlight 官方更新日志「Profile System Updates」宣布引入 `#include` 语法与三种模式，但实测该版本**大部分用例未真正落地**：

- `#include`（无感叹号）：CLI 和 UI 路径均不加载引用文件内容，`[Proxy]` 段从展开配置中消失，`proxies` 为空。
- `#!include` 单文件：正常加载，UI 可编辑（改动写回文件）。
- `#!include A.dconf, B.dconf`（逗号式多文件）：**能加载**，但官方说"只读"，实测 UI **仍可编辑**（不遵守只读声明）。
- `#!include A.dconf` + `#!include B.dconf`（独立两行多文件）：能合并加载，只读状态未 UI 实测（按官方逻辑应为只读）。
- 混合内容（`#!include` + 内联规则混排）：能加载（内部 123 规则 + 新增 1 条 = 124），官方说"只读"未实测。

**结论**：3821 的 Profile System Updates 中，**只有"单文件 `#!include` 段 UI 可编辑写回"这一项真正落地了**（之前版本单文件 include 段也是 UI 只读的）。其余行为（`#include` 语法、多文件/混合内容只读）基本未实装或未生效，目前仍须用 `#!include`。功能随版本演进可能有变，需按实测为准。

当前版本支持的三种用法模式（均以 `#!include` 实测为主）：

1. **单一 Dedicated Include（UI 可编辑）**

   [Proxy]
   #!include proxy.dconf

   段内只有一条 `#!include` 指令时，该段仍可在 UI 中完整编辑；通过 UI 做的任何修改都会正确写回 proxy.dconf。

2. **Multiple Includes（只读）**

   [Proxy]
   #!include a.dconf, b.dconf

   多个文件合并进同一个段。因为 UI 无法判断修改应写回哪个文件，该段转为只读，不能通过 UI 编辑。

3. **混合内容 + Include（新，只读）**

   [Rule]
   #!include common-rule-a.dconf
   DEST-PORT,123,DIRECT
   #!include common-rule-b.dconf

   `#!include` 可以与段内普通内容自由混排。如果段内**只有一条 `#!include` 引用指令**（如 `[Proxy]` 段内仅 `#!include Proxy.dconf`），则该段本身无可编辑的配置项——它就是一个引用指针，要改内容应直接编辑被引用的 dconf 文件。

**dconf 与 conf 在配置列表中的显示区别**（5.102.0 (3821) 实测）：
- 两者均显示在**同一配置列表**中，没有分开显示
- 区别在于功能：`.conf` 是完整配置，可切换为当前配置；`.dconf` 是非完整配置片段（被 #!include 引用），虽然列表里能看到，但不能独立切换为当前配置使用
- 官方手册（KB_CONTENT.md）第 304 行："dconf 文件在 Surge iOS 里可在列表中显示，并可以使用文本编辑"

**5.102.0 (3821) / 2026-08-19 起**，配置列表中点开 dconf 文件已可直接编辑（以前不能编辑）。

如果段内是 `#!include` + 内联规则混排，则内联规则部分可编辑，引用部分仍来自外部文件。
实测：`#!include Rule.dconf` + 一行内联规则后，展开配置包含全部 123 条规则 + 新增规则（共 124 条），验证通过。

注意事项：

- 在 `[Rule]` 段使用时尤其要注意：**FINAL 规则会立即终止规则匹配**，任何在 FINAL 之后定义或 include 的规则都不会被评估。若将多个规则文件 include 进 `[Rule]`，务必保证包含 FINAL 的规则文件放在最后。


### Linked Profiles Mac 6.0.0+


`#!include` can also reference a remote managed profile (a URL) directly. This lets you build a local "overlay" profile that keeps following updates from the upstream config.


[Rule]
#!include https://example.com/managed.conf
When the referenced content is read-only, Surge will prompt to create a linked layer if you try to edit those sections. The local layer stores only your overrides, while the remote managed profile keeps receiving updates automatically.


## Modules


Detached profile sections split one profile into multiple files. Modules are different: they patch selected parts of a profile to enable a specific behavior, and can be turned on and off independently.


## Line Requirement


A line can be constrained to take effect only in specific environments, using the `#!REQUIREMENT` statement or the simplified notations `#!IOS-ONLY`, `#!MACOS-ONLY`, and `#!TVOS-ONLY`. See Line Requirement.

---
## Profile / Managed Profile

# Managed Profile


Surge can automatically update a profile from a URL. A managed profile starts with:


#!MANAGED-CONFIG http://test.com/surge.conf interval=60 strict=true
The profile can only be updated while the main Surge app is running.


Ensure the new remote profile also includes the `#!MANAGED-CONFIG` line. Without it, the profile reverts to a standard profile.


## Parameters


#### interval


Optional, in seconds, default: 86400


Set the update interval for the profile. This is the shortest time before an update may be triggered; Surge does not necessarily update immediately after the interval passes.


#### strict


Optional, Boolean, default: false


If `strict` is true, Surge requires a successful update after the interval arrives. Otherwise, if the update fails, the user may continue using the outdated profile.


Note: Even when `strict` is true, the user can still start Surge from a widget or the VPN switch in Settings.


## REQUIREMENT Statement


The `!REQUIREMENT` statement can be used at the beginning or end of a profile line to limit the line's effect to specific environments:


#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB
Group = url-test, policyA, policyB //!REQUIREMENT CORE_VERSION<22
Since requirement expressions are lost when a profile is modified in the UI, this feature is mainly used in managed and enterprise profiles. It lets one managed profile serve clients on different platforms and Surge versions.


See Line Requirement for the expression syntax, available variables and operators, Core Version values, and the simplified notations (`#!IOS-ONLY`, `#!MACOS-ONLY`, `#!TVOS-ONLY`).


## FORBIDDEN-AUTO-UPGRADE Statement


Starting with Surge iOS 5.11.0 and Mac 5.7.0, Surge can automatically optimize profiles during upgrades so managed profiles can use newer features when possible.


If you do not want the profile to apply certain automatic optimizations, use the `FORBIDDEN-AUTO-UPGRADE` expression.


Example:


#!FORBIDDEN-AUTO-UPGRADE smart-group
Currently available optimization keywords include


- `smart-group`: automatically upgrades `url-test/load-balance` groups to `smart` groups.

---
## Profile / Module

# Module


A module is a set of settings that overrides the current profile. You may use modules to:


- Tweak settings in a non-editable profile, such as a managed profile or enterprise profile.

- Change part of the settings with one tap. For example, you may use a module to enable MITM for all hostnames and adjust the filter temporarily.

- Use a module written by others to accomplish a particular task. For example, a coworker may share a module that rewrites API requests to a test server.

- Customize a shared profile for different devices or scenarios. The enabled state of modules is not synced to other devices.


## Basic Concepts


A module is like a patch to the current profile. The settings of modules have a higher priority than the settings of the profile.


There are three types of modules:


- Internal Modules: Provided by Surge itself.

- Local Modules: `.sgmodule` files placed in the profile directory.

- Installed Modules: Modules installed with a URL.


Compared with detached profile sections, which split one profile into multiple files, modules patch selected parts of a profile to enable a specific behavior. However:


- Modules cannot adjust the content of `[Proxy]` and `[Proxy Group]` sections. Rule lines may only be inserted at the top of the rule list and are restricted to internal policies.

- A module cannot adjust the CA certificate of MITM.

- The settings of a module override the main profile, so they cannot be adjusted via the UI.


## Write a Module


The syntax of a module is the same as the profile. You are allowed to override these sections:


- General, MITM


Override: `key = value`

- Append to the original value: `key = %APPEND% value`

- Insert in the front of the original value: `key = %INSERT% value`


You can manipulate the `hostname` and `skip-server-cert-verify` fields only in a MITM section.


The legacy `[Replica]` section used by the HTTP capture feature was removed in Surge Mac 5.4.0, so modules no longer need to patch it.


- `[WireGuard *]` sections


  WireGuard policies live in sections whose names start with `WireGuard`. Modules can override or append keys inside those sections just like the main profile.


- `[Ruleset *]` sections


  When you define inline rule sets, modules may patch them as well, which is useful for managed configurations that ship inline lists.


- Rule, Script, URL Rewrite, Header Rewrite, Host


  New lines are inserted at the top of the original content.


  The rules in a module can only use internal policies: DIRECT, REJECT, and REJECT-TINYGIF.


- Metadata


  You may add metadata in a module file:


  #!name=Name Here
  #!desc=Description Here
  You may limit a module to a specified platform. (Optional)


  #!system=mac


## Examples


```
#!name=MitM All Hostnames
#!desc=Perform MitM on all hostnames with port 443, except those to Apple and other common sites which can't be inspected. You still need to configure a CA certificate and enable the main switch of MitM.

[MITM]
hostname = -*.apple.com, -*.icloud.com, -*.mzstatic.com, -*.crashlytics.com, -*.facebook.com, -*.instagram.com, *

```

```
#!name=Game Console SNAT
#!desc=Let Surge handle SNAT conversation properly for PlayStation, Xbox, and Nintendo Switch. Only useful if Surge Mac acts the router for these devices.
#!system=mac
[General]
always-real-ip = %APPEND% *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com

```

## Parameter Tables Mac 5.5.0+


Use the `#!arguments` metadata to declare parameters that the user can customize when enabling the module. Separate multiple parameters with commas. Use a colon after a parameter name to provide its default value; the default value is optional.


#!arguments=hostname:example.com,enable_mitm:true
#!arguments-desc=Configure the hostname and whether MITM is enabled.


`#!arguments-desc` is optional. Its value is displayed as a general description for the parameter table; it does not define a separate description for each parameter.


Reference a parameter by wrapping its name in three braces. Surge replaces every declared placeholder with the configured value, or its default value when the user has not provided one, before applying the module. Parameter names and placeholders are case-sensitive.


[MITM]
hostname = {{{hostname}}}

[Script]
example = type=generic, script-path=script/example.js, argument="{{{enable_mitm}}}"


Values entered by the user are saved with the module instance and shown again when its parameters are edited.


The query-string form (hostname=example.com&enable_mitm=true) and %PARAMETER% placeholders are not supported for module parameter tables. %APPEND% and %INSERT% are separate module operators and are unrelated to parameter substitution.


Use only letters, numbers, and underscores in parameter names, and remove unused placeholders when deleting an argument.


### 实战补充：`#!arguments` 使用经验（2026-08-19 实测）

**与 Egern `env_schema` 的本质区别**：
- Egern `env_schema` 支持 `options` 枚举列表，呈现在 UI 中为**下拉选择器**，用户点选而非输入
- Surge `#!arguments` 只有**自由文本输入框**，无 options 枚举，校验靠 `#!arguments-desc` 描述引导
- 所以 Surge 能"编辑参数"但做不出"下拉选择"。如果需要在描述中提示可选值，直接在 `#!arguments-desc` 里列出来

**必须 reload 才生效**：
- 参数替换发生在 reload 时的展开配置阶段（非运行时）
- 改完参数后必须 Surge 中 reload 配置 / 刷新模块，否则 `{{{KEY}}}` 占位符不会被替换，脚本收到的是原始占位符字符串

**证据**：`#!arguments` 替换链路完整验证——模块 `{{{CLIENT}}}` 占位符 → reload 时替换进 `argument=tme_redirect=XXX` → 注入脚本 `$argument` → 脚本正则提取值使用。**改参数无需改脚本**，两解耦。

**参数命名规范**：只使用字母、数字、下划线，大小写敏感。`{{{CLIENT}}}` 与 `{{{client}}}` 不同。

**实际案例参考**：`mickeu/surge` 仓库的 `TG链接重定向.sgmodule` 使用 `#!arguments=CLIENT:Turrit` 让用户切换跳转目标客户端；xream/scripts 的 `net-lsp-x.sgmodule` 大量参数（DOMESTIC_IPv4/ICON 等）均通过此机制可编辑，详见其 README。

## Requirements iOS 5.10.0+ Mac 5.6.0+


A module may add a `#!requirement=` description, allowing for more complex usage condition restrictions. For example, if the module uses the newly added Body Rewrite feature, it needs to restrict the version of the Surge core.


#!requirement=CORE_VERSION>=20
It also supports logical expressions, such as `CORE_VERSION>=20 && (SYSTEM = 'iOS' || SYSTEM = 'tvOS')`.


The variables that can be used for judgment are as follows:


- CORE_VERSION: Number, such as `20`

- SYSTEM: String, such as `macOS`, `iOS`, `tvOS`

- SYSTEM_VERSION: String, such as `Version 17.4.1 (Build 21E236)`

- DEVICE_MODEL: String, such as `Mac15,8`

- LANGUAGE: String, such as `zh-Hans`


These are the same variables used by line requirements; see that page for Core Version values.

---
## Profile / Requirement Expressions

# Line Requirement iOS 5.11.0+ Mac 5.7.0+


You can set constraints to make a certain line of configuration effective only when specific conditions are met. This is mainly useful for sharing one profile across devices, platforms, and Surge versions.


Group = url-test, policyA, policyB #!REQUIREMENT CORE_VERSION<22
For items that support an enabled/disabled state, lines that do not meet the conditions are treated as disabled. Other unmatched lines are treated as comments.


## Start-of-Line and End-of-Line Forms


A `#!REQUIREMENT` expression can be placed at the beginning of a line or appended to the end of a line:


#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB
Group = url-test, policyA, policyB //!REQUIREMENT CORE_VERSION<22
Since versions earlier than Surge iOS 5.11.0 and Surge Mac 5.7.0 do not support this expression, both forms are provided so you can support older clients. In the example above, an older version treats the first line as a normal comment and the end-of-line requirement on the second line as a regular comment, so only the second line takes effect. A newer version evaluates both expressions and uses the Smart group instead.


## REQUIREMENT Expression


Variables available for judgment: `CORE_VERSION`, `SYSTEM`, `SYSTEM_VERSION`, `DEVICE_MODEL`, `LANGUAGE`.


Available operators: `=`, `==`, `>=`, `=>`, `<=`, `=<`, `>`, `<`, `!=`, `<>`, `AND`, `&&`, `OR`, `||`, `NOT`, `!`, `BEGINSWITH`, `CONTAINS`, `ENDSWITH`, `LIKE`, `MATCHES`.


A typical example of variable values:


CORE_VERSION: 22
SYSTEM: iOS
SYSTEM_VERSION: System Version 17.4.1 (Build 21E236)
DEVICE_MODEL: iPhone16,1
LANGUAGE: en-US
Strings in expressions should be wrapped in `'`, such as `#!REQUIREMENT SYSTEM=='macOS'`.


When an expression contains spaces, wrap the whole expression in `"`.


`#!REQUIREMENT "CORE_VERSION>=22 AND SYSTEM=='iOS'" Group = smart, policyA, policyB`


### Core Version


Core Version can be used to determine whether a feature is available.


Starting with Surge Mac 6.8.0 and Surge iOS 5.21.0, Core Version is derived from the corresponding Surge Mac version instead of being maintained separately. The value is encoded as `major * 1000000 + minor * 1000 + patch`. For example, Surge Mac 6.8.0 and Surge iOS 5.21.0 use Core Version `6008000`. iOS 5.21.0+ Mac 6.8.0+


Earlier releases used independently assigned Core Version values:


- 22: Surge Mac 5.7.0, Surge iOS 5.11.0, Smart Group

- 20: Surge Mac 5.6.0, Surge iOS 5.10.0, Body Rewrite, Inline Map Local


## Simplified Notation iOS 5.14.3+ Mac 5.10.0+


Three simplified notations are provided for convenience: `#!IOS-ONLY`, `#!MACOS-ONLY`, `#!TVOS-ONLY`.


DOMAIN,reject.com,REJECT #!MACOS-ONLY
## Usage in Managed Profiles


Requirement expressions are lost when a profile is modified in the UI, so this feature is mainly used in managed profiles and enterprise profiles.

---
## Profile / Keystore

# Keystore


The `[Keystore]` section stores certificates and private keys used elsewhere in the profile. Other sections and policies reference a keystore item by its name, keeping the key material in one place.


[Keystore]
cert1 = type=p12, base64=<P12 base64 string here>, password=123456
key1 = type=openssh-private-key, base64=<base64 encoded private key file>
Each line defines one item: `name = key=value, key=value, ...`


#### type


Optional, `p12` or `openssh-private-key`


The item type. If omitted, an item with a `password` is treated as `p12`; an item without one is treated as `openssh-private-key`.


#### base64


Required, Base64 string


The Base64-encoded content of the certificate or key file: a PKCS#12 (.p12) file for `p12` items, or an OpenSSH private key file for `openssh-private-key` items.


#### password


Optional, string


The password of the PKCS#12 file.


## Client Certificate for TLS Proxy


A `p12` item can act as the client certificate of a TLS-based proxy, referenced with the `client-cert` parameter:


[Proxy]
Proxy = https, example.com, 443, client-cert=cert1

[Keystore]
cert1 = base64=<P12 base64 string here>, password=123456
See TLS parameters for details.


## MITM CA Certificate


A `p12` item can provide the CA certificate and key for HTTPS decryption, referenced with the `ca-keystore-name` parameter in the `[MITM]` section, as an alternative to the inline `ca-p12` parameter. See MITM.


## SSH Private Key


An `openssh-private-key` item provides the private key for an SSH policy, referenced with the `private-key` parameter:


[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, private-key=key1

[Keystore]
key1 = type=openssh-private-key, base64=[The base64 encoded content of the private key file]
You must Base64-encode the entire private key file again, even though the private key file uses Base64 encoding itself. RSA, ECDSA, ED25519, and DSA keys are supported; see the SSH policy page for details.

---
## Profile / Host List Parameter Type

# Host List Parameter Type


In Surge, many parameters use the Host List type to accommodate various complex needs, such as `force-http-engine-hosts` and `always-raw-tcp-hosts` in the [General] section, the `hostname` parameter of [MITM], and more.


A Host List parameter is a list separated by `,` and follows these rules:


- Use prefix `-` to exclude a hostname.

- Wildcard characters `*` and `?` are supported.

- Items in the list are matched in order. Once a match succeeds, matching stops. Therefore, items at the front have higher priority. When using the `-` prefix, write excluded hostnames at the front.

- If a port number is not provided, Surge automatically appends the standard port number for that parameter. For example, for the `force-http-engine-hosts` parameter, a bare hostname is only effective for port 80. For the MITM feature, it is only effective for port 443.

- Use suffix `:port` to match other ports.

- Use suffix `:0` to match all ports.

- Use `<ip-address>` to match all hostnames using an IPv4/IPv6 address directly instead of a domain.

- Use `<ipv4-address>` to match all hostnames using an IPv4 address directly instead of a domain.

- Use `<ipv6-address>` to match all hostnames using an IPv6 address directly instead of a domain.

- Use `<simple-hostname>` to match all hostnames without a dot.


Taking the `force-http-engine-hosts` parameter as an example:


- `-*.apple.com`: Excludes all requests sent to *.apple.com on port 80.

- `www.google.com`: Uses forced HTTP processing for www.google.com on port 80.

- `www.google.com:8080`: Uses forced HTTP processing for www.google.com on port 8080.

- `www.google.com:0`: Uses forced HTTP processing for www.google.com on all ports.

- `*:0`: Uses forced HTTP processing for all hostnames on all ports.

- `-<ip-address>`: Excludes all requests using an IPv4/IPv6 address directly.


## Example


When configuring the hostname list for MITM, if you want to decrypt all HTTPS connections but exclude well-known hostnames that cannot be decrypted due to certificate pinning, you can write it like this:


```
[MITM]
hostname = -*icloud*, -*.mzstatic.com, -*.facebook.com, -*.instagram.com, -*.twitter.com, -*dropbox*, -*apple*, -*.amazonaws.com, -<ip-address>, *

```

---
## Profile / General Section Options

# The [General] Section


The `[General]` section holds Surge's global settings: logging, DNS, the virtual network interface (VIF), proxy service listeners, remote control, connectivity testing, and traffic processing behavior. All keys are optional `key = value` lines; keys are case-insensitive.


[General]
loglevel = notify
dns-server = 223.5.5.5, 114.114.114.114
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, localhost, *.local
test-timeout = 5
This page lists every user-facing key. Some subjects have dedicated chapters with full details:


- DNS keys are covered in depth in the DNS chapter.

- MITM options live in the MITM section, not in `[General]`.

- Per-network overrides of some keys are available via Subnet Settings.


As the options change frequently, you may look up the most up-to-date explanation for the `[General]` section options within the app:


- Surge Mac: Main Window Menu -> Help -> Profile Syntax

- Surge iOS: More Tab -> Help -> Profile Syntax


Several keys take the Host List parameter type; see Host List Parameter Type for the matching rules.


## Common Parameters


Available on both Surge iOS and Surge Mac.


### Logging & Debugging


#### loglevel


Optional, `verbose` | `info` | `notify` | `warning`, default: `notify`


Log level. It is not recommended to enable `verbose` in daily use because it significantly affects performance.


#### debug-cpu-usage


Optional, Boolean, default: false


Enable CPU debug mode. This may slow down the performance. Intended for troubleshooting with the support team.


#### debug-memory-usage


Optional, Boolean, default: false


Enable memory debug mode. This may slow down the performance. Intended for troubleshooting with the support team.


### DNS


These keys configure Surge's DNS client. See the DNS chapter for how Surge resolves names and the Encrypted DNS page for DoH/DoQ/DoT details.


#### dns-server


Optional, comma-separated IP addresses (optionally `ip:port`), or `system`


The IP addresses of upstream DNS servers. The literal value `system` uses the system resolver. See DNS Servers for the full syntax.


If an encrypted DNS URL is found in this key, Surge automatically moves it to `encrypted-dns-server` when loading the profile (legacy support).


#### encrypted-dns-server


Optional, comma-separated URLs


The URLs of the encrypted DNS servers. If encrypted DNS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the encrypted DNS URL.


Supported protocols:


- DNS over HTTPS: `https://example.com`

- DNS over HTTP/3: `h3://example.com`

- DNS over QUIC: `quic://example.com`

- DNS over TLS: `tls://example.com`

- DNS over TCP: `tcp://example.com` &#x2014; plain, unencrypted DNS over TCP on port 53 by default; use it only with trusted servers.


The legacy key `doh-server` is accepted and rewritten to this key on save. See Encrypted DNS.


#### encrypted-dns-follow-outbound-mode


Optional, Boolean, default: false


By default, the encrypted DNS lookup uses the direct outbound. Enabling the option makes the encrypted DNS requests follow the outbound mode settings and rules. (Legacy key: `doh-follow-outbound-mode`.)


#### encrypted-dns-skip-cert-verification


Optional, Boolean, default: false


Skip the encrypted DNS server certificate verification, which is insecure. (Legacy key: `doh-skip-cert-verification`.)


#### allow-dns-svcb


Optional, Boolean, default: false


The iOS/macOS system might perform an SVCB record DNS lookup instead of a standard A record lookup. This causes Surge to fail to return a virtual IP address. So by default, the SVCB record lookup is forbidden to force the system to perform an A record lookup.


#### use-local-host-item-for-proxy


Optional, Boolean, default: false


By default, DNS lookup is always performed on the remote server if a proxy policy is used. After enabling this option, Surge uses the IP address instead of the domain to set up the proxy connection if the local DNS mapping result of the target domain exists. See Local DNS Mapping.


#### hijack-dns


Optional, comma-separated `ip[:port]` entries or `*[:port]`, default port: 53


By default, Surge only returns fake IP addresses for DNS queries sent to the Surge DNS address (`198.18.0.2`). Queries sent to a standard DNS server are forwarded.


Some devices or software always use a hardcoded DNS server. (For example, Google Speakers always use 8.8.8.8.) You may use this option to hijack the query to get a fake address. Each entry is either an IPv4 address (optionally with a port) or `*`; use `hijack-dns = *:53` to hijack all DNS queries.


The fake DNS responder listens on `198.18.0.2` (IPv4) and `fd00:6152::2` (IPv6), so even pure IPv6 networks can point their clients to Surge. See Advanced DNS Topics.


#### always-real-ip


Optional, Host List


This option asks Surge to return a real IP address instead of a fake IP address when Surge VIF handles a DNS question. The DNS packet is forwarded to upstream DNS servers.


This parameter is of the Host List type; for detailed rules see Host List Parameter Type. See also Advanced DNS Topics.


### GeoIP Database


See IP-Based Rules for how the GeoIP database is used.


#### geoip-maxmind-url


Optional, URL


The URL of the GeoIP database for updating.


#### disable-geoip-db-auto-update


Optional, Boolean, default: false


Disable the auto-updating for the GeoIP database.


### IPv6 & Virtual Network Interface


See Enhanced Mode for the VIF concept.


#### ipv6


Optional, Boolean, default: false


Enable full IPv6 support. After enabling this option, Surge queries AAAA records when accessing domain names. Even if this option is not enabled, you can still access IPv6 sites by using IPv6 addresses directly. Enabling it may increase DNS latency; turn it on only when needed.


#### ipv6-vif


Optional, `disabled` | `auto` | `always`, default: `disabled`


Allow IPv6 through Surge VIF. Useful when you want Surge to handle raw TCP connections connecting to IPv6 addresses.


- `disabled`: Never set up the Surge VIF with IPv6. (The legacy value `off` is also accepted.)

- `auto`: Only set up the Surge VIF with IPv6 if the local network has a valid IPv6 network.

- `always`: Always set up the Surge VIF with IPv6. This may break apps on networks without IPv6 connectivity, and Surge warns about it during profile verification.


#### tun-excluded-routes


Optional, comma-separated IPv4/IPv6 CIDRs


Surge VIF can only process TCP, UDP, and ICMP protocols. Use this option to bypass specific IP ranges to allow all traffic to pass through.


Notice: This option only works for Surge VIF. Requests handled by Surge Proxy Server aren't affected. Combine `skip-proxy` and `tun-excluded-routes` to make sure that specific traffic bypasses Surge.


IPv6 CIDR blocks are supported when IPv6 VIF is enabled.


#### tun-included-routes


Optional, comma-separated IPv4/IPv6 CIDRs


By default, the Surge VIF interface declares itself as the default route. However, since the Wi-Fi interface has a smaller route, some traffic may not go through the Surge VIF interface. Use this option to add a smaller route.


Avoid listing private ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) here; it is normally unnecessary and can cause system issues.


IPv6 CIDR blocks are supported when IPv6 VIF is enabled.


#### icmp-forwarding iOS 5.14.3+ Mac 5.10.0+


Optional, Boolean, default: true


When the enhanced mode is enabled, to reduce interference with users, Surge will directly forward all ICMP packets so as not to affect the use of tools like ping.


However, this may lead to IP leakage for some users who are extremely privacy-conscious. Disable this option to stop ICMP forwarding; ping will no longer work through Surge.


### System Proxy Bypass


#### skip-proxy


Optional, Host List


In the iOS version, this option forces connections to these domain/IP ranges to be handled by Surge VIF instead of Surge proxy. In the macOS version, these settings are applied to the system when "Set as System Proxy" is enabled. This option is used to fix compatibility problems with some apps; it is not a way to keep requests off a proxy policy.


- To specify a single domain, enter the domain name - for example, apple.com.

- To specify all websites on a domain, use an asterisk before the domain name - for example, `*apple.com`.

- To specify a specific part of a domain, specify each part - for example, store.apple.com.

- To specify hosts or networks by IP addresses, enter a specific IP address such as 192.168.2.11 or an address range, such as `192.168.2.*` or 192.168.2.0/24.


Notice: If you enter an IP address or address range, you are only able to bypass the proxy when you connect to that host using that address, not when you connect to the host by a domain name that resolves to that address.


For the general matching rules see Host List Parameter Type.


#### exclude-simple-hostnames


Optional, Boolean, default: false


Just like the `skip-proxy` parameter. This option lets requests using simple hostnames (without a dot) be handled by Surge VIF instead of Surge proxy.


### Proxy Services & Remote Access


#### proxy-restricted-to-lan iOS 5.13.1+ Mac 5.8.1+


Optional, Boolean, default: true


#### gateway-restricted-to-lan iOS 5.13.1+ Mac 5.8.1+


Optional, Boolean, default: true


It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. Both are enabled by default.


#### external-controller-access


Optional, `key@ip:port`


This option allows an external controller to control Surge, such as Surge Dashboard (macOS) and Surge iOS Remote Controller (iOS). E.g.: `key@0.0.0.0:6165`. See Dashboard.


#### http-api


Optional, `key@ip:port`


This option allows using HTTP APIs to control Surge. E.g.: `key@0.0.0.0:6166`. See HTTP API.


#### http-api-tls


Optional, Boolean, default: false


Use HTTPS protocol instead of HTTP for the HTTP API. The MITM CA certificate must be configured first. You need to install the certificate on the client's device manually.


#### http-api-web-dashboard


Optional, Boolean, default: false


You may control Surge via a web browser after enabling this. The web dashboard is served on the `http-api` listener.


### Connectivity Testing


See Testing for latency and throughput testing details, and Common Policy Parameters for per-policy overrides.


#### internet-test-url


Optional, HTTP URL, default: `http://bing.com/`


The URL for the Internet connectivity testing. Also, the testing URL for the DIRECT policy.


#### proxy-test-url


Optional, HTTP URL, default: `http://bing.com/`


The default testing URL for proxy policies.


#### test-timeout


Optional, in seconds, default: 5


The default connectivity testing timeout for proxy policies. (Tests for the DIRECT policy use a 10-second timeout.)


#### proxy-test-udp


Optional, `hostname@ipv4`


The default UDP test parameter for proxies. E.g.: `apple.com@8.8.8.8`. The test query is sent to the given IPv4 address on port 53.


### Traffic Processing


#### force-http-engine-hosts


Optional, Host List


Make Surge treat TCP connections as HTTP requests. The Surge HTTP engine processes the requests, and advanced features such as capture, rewrite, and scripting become available. See HTTP Processing Overview.


By default, only connections on port 80 are matched. Append `:port` to match another port, `host:0` to match all ports of a host, or `*:0` to match everything. Prefix an entry with `-` to exclude it.


This parameter is of the Host List type; for detailed rules see Host List Parameter Type.


#### always-raw-tcp-hosts iOS 5.8.0+ Mac 5.4.0+


Optional, Host List


Surge will automatically sniff the protocol for TCP requests sent to ports 80 and 443, enabling advanced HTTP/HTTPS features while optimizing performance. However, this may cause some compatibility issues. If you encounter problems, you can add the hostname here, and Surge will not sniff these requests' protocols.


This parameter is of the Host List type; for detailed rules see Host List Parameter Type.


#### always-raw-tcp-keywords Mac 5.5.0+


Optional, comma-separated keywords


Behaves similar to `always-raw-tcp-hosts` but matches by substring rather than a host list. Any hostname containing one of the keywords will skip protocol sniffing and stay in raw TCP mode, which helps when the exact hostname is not predictable.


#### udp-policy-not-supported-behaviour


Optional, `REJECT` | `DIRECT`, default: `REJECT`


The fallback behavior when UDP traffic matches a policy that doesn't support UDP relay. Starting from Surge Mac 6.0.0, the default is `REJECT` to avoid leaking traffic unknowingly. See UDP Relay.


#### udp-priority


Optional, Boolean, default: true


When enabled, Surge prioritizes UDP packets when the system load is very high and packet processing is delayed. Also known as game mode.


#### block-quic iOS 5.14.6+ Mac 5.10.3+


Optional, `per-policy` | `all-proxy` | `all` | `always-allow`, default: `per-policy`


This parameter is used to globally override the behavior of whether to block QUIC traffic:


- `per-policy`: Determined by each policy's `block-quic` parameter. This is the default value.

- `all-proxy`: Overrides the proxy policies' `block-quic` parameter, blocking all QUIC traffic through proxies.

- `all`: Overrides all policies' `block-quic` parameters, blocking everything including DIRECT policies.

- `always-allow`: Overrides the proxy policies' `block-quic` parameter, allowing everything.


See the per-policy `block-quic` parameter.


### Error Pages


#### show-error-page Mac 5.8.0+


Optional, Boolean, default: true


Controls whether Surge displays its built-in HTTP error page when a request fails (for example, because a policy rejects it or a proxy cannot be reached). Set it to `false` if you prefer the client to receive the raw network error instead of the Surge error page.


#### show-error-page-for-reject


Optional, Boolean, default: false


Show an error webpage for the REJECT policy if the request is a plain HTTP request.


## Surge iOS Only Parameters


### Working Mode


#### compatibility-mode


Optional, integer 0&#x2013;5, default: 0


This option is used to control the working mode of Surge iOS.


- 0: Auto. In versions of Surge iOS prior to 5.8.0 this is equivalent to 1; from 5.8.0 it is equivalent to 3.

- 1: Proxy Takeover + VIF. In this mode, proxy takeover has higher priority than VIF takeover, offering the best performance, but some apps may check for proxy settings and refuse to work.

- 2: Proxy Takeover Only.

- 3: VIF Takeover Only. The default working mode of the latest version.

- 4: Proxy Takeover + VIF, but the proxy uses the VIF address instead of the loopback address.

- 5: VIF Takeover Only, but the VIF routing uses multiple smaller routes for takeover and does not configure a default route. Can be used to bypass some special issues (e.g., HomeKit Secure Camera).


#### auto-suspend iOS 5.11.0+


Optional, Boolean, default: true


Automatically suspend Surge iOS when a network taken over by a Surge Mac gateway is detected.


### Sharing Proxy Services over LAN


#### allow-wifi-access


Optional, Boolean, default: false


Allow Surge proxy services access from other devices in the LAN.


#### allow-hotspot-access


Optional, Boolean, default: false


Allow Surge proxy services access from other devices while Personal Hotspot is on.


#### wifi-access-http-port


Optional, port number, default: 6152


The port number of the Surge HTTP proxy service.


#### wifi-access-socks5-port


Optional, port number, default: 6153


The port number of the Surge SOCKS5 proxy service.


#### wifi-access-http-auth


Optional, `username:password`


Require authentication for the Surge HTTP proxy service. E.g.: `username:password`


### Network Behavior


#### wifi-assist


Optional, Boolean, default: false


Enable Wi-Fi Assist: set up connections with cellular data when the Wi-Fi network performs poorly.


#### all-hybrid


Optional, Boolean, default: false


Instead of setting up connections with cellular data when the Wi-Fi network is poor, always set up connections with Wi-Fi and cellular data simultaneously.


This option can improve the network experience significantly on a poor Wi-Fi network or when the Wi-Fi network is switching.


This feature applies to all TCP connections and DNS lookups. Only enable it if you have an unlimited cellular data plan.


#### hide-vpn-icon


Optional, Boolean, default: false


Hide the VPN icon in the status bar. It may cause system issues during network switching; use with caution.


### VPN Tunnel Scope


#### include-all-networks


Optional, Boolean, default: false


By default, some requests might not be taken over by Surge. For example, apps can bind to the physical network interface to bypass Surge VIF. Enable the Include All Networks option to make sure all requests are handled by Surge without leaking. This option is useful when you use Surge as a firewall. (Requires iOS 14.0 or above.)


Enabling this option may cause AirDrop and Xcode debugging issues, Surge Dashboard via USB not working, and other unexpected side effects. Use with caution.


#### include-local-networks


Optional, Boolean, default: false


Enable this option to make Surge VIF handle requests sent to LAN. (Requires iOS 14.2 or above.)


Enabling this option may cause AirDrop and Xcode debugging issues, Surge Dashboard via USB not working, and other unexpected side effects. Use with caution.


Must be used in conjunction with `include-all-networks=true`.


#### include-apns


Optional, Boolean, default: false


Enable this option to make Surge VIF handle network traffic for the Apple Push Notification service (APNs).


Must be used in conjunction with `include-all-networks=true`.


#### include-cellular-services


Optional, Boolean, default: false


Enable this option to make Surge VIF handle internet-routable network traffic for cellular services (VoLTE, Wi-Fi Calling, IMS, MMS, Visual Voicemail, etc.).


Note that some cellular carriers route cellular services traffic directly to the carrier network, bypassing the internet. Such cellular services traffic is always excluded from the tunnel.


Must be used in conjunction with `include-all-networks=true`.


## Surge Mac Only Parameters


#### http-listen


Optional, comma-separated listener strings `[password@]address[:port]`, default port: 6152


The HTTP proxy service listen parameter. E.g.: `0.0.0.0:6152`. The address must be an IP literal (wrap an IPv6 address in `[...]` when a port is present). The port may be omitted, in which case 6152 is used. Multiple comma-separated listeners are allowed. The proxy service is off when neither `http-listen` nor `socks5-listen` is set.


The legacy keys `interface` + `port` are accepted and migrated to this key on save.


#### socks5-listen


Optional, comma-separated listener strings `address[:port]`, default port: 6153


The SOCKS5 proxy service listen parameter. E.g.: `0.0.0.0:6153`. Same syntax as `http-listen`, except that a password component is not allowed because the SOCKS5 service does not support authentication.


The legacy keys `socks-interface` + `socks-port` are accepted and migrated to this key on save.


#### set-system-socks-proxy


Optional, Boolean, default: true


When "Set as System Proxy" is enabled, also configure the system SOCKS proxy setting, in addition to the system HTTP/HTTPS proxy settings.


#### read-etc-hosts


Optional, Boolean, default: true


Follow local DNS mapping items in `/etc/hosts`. See Local DNS Mapping.


#### subnet-exp-wifi-always-match


Optional, Boolean, default: true


When enabled, SSID/BSSID subnet expression patterns still match even when Wi-Fi is not the primary network interface. Disable it to make these patterns match only when Wi-Fi is the primary interface.


This key replaces the legacy `use-default-policy-if-wifi-not-primary` key, which is accepted and migrated with its meaning inverted.

---
## Rules / Overview

# Rules Overview


Surge decides how to handle every request by testing it against the rule list in the `[Rule]` section of the profile. Each rule pairs a matching condition with a policy: forward the request to a proxy, connect directly, or reject it.


[Rule]
DOMAIN-SUFFIX,company.com,ProxyA
DOMAIN-KEYWORD,google,DIRECT
GEOIP,US,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
FINAL,ProxyB
## Composition


Each rule consists of three parts: a rule type, a value to match, and a policy.


           TYPE,          VALUE,          POLICY
Example:   DOMAIN-SUFFIX, apple.com,      DIRECT
           IP-CIDR,       192.168.0.0/16, ProxyA

- TYPE: one of the rule types listed in the index below.

- VALUE: what the rule matches against. The `FINAL` rule has no value. If a value contains commas (e.g. a regex), wrap it in double or single quotes.

- POLICY: the name of a proxy policy, a policy group, a built-in policy such as `DIRECT` or the REJECT family, or a `DEVICE:<name>` policy targeting a Surge Ponte device.


Optional parameters may be appended after the policy, separated by commas:


IP-CIDR,192.168.0.0/16,DIRECT,no-resolve
Inline comments starting with `//`, `#`, or `;` are allowed at the end of a rule line.


The rule list must end with an enabled FINAL rule, which defines the default policy for requests that match nothing else.


## Evaluation Order


Rules are evaluated strictly from top to bottom. The first rule that matches decides the policy; all later rules are ignored. Order your rules from most specific to most general.


Two things bypass the normal top-to-bottom evaluation:


- Rules tagged with `pre-matching` are extracted and checked before everything else (see Pre-matching).

- When the outbound mode is set to Direct or Global instead of Rule-Based, the rule list is not consulted at all.


## Rules and DNS


Domain-based rules only inspect the requested hostname, so they never require a DNS lookup. IP-based rules (`IP-CIDR`, `IP-CIDR6`, `GEOIP`, `IP-ASN`) match against the resolved IP address:


- If the request already targets an IP literal, IP-based rules match it directly, and `GEOIP`/`IP-ASN` look it up without a DNS query.

- If the request targets a domain, evaluation pauses at the first IP-based rule, Surge performs the DNS lookup, and evaluation resumes at the same rule. The result is cached, so at most one lookup is performed per request.

- With the `no-resolve` parameter, an IP-based rule is simply skipped for requests whose address has not been resolved, instead of triggering a lookup.


If the DNS lookup fails, rule evaluation aborts and the request fails with a DNS error &#x2014; unless the FINAL rule carries the dns-failed parameter, in which case the FINAL policy is used instead.


Place domain-based rules before IP-based rules. Requests decided by a domain rule skip DNS resolution entirely, which reduces latency and avoids failures for domains that cannot be resolved locally.


## Pre-matching


Normally a rule decision happens only after Surge receives the first packet of a connection. Rules tagged with `pre-matching` and using a REJECT-family policy are additionally evaluated at the DNS-query and TCP-handshake stages, so unwanted requests are rejected with minimal overhead:


DOMAIN,ad.example.com,REJECT,pre-matching
Pre-matched rules have the highest priority. Only certain rule types support the tag, and the policy must be one of the REJECT family. See REJECT Policy for the full behavior details and the list of supported types.


## Rule Parameters


The following optional parameters can be appended to rule lines. Each rule page documents the parameters relevant to its types in detail.


[TABLE]


|
Parameter |
 Form |
 Applies to |
 Effect |
 |


|
 `no-resolve` |
 flag |
 IP-CIDR, IP-CIDR6, GEOIP, IP-ASN, RULE-SET, DOMAIN-SET |
 Skip the rule for unresolved domain requests instead of triggering a DNS lookup. On RULE-SET, applies to every sub-rule. |
 |

|
 `dns-failed` |
 flag |
 FINAL only |
 Use the FINAL policy when a DNS lookup fails during rule evaluation. |
 |

|
 `extended-matching` |
 flag |
 DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-WILDCARD, URL-REGEX, RULE-SET, DOMAIN-SET |
 Also match the TLS SNI and the HTTP Host header (or `:authority`). On RULE-SET/DOMAIN-SET, applies to every entry. |
 |

|
 `pre-matching` |
 flag |
 Domain types, IP types, SRC-IP, DEST-PORT, SRC-PORT, SUBNET, CELLULAR-CARRIER, CELLULAR-RADIO, logical rules, RULE-SET, DOMAIN-SET |
 Evaluate the rule in the pre-matching phase. Top-level rules only; the policy must be a REJECT-family policy. See REJECT Policy. |
 |

|
 `notification-text=<text>` |
 key=value |
 Any rule, including FINAL |
 Post a user notification with the given text when the rule matches. |
 |

|
 `notification-interval=<seconds>` |
 key=value |
 Any rule, including FINAL |
 Minimum interval between notifications for the same rule. Default: 300 seconds. |
 |

|
 `update-interval=<seconds>` |
 key=value |
 RULE-SET, DOMAIN-SET |
 Re-download interval for the external resource. Default: 86400 (24 hours). A negative value disables auto-updating. |
 |

|
 `requires-resolve` |
 flag |
 SCRIPT only |
 Perform a DNS lookup before running the rule script, so the script can access the resolved addresses. |
 |

|
 `always-capture=<session-name>` |
 key=value |
 Any rule, including FINAL |
 Force-enable HTTP capture for connections matched by the rule, recorded under the named capture session. Intended for debugging. |
 |


[/TABLE]
Unknown parameters are silently ignored.


### notification-text and notification-interval


Use these parameters to get notified when a specific rule fires:


DOMAIN-SUFFIX,example.com,Proxy,notification-text=Example matched,notification-interval=600
Notifications for the same rule are throttled to one per `notification-interval` seconds (default 300).


## Rule Type Index


[TABLE]


|
Type |
 Matches |
 Page |
 |


|
 `DOMAIN` |
 Exact hostname |
 Domain Rules |
 |

|
 `DOMAIN-SUFFIX` |
 Hostname and its subdomains |
 Domain Rules |
 |

|
 `DOMAIN-KEYWORD` |
 Hostname containing a substring |
 Domain Rules |
 |

|
 `DOMAIN-WILDCARD` |
 Hostname against a wildcard pattern |
 Domain Rules |
 |

|
 `DOMAIN-SET` |
 Hostname against an external domain list |
 Domain Rules |
 |

|
 `IP-CIDR` |
 IPv4 address range |
 IP Rules |
 |

|
 `IP-CIDR6` |
 IPv6 address range |
 IP Rules |
 |

|
 `GEOIP` |
 Country of the destination IP |
 IP Rules |
 |

|
 `IP-ASN` |
 Autonomous system number of the destination IP |
 IP Rules |
 |

|
 `USER-AGENT` |
 HTTP User-Agent header |
 HTTP Rules |
 |

|
 `URL-REGEX` |
 Request URL against a regex |
 HTTP Rules |
 |

|
 `PROCESS-NAME` |
 Originating process (Mac only) |
 Process Rules |
 |

|
 `DEST-PORT` |
 Destination port |
 Source and Port Rules |
 |

|
 `SRC-PORT` |
 Client source port |
 Source and Port Rules |
 |

|
 `IN-PORT` |
 Surge listen port the request arrived on |
 Source and Port Rules |
 |

|
 `SRC-IP` |
 Client IP address |
 Source and Port Rules |
 |

|
 `DEVICE-NAME` |
 Client device name |
 Source and Port Rules |
 |

|
 `MAC-ADDRESS` |
 Client MAC address |
 Source and Port Rules |
 |

|
 `PROTOCOL` |
 Connection protocol |
 Protocol and Network Rules |
 |

|
 `HOSTNAME-TYPE` |
 Form of the hostname (domain/IP literal) |
 Protocol and Network Rules |
 |

|
 `SUBNET` |
 Current network (SSID, BSSID, router, type) |
 Protocol and Network Rules |
 |

|
 `CELLULAR-RADIO` |
 Current cellular radio technology (iOS only) |
 Protocol and Network Rules |
 |

|
 `CELLULAR-CARRIER` |
 Current cellular carrier (iOS only) |
 Protocol and Network Rules |
 |

|
 `AND` |
 All sub-rules match |
 Logical Rules |
 |

|
 `OR` |
 Any sub-rule matches |
 Logical Rules |
 |

|
 `NOT` |
 Sub-rule does not match |
 Logical Rules |
 |

|
 `SCRIPT` |
 Result of a JavaScript rule script |
 Script Rules |
 |

|
 `RULE-SET` |
 A bundle of rules from a file, URL, or inline section |
 Rule Sets |
 |

|
 `FINAL` |
 Everything (default policy) |
 Final Rule |
 |


[/TABLE]

---
## Rules / Domain Rules

# Domain Rules


Domain rules match the hostname of a request. They are the most common rule types and never trigger a DNS lookup, so they should generally be placed before IP rules.


[Rule]
DOMAIN,www.apple.com,Proxy
DOMAIN-SUFFIX,apple.com,DIRECT
DOMAIN-KEYWORD,google,Proxy
## Matching Semantics


All domain rule types test the hostname of the request. Matching is case-insensitive, and a trailing root dot in the hostname (`example.com.`) is ignored.


By default only the requested hostname is tested. With the extended-matching parameter described below, the TLS SNI and the HTTP Host header are tested as well.


## Rule Types


#### DOMAIN


DOMAIN,www.apple.com,Proxy
Matches if the hostname equals the value exactly.


#### DOMAIN-SUFFIX


DOMAIN-SUFFIX,apple.com,Proxy
Matches the domain itself and all of its subdomains. For example, `DOMAIN-SUFFIX,google.com` matches `google.com`, `www.google.com`, and `mail.google.com`, but does not match `content-google.com`.


#### DOMAIN-KEYWORD


DOMAIN-KEYWORD,google,Proxy
Matches if the hostname contains the value as a substring. Wildcard characters are not interpreted; the value is treated literally.


#### DOMAIN-WILDCARD


DOMAIN-WILDCARD,api-*.example.com,Proxy
Matches the hostname against a wildcard pattern:


- `*` matches any number of characters, including none. It also crosses dots, so `*.example.com` matches `a.b.example.com`.

- `?` matches exactly one character.

- `[...]` character classes are supported.


Matching is case-insensitive. Use `DOMAIN-WILDCARD` when `DOMAIN-SUFFIX` and `DOMAIN-KEYWORD` are not precise enough, e.g. to match a naming pattern like `cdn?.example.com`.


#### DOMAIN-SET


DOMAIN-SET,https://example.com/adblock.txt,REJECT
DOMAIN-SET,my-domains.txt,Proxy
Matches the hostname against an external list of domains. Designed for very large lists (such as ad-blocking lists): sets are preprocessed into an index that supports fast lookup for hundreds of thousands of entries. A single set may contain up to 1,000,000 entries.


The value is either a URL (`http://` or `https://`) or a local file path, absolute or relative to the profile directory.


### DOMAIN-SET File Format


The file is plain text with one entry per line:


# Exact hostname
example.com

# Leading dot: matches ads.example.org and all of its subdomains
.ads.example.org

- A plain line matches the hostname exactly, like a `DOMAIN` rule.

- A line starting with `.` matches the domain itself and all subdomains, like a `DOMAIN-SUFFIX` rule.

- Lines starting with `#` or `//` are comments; blank lines are ignored.

- Invalid lines are skipped with a warning; they do not invalidate the set.


The `DOMAIN-SET` line accepts the `update-interval=<seconds>` parameter to control how often a URL-based set is re-downloaded (default 86400 seconds; a negative value disables auto-updating). Local files are watched and reloaded automatically when changed.


If you need to mix domain entries with other rule types in one external file, use RULE-SET instead. The same URL or file cannot be used both as a RULE-SET and as a DOMAIN-SET in one profile.


## Parameters


#### extended-matching iOS 5.8.0+ Mac 5.4.0+


DOMAIN-SUFFIX,example.com,Proxy,extended-matching
When this parameter is enabled, the rule also tries to match the TLS SNI and the HTTP Host header (or `:authority`). This helps when a client connects to an IP address directly, so the requested hostname alone would not reveal the destination domain.


The parameter is available for `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD`, and `DOMAIN-WILDCARD` rules. To apply it to every entry of a set, append the parameter to the corresponding `DOMAIN-SET` or `RULE-SET` line.


#### pre-matching iOS 5.14.0+ Mac 5.9.0+


All domain rule types support the `pre-matching` parameter with REJECT-family policies, allowing requests to be rejected at the DNS and TCP-handshake stages. See REJECT Policy.

---
## Rules / IP Rules

# IP Rules


IP rules match the destination IP address of a request. There are four IP-based rule types: `IP-CIDR`, `IP-CIDR6`, `GEOIP`, and `IP-ASN`.


[Rule]
IP-CIDR,192.168.0.0/16,DIRECT
GEOIP,US,DIRECT
IP-ASN,13335,Proxy
## IP Rules and DNS


IP rules need a resolved address to work:


- If the request targets an IP literal, the rule matches it directly; `GEOIP` and `IP-ASN` perform their database lookup without a DNS query.

- If the request targets a domain, Surge performs a DNS lookup when evaluation reaches the first IP-based rule, then resumes evaluation with the result. `IP-CIDR` and `GEOIP`/`IP-ASN` lookups test the first IPv4 record of the result (falling back to the IPv6 record for `GEOIP`/`IP-ASN`); `IP-CIDR6` tests the first IPv6 record.

- If the DNS lookup fails, rule evaluation aborts and the request fails with a DNS error, unless the FINAL rule carries the dns-failed parameter.


To avoid the lookup, append the no-resolve parameter.


## Rule Types


#### IP-CIDR


IP-CIDR,192.168.0.0/16,DIRECT
IP-CIDR,10.0.0.0/8,DIRECT
IP-CIDR,172.16.0.0/12,DIRECT
IP-CIDR,127.0.0.0/8,DIRECT
Matches if the destination IPv4 address falls in the specified range.


Since Surge Mac 6.0.0, you may also provide a single IPv4 address without the `/` mask. It is treated as `/32`:


IP-CIDR,8.8.8.8,Proxy
#### IP-CIDR6


```
IP-CIDR6,2001:db8:abcd:8000::/50,DIRECT

```

Matches if the destination IPv6 address falls in the specified range.


Single IPv6 addresses are supported too &#x2014; writing `IP-CIDR6,2404:6800::`, for example, is equivalent to `/128`.


#### GEOIP


GEOIP,US,DIRECT
Matches if the destination IP address belongs to the specified country, according to the GeoIP database. The value is an ISO country code and is case-insensitive.


#### IP-ASN


IP-ASN,13335,Proxy
Matches if the destination IP address belongs to the specified autonomous system. The value is a decimal ASN; an `AS` prefix is also accepted (`IP-ASN,AS13335,Proxy`).


## Parameters


#### no-resolve


GEOIP,US,DIRECT,no-resolve
IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
With this parameter, the rule is skipped for requests targeting a domain whose address has not been resolved yet, instead of triggering a DNS lookup. The rule still matches requests that target IP literals.


If some domains cannot be resolved by the local DNS server, make sure no IP-based rule without `no-resolve` appears before the rule that matches those domains. Otherwise rule evaluation fails with a DNS error. Adding `no-resolve` to the IP-based rules, or adding dns-failed to the FINAL rule, avoids the issue.


#### pre-matching iOS 5.14.0+ Mac 5.9.0+


All four IP rule types support the `pre-matching` parameter with REJECT-family policies. See REJECT Policy.


## GeoIP and ASN Databases


#### GeoIP country database


`GEOIP` rules use a MaxMind GeoLite2 country database. A copy is bundled with Surge, and Surge periodically downloads updates. Two `[General]` settings control this (see General Settings):


- `geoip-maxmind-url`: the download URL for database updates. The default is `https://nssurge.com/resource/geoip-database.tar.gz`. You may point it to another source; both a `.tar.gz` archive containing `GeoLite2-Country.mmdb` and a raw `.mmdb` file are accepted.

- `disable-geoip-db-auto-update`: set to `true` to disable automatic updates. You can still update the database manually from the app UI.


#### ASN database


`IP-ASN` rules use a bundled GeoLite2 ASN database, which is updated together with app updates. There is no configuration key for it and no separate download mechanism.

---
## Rules / HTTP Rules

# HTTP Rules


HTTP rules match properties of an HTTP request: the User-Agent header and the request URL. They only take effect for requests processed by Surge's HTTP engine; plain TCP or UDP connections are never matched by these rules.


[Rule]
USER-AGENT,Instagram*,Proxy
URL-REGEX,^http://example\.com/api/,DIRECT
## When HTTP Rules Apply


A request is visible to HTTP rules only when the HTTP engine handles it and the relevant property is available:


- Plain HTTP requests handled by the HTTP engine expose both the URL and the User-Agent header. This includes requests sent to Surge's HTTP proxy port and TCP connections forced into HTTP processing with `force-http-engine-hosts`.

- HTTPS requests expose their full URL and headers only when MITM decryption is enabled for the hostname.

- For HTTPS requests that are not decrypted, no URL is available, so `URL-REGEX` cannot match. `USER-AGENT` can only match if the client happens to send a User-Agent header in the proxy CONNECT request.


See HTTP Processing Overview for how traffic reaches the HTTP engine.


## Rule Types


#### USER-AGENT


USER-AGENT,Instagram*,DIRECT
Matches if the User-Agent header of the request matches the value. Wildcard characters `*` and `?` are supported. Matching is case-sensitive.


#### URL-REGEX


URL-REGEX,^http://google\.com,DIRECT
Matches if the complete request URL matches the regular expression. The rule matches when the pattern is found anywhere in the URL; anchor with `^` when you want a prefix match. The regular expression is case-sensitive.


For plain HTTP requests the tested string is the full URL, e.g. `http://example.com/path?query`. For HTTPS requests with MITM enabled, it is the decrypted URL, e.g. `https://example.com/path?query`.


If the value contains commas, wrap it in double quotes:


URL-REGEX,"^http://example\.com/(a|b),?c",Proxy
extended-matching
You can append the `extended-matching` parameter to also test URL variants in which the host part is replaced by the TLS SNI and by the HTTP Host header (or `:authority`), which helps when the request targets an IP address or the Host differs from the URL host:


```
URL-REGEX,^https://example\.com,Proxy,extended-matching

```

---
## Rules / Process Rules

# Process Rules


You may assign a policy to requests from a specific process. Process rules are available on Surge Mac only; Surge iOS ignores these rules.


[Rule]
PROCESS-NAME,Telegram,Proxy
#### PROCESS-NAME Mac Only


Matches the executable of the process that originated the request. The rule expression supports three matching modes, selected by the shape of the value:


- Filename Mode


 If the expression does not start with `/`, it matches only the executable file name, regardless of its path.


 Wildcards `*` and `?` are supported. For example: `PROCESS-NAME,Google*`


- Full Path Mode


 If the expression starts with `/` (and does not end with `/`), it matches the executable's full absolute path.


 Wildcards `*` and `?` are supported in this mode as well. For example: `PROCESS-NAME,/usr/bin/ssh` or `PROCESS-NAME,/Applications/*.app/Contents/MacOS/*`


- App Bundle Mode Mac 6.0.0+


 If the expression starts with `/` and also ends with `/`, the executable path is matched by prefix.


 This mode is particularly useful for application bundles that contain multiple executables. For example: `PROCESS-NAME,/Applications/ChatGPT.app/`


Matching is case-sensitive in all modes.


Process rules do not support the `pre-matching` parameter, since the originating process is not known at the DNS-query stage.

---
## Rules / Source and Port Rules

# Source and Port Rules


These rule types match where a request comes from &#x2014; the client's address, port, device name, or MAC address &#x2014; and which ports are involved. Port rules are useful on any setup; source-based rules matter mainly when other devices send traffic through Surge.


[Rule]
DEST-PORT,22,DIRECT
SRC-IP,192.168.20.0/24,Proxy
DEVICE-NAME,Kids-iPad,REJECT
## When Source-Based Rules Make Sense


Requests originating from apps on the local device all share the same local source, so `SRC-IP`, `DEVICE-NAME`, and `MAC-ADDRESS` are only meaningful when Surge handles traffic from other devices:


- Surge Mac running in Gateway Mode as the router for a LAN.

- LAN devices using Surge as their HTTP or SOCKS5 proxy.

- Devices with names assigned by the built-in DHCP server.

- Remote devices connected through Surge Ponte.


Use them to apply different policies per device, for example giving a set-top box a dedicated proxy or blocking traffic from a specific device.


## Port Expressions


`DEST-PORT`, `SRC-PORT`, and `IN-PORT` share the same value grammar:


- A plain port number: `IN-PORT,6153`

- A closed range: `DEST-PORT,10000-20000`

- The operators `>`, `<`, `>=`, `<=`: `SRC-PORT,>=50000` iOS 5.8.4+ Mac 5.4.4+


## Rule Types


#### DEST-PORT


DEST-PORT,80-81,DIRECT
Matches if the destination port of the request matches.


#### SRC-PORT iOS 5.8.4+ Mac 5.4.4+


SRC-PORT,>=50000,DIRECT
Matches if the client's source port number matches.


#### IN-PORT


IN-PORT,6152,DIRECT
Matches if the Surge listen port that accepted the request matches. Useful when Surge listens on multiple ports and you want different behavior per port.


#### SRC-IP


SRC-IP,192.168.20.100,DIRECT
Matches if the client IP address of the request matches. Both IPv4 and IPv6 addresses are supported.


The value may also be a CIDR range:


SRC-IP,192.168.20.0/24,DIRECT
A single address matches exactly; a CIDR value matches any client address in the range.


#### DEVICE-NAME


DEVICE-NAME,Kids-iPad,REJECT
Matches if the client's device name matches. Wildcard characters `*` and `?` are supported; matching is case-sensitive.


- For Surge Ponte access, the device name is the device name configured in the client device's system settings.

- If Surge DHCP is enabled, LAN devices can be matched by the custom device name shown in the device view.


#### MAC-ADDRESS Mac 6.1.0+


MAC-ADDRESS,A4:83:E7:11:22:33,Proxy
Matches the MAC address of the accessing device. This only works for devices on the same local area network; if the request was forwarded by a gateway, the MAC address cannot be obtained.

---
## Rules / Protocol and Network Rules

# Protocol and Network Rules


These rule types match on properties of the connection itself or the network environment, rather than the destination: the connection protocol, the form of the hostname, the current cellular network, and the current Wi-Fi or wired network. Use them to route traffic differently depending on how the request was made or where the device currently is.


PROTOCOL,STUN,REJECT
SUBNET,SSID:MyHome,DIRECT
FINAL,Proxy
## PROTOCOL


Rule matches if the protocol of the request matches. The accepted values are `HTTP`, `HTTPS`, `TCP`, `UDP`, `QUIC`, `STUN`, `MTProto`, `DOH`, `DOH3`, `DOQ`, `DOT`, and `DNS`.


PROTOCOL,HTTP,DIRECT
The comparison is case-sensitive; write the keywords exactly as listed above.


Two keywords act as umbrella matchers:


- `PROTOCOL,TCP` also matches HTTP, HTTPS, and MTProto connections, so a single rule can cover all TCP-based traffic.

- `PROTOCOL,UDP` also matches QUIC and STUN connections.


Use `MTProto` to match connections accepted by the built-in MTProto proxy server. iOS 5.21.0+ Mac 6.8.0+


PROTOCOL,MTProto,Proxy

- Due to the existence of multiple draft versions of QUIC, not all QUIC traffic can be recognized by Surge.

- STUN detection is available for filtering P2P traffic; `PROTOCOL,STUN` matches STUN packets specifically so they can be blocked or forwarded.

- The keywords `DOH`, `DOH3`, `DOQ`, `DOT`, and `DNS` only match DNS requests sent by Surge itself (`DOT` matches DNS over TLS connections and `DNS` matches plain DNS over TCP connections configured with the `tcp://` prefix). By default these requests bypass the rule system and always use the DIRECT policy; set `encrypted-dns-follow-outbound-mode=true` in the [General] section to route them through rules. See Encrypted DNS.


The PROTOCOL rule does not support the `pre-matching` flag.


## HOSTNAME-TYPE Mac 5.7.3+


Rule matches the form of the hostname in a request. The supported keywords are:


- `IPv4`: hostname is an IPv4 literal.

- `IPv6`: hostname is an IPv6 literal.

- `DOMAIN`: hostname contains dots and is a regular domain name.

- `SIMPLE`: hostname without a dot, such as `localhost`.


HOSTNAME-TYPE,IPv6,REJECT
HOSTNAME-TYPE,SIMPLE,DIRECT
The keywords are case-sensitive: `IPv4` and `IPv6` must be written with this exact capitalization. An unrecognized keyword invalidates the rule.


## CELLULAR-RADIO iOS Only


Rule matches if the cellular radio technology of the current network matches. The rule only matches when the device is not on Wi-Fi. The possible values are `GPRS`, `Edge`, `WCDMA`, `HSDPA`, `HSUPA`, `CDMA1x`, `CDMAEVDORev0`, `CDMAEVDORevA`, `CDMAEVDORevB`, `eHRPD`, `HRPD`, `LTE`, `NRNSA`, and `NR`. The comparison is case-sensitive.


CELLULAR-RADIO,LTE,DIRECT
## CELLULAR-CARRIER iOS Only


Rule matches if the mobile carrier of the current cellular network matches. The value is the carrier's MCC (mobile country code) followed by the MNC (mobile network code) as a single string of digits. The rule only matches when the device is not on Wi-Fi.


CELLULAR-CARRIER,310260,Proxy
To match the same condition inside a subnet expression (for example in a Subnet Policy Group or an SSID Setting), use the `MCCMNC:` prefix described below.


## SUBNET


Rule matches if the current network matches the subnet expression.


SUBNET,TYPE:WIRED,DIRECT
SUBNET,SSID:MyHome,Proxy
Only the network of the outgoing interface is considered: the rule describes the network Surge is currently on, not the destination of the request.


### Subnet Expressions


Subnet expressions are also used outside the [Rule] section: the Subnet Policy Group and the SSID Setting section accept the same syntax. This section is the canonical reference.


A subnet expression takes one of these forms:


#### `SSID:<value>`


Matches the Wi-Fi network name (SSID). Wildcard characters `*` and `?` are allowed. The comparison is case-sensitive.


SUBNET,SSID:Office-*,DIRECT
#### `BSSID:<value>`


Matches the Wi-Fi access point MAC address (BSSID). Wildcard characters are allowed. The comparison is case-insensitive.


SUBNET,BSSID:aa:bb:cc:*,DIRECT
#### `ROUTER:<ip>`


Matches the default gateway IP address of the current network exactly.


SUBNET,ROUTER:192.168.1.1,DIRECT
#### `TYPE:WIFI` / `TYPE:WIRED` / `TYPE:CELLULAR`


Matches all Wi-Fi networks, all wired networks, or all cellular networks respectively. The type keyword is case-insensitive.


SUBNET,TYPE:CELLULAR,DIRECT
#### `MCCMNC:<digits>`


Matches the mobile carrier of the current cellular network by MCC+MNC. The expression only matches when the device is not on Wi-Fi.


SUBNET,MCCMNC:310260,Proxy
#### Bare value (legacy)


If no prefix is given, the value is compared for compatibility with old profiles: a value containing `*` or `?` is wildcard-matched against the SSID; otherwise it matches the SSID exactly, the BSSID case-insensitively, or the router IP exactly.


Prefer the prefixed forms in new profiles.

---
## Rules / Logical Rules

# Logical Rules


Logical rules combine multiple sub-rules with the operators AND, OR, and NOT for conditions that no single rule type can express, such as "this domain, but only from this client" or "everything except this network".


AND,((SRC-IP,192.168.1.110),(DOMAIN-SUFFIX,example.com)),DIRECT
## Syntax


```
AND,((Rule1),(Rule2),...),Policy
OR,((Rule1),(Rule2),...),Policy
NOT,((Rule1)),Policy

```

Each sub-rule is written in parentheses, without a policy of its own &#x2014; the same form used inside rule set files. Sub-rule values containing commas may be quoted.


- `AND` matches if all sub-rules match.

- `OR` matches if any sub-rule matches. Evaluation short-circuits in both cases.

- `NOT` inverts the result of its sub-rule. It takes exactly one sub-rule.


## Nesting


A logical rule may contain other logical rules, up to a maximum nesting depth of 10.


AND,((NOT,((SRC-IP,192.168.1.110))),(DOMAIN-SUFFIX,example.com)),DIRECT
Any rule type that is valid inside a rule set can be used as a sub-rule, including `RULE-SET` and `SCRIPT`. `FINAL` cannot be a sub-rule.


## Examples


Route a domain through a proxy only when on cellular:


AND,((DOMAIN-SUFFIX,example.com),(SUBNET,TYPE:CELLULAR)),Proxy
Reject QUIC traffic to a set of domains:


AND,((PROTOCOL,UDP),(RULE-SET,https://example.com/streaming.list)),REJECT
Send everything except LAN destinations from a specific client through a proxy:


```
AND,((SRC-IP,192.168.1.120),(NOT,((RULE-SET,LAN)))),Proxy

```

## Flags on logical rules


- Sub-rules may carry their own `no-resolve` and `extended-matching` flags, with the same meaning as on top-level rules.

- The `pre-matching` flag cannot be placed on a sub-rule, but the whole logical rule may be flagged `pre-matching` if every sub-rule type supports pre-matching and the policy is a REJECT-family policy. See the flags table in the rules overview.


```
AND,((DOMAIN-SUFFIX,tracker.example.com),(DEST-PORT,443)),REJECT,pre-matching

```

---
## Rules / Script Rules

# Script Rule


The SCRIPT rule delegates the matching decision to a JavaScript script, for conditions beyond what the built-in rule types can express.


SCRIPT,ScriptName,DIRECT
The value is the name of a script defined in the [Script] section with `type=rule`:


[Script]
ssid-rule = type=rule,script-path=ssid-rule.js

[Rule]
SCRIPT,ssid-rule,DIRECT
The script receives the request details (hostname, ports, protocol, process path, User-Agent, URL, source address, listen port, DNS result) in `$request` and must call `$done({matched: true})` or `$done({matched: false})`. See Script Type: rule for the full parameter list and examples.


#### requires-resolve


By default, a SCRIPT rule does not trigger a DNS lookup, so `$request.dnsResult` may be empty for domain hostnames. Add the `requires-resolve` flag to perform the DNS lookup before the script runs:


SCRIPT,ssid-rule,DIRECT,requires-resolve
The script's result is cached for the rest of the evaluation of the same request, so referencing the same script from multiple rules does not run it repeatedly.


The SCRIPT rule does not support the `pre-matching` flag.

---
## Rules / Rule Set

# Rule Set


The RULE-SET rule references a bundle of rules &#x2014; built into Surge, embedded in the profile, or loaded from a file or URL &#x2014; and applies one policy to every request matched by any rule in the set. Use it to keep long rule lists out of the main profile and to share lists between profiles.


RULE-SET,https://example.com/streaming.list,Proxy
RULE-SET,LAN,DIRECT
The value is resolved in this order:


- An internal rule set name (`SYSTEM` or `LAN`).

- An inline rule set: the name of a `[Ruleset <name>]` section in the profile.

- An external resource: an `http://`/`https://` URL, or a local file path (absolute, or relative to the profile directory).


## Internal Rule Sets


Surge provides two built-in rule sets.


The internal rule set contents may change between Surge versions. The listings below reflect the current version; check the rule set details in the app for the authoritative list.


### SYSTEM


RULE-SET,SYSTEM,DIRECT
Matches most requests sent by macOS and iOS itself. Requests from the App Store, iTunes, and other content services are not included. Current contents:


DOMAIN,api.smoot.apple.com
DOMAIN,captive.apple.com
DOMAIN,xp.apple.com
DOMAIN,configuration.apple.com
DOMAIN,guzzoni.apple.com
DOMAIN,smp-device-content.apple.com
DOMAIN,aod.itunes.apple.com
DOMAIN,mesu.apple.com
DOMAIN,api.smoot.apple.cn
DOMAIN,gs-loc.apple.com
DOMAIN,mvod.itunes.apple.com
DOMAIN,streamingaudio.itunes.apple.com
DOMAIN-SUFFIX,ess.apple.com
DOMAIN-SUFFIX,push-apple.com.akadns.net
DOMAIN-SUFFIX,push.apple.com
DOMAIN-SUFFIX,lcdn-locator.apple.com
DOMAIN-SUFFIX,lcdn-registration.apple.com
DOMAIN-SUFFIX,ls.apple.com
PROCESS-NAME,trustd
PROCESS-NAME,netbiosd
### LAN


```
RULE-SET,LAN,DIRECT

```

Matches private and special-purpose IP ranges and the `.local` suffix. Note that this rule set triggers a DNS lookup for domain hostnames (unless `no-resolve` is added to the RULE-SET line). Current contents:


DOMAIN-SUFFIX,local
IP-CIDR,0.0.0.0/8
IP-CIDR,10.0.0.0/8
IP-CIDR,100.64.0.0/10
IP-CIDR,127.0.0.0/8
IP-CIDR,169.254.0.0/16
IP-CIDR,172.16.0.0/12
IP-CIDR,192.0.0.0/24
IP-CIDR,192.0.2.0/24
IP-CIDR,192.168.0.0/16
IP-CIDR,224.0.0.0/4
IP-CIDR6,::1/128
IP-CIDR6,fc00::/7
IP-CIDR6,fe80::/10
## Inline Rule Sets Mac 5.3.1+


Instead of hosting the list externally, you can embed the rules directly in the profile as a `[Ruleset <name>]` section and reference the section name:


[Ruleset Streaming]
DOMAIN-SUFFIX,netflix.com
DOMAIN-SUFFIX,netflix.net
DOMAIN,netflixdnstest0.com

[Rule]
RULE-SET,Streaming,StreamingProxy
Inline rule sets use the same line syntax as external files and benefit from the same preprocessing optimizations. Modules can also contribute inline rule sets.


## External Rule Sets


The rule set file is a plain text file with one rule per line, written without the policy component:


# Comment lines start with #, // or ;
DOMAIN-SUFFIX,example.com
DOMAIN,cdn.example.org,extended-matching
IP-CIDR,203.0.113.0/24,no-resolve
IP-ASN,13335

- Per-line options such as `no-resolve` and `extended-matching` are allowed.

- `FINAL` and the `pre-matching` flag are not allowed inside a rule set file.

- Invalid lines are skipped with a warning; they do not invalidate the whole set.

- A set may contain at most 1,000,000 entries.


External rule sets are downloaded and cached. Local files are watched and reloaded automatically when they change. The same URL or file path cannot be used as both a RULE-SET and a DOMAIN-SET in one profile.


## Options on the RULE-SET Line


Options on the RULE-SET line apply to the whole set:


#### no-resolve


Removes the set's DNS requirement and forces `no-resolve` on every sub-rule. IP-based sub-rules are then skipped for domain hostnames that have not been resolved yet, instead of triggering a DNS lookup.


#### extended-matching


Forces extended matching on every sub-rule: domain rules in the set also match against the TLS SNI and HTTP Host header. Note that if any domain rule inside the set file already carries the flag, it is applied to all domain rules of that set.


#### update-interval


Optional, seconds, default 86400 (24 hours).


Re-download interval for URL-based rule sets. Set a negative value (e.g. `-1`) to disable automatic updates.


RULE-SET,https://example.com/social.list,Proxy,no-resolve,extended-matching,update-interval=43200
#### pre-matching


A RULE-SET rule may be flagged `pre-matching` if the policy is a REJECT-family policy; the whole set then participates in the pre-matching phase. See Rules Overview for how pre-matching works.


## Performance


Rule sets are preprocessed into indexes when loaded, so even very large sets match efficiently:


- DOMAIN and DOMAIN-SUFFIX entries are compiled into a domain index; sets with more than 1000 domain entries use an on-disk database instead of an in-memory tree.

- If a set contains more than 50 IP-CIDR (or IP-CIDR6) entries, they are compiled into a binary IP database.

- IP-ASN entries are checked in constant time.

- All other rule types are evaluated linearly.


When a sub-rule matches, the log records it as `Sub-rule matched: <rule> (in <set name>)`.


## RULE-SET vs. DOMAIN-SET


A DOMAIN-SET file is a plain list of hostnames (one per line, with an optional leading dot for suffix matching) and can only match domains. A RULE-SET file contains full rule declarations of any type valid in a set. For pure domain lists, DOMAIN-SET files are simpler to maintain; RULE-SET is required as soon as the list mixes rule types.


The `[Host]` section also accepts `RULE-SET:` and `DOMAIN-SET:` prefixes as match keys for DNS mapping; see Local DNS Mapping.

---
## Rules / FINAL Rule

# Final Rule


The FINAL rule defines the default policy for requests not matched by any other rule. Write it after all other rules; the [Rule] section must end with a FINAL rule.


[Rule]
DOMAIN-SUFFIX,company.com,ProxyA
DOMAIN-KEYWORD,google,DIRECT
GEOIP,US,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
FINAL,ProxyB
A FINAL rule always matches, so any rules written below it never take effect. If several enabled FINAL rules are present, the last one is the effective one. FINAL is not allowed inside rule set files or as a sub-rule of a logical rule.


## Options


#### dns-failed


If a DNS lookup fails while evaluating an IP-based rule, the request normally fails with an error. With the `dns-failed` option, Surge uses the FINAL rule's policy instead:


FINAL,ProxyB,dns-failed
This option only makes sense with a non-DIRECT policy &#x2014; a direct connection to a hostname that cannot be resolved would fail anyway, while a proxy can perform the DNS resolution remotely.


Like other rules, FINAL also accepts the `notification-text` and `notification-interval` options; see Rules Overview.


## Relationship to Outbound Mode


The FINAL rule is the default only within Rule-Based Proxy outbound mode. In Direct or Global Proxy outbound mode, the rule system &#x2014; including FINAL &#x2014; is bypassed entirely: all traffic goes direct or to the selected global policy.

---
## Policies / Overview

# Policies


A policy tells Surge how to handle a request once a rule has matched it: connect directly, reject it, or forward it to a proxy server. Every rule ends with a policy name, and the FINAL rule picks the policy for all unmatched requests.


There are three kinds of policies:


- Built-in policies: predefined policies such as `DIRECT` and `REJECT`. See Built-in Policies and the REJECT family.

- Proxy policies: forward the request to a proxy server. Declared in the `[Proxy]` section.

- Policy groups: select one policy from a set of policies, manually or automatically. See Policy Groups.


## The [Proxy] Section


Each line in the `[Proxy]` section declares one proxy policy:


Name = <type>, <arguments...>, key1=value1, key2=value2
For all server-based proxy types, the first two arguments are the server hostname and port. The remaining parameters are written as `key=value` pairs. Quote a value if it contains commas.


[Proxy]
ProxyHTTPS = https, 1.2.3.4, 443, username, password
ProxySS = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd
ProxySnell = snell, 1.2.3.4, 8000, psk=pwd, version=5
## Referencing Policies


A policy name can be used anywhere a policy is accepted:


- As the target of a rule: `DOMAIN-SUFFIX,example.com,ProxySS`

- As a member of a policy group: `Group = select, ProxySS, ProxySnell, DIRECT`

- As the value of the `underlying-proxy` parameter to build a proxy chain.


## Supported Proxy Protocols


[TABLE]


|
Type keyword |
 Protocol |
 Notes |
 |


|
 `http` / `https` |
 HTTP / HTTPS |
 HTTPS = HTTP proxy over TLS |
 |

|
 `h2-connect` |
 HTTP/2 CONNECT |
 Mac 6.6.0+ |
 |

|
 `socks5` / `socks5-tls` |
 SOCKS5 / SOCKS5-TLS |
  |
 |

|
 `ss` |
 Shadowsocks |
  |
 |

|
 `snell` |
 Snell |
 Versions 1&#x2013;6 |
 |

|
 `vmess` |
 VMess |
  |
 |

|
 `trojan` |
 Trojan |
  |
 |

|
 `tuic` / `tuic-v5` |
 TUIC |
 QUIC-based |
 |

|
 `hysteria2` |
 Hysteria 2 |
 QUIC-based iOS 5.8.0+ Mac 5.4.0+ |
 |

|
 `anytls` |
 AnyTLS |
 iOS 5.17.0+ Mac 6.4.3+ |
 |

|
 `trust-tunnel` |
 Trust Tunnel |
 Mac 6.4.4+ |
 |

|
 `ssh` |
 SSH |
  |
 |

|
 `wireguard` |
 WireGuard |
 L3 VPN as proxy |
 |

|
 `tailscale` |
 Tailscale |
 iOS 5.20.0+ Mac 6.7.0+ |
 |

|
 `external` |
 External Proxy Program |
 Mac Only |
 |


[/TABLE]
The built-in type keywords `direct`, `reject`, `reject-drop`, `reject-no-drop`, and `reject-tinygif` may also appear in the `[Proxy]` section to define aliases of the built-in policies. See Built-in Policies.


## Shared Parameters


Besides the protocol-specific parameters documented on each protocol page, several parameter groups are shared across policy types:


- Common Policy Parameters: egress control (`interface`, `ip-version`, `tfo`, ...), testing (`test-url`, ...), and proxy chaining (`underlying-proxy`).

- TLS Parameters: parameters shared by TLS- and QUIC-based protocols, plus Shadow TLS obfuscation.

- UDP Relay: UDP protocol support matrix and related parameters.

---
## Policies / Built-in Policies

# Built-in Policies


Surge provides several built-in policies, the most important being `DIRECT` and `REJECT`. `DIRECT` sends the request directly to the host; `REJECT` rejects it. They can be used in rules and policy groups without any declaration.


#### DIRECT


Send the request to the host directly.


#### CELLULAR iOS Only


Prefer the cellular network over the Wi-Fi network. If the cellular network is unavailable, other interfaces are used instead.


#### CELLULAR-ONLY iOS Only


Use the cellular network only. The connection fails if the cellular network is not available.


#### HYBRID iOS Only


Try to set up connections with the Wi-Fi and cellular network simultaneously, then use the faster link. Only meaningful while the All Hybrid option is not on.


#### NO-HYBRID iOS Only


Never try to set up connections with the cellular network if Wi-Fi is available. Only meaningful while either the All Hybrid or Wi-Fi Assist option is enabled.


For `REJECT`, `REJECT-DROP`, `REJECT-NO-DROP`, and `REJECT-TINYGIF`, see the REJECT Policy page.


## Alias


You can define an alias of a built-in policy in the `[Proxy]` section, using one of the type keywords `direct`, `reject`, `reject-drop`, `reject-no-drop`, or `reject-tinygif`:


[Proxy]
On = direct
Off = reject
`On` and `Off` can then be used as policy names in rules and policy groups.


An alias accepts the common policy parameters, which makes it useful for egress control. For example, a direct alias bound to a specific network interface:


[Proxy]
Corp-VPN = direct, interface = utun0
WiFi = direct, interface = en2, allow-other-interface=true
A `[Proxy]` line that redefines the name `DIRECT` is silently ignored. Redefining any other built-in policy name, such as `REJECT` or `CELLULAR`, is a configuration error.

---
## Policies / REJECT Policies

# REJECT Policy


To meet different needs, Surge has multiple built-in REJECT policies. In most cases, using `REJECT` directly is sufficient. If there are special requirements, consider the derivative policies.


#### REJECT


Reject the request. If the request is HTTP, an error page is returned. This behavior can be controlled by the `show-error-page-for-reject` option in the [General] section.


#### REJECT-TINYGIF


Reject the request. If the request is HTTP, a 1px transparent GIF is returned, which is useful for ad blocking.


#### REJECT-DROP


Reject the request. Unlike REJECT, this policy silently discards the connection. Some applications have very aggressive retry logic and immediately retry after a connection failure, leading to a request storm. Using this policy can mitigate the issue.


#### REJECT-NO-DROP


If a large number of requests to a hostname trigger the `REJECT`/`REJECT-TINYGIF` policy within a short period of time (the threshold is 50 times within 30 seconds in the current version), Surge automatically upgrades the policy to `REJECT-DROP` to avoid wasting resources.


Use the `REJECT-NO-DROP` policy to avoid this behavior: it rejects the request and is never upgraded to `REJECT-DROP`.


## Pre-matching Reject iOS 5.14.0+ Mac 5.9.0+


Due to the extensive range of properties that Surge's rule system can evaluate, rule determination can normally only occur after receiving the first TCP packet. This results in excessive unnecessary overhead when dealing with storm requests or ad-blocking needs.


The pre-matching feature quickly rejects requests with low overhead. For rules using a REJECT policy, enable it with the `pre-matching` tag:


[Rule]
DOMAIN,ad.com,REJECT,pre-matching
Rules marked with `pre-matching` take effect before the normal rule matching process, thus having the highest priority.


All rules marked with `pre-matching` are extracted for prioritized matching and executed during the DNS resolution and TCP SYN phases. If a DNS domain is matched, Surge returns No Record directly. If a TCP SYN is matched, Surge generates a TCP RST response immediately. In case of numerous requests, Surge escalates to packet loss. UDP is handled similarly.


Additionally, each rule only appears once in the recent request list every 5 minutes to avoid flooding.


The rule types that can be marked with `pre-matching`:


- Domain types: DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-SET, DOMAIN-WILDCARD

- IP types: IP-CIDR, IP-CIDR6, GEOIP, IP-ASN

- Logical rules: AND, OR, NOT

- Others: SUBNET, CELLULAR-RADIO, CELLULAR-CARRIER, DEST-PORT, SRC-PORT, SRC-IP


RULE-SET can also be used, but its content is subject to the above restrictions as well.


## Pre-matching Technical Details


For optimal user experience, rejections are made during the pre-matching phase. The derivative policies behave slightly differently.


#### For DNS queries


- If a REJECT policy is matched, Surge returns a No Record DNS response. If the frequency limit built into the REJECT policy is triggered, the DNS query is discarded without a response.


- If a REJECT-DROP policy is matched, the DNS query is discarded without a response.


- If a REJECT-NO-DROP policy is matched, it returns a special IP address 198.18.0.244; Surge generates TCP RST responses for all TCP connections accessing this address.


#### For TCP requests using IP


- If a REJECT policy is matched, Surge directly generates TCP RST responses; if the frequency limit built into the REJECT policy is triggered, it discards the corresponding TCP SYN handshake packet.


- If a REJECT-DROP policy is matched, Surge directly discards the TCP SYN handshake packet.


- If a REJECT-NO-DROP policy is matched, Surge directly generates TCP RST responses.


Some software has aggressive retry logic that immediately retries after a request fails, causing abnormal CPU usage. Even for the REJECT-NO-DROP policy, when Surge generates a large number of TCP RST packets in a short period of time (the threshold is 100 times within 3 seconds in the current version), a protection mechanism pauses returning TCP RST and drops packets instead.


#### For UDP packets


Since UDP packets have no handshake overhead, there is no pre-matching phase; they are directly matched using the main rule set:


- If a REJECT policy is matched, an ICMP Administratively Prohibited response is generated. If the frequency limit built into the REJECT policy is triggered, packets are discarded.


- If a REJECT-DROP policy is matched, packets are directly discarded.


- If a REJECT-NO-DROP policy is matched, an ICMP Administratively Prohibited response is generated.

---
## Policies / Common Policy Parameters

# Common Policy Parameters


These parameters can be appended as `key=value` pairs to any policy line, regardless of the proxy protocol. Protocol-specific parameters are documented on each protocol page; parameters shared by TLS-based protocols are on the TLS Parameters page, and UDP-related parameters on the UDP Relay page.


The egress and testing parameters below apply to both proxy policies and built-in policy aliases, except where noted.


## Egress Parameters


#### interface


Optional, network interface name, default: automatic.


Force the policy to use a specified outgoing network interface:


ProxyHTTP = http, 1.2.3.4, 443, username, password, interface = en2
A direct policy alias supports the `interface` parameter like a proxy policy:


[Proxy]
Corp-VPN = direct, interface = utun0
WiFi = direct, interface = en2, allow-other-interface=true
Make sure the interface has a valid route table for the destination address. WireGuard and Tailscale policies do not support interface binding.


#### allow-other-interface


Optional, boolean, default: false.


When true, if the desired interface is unavailable, Surge is allowed to use the default interface to bind the connection. Otherwise, the connection fails directly.


ProxyHTTP = http, 1.2.3.4, 443, username, password, interface = en2, allow-other-interface=true
#### dns-follow-interface iOS 5.15.2+ Mac 5.2.0+


Optional, boolean, default: false.


Make the `interface` parameter of the policy also take effect for DNS queries; DNS requests that match the policy will use this interface for queries. (If DNS is triggered during the rule matching stage, a specific interface will not be used.)


#### no-error-alert


Optional, boolean, default: false. Proxy policies only.


Do not show error alerts for this policy.


#### ip-version


Optional, `dual` / `v4-only` / `v6-only` / `prefer-v4` / `prefer-v6`, default: `dual`.


Choose the behavior between IPv4 and IPv6 protocols. The option only affects the connection to the proxy server, so it only makes sense when the proxy server's hostname is a domain. If an underlying proxy is configured, this option has no effect since the DNS resolution happens remotely.


- `dual`: use the fastest link.

- `v4-only` / `v6-only`: use only the specified address family.

- `prefer-v4` / `prefer-v6`: prefer the specified address family.


Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, `prefer-v4` and `prefer-v6` use the preferred address family first during TCP connection establishment. If a connection cannot be established within 3 seconds, Surge also starts trying addresses from the other family. iOS 5.21.0+ Mac 6.8.0+


#### hybrid iOS Only


Optional, `auto` / `on` / `off`, default: `auto`.


Set up the connection with cellular data and Wi-Fi simultaneously, then use the faster link. When omitted (`auto`), the connection follows the global All Hybrid setting; `on` and `off` force the behavior for this policy. `true`/`false` are also accepted.


#### tfo


Optional, boolean, default: false.


Enable TCP Fast Open.


#### tos


Optional, 0&#x2013;255 in decimal or `0x` hexadecimal, default: 0.


Customize the IP TOS value.


#### ecn iOS 5.8.0+ Mac 5.4.0+


Optional, `auto` / `on` / `off`, default: `auto`. Proxy policies only.


Enable ECN (Explicit Congestion Notification) support. It can improve bandwidth performance in high packet loss environments, but enabling it in unsupported network environments may result in connection failure. The parameter takes effect for QUIC-based protocols and WireGuard/Tailscale policies; it has no effect on plain TCP protocols.


On supported systems, ECN is enabled by default for QUIC-based proxy protocols starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. These protocols automatically fall back to non-ECN handling when an anomaly is detected. WireGuard and Tailscale policies remain disabled by default. Use `ecn=true` or `ecn=false` to override the applicable default explicitly. iOS 5.21.0+ Mac 6.8.0+


#### block-quic iOS 5.8.0+ Mac 5.4.0+


Optional, `auto` / `on` / `off`, default: `auto`.


Forwarding QUIC traffic through a proxy may cause performance issues. Enabling this option blocks QUIC traffic, causing the client to fall back to the traditional HTTPS/TCP protocol.


- `auto`: automatically decide based on whether the policy is suitable for forwarding QUIC traffic.

- `on`: block QUIC traffic.

- `off`: do not block QUIC traffic.


If this parameter is omitted, proxy policies block QUIC by default, while DIRECT and other built-in policies do not. Mac 6.4.3+


## Testing Parameters


#### test-url


Optional, HTTP(S) URL, default: the global `proxy-test-url`/`internet-test-url` setting.


Override the global testing URL for this policy. The URL is used for availability and latency testing by performing an HTTP HEAD request.


Proxy = snell, 1.2.3.4, 8000, psk=pwd, version=5, test-url=http://google.com
#### test-timeout


Optional, in seconds, default: the global `test-timeout` setting.


Override the global testing timeout for this policy.


#### test-udp


Optional, `hostname@ipv4`, default: the global `proxy-test-udp` setting.


Override the global `proxy-test-udp` setting for this policy. The UDP relay is tested by performing a DNS lookup of the hostname via the given server. See UDP Relay.


Proxy = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd, udp-relay=true, test-udp=google.com@1.1.1.1
## Proxy Chain


#### underlying-proxy


Optional, the name of another proxy policy or policy group. Proxy policies only.


Use a proxy to connect to another proxy, aka proxy chain. Surge first establishes a connection to the underlying policy, then connects to the target proxy server through it.


[Proxy]
Entry = https, entry.example.com, 443, username, password
Exit = snell, exit.example.com, 443, psk=pwd, version=5, underlying-proxy=Entry
With this configuration, traffic sent to the `Exit` policy is relayed through `Entry`: client &#x2192; Entry &#x2192; Exit &#x2192; destination.


Notes:


- The value may also be a policy group name, so the entry node can be selected dynamically.

- When an underlying proxy is configured, DNS resolution of the target proxy's hostname happens remotely, so the `ip-version` parameter has no effect.

- `underlying-proxy` cannot be combined with the `port-hopping` parameter of QUIC-based protocols.

---
## Policies / TLS and Shadow TLS

# TLS Parameters


All proxy protocols carried over TLS or QUIC share a common set of TLS parameters: HTTPS, SOCKS5-TLS, HTTP/2 CONNECT, Trust Tunnel, Trojan, TUIC, Hysteria 2, AnyTLS, and VMess with `tls=true`. This page also covers the Shadow TLS obfuscation layer, which can wrap most TCP-based protocols.


[Proxy]
Proxy = https, example.com, 443, sni=cdn.example.com, server-cert-verify-name=example.com
## Parameters


#### skip-cert-verify


Optional, boolean, default: false.


If enabled, Surge does not verify the server's certificate. Use with caution: it allows man-in-the-middle attacks on the proxy connection.


#### sni


Optional, hostname or `off`, default: the proxy hostname.


Customize the Server Name Indication (SNI) sent during the TLS handshake. By default, Surge sends the SNI using the hostname like most browsers. Use `sni=off` to turn off SNI completely.


#### server-cert-verify-name iOS 5.21.0+ Mac 6.8.0+


Optional, hostname.


Specify the hostname used to verify the proxy server certificate independently from SNI. This is useful when the TLS endpoint needs one SNI value but its certificate must be verified against another name. It applies to all TLS- and QUIC-based proxy protocols.


#### server-cert-fingerprint-sha256


Optional, SHA-256 fingerprint (64 hexadecimal characters).


Use a pinned server certificate instead of the standard X.509 validation.


#### alpn iOS 5.20.0+ Mac 6.7.0+


Optional, comma-separated protocol list (quote the value if it contains multiple entries).


Customize the ALPN value used during the TLS handshake. It must match a protocol supported by the proxy server. When unset, TUIC and Hysteria 2 use `h3` by default.


#### client-cert


Optional, the name of a `[Keystore]` item.


Use a client certificate for mutual TLS authentication. The certificate is stored in the [Keystore] section:


[Proxy]
Proxy = https, example.com, 443, client-cert=cert1

[Keystore]
cert1 = base64=<P12 base64 string here>, password=123456
## Shadow TLS


Shadow TLS is a proxy obfuscator that can wrap TCP-based proxy protocols. Starting from Surge iOS 5.2.0 and Surge Mac 4.10.0, Surge supports the Shadow TLS v2 protocol. Append `shadow-tls-password` to a proxy declaration to enable it:


[Proxy]
STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2
Starting from Surge iOS 5.5.0 and Surge Mac 5.0.3, Surge supports the Shadow TLS v3 protocol:


STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2, shadow-tls-version=3, shadow-tls-sni=example.com
Shadow TLS cannot be combined with TUIC, WireGuard, or Tailscale policies; attempting to do so is a configuration error. As a TCP-based wrapper, it is also not meaningful for other QUIC-based protocols.


#### shadow-tls-password


Required. It must match the server's setting.


#### shadow-tls-sni


Optional, hostname. Required when `shadow-tls-version=3`.


The SNI sent to the server during the Shadow TLS handshake in plain text. If not set, no SNI is sent.


#### shadow-tls-version


Optional, `2` or `3`, default: 2.


The Shadow TLS protocol version.

---
## Policies / UDP Relay

# UDP Relay


Surge processes UDP traffic with the same rule system as TCP. When UDP traffic matches a rule that resolves to a proxy policy, the policy must support UDP relay to forward it. This page lists which protocols support UDP relay and the related parameters.


## Protocol Support


[TABLE]


|
Protocol |
 UDP relay |
 |


|
 SOCKS5 / SOCKS5-TLS |
 Yes, requires `udp-relay=true` |
 |

|
 Shadowsocks |
 Yes, requires `udp-relay=true` |
 |

|
 Snell |
 Yes, version 3 and above (automatic) |
 |

|
 VMess |
 Yes |
 |

|
 Trojan |
 Yes |
 |

|
 TUIC |
 Yes |
 |

|
 Hysteria 2 |
 Yes |
 |

|
 AnyTLS |
 Yes |
 |

|
 WireGuard |
 Yes |
 |

|
 Tailscale |
 Yes |
 |

|
 External Proxy Program (Mac) |
 Yes, requires `udp-relay=true` |
 |

|
 HTTP / HTTPS |
 No |
 |

|
 HTTP/2 CONNECT |
 No |
 |

|
 Trust Tunnel |
 No |
 |

|
 SSH |
 No |
 |


[/TABLE]
The built-in DIRECT and REJECT policy families always handle UDP traffic.


## Parameters


#### udp-relay


Optional, boolean, default: false. Applies to SOCKS5, SOCKS5-TLS, Shadowsocks, and External Proxy Program policies.


Since UDP relay is an optional feature for these servers, it must be enabled explicitly:


[Proxy]
ProxySOCKS5 = socks5, 1.2.3.4, 1080, username, password, udp-relay=true
ProxySS = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd, udp-relay=true
#### udp-port iOS 5.14.0+ Mac 5.9.0+


Optional, port number, default: the main server port. Applies to Shadowsocks and Snell policies.


Use another server port when performing UDP forwarding. This can be used when the server's TCP and UDP services do not listen on the same port, for example when Shadow TLS occupies the TCP port.


## Behavior for Unsupported Policies


When UDP traffic matches a policy that does not support UDP relay, the fallback behavior is controlled by the `udp-policy-not-supported-behaviour` option in the [General] section. Possible values are `DIRECT` and `REJECT`. Starting from Surge Mac 6.0.0, the default is `REJECT` to avoid leaking traffic unknowingly.


## UDP Testing


Latency tests only measure the TCP path. To test a policy's UDP relay, Surge performs a DNS lookup through the relay, configured as `hostname@server-ip`:


- The global default endpoint is set by `proxy-test-udp` in the [General] section, e.g. `proxy-test-udp = apple.com@8.8.8.8`.

- The per-policy `test-udp` parameter overrides the global setting, e.g. `test-udp=google.com@1.1.1.1`.

---
## Policies / HTTP Proxy

# HTTP, HTTPS, and HTTP/2 CONNECT Proxy


Surge supports the standard HTTP proxy family: plain HTTP proxy (`http`), HTTP proxy over TLS (`https`), and HTTP/2 CONNECT proxy (`h2-connect`). Use these types when connecting to a standard proxy server such as Squid, TinyProxy, or another Surge-compatible HTTP proxy endpoint.


[Proxy]
ProxyHTTP = http, 1.2.3.4, 443, username, password
ProxyHTTPS = https, 1.2.3.4, 443, username, password
ProxyH2 = h2-connect, example.com, 443
Declaration syntax:


Name = http, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = https, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = h2-connect, <host>, <port>[, parameter=value, ...]
The `https` and `h2-connect` Mac 6.6.0+ types always connect over TLS. HTTP/2 CONNECT multiplexes multiple requests over a single TCP connection.


None of these types supports UDP relay.


### Parameters


#### username / password


Optional.


Credentials for proxy authentication. They may be given positionally after the port, or as named parameters:


ProxyH2 = h2-connect, example.com, 443, username=user, password=pass
#### always-use-connect


Optional, Boolean, default: false.


Always use the HTTP CONNECT method to relay the request, even for plain HTTP requests. Applies to `http` and `https` only.


#### headers Mac 6.6.0+


Optional.


Add custom request headers to proxy handshake requests. Multiple headers are separated by semicolons.


Proxy = http, example.com, 8080, headers=X-Client:Surge;X-Token:abc
Proxy = h2-connect, example.com, 443, headers=X-Padding:<random-string(16-32)>
The value supports `<random-string(n)>` and `<random-string(min-max)>` placeholders. Surge generates a URL-safe random string when connecting, which can be used for dynamic padding or request fingerprint perturbation.


For HTTP and HTTPS proxy policies, a configured header replaces an original field with the same name, including the `Host` field. iOS 5.20.0+ Mac 6.7.0+


#### max-streams Mac 6.6.0+


Optional, default: 3.


For `h2-connect` only. Control the maximum number of multiplexed sub-connections over the same TCP connection. A large value may hurt performance in some environments.


### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since `https` and `h2-connect` connect over TLS, they also accept the TLS parameters, such as `sni`, `skip-cert-verify`, and `client-cert`.

---
## Policies / SOCKS5 Proxy

# SOCKS5 Proxy


Surge supports the standard SOCKS5 proxy protocol (`socks5`) and SOCKS5 over TLS (`socks5-tls`). SOCKS5 is a simple, widely supported protocol; use `socks5-tls` when the server wraps the SOCKS5 session in TLS for transport security.


[Proxy]
ProxySOCKS5 = socks5, 1.2.3.4, 443, username, password
ProxySOCKS5TLS = socks5-tls, 1.2.3.4, 443, username, password, skip-cert-verify=false
Declaration syntax:


Name = socks5, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = socks5-tls, <host>, <port>[, <username>, <password>][, parameter=value, ...]
### Parameters


#### username / password


Optional.


Credentials for SOCKS5 username/password authentication. They may be given positionally after the port, or as named parameters.


#### udp-relay


Optional, Boolean, default: false.


Enable UDP relay with the SOCKS5 UDP ASSOCIATE command. Since UDP relay is an optional feature of the SOCKS5 protocol and the server may not support it, you must enable it explicitly.


### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since `socks5-tls` connects over TLS, it also accepts the TLS parameters, such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see UDP Relay.

---
## Policies / Shadowsocks

# Shadowsocks


Surge supports the Shadowsocks protocol (`ss`), a popular encrypted proxy protocol, including the Shadowsocks 2022 edition and simple-obfs&#x2013;style obfuscation.


[Proxy]
Proxy-SS = ss, 1.2.3.4, 8000, encrypt-method=chacha20-ietf-poly1305, password=abcd1234
Declaration syntax:


Name = ss, <host>, <port>, encrypt-method=<method>, password=<password>[, parameter=value, ...]
### Parameters


#### encrypt-method


Required.


The encryption method. It must match the server's setting. Supported values:


- AEAD 2022: `2022-blake3-aes-128-gcm`, `2022-blake3-aes-256-gcm`

- AEAD: `aes-128-gcm`, `aes-192-gcm`, `aes-256-gcm`, `chacha20-ietf-poly1305`, `xchacha20-ietf-poly1305`

- Stream (legacy, not recommended): `rc4`, `rc4-md5`, `aes-128-cfb`, `aes-192-cfb`, `aes-256-cfb`, `aes-128-ctr`, `aes-192-ctr`, `aes-256-ctr`, `salsa20`, `chacha20`, `chacha20-ietf`

- `none`


#### password


Required.


The pre-shared password. It is required unless `encrypt-method` is `none`.


For Shadowsocks 2022 methods, the password must be a Base64-encoded key of exactly 16 bytes (`2022-blake3-aes-128-gcm`) or 32 bytes (`2022-blake3-aes-256-gcm`). For identity-based multi-user authentication, use the form `serverKey:userKey` with both parts Base64-encoded keys of the same size.


#### udp-relay


Optional, Boolean, default: false.


Enable UDP relay. Since UDP relay is optional for a Shadowsocks server, you must enable it explicitly.


#### udp-port iOS 5.14.0+ Mac 5.9.0+


Optional.


When performing UDP forwarding, use another server port number. This can be used when the server's TCP and UDP services do not listen on the same port, for example, when Shadow TLS occupies the TCP port.


#### obfs


Optional, `http` or `tls`.


Enable simple-obfs&#x2013;style traffic obfuscation. It must match the server's obfuscation setting.


#### obfs-host


Optional.


The hostname used in the obfuscation handshake.


#### obfs-uri


Optional.


The URI used in the obfuscation request. Only meaningful with `obfs=http`.


The legacy `custom` policy type from very old configurations is parsed as a Shadowsocks policy; the external module URL in its declaration is ignored. Use the `ss` type instead.


### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. For details on UDP forwarding behavior, see UDP Relay.

---
## Policies / Snell

# Snell


Snell is a lean encrypted proxy protocol designed by the Surge team for maximum performance and simplicity. Surge supports protocol versions 1 through 6. See the Snell knowledge base for server downloads and release notes.


[Proxy]
Proxy-Snell = snell, 1.2.3.4, 8000, psk=password, version=4
Declaration syntax:


Name = snell, <host>, <port>, psk=<psk>, version=<n>[, parameter=value, ...]
Surge Mac also ships a built-in Snell server that accepts incoming Snell connections.


### Parameters


#### psk


Required.


The pre-shared key. It must match the server's setting.


#### version


Optional, 1&#x2013;6, default: 1.


The Snell protocol version. It must match the server version. Always declare it explicitly; when omitted, Surge assumes the legacy v1 protocol.


#### reuse


Optional, Boolean, default: false.


Enable connection reuse. Only meaningful for v4 and later; Snell v2 always reuses connections, and v1/v3 never do.


#### obfs


Optional.


Enable traffic obfuscation. Availability depends on the protocol version:


- v1&#x2013;v3: `http` or `tls`

- v4 and v5: `http` only

- v6: obfuscation is not supported


#### obfs-host


Optional.


The hostname used in the obfuscation handshake.


#### obfs-uri


Optional.


The URI used in the obfuscation request. Only meaningful with `obfs=http`.


#### udp-port


Optional.


When performing UDP forwarding, use another server port number. This can be used when the server's TCP and UDP services do not listen on the same port.


#### mode


Optional, `default` | `unshaped` | `unsafe-raw`, default: `default`. Snell v6 only.


Select the transport mode. The value must match the `mode` setting of the Snell v6 server:


- `default`: The standard mode with encryption and PSK-derived traffic shaping. Use it for normal deployments.

- `unshaped`: Keep encryption but disable traffic shaping.

- `unsafe-raw`: Disable both traffic shaping and encryption. As the name suggests, this mode provides no confidentiality; only use it for debugging or inside an already-secured tunnel.


Setting `mode` on a policy with a version lower than 6 is a profile error.


### UDP Relay


Snell supports UDP relay with protocol version 3 and later. No parameter is required; UDP forwarding is available automatically.


With `version=5`, Surge automatically uses QUIC Proxy Mode when relaying QUIC traffic, which converts the QUIC transport instead of tunneling it datagram by datagram. This is a runtime behavior with no profile parameter.


### Snell v6 iOS 5.20.0+ Mac 6.7.0+


Set `version=6` to use Snell v6:


Proxy-Snell-v6 = snell, 1.2.3.4, 8000, psk=password, version=6
Snell v6 derives a deployment-specific protocol profile from the PSK automatically, so no obfuscation parameters need to be configured on the client; traffic shaping is derived automatically. The optional `mode` parameter described above can switch the transport to `unshaped` or `unsafe-raw` when the server is configured accordingly. Unlike Snell v5, v6 does not support QUIC Proxy Mode.


The Snell v6 server adds two server-side network controls. These are Snell server configuration items, not Surge proxy-policy parameters:


- `dns-ip-preference`: Controls address-family selection for DNS results. The available values are `default`, `prefer-ipv4`, `prefer-ipv6`, `ipv4-only`, and `ipv6-only`.

- `listen`: Accepts multiple comma-separated listening addresses, for example `listen = 0.0.0.0:7177,[::]:7177`.


Snell v6 is currently in beta and may receive incompatible protocol changes. Keep both the Surge client and the Snell server updated to compatible beta versions. See Introducing Snell v6 for design details and the Snell knowledge base for server downloads.


### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Snell is also a common companion for Shadow TLS obfuscation. For details on UDP forwarding behavior, see UDP Relay.

---
## Policies / VMess

# VMess


Surge supports the VMess protocol, the proxy protocol of the V2Ray project, including the AEAD handshake, optional TLS, and WebSocket transport.


[Proxy]
Proxy-VMess = vmess, 1.2.3.4, 8000, username=0233d11c-15a4-47d3-ade3-48ffca0ce119
Declaration syntax:


Name = vmess, <host>, <port>, username=<UUID>[, parameter=value, ...]
VMess supports UDP relay. No parameter is required; UDP forwarding is available automatically.


### Parameters


#### username


Required.


The VMess user ID. It must be a valid UUID.


#### encrypt-method


Optional, `aes-128-gcm` or `chacha20-ietf-poly1305`, default: `aes-128-gcm`.


The data encryption method.


#### vmess-aead


Optional, Boolean, default: false.


Use the VMess AEAD handshake instead of the legacy handshake. It must match the server's setting.


#### tls


Optional, Boolean, default: false.


Connect to the server over TLS. When enabled, the TLS parameters also apply.


#### ws


Optional, Boolean, default: false.


Use the WebSocket transport layer.


#### ws-path


Optional, default: `/`.


The path used for the WebSocket handshake. It must start with `/`.


#### ws-headers


Optional.


Extra headers for the WebSocket handshake, as pipe-separated `Header:Value` pairs:


Proxy-VMess = vmess, 1.2.3.4, 8000, username=0233d11c-15a4-47d3-ade3-48ffca0ce119, ws=true, ws-path=/v2, ws-headers=Host:example.com|X-Token:abc
### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. With `tls=true`, the TLS parameters apply, such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see UDP Relay.

---
## Policies / Trojan

# Trojan


Surge supports the Trojan protocol, a proxy protocol that disguises traffic as ordinary TLS connections. Trojan always connects over TLS, so it pairs naturally with a real certificate on port 443.


[Proxy]
Proxy-Trojan = trojan, 192.168.20.6, 443, password=password1
Declaration syntax:


Name = trojan, <host>, <port>, password=<password>[, parameter=value, ...]
Trojan supports UDP relay. No parameter is required; UDP forwarding is available automatically.


### Parameters


#### password


Required.


The password. It must match the server's setting.


#### ws


Optional, Boolean, default: false.


Use the WebSocket transport layer.


#### ws-path


Optional, default: `/`.


The path used for the WebSocket handshake. It must start with `/`.


#### ws-headers


Optional.


Extra headers for the WebSocket handshake, as pipe-separated `Header:Value` pairs, for example `ws-headers=Host:example.com|X-Token:abc`.


### Common Parameters


All proxy policies accept the common policy parameters, such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since Trojan always connects over TLS, the TLS parameters also apply, such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see UDP Relay.

---
## Policies / TUIC

# TUIC


TUIC is a proxy protocol built on QUIC. It always encrypts traffic with TLS over QUIC and supports both TCP and UDP relay with connection multiplexing.


Surge supports two protocol versions with different type keywords:


- `tuic` &#x2014; TUIC v4, which authenticates with a token.

- `tuic-v5` &#x2014; TUIC v5, which authenticates with a UUID and password pair.


Use the keyword that matches your server's protocol version: v4 servers use `token`, and v5 servers use `uuid` + `password`. The two versions are not interchangeable.


[Proxy]
Proxy-TUIC = tuic, 192.168.20.6, 443, token=pwd, alpn=h3
Proxy-TUIC-v5 = tuic-v5, 192.168.20.6, 443, uuid=0233d11c-15a4-47d3-ade3-48ffca0ce119, password=pwd, alpn=h3
## Parameters


#### token


Required for `tuic` (v4). The authentication token, which must match the server's setting. Not used by `tuic-v5`.


#### uuid


Required for `tuic-v5`. The user UUID, in the standard hyphenated form. Not used by `tuic` (v4).


#### password


Required for `tuic-v5`. The password paired with the UUID. Not used by `tuic` (v4).


#### alpn


Optional. Default: h3.


Customize the ALPN value used during the QUIC-TLS handshake. It must match the server's ALPN setting.


#### port-hopping


Optional. Rotate among a list of ports or ranges instead of the main port. Behaves the same as for Hysteria 2.


Port hopping cannot be combined with the `underlying-proxy` parameter.


#### port-hopping-interval


Optional. In seconds. Default: 30. The interval for rotating among the configured ports &#x2014; see Hysteria 2.


## Notes


- UDP relay is always supported; no extra parameter is needed. See UDP Relay.

- As a QUIC-based protocol, TUIC enables ECN by default on supported systems. See the `ecn` parameter in Common Policy Parameters.

- Shadow TLS cannot be used with TUIC policies.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.

- TLS Parameters &#x2014; shared TLS parameters such as `skip-cert-verify`, `sni`, and certificate pinning.

- UDP Relay

---
## Policies / Hysteria 2

# Hysteria 2 iOS 5.8.0+ Mac 5.4.0+


Hysteria 2 is a proxy protocol built on QUIC, designed for high throughput on lossy networks. It always encrypts traffic with TLS over QUIC and supports both TCP and UDP relay with connection multiplexing.


[Proxy]
Proxy-Hysteria = hysteria2, 192.168.20.6, 443, password=pwd, download-bandwidth=100
## Parameters


#### password


Required. The authentication password, which must match the server's setting.


#### download-bandwidth


Optional. In Mbps.


Advertise the expected download bandwidth to the server as a hint for Hysteria's congestion control.


#### port-hopping


Optional.


Configure a list of ports or ranges, separated by semicolons (for example `1234;5000-6000`). Surge periodically rotates among them instead of using the main port. When this parameter is set, the primary port in the declaration is ignored.


Port hopping cannot be combined with the `underlying-proxy` parameter.


#### port-hopping-interval


Optional. In seconds. Default: 30.


The interval for rotating among the configured ports.


#### salamander-password Mac 6.4.3+


Optional. Enable Salamander obfuscation using the specified password.


Cannot be combined with `gecko-password`; the two obfuscation modes are mutually exclusive.


#### gecko-password iOS 5.20.0+ Mac 6.7.0+


Optional. Enable Gecko obfuscation using the specified password.


Cannot be combined with `salamander-password`; the two obfuscation modes are mutually exclusive.


## Notes


- UDP relay is always supported; no extra parameter is needed. See UDP Relay.

- The default ALPN value is `h3`; use the `alpn` parameter to override it.

- As a QUIC-based protocol, Hysteria 2 enables ECN by default on supported systems. See the `ecn` parameter in Common Policy Parameters.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.

- TLS Parameters &#x2014; shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.

- UDP Relay

---
## Policies / AnyTLS

# AnyTLS iOS 5.17.0+ Mac 6.4.3+


AnyTLS is a TLS-based proxy protocol designed to mitigate TLS-in-TLS fingerprinting by using flexible traffic padding. Surge supports the AnyTLS v2 protocol.


[Proxy]
Proxy-AnyTLS = anytls, 192.168.20.6, 443, password=pwd
## Parameters


#### password


Required. The authentication password, which must match the server's setting.


#### reuse


Optional. Boolean. Default: true.


According to the AnyTLS specification, connection reuse is enabled by default. Set `reuse=false` to disable it.


## Notes


- AnyTLS always encrypts traffic with TLS; all shared TLS parameters apply.

- UDP relay is supported (UDP over TCP); no extra parameter is needed. See UDP Relay.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.

- TLS Parameters &#x2014; shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.

- UDP Relay

---
## Policies / Trust Tunnel

# Trust Tunnel Mac 6.4.4+


Trust Tunnel is a TLS-based proxy protocol developed and maintained by AdGuard. Surge currently supports the HTTP/2 (TCP) mode, which relays TCP connections as multiplexed streams over an HTTP/2 connection. UDP forwarding is not yet supported.


[Proxy]
Proxy-TrustTunnel = trust-tunnel, 192.168.20.62, 443, username=test, password=test
## Parameters


#### username


Required. The username for authentication.


#### password


Required. The password for authentication.


#### headers Mac 6.6.0+


Optional. Add custom request headers to proxy handshake requests, with the same syntax and `<random-string>` placeholder support as for HTTP proxies. See HTTP proxy parameters for the full description.


Proxy = trust-tunnel, example.com, 443, username=test, password=test, headers=X-Padding:<random-string(16-32)>
#### max-streams Mac 6.6.0+


Optional. Default: 3. The maximum number of multiplexed sub-connections over the same TCP connection. See HTTP proxy parameters for details.


## Notes


- Trust Tunnel always encrypts traffic with TLS; all shared TLS parameters apply.

- UDP relay is not supported. See UDP Relay for how Surge handles UDP requests matched to a policy without UDP support.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.

- TLS Parameters &#x2014; shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.

- UDP Relay

---
## Policies / SSH

# SSH


Surge can use the SSH protocol as a proxy policy, an equivalent to `ssh -D`. Surge multiplexes requests as channels over a single SSH session.


[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw
## Authentication


Either `password` or `private-key` must be provided.


- Password authentication:


[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw

- Public key authentication, with the private key stored in the Keystore section:


```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, private-key=key1

[Keystore]
key1 = type=openssh-private-key, base64=[The base64 encoded content of the private key file]

```

You must use base64 to encode the entire private key file again, even though the private key file uses the base64 encoding itself.


All four types of private keys, RSA/ECDSA/ED25519/DSA, are supported. ECDSA P-521 private keys can be imported starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. iOS 5.21.0+ Mac 6.8.0+


## Parameters


#### username


Required. The SSH login user.


#### password


The password for authentication. Required unless `private-key` is used.


#### private-key


The name of an item in the Keystore section containing an OpenSSH private key. Required unless `password` is used.


#### idle-timeout


Optional. In seconds. Default: 180.


Tear down the SSH connection after it has been idle for this long.


[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180
#### server-fingerprint


Optional. Pin the server's public key fingerprint. See Pinning the Server Fingerprint below.


## Algorithm Requirements


Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. It means that the SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)


## Pinning the Server Fingerprint


To cope with MITM attacks, you can specify the server's public key fingerprint with `server-fingerprint`, which ensures that only legitimate servers are connected.


Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, Surge emits a one-time security warning when connecting without a configured fingerprint. iOS 5.21.0+ Mac 6.8.0+


[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180, server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz"
As there may be multiple public keys for a server, the `server-fingerprint` parameter supports configuring multiple fingerprints, separated by commas.


server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz,ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7aoFCymj8NJL+xMqYzRLGpIfVd2sebgtnD3cplG7/lrvPGYIpRAOkKqdUBOkRd2x68JFe0u+gBHQxFkv8o81Saqr6qxcrq4mPiyqxOTRkvDMtYrjJ4AJZE26nCzHRCC7Ji6Mq2OtepTJcC9uk2LLcRrF3G05qu6ToeK1LgXgqc+b2RLOQJ1AXEeNgn0NIXWlBv4AhQRJ6fFQi4HO/jkxpFNfzKY+dPDx6P3VAazYa2nl8wpLbXt+tq6SBv8RctwDuYszAbjSCPPJq7ToX/Svqqbl82qtOLOofcQ8/f8809i4RQ0yuEpVLnVVWd7cZx5h45vt+/I1Ifr2pS7BqhLL/,ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLdhR3D2BvyD7FTXfx0CrjZF2tVgoVRFi1poGKoX0eXc9OlpiaqNos4niiN0GWyoT4mL724cgvaL+vHW8sTZE5A="
If the server's sshd supports ed25519, only the fingerprint of ssh-ed25519 is needed.


You may obtain the server fingerprint from the `~/.ssh/known_hosts` file. Or you may use the command `ssh-keyscan example.com` in a trusted network environment to fetch it. Remove the hostname at the front of the line before copying it to Surge.


## Notes


- UDP relay is not supported. See UDP Relay for how Surge handles UDP requests matched to a policy without UDP support.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.

- Keystore &#x2014; storing private keys and certificates.

- UDP Relay

---
## Policies / WireGuard

# WireGuard


The `wireguard` policy type turns a layer-3 WireGuard tunnel into a regular Surge outbound policy. Surge maintains an internal IP stack for each WireGuard policy, encrypts each packet for the peer selected by `allowed-ips`, and sends the encrypted UDP datagrams either directly or through another policy. Both TCP and UDP relay are supported.


A WireGuard policy is an application-level outbound policy. It does not install a system-wide WireGuard VPN: only connections selected by Surge rules, policy groups, or manual selection enter the tunnel. The device's global route table is not changed.


A complete configuration has two parts: a policy line in `[Proxy]` and a matching `[WireGuard <section-name>]` section. The section may be placed in a detached profile section.


## Quick Start


A peer-to-peer policy that reaches a private subnet by IP:


[Proxy]
Office WG = wireguard, section-name=office-wg

[WireGuard office-wg]
private-key = <client-private-key>
self-ip = 10.20.0.2
mtu = 1280
peer = (public-key = <server-public-key>, allowed-ips = "10.20.0.0/24, 192.168.50.0/24", endpoint = vpn.example.com:51820)

[Rule]
IP-CIDR,192.168.50.0/24,Office WG,no-resolve
A general proxy policy that routes Internet traffic through a WireGuard gateway:


[Proxy]
WG Gateway = wireguard, section-name=wg-gateway

[WireGuard wg-gateway]
private-key = <client-private-key>
self-ip = 10.30.0.2
dns-server = 10.30.0.1
mtu = 1280
peer = (public-key = <server-public-key>, allowed-ips = 0.0.0.0/0, endpoint = gateway.example.com:51820, keepalive = 25)
The presence of `dns-server` decides the policy's role:


- Peer-to-peer policy (no `dns-server`): intended for IP-based access to specific peers or private routes. Destination names cannot normally be resolved through the policy; use IP-based rules. The default latency test is a native WireGuard RTT probe.

- General proxy policy (one or more `dns-server` values): treated as a normal outbound proxy and tested with the standard URL test.


This classification is static and only selects the default test mechanism and the tests offered in the runtime UI. Actual reachability is always determined by peer `allowed-ips`, server-side routing, and server-side forwarding/NAT. `allowed-ips = 0.0.0.0/0` only selects a peer inside Surge; the server must still forward the traffic and normally perform source NAT for Internet access.


## Prerequisites and Limitations


Prepare in advance: a client private key, at least one peer public key, a unique client tunnel IPv4/IPv6 address, the peer endpoint host and UDP port, and the destination prefixes routed to each peer. For a general proxy policy, also a DNS resolver reachable inside the tunnel and a peer route covering it.


- Surge acts as a WireGuard client only; it does not expose a WireGuard server.

- Key distribution, address assignment, and server configuration are outside the WireGuard protocol and must be prepared separately.

- WireGuard returns no descriptive authentication or routing errors. Invalid keys, blocked UDP, missing routes, and missing server-side NAT all commonly appear as timeouts.

- The main supported payloads are TCP and UDP. Surge only answers ICMP/ICMPv6 echo requests sent to the configured local tunnel address.

- The graphical editor supports one peer; configure multiple peers in profile text.

- Treat private and preshared keys as secrets; they are masked when Surge exports a profile without sensitive data. Reusing the same private key or tunnel address on simultaneously active devices can cause route conflicts, handshake instability, or traffic delivery to the wrong device.


## Policy Line


[Proxy]
Office WG = wireguard, section-name=office, test-timeout=8, ecn=true
Common policy parameters apply, with L3-specific exceptions: `interface` binding and the `shadow-tls-*` parameters are not supported for WireGuard policies.


#### `section-name`


Required.


Name of the `[WireGuard <name>]` section used by this policy. It must exactly match the section suffix. The referenced section must contain a private key, at least one local tunnel address, and at least one complete peer. Section names are profile identifiers only; they are not sent to the peer.


#### `underlying-proxy`


Optional, policy or group name, default: DIRECT.


Transports the encrypted WireGuard UDP datagrams through another Surge policy. Without it, Surge resolves peer endpoint hostnames with the normal Surge DNS resolver and sends datagrams directly from the selected physical interface. With it:


- encrypted datagrams are carried by a Surge UDP connector through the selected policy;

- endpoint hostname resolution can occur through that connector rather than locally;

- a policy group is evaluated to its current final policy, and a change of the effective policy resets the WireGuard transport sockets.


Avoid dependency loops in which the underlying policy eventually selects the same WireGuard policy. `underlying-proxy` only affects transport to the peer endpoint; it is unrelated to `dns-server`, which resolves destination names inside the tunnel.


#### `test-url`


Optional, plain `http://` URL.


Forces the standard URL test even when the policy has no `dns-server` and would otherwise use the native RTT probe. Only plain HTTP URLs are accepted. The host must be resolvable and routable through the WireGuard policy &#x2014; for a peer-to-peer configuration, use an IP-literal or internal URL reachable through the configured routes.


#### `test-timeout`


Optional, in seconds, default: global `test-timeout`, otherwise 5.


Limits the actual RTT probe or HTTP test. Surge additionally allows up to 10 seconds for L3 initialization (endpoint resolution, socket setup, first handshake), so `test-timeout=5` can take up to about 15 seconds when the session must first be initialized.


## WireGuard Section


[WireGuard office]
private-key = <client-private-key>
self-ip = 10.20.0.2
peer = (public-key = <peer-public-key>, allowed-ips = 10.20.0.0/24, endpoint = vpn.example.com:51820)
#### `private-key`


Required.


Client private key, in standard WireGuard Base64 encoding or as a 64-character hexadecimal representation of the 32-byte key.


#### `self-ip`


Conditional: at least one of `self-ip` and `self-ip-v6` is required.


Client IPv4 tunnel address. This is a plain address, not a CIDR prefix, and must match the client address expected by the remote configuration. Each simultaneously active client should use a unique address.


#### `self-ip-v6`


Conditional: at least one of `self-ip` and `self-ip-v6` is required.


Client IPv6 tunnel address. The configured address families also determine which tunneled DNS resolver families are usable: an IPv4 DNS server requires `self-ip`; an IPv6 DNS server requires `self-ip-v6`.


#### `dns-server`


Optional, comma-separated resolvers.


DNS resolvers used inside the tunnel, e.g. `dns-server = 10.20.0.1, fd00:20::1`. Accepted entries are plain IPv4/IPv6 addresses, supported IP-and-port forms, and `system`. IPv4 multicast addresses and encrypted-DNS URLs are not accepted.


Queries to these resolvers travel through the WireGuard session, so each resolver needs a matching `allowed-ips` route and must be reachable on the remote network. The presence of this field also classifies the policy as a general proxy policy (see Quick Start).


The `dns-server` field does not resolve the peer's `endpoint` hostname. Endpoint lookup uses normal Surge DNS when transport is direct, or the underlying connector when `underlying-proxy` is configured.


#### `prefer-ipv6`


Optional, Boolean, default: false.


When both local address families are configured and a destination name returns both A and AAAA records, prefer IPv6. It does not create IPv6 routes or reachability by itself.


#### `mtu`


Optional, 576&#x2013;1420, default: 1280.


Layer-3 tunnel MTU. Surge drops an outbound packet that exceeds it. Too large a value may produce stalls or black holes on paths with extra encapsulation (lower it if large transfers stall); an unnecessarily small value increases overhead.


#### `peer`


Required, one or more peer definitions.


Each peer is a parenthesized field list; multiple peers are separated by commas, and multiple `peer =` lines accumulate:


peer = (public-key = <peer-a-key>, allowed-ips = 10.10.0.0/16, endpoint = a.example.com:51820), (public-key = <peer-b-key>, allowed-ips = 10.20.0.0/16, endpoint = b.example.com:51820)
## Peer Fields


#### `public-key`


Required.


The remote peer's public key, Base64 or 32-byte hexadecimal.


#### `allowed-ips`


Required, comma-separated IPv4/IPv6 CIDRs (quote the value if it contains commas).


Defines which outbound destination prefixes select this peer. Surge builds separate IPv4 and IPv6 route tables from all peers' `allowed-ips` and uses the most specific matching prefix; a narrow route on one peer overrides a broader route on another (e.g. a `10.0.0.0/8` peer wins over a `0.0.0.0/0` peer for those addresses). If no route matches, Surge logs the missing route and drops the packet &#x2014; unmatched traffic is never sent directly as a fallback.


A default route (`0.0.0.0/0`, `::/0`) only makes all addresses select the peer; it neither proves the peer forwards Internet traffic nor changes the policy classification.


#### `endpoint`


Required, host and UDP port.


The peer address, e.g. `vpn.example.com:51820`. IPv4 addresses, IPv6 addresses in supported host-and-port syntax (e.g. `[2001:db8::10]:51820`), and domain names are accepted. Surge periodically re-resolves domain endpoints and updates the transport address if the result changes; if the address family changes, transport sockets are rebuilt.


#### `preshared-key`


Optional.


An additional 32-byte symmetric key added to the handshake. It must match the peer configuration exactly.


#### `keepalive`


Optional, in seconds, 0&#x2013;65535, default: 0 (disabled).


WireGuard persistent keepalive interval, commonly used when the client is behind NAT and the mapping must stay active. Avoid unnecessarily short intervals; they increase background traffic and power use.


#### `client-id` iOS 5.3.1+ Mac 4.10.3+


Optional.


Some services &#x2014; such as Cloudflare WARP &#x2014; use bytes 1&#x2013;3 of the WireGuard packet's reserved area as a client or routing ID. Surge writes these bytes on outbound packets and clears them on inbound packets before WireGuard processing. Accepted forms: slash-separated decimals (`client-id = 83/12/235`), three-byte hexadecimal, or four-character Base64. Leave it unset for standard WireGuard deployments.


[WireGuard warp]
private-key = <client-private-key>
self-ip = 172.16.0.2
self-ip-v6 = 2606:4700:110:0000::2
dns-server = 1.1.1.1, 2606:4700:4700::1111
peer = (public-key = <peer-public-key>, allowed-ips = "0.0.0.0/0, ::/0", endpoint = engage.cloudflareclient.com:2408, client-id = 83/12/235)
## Lifecycle


WireGuard sessions are prepared at profile load; sockets and handshakes start on demand. Surge builds the route tables, resolves endpoints, evaluates `underlying-proxy`, creates one UDP transport per peer, and forces initial handshakes; the session is ready once a peer returns a valid WireGuard packet. Surge then advances the WireGuard timers for retransmission, rekeying, keepalive, and expiration, and requests a new handshake when traffic needs an expired peer.


A network change or an effective underlying-policy change invalidates the sockets and triggers reconstruction. Incoming fragments can be reassembled before delivery.


## Policy Testing iOS 5.20.0+ Mac 6.7.0+


The test mode is selected statically from the profile:


- no `dns-server` and no explicit `test-url`: native WireGuard RTT probe;

- one or more `dns-server` values, or an explicit `test-url`: standard URL test.


Native RTT probe: Surge starts or resumes the session, forces a handshake to every configured peer, and completes when the first peer returns a valid WireGuard packet, reporting the round-trip time and responding endpoint. The result measures peer reachability and handshake RTT only &#x2014; it does not prove that routes, DNS, or Internet egress work. With multiple peers, the fastest peer completes the test.


Standard URL test: the same HTTP test path as normal proxies, covering destination resolution, routing, WireGuard transport, remote forwarding, and the HTTP response. A failure can therefore mean a handshake failure, a missing `allowed-ips` route, an unreachable tunnel DNS server, missing remote forwarding/NAT, a blocked destination, or an HTTP timeout. An explicit `test-url` can point at a service inside the private network to test a peer-to-peer policy against a specific application.


Both modes allow an extra 10 seconds for L3 initialization on top of `test-timeout`. The first test after a network change or long inactivity may be slower because endpoint DNS, sockets, and handshakes must be recreated.


The runtime detail view shows the effective underlying policy, active TCP/UDP counts, peer endpoints and handshake states, and recent errors. For a peer-to-peer policy, only the RTT test is offered; a general proxy policy keeps the standard latency, DNS, UDP, and external-address tests.


## ECN and DSCP


ECN iOS 5.8.0+ Mac 5.4.0+ is a policy-line option, not a section field, and is disabled by default for WireGuard policies:


[Proxy]
WG Gateway = wireguard, section-name=wg-gateway, ecn=true
On supported OS versions, Surge preserves ECN information for tunneled traffic and applies RFC 6040-style merging on received markings. Disable it if it causes connectivity problems on an incompatible network. See Common Policy Parameters.


Following the WireGuard protocol recommendation, Surge marks handshake packets with DSCP `0x88` (AF41) to improve handshake success on networks that honor this class. Regular tunnel packets are not automatically marked.


## Troubleshooting


- The RTT test times out. Check keys (including any preshared key), endpoint host/port, firewalls, UDP reachability on the current network, `underlying-proxy` UDP support, duplicate client keys or addresses, and whether any peer is online. Because WireGuard produces no descriptive remote errors, most configuration mistakes appear as timeouts.

- Handshake works but a private address is unreachable. Verify the destination is covered by the intended peer's `allowed-ips`, then remote routing and firewall policy. A handshake proves only that the peers can exchange authenticated packets.

- URL test fails but RTT works. Check `dns-server` reachability through `allowed-ips`, default or destination routes, remote IP forwarding, source NAT, the test URL, and IPv4/IPv6 family compatibility.

- Domain names do not resolve. Confirm `dns-server` is present, uses a family with a configured local address, is covered by `allowed-ips`, and permits queries from the client. Only IP addresses working is expected behavior for a peer-to-peer policy without `dns-server`.

- One of several peers never receives traffic. Inspect overlapping `allowed-ips`; longest-prefix matching may always select another peer.

- Large transfers stall. Lower `mtu` and retest; encapsulation through another proxy or a small-MTU path can black-hole large packets while handshakes still work.


For a Tailscale-managed WireGuard mesh, see the Tailscale policy.

---
## Policies / Tailscale

# Tailscale iOS 5.20.0+ Mac 6.7.0+


The `tailscale` policy type joins a tailnet as a node and exposes that tailnet as a Surge outbound policy, supporting both TCP and UDP relay. Surge registers the node with the control server, receives the peer, route, DNS, and DERP configuration, creates WireGuard tunnels to authorized peers, uses direct UDP paths where possible and DERP relays otherwise, routes each packet to the best-matching peer, and resolves MagicDNS names inside the policy &#x2014; all without installing a separate system VPN.


A Tailscale policy is an application-level outbound policy, not a replacement for the system Tailscale client: only traffic selected by Surge rules or an explicit policy choice uses the tailnet. Interactive sign-in, automatic MagicDNS and peer-address routing, and the always-on session default require Surge iOS 5.21.0 or Surge Mac 6.8.0. Earlier versions require an auth key and explicit routing rules, and tear down an idle session after 600 seconds by default. iOS 5.21.0+ Mac 6.8.0+


A complete configuration has two parts: a policy line in `[Proxy]` and a matching `[Tailscale <section-name>]` section.


## Quick Start


[Proxy]
My Tailnet = tailscale, section-name=my-tailnet

[Tailscale my-tailnet]
auth-key = tskey-auth-example
hostname = surge-mac
`section-name` must exactly match the section suffix. As an alternative to `auth-key`, open the Tailscale policy editor in Surge and complete interactive sign-in; Surge then saves the section with `interactive-login = true`. The two login methods are mutually exclusive, and copying an `interactive-login` line to another device does not copy the locally stored identity.


Automatic routing is enabled by default: after the session discovers the tailnet, Surge routes its MagicDNS suffix and the individual IPv4/IPv6 addresses of visible peers to this policy. You can still select the policy directly or add explicit rules for subnet routes or broader ranges:


[Rule]
DOMAIN-SUFFIX,example-tailnet.ts.net,My Tailnet
IP-CIDR,100.64.0.0/10,My Tailnet,no-resolve
The actual MagicDNS suffix and address ranges are assigned by the control plane &#x2014; use the values shown by your tailnet. Set `auto-add-magic-dns-rule = false` if all routing should be controlled by explicit rules.


## Prerequisites and Limitations


You need a Tailscale (or compatible) control server account, plus either an auth key that can register a node without interactive login or access to Surge's policy editor for interactive sign-in, and any required ACL, subnet-route, or exit-node approvals in the control plane. Treat auth keys as secrets: a valid reusable key can add a node to the tailnet, subject to its server-side restrictions.


- The policy handles outbound traffic selected by Surge. It does not advertise this device as a subnet router or exit node, and does not expose inbound services to the tailnet.

- The control server still determines ACLs, peer visibility, routes, DNS settings, exit-node availability, and node authorization. A route advertised by a peer is usable only when the control plane delivers it to this node.


## Policy Line


[Proxy]
Office Tailnet = tailscale, section-name=office, test-timeout=8
Common policy parameters apply, with L3-specific exceptions: `interface` binding and the `shadow-tls-*` parameters are not supported.


#### `section-name`


Required.


Name of the `[Tailscale <name>]` section used by this policy. The referenced section must exist and configure exactly one login method: `auth-key` or `interactive-login = true`.


#### `underlying-proxy`


Optional, policy or group name, default: DIRECT.


By default, DERP, STUN, and direct peer-path traffic originate through DIRECT. When `underlying-proxy` is configured, DERP relay connections use that policy and direct physical UDP sockets are disabled, so peer traffic uses DERP relay transport only. This prevents accidental bypass of the requested policy, but means a chained Tailscale policy usually has higher latency and depends on DERP availability. A policy group is evaluated to its current final policy. Avoid dependency loops in which the underlying policy eventually selects the same Tailscale policy.


Access to `control-url` is a separate case: Surge handles it through the standard outbound mode and the normal rule system, and `underlying-proxy` has no effect on it (see `control-url`).


#### `test-url`


Optional, plain `http://` URL (HTTPS is not accepted).


Always selects the standard URL test. If no exit node or advertised route can reach the URL, the test fails even when tailnet peer connectivity works. For a policy without an exit node, either omit `test-url` to use the native connectivity probe, or use a URL hosted on an address reachable through the tailnet.


#### `test-timeout`


Optional, in seconds, default: global `test-timeout`, otherwise 5.


Limits the actual probe or HTTP test. Surge additionally allows up to 10 seconds for Tailscale initialization (control registration, netmap acquisition, DERP setup, first WireGuard handshake), so `test-timeout=5` may take up to about 15 seconds overall.


## Tailscale Section


Use only the documented fields below. The parser may ignore an unrecognized key, but this is not a supported extension mechanism; a malformed line or invalid value for a recognized key makes the profile invalid.


#### `auth-key`


One login method required; cannot be combined with `interactive-login`.


Auth key sent during node registration. A key that requires interactive approval cannot complete auth-key registration; use interactive sign-in instead. Recommended server-side restrictions: short expiration, single use unless reuse is required, preauthorization, and appropriate tags and ACLs. The key is omitted or masked when Surge exports a profile without sensitive data.


Surge stores the Tailscale machine identity in a local state file selected by a SHA-256 hash of the auth key, so reusing the same key and profile preserves the identity across restarts; changing the key normally creates a different node identity.


#### `interactive-login` iOS 5.21.0+ Mac 6.8.0+


One login method required, Boolean, default: false; cannot be combined with `auth-key`.


Uses an identity authorized through Surge's interactive Tailscale sign-in (macOS and iOS). Start sign-in from the policy editor and open the authorization URL supplied by the control server; Surge then stores the machine and node identity locally and writes `interactive-login = true` instead of an auth key.


The line is only a reference to local login state &#x2014; it contains no transferable credentials and does not start a browser login by itself. If the local state is missing or damaged, Surge asks you to sign in again from the policy editor. The state is associated with the section name, so renaming the section may require signing in again.


#### `control-url`


Optional, URL, default: `https://controlplane.tailscale.com`.


Control server URL, for the standard Tailscale control plane or a compatible service such as a privately operated control server. HTTPS is strongly recommended; the initial server-key retrieval is protected with HTTPS even when an `http` URL is supplied, while subsequent transport follows the configured URL.


Surge accesses this URL through the standard outbound mode and the normal rule system; `underlying-proxy` does not participate. Configure the desired route with rules &#x2014; and make sure the matching rule does not select this Tailscale policy, directly or through a policy group. That recursive selection deadlocks: the policy waits for the control connection, while the control connection waits for the policy.


#### `hostname`


Optional, default: a platform-derived name such as `surge-macos`.


Node hostname sent during registration, normalized to lowercase. The DNS name displayed by MagicDNS may include an additional tailnet suffix assigned by the control plane.


#### `derp-only`


Optional, Boolean, default: false.


Forces all encrypted peer traffic through DERP relays even when the effective underlying policy is DIRECT. In DERP-only mode, no physical peer-to-peer UDP sockets are opened; STUN netcheck, direct endpoint discovery, discovery pings, and direct-path heartbeats are disabled; and previously learned direct-path state is not used. DERP connections still use the effective underlying policy, and control-plane connections continue to follow the rule system.


A non-DIRECT `underlying-proxy` already makes the transport DERP-only; this field is useful when the surrounding connections should remain direct but peer-to-peer UDP must not be attempted.


#### `auto-add-magic-dns-rule` iOS 5.21.0+ Mac 6.8.0+


Optional, Boolean, default: true.


Once Surge receives the tailnet's network map and DNS configuration, it automatically routes the discovered MagicDNS domain suffix and each visible peer's individual IPv4 and IPv6 tailnet addresses to this policy, refreshing the routes as the map changes. The option name is retained for compatibility, but it controls both the MagicDNS suffix rule and the peer-address rules.


Advertised subnet routes, exit-node traffic, and other broader destinations still require explicit rules or manual policy selection. When enabled, Surge starts the session right after loading the profile so the required information can be discovered before matching traffic arrives.


#### `exit-node`


Optional, default: `none`.


- `none`: disable exit-node routing; default routes from all peers are ignored while more specific routes remain usable. If default-route traffic is attempted while usable exit nodes exist, Surge drops the packet and reports a one-time warning naming the available nodes, so a missing setting is not mistaken for a connectivity failure.

- `auto`: select an exit node only when exactly one usable candidate exists. With zero or with two or more candidates, none is selected &#x2014; the ambiguity is intentional, because an arbitrary choice could change egress location or trust boundaries; a warning lists the candidates when default-route traffic is attempted.

- An explicit selector: match one peer by stable ID, full DNS name, short DNS name (the first label), or tailnet IPv4/IPv6 address. Matching is case-insensitive and ignores a trailing dot. The match must be unique and the peer usable; a missing, offline, or ambiguous match produces no exit-node route and no fallback.


exit-node = office-exit.example-tailnet.ts.net
An exit-node candidate is a peer advertising an IPv4 or IPv6 default route; it is usable only while present, online, and with an allocated tunnel. Only the selected node's default routes are installed, so overlapping exit nodes never compete in the route table. Even with an exit node, Surge does not change the device's global default route &#x2014; the node receives only the connections Surge assigned to this policy.


#### `idle-keepalive` iOS 5.21.0+ Mac 6.8.0+


Optional, in seconds, default: always on.


Controls how long an unused session stays alive after its last TCP connection or UDP mapping closes. A positive value tears down networking after that many idle seconds (the idle monitor checks periodically, so teardown may occur slightly late); omitted, `0`, or `-1` keeps the session running continuously. Idle teardown closes control and DERP connections and releases peer tunnels and routes, but preserves the local key state; the next connection restarts networking, so the first operation after teardown pays control, route, and handshake latency. Use a positive value such as `600` only when reducing background network and memory usage matters more than restart latency.


#### `prefer-ipv6`


Optional, Boolean, default: false.


Prefer IPv6 for the layer-3 session and DNS result selection when both families are available. It does not create IPv6 connectivity by itself.


#### `dns-server`


Optional, comma-separated resolvers, default: resolvers from the control plane.


Overrides the resolver list received from the control plane. Accepted entries are plain IPv4/IPv6 addresses or an IP with a port in Surge's supported address-and-port syntax; IPv4 multicast addresses are rejected, and encrypted-DNS (DoH/DoQ/DoT) URLs do not belong here. Control-provided search domains and locally synthesized MagicDNS records are still applied.


The resolver must be reachable through this policy's route table &#x2014; a resolver at a tailnet IP requires an authorized peer route for that IP; an unroutable resolver causes lookup failures.


#### `mtu`


Optional, 576&#x2013;1420, default: 1280.


Layer-3 MTU; larger packets are dropped. The conservative default works well across direct UDP, DERP, IPv4, and IPv6 paths. Increase it only when the entire path supports it; lower it when diagnosing fragmentation or black-hole behavior.


## More Examples


An explicit exit node &#x2014; only traffic assigned to the policy uses it:


[Proxy]
Tailnet Exit = tailscale, section-name=tailnet-exit, test-timeout=8

[Tailscale tailnet-exit]
auth-key = tskey-auth-example
hostname = surge-exit-client
exit-node = office-exit.example-tailnet.ts.net
A custom control server with a custom resolver:


[Tailscale private-tailnet]
auth-key = tskey-auth-example
control-url = https://control.example.com
hostname = surge-private
dns-server = 100.64.0.53
Chained through another policy (peer traffic uses DERP over the upstream; direct UDP is disabled):


[Proxy]
Tailnet via Proxy = tailscale, section-name=chained-tailnet, underlying-proxy=Upstream
A test URL inside the tailnet &#x2014; the URL must resolve and route through it:


[Proxy]
Office Tailnet = tailscale, section-name=office, test-url=http://health.office.example-tailnet.ts.net/, test-timeout=8
## Routing and Transport


Each authorized peer arrives with a set of allowed IP prefixes. Surge builds separate IPv4 and IPv6 route tables and uses the most specific matching route for each outbound packet: a `100.x.y.z/32` route reaches an individual node, a subnet route such as `10.20.0.0/16` reaches the authorized subnet router advertising it, and a default route represents exit-node capability (handled per `exit-node`). If no route matches, the packet cannot be delivered &#x2014; Surge never bypasses the policy and sends it directly.


Surge creates a WireGuard tunnel per usable peer, may proactively handshake online peers, advances the WireGuard timers on a shared schedule, and rehandshakes expired tunnels that active connections depend on. Encrypted packets are handed to MagicSock, which chooses a direct endpoint or DERP relay path.


Direct UDP paths. When the effective underlying policy is DIRECT and `derp-only` is disabled, Surge opens physical UDP sockets bound to the primary physical interface (so Tailscale's own transport packets do not loop back into the Surge virtual interface). An IPv6 socket is opened only when the network provides IPv6 connectivity; its absence does not prevent IPv4 direct paths or DERP.


DERP relay. DERP provides a relay path when direct connectivity is unavailable or not yet discovered &#x2014; a valid working state, just with higher latency. Surge picks a provisional DERP region, later refined by netcheck latency measurements; the home DERP connection is established during startup, other regions are opened lazily, and home-region reconnects use increasing backoff.


Netcheck and discovery. After the DERP map and sockets are ready, Surge runs network checks at most about once per minute: it probes STUN endpoints for public reflexive addresses, measures DERP reachability, and reports updated endpoints and the preferred region to the control plane. When no trusted direct path exists, traffic flows through DERP while rate-limited peer endpoint discovery probes candidates and exchanges endpoint information via DERP. A responsive direct endpoint is trusted for a short interval, active paths receive heartbeats, unanswered pings expire, and an alternative endpoint replaces the current best one only when meaningfully faster, avoiding path flapping. Runtime peer status shows whether the current path is `direct` or `relay`, with the endpoint and measured latency.


## DNS and MagicDNS


Surge picks resolvers in order: `dns-server` from the section, then resolvers delivered by the control plane. The list is private to this policy; it does not replace the device's system DNS.


When MagicDNS is enabled, Surge synthesizes local DNS records from the local node's DNS name and addresses, each visible peer's DNS name and addresses, and extra records supplied by the control plane. Names are normalized to lowercase without a trailing dot; both IPv4 and IPv6 records may be present, with `prefer-ipv6` steering the choice. Control-plane search domains are applied to the policy DNS client, though fully qualified names remain the clearest choice in profiles and diagnostics.


DNS queries themselves travel through the Tailscale policy, so an upstream resolver address needs a matching peer route. If names appear in runtime status but external tailnet DNS queries time out, verify the resolver address and its authorized route.


## Lifecycle


The session has four runtime states: `idle` (networking not running), `starting`, `ready`, and `failed` (terminal startup or authorization error). By default the session starts after profile load and stays active even when unused, keeping control and relay state warm; with a positive `idle-keepalive` it may stop and restart on demand.


Persistent machine, node, and network-lock key material lives in application-support storage (state file named from the auth-key hash or, for interactive login, the section name; the path-discovery key is ephemeral). This lets a session restart without replacing its cryptographic identity &#x2014; protect that storage as you would the auth key. Registration requests a non-ephemeral node: Surge fetches the control server key, establishes a Noise-based control transport, registers over HTTP/2 with the machine/node/network-lock keys, hostname, endpoints, and credentials, then starts the streaming map request. Runtime control stages appear as `idle`, `fetching-key`, `connecting`, `registering`, `map-streaming`, or `closed`.


The control stream delivers full maps (which rebuild peer and route state, reusing tunnels whose node keys are unchanged) and incremental changes. If no map frame arrives for about 150 seconds, Surge reconnects the stream; transient control errors retry with increasing delay from roughly 100 milliseconds up to 30 seconds, preserving the data plane where possible. An authorization failure is terminal for the current attempt: Surge tears down networking, reports the error, and fails new operations quickly; corrected configuration, a fresh sign-in, or a network change permits a new attempt (the network-change retry also covers false authorization symptoms from captive portals or TLS interception). The session becomes ready as soon as it has a valid network map and usable data plane &#x2014; it does not wait for the home DERP connection.


A network change invalidates old sockets; control and transport state are rebuilt, peer data is refreshed from the new netmap, and always-on sessions warm up again without waiting for traffic.


## Policy Testing


The test mode is decided statically from the configuration, not from live session state:


- No configured exit node and no explicit `test-url` &#x2014; the policy is treated as peer-to-peer, and Surge measures tunnel reachability with the native Tailscale connectivity probe: it prepares the session, then probes a bounded set of eligible online peers with Tailscale discovery ping (preferring peers with a trusted direct path), or pings the home DERP connection when no eligible peer is available. The result indicates whether the measured path is direct or relay; the reported RTT excludes session initialization time.

- A configured exit node (`auto` or explicit) or an explicit `test-url` &#x2014; the policy is expected to provide Internet egress, so Surge uses the standard URL test: an HTTP `HEAD` request through the policy. When the server permits connection reuse, a subsequent request yields a latency less dominated by connection setup. If a configured exit node is not currently usable (offline, ambiguous, or unmatched), the URL test runs and fails rather than silently falling back to the peer probe, surfacing the misconfiguration.


Both modes add up to 10 extra seconds for initialization and handshake work on top of the effective test timeout; the allowance and the probe budget share a single deadline rather than being applied twice.


The runtime status view shows the session state and control stage, hostname and control URL, local addresses and MagicDNS name, effective underlying policy and transport mode, connection counts, exit-node selector/candidates/selection, DERP regions, UDP ports and reported endpoints, last netcheck age, DNS configuration and synthesized records, and per-peer online state, path type, latency, and exit-node eligibility. The offered test controls follow the same static classification: a peer-to-peer policy exposes only the RTT test (throughput, UDP, and NAT-type tests require Internet egress), while an exit-node policy exposes the full set. A policy torn down by `idle-keepalive` may show little peer or transport information until something restarts it &#x2014; this is expected.


## Troubleshooting


- Registration fails immediately. Check for a missing/expired/revoked/malformed auth key, a consumed single-use key, both or neither login method configured, missing interactive-login state, a key that requires interactive authorization, a server-side rejection of the hostname/tags/registration, or clock, TLS-interception, or captive-portal problems. Replace the key or sign in again from the policy editor; a network change permits a retry after a captive-portal failure.

- The policy remains in `starting`. Read the control stage: `fetching-key`/`connecting` point to control URL, DNS, TLS, or rule-selected outbound issues; `registering` to auth or authorization issues; `map-streaming` means Surge may still be waiting for an address, DERP map, or usable data plane. Verify the ControlURL rule does not recursively select this policy, and that any `underlying-proxy` group resolves to a working final policy.

- The session has no local address. The control plane assigns tailnet addresses; confirm the node is authorized and the netmap includes them.

- A peer is visible but unreachable. Verify the peer is online, ACLs permit the traffic, the destination is within the peer's delivered routes, any subnet route is approved, the packet fits the MTU, and the service is listening. A `relay` path is slower but should work; if nothing works, inspect handshake and DERP status.

- Direct connectivity is never established. Expected with `derp-only = true` or a non-DIRECT `underlying-proxy`; otherwise restrictive NAT, firewalls, blocked UDP, or missing IPv6 may force DERP relay.

- `exit-node = auto` selects nothing. More than one candidate is online (configure an explicit selector) or none is usable (verify default-route advertisement and approval). An explicit selector must uniquely match an online candidate &#x2014; check spelling, suffix, stable ID, address, and approval; there is no fallback.

- MagicDNS names do not resolve. Check that MagicDNS is enabled in runtime DNS status, the name appears in synthesized records, the expected search domain was delivered, a custom `dns-server` is not overriding the intended resolver, and the resolver IP has a route through the policy. Try the FQDN and the tailnet IP to separate DNS from routing problems.

- A URL test fails while tailnet connections work. Without an exit node, a public URL is usually not routed through the policy: remove `test-url` to use the native probe, or use a tailnet-reachable URL. With an exit node, confirm it is selected and online. A first test may take the timeout plus the 10-second initialization allowance.

- First use after inactivity is slow. Occurs with a positive `idle-keepalive`: the session must restart networking and handshake again. Remove the option (or set `0`/`-1`) for always-on behavior.

- Large transfers stall. The configured MTU may exceed the path MTU; return to `mtu = 1280` or lower while testing.


Operational guidance: prefer HTTPS control URLs; limit auth-key lifetime, reuse, tags, and ACLs; remember an exit node can observe and egress the traffic assigned to it, so select it explicitly when multiple candidates exist; treat a custom control server and DERP infrastructure as part of the trust boundary; review control-plane ACLs and route approvals rather than relying only on Surge rules.


Tailscale is a trademark of Tailscale Inc. This document describes Surge's compatible policy implementation and its behavior; it does not describe every feature of the standalone Tailscale client or control service.

---
## Policies / External Proxy Program

# External Proxy Program Mac Only


Surge Mac supports the External Proxy Program policy, which allows Surge to work with other proxy software: Surge launches an external program and forwards requests to the local SOCKS5 port it listens on.


The following is an SSH example. The policy type keyword is `external`.


[Proxy]
external = external, exec = "/usr/bin/ssh", args = "11.22.33.44", args = "-D", args = "127.0.0.1:1080", local-port = 1080, addresses = 11.22.33.44
Surge iOS does not support external proxy programs. The `external` policy is treated as `REJECT` on iOS.


## Parameters


#### exec


Required. The path of the external program's executable.


#### local-port


Required. The SOCKS5 port that the external program listens on at 127.0.0.1. Surge forwards requests to this port.


#### args


Optional. A command-line argument passed to the external program. The parameter can be used repeatedly to append multiple arguments in order.


#### addresses


Optional. A proxy server IP address to be excluded from the VIF routes when Enhanced Mode is on. The parameter can be used repeatedly to append multiple addresses. Hostnames and domains are not supported.


#### udp-relay


Optional. Boolean. Default: false.


Relay UDP traffic through the external program's local SOCKS5 port. The external program must support SOCKS5 UDP relay.


## Lifecycle


Surge will do the following:


- When the policy is used, Surge starts the external process with the `exec` and `args` parameters, then forwards the request to SOCKS5 `127.0.0.1:[local-port]`.

- If the external process is terminated, Surge restarts it automatically when the policy is used.

- Surge automatically excludes the addresses in the `addresses` parameter from the VIF routes when Enhanced Mode is on. Use the proxy server IP address in this field. Hostnames and domains are not supported.

- Surge always uses the `DIRECT` policy for requests from external processes. Children of external processes are handled the same way for plugin programs such as `obfs-local`.

- Surge automatically shuts down all external processes when it exits, and automatically cleans up route table items when Enhanced Mode shuts down.


Some notes:


- The behavior of items 3 and 4 overlaps. Prefer the `addresses` declaration to exclude VIF processing, which reduces processing overhead. Item 4 is an additional protection.

- stdout and stderr of external processes are redirected to `/tmp/Surge-External-xxxxxx.log` for troubleshooting.

- External processes may take a short time to start. If a connection refused error is encountered when forwarding to `127.0.0.1:[local-port]`, Surge automatically retries after 500 ms, up to 6 times per request.


## See Also


- Common Policy Parameters &#x2014; shared parameters such as `interface`, `tfo`, and `test-url`.

- UDP Relay

---
## Policy Groups / Overview

# Policy Groups


A policy group contains multiple policies and exposes them as a single policy name. Rules can then reference the group instead of a concrete policy, so you can change how traffic is routed without touching the rules. A group may contain built-in policies, proxy policies, or other policy groups.


Policy groups are declared in the `[Proxy Group]` section:


[Proxy Group]
Proxy = select, ProxyA, ProxyB, DIRECT
Auto = url-test, ProxyA, ProxyB
Smart = smart, ProxyA, ProxyB
Each line follows the pattern `Name = type, member1, member2, ..., key=value, ...`. Components containing `=` are parameters; all other components are member policy names.


## Group Types


[TABLE]


|
Type |
 Behavior |
 |


|
 `select` |
 Manually choose a policy in the UI. |
 |

|
 `url-test` |
 Automatically choose the policy with the best latency test result. |
 |

|
 `fallback` |
 Choose the first available policy by declared priority. |
 |

|
 `load-balance` |
 Distribute requests among available policies. |
 |

|
 `smart` |
 Dynamically select a policy using observed connection quality and site history. |
 |

|
 `subnet` |
 Choose a policy according to the current network. |
 |


[/TABLE]
The legacy keyword `ssid` is still accepted as an alias of `subnet` for compatibility.


## Nesting Groups


A group may include other groups as members. This works for all group types except `smart`, which silently ignores nested groups and built-in policies among its members.


When a nested group is tested, it contributes its own effective result: a nested `select` group is tested through its currently selected policy, while other nested groups are tested through their whole member set.


Group references must not form a loop. If a loop is detected (for example, `A` includes `B` and `B` includes `A`), Surge logs a warning and the affected group temporarily behaves as a reject policy (shown as `FAILED` in logs). If a group ends up with no usable member at all, Surge falls back to `DIRECT` (shown as `SUBSTITUTE` in logs) and raises a one-time warning.


## How Testing Works


The automatic group types (`url-test`, `fallback`, `load-balance`, `smart`) rely on latency tests: Surge sends an HTTP HEAD request to a testing URL through each member policy and records the result. Testing is lazy &#x2014; Surge retests when a group is used and the previous result has expired or the network has changed.


The testing URL and timeout are resolved per policy: an explicit `test-url` policy parameter wins; otherwise the global `proxy-test-url` (for proxies) or `internet-test-url` (for direct-type policies) from `[General]` is used. See Common Group Parameters for details, and Policy Parameters for the per-policy testing options.

---
## Policy Groups / Manual Selection (Select)

# Manual Selection Group


A `select` group lets you choose which policy is used from the user interface. It is the most common group type: rules point to the group, and you switch the actual policy manually.


SelectGroup = select, ProxyHTTP, ProxyHTTPS, DIRECT, REJECT
The selection is persisted per profile. If no selection has been made yet, or the previously selected policy is no longer a member of the group, the first member is used.


In Surge iOS, you may use the widget to quickly switch the policy for manual selection groups. In Surge Mac, you may switch the policy in the menu bar.


A `select` group is often combined with external policy lists &#x2014; see Policy Including for `policy-path`, `include-all-proxies`, and `include-other-group`.


For parameters shared by all group types (`hidden`, `icon-url`, ...), see Common Group Parameters.

---
## Policy Groups / Automatic Testing (URL Test)

# Automatic Testing Group


A `url-test` group automatically selects the member policy with the best latency test result. Use it when you have several similar proxy servers and always want the fastest one.


AutoTestGroup = url-test, ProxySOCKS5, ProxySOCKS5TLS
## How Testing Works


Surge tests each member by sending an HTTP HEAD request to the testing URL through that policy. The testing URL comes from the policy's own `test-url` parameter if set, otherwise from the global `proxy-test-url` / `internet-test-url` options in `[General]`. See Common Group Parameters for the full resolution rules.


The measurement runs in two rounds: the first HEAD request establishes the connection (DNS, TCP, and proxy handshake), and if the server supports HTTP keep-alive, a second HEAD request is sent on the reused connection. The duration of the second request is the reported score, so the score approximates the pure request round-trip time and excludes handshake overhead. If the testing URL does not support connection reuse, the score is the full first-round time, and Surge logs a one-time warning that the result is inaccurate.


Test results are not refreshed on a fixed schedule. A retest is triggered when the group is used and the previous result is older than `interval`, or the network has changed since the last test. You can also trigger a full test round manually from the UI.


The group selects the member with the lowest score among those that passed the test. When the winner changes, Surge posts a "Group has a new optimal option" notification unless `no-alert` is set.


The legacy `url =` parameter on a group line has no effect in current versions. Use the per-policy `test-url` parameter or the global `proxy-test-url` option instead.


## Temporary Override


You can temporarily override the result of automatic testing by manually selecting a policy. See Temporary Override.


## Parameters


#### `interval`


Optional, in seconds, default: 600


How long a test result stays valid. When the group is used and the result is older than this interval, Surge retests in the background. A network change also invalidates the result.


#### `tolerance`


Optional, in milliseconds, default: 100


Switch damping. The selected policy changes only when it failed the test, or when the new best policy is faster than the currently selected one by more than the tolerance. This prevents policies with similar latency from constantly alternating.


An explicit `tolerance=0` is honored and switches to the fastest policy on every result change.


#### `timeout`


Optional, in seconds, no default


Availability filter based on the test score: a member qualifies as a candidate only if its tested latency is below this value. If omitted, no filtering by score is applied.


This is not the connection timeout of the test itself. The per-test timeout is controlled by the per-policy `test-timeout` parameter or the global `test-timeout` option (default 5 seconds) &#x2014; see Common Group Parameters.


#### `evaluate-before-use`


Optional, Boolean, default: false


By default, when an automatic testing group is used for the first time, Surge uses the first policy in the group and starts testing in the background.


If this option is enabled, Surge waits for the first test round to finish before handling the request. If the evaluation fails, the request fails with an error.

---
## Policy Groups / Fallback

# Fallback Group


A `fallback` group selects an available policy by priority. Availability is checked with the same URL test as an automatic testing group, but a fallback group only cares whether a policy is available, not its exact latency. Policies listed earlier have higher priority.


FallbackGroup = fallback, ProxySOCKS5, ProxySOCKS5TLS
Surge walks the members in declared order and picks the first one whose latest test succeeded (and whose latency is below `timeout`, if set). If no member qualifies, the first member is used regardless, so traffic is never left without a policy.


When the selected policy changes, Surge posts a notification unless `no-alert` is set.


## Temporary Override


You can temporarily override the result of automatic testing by manually selecting a policy. See Temporary Override.


## Parameters


#### `interval`


Optional, in seconds, default: 600


How long an availability result stays valid. When the group is used and the result is older than this interval, Surge retests in the background. A network change also invalidates the result.


#### `timeout`


Optional, in seconds, no default


Treat a member as unavailable if its tested latency is not below this value. This is separate from the per-test connection timeout (`test-timeout`, default 5 seconds) &#x2014; see Common Group Parameters.


#### `evaluate-before-use`


Optional, Boolean, default: false


If enabled, when the group is used for the first time, Surge waits for the first test round to finish instead of using the first member while testing in the background.

---
## Policy Groups / Load Balance

# Load Balance Group


A `load-balance` group distributes requests among its available members. Use it to spread traffic over several servers instead of always using a single one.


Balance = load-balance, ProxyA, ProxyB, ProxyC
## Behavior


Availability is determined by the same URL test as an automatic testing group: the available set contains the members whose latest test succeeded (and whose latency is below `timeout`, if set). The set is rebuilt after every test round.


- Without `persistent`, each request picks a uniformly random policy from the available set.

- If no member is currently available, all members are used as candidates.

- The testing parameters `interval`, `timeout`, and `evaluate-before-use` work the same way as for an automatic testing group.

- A load-balance group never posts policy change notifications.

- When nested inside another group, the group's own test score is the mean score of its available members.


## Temporary Override


You can temporarily pin the group to a single member, which skips balancing. See Temporary Override.


## Parameters


#### `persistent`


Optional, Boolean, default: false


When `persistent=true`, the same policy is used for the same target hostname: the policy is chosen by hashing the target hostname over the available members. This helps avoid triggering risk controls on the target site due to changing egress IPs. The selection may still change when the available set changes.

---
## Policy Groups / Smart Group

# Smart Group iOS 5.11.0+ Mac 5.7.0+


A Smart Group dynamically selects a policy using the observed quality of real connections, and can retry another policy when the selected one is unavailable or performs poorly. Use it when you want hands-off selection that adapts to actual traffic rather than periodic latency tests alone.


[Proxy Group]
Smart = smart, ProxyA, ProxyB
Only proxy policies can be members of a Smart Group: nested policy groups and built-in policies (such as `DIRECT`) are silently ignored.


## How Selection Works


Each member policy gets a continuously updated delay score:


- The base of the score is a time-weighted moving average of the first-response latency of real connections &#x2014; the time from connecting until the first response byte arrives. URL test results also feed into the same score.

- A packet-loss penalty is added based on the observed TCP retransmission ratio (roughly 50 ms per 1% of loss).

- The optional `policy-priority` factor is applied as a multiplier.


When a request comes in, policies whose score is close to the best one form the preferred set; one of them is used. The remaining healthy policies and then the failed ones form an ordered retry list, so if the chosen policy fails, the connection can fall back to the next candidate.


Failure handling: a connection that dies before receiving any data sharply worsens the policy's score, and a policy whose average delay grows too large is marked as failed until later tests or traffic recover it.


Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, Smart Groups also use UDP response latency and silent relay failures when scoring policies. A connection that receives no response data within 3 seconds is treated as failed so another policy can be tried sooner. iOS 5.21.0+ Mac 6.8.0+


### Per-site Memory


The group remembers, per site, which policies recently succeeded or failed. A policy known to work well for a site is preferred for that site unless it has become much slower than the best candidate; a policy that recently failed for the site is demoted. This memory expires after about one hour.


### Testing


A Smart Group retests its members on a fixed 5-minute schedule; the `interval` parameter has no effect on Smart Groups. When the group has many members (more than 12), regular rounds test only a subset &#x2014; the most-used policies plus the least-recently-tested ones &#x2014; while a manually triggered test always tests every member.


The `evaluate-before-use` parameter is supported and works the same way as for an automatic testing group.


The policy displayed as the group's current selection is the most-used one in the recent period, not necessarily the one every new connection will use.


## Temporary Override


You can temporarily pin the group to a specific member. See Temporary Override.


## Parameters


#### `policy-priority`


Optional, quoted list of `regex:factor` pairs separated by `;`, default: 1.0 for all policies


Applies a multiplier to the score of policies whose names match an expression; the first matching expression wins. Values below `1` increase preference and values above `1` reduce preference:


Smart = smart, ProxyA, ProxyB, policy-priority="Premium:0.9;Backup:1.3"
Priority values must be positive. Zero and negative values are rejected starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. iOS 5.21.0+ Mac 6.8.0+

---
## Policy Groups / Subnet Group

# Subnet Group


A `subnet` group automatically selects a policy based on the current network environment, such as the connected Wi-Fi network or the network type.


Subnet Group = subnet, default = ProxyHTTP, SSID:MyHome = ProxySOCKS5, TYPE:WIFI = ProxyHTTP
Starting from Surge iOS 4.12.0 and Surge Mac 4.5.0, the SSID group was renamed to Subnet Group.
The legacy SSID Group syntax is still supported. You may use the group type keyword `subnet` or `ssid` for compatibility.


## Conditions


Each entry of the form `<subnet expression> = Policy` maps a network condition to a policy. The SUBNET rule page is the canonical reference for subnet expressions. In summary:


- `SSID:value` &#x2014; match the Wi-Fi SSID; wildcard characters are allowed.

- `BSSID:value` &#x2014; match the Wi-Fi BSSID; wildcard characters are allowed.

- `ROUTER:value` &#x2014; match the router (default gateway) IP address.

- `TYPE:WIFI` / `TYPE:WIRED` / `TYPE:CELLULAR` &#x2014; match the network type.

- `MCCMNC:value` &#x2014; match the cellular carrier MCC+MNC code; only matches when Wi-Fi is not connected.

- A bare value without a prefix matches SSID/BSSID/router IP, for legacy compatibility.


Conditions are evaluated in the declared order and the first match wins; if no condition matches, the `default` policy is used. The result is re-evaluated whenever the network changes.


Subnet groups do not support the other common group parameters (`policy-path`, `include-*`, `policy-regex-filter`, `no-alert`, ...); only `hidden` and `icon-url` are available besides the entries below.


You can also temporarily override the group with a manually selected policy, just like other automatic groups &#x2014; see Common Group Parameters.


## Parameters


#### `default`


Required


The policy used when no subnet expression matches.


#### `cellular`


Optional (Deprecated, use a `TYPE:CELLULAR` condition instead)


The policy for cellular networks. If set, it takes precedence over the condition entries when the device is on a cellular network. If it is not provided, the condition list and then the default policy apply.

---
## Policy Groups / Policy Including

# Policy Including


A policy group can build its member list from sources other than the literal names on its line: an external file or URL (`policy-path`), all proxies in the profile (`include-all-proxies`), or the members of another group (`include-other-group`).


## Include External Policies


A policy group may import policies defined in an external file or from a URL.


egroup = select, policy-path=proxies.txt
The resource may be either of:


- A policy list: one policy line per line, in the same format as the `[Proxy]` section. Blank lines and lines starting with `#` or `//` are ignored. Invalid lines are logged and skipped; policies whose names duplicate an existing policy are skipped with a warning.

- A complete Surge profile: if the content contains a `[Proxy]` section, the policies in that section are used.


Proxy-A = https, example1.com, 443
Proxy-B = https, example2.com, 443
Remote resources are cached on disk and re-downloaded periodically.


#### `update-interval`


Optional, in seconds, default: 86400


The update interval for a remote `policy-path`. Only meaningful when the path is a URL.


#### `policy-regex-filter`


Optional, regex


Only use the policies whose name matches the regex. It applies to members from `policy-path`, `include-all-proxies`, and `include-other-group`, but not to explicitly listed members. The value must be a valid regular expression.


#### `external-policy-modifier`


Optional, quoted `key=value` list


Modify the parameters of every imported external policy. The listed parameters override those in the imported policy lines.


For example, enabling TFO and changing the testing URL:


external-policy-modifier="test-url=http://apple.com/,tfo=true"
#### `external-policy-name-prefix`


Optional


Add a prefix to the policy names of the sub-policies in this external policy group to facilitate differentiation when multiple different external policy groups are used simultaneously. The prefix must not contain the `=` character.


Imported policies are processed in this order: `policy-regex-filter` &#x2192; `external-policy-name-prefix` &#x2192; `external-policy-modifier`.


## Include Existing Policies iOS 4.12.0+ Mac 4.5.0+


You can use `include-all-proxies` and `include-other-group` to include all proxies or reuse existing definitions from another group.


#### `include-all-proxies`


Optional, Boolean, default: false


The parameter `include-all-proxies=true` includes all proxy policies defined in the `[Proxy]` section (built-in policies and groups are not included). It can be used with the `policy-regex-filter` parameter for filtering.


#### `include-other-group`


Optional, comma-separated list of group names (quotable)


Parameter `include-other-group="group1,group2"` includes the resolved member policies from other policy groups; multiple groups can be listed separated by commas. Inclusion is recursive, and it can be used with the `policy-regex-filter` parameter for filtering.


## Ordering


Members are assembled in this order: explicitly listed members (in declared order), then `include-other-group` members (in the listed group order), then `include-all-proxies` members, then `policy-path` externals. Duplicate names keep the first occurrence.


- `include-all-proxies`, `include-other-group`, and `policy-path` parameters are allowed to be used in a single policy group at the same time. The `policy-regex-filter` parameter applies to all three.

- When precise member ordering matters (e.g., fallback groups), prefer nesting policy groups with `include-other-group` instead of relying on the assembly order of mixed sources.

---
## Policy Groups / Common Group Parameters

# Common Group Parameters


These parameters are available on all group types, with one exception: subnet groups support only `hidden` and `icon-url` (see Subnet Group). The parameters for importing members (`policy-path`, `include-all-proxies`, `include-other-group`, and their companions) are documented on the Policy Including page.


#### `no-alert`


Optional, Boolean, default: false


Do not show the policy change notification for this group. The "Group has a new optimal option" notification is only posted by `url-test` and `fallback` groups, so this parameter has no effect on other group types &#x2014; `load-balance`, `smart`, and `select` groups never notify.


#### `hidden`


Optional, Boolean, default: false


Do not show the group in the menu (Surge Mac) and the policy selection view (Surge iOS).


#### `icon-url` Mac 6.5.0+


Optional


Configure an icon for a policy group for display in the policy selection interface. This parameter currently needs to be edited manually in the profile.


Example:


Group = select, ProxyA, ProxyB, icon-url=https://example.com/icon.png
## Testing URL and Timeout


The automatic group types test their members with an HTTP HEAD request. For each member policy, the testing URL is resolved as follows:


- The policy's own `test-url` parameter, if set.

- Otherwise, a global option from `[General]`: `internet-test-url` for direct-type policies, `proxy-test-url` for proxy policies. Both default to `http://bing.com/`.


The per-test timeout is resolved similarly: the policy's `test-timeout` parameter, then the global `test-timeout` option, then 5 seconds by default (10 seconds for direct-type policies).


These per-policy parameters are documented in Policy Parameters. Do not confuse the per-test `test-timeout` with the `timeout` parameter of `url-test`/`fallback` groups, which filters candidates by their measured latency.


## Temporary Override


The automatic group types &#x2014; `url-test`, `fallback`, `load-balance`, `subnet`, and `smart` &#x2014; can be temporarily overridden by manually selecting a policy:


- In Surge Mac, you can find the override option in the corresponding group in the main menu.


- In Surge iOS, you can find the override option by long-pressing on the corresponding policy's menu in the policy group view.


While an override is active, the group always uses the selected policy and automatic testing for the group is no longer triggered by use. Overrides for groups that no longer exist are cleared when the profile reloads.

---
## DNS / Overview

# DNS Overview


Surge uses its own DNS client for all outgoing requests and for rule evaluation. It may behave differently from the DNS client of your operating system, and it is tuned for performance and reliability rather than strict RFC resolver semantics.


Surge's DNS subsystem has two roles:


- The internal DNS client resolves domains for connections that Surge itself establishes and for rules that need an IP address (such as `IP-CIDR` and `GEOIP`). Its behavior is described on this page.

- A DNS responder for the virtual network interface: when Enhanced Mode or the iOS VPN tunnel is active, DNS queries from the system and other devices are answered by Surge directly, normally with fake IP addresses. See Advanced DNS Topics.


To customize the upstream servers used by the internal client, see DNS Servers and Encrypted DNS. To override results for specific domains, see Local DNS Mapping.


## Concurrent Querying


Surge queries all configured DNS servers simultaneously to improve performance, similar to dnsmasq with the `--all-servers` parameter. The first valid answer wins. Surge iOS and Surge Dashboard show which server responded first.


If no answer arrives within 1 second, Surge resends the query to all servers. After 5 attempts (about 5 seconds in total), the lookup fails with a DNS error.


## A and AAAA Queries


When IPv6 is enabled (`ipv6 = true` in `[General]`) and the current network has IPv6 connectivity, Surge sends both A and AAAA questions in parallel and waits for both answers before completing the lookup. If only one record type has been answered when the retry timer fires, Surge completes the lookup with the partial result.


If 5 consecutive lookups receive an A answer while the AAAA answer times out, Surge concludes that the upstream servers never return AAAA answers on the current network and stops sending AAAA questions. A log event is raised when this happens. AAAA querying resumes after a network change or a DNS cache flush.


## Empty Answers


Some domain names have poorly-performing authoritative name servers, causing upstream DNS servers to return empty answers due to server-side timeout or other connectivity issues. Surge reports an empty DNS answer error only if all upstream DNS servers explicitly return empty answers, or if some servers return empty answers and the rest fail to respond in time. An empty answer from a single server never fails the lookup as long as another server returns records.


## Caching


Results are cached according to the TTL of the returned records (the smallest TTL in the record set determines the expiry).


Surge uses optimistic caching: when a cached entry has expired, it is still returned to the caller immediately, while a refresh query runs in the background. This removes DNS latency from repeated connections at the cost of occasionally using a slightly stale address.


The cache holds up to 200 entries on iOS and 2000 entries on macOS, with least-recently-used eviction. The cache is flushed automatically on network changes, and can be flushed manually from the UI, the CLI, or the HTTP API. Identical in-flight lookups are coalesced into a single query.


## Special Hostnames


- Simple hostnames (names without a dot, such as `nas`): Surge appends the system's first search domain (`nas` &#x2192; `nas.example.lan`) and forwards the query to the system DNS servers.

- Names ending with `.local`: resolved through the system resolver library by default, so mDNS/Bonjour names keep working. See Local DNS Mapping for related options.

- Fully qualified names with a trailing dot (`example.com.`): the trailing dot is stripped and search-domain rewriting is suppressed.

- IP literals: returned as-is without any lookup.

---
## DNS / DNS Servers

# DNS Servers


Surge uses the DNS server addresses from the operating system by default. Use the `dns-server` parameter in the `[General]` section to override them.


[General]
dns-server = 8.8.8.8, 8.8.4.4
## Syntax


The value is a comma-separated list of servers. Each item is one of:


- An IPv4 or IPv6 address, optionally with a port: `1.1.1.1`, `192.0.2.53:5353`, `::1`. The default port is 53. Hostnames are not allowed.

- The keyword `system`, which includes the current system DNS servers together with the other listed servers. Duplicate servers are ignored.


[General]
dns-server = system, 8.8.8.8, 8.8.4.4
If `dns-server` is not set at all, Surge uses the system DNS servers.


When `ipv6 = false`, IPv6 server addresses are dropped from the list.


All listed servers are queried concurrently and the first answer wins; see DNS Overview for the full query behavior.


## DNS over TCP iOS 5.21.0+ Mac 6.8.0+


Prefix a server with `tcp://` to send traditional (unencrypted) DNS queries over TCP with a persistent connection. A hostname may be used in the URL, and the port is optional (default 53).


[General]
dns-server = tcp://dns.example.com, tcp://192.0.2.53:5353
Internally, `tcp://` servers are handled by the same subsystem as encrypted DNS servers. As a result, once any `tcp://` server is configured, plain UDP servers listed alongside it are no longer used for ordinary domains &#x2014; they are only used to resolve the hostname of the `tcp://` server itself. See Encrypted DNS for details.


## Per-Network Overrides


You can use a different set of DNS servers on a specific Wi-Fi network or subnet with the `dns-server` and `encrypted-dns-server` parameters in the `[SSID Setting]` section. These replace the global values while connected to that network. See SSID Setting.


```
[SSID Setting]
SSID:MyHome dns-server=192.168.1.1

```

---
## DNS / Encrypted DNS

# Encrypted DNS


Surge can send DNS queries over encrypted transports (DoH, DoH3, DoQ, DoT) instead of plain UDP. Configure the `encrypted-dns-server` parameter in the `[General]` section with one or more server URLs.


[General]
encrypted-dns-server = https://8.8.8.8/dns-query
You may specify multiple servers, separated by commas. All of them are queried concurrently and the first answer wins.


If encrypted DNS is configured, traditional DNS servers are only used to test connectivity and to resolve the hostnames in the encrypted DNS URLs themselves; all other domains are resolved through the encrypted servers. This bootstrap exemption also covers hostnames in encrypted DNS URLs used by `[Host]` `server:` items.


## Supported Protocols


[TABLE]


|
URL scheme |
 Protocol |
 Default port |
 |


|
 `https://` |
 DNS over HTTPS (DoH) |
 443 |
 |

|
 `h3://` |
 DNS over HTTP/3 (DoH3) |
 443 |
 |

|
 `quic://` |
 DNS over QUIC (DoQ) |
 853 |
 |

|
 `tls://` |
 DNS over TLS (DoT) |
 853 |
 |

|
 `tcp://` |
 Traditional DNS over TCP |
 53 |
 |


[/TABLE]
`tcp://` is not encrypted &#x2014; it sends plain DNS queries over a persistent TCP connection. It is handled by the same subsystem as the encrypted transports, so all options on this page apply to it as well. A `tcp://` URL may only contain a host and an optional port. See also DNS Servers.


The special value `off` disables encrypted DNS. It is mainly useful in per-network overrides: the `[SSID Setting]` section accepts an `encrypted-dns-server` parameter to replace or disable the global value on a specific network. See SSID Setting.


[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=off
## Use Encrypted DNS for Specified Domains


You can assign an encrypted DNS server to specific domains with a `server:` mapping in the `[Host]` section, while other domains keep using the normal servers.


[Host]
example.com = server:https://cloudflare-dns.com/dns-query
See Local DNS Mapping for the full `[Host]` syntax.


## Parameters


#### encrypted-dns-skip-cert-verification


Optional, Boolean, default: false


Skip the server certificate verification for all encrypted DNS connections. This is insecure; use it only for testing.


#### encrypted-dns-follow-outbound-mode


Optional, Boolean, default: false


By default, encrypted DNS connections always use the DIRECT policy and bypass the rule system.


When enabled, encrypted DNS connections follow the outbound mode settings and are matched against the rules like normal requests. You can then configure a rule for the DNS server's hostname to use a proxy, or match the connections with a PROTOCOL rule:


- `PROTOCOL,DOH` &#x2014; DNS over HTTPS (`https://`)

- `PROTOCOL,DOH3` &#x2014; DNS over HTTP/3 (`h3://`)

- `PROTOCOL,DOQ` &#x2014; DNS over QUIC (`quic://`)

- `PROTOCOL,DOT` &#x2014; DNS over TLS (`tls://`)

- `PROTOCOL,DNS` &#x2014; DNS over TCP (`tcp://`)


If an encrypted DNS connection matches a proxy policy whose server is itself configured with a domain name, resolving that domain would require DNS and create a loop. Surge logs a warning and falls back to DIRECT for the DNS connection in this case. To avoid the fallback, use an IP address as the proxy's server address, or add a `[Host]` IP mapping for the proxy's domain.

---
## DNS / Local DNS Mapping

# Local DNS Mapping


Surge supports local DNS mapping with the `[Host]` section. It is similar to `/etc/hosts`, but with more powerful features, including wildcards, aliases, per-domain DNS server assignment, and script-based resolution.


[Host]
abc.com = 1.2.3.4
*.dev = 6.7.8.9
foo.com = bar.com
bar.com = server:8.8.8.8
Items are evaluated top to bottom, and the first matching item wins. Local DNS mapping applies to Surge's internal DNS client and to the fake-IP DNS responder in Enhanced Mode. The hostnames of your proxy servers are never matched against `[Host]` items, to avoid resolution loops.


## IP Address Mapping


Map a hostname to a fixed IP address. Surge answers the mapping authoritatively without querying any upstream server.


[Host]
abc.com = 1.2.3.4
Multiple addresses may be given as a comma-separated list, and IPv4 and IPv6 addresses may be mixed:


[Host]
abc.com = 1.2.3.4, 5.6.7.8, ::1
## Wildcards


Patterns may use the wildcards `*` (any sequence of characters) and `?` (a single character). Surge uses simple string matching against the whole hostname. For example, `*google.com` matches `google.com`, `foo.google.com`, and `bargoogle.com`. `*.google.com` does not match `google.com`.


[Host]
*.dev = 6.7.8.9
## Alias


An alias works like a CNAME record: the value is another hostname, and the lookup is restarted with that name.


[Host]
foo.com = bar.com
## Assigning DNS Servers


You can assign specific DNS servers to one or more domains with a `server:` value.


[Host]
bar.com = server:8.8.8.8
Each server is an IP address with an optional port (default 53) or an encrypted DNS URL (any supported scheme):


[Host]
example.com = server:https://cloudflare-dns.com/dns-query
Multiple DNS servers can be specified as a comma-separated list. iOS 5.21.0+ Mac 6.8.0+


[Host]
bar.com = server:8.8.8.8,1.1.1.1
### System Resolution


Since Surge has its own DNS client implementation, some special hostnames may fail to resolve. Use `server:system` to hand the lookup over to the system:


[Host]
Macbook = server:system
`server:syslib` is an alias of `server:system`; the two values behave identically. The actual behavior depends on the working mode:


- In normal (proxy) mode, the lookup is performed by the system resolver library.

- In enhanced mode, the query stays inside Surge but is forwarded to the DNS servers currently configured in the operating system, since the traditional system resolver might be bypassed.


`server:force-syslib` always uses the system resolver library, even in enhanced mode. This is intended for special domains such as mDNS names. Do not use it for general domains, because it may cause recursive requests. Mac 6.4.3+


By default, all hostnames with the `.local` suffix are resolved by the system.


## Script-Based Resolution


Use `script:<name>` to resolve a domain with a DNS script, which may return addresses directly or redirect the query to other servers:


[Host]
example.com = script:dnspod
*.example.com = script:dnspod
The name refers to a `type=dns` script defined in the `[Script]` section. See DNS Script for the script interface and a complete example.


## Referencing Rule Sets Mac 5.10.0+


When you already maintain large rule sets or domain sets, reproducing the same list in `[Host]` is tedious. Surge allows binding an entire `DOMAIN-SET` or `RULE-SET` to a DNS mapping entry so that the upstream or IP mapping is shared automatically.


[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.example.com/dns-query
RULE-SET:https://example.com/rules.txt = 10.0.0.10
`DOMAIN-SET:` expects a domain list, while `RULE-SET:` uses the standard rule set format. Since the matching happens before any DNS resolution, only domain-based entries in a rule set can match; IP-based entries are ignored. This syntax follows the same remote file format described in Rule Set and is especially helpful for encrypted DNS assignments that need to stay aligned with a managed list.


## /etc/hosts (macOS)


On macOS, Surge reads the entries in `/etc/hosts` and appends them after the profile's `[Host]` items, so profile items take precedence. The file is watched and reloaded automatically when it changes. Set `read-etc-hosts = false` in `[General]` to disable this behavior (it is enabled by default).


## Use Local DNS Items for Proxied Requests


[General]
use-local-host-item-for-proxy = true
By default, DNS resolution for proxied requests happens on the remote proxy server, because Surge sends proxy requests with the original domain names, and `[Host]` items are bypassed.


After enabling this option, for requests whose target domain matches a local DNS mapping record, Surge sends the proxy request with the mapped IP address instead of the domain. If the record has multiple addresses, one is chosen at random.


It only works for local DNS mapping records using IP addresses; `server:` and `script:` items are not affected.

---
## DNS / Advanced DNS Topics

# Advanced DNS Topics


This page describes how DNS behaves when the Surge virtual network interface (VIF) is active &#x2014; in Enhanced Mode, the iOS VPN tunnel, or gateway mode &#x2014; and the options that control it.


## The Fake-IP DNS Responder


When the VIF is active, Surge runs its own DNS responder, and the system (or the client devices in gateway mode) is configured to use it. The responder listens on designated addresses:


- macOS: `198.18.0.2` (also advertised via DHCP in gateway mode)

- iOS: `198.18.0.4`

- IPv6: `fd00:6152::2`


Any query sent to an address in the range `198.18.0.2`&#x2013;`198.18.0.9` is treated as addressed to Surge's DNS responder.


For ordinary A and AAAA questions, the responder does not perform a real lookup. Instead, it instantly answers with a fake IP address from the reserved block `198.18.0.0/15` (IPv4 pool `198.18.1.1`&#x2013;`198.19.255.254`; IPv6 fake addresses use a dedicated prefix under `fd00:6152::`). Surge remembers the fake IP &#x21C4; domain mapping persistently. When a connection to a fake IP arrives through the VIF, Surge converts it back to the original domain for rule matching and outbound handling. This design means:


- No DNS latency is added before the connection starts; the real lookup happens only if the matched policy actually needs an IP address.

- Rules always see the original domain, even for clients that resolve addresses themselves.


Fake answers use a short TTL (5 seconds on iOS, 30 seconds on macOS) so that clients re-query frequently and stale mappings disappear quickly. A query only receives fake addresses for the address family it arrived over: an AAAA question arriving over IPv4 gets an empty answer, and vice versa, so clients only get fake IPs they can actually route to Surge.


Queries that are not simple A/AAAA questions (such as TXT or MX) are forwarded to the upstream DNS servers, using the same server configuration as the internal DNS client. Local DNS Mapping `server:` items are honored for forwarded queries as well.


## hijack-dns


By default, only queries sent to the designated Surge DNS addresses are answered with fake IPs; queries sent to a standard DNS server pass through normally.


Some devices or software always use a hardcoded DNS server (for example, Google speakers always use 8.8.8.8). Use the `hijack-dns` parameter in `[General]` to intercept those queries so they also receive fake addresses:


[General]
hijack-dns = 8.8.8.8:53, 8.8.4.4:53
Each entry is an IPv4 address or `*`, with an optional port (default 53). Use `hijack-dns = *:53` to hijack all DNS queries. Only packets that parse as valid DNS queries are hijacked; other traffic to the listed destinations passes through unaffected.


## always-real-ip


Some scenarios require the client to receive a real, routable IP address instead of a fake one &#x2014; for example, NAT-type detection for game consoles, or hostnames used by VPN clients. The `always-real-ip` parameter exempts domains from the fake-IP mechanism:


[General]
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
The value is matched against the query domain with wildcard support; it is a Host List parameter, see Host List Parameter Type for the detailed rules. Matching queries are forwarded to the upstream DNS servers and the real answer is returned to the client.


For exempted domains, `[Host]` IP mappings are answered authoritatively by the responder. For all other domains, the client still receives a fake IP, and any `[Host]` mapping takes effect later when Surge establishes the real connection.


## allow-dns-svcb


Optional, Boolean, default: false


Modern systems may perform an SVCB/HTTPS (type 65) record lookup instead of a standard A record lookup. Such answers can carry IP hints, which would bypass the fake-IP mechanism. By default, Surge rejects these queries as not-implemented, forcing the client to fall back to a standard A record lookup. Enable this option only if you need SVCB/HTTPS records to pass through.


## REJECT at DNS Time


Domain-based rules flagged `pre-matching` with a REJECT-family policy are enforced by the DNS responder itself: a matching query is answered with no record (REJECT), silently dropped (REJECT-DROP), or answered with the special sink address `198.18.0.244` (REJECT-NO-DROP), so the request is blocked before any connection is attempted. See REJECT Policy for details.


## Related Options


- `dns-follow-interface` &#x2014; a policy parameter that binds the DNS lookup for a connection to the same network interface as the connection itself. See Policy Parameters.

- `no-resolve` &#x2014; a flag on IP-based rules that prevents them from triggering DNS lookups during rule evaluation. See IP-Based Rules.

- `dns-failed` &#x2014; a flag on the FINAL rule that controls behavior when rule evaluation cannot finish due to a DNS failure. See FINAL.


The responder answers the canary domain `use-application-dns.net` with NXDOMAIN, which tells Firefox to disable its built-in DNS over HTTPS and keep using the system resolver, so that Surge can continue to see the domains being requested.

---
## HTTP Processing / Overview

# HTTP Processing


Surge can inspect and modify the HTTP traffic that flows through it: rewriting URLs, headers, and bodies, returning local mock responses, and running JavaScript against requests and responses. This chapter covers the built-in rewrite features; scripting has its own chapter.


## Which traffic can be processed


All HTTP processing features require the traffic to be handled by Surge's HTTP engine, which parses the stream as HTTP messages:


- Plain HTTP traffic is handled automatically. When a new TCP connection arrives, Surge sniffs the first bytes; if they look like an HTTP request, the connection is passed to the HTTP engine.

- Cleartext HTTP on non-standard ports may not be detected by sniffing. Use the `force-http-engine-hosts` parameter in the `[General]` section to force connections to specific hosts and ports through the HTTP engine. It only affects cleartext traffic and never decrypts TLS. See General section.

- To exclude hosts from HTTP processing entirely, use the `always-raw-tcp-hosts` parameter in the `[General]` section. Matching connections are forwarded as raw TCP streams without sniffing or parsing.

- HTTPS traffic is an opaque TLS tunnel by default. Surge can only process it after decrypting it with MITM for that hostname. Without MITM, none of the rewrite features apply to HTTPS requests.


Both `force-http-engine-hosts` and `always-raw-tcp-hosts` are of the Host List parameter type.


## Processing pipeline


When a request passes through the HTTP engine, the modification features run in this order:


- Header Rewrite

- URL Rewrite

- Body Rewrite

- Script processing


A request or response may be modified by only one script. The rewrite features have no such limit: if multiple rewrite rules match, they take effect in sequence.


Map Local is also evaluated in the request path: when a Map Local rule matches, Surge returns the local response directly and skips the upstream request.


## Inspecting the results


Requests handled by the HTTP engine appear as individual HTTP requests in the Dashboard's capture viewer, with full headers and bodies available. This is the easiest way to verify that your rewrite rules match and produce the expected result: the request detail view shows the notes for applied rewrites and scripts.

---
## HTTP Processing / MITM

# HTTPS Decryption (MITM)


Surge can decrypt HTTPS traffic with a man-in-the-middle (MITM) attack, so that the HTTP processing features can work on HTTPS requests. See the Wikipedia article for background on the technique.


A minimal configuration looks like this:


[MITM]
ca-p12 = MIIJtQ.........
ca-passphrase = password
hostname = *.google.com
h2 = true
Surge only decrypts traffic to hosts declared in `hostname`.


## CA certificate


To perform MITM, Surge needs a CA certificate that the system trusts.


The certificate generator can generate a new CA certificate for debugging and make it trusted by the system. It is available in Surge Dashboard (Mac version) and the Surge iOS Config Editor. The certificate is generated locally and saved only in your profile and the system Keychain. The key of the new certificate is generated randomly using OpenSSL.


You can also use an existing CA certificate. Export the certificate to PKCS#12 format (.p12) with a passphrase. The passphrase cannot be empty due to system limitations. Use the `base64` command to encode the certificate, then set `ca-p12` and `ca-passphrase` in the profile.


Some applications use certificate pinning and refuse any certificate not issued by the expected CA. Enabling decryption for these hosts breaks their connections. If a client completes the TLS handshake but disconnects without sending a request, Surge logs a hint that the host is likely protected by certificate pinning.


## Parameters


#### `hostname`: Host List


The list of hosts to decrypt. This parameter is of the Host List parameter type; the default port is 443:


- Wildcards `*` and `?` are supported.

- Use the `-` prefix to exclude a host. Items are matched in order, so put exclusions first: `hostname = -*.apple.com, -*.icloud.com, *` decrypts everything except Apple and iCloud hosts.

- A bare `example.com` entry matches port 443 only. Use `example.com:8443` to match another port, or `example.com:0` to match all ports.

- For TLS or QUIC connections identified by the sniffed SNI, a bare entry matches regardless of the connection's actual port. So a plain `example.com` entry still decrypts TLS traffic to that host on non-standard ports as long as the SNI is visible.

- Special tokens like `<ip-address>` and `<simple-hostname>` are available; see the Host List reference.


An invalid entry in the list produces a profile warning instead of a parse error, so a single typo does not prevent the profile from loading.


#### `hostname-disabled`: Optional, Host List


Entries in this list are removed from the effective `hostname` list. Surge's UI uses this key to temporarily disable a hostname without deleting it from the profile; you may also edit it manually.


#### `ca-p12`: Optional, string


The CA certificate and private key in PKCS#12 format, base64-encoded.


#### `ca-passphrase`: Optional, string


The passphrase of the PKCS#12 data. It cannot be empty due to system limitations.


#### `ca-keystore-name`: Optional, string


Use a certificate stored in the Keystore section instead of an inline `ca-p12`. The value is the name of a Keystore item of p12 type. When set, it takes precedence over `ca-p12`.


#### `skip-server-cert-verify`: Optional, Boolean, default: false


Do not verify the certificate of the remote server while performing MITM. This relaxes verification of the real server only; the client side still receives the Surge-generated certificate.


#### `h2`: Optional, Boolean, default: false


MITM over HTTP/2: decrypt HTTPS traffic with MITM over the HTTP/2 protocol, which can improve the performance of concurrent requests.


#### `client-source-address`: Optional, list


Enable the MITM function for specific client devices only.


- This is a list parameter using commas as the separator.

- You may specify a single IP address or use a CIDR block. Both IPv4 and IPv6 are supported.

- You may use the `-` prefix to exclude some clients, e.g. `client-source-address = -192.168.1.2, 0.0.0.0/0`.

- If the parameter is not set, MITM is enabled for all clients. This is equivalent to `client-source-address = 0.0.0.0/0, ::/0`.

- `127.0.0.1` should be included if you want to enable MITM for the current device.

- Since Surge Mac version 6.1.0, this parameter can use MAC addresses to match specific clients.


#### `auto-quic-block`: Optional, Boolean, default: true iOS 5.8.0+ Mac 5.4.0+


When a QUIC connection (i.e. HTTP/3) hits the MITM hostname list, Surge automatically blocks that QUIC connection, causing the client to fall back to HTTP/2 or HTTP/1.1 so the traffic can be intercepted by MITM.

---
## HTTP Processing / URL Rewrite

# URL Rewrite


Surge can rewrite a request's URL transparently, return a redirect response, or reject the request entirely, based on regular expression matching against the URL.


Example:


[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
^http://yachen\.com https://yach.me 302
^http://ad\.com/ad\.png _ reject
Each rule consists of three parts: a regular expression, a replacement, and a type. If the type is omitted, `header` is used.


The regular expression is matched against the full request URL. The replacement supports capture group references such as `$1`.


URL Rewrite only applies to requests handled by the HTTP engine. HTTPS requests can only be rewritten if MITM is enabled for the hostname. See HTTP Processing for details.


### Header Mode


Surge modifies the request in place and redirects it to another host if necessary. The client does not notice the rewrite.


The `Host` field in the request header is modified to match the new URL.


[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
If multiple header-mode rules match a request, only the first one is applied. The rewritten URL must be a valid `http`, `https`, or `ws` URL, otherwise the rewrite is discarded.


### 302 Mode


Surge returns a 302 redirect response to the client, with the replacement as the `Location`.


[URL Rewrite]
^http://yachen\.com https://yach.me 302
### 307 Mode


Same as 302 mode, but returns a 307 redirect response. Unlike 302, a 307 redirect requires the client to keep the original request method and body when following the redirect.


[URL Rewrite]
^http://yachen\.com https://yach.me 307
In 302 and 307 modes, the replacement may contain the placeholder `{{{GATEWAY_ADDRESS}}}`, which is substituted with the default router address of the current outgoing network interface.


### Reject Mode


Reject the request if the pattern is matched. The replacement parameter is ignored; use `_` as a placeholder.


[URL Rewrite]
^http://ad\.com/ad\.png _ reject
### Matching details


Besides the request-line URL, Surge also tries matching with the URL rebuilt from the `Host` header value and from the underlying connection's hostname. A rule can therefore match even when these differ from the host in the request line.

---
## HTTP Processing / Header Rewrite

# Header Rewrite


Surge can rewrite the headers of HTTP requests before they are forwarded to the server, and the headers of HTTP responses before they are returned to the client.


Example:


[Header Rewrite]
http-request ^http://example.com header-add DNT 1
http-request ^http://example.com header-del Cookie
http-request ^http://example.com header-replace User-Agent Unknown
http-response ^http://example.com header-replace-regex Date 2022 2023
Each rule consists of several parts:


- HTTP direction: `http-request` or `http-response`. Old versions only supported modifying the request, so this part can be omitted, which means `http-request`:


 [Header Rewrite]
 ^http://example.com header-add DNT 1


- URL regular expression


- Action type

- Header field

- Value (not used by `header-del`)

- Replace template (only for `header-replace-regex`)


Header Rewrite only applies to requests handled by the HTTP engine. HTTPS requests can only be modified if MITM is enabled for the hostname. See HTTP Processing for details.


### header-add


Append a new header line to the header, even if the header field already exists.


Example:


[Header Rewrite]
http-request ^http://example.com header-add DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
### header-del


Delete a header line from the header.


Example:


[Header Rewrite]
http-request ^http://example.com header-del DNT

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
### header-replace


Replace a header value in the header. If the header field doesn't exist, nothing happens.


Example:


[Header Rewrite]
http-request ^http://example.com header-replace DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
If you would like to add a header line, or replace it whenever the field exists, use `header-del` and `header-add` together:


[Header Rewrite]
^http://example.com header-del DNT
^http://example.com header-add DNT 1
### header-replace-regex


Replace a header value with a regular expression and a template. If the header field doesn't exist, nothing happens.


[Header Rewrite]
http-request ^http://example.com header-replace-regex User-Agent Safari Chrome

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Chrome/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0
### Limitations


Header Rewrite cannot change the message framing. If a rewrite changes the `Content-Length` or `Transfer-Encoding` headers, the modification is rejected and the request fails.

---
## HTTP Processing / Body Rewrite

# Body Rewrite iOS 5.10.0+ Mac 5.6.0+


Surge can rewrite the body of an HTTP request or response, replacing the original content with regular expressions or manipulating a JSON body with jq expressions.


Example:


[Body Rewrite]
http-request ^http(s)?://example\.com value abc
http-response ^http(s)?://example\.com documents Surge
Body Rewrite only applies to requests handled by the HTTP engine. HTTPS bodies can only be modified if MITM is enabled for the hostname. See HTTP Processing for details.


### Syntax


Each line contains a rewrite rule, with parameters separated by spaces, starting with `http-request` or `http-response`. The second parameter is the regular expression for the URL to take effect. The third parameter is the regular expression for replacement, and the fourth parameter is the content of replacement.


`http-response ^https?://example\.com/ regex replacement`


You may continue adding regular expressions and replacement content afterwards for consecutive replacements:


http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2
http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2 regex3 replacement3
&#x2026;
The replacement supports capture group references such as `$1`. The `^` and `$` anchors match at the beginning and end of each line of the body.


- If a request hits multiple body rewrite rules, they are executed in sequence.

- Even if the original request does not contain a body, new content may still be generated through body rewrite, such as using the `^$` expression.


The body must be valid UTF-8 text for regex-based rewriting. If it is not, the rule is skipped and a note is added to the request journal.


### JQ Body Rewrite iOS 5.14.0+ Mac 5.9.0+


You can use jq expressions to manipulate a JSON body:


http-request-jq url-pattern jq-expression
http-response-jq url-pattern jq-expression
For example:


http-response-jq ^http://httpbingo.org/anything '.headers |= with_entries(select(.key | test("^X-") | not))'
Notes:


- The body must be valid JSON; otherwise, the rule is skipped and a note is added to the request journal.

- If the jq expression produces empty output, the original body is kept.

- An invalid jq expression produces a warning and the rule is skipped.


### Interaction with scripts


If both a body rewrite rule and an HTTP script match the same request or response, the body rewrite is applied first, and the script receives the rewritten body.


### Limitations


- Body rewrite requires buffering the full body. A request body may be buffered up to 32 MB; if it exceeds the limit, the connection is dropped.

- A response body may be modified only up to 1 MB on iOS and 10 MB on macOS. If the response exceeds the limit, Surge gives up the modification and streams the response through unmodified.

- Request body rewrite is not supported when the request uses `Transfer-Encoding: chunked` or `Expect: 100-continue`. Surge logs a warning and forwards the request unmodified.

- When the body is modified, Surge normalizes the related headers automatically: the body is decompressed first if necessary, and `Content-Length` is recalculated.

---
## HTTP Processing / Map Local

# Map Local


You may mock an HTTP server and return a static response without sending the request upstream. This feature is also called Mock or API Mocking. If you want to return a response dynamically, try scripting.


Example:


[Map Local]
^http://surgetest\.com/json data-type=text data="{}" status-code=500
^http://surgetest\.com/gif data-type=tiny-gif status-code=200
^http://surgetest\.com/file data-type=file data="data/map-local.json" header="a:b|foo:bar"
^http://surgetest\.com/base64 data="dGVzdA==" data-type=base64
When a rule matches, Surge builds the response locally and skips the upstream request entirely.


Map Local only applies to requests handled by the HTTP engine, and only when the Rewrite feature is enabled. HTTPS requests can only be matched if MITM is enabled for the hostname. See HTTP Processing for details.


### Parameters


#### URL Pattern


Each line is defined by multiple parameters, separated by spaces, the first of which is a regular expression for the URL. If an HTTP request (or a decrypted HTTPS request) matches this expression, the rule is applied.


#### `data-type`: Optional, default: file


Surge currently supports four types of data:


- `file`: Returns the content of a specific file or URL.

- `text`: Returns the text of the data field, encoded in UTF-8. iOS 5.9.1+ Mac 5.5.1+

- `tiny-gif`: Returns a 1px GIF. iOS 5.9.1+ Mac 5.5.1+

- `base64`: Returns binary data encoded in base64. iOS 5.9.1+ Mac 5.5.1+


If `data-type` is omitted, `file` is used.


#### `data`


- For `file` type, this field should be the path to the data file, with relative paths being relative to the profile's directory. On macOS, absolute paths can also be used. A URL may also be used; the resource is downloaded and cached. On iOS and tvOS, the file size is limited to 15 MB.


- For `text` type, this field is the content itself.


- For `tiny-gif` type, this field is meaningless.


- For `base64` type, this field should contain valid base64 data.


You can use `data-type=text data=""` to return an empty result.


#### `header`: Optional


Customize the HTTP headers of the returned response. Use `|` to separate multiple key-value pairs, e.g. `header="a:b|foo:bar"`.


The value may also be a base64-encoded string of newline-separated header lines. If the value contains no `:`, Surge treats it as base64.


#### `status-code`: Optional, 200&#x2013;999, default: 200


The HTTP status code of the returned response. Values outside 200&#x2013;999 are invalid. The upper bound of 999 allows mocking non-standard status codes.


### About Content-Type


You can use the `header` parameter to control the `Content-Type` of the returned response. If not provided, Surge tries to complete it automatically:


- For `file` type, Surge tries to convert the file extension to a MIME type. If it fails, `application/octet-stream` is used.


- For `text` type, `text/plain` is used by default.


- For `tiny-gif` type, `image/gif` is used by default.


- For `base64` type, `application/octet-stream` is used by default.

---
## Scripting / Overview

# Scripting


You may use JavaScript to extend the abilities of Surge. Scripting requires Surge iOS 4 or Surge Mac 3.3.0. Scripts are declared in the `[Script]` section of the profile and are triggered by HTTP traffic, rule matching, DNS resolution, system events, cron timers, or manual invocation.


[Script]
script1 = type=http-response,pattern=^http://www.example.com/test,script-path=test.js,requires-body=true
script2 = type=cron,cronexp="* * * * *",script-path=fired.js
script3 = type=dns,script-path=dns.js
There are seven script types:


- http-request &#x2014; modify or short-circuit an HTTP request

- http-response &#x2014; modify an HTTP response

- rule &#x2014; implement a custom rule with the `SCRIPT` rule type

- dns &#x2014; implement a custom DNS resolver via a `[Host]` entry

- event &#x2014; react to system events such as network changes

- cron &#x2014; run on a schedule

- generic &#x2014; run only when invoked manually, from Shortcuts, or from a panel


## Declaration


Each line takes the form `name = comma-separated key=value parameters`:


name = type=http-response,pattern=^http://example.com,script-path=test.js,requires-body=true
The `script-path` parameter is mandatory; a line without it is rejected.


A legacy form is still parsed for compatibility:


<type> <value> <parameters>
For example, `http-response ^http://example.com script-path=x.js,requires-body=true`. The `<value>` maps to `pattern` (http-request/http-response), `cronexp` (cron), `event-name` (event), or the script name (rule/dns/generic). If no name is given, the script name defaults to the last path component of `script-path`. Use the modern form for new profiles.


### Parameters


#### `type`: Optional, default: generic


One of the seven script types listed above. An unknown type string rejects the line. Always declare the type explicitly.


#### `script-path`: Required


The path of the script: a relative path (resolved against the profile directory), an absolute path, or an HTTP(S) URL. Remote scripts are downloaded and cached automatically.


#### `script-update-interval`: Optional, in seconds, default: 86400


The auto-update interval when `script-path` is a URL.


#### `timeout`: Optional, in seconds, default: 5


The longest-running time for the script. If the script does not call `$done()` before the timeout, the session is terminated with a timeout warning. With the JSC engine, the timeout also terminates runaway synchronous JavaScript; the WebView engine enforces the timeout with a wall-clock timer only.


#### `argument`: Optional


An arbitrary string exposed to the script as the `$argument` global.


#### `engine`: Optional, auto/jsc/webview, default: auto


Selects the script engine. See the Script Engine section below.


#### `debug`: Optional, Boolean, default: false


Enables debug mode, which has two effects:


- The script is reloaded from the filesystem before every run instead of using the cache (local script paths only).

- For `http-request` and `http-response` scripts, `console.log()` output also appears in the request's notes in the traffic viewer.


#### `pattern`: Required for http-request and http-response, regex


The regex pattern to match the request URL. Only the first enabled matching script in profile order runs for a request; at most one `http-request` and one `http-response` script run per request.


#### `requires-body`: Optional, Boolean, default: false


Buffers the entire request/response body and passes it to the script, allowing the script to replace the body. This behavior is expensive; only enable it when necessary.


#### `max-size`: Optional, in bytes, default: 1 MB (iOS) / 10 MB (Mac)


The maximum allowed size for the request/response body when `requires-body` is enabled. If a response body exceeds the limit, Surge falls back to passthrough mode and skips the script for that request. If a request body exceeds the limit, the connection is terminated. A value of `-1` removes the limit (up to a hard cap).


#### `binary-body-mode`: Optional, Boolean, default: false


The raw binary body data is passed to the script as a `Uint8Array` instead of a string, and the script may return a `Uint8Array` body. The setting is exposed to the script as `$script.binaryBodyMode`.


#### `full-header-mode`: Optional, Boolean, default: false


Headers are delivered to the script as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields such as `Set-Cookie`. The script's returned `headers` may be either a plain object or an array of `{field, value}` objects.


#### `cronexp`: Required for cron


The cron expression, in standard 5-field form or 6-field form with a leading seconds field. Quote the value since it contains spaces, e.g. `cronexp="0 8 * * *"`. A cron script firing more than 10 times per hour triggers a battery-consumption warning.


#### `event-name`: Required for event


The name of the event to hook. Available events: `network-changed` and `notification`. An event script without `event-name` never runs.


#### `wake-system`: Optional, Boolean, default: false iOS Only


For cron scripts on iOS: schedules a silent local notification at the next fire time so the system wakes Surge to run the script.


## Script Engine iOS 5.9.0+ Mac 5.5.0+


Surge contains two JavaScript engines.


### JavaScriptCore (`engine=jsc`)


- Advantages:
The engine initializes quickly, and the overhead when calling is low (low latency).


- Disadvantages:
Since JSC runs inside the NE process on iOS, it increases the memory usage of the Surge NE process significantly, possibly leading to system termination due to exceeding memory limits.


At most 2 JSC sessions run in parallel; additional sessions are queued.


### WebView (`engine=webview`)


- Advantages:
The WebView runs in a separate independent process, so script execution has almost no impact on the memory usage of the NE process and will not cause the Surge NE process to be terminated due to memory usage issues.

- The WebView JavaScript environment can use JIT, which greatly improves execution efficiency for complex or CPU-intensive scripts.

- WebAPI (fetch, crypto, TextDecoder, etc.) can be used.


- Disadvantages:
The engine's initialization time overhead is slightly higher.

- Transferring a large amount of data between the script and Surge crosses process boundaries, which is less efficient. This is most apparent when using `binary-body-mode` to process large bodies.


At most 3 WebView sessions run in parallel; additional sessions are queued.


### Usage Recommendations


- For small, frequently called, simple scripts, such as rule and dns type scripts, JSC is recommended.

- For complex, high-memory scripts (such as parsing an MB-level HTTP body as JSON), WebView is recommended.

- If a script uses WebAPI, explicitly configure `engine=webview` so that users are prompted when the script runs in an environment without WebView support.


### Configuration


Add the `engine` parameter to the script line: `auto`, `jsc`, or `webview`. The default is `auto`, which always uses WebView where available.


### Engine Availability


- iOS: JSC and WebView

- macOS
macOS 10.15 and below: only JSC

- macOS 11.0 and above: JSC and WebView


- tvOS: only JSC


## Performance Constraints


Scripting with `requires-body` requires Surge to load the entire body into memory. A huge response body may cause Surge iOS to crash since the iOS system limits the maximum amount of memory the Network Extension can occupy. Write `pattern` regexes as narrowly as possible and only enable body access for necessary URLs.


Sessions beyond the parallel engine limits are queued; a session that cannot start within the timeout window completes as a timeout.


## Debugging


- Enable the `debug` parameter to reload the script from disk on every run and mirror `console.log()` output into the request notes for HTTP scripts.

- `console.log()` output is written to a per-script log file. You can view the logs on the device, or remotely with Logbook.

- The built-in script editor in both apps can evaluate a script immediately with mock input; the script receives `$trigger = "editor"`.

- On Surge iOS, you can manually trigger a script by long-pressing on it, or with the system Shortcuts app. A Shortcuts invocation may pass a parameter, available to the script as `$intent.parameter`.

- The HTTP API provides endpoints to evaluate scripts: `POST /v1/scripting/evaluate` evaluates arbitrary script text with mock input, and `POST /v1/scripting/cron/evaluate` runs a configured cron script by name.

---
## Scripting / JavaScript API Reference

# JavaScript API


This page documents the JavaScript API available to Surge scripts. The input globals and result shapes specific to each script type are documented on the corresponding type pages (http-request, http-response, rule, dns, event, cron, generic).


## Globals


The following globals are injected into every script, regardless of type.


#### `$environment`


An object describing the runtime environment:


- `$environment.system<String>`: The OS name, such as iOS or macOS.

- `$environment["surge-build"]<String>`: The build number of Surge.

- `$environment["surge-version"]<String>`: The short version number of Surge.

- `$environment.language<String>`: The current UI language of Surge.

- `$environment["device-model"]<String>`: The current device model. iOS 5.9.0+ Mac 5.5.0+


Keys containing hyphens require bracket access.


#### `$script`


Information about the script being evaluated:


- `$script.name<String>`: The script name.

- `$script.type<String>`: The script type.

- `$script.startTime<Number>`: The time when the current run started, as UNIX epoch seconds.

- `$script.sessionID<String>`: A short random ID identifying this run; it prefixes the script's log lines.

- `$script.binaryBodyMode<Boolean>`: Whether the `binary-body-mode` parameter is enabled.


#### `$network`


An object describing the current network environment: `wifi` (`ssid`, `bssid`), `v4` (`primaryAddress`, `primaryInterface`, `primaryRouter`), `v6` (`primaryAddress`, `primaryInterface`), `dns` (an array of the current DNS servers), and on iOS `cellular-data` (`carrier`, `radio`).


#### `$argument`


The string given by the `argument` parameter in the script declaration. Only present if the parameter is configured.


#### `$trigger`


Present only for some launch paths, describing how the script was started: `"editor"` (script editor), `"http-api"` (`POST /v1/scripting/evaluate`), `"intent"` (Shortcuts), `"button"` (panel tap), or `"auto-interval"` (periodic panel refresh). Not set for normal HTTP, rule, dns, event, or cron-timer triggers.


#### `$intent`


Present when the script is triggered from the system Shortcuts app. `$intent.parameter` contains the parameter passed by the shortcut.


#### `$input`


Present when the script is invoked by a panel: `{purpose: "panel", position, panelName}`. See the Information Panel page for the panel result contract.


Type-specific input globals &#x2014; `$request`, `$response`, `$domain`, `$event`, `$cronexp` &#x2014; are documented on the type pages.


## $done


Every script must call `$done()` exactly once to indicate completion, even scripts that do not produce a result. If `$done()` is never called, the session ends by timeout with a warning. Extra calls are ignored.


- `$done()` and `$done({})` are equivalent for `http-request` and `http-response` scripts: the request/response continues untouched.

- `$done({abort: true})` terminates the connection (`http-request` and `http-response` scripts).

- For other types, the accepted result shapes are documented on each type page. For `cron` and `event` scripts the result is ignored.


An uncaught exception aborts the session and the script has no effect.


## $httpClient


#### `$httpClient.get(options<String|Object>, callback<Function>)`


Performs an HTTP request. The same signature is available for all methods: `$httpClient.get`, `$httpClient.post`, `$httpClient.put`, `$httpClient.delete`, `$httpClient.head`, `$httpClient.options`, `$httpClient.patch`.


The first parameter can be a URL string or an options object:


{
  url: "http://www.example.com/",
  headers: {
    "Content-Type": "application/json"
  },
  body: "{}",
  timeout: 5
}
`url` is required and must be an HTTP(S) URL. If the `headers` field exists, it overwrites all existing header fields. `body` can be a string, an object (encoded to a JSON string, with `Content-Type` set to `application/json`), or a TypedArray.


Options:


- `timeout`: The request timeout in seconds. The default is 5 seconds.

- `policy`: Perform the request with an existing policy, given by name.

- `policy-descriptor`: Perform the request with a temporary policy, given by a full policy descriptor string. Takes precedence over `policy`.

- `insecure`: If true, HTTPS requests do not verify the server certificate. iOS 5.9.0+ Mac 5.5.0+

- `auto-redirect`: Controls whether 30x HTTP status codes are followed automatically, enabled by default. iOS 5.9.0+ Mac 5.5.0+

- `auto-cookie`: Controls whether Cookie-related fields are processed and stored automatically, enabled by default. If turned off, the Cookie header is passed as a normal field. iOS 5.9.0+ Mac 5.5.0+

- `binary-mode`: If true, the response data is delivered as a `Uint8Array` instead of a string. iOS 5.4.1+ Mac 5.0.1+

- `full-header-mode`: If true, the response headers are delivered as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields.


Callback: `callback(error<String>, response<Object>, data<String|Uint8Array>)`. When successful, `error` is null and the response object contains `status` and `headers`.


Requests made by scripts appear in the traffic viewer. At most 20 concurrent requests are allowed per script run; request and response bodies are capped at 32 MB on iOS and 256 MB on Mac.


## $httpAPI


#### `$httpAPI(method<String>, path<String>, body<Object>, callback<Function>(result<Object>))`


Calls Surge's own HTTP API to control Surge's functions. No authentication parameters are required. For a GET request, the body object is converted to a query string. The callback receives the parsed JSON result.


## $persistentStore


Simple persistent key-value storage. If the key is omitted, scripts with the same `script-path` share the same storage entry; use an explicit key to share data among different scripts. Keys must be plain names without path separators.


#### `$persistentStore.write(data<String>, [key<String>])`


Saves data permanently. Only a string is allowed; returns true on success. Passing `null` as the data deletes the entry. The maximum value size is 4 MB on iOS and 32 MB on Mac.


#### `$persistentStore.read([key<String>])`


Returns the saved string, or null if the entry does not exist.


Tips: Surge Mac writes the $persistentStore data to the directory `~/Library/Application Support/com.nssurge.surge-mac/SGJSVMPersistentStore/`. You may edit the files here directly for debugging.


## $notification


#### `$notification.post(title<String>, subtitle<String>, body<String>[, options<Object>])`


Posts a system notification.


Available options: iOS 5.11.0+ Mac 5.7.0+


- `action`: The operation performed after the user opens Surge by tapping the notification.
`open-url`: Opens a URL, provided by the `url` option.

- `clipboard`: Copies content to the clipboard (confirmed by the user), provided by the `text` option.


- `url`: The URL for the `open-url` action. Providing `url` without `action` implies `open-url`.

- `text`: The string for the `clipboard` action.

- `media-url`: Attaches media content, such as an image, fetched from an HTTP(S) URL.

- `media-base64`: Same as above, but the content is provided directly as base64. Requires the MIME type via the `media-base64-mime` option.

- `auto-dismiss`: Boolean; automatically dismisses the notification after a period of time (usually 10 s).

- `sound`: Boolean; plays the default notification sound.


A script hooked to the `notification` event may not call `$notification.post`, to prevent notification loops.


## $utils


#### `$utils.geoip(ip<String>)`


Performs a GeoIP lookup. Returns the ISO 3166 country code.


#### `$utils.ipasn(ip<String>)`


Looks up the AS number of the IP address, or null if unknown. The WebView engine may return the number as a numeric string.


#### `$utils.ipaso(ip<String>)`


Looks up the AS organization name of the IP address.


#### `$utils.ungzip(binary<Uint8Array>)`


Decompresses gzip data. Returns a `Uint8Array`, or null on failure. The output size is capped at 16 MB on iOS and 128 MB on Mac.


## $surge


The `$surge` module controls Surge itself. All setters return a Boolean indicating success.


#### `$surge.setSelectGroupPolicy(groupName<String>, policyName<String>)`


Changes the selected policy of a select policy group. The policy must be one of the group's sub-policies.


#### `$surge.selectGroupDetails()`


Returns an object describing all select groups: `{groups: {groupName: [subPolicyNames]}, decisions: {groupName: selectedPolicy}}`.


#### `$surge.retestGroup(groupName<String>, callback<Function>(result<Object>))`


Forces a retest of an automatic testing group. The callback result contains `availablePolicyNames`.


#### `$surge.setOutboundMode(mode<String>)`


Sets the outbound mode: `"direct"`, `"global-proxy"`, or `"rule"`.


#### `$surge.setHTTPCaptureEnabled(enabled<Boolean>)`


Toggles HTTP capture.


#### `$surge.setRewriteEnabled(enabled<Boolean>)`


Toggles the rewrite feature.


#### `$surge.setEnhancedModeEnabled(enabled<Boolean>)` Mac Only


Toggles Enhanced Mode.


#### `$surge.setCellularModeEnabled(enabled<Boolean>)` Mac Only


Toggles cellular data mode.


#### `$surge.logbook(content<String>)`


Writes a line into Surge's Logbook (Recent Events) under the script's name.


## Miscellaneous


#### `console.log(message)`


Logs a message to the script's log file. Objects are JSON-stringified. In debug mode, the output of `http-request`/`http-response` scripts also appears in the request's notes. Log lines are truncated at 512 KB.


#### `setTimeout(function[, delay])`


Same as `setTimeout` in browsers, with limits: the maximum delay is 24 hours, and at most 64 timers may be pending at once. `clearTimeout` is available only under the WebView engine. All pending timers are cancelled when the script run completes.


Under the WebView engine, scripts additionally have access to the standard WebAPI (fetch, TextDecoder, crypto, etc.). If a script relies on WebAPI, declare `engine=webview` explicitly; see the Script Engine section in the Scripting Overview.

---
## Scripting / HTTP Request Script

# http-request Script


An http-request script inspects and modifies an HTTP request before Surge performs rule matching and sends it upstream. Use it when URL Rewrite or Header Rewrite cannot express the change you need, or when you want to answer a request with a mock response without any network operation.


[Script]
modify-req = type=http-request,pattern=^https?://httpbin\.org,script-path=http-request.js,requires-body=true,max-size=16384
Like other HTTP processing features, the script only sees requests that go through Surge's HTTP engine. HTTPS requests require MITM to be enabled for the host. See HTTP Processing Overview.


## Trigger


The script runs when the full request URL matches the `pattern` regex. The URL is also tested with the host component replaced by the `Host` header value and by the SNI hostname, so a pattern written against the logical hostname still matches.


At most one script runs per request: the first enabled http-request script in the profile whose pattern matches wins.


## Parameters


These parameters apply to http-request (and http-response) script lines, in addition to the common script parameters.


#### pattern


Required, regular expression


The regex matched against the request URL. The line is invalid if the regex does not compile.


#### requires-body


Optional, true/false, default false


Buffers the entire request body and passes it to the script, allowing the script to replace it. This is expensive &#x2014; the whole body is held in memory &#x2014; so only enable it when necessary.


#### max-size


Optional, bytes, default 1 MB on iOS, 10 MB on macOS


The maximum body size buffered for the script. If a request body exceeds this limit, the connection is rejected with an error. Use `-1` for no limit (a hard cap of 32 MB for request bodies still applies).


#### binary-body-mode


Optional, true/false, default false


Passes the body to the script as a `Uint8Array` instead of a UTF-8 decoded string, and accepts a `Uint8Array` back. Use it for non-text bodies. The current mode is exposed to the script as `$script.binaryBodyMode`.


#### full-header-mode


Optional, true/false, default false


Delivers `$request.headers` as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields and their order. The `headers` value returned to `$done()` may then also be either form.


## Input


The script receives the request as the `$request` global:


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$request.url` |
 String |
 Request URL. |
 |

|
 `$request.method` |
 String |
 Request HTTP method. |
 |

|
 `$request.headers` |
 Object |
 Request HTTP headers. An array of `{field, value}` objects in full-header-mode. |
 |

|
 `$request.body` |
 String or Uint8Array |
 Request body. Only present when `requires-body=true` and the body is not empty. `Uint8Array` in binary-body-mode. |
 |

|
 `$request.id` |
 String |
 A unique ID for the request, stable between the http-request script and the paired http-response script. |
 |


[/TABLE]
## Result


The script must finish by calling `$done()` with an object. The object may contain:


- `url<String>`: Replace the request URL. Unlike URL Rewrite, this does not update the `Host` header field; return a modified `headers` object as well if necessary.

- `headers<Object or Array>`: Replace all request headers. Do not produce headers inconsistent with the actual body framing (such as a wrong `Content-Length`); Surge rejects the request if the resulting framing is ambiguous.

- `body<String or Uint8Array>`: Replace the request body. Only works when `requires-body=true`.

- `response<Object>`: If this object exists, Surge returns an HTTP response directly without any network operation. The object may contain:
`status<Number>`: Response HTTP status code. (Optional. Default: 200)

- `headers<Object or Array>`: Response HTTP headers. (Optional)

- `body<String or Uint8Array>`: Response HTTP body. (Optional)


- `abort<Boolean>`: If true, Surge aborts the request and closes the connection.


Calling `$done({})` &#x2014; or `$done()` with no argument &#x2014; continues the request untouched. To abort a request, use `$done({abort: true})`; a bare `$done()` does not abort it.


// Reject requests from a specific client
if ($request.headers['User-Agent'] === 'BadBot') {
    $done({abort: true});
} else {
    $done({});
}
## Limitations


- The request body may not be overwritten when the request uses chunked transfer encoding.

- The request body may not be overwritten when an `Expect: 100-continue` header exists.


In both cases the script may still run for header modification, but body changes are not applied.


## Example


let headers = $request.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});
A mock response without a network request:


```
$done({
    response: {
        status: 200,
        headers: {'Content-Type': 'application/json'},
        body: '{"result": "ok"}'
    }
});

```

---
## Scripting / HTTP Response Script

# http-response Script


An http-response script inspects and modifies an HTTP response before Surge delivers it to the client. Use it to rewrite response status, headers, or body in ways that the static rewrite features cannot express.


[Script]
modify-resp = type=http-response,pattern=^https?://www\.example\.com/test,script-path=test.js,requires-body=true,max-size=16384
Like other HTTP processing features, the script only sees requests that go through Surge's HTTP engine. HTTPS requests require MITM to be enabled for the host. See HTTP Processing Overview.


## Trigger


The script runs when the response arrives for a request whose URL matches the `pattern` regex. At most one script runs per response: the first enabled http-response script in the profile whose pattern matches wins.


## Parameters


These parameters apply to http-response (and http-request) script lines, in addition to the common script parameters. See the http-request page for the full descriptions.


#### pattern


Required, regular expression


The regex matched against the request URL.


#### requires-body


Optional, true/false, default false


Buffers the entire response body (decompressed) and passes it to the script, allowing the script to replace it. Without `requires-body`, the script runs as soon as the response header arrives and must not return a `body` in its result.


#### max-size


Optional, bytes, default 1 MB on iOS, 10 MB on macOS


The maximum body size buffered for the script. If the response body exceeds this limit, Surge falls back to passthrough mode: the script is skipped for this request and a note is attached to the request record. Use `-1` for no limit.


#### binary-body-mode


Optional, true/false, default false


Passes the body as a `Uint8Array` instead of a UTF-8 decoded string, and accepts a `Uint8Array` back.


#### full-header-mode


Optional, true/false, default false


Delivers headers as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields such as `Set-Cookie`.


Scripting with `requires-body` requires Surge to load the entire response body into memory. On iOS, the system limits the memory a Network Extension may use, so a huge response body can cause problems. Keep patterns narrow and only enable body access for the URLs that need it.


## Input


The script receives both the request and the response:


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$request.url` |
 String |
 Request URL. |
 |

|
 `$request.method` |
 String |
 Request HTTP method. |
 |

|
 `$request.headers` |
 Object |
 Request HTTP headers. |
 |

|
 `$request.id` |
 String |
 A unique ID for the request, stable between the http-request script and the paired http-response script. |
 |

|
 `$response.status` |
 Number |
 Response HTTP status code. |
 |

|
 `$response.headers` |
 Object |
 Response HTTP headers. An array of `{field, value}` objects in full-header-mode. |
 |

|
 `$response.body` |
 String or Uint8Array |
 Response HTTP body, decoded to a string with UTF-8 unless binary-body-mode is set. Only present when `requires-body=true` and the body is not empty. |
 |


[/TABLE]
## Result


The script must finish by calling `$done()` with an object. The object may contain:


- `status<Number>`: Replace the status code.

- `headers<Object or Array>`: Replace all response headers.

- `body<String or Uint8Array>`: Replace the response body. Only works when `requires-body=true`. A script running without `requires-body` must not return a body; doing so aborts the connection.

- `abort<Boolean>`: If true, Surge aborts the connection instead of delivering the response.


Calling `$done({})` &#x2014; or `$done()` with no argument &#x2014; delivers the response untouched.


## Example


```
let headers = $response.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});

```

---
## Scripting / Rule Script

# rule Script


A rule script implements a custom rule condition in JavaScript. A SCRIPT rule in the [Rule] section refers to the script by name; the script inspects the request and reports whether it matches.


[Script]
ssid-rule = type=rule,script-path=ssid-rule.js

[Rule]
SCRIPT,ssid-rule,DIRECT
Profile verification fails if a SCRIPT rule references a script name that does not exist.


## Trigger


The script runs when rule evaluation reaches the SCRIPT rule line. The result is cached for the rest of the evaluation of the same request, so referencing the same script from multiple rules does not run it repeatedly.


If the script is missing or scripting is disabled, the rule is treated as not matched.


Rule scripts run in the hot path of connection handling. Keep them small and fast, and avoid asynchronous operations where possible. The JSC engine is recommended for rule scripts; see Script Engine.


## Input


The request details are provided as the `$request` global. Fields that are unavailable for a particular request are `null`.


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$request.hostname` |
 String |
 Target hostname (a domain or an IP address). |
 |

|
 `$request.destPort` |
 Number |
 Target port. |
 |

|
 `$request.sourcePort` |
 Number |
 Source port of the client connection. iOS 5.8.4+ Mac 5.4.4+ |
 |

|
 `$request.protocol` |
 String |
 Protocol of the request: `HTTP`, `HTTPS`, `TCP`, `UDP`, `QUIC`, or `STUN`. iOS 5.8.4+ Mac 5.4.4+ |
 |

|
 `$request.processPath` |
 String |
 Path of the process that initiated the request (Surge Mac). |
 |

|
 `$request.userAgent` |
 String |
 User-Agent of the request, if available. |
 |

|
 `$request.url` |
 String |
 Request URL, if the request is an HTTP request handled by the HTTP engine. |
 |

|
 `$request.sourceIP` |
 String |
 Source IP address of the client. |
 |

|
 `$request.listenPort` |
 Number |
 The Surge listen port that accepted the request. |
 |

|
 `$request.dnsResult` |
 Object |
 DNS resolution result: `{v4Addresses: [String], v6Addresses: [String]}`. Only populated with the `requires-resolve` option. |
 |


[/TABLE]
## DNS Resolution


By default, a SCRIPT rule does not trigger a DNS lookup, behaving like other rules with the `no-resolve` flag: for a domain-based request, `$request.dnsResult` is empty. Use the `requires-resolve` option on the rule line to make Surge resolve the hostname first:


SCRIPT,ssid-rule,DIRECT,requires-resolve
The result then appears in `$request.dnsResult`.


## Result


The script must finish by calling `$done()` with an object containing a `matched` boolean:


$done({matched: true});   // the rule matches; use its policy
$done({matched: false});  // continue with the next rule
## Example


Match a hostname only when connected to a specific Wi-Fi network:


```
var hostnameMatched = ($request.hostname === 'home.com');
var ssidMatched = ($network.wifi.ssid === 'My Home');

$done({matched: (hostnameMatched && ssidMatched)});

```

---
## Scripting / DNS Script

# dns Script


A dns script implements a custom DNS resolver in JavaScript. A Local DNS Mapping entry in the [Host] section refers to the script by name; the script resolves the domain, either by returning addresses directly or by delegating to specific upstream DNS servers.


[Script]
dnspod = type=dns,script-path=dnspod.js

[Host]
example.com = script:dnspod
*.example.com = script:dnspod
Wildcard patterns are allowed on the domain, as with other [Host] entries. Profile verification fails if a [Host] entry references a script name that does not exist.


## Trigger


The script runs when Surge needs to resolve a domain that matches the [Host] entry.


DNS scripts run in the hot path of connection handling. Keep them small and fast. The JSC engine is recommended for dns scripts; see Script Engine.


## Input


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$domain` |
 String |
 The domain name to resolve. |
 |


[/TABLE]
## Result


The script must finish by calling `$done()` with an object containing one of the following:


- `address<String>`: Use this IP address as the result. It must be a valid IPv4/IPv6 address in string form.

- `addresses<Array>`: Use multiple IP addresses as the result.

- `server<String>`: Ask Surge to look up the domain via a specified upstream DNS server. It must be a valid IPv4/IPv6 address in string form.

- `servers<Array>`: Ask Surge to look up the domain via multiple specified upstream DNS servers.


When returning `address` or `addresses`, an additional `ttl<Number>` may also be returned to add the result to the DNS cache and avoid repeated lookups. The unit is seconds.


Calling `$done({})` makes Surge fall back to standard DNS resolution for the domain.


## Example


Use the public HTTP DNS API of DNSPod as a resolver:


```
$httpClient.get('http://119.29.29.29/d?dn=' + $domain, function(error, response, data){
  if (error) {
    $done({}); // Fallback to standard DNS query
  } else {
    $done({addresses: data.split(';'), ttl: 600});
  }
});

```

---
## Scripting / Event Script

# event Script


An event script runs when a specific Surge event occurs. Use it to react to environment changes &#x2014; for example, adjusting a policy group when the network changes.


[Script]
on-network-changed = type=event,event-name=network-changed,script-path=network-changed.js
## Parameters


#### event-name


Required, event name string


The name of the event to hook. If the parameter is missing, the script is never triggered. Two events are available:


- `network-changed`: Triggered when the system network changes. No event data.

- `notification`: Triggered whenever Surge posts a notification. The script receives the message even if the notification's category is turned off in the settings.


## Input


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$event.name` |
 String |
 The event name. |
 |

|
 `$event.data` |
 Object |
 Event data; contents depend on the event type. |
 |


[/TABLE]
For the `notification` event, `$event.data` contains the notification's `title`, `subtitle`, `body`, and `identifier` fields (absent fields are omitted). If the notification was posted by a script via `$notification.post`, the options object passed to it is echoed back as the `script-options` field.


## Result


The script must call `$done()` to complete. The result object is ignored; a bare `$done()` is enough.


## Constraints


- A script hooked to the `notification` event may not call `$notification.post` itself. This restriction prevents infinite notification loops; violating it aborts the script with an exception.

- Event scripts can also be triggered manually (for example via the Shortcuts app on iOS); in that case `$event.name` is `manually`.


## Examples


Post a notification with the current DNS servers when the network changes:


// on-network-changed = type=event,event-name=network-changed,script-path=network-changed.js

$notification.post('DNS Update', $network.dns.join(', '));

$done();
Log every notification Surge posts:


```
// log-notifications = type=event,event-name=notification,script-path=notification.js

console.log($event.data);

$done();

```

---
## Scripting / Cron Script

# cron Script


A cron script runs on a schedule described by a cron expression. Use it for periodic tasks such as switching a policy group by time of day or refreshing data with `$httpClient`.


[Script]
nightly = type=cron,cronexp="0 2 * * *",script-path=cron.js
## Parameters


#### cronexp


Required, cron expression string


The schedule, as a string of five or six space-separated fields. Quote the value with `"` since it contains spaces.


- A five-field expression is the standard form (minute, hour, day of month, month, day of week); the schedule has minute resolution.

- A six-field expression prepends a seconds field for second-level resolution.


Examples:


- At 2 AM daily: `0 2 * * *`

- At 5 AM and 5 PM daily: `0 5,17 * * *`

- Every minute: `* * * * *`

- Every second: `* * * * * *`

- Every Sunday at 5 PM: `0 17 * * sun`

- Every 10 minutes: `*/10 * * * *`


#### wake-system iOS Only


Optional, true/false, default false


Schedules a silent local notification at the next fire time so that the system wakes Surge to run the script even when the device is idle. Without it, a fire time may be missed while the app is suspended by the system.


## Input


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$cronexp` |
 String |
 The cron expression that scheduled this run. |
 |


[/TABLE]
When the script is triggered manually instead of by the timer, `$trigger` indicates the source (for example `intent` when run from the Shortcuts app, with the optional Shortcuts parameter in `$intent.parameter`).


## Result


The script must call `$done()` to complete. The result object is ignored; a bare `$done()` is enough. If `$done()` is never called, the run ends with a timeout warning after the script `timeout` (default 5 seconds) &#x2014; set a larger `timeout` parameter if the task legitimately needs more time.


## Manual Triggering


Besides the timer, a cron script can be run on demand:


- Surge iOS: long-press the script, or use the Shortcuts app.

- Surge Mac: run the script from the UI.

- HTTP API: `POST /v1/scripting/cron/evaluate` with body `{"script_name": "..."}`.


## Constraints


- A cron script that fires more than 10 times per hour triggers a battery consumption warning. Avoid very frequent schedules on iOS.


## Example


Switch a select group's policy at 2 AM daily, using the `$surge` API:


```
// nightly = type=cron,cronexp="0 2 * * *",script-path=cron.js
$surge.setSelectGroupPolicy('Group', 'Proxy');
$done();

```

---
## Scripting / Generic Script

# generic Script


A generic script has no automatic trigger. Use it for utility scripts that you run on demand, or as the data source of an Information Panel.


[Script]
my-tool = type=generic,script-path=my-tool.js
`generic` is also the default type: a [Script] line without a `type` parameter is treated as a generic script.


## Trigger


A generic script only runs when invoked by name:


- Surge iOS: long-press the script, or run it from the system Shortcuts app.

- Script editor: evaluate the script directly in the editor of either app.

- HTTP API: `POST /v1/scripting/evaluate` evaluates the given script text.

- Information Panel: a `[Panel]` entry with `script-name=` runs the script to render the panel content.


## Input


There is no type-specific input. The common globals are available as usual (`$network`, `$environment`, `$script`, `$argument`, &#x2026;), plus context globals describing how the script was launched:


[TABLE]


|
Field |
 Type |
 Description |
 |


|
 `$trigger` |
 String |
 How the script was launched: `editor` (script editor), `http-api` (HTTP API), `intent` (Shortcuts), `button` (panel tapped), or `auto-interval` (periodic panel refresh). |
 |

|
 `$intent.parameter` |
 String |
 The parameter passed from the Shortcuts app. Only present when triggered by a Shortcut. |
 |

|
 `$input` |
 Object |
 Panel context, only present when triggered by a panel: `{purpose: "panel", position, panelName}`. |
 |


[/TABLE]
## Result


For a plain manual run, the result passed to `$done()` is ignored; a bare `$done()` is enough.


When the script backs an Information Panel, return the panel content:


$done({
    title: 'My Panel',        // required
    content: 'Hello, Surge',  // optional
});
The result object may contain `title` (required), `content`, `style`, `icon`, and `icon-color`. See Information Panel for details.


## Example


```
// my-tool = type=generic,script-path=my-tool.js

$httpClient.get('https://api.ipify.org', function(error, response, data) {
  if (error) {
    console.log('Request failed: ' + error);
  } else {
    console.log('Current public IP: ' + data);
  }
  $done();
});

```

---
## Features / Enhanced Mode (VIF)

# Enhanced Mode


Some applications do not follow the system proxy settings. Enhanced Mode ensures Surge handles the traffic of all applications: Surge creates a virtual network interface (VIF) and registers it as the default route, capturing raw traffic regardless of proxy settings.


On Surge iOS, the VIF is part of the VPN-based takeover and is enabled by default. On Surge Mac, Enhanced Mode must be started manually.


## How the VIF Works


While the VIF is active, Surge answers all DNS queries with a virtual (fake) IP address in the `198.18.0.0/15` block. When a connection to a fake IP arrives on the VIF, Surge maps it back to the original domain name for rule matching and establishes the real connection itself. See Advanced DNS Topics for details on fake-IP behavior and related options such as `always-real-ip` and `hijack-dns`.


## Limitations


The Surge VIF can only process TCP, UDP, and ICMP traffic. Other protocols cannot pass through the VIF, so only enable this feature when necessary.


ICMP traffic cannot be proxied. Surge forwards ICMP packets directly and the VIF returns responses itself, so tools like ping keep working. Privacy-conscious users can disable this behavior with the `icmp-forwarding` option.


## Related [General] Options


These options in the [General] section tune the VIF behavior:


- `tun-excluded-routes`: bypass specific IP ranges from the VIF, letting all traffic in those ranges pass through untouched.

- `tun-included-routes`: publish additional smaller routes on the VIF so they take priority over interface-local routes.

- `ipv6-vif`: control whether the VIF is set up with IPv6.

- `icmp-forwarding`: control the ICMP forwarding behavior described above.


## Implementation Note


Starting from Surge Mac 5.8.0, Enhanced Mode is powered by Apple's Network Extension framework instead of the legacy utun driver. Existing configuration parameters such as `vif-mode` stay in the profile for backward compatibility but no longer affect the runtime behavior.

---
## Features / Gateway Mode

# Gateway Mode Mac Only


Surge Mac can operate as a layer-3 gateway, handling the traffic of other devices in the local network. Point another device's gateway (and DNS) at the Mac running Surge, and its traffic goes through the same rule and policy pipeline as local traffic. This lets devices that cannot run Surge themselves &#x2014; game consoles, TVs, or other computers &#x2014; benefit from Surge's rules, policies, and DNS handling.


Gateway Mode is enabled from the Surge Mac app UI; the profile does not carry a switch for it. Surge can also act as the DHCP server for the network, assigning addresses and announcing itself as the gateway and DNS server automatically. See DHCP for lease configuration.


## Device Management


Devices handled by the gateway appear in the device list, where you can inspect their traffic and adjust per-device settings such as a custom device name. The device list is available in the Surge Mac app and the Surge Dashboard, and can also be inspected with the `device` command of surge-cli.


## Per-Device Policies


To apply different rules to different client devices, use the `SRC-IP`, `DEVICE-NAME`, and `MAC-ADDRESS` rule types. See Source and Port Rules.


DEVICE-NAME,Apple-TV,Proxy
SRC-IP,192.168.1.100,DIRECT
## Access Restriction


By default, the gateway service only accepts devices from the current subnet, so a misconfiguration (such as a DMZ setup) does not expose it to the Internet. This is controlled by the `gateway-restricted-to-lan` option, which is enabled by default.


## UDP Fast Path Mac 6.4.0+


When Surge Mac operates in Gateway VM mode, devices that create thousands of short-lived UDP flows (such as P2P downloaders or online games) can exhaust the standard layer-4 proxy engine. The UDP Fast Path feature automatically downgrades those high-connection clients to a lightweight L3 forwarding mode whenever they exceed the threshold (10 connections within 1 second or 30 within 10 seconds).


- Packets forwarded via the fast path bypass the proxy engine entirely and therefore cannot be matched by rules or MITM.

- Destination ports below 1024 stay in normal mode to preserve compatibility with common services.

- You can toggle the fast path for each client device from the Dashboard/Device list if you need to pin a client to either behavior.

---
## Features / DHCP Server

# DHCP Mac Only


Surge can provide DHCP service for devices in the local network when Gateway Mode and the related network features are enabled.


Statically assigned IP addresses are automatically excluded from the dynamic address pool, preventing the same address from being allocated to another client. Mac 6.8.0+


## DHCP Section Mac 6.5.0+


The `[DHCP]` section can customize DHCP lease behavior. These parameters are only intended for users with special requirements; the default settings are sufficient in most cases.


[DHCP]
max-lease-time = 86400
default-lease-time = 43200
min-lease-time = 600
one-lease-per-client = true
ping-check = true
### Parameters


#### max-lease-time


Optional, seconds


The maximum lease time.


#### default-lease-time


Optional, seconds


The default lease time.


#### min-lease-time


Optional, seconds


The minimum lease time.


#### one-lease-per-client


Optional, Boolean


When enabled, Surge keeps only one active lease for each client.


#### ping-check


Optional, Boolean


When enabled, Surge checks whether an address is already in use before assigning it.

---
## Features / Subnet Settings

# Subnet Settings


Subnet settings apply specific parameters only while the device is on a matching network. Each line consists of a subnet expression followed by comma-separated `key=value` parameters.


For compatibility reasons, the subnet settings section is named `[SSID Setting]` in the profile.


[SSID Setting]
SSID:MyHome suspend=true
The subnet expression may use the `SSID:`, `BSSID:`, `ROUTER:`, and `TYPE:` forms; see Subnet Expressions for the full syntax.


## Parameters


#### suspend


Optional, Boolean


Suspend Surge temporarily under the matching networks.


[SSID Setting]
SSID:MyHome suspend=true
#### cellular-fallback iOS Only


Optional, `default` | `off` | `wifi-assist` | `hybrid`


Control the Wi-Fi Assist and Hybrid Network behavior for the matching networks.


[SSID Setting]
SSID:MyHome cellular-fallback=off

- `cellular-fallback=default`
Use the global Wi-Fi Assist and Hybrid Network settings.

- `cellular-fallback=off`
Turn off Wi-Fi Assist and Hybrid Network for the network.

- `cellular-fallback=hybrid`
Turn on Hybrid Network for the network.

- `cellular-fallback=wifi-assist`
Turn on Wi-Fi Assist for the network.


#### cellular-mode Mac Only


Optional, Boolean


Treat the matching networks as metered networks. While connected to such a network, Surge Mac automatically turns on Metered Network Mode: only the applications on the allowed list may access the Internet, and connections from other processes are rejected. Configure the allowed applications in the Surge Mac UI. See Platform Differences for an overview of Metered Network Mode.


[SSID Setting]
SSID:PhoneHotspot cellular-mode=true
#### tfo-behaviour


Optional, `auto` | `force-enabled` | `force-disabled`


Override the TCP Fast Open behavior for the matching networks.


[SSID Setting]
SSID:MyHome tfo-behaviour=force-enabled

- `tfo-behaviour=auto`
Use the default TFO behavior.

- `tfo-behaviour=force-disabled`
Disable TFO for the network completely.

- `tfo-behaviour=force-enabled`
Forcibly enable TFO for the network. This option makes Surge ignore the system TFO blackhole detection mechanism.


#### dns-server


Optional, comma-separated IP addresses or `system`


#### encrypted-dns-server


Optional, comma-separated URLs or `off`


Override the DNS settings for the matching networks.


[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=https://1.1.1.1/
If encrypted DNS is configured in the global DNS settings, you must explicitly set `encrypted-dns-server=off` to use traditional DNS on the matching network.


```
[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=off

```

---
## Features / Port Forwarding

# Port Forwarding iOS 5.14.3+ Mac 5.10.0+


Surge can listen on a specific local port and forward TCP requests from that port to a specific host. This feature works independently, even when Surge request handling (system proxy or enhanced mode) is not enabled.


[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
Each line takes the form:


<listen-address:port> <target-host:port> policy=<policy-name>
#### policy


Optional, policy name


The policy used for the forwarded connections. If it is not specified, standard rule matching determines the policy.


## Use Cases


This feature is commonly used in development and debugging scenarios, such as connecting to a server like MariaDB through an SSH proxy: Surge listens on a local port and forwards the connection to the database host via the configured policy.

---
## Features / Surge Ponte

# Surge Ponte


Surge Ponte links your Surge devices into a device-to-device network, so one device can reach another remotely &#x2014; for example, accessing your home network from outside. Devices signed in to the same iCloud account register themselves automatically; a device can also be shared with another iCloud account explicitly using a confirmation code.


Every Surge device can act as a Ponte client, but only Surge Mac can serve as the Ponte server (the access point for a home network). See Platform Differences.


## How It Works


Ponte devices register through iCloud and can then reach each other:


- By hostname: each device is reachable as `<name>.sgponte`, where the name is the device name from the device's system settings. These names are handled by Surge itself; they are not public DNS domains.

- As a policy: a rule can send matching traffic through another device by using `DEVICE:<name>` as the policy.


Depending on network conditions, a Ponte connection can be established over several channel types: Direct Access, NAT Traversal, Proxy NAT Traversal, LAN Only, and IPv6. Surge selects the channel automatically.


Setup is performed with the guided wizard in the Surge app. Most Ponte state &#x2014; device records, keys, and ports &#x2014; is stored in iCloud and app data rather than in the profile, so there is usually nothing to configure by hand.


## The [Ponte] Section


The profile carries only the Ponte parameters that reference proxy policies, as `key = value` lines:


[Ponte]
client-proxy-name = Relay-Proxy
server-proxy-name = Proxy-A, Proxy-B
#### `client-proxy-name`: Optional, policy name


The relay proxy for the client: the proxy policy this device uses to reach other Ponte devices when a relay is needed.


#### `server-proxy-name`: Optional, comma-separated policy names


The proxies the Ponte server may use for proxy-assisted NAT traversal. The referenced proxy must support Full Cone UDP relay; the setup wizard verifies this. Surge keeps these references in sync automatically when the referenced policy is renamed or deleted.


## Related Features


- The DEVICE-NAME rule matches incoming requests by the client's device name. For Surge Ponte access, the device name is the device name in the client device's system settings.

- The Surge Dashboard and iOS Remote Controller can connect to a remote device through its `<name>.sgponte` hostname when remote controller access is enabled. See Dashboard.

---
## Features / Built-in Snell Server

# Built-in Snell Server Mac Only


Surge Mac can accept incoming Snell proxy connections with the `[Snell Server]` section, letting other Surge devices use the Mac as a Snell server.


[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
When `version` is omitted, the server uses Snell v1. Existing configurations continue to work unchanged.


### Parameters


#### interface


The local address the server listens on, e.g. `0.0.0.0`.


#### port


The TCP listening port.


#### psk


The pre-shared key. Clients must be configured with the same PSK.


#### version


Optional, 1 or 6, default: 1.


The Snell protocol version served. Only `1` and `6` are accepted.


#### mode


Optional, `default` | `unshaped` | `unsafe-raw`, default: `default`. Snell v6 only.


The transport mode. Use `default` for normal deployments. Clients must set the matching `mode` parameter on their Snell policies.


### Snell v6 Mac 6.8.0+


Set `version=6` to enable the Snell v6 server:


[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
version = 6
mode = default
The built-in Snell v6 server supports reusable encrypted TCP transports and UDP tunneling. Its protocol profile is derived automatically from the PSK, so no traffic-shaping profile needs to be configured manually.


Adding `version=6` is required to opt in. Existing `[Snell Server]` sections without a version continue to use Snell v1.


### Client Configuration


Configure an outbound Snell policy on the client with a matching PSK and version:


[Proxy]
My Snell Server = snell, server.example.com, 6160, psk=RANDOM_KEY_HERE, version=6
See the Snell policy reference for all client-side parameters.

---
## Features / MTProto Proxy Server

# MTProto Proxy Server iOS 5.21.0+ Mac 6.8.0+


Surge can operate as an incoming MTProto proxy server for Telegram. A Telegram client connects to a listening port on Surge and identifies the Telegram data center (DC) it needs. Surge authenticates the proxy transport, maps the requested DC to a current production endpoint, evaluates the connection with the normal rule system, and relays the stream to Telegram.


MTProto proxy is a Telegram-specific proxy protocol. It is not a general-purpose proxy such as HTTP or SOCKS5, and it cannot be used by arbitrary applications or to reach arbitrary destinations.


An MTProto proxy&#x2014;including Surge&#x2014;does not possess the client's Telegram authorization keys and cannot decrypt message contents, alter authenticated messages, or impersonate Telegram's servers. Surge handles only the proxy transport layer; the relayed MTProto payload keeps Telegram's normal client-to-DC encryption. For details, see Telegram's MTProxy and MTProto documentation.


## Why MTProto Instead of SOCKS5


Telegram clients also support SOCKS5, but a native MTProto listener has important advantages for Telegram traffic:


- Telegram has a notorious SOCKS5 bug in which it can put an IPv6 destination address into an IPv4 request, flooding Surge with invalid connection attempts. MTProto avoids this path entirely.

- Telegram's IPv4 servers have a bug that can easily cause connections to hang without responding; IPv6 nodes do not. Because MTProto lets the proxy choose the concrete DC address, setting `ipv6=true` resolves this persistent problem. (The outbound proxy must support IPv6 forwarding.)

- An MTProto client requests a Telegram DC ID rather than a concrete server address, so Surge controls the DC-to-endpoint mapping instead of depending on an address chosen by the client.

- Telegram taken over via SOCKS5 or via VIF can easily get stuck on "Updating" after switching networks. With MTProto, DC IP selection is handled by Surge, which greatly reduces the chance of getting stuck.

- A DC can have multiple production endpoints. If one address fails, Surge marks it and uses the next eligible address for a subsequent connection to the same DC.

- The DC mapping source can be overridden with `dc-config-url` when a deployment requires different endpoint selection or update control.


All resulting DC connections still pass through Surge's normal rule system.


## Quick Start


Add the following section to the profile:


[MTProto]
interface = 127.0.0.1
port = 5753
secret = 0123456789abcdef0123456789abcdef
ipv6 = true
Generate a random secret with:


openssl rand -hex 16

After applying the profile, configure Telegram with:


- Server: an address that reaches the configured `interface`.

- Port: `5753` in this example.

- Secret: the exact secret from the profile.


Telegram also accepts proxy links in these forms:


tg://proxy?server=proxy.example.com&port=5753&secret=<secret>
https://t.me/proxy?server=proxy.example.com&port=5753&secret=<secret>

Do not publish a proxy link unless everyone who receives it is intended to use the server.


## Configuration


Only one `[MTProto]` section and one listener are supported in a profile.


#### `interface`: Required, IPv4 or IPv6 address


The local address on which Surge listens. Use `127.0.0.1` when Telegram runs on the same device and no remote client should connect; bind a specific LAN address (e.g. `192.168.1.10`) for a client on the same LAN. `0.0.0.0` exposes the listener on all available IPv4 interfaces &#x2014; convenient, but protect the port with host and network firewalls. For public access behind a router, forward the external TCP port to the Surge device's listening address and port, and put the public hostname in Telegram rather than the private LAN address.


Configuring 0.0.0.0 in Surge iOS is invalid; it will be automatically rewritten as 127.0.0.1.


#### `port`: Required, 1&#x2013;65535


The TCP port accepted by Surge. It must not conflict with another Surge listener or another process. If a router maps a different public port to this internal port, use the public port in Telegram and keep the internal port in the Surge profile.


#### `secret`: Required, 32 hexadecimal characters


The 16-byte MTProxy secret, the only client authentication credential. It is not a Telegram account password, bot token, or API key, and knowing it does not grant access to a Telegram account &#x2014; but anyone who knows it and can reach the listener can use the proxy and consume its bandwidth.


Accepted forms are the bare 32-character hex secret, or the same secret with the Telegram `dd` transport prefix:


secret = 0123456789abcdef0123456789abcdef
secret = dd0123456789abcdef0123456789abcdef
When `dd` is used, keep the prefix when entering the secret in Telegram or constructing a proxy link. The Fake TLS `ee...` secret format is not supported. Surge masks this field when exporting a profile without sensitive data.


#### `ipv6`: Optional, Boolean, default: false


The address family used for Surge's outgoing connections to Telegram DCs: with the default value Surge selects only IPv4 endpoints, with `ipv6=true` only IPv6 endpoints. Make sure the Surge device and every outbound proxy in the selected policy path can carry IPv6 destinations. This setting does not control the listener address (`interface`), and Surge does not switch it automatically based on the current system IPv6 availability.


#### `dc-config-url`: Optional, HTTP or HTTPS URL


Overrides the URL used to update the production DC mapping JSON. The default is:


https://raw.githubusercontent.com/surge-networks/MTProtoDCConfigGenerator/refs/heads/main/mtproto-dc-config.json

This is the supported mechanism for overriding the DC ID-to-address mapping. The URL must provide a complete mapping document; individual DC/IP pairs are not declared inline in the Surge profile.


Changing this URL invalidates the update timestamp associated with the previous source. The next MTProto connection continues using the current mapping and starts a non-blocking update from the new URL.


## Rule Evaluation and Outbound Policies


After resolving the requested DC, Surge creates a standard TCP request whose target is the selected Telegram IP address and port. The normal rule system then chooses the outbound policy.


- Use the `PROTOCOL,MTProto` rule to match all Telegram traffic.

- The target is normally an IP address, not a Telegram hostname. IP-based rules, ASN rules, and a Telegram ruleset containing the mapped addresses are the most reliable choices.

- A local Telegram process may provide process metadata. A client connecting from another device cannot provide the remote process identity to Surge.

- The source client address and the mapped Telegram destination remain distinct in the request record.

- If a selected Telegram endpoint fails, the next incoming connection for that DC uses the next compatible endpoint. Telegram may also retry by opening another MTProto connection.


## Telegram DC Resolution


Each production DC can have multiple IPv4, IPv6, general, media, and transport-specific endpoints, so a DC ID is not a one-to-one mapping to a single IP address.


The Telegram client writes a signed DC ID into the MTProxy initialization payload: a positive value such as `2` requests a general endpoint for DC 2; a negative value such as `-2` requests a media endpoint. Surge uses the absolute value as the DC number and retains the general/media distinction while selecting an endpoint. It:


- Excludes options that require an unsupported `tcpo_only` or per-endpoint secret transport.

- Excludes media-only options for a general request.

- Prefers media-only options for a media request when they are available.

- Prefers Telegram options marked `static`.

- Selects only IPv4 candidates by default, or only IPv6 candidates when `ipv6=true`.

- Selects the first remaining endpoint in the order provided by the DC configuration.

- Marks an endpoint as failed if the backend connection cannot be established or closes before returning any data. A subsequent connection for the same signed DC ID selects the next remaining endpoint.

- Clears the failure marks after every eligible endpoint has failed, then starts again from the first endpoint.


It is normal for an account whose home DC is DC 5 to create connections to DC 2 or another DC &#x2014; Telegram uses other DCs for configuration, media, migration, and service operations &#x2014; so Surge honors the DC requested by each connection rather than forcing all traffic to the account's home DC.


## DC Configuration, Cache, and Updates


The Surge application bundle includes a production DC mapping snapshot generated from Telegram's `help.getConfig`, so the first MTProto connection does not depend on network access to the update URL.


The update flow is:


- Surge loads a valid persistent JSON mapping into memory if one exists; otherwise it loads the bundled mapping.

- Each connection is resolved immediately from the in-memory mapping.

- If no persistent file exists, or its modification date is older than 30 days, the next access starts one non-blocking HTTP update. The triggering connection does not wait for the download, and repeated connections do not start parallel updates.

- A valid response replaces both the in-memory and persistent mapping.

- A download error, non-200 response, or invalid JSON leaves the existing mapping untouched. Surge keeps serving from the current mapping and can retry after the core is restarted, because the stale on-disk timestamp is not replaced.


The JSON `expires` value returned by Telegram is preserved as metadata but does not control Surge's refresh schedule; Surge uses the local persistent file's modification date and the 30-day interval.


The update request is made by Surge's standard HTTP client and follows normal outbound rule evaluation. Make sure the update host is reachable through the selected policy.


## Hosting a Custom DC Configuration


A custom `dc-config-url` should publish the production result generated from Telegram's `help.getConfig`; do not scrape source code arrays or combine production, test, and IPv6 test tables manually.


The response must be HTTP 200, valid JSON, no larger than 256 KiB, and contain a `version` value of `1` plus at least one valid option. A simplified example:


{
  "version": 1,
  "date": 1784605659,
  "expires": 1784609827,
  "this_dc": 2,
  "options": [
    {
      "id": 2,
      "ip": "149.154.167.41",
      "port": 443,
      "flags": 16
    }
  ]
}

Each option contains:


[TABLE]


|
Field |
 Required |
 Description |
 |


|
 `id` |
 Yes |
 Positive production DC ID. |
 |

|
 `ip` |
 Yes |
 IPv4 or IPv6 endpoint string. |
 |

|
 `port` |
 Yes |
 TCP port from 1 through 65535. |
 |

|
 `flags` |
 No |
 Telegram `dcOption` flag bitset; omitted means zero. |
 |

|
 `secret` |
 No |
 Base64-encoded per-endpoint transport secret. Such endpoints are currently not selected for raw relay. |
 |


[/TABLE]
Relevant flag values are `1` for IPv6, `2` for media-only, `4` for `tcpo_only`, `8` for CDN, `16` for static, `32` for `this_port_only`, and `1024` for an endpoint secret. Values can be combined.


`date`, `expires`, and `this_dc` are useful source metadata but are not required for endpoint lookup. Surge adds an internal source-URL marker to its persistent copy; publishers do not need to provide that field.


## Request Records and Traffic Statistics


A successfully mapped connection appears as a normal TCP request, for example `149.154.167.41:443 (Telegram DC 2 Static)`; other suffixes include `Media` and `IPv6`. The request details also contain a connection note similar to:


Incoming proxy protocol: MTProto, DC ID: 2 (general), mapped address: 149.154.167.41:443

The suffix is descriptive only. The actual target hostname, port, remote host, and rule evaluation use the mapped endpoint without the annotation.


Traffic directions are shown from the incoming client's perspective: upload is bytes sent by Telegram through Surge toward the DC; download is bytes returned by the DC to Telegram. A short-lived connection can legitimately have traffic in only one direction, especially during probing, retry, or a remote close. A large number of repeated upload-only connections usually indicates that the selected DC path or outbound policy is being closed before Telegram receives a response.


## Connection Lifecycle and Performance


Telegram decides how many MTProto connections to open and which DC each uses. Surge preserves that model:


- One incoming TCP connection creates one outgoing DC connection.

- Connections for different DCs remain separate; backend DC connections are not pooled or multiplexed across clients.

- The connection passes through the same rule and connector pipeline as other Surge TCP requests.

- MTProxy AES-CTR processing is streamed through the connection and does not alter payload length.


Opening several short connections is not inherently an error: Telegram can probe endpoints, switch DCs, recover from network changes, and maintain separate general and media paths.


## Complete Examples


Same-device proxy:


[MTProto]
interface = 127.0.0.1
port = 5753
secret = <32 random hexadecimal characters>
LAN or public listener with a custom update mirror:


[MTProto]
interface = 0.0.0.0
port = 5753
secret = dd<32 random hexadecimal characters>
dc-config-url = https://example.com/telegram/mtproto-dc-config.json
When exposing this example publicly, also configure the operating-system firewall, router/NAT mapping, and public hostname. The Surge profile alone does not publish the port to the Internet.

---
## Tools / Dashboard

# Surge Dashboard


Surge Dashboard is a graphical interface for reviewing requests, inspecting the DNS cache, and managing devices. It is included with Surge Mac and can connect either to the local Surge instance or to a remote Surge instance.


## Local and Remote Connections


On macOS, the Dashboard connects to the local Surge instance directly, with no configuration required.


The Dashboard can also manage a remote Surge instance &#x2014; another Surge Mac, or a Surge iOS device &#x2014; when `external-controller-access` is configured on the remote instance:


[General]
external-controller-access = apassword@127.0.0.1:8888
For Surge iOS, the Dashboard can connect over Wi-Fi or over USB. Since inbound connections from cellular networks are always rejected, connect the device over USB to inspect traffic while it is using a cellular connection.


Surge Dashboard can also read Logbook content from remote Surge Mac and Surge iOS instances.


## Parameters


#### `external-controller-access`


This `[General]` option enables management from an external controller, such as Surge Dashboard or Surge CLI with `--remote`.


The value is made up of three parts: password, listen address, and port number, in the form `password@address:port`. No part can be omitted.


On Surge iOS, the listen address controls which connections are accepted:


- `127.0.0.1`: only USB connections are allowed.

- `0.0.0.0`: connections from the local Wi-Fi network are also allowed.


Connections from cellular networks are always restricted for security reasons.


## Web Dashboard


Besides the native Dashboard, Surge also provides a web-based dashboard served by the HTTP API. Enable it with the `http-api-web-dashboard` option; see HTTP API and the [General] section reference.

---
## Tools / Logbook

# Logbook Mac 6.6.0+


Logbook persistently records Surge events so they remain available after Surge is closed. The current version keeps the most recent 7 days of events by default.


Surge records Logbook entries for events such as profile reloads, network switching, crash recovery, updates, and DHCP-related changes. More event types may be added in future versions.


## Remote Viewing


Surge Dashboard can read Logbook content from remote Surge Mac and Surge iOS instances. Script-type records support remote viewing of input, output, and log output.


Logbook records can also be read from the command line with `surge-cli logbook`; see Surge CLI.

---
## Tools / Testing

# Testing


Surge uses testing URLs for internet connectivity checks, proxy latency tests, and throughput tests.


## Connectivity and Latency Testing


- `internet-test-url` in `[General]` sets the URL used for internet connectivity checks; it is also the test URL for the DIRECT policy.

- `proxy-test-url` in `[General]` sets the default test URL for proxy policies. A policy can override it with its own `test-url` parameter.

- `test-timeout` in `[General]` sets the default timeout for connectivity tests. A policy can override it with its own `test-timeout` parameter.


See the [General] section reference for these options, and Common Group Parameters for how policy groups resolve testing URLs and timeouts.


## Throughput Test Parameters Mac 6.4.4+


The `[Testing]` section customizes the download and upload parameters used by the throughput test.


[Testing]
download-url =
upload-url =
download-url-proxy =
upload-url-proxy =
download-concurrency = 4
upload-concurrency = 4
download-duration-limit = 10s
upload-size-limit = 1GB
upload-duration-limit = 10s
#### `download-url`


Optional, URL


The URL used for the download throughput test.


#### `upload-url`


Optional, URL


The URL used for the upload throughput test.


#### `download-url-proxy`


Optional, URL


The URL used for the download throughput test through proxy policies. If this parameter is omitted, Surge uses `download-url`.


#### `upload-url-proxy`


Optional, URL


The URL used for the upload throughput test through proxy policies. If this parameter is omitted, Surge uses `upload-url`.


#### `download-concurrency`


Optional, integer, default: 4


The number of concurrent download connections.


#### `upload-concurrency`


Optional, integer, default: 4


The number of concurrent upload connections.


#### `download-duration-limit`


Optional, duration, default: 10s


The maximum duration of the download test.


#### `upload-size-limit`


Optional, size, default: 1GB


The maximum amount of data uploaded during the upload test.


#### `upload-duration-limit`


Optional, duration, default: 10s


The maximum duration of the upload test.

---
## Tools / CLI

# Surge CLI


Surge Mac provides a CLI program for controlling Surge from the command line. You may find it at `/Applications/Surge.app/Contents/Applications/surge-cli`.


Use `--help` to get the latest usage information.


Available commands:
  reload - Reload the main profile
  switch-profile <profile-name> - Switch to another profile

  stop - Shutdown Surge
  unattended-upgrade - Perform an unattended Surge upgrade if available

  dump active - Show all active connections
  dump request - Show recent connections
  dump rule - Show all effective rules
  dump policy - Show all proxies and policy groups
  dump dns - Show DNS caches
  dump profile [original / effective] - Show the original profile and the effective profile modified by modules
  dump event - Show events

  watch request - Keep tracing the new requests

  environment - Show environment settings
  set <key-path> <value> - Modify environment settings

  test-network - Test the network delay
  test-policy <policy-name> - Test a proxy
  test-all-policies - Test all proxies
  test-group <group-name> - Immediately retest a policy group

  kill <connection-id> - Kill an active connection
  flush dns - Flush DNS cache
  diagnostics - Run network diagnostics
  set-log-level <log-level> - Change log level without writing to the profile

  script evaluate <script-js-path> [mock-script-type] [timeout] - Load a script from a file and evaluate

Available parameters:
  --raw - Output the result in raw JSON format
  --remote/-r - Connect to a remote Surge instance instead of the local. e.g. --remote password@192.168.2.2:6170
  -c <profile-path> - Check whether a profile is valid
The `--remote` parameter requires `external-controller-access` to be configured on the remote instance; see Surge Dashboard.


## Expanded Management and Diagnostics Mac 6.8.0+


Surge CLI includes the following additional command groups. Use `surge-cli <command> --help` for the complete options supported by a command.


[TABLE]


|
Command |
 Purpose |
 |


|
 `status` |
 Show the active profile, outbound mode, feature states, uptime, and version information. |
 |

|
 `version` |
 Show Surge, Core, Controller protocol, operating-system, and device versions. |
 |

|
 `dump summary` |
 Show a passive summary of interfaces, addresses, routers, DNS servers, Wi-Fi or cellular state, and configuration warnings. |
 |

|
 `mode` |
 View or switch the Rule, Direct, and Global Proxy outbound modes. |
 |

|
 `global-policy` |
 View or change the policy used in Global Proxy mode. |
 |

|
 `policy-group` |
 List groups, inspect or change selections, and clear an automatic-group override. |
 |

|
 `profile` |
 Inspect, validate, list, or switch profiles. Listing and validation are available on macOS. |
 |

|
 `module` |
 List modules and enable or disable multiple modules. |
 |

|
 `feature` |
 Inspect or control MitM, Rewrite, Scripting, HTTP Capture, Packet Capture, and Cellular Mode. System Proxy and Enhanced Mode are also available on macOS. |
 |

|
 `device` |
 List or inspect Gateway Mode devices on macOS. |
 |

|
 `reconnect-device` |
 Reconnect an access-point client on macOS. |
 |

|
 `script list` / `script run` |
 List configured scripts or run a cron script by name. |
 |

|
 `log` / `log watch` |
 Read recent logs or stream new log entries. |
 |

|
 `logbook` / `script-log` |
 Read structured Logbook records or the log from a script execution. |
 |

|
 `benchmark encryption` |
 Measure encryption and decryption performance on the Surge device. |
 |

|
 `managed-profile update` |
 Force an update check for the active managed profile, validate the result, replace the profile, and reload it. |
 |

|
 `test-policy-bandwidth` |
 Run a bandwidth test for a policy. |
 |

|
 `proxy-runtime-status` |
 Show protocol-specific runtime details, including Tailscale and WireGuard state. |
 |


[/TABLE]
These commands can operate compatible Surge iOS 5.21.0 and Surge tvOS 5.21.0 instances through `--remote`. Query and diagnostic commands use readable formatted output by default; use `--raw` for automation. Remote Controller passwords can be entered through the secure prompt, `SURGE_CLI_PASSWORD`, or `--password-stdin` instead of placing the password in the command line.


See Surge CLI Updates for an overview of the new commands.


## Agent Skill Mac 6.5.0+


Surge includes an agent skill that exposes `surge-cli` capabilities to AI agents that support skills. The skill can be installed from `/Applications/Surge.app/Contents/Resources/Skills/`. Use a symbolic link when installing it so the skill can be updated together with the application bundle.


The bundled skill in Surge Mac 6.8.0 includes instructions for the expanded management and diagnostics commands described above. Mac 6.8.0+

---
## Tools / HTTP API

# HTTP API iOS 4.4.0+ Mac 4.0.0+


You may use the HTTP API to control Surge programmatically.


## Configuration


[General]
http-api = examplekey@0.0.0.0:6171
http-api-tls = false
http-api-web-dashboard = false
Setting `http-api-web-dashboard = true` enables a web dashboard served on the same listener, so you can control Surge from a web browser. See the [General] section reference for these options.


## Authentication


The API key must be filled in the `X-Key` header for all requests.


GET /v1/events
X-Key: examplekey
Accept: */*
In some specific situations, if it is not convenient to set the header, you can also pass it through the URL query. For example, directly downloading the CA certificate through a browser.


http://127.0.0.1:6171/v1/mitm/ca?x-key=examplekey
## HTTPS (TLS)


Setting `http-api-tls = true` enables HTTPS support for the HTTP API service. Surge will use the CA certificate of MITM to generate the server certificate for the corresponding access address. You need to install the certificate on the client device manually.


## Basic Constraints


Surge only uses GET and POST methods.


- For the GET method, use URL queries to send parameters.

- For the POST method, use a JSON body to send parameters.


Surge always returns a JSON body as the response.


## Paths


### Toggle Capabilities


- GET /v1/features/mitm

- POST /v1/features/mitm

- GET /v1/features/capture

- POST /v1/features/capture

- GET /v1/features/rewrite

- POST /v1/features/rewrite

- GET /v1/features/scripting

- POST /v1/features/scripting

- GET /v1/features/system_proxy (Surge Mac Only)

- POST /v1/features/system_proxy (Surge Mac Only)

- GET /v1/features/enhanced_mode (Surge Mac Only)

- POST /v1/features/enhanced_mode (Surge Mac Only)


Use the GET method to obtain the state of a capability.


GET Response example:


{"enabled":true}
Use the POST method to adjust the state of a capability.


POST Request example:


{"enabled":true}
### Outbound Mode


- GET /v1/outbound

- POST /v1/outbound


Use GET to obtain the outbound mode, and use POST to change it.


GET Response example:


{"mode":"rule"}
POST Request example:


{"mode":"rule"}
Possible modes: direct, proxy, rule


- GET /v1/outbound/global

- POST /v1/outbound/global


Obtain or change the default policy for global outbound mode.


GET Response example:


{"policy":"ProxyA"}
POST Request example:


{"policy":"ProxyB"}
### Proxy Policy


- GET /v1/policies


List all policies.


- GET /v1/policies/detail?policy_name=ProxyNameHere


Obtain the detail of a policy.


- POST /v1/policies/test


Test policies with a URL.


Request example:


{"policy_names": ["ProxyA", "ProxyB"], "url": "http://bing.com"}

- GET /v1/policy_groups


List all policy groups and their options.


- GET /v1/policy_groups/test_results


Obtain the test result of a url-test/fallback/load-balance group.


- GET /v1/policy_groups/select?group_name=GroupNameHere


Obtain the option of a select group.


Response example:


{"policy": "ProxyA"}

- POST /v1/policy_groups/select


Change the option of a select group.


Request example:


{"group_name": "GroupA", "policy": "ProxyA"}

- POST /v1/policy_groups/test


Test a group immediately.


Request example:


{"group_name": "GroupA"}
Response example:


{
    "available": [
        "ProxyA",
        "ProxyB"
    ]
}
### Requests


- GET /v1/requests/recent


List recent requests.


- GET /v1/requests/active


List all active requests.


- POST /v1/requests/kill


Kill an active request.


Request example:


{"id": 100}
### Profiles


- GET /v1/profiles/current?sensitive=0


Obtain the text content of the current profile. If `sensitive` is false, all password fields are masked.


- POST /v1/profiles/reload


Execute profile reloading immediately.


- POST /v1/profiles/switch (Surge Mac Only)


Request example:


{"name": "Profile2"}
Switch to another profile.


- GET /v1/profiles Mac Only 4.0.6+


Get all available profile names.


- POST /v1/profiles/check Mac Only 4.0.6+


Request example:


{"name": "Profile2"}
Check the profile. If the profile is invalid, an error is returned. Otherwise, the `error` field is null.


### DNS


- POST /v1/dns/flush


Flush the DNS cache.


- GET /v1/dns


Obtain the current DNS cache content.


- POST /v1/test/dns_delay


Test the DNS delay.


### Modules


- GET /v1/modules


List the available and enabled modules.


Response example:


{
    "enabled": [
        "router.com"
    ],
    "available": [
        "Game Console SNAT",
        "Google Home Devices",
        "router.com",
        "MitM All Hostnames"
    ]
}

- POST /v1/modules


Enable or disable modules.


Request example:


{
    "router.com": false,
    "Google Home Devices": true
}
### Scripting


- GET /v1/scripting


List all the configured scripts.


- POST /v1/scripting/evaluate


Evaluate a script with a mock environment. `script_text` is required; `mock_type` is a script type string such as `http-request` or `cron` (default: cron). The `$trigger` global is set to `http-api` during evaluation.


Request example:


{
    "script_text": "The content of JS script",
    "mock_type": "cron",
    "timeout": 5
}

- POST /v1/scripting/cron/evaluate


Evaluate a configured cron script immediately by name. Only cron-type scripts are accepted.


Request example:


{
    "script_name": "script1"
}
### Device Management Mac Only 4.0.6+


- GET /v1/devices


Obtain the list of the current active and saved devices.


- GET /v1/resources/devices-icon?id={iconID}


Obtain the icon of a device. You may get the iconID from device.dhcpDevice.icon.


- POST /v1/devices


Change the device properties. The `physicalAddress` field is required. You may adjust one or more properties from `name`, `address`, and `shouldHandledBySurge`.


Request example:


{
    "physicalAddress":"F0:9F:C2:00:00:00",
    "name": "Computer",
    "address": "192.168.1.200",
    "shouldHandledBySurge": true
}
### Misc


- POST /v1/stop


Shutdown the Surge engine. If Always On is enabled on Surge iOS, the Surge engine will restart.


- GET /v1/events


Obtain the content of the event center.


- GET /v1/rules


Obtain the list of rules.


- GET /v1/traffic


Obtain traffic information.


- POST /v1/log/level


Change the log level for the current session.


Request example:


{"level": "verbose"}

- GET /v1/mitm/ca


Obtain the CA certificate for MITM, in DER binary format. (Certificate only, no private key included)

---
## Tools / URL Scheme

# URL Scheme


Surge supports URL scheme actions on iOS and macOS for automating common operations, such as starting Surge or installing a configuration.


On iOS, use the `surge` scheme:


surge:///start
On macOS, use the `surge` scheme. The `surgeconfig` scheme is also supported for compatibility. Mac 6.7.0+


surge:///install-config?url=x
surgeconfig:///install-config?url=x
## Actions


- `surge:///start`


Start with the selected configuration. iOS only.


- `surge:///stop`


Stop the current session. iOS only.


- `surge:///toggle`


Start or stop with the selected configuration. iOS only.


- `surge:///install-config?url=x`


Install a configuration from a URL. The URL should be encoded in percent encoding.


- `surge:///install-module?url=x`


Install a module from a URL. The URL should be encoded in percent encoding.


- `surge:///email-license?email=x&key=y`


Open the email license activation flow and prefill the email and license key.


On iOS, this is available only when no active non-trial license is installed.


On macOS, this is available only while the activation window is open.


- `surge:///enterprise-license?companyID=x&userID=y&passcode=z`


Open the team license activation flow and prefill the company ID, user ID, and passcode.


`team-license` is an alias of `enterprise-license`:


surge:///team-license?companyID=x&userID=y&passcode=z
The following parameter aliases are also accepted:


`companyID`, `company-id`, `company_id`, `company`

- `userID`, `user-id`, `user_id`, `user`

- `passcode`, `pass-code`, `pass_code`


On iOS, this is available only when no active non-trial license is installed.


On macOS, this is available only while the activation window is open.


## Options


- `autoclose=true`


Automatically close Surge after the action is completed. iOS only. Cannot be used with `install-config`.


Example:


surge:///toggle?autoclose=true


## x-callback-url


Surge supports the x-callback-url specification from v3.4. The URL scheme is `surge` and the available actions are `start`, `stop`, and `toggle`.

---
## Tools / Information Panel

# Information Panel iOS Only 4.9.3+


Surge iOS lets you customize one or more information panels shown in the main view. A panel can display static text from the profile or dynamic content generated by a script.


To access this feature, users need an active subscription that expires after September 22, 2021. If the subscription expires while a `[Panel]` profile section is still configured, the panel will not be displayed, but this does not affect the normal use of other features.


Example:


[Panel]
PanelA = title="Panel Title",content="Panel Content\nSecondLine",style=info
The supported `style` values are `good`, `info`, `alert`, and `error`.


`PanelA` is the name of the information panel. This name is passed to the script in script mode.


## Static Mode


The panel generated by the configuration above is static. It can be used with a managed or enterprise profile to update panel content when the profile updates. See Managed Profile.


## Dynamic Mode


The contents of the panel can be updated by a script.


[Panel]
PanelB = title="Panel Title",content="Panel Content\nSecondLine",style=info,script-name=panel

[Script]
panel = script-path=panel.js,type=generic
Generic scripts can update panels. When the user taps the refresh button, the script is evaluated with these parameters:


$input : {
    purpose: "panel",
    position: "policy-selection",
    panelName: "PanelB"
},
$trigger: "button" // or "auto-interval"
The script should return the `title`, `content`, and `style` fields in `$done()`.


Before the script is evaluated for the first time, the panel uses the static content in the definition line. After running, Surge automatically caches the returned result of the last script execution and always displays it until the next refresh.


A sample script:


$httpClient.get("https://api.my-ip.io/ip", function(error, response, data){
    $done({
        title: "External IP Address",
        content: data,
    });
});
You may also use the `update-interval` parameter to make the panel update automatically.


[Panel]
PanelB = title="Panel Title",content="Panel Content\nSecondLine",style=info,script-name=panel,update-interval=60
Auto-updating only occurs when the user switches to the policy selection view. You may specify a small value, such as 1, to make the panel update every time.


## More Customization


- When the `style` field is not passed, the card displays only text and no icon.

- When the `style` field is not passed, the `icon` field can customize the icon with any valid SF Symbol name, such as `bolt.horizontal.circle.fill`.

- When using the `icon` field, pass the `icon-color` field to control the icon color. The value is a HEX color code.

---

## Changelog / Beta Updates

### Surge 5.102.0 (3813) — 2026-08-11 TestFlight

**New Feature: Terminal (CLI on iOS)**
- Surge iOS 现可通过 CLI 直接操作，包含完整的调试和诊断工具集
- `rule explain` 命令可查看规则评估和策略组决策逻辑
- 虚拟终端支持交互式操作、命令自动补全和历史记录
- 为未来 Surge iOS 的 AI Agent 功能奠定基础
- 详情见 `[Tools / CLI](#tools--cli)` 章节

**New Icons: Arctic & Pulse**
- 原 Surge Enterprise 图标更名为 Arctic，向所有用户开放
- 新增 Pulse 图标

**Protocol Updates**
- **MASQUE 代理支持**：基于 HTTP/3 (QUIC) CONNECT 实现多路 TCP 隧道和 CONNECT-UDP 数据报
- **HTTP/2 CONNECT UDP 中继**：可通过 `udp-relay=true` 参数转发 UDP 流量
- **TrustTunnel HTTP/3**：支持 `h3=true` 使用 HTTP/3 传输

**Policy Group**
- **组级代理链**：策略组可指定 `underlying-proxy` 底层代理，组内所有具体代理成员均通过该底层代理连接
- 可在策略组编辑器中通过 "Through Another Proxy" 配置

**HTTP API**
- 新增 **Prometheus 兼容的 `/metrics` 端点**，暴露：
  - Build information / Uptime / Memory usage
  - Active requests / DNS cache size
  - Security bans / Interface traffic
  - Per-policy traffic
- 详情见 `[Tools / HTTP API](#tools--http-api)` 章节

**Other**
- 推出新 X 账号 [@SurgeBeta](https://x.com/SurgeBeta) 用于详细的 Beta 更新说明，与 Telegram 频道同步

### Surge 5.102.0 (3815) — 2026-08-12 TestFlight

**Bug Fix**
- 修复配置了 `underlying-proxy`（底层代理链）的策略组在 UI 中无法操作的问题

**DNS Enhancement**
- `[Host]` 规则现在支持为域名别名映射指定专用 DNS 服务器
- 语法：`foo.com = bar.com, server:https://example/dns-query`
- 功能：当访问 `foo.com` 时，按 `bar.com` 的映射关系处理，但使用指定的 DoH 服务器（而非默认 DNS）来解析
- 适用场景：不同域名需要走不同 DNS 解析源（如境外 DNS 做 geo-unblock、防污染等）

### Surge 5.102.0 (3818) — 2026-08-14 TestFlight

**Surge CLI**
- 新增 `vmnet status`：查看 VMNET 接口配置，包括地址、前缀、MTU 和诊断表大小
- 新增 `vmnet arp`：查看网关模式下客户端学习到的 IPv4 邻居
- 新增 `vmnet ndp`：查看 IPv6 邻居表
- 新增 `vmnet ra`：查看 IPv6 路由通告接管状态，包括客户端、已知路由器、RA 生命周期和黑名单设备

**macOS**
- 新增图形化端口转发编辑器，可创建和管理入站 TCP 转发规则：监听地址、监听端口、目标、出站策略均可通过 UI 配置，无需手动编辑配置
- 网关模式不可用时，网关相关的设备操作现已隐藏
- 修复 VIF 模式无默认路由时仍应用系统代理设置的问题

**iOS UI**
- 导航到新页面时，底部标签栏不再隐藏——避免在 push 过渡中触发已知的 UIKit UI 故障
- 脚本编辑器现已以独立模态界面打开，包含更新的工具栏、关闭操作和改进的键盘布局
- Remote Controller 和 Ponte Diagnostics 现已对所有 Ponte 设备可用，包括由其他 iCloud 账户共享的设备
- 其他 UI 改进

**Other Improvements**
- 更新 IPv6 fake-IP 范围，避免不必要的浏览器本地网络权限提示，同时保持与已缓存地址的兼容性
- 代理连接在协议握手期间关闭时，现提供更清晰的错误消息，并指导验证凭据、加密方法和协议设置
- 修复在写入数据时代理连接同步关闭可能导致的罕见崩溃
- 修复某些条件下递归 HTTP/3 定时器处理可能导致栈溢出的问题

### Surge 5.102.0 (3819) — 2026-08-14 TestFlight

**Profile Format / Detached Sections**
- 新增通配符 detached-section：`[Ruleset *]`、`[WireGuard *]`、`[Tailscale *]`，单个 `#!include` 即可从另一个本地或远程 profile 文件加载所有匹配的命名段

**Profile Environment**
- 新增 `DEVICE_NAME` 配置环境变量，可在 `#!REQUIREMENT` 中实现设备特定条件判断（如按设备名分支配置）

**Fixed**
- `[General]` 段值中包含 `#`、`//`、`;` 时，profile 保存重载后被截断或改变的问题
- HTTP/3 或其他 QUIC 会话在待处理数据被处理时同步关闭导致的罕见崩溃

**Tailscale**
- 改进交互式登录可靠性：中断或静默断开的登录会话现在会重连并继续现有的浏览器授权流程，而不是卡住

### Surge 5.102.0 (3820) — 2026-08-17 TestFlight

**Smart Group**
- 新增 Smart Group 图形化 Policy Priority（策略优先级）编辑器

**Tailscale**
- 交互式登录现在支持需要管理员设备审批的 tailnet：登录完成但设备仍待审批时，Surge 会明确提示
- 修复控制服务器给设备分配新 tailnet 地址后 Tailscale 流量不可用的问题
- 网络变化后通过重试临时失败的 UDP 绑定、刷新直连端点，改进了恢复能力
- 改进 WireGuard 和 Tailscale 对多 peer 及过期连接的处理

**Profile and Automation**
- iOS 上磁盘变更或 iCloud 同步的 profile 现在自动重载；若更新后的 profile 无效，Surge 保留当前可用配置并报告错误
- Event scripts 新增 `engine-started` 和 `profile-reloaded` 事件（原有 `network-changed` 之外）

**Notifications**
- 新增对新代理客户端、脚本通知、规则匹配通知的通知控制
- 本地和远程通知分类设置现在正确应用到动态生成的提醒
- 禁用策略组变更通知时，同时抑制临时组覆盖提醒

**Fixed**
- 改进 MITM 证书生成：叶子证书使用独立密钥，并修正传输的证书链
- 修复 QUIC 连接在接收侧背压后可能卡住的问题
- 修复 cron 脚本关闭与 Vector UDP 连接（含 Ponte 流量）相关的罕见死锁
- 高连接 churn 和本地端口耗尽场景下的稳定性改进
- 其他小 UI 问题修复

### Surge 5.102.0 (3821) — 2026-08-19 TestFlight

**Profile System Updates**
- `#include` 指令现在可在 Section 内与普通内容自由混排，支持三种模式：
  1. **Dedicated Include**（段内仅一条 `#include`）：UI 完全可编辑，改动正确写回引用文件
  2. **Multiple Includes**（`#include a.dconf, b.dconf`）：多文件合并，只读
  3. **Mixed Content and Includes**（新）：include 与普通内容混排，只读
- ⚠️ 实测（2026-08-19）：`#include`（无感叹号）在 3821 未实装，CLI/UI 均不加载；`#!include` 正常。单文件可编辑落地，多文件/混合只读未生效。详见下方「实测」段

**Tailscale**
- 控制台注册时不再误报客户端过旧，支持版本门控操作（如编辑设备 IP）

**iOS**
- 修复托管配置 `icon-url` 图标被自动生成占位图标遮挡的问题
- 自定义策略组图标在 Lucid/Gradient 主题下行为一致，两主题均有 Default 选项
- 模块下载/解析/文件写入/安装信息失败现在会明确报错而非静默失败
- 优化 iOS 26 脚本编辑器工具栏和文件选择布局
- 改进 iOS 26 上下文菜单预览的圆角样式

### Surge 5.102.0 (3822) — 2026-08-19 TestFlight

**Profile Diagnostics**
- WireGuard/Tailscale 策略引用缺失的配置段时，现在会给出明确警告
- 警告会说明：命名 `#!include` 只加载被引用文件中同名段

**Modules and Cloud Sync**
- 模块安装信息不再受 iCloud 数据管理（避免各种 iCloud 引发的问题）；iCloud 仅用于跨设备同步安装信息
- 云同步现在排除 `.git` 和 `node_modules` 目录，且云端缺失这两个目录时不会视为"删除本地内容"的指令

**iOS**
- 修复策略组图标修改在 profile reload 后偶发丢失的问题
- 优化 iOS 26 模块菜单，避免上下文菜单动画重叠，改进 Liquid Glass 呈现

### Surge 5.102.0 (3823) — 2026-08-20 TestFlight

**Tailscale**
- Tailscale 现在可以在直连不可用时，通过符合条件的 tailnet 设备建立 peer-relay 路径，路径优先级：Direct > Peer Relay > DERP
- 运行时信息可识别 Peer Relay 连接并显示其延迟

**Rule Editor**
- 本地文件和内联规则集现可在 macOS 和 iOS 上图形化编辑。支持添加/修改标准规则、逻辑规则、嵌套规则集和注释，可重新排序或删除条目
- 可直接从规则编辑器创建新的内联规则集，并存储为命名的 `[Ruleset ...]` 段

**Profile System Updates**
- 混合使用 `#include` 不再影响对应段的 UI 写回。Surge 会根据改动自动选择尽可能准确的写回目标

### Surge 5.102.0 (3825) — 2026-08-24 TestFlight

**Improved**
- **嵌套规则集（Nested Rulesets）可靠工作**：内联规则集可引用其他内联规则集，或外部 `RULE-SET` / `DOMAIN-SET` 源。循环引用会被清晰拒绝并显示引用链（不再导致递归匹配崩溃）
- 本地规则集编辑器现在更准确保留空行、独立/尾部注释、禁用规则；无效条目会报告来源文件与行号；注释行与主规则编辑器使用一致的可读呈现
- iOS 上虚拟 IP 记录与搜索结果使用自适配行高，避免长域名和用量详情被截断

**Fixed**
- 修复 iOS 上在规则集或逻辑规则内添加的规则，保存时错误保留隐藏策略值的问题

### Surge 5.102.0 (3828) — 2026-08-26 TestFlight（5.22.0 Release Candidate 1）

**Fixed**
- 小错误修复（Minor bug fixes）

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3829) — 2026-08-27 TestFlight（5.22.0 Release Candidate 2）

**Fixed**
- 崩溃修复（Crash fixes）

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3830) — 2026-09-01 TestFlight（5.22.0 Release Candidate 3）

**Fixed**
- 修复文件名包含某些特殊 emoji 时可能出现的问题

**Improved**
- 优化低内存模式的处理逻辑

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3833) — 2026-09-06 TestFlight

**Fixed**
- 修复经代理和隧道（含 WireGuard、Tailscale）的 UDP 连接流量统计缺失
- 修复 UDP 代理连接在接收数据包期间关闭时可能阻塞 Surge 其他流量的罕见问题

**Improved**
- 改进 iOS 资源更新：应用重新激活时恢复挂起的自动更新、避免重复下载、后台刷新成功后自动清除过期错误

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3835) — 2026-09-09 TestFlight

**新增**
- **中尺寸 iOS 小组件**：合并显示启动/停止控制、运行状态、一键切换三种出站模式（按规则代理 Rule-Based Proxy / 全局直连 Direct Outbound / 全局代理 Global Proxy）。中尺寸组件支持按钮交互，可在桌面直接切换 Surge 状态

**Fixed**
- 修复 Hysteria UDP 流量失败：某些服务器上 HTTP/3 Datagram 协商干扰了 UDP 转发
- 修复 iOS 上 SF Symbol 策略组图标未随外观模式（深色/浅色）切换正确适配
- 修复极端吞吐量性能测试下结果低于预期的 bug

（来源：@SurgeTestFlightFeed；当前本机已更新至 5.102.0 (3835)，此前 3826~3834 版本记录缺失待补）

### Surge 5.102.0 (3836) — 2026-09-10 TestFlight（5.22.1 Release Candidate 1）

**新增**
- GEOIP 和 IP-ASN 规则支持 **UNKNOWN**：可匹配数据库中无对应国家/ASN 条目的目标 IP；单条规则和规则集均支持

**Fixed**
- 修复极端上传吞吐量性能测试下结果低于预期的问题
- 修复 Wi-Fi Assist 或 Hybrid 模式下蜂窝备份连接失败可能过早中止正在进行的 Wi-Fi 连接尝试（含到本地网络目标的连接）的问题
- 修复 iOS/macOS 规则编辑器中，将规则切换为非 reject 策略或不支持的规则类型后 Pre-Matching 仍保持启用的问题

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3837) — 2026-09-11 TestFlight（5.22.1 Release Candidate 2）

**Improved**
- 使用 iOS 27 SDK 编译
- 策略组小组件在 iOS 27 上支持超大尺寸（extra-large）

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3842) — 2026-09-15 TestFlight

**新增**
- 策略组新增 `category` 参数用于分组显示，可在策略组数量较多时使用

**Improved**
- 所有 `test-url` 参数现在支持配置 HTTPS URL 进行测试；测试结果仍为单次 HTTP RTT 延迟，但由于 TLS 握手，策略较多时测试耗时可能显著增加

**Fixed**
- 回退上一版本的 MITM 安全强化（为每个不同域名生成独立密钥对）：该改动导致对大量不同域名并发 MITM 时明显延迟，经评估已回退

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3848) — 2026-09-19 TestFlight

**Improved**
- 性能与内存使用优化
- 优化添加规则页（Add Rule）：域名规则现在也可为 **SNI 嗅探请求**添加（此前 SNI sniffing 仅能通过 [General] 配置，现可在规则编辑器直接为嗅探流量加域名规则）；规则特定的附加配置（rule-specific additional configurations）可直接在添加页选择，无需再切到详情页

（来源：TestFlight 更新说明；3836~3847 版本记录缺失待补）

### Surge 5.102.0 (3850) — 2026-09-22 TestFlight

**Improved**
- 全局调整 UI 布局逻辑，优化 iPhone Duo 支持细节
- 改进 UDP 测试诊断：对无 Internet 出口的对等 Tailscale / WireGuard 策略，直接报告"不支持的测试"而不是等待超时

**Fixed**
- 修复 iOS 策略组分类选择器在分类超出可用宽度时的横向滚动问题
- 修复逻辑规则错误解析包含括号的策略名称的问题

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3851) — 2026-09-23 TestFlight

**Fixed**
- 同名内联规则集现在跨主配置和模块合并（而非互相替换），保留每个来源贡献的规则

（来源：用户提供 TestFlight 截图；日期按 TestFlight 有效期推算）

### Surge 5.102.0 (3852) — 2026-09-26 TestFlight

**Fixed**
- 修复策略组中使用 Ponte 策略时仍弹出 Ponte 错误通知的问题

（来源：@SurgeTestFlightFeed；3849 版本记录缺失待补）

### Surge 5.102.0 (3853) — 2026-09-29 TestFlight

**Improved**
- 优化切换网络时 Tailscale 和 WireGuard 的行为

**Fixed**
- 修复若干极罕见的崩溃

（来源：@SurgeTestFlightFeed）

### Surge 5.102.0 (3854) — 2026-10-01 TestFlight

**Fixed**
- 修复脚本引擎的兼容性问题

**Improved**
- 其他小优化和修复

（来源：@SurgeTestFlightFeed）

### Surge 5.102.0 (3855) — 2026-10-01 TestFlight

**New**
- 使用 URL-based 链接配置文件时，现在可以手动触发更新

**Fixed**
- 修复其他一些小问题

（来源：@SurgeTestFlightFeed）

---
## 实战场景：Tailscale exit node 借道家里电脑翻墙（免 VPS，2026-08-19 落地）

**适用场景**：主设备（iPhone/iPad，外网）想借家里电脑（Windows/Mac，连 CPE WiFi）的出口访问外网，且不买 VPS、不装 Tailscale 独立 App（iOS 上 Tailscale App 与 Surge 抢 VPN，不能共存）。

**链路**：主设备 Surge tailscale 策略 → tailnet → 家里电脑 Tailscale exit node → 电脑上代理软件（TUN 模式）→ 出网

**家里电脑（出口端）**：
1. 装 Tailscale，登录 tailnet，开 exit node：`tailscale up --advertise-exit-node`，并在 Tailscale 控制台批准
2. 装代理软件（Clash 等），开 TUN/全局模式——让转发流量也被接管（仅系统代理模式不会接管 exit node 转发流量）
3. 代理软件排除 `100.64.0.0/10`（tailnet 网段直连，避免环路）

**主设备（入口端，Surge 内配）**：
```
[Proxy]
🏠家里出口 = tailscale, section-name=home-exit, hidden=0
```
```
[Tailscale home-exit]
# exit-node = <电脑的tailnet主机名>.ts.net   ← 显式指定（推荐）
exit-node = auto                            # 仅一个候选时自动选
hostname = surge-主设备
interactive-login = true
```
- `interactive-login` 身份存本机，复制配置到别台设备不复制身份，每台要各自登录一次
- 首次使用在 Surge App 打开策略编辑器完成交互登录
- Surge 自动路由 tailnet 的 MagicDNS 后缀和各 peer 地址，无需手写规则；子网路由/exit node 流量需显式规则或手动选策略
- `100.64.0.0/10` 已在 skip-proxy，tailnet 流量不环绕

**实测状态（2026-08-19）**：节点已加入 Proxy.dconf（`🏠家里出口`），reload 后 proxies 3 节点、20 组正常。电脑端未配齐，exit-node 暂为 `auto`，待电脑配好后改显式值。

---
## 实战场景：签到脚本添加 logbook 日志簿记录（2026-08-19 落地）

**问题**：cron 签到脚本默认不写入日志簿（Logbook），只有脚本主动调 `$surge.logbook()` 才会记录。用户想保留原有通知不变，额外在日志簿留痕。

**$surge.logbook API**：
```
$surge.logbook(content<String>)
```
Writes a line into Surge's Logbook under the script's name.

**改动方式**：在脚本入口的 `.then()` 回调或主流程末尾加一行 logbook 调用，通知逻辑不动。

**PingMe 签到示例**（BoxJs 框架）：
```javascript
// 改前
startTasks().then(r => $.done());
// 改后
startTasks().then(r => {
    try { $surge?.logbook('PingMe签到完成'); } catch(e){}
    $.done();
});
```

**百度贴吧签到示例**（裸脚本）：
```javascript
// 改前
mainSign().then(function() { $done(); });
// 改后
mainSign().then(function() {
    try { $surge?.logbook('百度贴吧签到完成'); } catch(e){}
    $done();
});
```

**网上国网签到**（webpack 压缩包）：无法精确 hook 异步完成点，在文件末尾追加：
```javascript
try { $surge?.logbook('网上国网签到脚本已触发'); } catch(e) {}
```

**关键注意**：
- 用 `$surge?.logbook()`（可选链）避免非 Surge 环境下报错
- 用 `try/catch` 包裹，logbook 失败不影响原有通知
- **手动运行**（Surge App 编辑器 Run 按钮）时 logbook 标题显示 **Editor** 而非脚本名——这是 Surge evaluate 通道的正常行为，实际 cron 自动运行和 `surge-cli script run` 会显示正确的脚本名
- 改远程脚本后需更新 script-path URL（加 `?v=N`）或 `surge-cli script run` 强制刷新缓存

**推送记录**：三个脚本已推送到 mickeu/surge 仓库，commit: PingMe(2b567c6f)、TieBa(6dee3483)、95598(fdf08111)。Script.dconf 已加 `?v=2` 后去掉，最新版已部署。

---
## 实战场景：Speedtest 测速慢排查（走代理导致，2026-08-20 落地）

**现象**：用 Safari 打开 speedtest.net 测下载速度只有 ~90M，但用户确认基站/CPE 历史能到 300M。怀疑是配置问题。

**排查过程**：
1. `surge-cli rule explain https://www.speedtest.net/` 显示命中 **FINAL → 🇯🇵日本**（snell 节点）——测速走代理绕路
2. 用 `surge-cli log memory N` 看连接器类型：`SGDirectConnector` = 直连、`SGProxyConnector/SGSnell` = 代理
3. 日志确认 `reedelk.speedtestcustom.com -> zd.map.fastly.net`（CNAME 到 Fastly CDN）

**关键认知**：
- Speedtest 下载测速用的域名是 **`*.speedtestcustom.com`**（测速服务器容器域），不是 `speedtest.net` 本身
- 甚至可能 CNAME 到 Fastly 等其他 CDN
- 只给 `speedtest.net` + `ookla.com` 加直连**不够**

**修复**（加到 mickeu/surge 的 Direct_Supplement.list，位于 Global_All 之前）：
```
DOMAIN-SUFFIX,speedtest.net
DOMAIN-SUFFIX,ookla.com
DOMAIN-SUFFIX,speed.cloudflare.com
DOMAIN-SUFFIX,speedtestcustom.com   # ← 关键，speedtest 下载测速实际命中的容器域
```

**验证**：
- 直连规则生效后，`surge-cli rule explain www.speedtest.net` → `RULE-SET,Direct_Supplement.list,DIRECT`
- 日志确认测速连接全部 `SGDirectConnector`（直连），无 `SGProxyConnector`
- 速度提升曲线：90M → 102M → 154M → **255M**（接近 300 真实带宽）

**经验**：
1. 测速站点直连不能只看主域名，要覆盖实际下载用的 CDN/容器域名（speedtestcustom）
2. `surge-cli log memory N` 是判断请求走直连还是代理的可靠工具（看 Connector 类型）
3. `surge-cli rule explain` 对外部规则集的子规则匹配有时有缓存，以真实测速 + 日志为准
4. 改远程规则集后：`surge-cli external-resource update <key>` 强制拉新，必要时 URL 加 `?v=N`，生效后再去掉

---
## 实战场景：本地 IPA OTA 安装方案参考（Surge Map Local + 可信域名，2026-08-20 记录）

> ⚠️ 来源说明：这是**别人分享的方案**（一张 Minis 会话截图），非本机实测。上传者已确认"这是别人的图"。下述架构、步骤、验证结果是按他人分享整理，**是否在本机可用待验证**。

**需求**：iOS 通过 itms-services 协议安装本地 IPA（测试环境），需要将 manifest.plist 托管在可信 HTTPS 域名下。

**传统方案**：LocalDevVPN（本地 VPN + 自签根证书，让 iOS 信任本地 HTTPS 环境）。

**替代方案**：利用现有 Surge，用 Map Local 把可信域名映射到本地静态 manifest 文件，省去额外装 LocalDevVPN。

**架构**：
```
可信域名 (https://example.com/manifest.plist) 
  → Surge MITM 拦截 + Map Local 返回本地文件
  → manifest.plist 里 ipa URL 指向 127.0.0.1:PORT/app.ipa
  → 本地 HTTP 服务器（如 iSH python http.server）托管 IPA
  → iOS 安装服务下载 manifest → 读 ipa 地址 → 127.0.0.1 本地下载安装
```

**前置条件**：
1. Surge MITM 已开启，且目标域名已加入 MITM hostname 列表（Map Local 匹配 https 需要 MITM 开启）
2. Surge 的 MITM CA 已安装到 iOS 信任库（日常抓包需要）
3. 本地有 HTTP 服务器托管 IPA 文件（iSH python http.server 或任何能在 127.0.0.1 起服务的工具）

**操作步骤**：
1. `manifest.plist` 放在本地，ipa URL 写 `http://127.0.0.1:PORT/app.ipa`
2. 本地起 HTTP 服务器：`python3 -m http.server PORT`（在 IPA 所在目录）
3. Surge 配置加 Map Local：`^https://example.com/manifest\\.plist data-type=file data="path/to/manifest.plist"`
4. 在 Safari 打开 `itms-services://?action=download-manifest&url=https://example.com/manifest.plist` 触发安装

**验证方法**：按他人分享，manifest 安装流程中 127.0.0.1 的 IPA 会收到 HEAD 和 GET 请求（截图显示别人已跑通）。**本机是否可行未实测。**

**与 LocalDevVPN 对比**：
| 维度 | LocalDevVPN | Surge Map Local |
|------|-------------|-----------------|
| 额外安装 | 需装 LocalDevVPN app | 无需，Surge 已有 |
| 证书 | 装自签 CA 到 iOS 信任库 | 复用 Surge MITM CA（已安装） |
| manifest 托管 | 本地 HTTPS 服务器 | Map Local 返回本地文件 |
| IPA 托管 | 与 manifest 同一本地服务器 | 可独立（127.0.0.1 任意端口） |
| 适用场景 | 专用本地 HTTPS 环境 | 已有 Surge 代理的用户顺带使用 |

**注意**：此方案依赖 Surge 的 MITM 能力，如果不打算/不能信任 Surge MITM CA，则仍需 LocalDevVPN 或其他方案。

## 实战场景：配置自动同步到 GitHub 仓库（2026-08-21 落地）

**规则**：每次修改 Surge 本地配置中可公开的段（Rule.dconf 等）后，自动同步到 GitHub 仓库 mickeu/surge。

**涉及文件**：
- 本地配置目录：`/var/minis/mounts/nssurge/`
- 仓库克隆：`/var/minis/shared/surge-sync/`（mickeu/surge 的 main 分支）
- 同步脚本：`/var/minis/shared/sync-config.sh`

**可公开（可推仓库）**：
| 文件 | 仓库路径 | 说明 |
|------|---------|------|
| Rule.dconf | Config/Rule.dconf | 规则定义，无敏感信息 |
| Proxy Group.dconf | — | 策略组定义，含订阅 URL（无密钥），待确认后加入 |

**严禁公开（含密钥，只留本地）**：
| 文件 | 敏感内容 |
|------|---------|
| mitm-ca.dconf | CA 私钥 p12 |
| Proxy.dconf | snell psk |
| Script.dconf | 网上国网明文账号密码 |
| 被🐶追的猫.conf | 主配置含所有 include 引用 |

**同步流程**：
1. 修改完成后运行：`sh /var/minis/shared/sync-config.sh`
2. 脚本检查本地 vs 仓库克隆的差异，有变更则 `cp` → `git commit` → `git push`
3. 推送使用 `GITHUB_TOKEN` 环境变量（已在 Minis 中配置），不写入仓库持久化配置

**添加新同步文件**：
修改 `/var/minis/shared/sync-config.sh` 中的 `SYNC_MAP` 变量，按 `本地文件|仓库路径` 格式追加，前提是确认该文件不含任何密钥/密码。

**注意**：
- `raw.githubusercontent.com` 有 CDN 缓存延迟（几分钟到几十分钟），git 提交内容正确即可
- 缓存容器：`/var/minis/shared/surge-sync/` 的 `.git` 目录会被 `#!include` 引用，但 git 相关文件不影响 Surge 运行
- 改配置完整流程：改本地 dconf → 跑同步脚本 → Surge 重载

## 实战场景：域名规则写入规则集而非 Rule.dconf（2026-08-21 用户明确）

**规则**：新增任何域名规则（直连、代理、拦截等）必须写进仓库已有的规则集文件（如 `Direct_Supplement.list`、`Advertising_Supplement.list` 等），推送到 mickeu/surge，**不写死进 Rule.dconf**。Rule.dconf 只通过 `RULE-SET` 引用远程规则集。

**为什么不写进 Rule.dconf**：
- Rule.dconf 是规则编排文件，放的是规则集引用 + 少量特殊规则（如 sb.sb 防误判）
- 规则集文件（.list）是可复用、可独立维护的域名集合，Surge 通过 RULE-SET 远程拉取
- 分离后 Rule.dconf 保持精简，域名条目集中在规则集文件里，便于管理和复用

**操作流程**：
1. 编辑仓库中的规则集文件：`/var/minis/shared/surge-sync/<规则集>.list`（如 `Direct_Supplement.list`）
2. 按格式添加域名：`DOMAIN-SUFFIX,<域名>`（规则集文件不需要写策略名和注释，策略在 Rule.dconf 的 RULE-SET 引用行指定）
3. git commit + push 到 mickeu/surge
4. `surge-cli reload` 让 Surge 重新拉取远程规则集
5. 验证：`surge-cli rule match <域名>` 确认命中规则集 → 正确策略

**典型案例**：sensenova.cn 直连修复（2026-08-21）
- 问题：sensenova.cn 不在 ChinaMax_Domain 域名表里，Fake-IP 模式下漏到 FINAL→PROXY，走机场共享节点 IP 触发商汤限流
- 修复：`DOMAIN-SUFFIX,sensenova.cn` 加到 `Direct_Supplement.list`（commit cdf6cff），推 GitHub
- 验证：`surge-cli rule match token.sensenova.cn` → DIRECT

## 实战场景：限流/报错排查顺序——先查 Surge 路由再查 API（2026-08-21 复盘教训）

**一句话总结**：遇到 API 限流/报错，**先 `surge-cli rule match <域名>` 确认实际路由路径**，再查 API 侧，别被"Rate limited"表象直接去查配额。

**踩坑复盘**：日日新（sensenova.cn）频繁 Rate limited
- 错误排查方向：查 API 端点、查 key 有效性、猜 QPS/配额、分析商汤限流策略 → 全猜错
- 破局信息：用户说"关了 Surge 不限流" → 才意识到问题在 Surge 路由层
- 根因：sensenova.cn 不在 ChinaMax 域名表里，Fake-IP 模式下漏到 FINAL→PROXY，走机场共享节点 IP → 被商汤按共享 IP 限流
- 修复：`DOMAIN-SUFFIX,sensenova.cn` 加到 `Direct_Supplement.list`，强制直连

**正确排查顺序**：
1. 限流/报错时 → `surge-cli rule match <域名>` 看实际命中哪条规则、走什么策略
2. 如果走代理（PROXY/AIGC 等非 DIRECT）→ 先确认该域名是否应该走代理（国内 API 经常误走代理）
3. 确认路由没问题（走 DIRECT 直连）→ 再查 API 侧（端点、key、配额、QPS）
4. 判断 Surge 路由问题的强信号：用户说"关了 Surge 就通"

**Fake-IP 常见陷阱**：
- 国内小众/新域名未被 ChinaMax 域名表收录 → 域名类规则不命中
- IP 类规则（ASN/GEOIP）依赖 resolve 真实 IP，Fake-IP 下不稳定
- 最终漏到 FINAL→PROXY → 走共享代理节点 → 目标站按共享 IP 限流/封锁
- 修复：补到 `Direct_Supplement.list`（国内域名直连）或对应规则集

---
## 实战场景：APNs 蜂窝推送收不到（2026-08-22 已解决）

**现象**：蜂窝下官方 Telegram/X 收不到推送（第三方 TG 能收到），WiFi 下正常。全局代理模式蜂窝能收、规则模式不能。

**诊断**：APNs 直连 Apple 推送服务器在蜂窝下失败。真实推送域名是 `xp.apple.com`（搭配 `push.apple.com` 及子域 gateway/courier/feedback），`push.apple.com` 用 DoH 解析无 A 记录（只返回 SOA）——这不是配置问题，是蜂窝下 APNs 直连不可达。

**正确配置组合**：
```
[General]
include-all-networks = false    # 不能 true！否则所有流量走 Surge，QQ 等对代理敏感 App 断网
include-apns = true             # 只让 APNs 被 Surge VIF 处理（关键）
include-cellular-services = false
```
APNs 域名/IP 走代理（必须在 Apple_All 之前，否则被 Apple_All 拉直连）：
```
# Rule.dconf 或 AppleIntelligence.list，策略 AIGC/PROXY
DOMAIN-SUFFIX,xp.apple.com,PROXY
DOMAIN-SUFFIX,push.apple.com,PROXY
IP-CIDR,17.249.0.0/16,PROXY,no-resolve
IP-CIDR,17.252.0.0/16,PROXY,no-resolve
IP-CIDR,17.57.144.0/22,PROXY,no-resolve
IP-CIDR,17.188.128.0/18,PROXY,no-resolve
IP-CIDR,17.188.20.0/23,PROXY,no-resolve
```

**关键平衡**（踩坑）：
- `include-all-networks=true` + 蜂窝 = 所有 App 强行走代理 → QQ 断网（对代理敏感）、微信正常（宽容）
- 正确做法：精确保留 `include-apns=true` 只让 APNs 走 Surge，配合 APNs 代理规则，其他流量不动
- APNs IP 段来自 `shadowrocket/mokuai/Apns.module`（ttyyss2233/Tool），参考用，域名放 AppleIntelligence.list

**经验**：
- 只显示角标不弹通知 → App 自身通知设置问题，与推送通道无关
- 蜂窝推送问题先分清是通道（域名/IP 可达）还是策略（走代理/直连）

---

## Surge 面板脚本关键经验（2026-08-25 实测）

### 改脚本必须换全新文件名（Surge 缓存坑）
每次修改脚本/模块内容，必须换一个**全新的文件名**（v1→v2→v3），面板 `script-name` 和 `[Panel]` 脚本名同步更新。否则 Surge 缓存旧脚本内容，重载模块也不重拉，表现为"改了没反映"。
- GitHub raw 缓存也有延迟（几秒~几十秒），jsdelivr 可能更快或更慢，改完轮询确认同步再让用户装。

### 面板脚本（generic）指定出站策略的可行方法：规则法
**结论：generic 面板脚本里 `$httpClient` 的 `policy` 参数会超时，所有脚本内指定出站的方式都不可用。**
以下是实测确认的坑：
- `$httpClient.get(url, {policy: "组名"})` → **请求挂起超时**（JSCore 和 auto/webview 引擎都测过，不行）
- `$surge.selectGroupDetails()` → generic 面板脚本里**不可用**
- `$httpAPI("GET","/v1/policy_groups")` → 返回的**不是** Controller 的 `{groups:[{name,selected}]}`，而是对象映射（策略组名→值），结构不稳定

**正确姿势（规则法，已验证成功）**：
在模块的 `[Rule]` 段加一条规则，让目标域名走 `{{{GROUP}}}` 模板参数指定的策略组：
```
#!arguments=GROUP:PROXY
#!arguments-desc=要检测的策略组名称...
[Rule]
DOMAIN-SUFFIX,ip-api.com,{{{GROUP}}}
[Script]
MyScript = type=generic,timeout=15,script-path=https://...js,argument=group={{{GROUP}}}
[Panel]
MyScript = script-name=MyScript,title="xxx",content="点击刷新",style=info,update-interval=0
```
脚本里**不指定 policy**，直接 `$httpClient.get(apiURL, cb)` 靠规则出站。请求命中 `[Rule]` 段规则 → 走 `{{{GROUP}}}` 策略组 → 返回的就是该组当前选中节点的出口 IP。

### 模块参数模板
- 声明参数：`#!arguments=GROUP:PROXY`（参数名:默认值，冒号分隔，不是 Loon 的逗号）
- 参数说明：`#!arguments-desc=...`
- 模板引用：`{{{GROUP}}}` 替换到 `[Rule]` / `[Script]` argument 等任何文本位置
- 脚本内读参数：`$argument`（generic 脚本可用），解析 `group=xxx` 形式
- 参数传递已验证正常（填 `AIGC` 脚本收到 `AIGC`），问题从来不在参数传递，在出站指定

### 模块分类字段
Surge 模块头部支持 `#!category=分类名`（同 `DNS.sgmodule` 里的 `#!category=🍟 Fries`），用于在模块 UI 分类。`#!author=` 设作者。

### 超时兜底建议
面板脚本加 `setTimeout(finish, 9000)` 兜底，请求没回调时给出明确提示，避免面板一直显示"点击刷新"无反应。
