# Surge Mac-Release 更新日志

来源频道: https://t.me/SurgeTestFlight

## 2026-09-14 [post 1752](https://t.me/SurgeTestFlight/1752)

#Mac #Release

Version 6.9.1-12290 https://dl.nssurge.com/mac/v6/Surge-6.9.1-12290-fb384eba25d82267269116bf821f4643.zip

### Improvements
- The macOS logical rule editor now supports Pre-Matching for AND, OR, and NOT rules using a reject policy, and identifies unsupported sub-rules before saving.
- Added UNKNOWN support to GEOIP and IP-ASN rules, allowing you to match destination IP addresses with no corresponding country or ASN database entry. Supported in both individual rules and rule sets.

### Fixes
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Fixed dark menu text becoming unreadable on macOS 26 and improved menu bar icon colors when the system appearance changes.
- Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.
- Fixed Hysteria UDP traffic failing with servers where HTTP/3 Datagram negotiation interfered with UDP forwarding.
- Fixed macOS Smart policy group context menus showing outdated usage or incorrect priority adjustments.

Official Channel: @SurgeTestFlightFeed

## 2026-08-10 [post 1701](https://t.me/SurgeTestFlight/1701)

#Mac #Release

Version 6.8.1-12030 https://dl.nssurge.com/mac/v6/Surge-6.8.1-12030-69f4be88db9663476f31a6b264109f0b.zip

- Fixed an issue where the Host field could be unexpectedly rewritten when handling requests in HTTP mode.
- Fixed an issue in Gateway VM mode where unsolicited UDP packets sent to the gateway's own IP (such as NAT-PMP and unicast mDNS requests) could create excessive UDP sessions, causing high CPU usage.

Official Channel: @SurgeTestFlightFeed

## 2026-08-07 [post 1695](https://t.me/SurgeTestFlight/1695)

#Mac #Release

Version 6.8.0-11990 https://dl.nssurge.com/mac/v6/Surge-6.8.0-11990-f036c2c1b04dd8ce81d8aec114ccfdcf.zip

## What's New

### macOS 27

- Began adapting the Surge interface for macOS 27 and added workarounds for macOS system bugs that could cause crashes when opening remote connections or presenting modal sheets while the system text-completion interface was active.

### Snell v6 Server

- Added Snell v6 support to the built-in Snell proxy server. Use version=6 in the [Snell Server] section to enable it. Existing configurations continue to use Snell v1 by default.
- Supports default, unshaped, and unsafe-raw modes through the mode parameter.
- Supports reusable encrypted TCP transports and UDP tunneling.
- Improved Snell handshake validation, connection lifecycle handling, EOF processing, and malformed UDP packet handling.

### Tailscale

- Added interactive Tailscale sign-in on iOS and macOS. Resolve the issue where some enterprise users are unable to obtain the auth key.
- Added automatic Tailscale routing. Surge can discover the tailnet’s MagicDNS suffix and peer IPv4/IPv6 addresses, then automatically route matching domains and peer IP traffic through the corresponding Tailscale policy.
- Automatic Tailscale routing is enabled by default and can be disabled with auto-add-magic-dns-rule = false.
- Improved Tailscale session warm-up and recovery. Sessions now retry MagicDNS discovery after startup failures and network changes without requiring matching traffic to arrive first.
- Tailscale sessions now stay active by default. An omitted idle-keepalive, 0, or -1 keeps the session always active; set a positive value to enable idle teardown.
- Tailscale can now begin handling traffic as soon as a valid network map is received, without waiting for the home DERP connection to be established.
- Improved recovery after network changes and control-server reconnections by preserving the last known home DERP region and retrying peer handshakes at the appropriate time.
- Aligned DERP measurement and selection behavior with official Tailscale client, improving compatibility with custom DERP maps, STUN-only nodes, fallback probes, and temporarily unavailable control connections.
- Sensitive values such as authentication keys and authorization URLs are now redacted from verbose Tailscale control logs.

### Surge as MTProto Server

Surge now can operate as an incoming MTProto proxy server for Telegram. 

Please read manual for more information: https://manual.nssurge.com/features/mtproto.html https://manual.nssurge.com/features/mtproto.html

### CLI & AI Skills

Surge CLI has been significantly expanded into a comprehensive command-line management and diagnostics interface, with the following new commands: https://nssurge.com/blog/surge-cli-updates/ https://nssurge.com/blog/surge-cli-updates/

### Core Version Alignment

Starting with Surge Mac 6.8.0 and Surge iOS 5.21.0, the Core Version is derived directly from the corresponding Surge Mac version, eliminating the need to maintain a separate Core Version number. Please check the manual for more information: https://manual.nssurge.com/ https://manual.nssurge.com/

## Codebase Refactoring

After more than a decade of development, the Surge codebase has grown into a large and complex project. To further improve reliability, we have introduced AI-assisted code review across the entire codebase.

Every code change is independently reviewed by Fable 5, GPT-5.6 Sol, and a human developer before being merged, helping us identify potential security issues, rare crash scenarios, and subtle correctness problems.

完整更新内容: https://nssurge.com/support/mac/release-notes https://nssurge.com/support/mac/release-notes

Official Channel: @SurgeTestFlightFeed

## 2026-07-16 [post 1661](https://t.me/SurgeTestFlight/1661)

#Mac #Release

Version 6.7.0-11730 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11730-0a67faa98116f98471bc09b946def542.zip

### Tailscale Support

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check the manual for more information: https://manual.nssurge.com/policy/tailscale.html https://manual.nssurge.com/policy/tailscale.html

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Codebase Refactoring

We have completed a comprehensive review of Surge’s core functionality and resolved numerous implementation issues, edge cases, and long-standing inconsistencies.

This ongoing refactoring effort improves maintainability and helps provide a more robust foundation for future development.

### WireGuard

WireGuard policies now use a dedicated native RTT test when no DNS server is configured, making them suitable for peer-to-peer access without requiring a reachable test URL. When a DNS server is configured, the policy is treated as a standard outbound proxy and continues to use the regular URL test process. WireGuard runtime information and diagnostics have also been updated to reflect the applicable testing mode.

### Renovation

- Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.
- Added proxy runtime details to the proxy page; right-click to view.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.
- Enable the keep-alive mechanism for all QUIC-based protocols

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-01 [post 1588](https://t.me/SurgeTestFlight/1588)

#Mac #Release

Version 6.6.0-11270 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11270-68599760a9dfa8ea625dd4ce491e534e.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

### Proxy Protocol 

- Added HTTP/2 CONNECT proxy support. You can configure HTTP/2-based CONNECT proxy connections via the h2-connect type.
- HTTP, HTTPS, HTTP/2 CONNECT, and TrustTunnel proxies now support custom request headers. You can add extra headers in the proxy configuration using headers=, for example:

Proxy = http, example.com, 8080, headers=X-Client:Surge;X-Token:abc
Proxy = h2-connect, example.com, 443, headers=X-Padding:<random-string(16-32)>

Custom headers support the <random-string(n)> and <random-string(min-max)> placeholders. A URL-safe random string will be generated automatically when connecting, suitable for scenarios that require dynamic padding or request fingerprint perturbation.

- HTTP/2 CONNECT and the TrustTunnel proxy now support multiplexing. Because too many sub-connections multiplexed over the same TCP connection may cause performance issues, by default up to 3 sub-connections are allowed. This can be adjusted via the policy parameter max-streams.

### Policy Group Icon

- You can now edit the policy group icons directly via the UI.
- In addition to URL icons, you can also use Emoji, Surge’s built-in icon library, and SF Symbols.
- Policy group icons are now written directly into the profile in a way that is shared with the Surge iOS version.

### Agent Skill

- Add a wizard page for Agent Skill usage to the Help menu

### Other
- Fixed an issue where sending SNI did not strictly comply with RFC6066. Now, when an IP address is used as the hostname, the IP address will not be sent as SNI.
- Fixed an issue where crashes could occur when using ShadowTLS with certain servers.

Official Channel: @SurgeTestFlightFeed

## 2026-04-15 [post 1518](https://t.me/SurgeTestFlight/1518)

#Mac #Release

Version 6.5.0-10960 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10960-4b553c3553fbbe2a57301cdff9ffcf8e.zip

### Agent Skill
- Surge now fully supports AI agent skill operations. We have built in instructions on how to use surge-cli to operate Surge, and have fully exposed all capabilities of surge-cli. Tell the following to your agent that supports skills to use it: 

Install the skill from the /Applications/Surge.app/Contents/Resources/Skills/ directory using a symbolic link to ensure the skill can be updated along with the application bundle.
      
### Policy Group Icon 
- It is now supported, as in the iOS version, to configure an icon for a policy group for display. You need to configure the icon-url field. There is currently no UI setting; you need to modify the configuration manually.
      
### DHCP Section
Added support for a new ​DHCP configuration section to customize DHCP settings. You can now control max​-lease​-time, default​-lease​-time, min​-lease​-time, one​-lease​-per​-client, and ping​-check directly from profile parameters.

[DHCP]
max-lease-time = 86400
default-lease-time = 43200
min-lease-time = 600
one-lease-per-client = true
ping-check = true

This feature is only provided for users with special needs; generally, the default settings are sufficient and no configuration is required.
      
### Other Improvements
- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.
- Experimental support for compatibility-mode = 5

Official Channel: @SurgeTestFlightFeed

## 2026-03-07 [post 1485](https://t.me/SurgeTestFlight/1485)

#Mac #Release

Version 6.4.4-10660 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10660-fab7cfc6bfb84df1424f90970adfcd6a.zip

### Throughput Test
Now you can customize all the parameters of the throughput test.
[Testing]
download-url = 
upload-url =
download-url-proxy = // If not provided, use download-url
upload-url-proxy = // If not provided, use upload-url
download-concurrency = // Default is 4
upload-concurrency = // Default is 4
download-duration-limit = // Default is 10s
upload-size-limit = // Default is 1GB
upload-duration-limit =  // Default is 10s

      
### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view and local DNS mapping view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-14 [post 1441](https://t.me/SurgeTestFlight/1441)

#Mac #Release

Version 6.4.3-10320 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10320-a70a06382543d5a6ae0c0296e4148569.zip

### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.
- The QUIC block behavior for all proxy protocols is now set to block by default.

### Browser Integration
- Add support for the Brave browser.

### Proxy Editing Improvements
- When you hold down the Option key and click the Surge main menu, hidden policy groups will now be displayed.
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

### CLI Improvements
- Now you can use the surge-cli -c profile.conf command to check whether a profile is valid.

Official Channel: @SurgeTestFlightFeed

## 2025-12-09 [post 1373](https://t.me/SurgeTestFlight/1373)

#Mac #Release

Version 6.4.2-9830 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9830-28a1025189d49a3f938384b58c8f5000.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- IPv6 RA override no longer broadcasts new DNS addresses to ensure maximum compatibility.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-06 [post 1338](https://t.me/SurgeTestFlight/1338)

#Mac #Release

Version 6.4.1-9550 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9550-d5ca6e6585c0a68908898b04d45e846e.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-10-24 [post 1314](https://t.me/SurgeTestFlight/1314)

#Mac #Release

Version 6.4.0-9300 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9300-e98a7823cda03b486e25eef4e7642796.zip

      
### Surge Gateway VM UDP Fast Path
      
- Currently, when using Surge in gateway mode to take over a device, if P2P applications (such as BT downloads, game installers, live streaming, etc.) are used on the device, it may result in a large number of connections appearing in the Dashboard, slowing down overall speed. If the number of connections is extremely high, it may even exhaust system resources and force Surge to restart.

- The cause of this issue is that Surge operates as a layer 4 proxy, and for every UDP packet with a different quadruple, it needs to be handled as a new connection. For most applications, even if UDP is used, only a few logical connections are typically generated, so the overhead is completely acceptable. However, for P2P applications, nearly a thousand logical connections may be generated within a few seconds.

- Therefore, this version introduces a UDP Fast Path defense mechanism. When a client initiates a large number of UDP connections in a short period of time (10 within 1 second or 30 within 10 seconds), UDP Fast Path will be enabled for that client, downgrading UDP packet processing to L3. In this mode, performance is extremely high, far exceeding the physical network card speed limit, so there is no longer a need to worry about resource consumption issues.

Additionally:

-  Packets under UDP Fast Path will be forwarded directly and cannot go through the proxy.
-  For UDP packets with a destination port number less than 1024, they will always be forwarded using the normal processing mode to avoid affecting regular applications.

### Bug Fixes

- Fix the issue where the HTTP engine might get stuck when handling consecutive requests.
- Fixed the issue where using Snell v3 to carry UDP traffic could cause a crash.

Official Channel: @SurgeTestFlightFeed

## 2025-10-06 [post 1273](https://t.me/SurgeTestFlight/1273)

#Mac #Release

Version 6.3.1-8860 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8860-8f86c3db83766069231e9c48e858053e.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Optimized the menu for adding rules in the Dashboard
- Fixed the issue where the MAC-ADDRESS rule was not taking effect correctly.
- Fixed the issue where some application icons could not be displayed on macOS 26.1.
- Fixed a potential issue where reloading the profile could cause a freeze when Surge Ponte is enabled.
- Fix potential memory leaks when using TLS-based proxy protocols.
- Fixed some color issues on macOS 26.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-15 [post 1240](https://t.me/SurgeTestFlight/1240)

#Mac #Release

Version 6.3.0-8560 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8560-e2722a66aa0ecc9dd60c3e8707aae567.zip

- Ready for macOS 26.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-11 [post 1206](https://t.me/SurgeTestFlight/1206)

#Mac #Release

Version 5.10.5-3350 https://dl.nssurge.com/mac/v5/Surge-5.10.5-3350-e93dc85636fe529df08c6e4f80d0e8a9.zip

- Ready for Surge Mac 6.
- Fix the issue of incorrect main menu text color in dark mode on macOS 26 beta.

Official Channel: @SurgeTestFlightFeed

## 2025-08-10 [post 1204](https://t.me/SurgeTestFlight/1204)

#Mac #Release

Version 6.2.0-8310 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8310-710082409fef1dc8f4011dd74697969c.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-28 [post 1171](https://t.me/SurgeTestFlight/1171)

#Mac #Release

Version 6.1.0-8010 https://dl.nssurge.com/mac/v6/Surge-6.1.0-8010-18098a9cac2d1d9c4b477873e3b037cf.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.
- Improve the compatibility of IPv6 RA override with Windows clients.
- gQUIC support has been added to the QUIC Mode of Snell v5.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-17 [post 1118](https://t.me/SurgeTestFlight/1118)

#Mac #Release

Version 6.0.2-7560 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7560-e67bf53126620427b01e574242e88dc0.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.
- Fixed some interface layout issues on devices without a connected touchpad.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1099](https://t.me/SurgeTestFlight/1099)

#Mac #Release

Version 5.10.4-3330 https://dl.nssurge.com/mac/v5/Surge-5.10.4-3330-47c0d46e960e347dcd44f46002d50966.zip

- Ready for Surge Mac 6.
- Fixed issues for macOS 26 beta.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1096](https://t.me/SurgeTestFlight/1096)

#Mac #Release

Version 6.0.1-7400 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7400-cb59cf65ab136785580975a82cc49dbd.zip

- Restored support for Snell v2/v3.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-09 [post 1075](https://t.me/SurgeTestFlight/1075)

#Mac #Release

Version 6.0.0-7210 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7210-3c89094d79d9dcff8b276e7b55ecf004.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-08 [post 1073](https://t.me/SurgeTestFlight/1073)

#Mac #Release

Version 6.0.0-7200 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7200-6ba7c0acdfb6f06ac5275526f45c3662.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-08 [post 1070](https://t.me/SurgeTestFlight/1070)

#Mac #Release

Version 6.0.0-7180 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7180-2009a9384491de13d0208992598d186b.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-08 [post 1068](https://t.me/SurgeTestFlight/1068)

#Mac #Release

Version 6.0.0-7170 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7170-d654e9b5147eadded51b635bd4aafbf6.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1066](https://t.me/SurgeTestFlight/1066)

#Mac #Release

Version 6.0.0-7160 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7160-bfce42b2db85b3b55d36b36f8a9b1cd0.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1064](https://t.me/SurgeTestFlight/1064)

#Mac #Release

Version 6.0.0-7150 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7150-32d0282aa54a4fd07ec0b16ef9e30505.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1062](https://t.me/SurgeTestFlight/1062)

#Mac #Release

Version 6.0.0-7140 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7140-243ed968ff91701fab92c19cb344e11a.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1060](https://t.me/SurgeTestFlight/1060)

#Mac #Release

Version 6.0.0-7130 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7130-a6870304f8f473ecb1ded2a7418280ed.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1058](https://t.me/SurgeTestFlight/1058)

#Mac #Release

Version 6.0.0-7120 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7120-d55bb20c95a3d63600ab5f499408d678.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1056](https://t.me/SurgeTestFlight/1056)

#Mac #Release

Version 6.0.0-7110 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7110-608977a512f0c6d37134f3eecfd38746.zip

      
### Quick Release Highlights
Please refer to the knowledge base for the complete update notes: https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/release-notes/surge-mac-6-release-note

### UI Refresh
- Brand new design style
- New dashboard with richer metrics
- Almost all pages have been refined.
- The complete macOS 26 style adjustments will be made in subsequent versions.

### Surge Gateway VM
- Gateway VM (Layer 2 via VMNET) replaces the old DHCP mode, cutting overhead and enabling richer gateway features.  
- IPv6 RA Override issues higher-priority RA messages to selected devices, fixing Fake DNS conflicts and fully taking over IPv6 without affecting others.  

### New VIF Engine
- Comprehensive optimization for Network Extension, significantly improving performance and enhancing stability in special cases, restoring v2/v3 performance lost on macOS Sequoia.  

### Ponte 2.0
- Supports multiple NAT-traversal channels (IPv6 direct, several proxy relay lines) in parallel; clients auto-select the fastest.  
- Ships with a self-hosted, low-latency STUN service.

### Smart Group
- UDP flows now receive the same intelligent path selection as TCP.  
- Resolves prior conflicts with Snell connection reuse.

### Snell v5
- Dynamic Record Sizing trims latency on lossy links.  
- QUIC Proxy Mode (UDP-over-UDP) activates for QUIC traffic, encrypts only the handshake to shield SNI while avoiding TCP-over-UDP overhead.  

### Traffic Statistics
- Per-hostname views and month-long timelines.  
- Aggregates helper processes under their parent app.

### Fake DNS v6
- DNS server now answers AAAA on fd00:6152::2, allowing pure-IPv6 deployments.

### Linked Profiles
- #include can point directly to managed-profile URLs; Surge now prompts to create a linked layer when edits are attempted.

### Other Improvements
- Single-IP support in IP-CIDR and IP-CIDR6 rules (/32 or /128 implied).  
- PROTOCOL,TCP applies to HTTP/HTTPS for semantic parity.  
- Faster loading for huge profiles.  
- full-header-mode exposes complete header arrays.  
- Default fallback for proxies lacking UDP support: REJECT.  
- Adds zstd compression and faster wildcard matching.  
- Entire Advanced Settings page rewritten—every parameter editable in-app.

Official Channel: @SurgeTestFlightFeed

## 2025-07-07 [post 1053](https://t.me/SurgeTestFlight/1053)

#Mac #Release

Version 6.0.0-7100 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7100-403faa55c35e84189ebb5f03199b9ec0.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1051](https://t.me/SurgeTestFlight/1051)

#Mac #Release

Version 6.0.0-7090 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7090-3fe2013a818c6ceaa46f25531ae3304e.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1049](https://t.me/SurgeTestFlight/1049)

#Mac #Release

Version 6.0.0-7070 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7070-ab84e895b571d57e920893547fff049f.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1047](https://t.me/SurgeTestFlight/1047)

#Mac #Release

Version 6.0.0-7060 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7060-30b2b5a3f6adf5e82371f84edbca63bf.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1044](https://t.me/SurgeTestFlight/1044)

#Mac #Release

Version 6.0.0-7030 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7030-a49742ce9bb67c99f72baf84b62dc7b5.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1042](https://t.me/SurgeTestFlight/1042)

#Mac #Release

Version 6.0.0-7010 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7010-55620b6f19413f1b92ac6caa309a38d3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1040](https://t.me/SurgeTestFlight/1040)

#Mac #Release

Version 6.0.0-7000 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7000-4304f05f2019c0acadb3c70601eb3b1c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1038](https://t.me/SurgeTestFlight/1038)

#Mac #Release

Version 6.0.0-6980 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6980-509b98e167c8fc8f5d356e69c262a7f2.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1036](https://t.me/SurgeTestFlight/1036)

#Mac #Release

Version 6.0.0-6950 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6950-e9f00c7e424ee9cb74c684f5aa9862df.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1034](https://t.me/SurgeTestFlight/1034)

#Mac #Release

Version 6.0.0-6930 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6930-e9ad912908f8c3b0747221dea34d5f60.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1032](https://t.me/SurgeTestFlight/1032)

#Mac #Release

Version 6.0.0-6860 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6860-bcc8a10f6519aed3918c9004dcd0a2b3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1030](https://t.me/SurgeTestFlight/1030)

#Mac #Release

Version 6.0.0-6850 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6850-2123a9ea85159cb36abe9dd30bb11885.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1028](https://t.me/SurgeTestFlight/1028)

#Mac #Release

Version 6.0.0-6840 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6840-ef9bf8b23a1d6cb822310832bd6bb155.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1026](https://t.me/SurgeTestFlight/1026)

#Mac #Release

Version 6.0.0-6830 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6830-34500b67d6e7f6e3298e60fb54b04a08.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-03 [post 1023](https://t.me/SurgeTestFlight/1023)

#Mac #Release

Version 6.0.0-6810 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6810-6269ecafdbf6fb6bb5671766a02fbb6c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-03 [post 1021](https://t.me/SurgeTestFlight/1021)

#Mac #Release

Version 6.0.0-6760 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6760-f0029fae2cdc9374c9bf60914f9e4bfb.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1018](https://t.me/SurgeTestFlight/1018)

#Mac #Release

Version 6.0.0-6700 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6700-402a98b37d9806cdca40951b36e714eb.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1016](https://t.me/SurgeTestFlight/1016)

#Mac #Release

Version 6.0.0-6690 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6690-222b61553d2df858566ce2b31540a9d7.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1014](https://t.me/SurgeTestFlight/1014)

#Mac #Release

Version 6.0.0-6680 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6680-c85bb1313c4298261dffb088a2f43075.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1012](https://t.me/SurgeTestFlight/1012)

#Mac #Release

Version 6.0.0-6670 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6670-c2ac024733216518ffaf50743992ba14.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1010](https://t.me/SurgeTestFlight/1010)

#Mac #Release

Version 6.0.0-6660 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6660-d346f46d21547c3d905c4c4238f84f85.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1008](https://t.me/SurgeTestFlight/1008)

#Mac #Release

Version 6.0.0-6650 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6650-2c4cea3d5aa965830307b9713c662329.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 996](https://t.me/SurgeTestFlight/996)

#Mac #Release

Version 6.0.0-6590 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6590-c6e4026e99a06af4069177d0f6b6944d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 994](https://t.me/SurgeTestFlight/994)

#Mac #Release

Version 6.0.0-6580 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6580-19cddde88ee943fee08aa9df1387a2c3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 992](https://t.me/SurgeTestFlight/992)

#Mac #Release

Version 6.0.0-6570 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6570-d99b4dd607f2a7f1cf170e824b1c6a4d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 990](https://t.me/SurgeTestFlight/990)

#Mac #Release

Version 6.0.0-6560 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6560-e7156e3e07c271fc7b1c8f50222d0c1c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 1005](https://t.me/SurgeTestFlight/1005)

#Mac #Release

Version 6.0.0-6610 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6610-d2116e3eed2c9ac9876f579fc28bc310.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 1002](https://t.me/SurgeTestFlight/1002)

#Mac #Release

Version 6.0.0-6600 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6600-62817a8be002e0b3a3afef7d88769c5e.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 988](https://t.me/SurgeTestFlight/988)

#Mac #Release

Version 6.0.0-6550 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6550-935f1a0ce346835da1f9213a52cd5b25.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 986](https://t.me/SurgeTestFlight/986)

#Mac #Release

Version 6.0.0-6540 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6540-2ad14205d51fcf510fb1ba58a1f90c0d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 983](https://t.me/SurgeTestFlight/983)

#Mac #Release

Version 6.0.0-6530 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6530-09ef1aa2eee493b0a05ecc5f0a7104f1.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-29 [post 974](https://t.me/SurgeTestFlight/974)

#Mac #Release

Version 6.0.0-6480 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6480-f018946bc78c4f4b41664f8be4fa7c69.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-29 [post 972](https://t.me/SurgeTestFlight/972)

#Mac #Release

Version 6.0.0-6430 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6430-4b32e4c65f8b99e1902e061bde7fc2f8.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 970](https://t.me/SurgeTestFlight/970)

#Mac #Release

Version 6.0.0-6380 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6380-9e92b45e61db9ef0a53021bde549693c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 968](https://t.me/SurgeTestFlight/968)

#Mac #Release

Version 6.0.0-6360 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6360-23936e729b2632cd3cef3b3d50470ba8.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 966](https://t.me/SurgeTestFlight/966)

#Mac #Release

Version 6.0.0-6350 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6350-665c0fd38f72c61e47c1aadacb14580c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 964](https://t.me/SurgeTestFlight/964)

#Mac #Release

Version 6.0.0-6320 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6320-a11127ff556e409af1a7dabed663eca7.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-05-12 [post 949](https://t.me/SurgeTestFlight/949)

#Mac #Release

Version 5.10.3-3272 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3272-5cf851de0c9af2bf96ab410244010f9a.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Added dark mode support to the error page.
- Add integration support for the Dia browser.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-22 [post 896](https://t.me/SurgeTestFlight/896)

#Mac #Release

Version 5.10.2-3235 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3235-9255a55c4af59cbf0ed01b245ef86dcc.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-20 [post 862](https://t.me/SurgeTestFlight/862)

#Mac #Release

Version 5.10.1-3207 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3207-1e925800c695a40e8a34ceca6d856b0d.zip

- When enabling the HTTP capture switch, all active connections will now be forcibly interrupted to ensure that no requests are missed due to existing long connections.
- Optimized compatibility with some QUIC clients, such as Lark.
- Fixed an issue where download data bytes in statistics was incorrect after modifying the request HTTP using scripts or other mechanisms.
- Adjusted the priority of processing logic when forwarding QUIC. Now, for a proxy policy that does not support UDP forwarding, it will prioritize considering QUIC Block before falling back to DIRECT or REJECT.
- Fixed an issue where utun devices could not be used when binding the outbound interface.
- Fixed an issue where repeated notifications might continuously occur during Ponte Server retry failures.
- Resolved an issue where a specific request forwarded by Surge Ponte might get stuck under certain networks.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-20 [post 843](https://t.me/SurgeTestFlight/843)

#Mac #Release

Version 5.10.0-3195 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3195-d468f4e99b54bcde0432f2b5a0e38296.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

### #!REQUIREMENT upgrade
- Now provides three simple notations: #!IOS-ONLY, #!MACOS-ONLY, and #!TVOS-ONLY.
- Content disabled by this end-of-line comment can now be displayed and edited in the UI. It will appear as disabled when conditions are not met, and if enabled, restrictions will be automatically removed.

Example

DOMAIN,reject.com,REJECT #!MACOS-ONLY

### Host Optimization

Host section supports configuration using DOMAIN-SET and RULE-SET to improve matching efficiency. Use case:

[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.com/dns-query
RULE-SET:https://example.com/rules.txt = server:https://doh.com/dns-query

### Other Improvements

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-09 [post 760](https://t.me/SurgeTestFlight/760)

#Mac #Release

Version 5.9.3-3122 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3122-0244efc5738b3cebde7c87c556cfddb8.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-11-22 [post 729](https://t.me/SurgeTestFlight/729)

#Mac #Release

Version 5.9.2-3098 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3098-643c195efc1153b6d4993af6bba73a59.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-01 [post 629](https://t.me/SurgeTestFlight/629)

#Mac #Release

Version 5.9.0-3025 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3025-f8d045da66079150d4a281ed3770b3f6.zip

### New Features
- Added pre-matching rules for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- Body Rewrite supports using JQ expressions to manipulate JSON.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes

### Improvements
- The URL-REGEX rule now supports extended-matching tags.
- Allow the use of Ponte policy as an underlying proxy.
- Modify the termination logic of HTTP scripts. If a request needs to be interrupted, use $done({abort: true}). Other failures will not modify or terminate the request.
- Overall optimization and improvement of UDP forwarding.

### Bug Fixes
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.
- Fix the issue of not being able to obtain system routes on macOS 12.
- Fix the issue where determining the existence of IPv6 might be incorrect in some cases.
- Fix the issue where an incorrect message might sometimes indicate that the proxy settings have been modified by another program.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-14 [post 512](https://t.me/SurgeTestFlight/512)

#Mac #Release

Version 5.8.2-2946 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2946-b739968f1d90da3b755d3bf82941e8c2.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Improved HTTP engine compatibility with non-standard requests
- Enhanced error handling logic for encrypted DNS, retrying immediately upon encountering errors 
- Other bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-25 [post 484](https://t.me/SurgeTestFlight/484)

#Mac #Release

Version 5.8.1-2929 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2929-5220af95366dfacec7ca84cb8ddd122c.zip

 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-16 [post 451](https://t.me/SurgeTestFlight/451)

#Mac #Release

Version 5.8.0-2900 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2900-6379c9d5240ae1555772aed2eb977e69.zip

### Network Extension
- Due to numerous issues arising from the traditional utun takeover solution in newer system versions, starting from Surge Mac 5.8.0, Surge Mac will use Network Extension as the enhanced mode to take over the system network.
- The minimum system version requirement for Surge Mac is raised to macOS 12.
- Due to different required permissions, manual authorization operations is needed after updating.
- The vif-mode parameter will no longer be effective.
- Enhanced mode can now be used in conjunction with network sharing functionality, meaning you can directly create a Wi-Fi managed by Surge (requires wired network)

### Port Hopping

Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

Parameters:

- port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
- port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

### Other Improvments

- Due to the large amount of features requiring permissions in the new macOS system, a dedicated page has been added for managing system permissions.
- The syslib keyword for local DNS mapping can now be used in enhanced mode. However, in non-enhanced mode, the resolution is entirely handled by the system. In enhanced mode, Surge resolves it using the system's DNS address.
- Added [General] parameter show-error-page, which is used to control whether Surge's HTTP error page is displayed when an error occurs. This parameter is enabled by default, and the behavior is consistent with previous versions.

Official Channel: @SurgeTestFlightFeed

## 2024-08-31 [post 382](https://t.me/SurgeTestFlight/382)

#Mac #Release

Version 5.7.5-2826 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip

- The panel is now available in Surge Mac.
- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-06-21 [post 304](https://t.me/SurgeTestFlight/304)

#Mac #Release

Version 5.7.4-2806 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2806-afe67661ef616b7bbab189dec1473b68.zip

- Due to the sudden shutdown of a public STUN server that Surge Ponte relies on, resulting in the unavailability of Surge Ponte, we have carried out an emergency replacement. Additionally, we will build our own STUN server in the future to avoid such issues.
- Enhance compatibility with VPN and multiple network cards

    In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

    However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

    This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.
    
- Fix an issue where DOMAIN-SUFFIX rules may become invalid if duplicate DOMAIN and DOMAIN-SUFFIX rules are included in the rule set
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-06-21 [post 300](https://t.me/SurgeTestFlight/300)

#Mac #Release

Version 5.7.4-2805 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2805-bc9f3a083975f73e9d03ae05ee60eda8.zip

- Due to the sudden shutdown of a public STUN server that Surge Ponte relies on, resulting in the unavailability of Surge Ponte, we have carried out an emergency replacement. Additionally, we will build our own STUN server in the future to avoid such issues.
- Enhance compatibility with VPN and multiple network cards

    In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

    However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

    This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.
    
- Fix an issue where DOMAIN-SUFFIX rules may become invalid if duplicate DOMAIN and DOMAIN-SUFFIX rules are included in the rule set
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-05-29 [post 251](https://t.me/SurgeTestFlight/251)

#Mac #Release

Version 5.7.3-2785 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2785-048c0bdc5ee2b05dab39852d51a19ff4.zip

- Now you can see the number of times a rule has been used in the rule list.
- Optimized the implementation method of blocking QUIC traffic to increase the likelihood of clients correctly falling back.
- The Smart group will use the SUBSTITUTE policy (DIRECT) instead of failing directly when there are no sub-policies.
- Fixed an issue where the server-cert-fingerprint-sha256 parameter was not effective for TLS-like protocols with sni=off settings.
- Added a new rule type HOSTNAME-TYPE, used to determine the type of request hostname. Optional values are: IPv4, IPv6, DOMAIN, SIMPLE. (SIMPLE refers to hostnames without a dot, such as localhost)
- Optimized DNS request logs. Now more information is displayed. Additionally, if DIRECT policy connects directly without triggering DNS in the rule system, related DNS logs can still be shown.
- When deleting a policy that is being used by a policy group, it is now allowed to delete it directly and automatically remove it from all policy groups.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-10 [post 211](https://t.me/SurgeTestFlight/211)

#Mac #Release

Version 5.7.2-2762 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2762-9a963758f386b5da00e7744b2a7f254d.zip

- Optimize the matching performance of ASN rules in the rule set.
- Fix the issue where FINAL rules cannot be edited through UI.
- Fix the problem that invalid cron expressions would cause scripts to be executed repeatedly.
- Optimized the management mechanism of the script engine.
- Other detail issues fixed.

Official Channel: @SurgeTestFlightFeed

## 2024-05-10 [post 209](https://t.me/SurgeTestFlight/209)

#Mac #Release

Version 5.7.2-2761 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2761-d1600a18bbcc9bd9f6768e1a16a6b9e8.zip

- Optimize the matching performance of ASN rules in the rule set.
- Fix the issue where FINAL rules cannot be edited through UI.
- Fix the problem that invalid cron expressions would cause scripts to be executed repeatedly.
- Optimized the management mechanism of the script engine.
- Other detail issues fixed.

Official Channel: @SurgeTestFlightFeed

## 2024-04-29 [post 195](https://t.me/SurgeTestFlight/195)

#Mac #Release

Version 5.7.1-2758 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2758-f5ff0b10bf04ff39a861da762eb144af.zip

- Optimize the matching performance of small rule sets, especially evident on older CPU models.
- The external resource update page can display error information generated by rule set processing.
- Automatically ignore invalid empty lines in the rule set.
- Fixed an issue where applying temporary rules would not interrupt existing connections if a policy change occurred.
- Fixed an issue when using Ponte policy within Smart group, if the target device is itself, it was not automatically switched to DIRECT policy.
- Corrected the time error displayed in request logs for Ponte device requests.
- Fixed a low probability crash that occurs when external policy group content changes.
- During the initialization phase of Smart group, no longer display most used tags to avoid misunderstanding .
- Fixed a crash that could occur when adding a policy group if an external policy was selected but no URL was provided.
- Corrected an issue where items did not correctly display their storage location after being moved on the key management page.

Official Channel: @SurgeTestFlightFeed

## 2024-04-29 [post 193](https://t.me/SurgeTestFlight/193)

#Mac #Release

Version 5.7.1-2757 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2757-e7b680d5dc23e1258188adc4d81116d7.zip

- Optimize the matching performance of small rule sets, especially evident on older CPU models.
- The external resource update page can display error information generated by rule set processing.
- Automatically ignore invalid empty lines in the rule set.
- Fixed an issue where applying temporary rules would not interrupt existing connections if a policy change occurred.
- Fixed an issue when using Ponte policy within Smart group, if the target device is itself, it was not automatically switched to DIRECT policy.
- Corrected the time error displayed in request logs for Ponte device requests.
- Fixed a low probability crash that occurs when external policy group content changes.
- During the initialization phase of Smart group, no longer display most used tags to avoid misunderstanding .
- Fixed a crash that could occur when adding a policy group if an external policy was selected but no URL was provided.
- Corrected an issue where items did not correctly display their storage location after being moved on the key management page.

Official Channel: @SurgeTestFlightFeed

## 2024-04-25 [post 133](https://t.me/SurgeTestFlight/133)

#Mac #Release

Version 5.7.0-2724 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2724-acaafccea020f6afdc758c83057ffcbb.zip

### Smart Group

This is a new type of policy group, driven by our carefully designed algorithm engine, which can automatically select the appropriate policy from the sub-policies of this policy group. The goal of the Smart policy group is to replace the original automatic testing groups (url/load-balance/fallback), greatly optimizing the experience while minimizing the need for manual intervention in policy groups. Users only need to put the available policies into this group.

For details, see: https://kb.nssurge.com/surge-knowledge-base/guidelines/smart-group https://kb.nssurge.com/surge-knowledge-base/guidelines/smart-group

### Rule System
- Overall performance optimization of the rule system.
- Significant optimization of the indexing algorithm in large domain rule sets, improving the search efficiency by more than ten times for rule sets with more than 100,000 rules.
- Corrected the issue where sub-rules of logical rules within a rule set could not be covered by the no-resolve and extended-matching parameters of the rule set.
- Added a new rule type DOMAIN-WILDCARD, supporting ? and * domain name matching.
- DOMAIN-SET and RULE-SET are changed to strict validation. If there are invalid lines in the file, the entire rule set will be invalidated to avoid problems caused by misuse.

### IPv6
- The behavior of the ipv6-vif parameter has been modified. When set to always, IPv6 functionality will be enabled even if ipv6=true is not set.
- Added a warning for the ipv6-vif=always parameter.
- Adjusted the automatic retry mechanism. Accessing IPv6 addresses in a non-IPv6 network will no longer enter the retry process, and the request will fail immediately (solving the problem of some applications stalling when IPv6 VIF is enabled in a non-IPv6 environment, but the application will still continue to send IPv6 requests).

### Other Optimizations
- Enhanced $notification.post, adding support for media resources, sound hints, and automatic dismissal.
- Optimized WireGuard failure handling.
- Reduced the power consumption of the TUIC protocol during sleep.
- Improved the precision of time statistics in the request log system, now accurate to µs level.
- Optimized various abnormal retry mechanisms, avoiding high resource usage caused by continuous retry in the face of some specific problems. For operations that need to be retried continuously (such as WireGuard reconnection, Ponte server reporting to iCloud), Surge will now retry after 0.1s, 0.5s, 1s, 5s, 10s, 30s after an error.
- Optimized the caching system for external resources.
- Added the profile line modifier #!REQUIREMENT.

### Minor Adjustments
- Limited the length of logs that can be written to request notes in debug mode by scripts.
- Changed the default UDP test target to 1.0.0.1 http://1.0.0.1/.
- If incorrect types of fields are passed when using API in scripts, it will result in script errors.
- After the script is completed or times out, unfinished $httpClient will no longer call the callback function.

### Issue Fixes
- Fixed the issue where the HTTP Body captured from remote devices could not be read in the Dashboard.
- Fixed the problem where Header Rewrite rules could not match URLs based on the Host field.
- Corrected the issue where ip-version and tos parameters could not take effect when testing proxies.
- Fixed the crash issue caused by mistakenly passing null when executing scripts via HTTP-API.

