# Surge Other 更新日志

来源频道: https://t.me/SurgeTestFlight

## 2026-10-06 [post 1781](https://t.me/SurgeTestFlight/1781)

VS Code Extension

Added support for the Surge Language Support extension for VS Code, providing syntax highlighting and real-time diagnostics for profiles, modules, and rule sets. Includes automatic file detection and validation of policy references in detached configurations when the main profile is open. 

This extension relies on the Surge application package and requires Surge Mac 6.10.0 or later. Its profile parsing capabilities are automatically updated when Surge is upgraded.

https://marketplace.visualstudio.com/items?itemName=SurgeNetworks.surge-language-support https://marketplace.visualstudio.com/items?itemName=SurgeNetworks.surge-language-support

## 2026-10-05 [post 1777](https://t.me/SurgeTestFlight/1777)

Beta Updates

New Features - IP Rewrite
- Added the [IP Rewrite] section, which handles packets entering Surge VIF at the IP layer based on their destination address, before they reach any rule or policy. Available actions:- reflect: Swaps the source and destination addresses and sends the packet back to its sender.
- reject: Responds with a TCP RST to connection attempts and with an ICMP administratively prohibited message to other packets, so the sender fails immediately.
- drop: Silently discards the packet.

For example, you can use the following module to make Surge work as LocalDevVPN, allowing you to use certain developer toolchains on iOS devices.

#!name=Local Device Loopback
#!desc=Reflect 10.7.0.1 back to this device for on-device developer tools.
[General]
ipv6-vif = disabled // Some tools only recognize utun interfaces without an IPv6 address.
tun-included-routes = %INSERT% 10.7.0.1/32

[IP Rewrite]
10.7.0.1 = reflect

## 2026-09-25 [post 1768](https://t.me/SurgeTestFlight/1768)

A new guide has been added to the Surge Knowledge Base, covering how to remotely manage a Surge instance.

https://kb.nssurge.com/surge-knowledge-base/guidelines/remote-management https://kb.nssurge.com/surge-knowledge-base/guidelines/remote-management

## 2026-09-14 [post 1754](https://t.me/SurgeTestFlight/1754)

Beta Updates

- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.

## 2026-09-14 [post 1753](https://t.me/SurgeTestFlight/1753)

Surge Mac 6.9.1 & Surge iOS 5.22.1 are now available.

New Features
- [iOS] Policy group widgets now support the extra-large size on iOS 27.
- [iOS] Added a medium-sized iOS widget with start/stop controls, running status, and one-tap switching between Rule-Based Proxy, Direct Outbound, and Global Proxy.
- Added UNKNOWN support to GEOIP and IP-ASN rules, allowing IP addresses without matching country or ASN database entries to be matched. This works in both individual rules and rule sets.

Fixes and Improvements
- Fixed lower-than-expected results under extreme throughput performance testing.
- Fixed failed cellular backup connections in Wi-Fi Assist or Hybrid mode prematurely aborting an ongoing Wi-Fi connection attempt.
- Fixed Pre-Matching remaining enabled after changing a rule to a non-reject policy or unsupported rule type.
- Fixed Hysteria UDP forwarding with servers where HTTP/3 Datagram negotiation interfered with UDP traffic.
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where closing a UDP proxy connection during packet reception could stall other Surge traffic.
- Fixed SF Symbol policy-group icons not responding correctly to appearance changes on iOS.
- [iOS] Improved resource updates on iOS: pending automatic updates resume when the app becomes active, duplicate downloads are avoided, and stale errors are cleared after a successful background refresh.
- [Mac] Fixed macOS Smart policy group context menus showing outdated usage or incorrect priority adjustments.
- [Mac] Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.

## 2026-09-01 [post 1742](https://t.me/SurgeTestFlight/1742)

Surge iOS 5.22.0 is now available on the App Store.

New Features

* Added a full-featured Terminal to Surge iOS, providing CLI-based diagnostics, rule explanations, policy-group inspection, command completion, and command history.
* Added MASQUE proxy support using HTTP/3 CONNECT and CONNECT-UDP.
* HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
* TrustTunnel can now use HTTP/3 transport with h3=true.
* Added group-level proxy chaining. Policy groups can connect concrete proxy members through an underlying proxy.
* Added a Prometheus-compatible /metrics endpoint to the HTTP Controller.
* Added a graphical Policy Priority editor for Smart Groups.
* Added event-script support for engine-started and profile-reloaded.
* Added notification controls for proxy clients, scripts, and rule matches.
* Added Arctic and Pulse app icons.

Tailscale

* Added peer-relay support through eligible tailnet devices, with Direct → Peer Relay → DERP priority and runtime latency information.
* Interactive sign-in now supports tailnets that require administrator device approval.
* Improved recovery from interrupted sign-in by reconnecting and continuing the existing authorization flow.
* Improved compatibility with the Tailscale administration console and version-gated operations.
* Fixed connectivity issues after the control server assigns a new tailnet address.
* Improved recovery after network changes, UDP binding failures, expired connections, and in multi-peer configurations.

Profiles, Includes, and Rulesets

* #include (?q=%23include) directives can now be freely combined with regular section content.
* Sections using multiple or mixed includes are presented as read-only when their write-back destination is ambiguous.
* Added wildcard detached-section includes for [Ruleset *], [WireGuard *], and [Tailscale *].
* Added DEVICE_NAME to the profile environment for use in #!REQUIREMENT.
* Added diagnostics for missing WireGuard and Tailscale configuration sections and clarified named-include behavior.
* Local and inline rulesets can now be edited graphically on macOS and iOS.
* Rulesets can reference other inline rulesets as well as external RULE-SET or DOMAIN-SET sources.
* Circular ruleset references are rejected with a clear reference chain.
* The ruleset editor now better preserves blank lines, comments, disabled rules, and source locations.
* Fixed rules created inside rulesets or logical rules retaining an unintended hidden policy value.
* Improved selection of the appropriate write-back target when mixed includes are used.
* Fixed [General] values containing #, //, or ; being altered after saving.
* Profiles changed on disk or through iCloud now reload automatically, while invalid updates leave the working configuration active.
* Module installation state is no longer governed directly by iCloud.
* Cloud synchronization now excludes .git and node_modules.

UI and Editing

* The bottom tab bar remains visible during navigation to avoid UIKit transition glitches.
* The Script Editor now uses a dedicated modal interface with an improved toolbar and keyboard layout.
* Remote Controller and Ponte Diagnostics are available for all Ponte devices, including shared devices.
* Improved policy-group icon handling across themes and profile reloads.
* Improved iOS 26 context menus, previews, and module presentation.
* Virtual IP records and search results now use self-sizing rows.
* Fixed policy groups using an underlying proxy being unavailable from the UI.
* Improved module error reporting for download, parsing, writing, and installation failures.

Networking and Reliability

## 2026-09-01 [post 1741](https://t.me/SurgeTestFlight/1741)

* [Host] domain aliases can specify a dedicated DNS server.
* Updated the IPv6 fake-IP range to avoid unnecessary browser local-network permission prompts.
* Fixed rare crashes when proxy or QUIC connections close synchronously during data processing.
* Fixed recursive HTTP/3 timer processing that could cause a stack overflow.
* Fixed QUIC connections stalling after receive-side backpressure.
* Fixed long-running Ponte and Vector sessions eventually exhausting their ability to open relayed streams.
* Fixed rare deadlocks involving cron-script shutdown and Vector UDP connections.
* Improved stability during heavy connection churn and local-port exhaustion.
* Improved MITM certificate generation and certificate-chain handling.
* Fixed several additional crashes and minor issues.

## 2026-09-01 [post 1740](https://t.me/SurgeTestFlight/1740)

Surge Mac 6.9.0 is Now Available

* MASQUE & HTTP/3 — Added MASQUE proxy support with HTTP/3 CONNECT and CONNECT-UDP, plus HTTP/3 transport for TrustTunnel.
* Tailscale Peer Relay — Added Peer Relay support with Direct → Peer Relay → DERP path selection, plus improved sign-in and connectivity recovery.
* Surge CLI — Significantly expanded the CLI with rule explanations, DNS tracing, HTTP probing, runtime diagnostics, VM Gateway inspection, and more.
* Proxy Chaining — Policy groups can now route their proxy members through an underlying proxy.
* Profile System — #!include can now be freely mixed with inline content, with wildcard includes for Ruleset, WireGuard, and Tailscale sections.
* New Editors — Redesigned major configuration interfaces and added graphical editors for rulesets and Port Forwarding.
* Prometheus Metrics — Added a Prometheus-compatible /metrics endpoint for runtime and traffic monitoring.
* Gateway & Reliability — Improved IPv6 Gateway Mode and reliability across QUIC, DNS, Ponte, Vector, and high-connection-load scenarios.

For the complete release notes, please visit:
https://nssurge.com/support/mac/release-notes https://nssurge.com/support/mac/release-notes

## 2026-08-24 [post 1733](https://t.me/SurgeTestFlight/1733)

Beta Updates

Improved

- Nested rulesets now work reliably: inline rulesets can reference other inline rulesets or external RULE-SET and DOMAIN-SET sources. Circular references are rejected with a clear reference chain instead of causing recursive matching.
- The local ruleset editor now preserves blank lines, standalone and trailing comments, and disabled rules more accurately. Invalid entries report their source file and line number, while comment rows use the same readable presentation as the main rule editor.
- Virtual IP records and search results on iOS now use self-sizing rows, preventing longer domains and usage details from being clipped.

Fixed

- Fixed rules added inside a ruleset or logical rule on iOS incorrectly retaining a hidden policy value when saved.

## 2026-08-20 [post 1730](https://t.me/SurgeTestFlight/1730)

Beta Updates

- Tailscale can now establish peer-relay paths through eligible tailnet devices when a direct connection is unavailable, with Direct > Peer Relay > DERP path priority. Runtime details identify Peer Relay connections and display their latency.
- Local-file and inline rulesets can now be edited graphically on macOS and iOS. Add or modify standard rules, logical rules, nested rulesets, and comments, then reorder or remove entries as needed. Create new inline rulesets directly from the rule editor and store them as named [Ruleset ...] sections in the profile.
- The previously added mixed use of #include will no longer affect UI write-back for the corresponding sections. Surge will automatically select the write-back target as accurately as possible based on the changes.

## 2026-08-18 [post 1727](https://t.me/SurgeTestFlight/1727)

Beta Updates

macOS Interface

- Reworked the proxy editor, policy-group editors, parameter dialogs, and the General, Interface, DNS, Profile, and License pages using a new System Settings-style card interface.

Surge CLI & Remote Control

- Added restart-engine, which completely restarts the engine, closes active connections, and clears caches and temporary rules.
- reload continues to apply only changed profile sections whenever possible, preserving unaffected runtime state.
- Restart Engine is also available from Surge Dashboard and the iOS Remote Controller maintenance menu.

Tailscale

- Improved compatibility with the Tailscale administration console. Surge devices are no longer incorrectly reported as using an outdated client, enabling version-gated operations such as editing the device IP address.

iOS

- Fixed managed-profile icon-url icons being hidden by automatically generated placeholder icons.
- Custom policy-group icons now behave consistently across Lucid and Gradient themes, with a Default option available in both.
- Module download, parsing, file-writing, and installation-information failures are now reported instead of failing silently.
- Refined the Script Editor toolbar and file-selection layout on iOS 26.
- Improved context-menu previews on iOS 26 by following the system’s native corner styling.

## 2026-08-18 [post 1726](https://t.me/SurgeTestFlight/1726)

Profile System Updates

The #include (?q=%23include) directive can now be freely combined with other content within a section. The following usage patterns are supported:

1. Dedicated Include

[Proxy]
#include (?q=%23include) proxy.dconf

When a section consists of a single #include (?q=%23include) directive, it remains fully editable in the UI. Any changes made through the UI will be correctly written back to proxy.dconf.

2. Multiple Includes

[Proxy]
#include (?q=%23include) a.dconf, b.dconf

This combines content from multiple files into a single section. Since the UI cannot determine how changes should be written back to the individual files, the section becomes read-only and cannot be modified through the UI.

3. Mixed Content and Includes (New)

[Rule]
#include (?q=%23include) common-rule-a.dconf
DEST-PORT,123,DIRECT
#include (?q=%23include) common-rule-b.dconf

#include (?q=%23include) directives can now be freely mixed with regular content within the same section. As with multiple includes, the UI cannot determine the appropriate write-back behavior, so the section will be read-only.

Note: When using this feature in the [Rule] section, keep in mind that a FINAL rule immediately terminates rule matching. Any rules included or defined after it will therefore never be evaluated.

## 2026-08-17 [post 1724](https://t.me/SurgeTestFlight/1724)

Beta Updates

Smart Group

- Added a graphical Policy Priority editor for Smart Groups on macOS and iOS.

Tailscale

- Interactive sign-in now supports tailnets that require administrator device approval. Surge clearly indicates when sign-in has completed but the device is still awaiting approval.
- Fixed Tailscale traffic becoming unavailable when the control server assigned the device a new tailnet address.
- Improved recovery after network changes by retrying temporarily failed UDP bindings and refreshing direct-connect endpoints.
- Improved WireGuard and Tailscale handling of multiple peers and expired connections.

Profile and Automation

- On iOS, profile changes made on disk or received through iCloud now reload automatically. If the updated profile is invalid, Surge keeps the working configuration active and reports the error.
- Event scripts can now respond to engine-started and profile-reloaded, in addition to network-changed.

Notifications

- Added notification controls for new proxy clients, script notifications, and rule-matched notifications.
- Local and remote notification category settings now correctly apply to dynamically generated alerts.
- Disabling policy-group change notifications now also suppresses temporary group-override alerts.

Fixed

- Improved MITM certificate generation by using separate keys for generated leaf certificates and correcting the transmitted certificate chain.
- Fixed QUIC connections potentially stalling after receive-side backpressure.
- Fixed rare deadlocks involving cron-script shutdown and Vector UDP connections, including Ponte traffic.
- Improved stability under heavy connection churn and local-port exhaustion.
- Other small UI issues.

## 2026-08-17 [post 1723](https://t.me/SurgeTestFlight/1723)

UniFi Controller Integration (Beta)

When Surge is operating in DHCP mode, Dashboard device management can integrate with the UniFi Controller. You can directly view the corresponding device’s SSID, AP, Wi-Fi version, and other information in Surge’s Dashboard. You can also force a specific device to reconnect.

Meanwhile, this feature is provided entirely by a new, extensible plugin mechanism, allowing plugins to be written to support any AP Controller or router.

This feature is currently in beta, so no UI configuration interface is provided yet. It can only be configured through surge-cli or the AI Skill. After installing the Surge AI Skill, simply ask the AI to help integrate your UniFi AP Controller. Alternatively, ask the AI to write a new plugin based on your router.

Plugin System (Beta)

- Added the Surge Plugin System on macOS. Plugins run as isolated JavaScript extensions independent of the active profile.
- The first supported plugin type is ap-controller, which can supply Wi-Fi information for the device panel and reconnect wireless clients. The existing UniFi Controller integration is now provided as a built-in plugin.

As it is still in the beta phase, the mechanism for installing plugins remotely via plugin install has not yet been enabled. Currently, only loading and running local content via plugin load is supported.

## 2026-08-14 [post 1722](https://t.me/SurgeTestFlight/1722)

Profile System Updates
- Added wildcard detached-section includes for [Ruleset *], [WireGuard *], and [Tailscale *]. A single #!include can now load all matching named sections from another local or remote profile file.
- Added DEVICE_NAME to the profile environment, enabling device-specific conditions in #!REQUIREMENT.
- [Mac] The current Reload Profile option will compare the differences between the old and new profiles and apply only the changes. It will not terminate existing active connections unless necessary. (Same behavior as editing through the UI previously.)
- [Mac] Added a Restart Engine option, which behaves like Reload Profile in the previous version and completely restarts the core once.

## 2026-08-13 [post 1719](https://t.me/SurgeTestFlight/1719)

Beta Updates

### Surge CLI

- Added vmnet status to inspect the VMNET interface configuration, including addresses, prefixes, MTU, and diagnostic table sizes.
- Added vmnet arp to inspect IPv4 neighbors learned from Gateway Mode clients.
- Added vmnet ndp to inspect the IPv6 neighbor table.
- Added vmnet ra to inspect IPv6 Router Advertisement takeover status, including clients, known routers, RA lifetimes, and blacklisted devices.

### macOS

- Added a graphical Port Forwarding editor for creating and managing incoming TCP forwarding rules. Listening address, listening port, destination, and outbound policy can all be configured without editing the profile manually.
- Gateway-related device actions are now hidden when Gateway Mode is unavailable.
- Fixed system proxy settings being applied when using VIF mode without a default route.

### iOS UI

- When navigating to a new page, the bottom tab bar is no longer hidden. This change was made to avoid triggering known UIKit UI glitches that can occur when the tab bar is hidden during push transitions.
- The Script Editor now opens in a dedicated modal interface, with an updated toolbar, close action, and improved keyboard layout.
- Remote Controller and Ponte Diagnostics are now available for all Ponte devices, including devices shared by another iCloud account.
- Other UI improvements.

### Other Improvements

- Updated the IPv6 fake-IP range to avoid unnecessary browser local-network permission prompts, while retaining compatibility with previously cached addresses.
- Proxy connections closed during the protocol handshake now provide a clearer error message, with guidance to verify credentials, encryption methods, and protocol settings.
- Fixed rare crashes that could occur when proxy connections were synchronously closed while data was being written.
- Fixed recursive HTTP/3 timer processing that could cause a stack overflow under certain conditions.

## 2026-08-12 [post 1716](https://t.me/SurgeTestFlight/1716)

DNS Updates

Host rules now support specifying a dedicated DNS server for domain aliases, for example: foo.com http://foo.com/ = bar.com http://bar.com/, server:https://example/dns-query.

## 2026-08-11 [post 1711](https://t.me/SurgeTestFlight/1711)

iOS TestFlight Updates

New Feature: Terminal
You can now operate Surge directly through the CLI on Surge iOS.
- CLI mode includes a comprehensive set of debugging and diagnostic tools for troubleshooting. For example, the rule explain command can be used to inspect how rules are evaluated and how policy groups make their decisions.
- The new virtual Terminal provides a full interactive experience, including command auto-completion and history. For details on available commands, refer to the Surge Manual or simply run help in the Terminal.

Other reasons why you might want to use Surge from the CLI:
- It’s cool. Maybe even cooler when you’re using it on an iPhone Fold later this year.
- Bringing full CLI capabilities to iOS also lays the groundwork for future AI Agent features on Surge iOS.

New Icons: Arctic & Pulse
- The former Surge Enterprise icon now has a new name: Arctic, and is available for everyone to use.
- Added a new icon: Pulse.

## 2026-08-11 [post 1710](https://t.me/SurgeTestFlight/1710)

Surge iOS 更新了系统版本的兼容性：iOS 最低要求是 iOS 16，此前是 iOS 15  iPhone 设备需装有 iOS 16.0 或更高版本。  iPad 设备需装有 iPadOS 16.0 或更高版本。  Mac 需要 macOS 13.0 或更高版本以及装有 Apple M1 或更高版本芯片的 Mac。  Apple TV 设备需装有 Apple tvOS 17.0 或更高版本。  Apple Vision 设备需装有 visionOS 1.0 或更高版本。  说明：iOS < 16.0…

## 2026-08-10 [post 1708](https://t.me/SurgeTestFlight/1708)

Prometheus Metrics Endpoint

Surge now provides a Prometheus-compatible metrics endpoint at GET /v1/metrics, making it easy to integrate Surge with Prometheus and Grafana for long-term monitoring and visualization. This is particularly useful for gateway deployments that run continuously.

The endpoint exposes cumulative traffic counters for each network interface and policy (surgeinterface_bytes_total and surge_policy_bytestotal), which can be combined with PromQL functions such as rate() for real-time throughput or increase() for traffic usage over any time window.

It also provides metrics for the Surge engine’s memory footprint (surgememorybytes), in-flight requests, DNS cache size, active unauthorized-access bans, uptime, and build information. The memory metric can be especially useful on iOS for monitoring Network Extension memory usage over time.

The metrics endpoint uses the same authentication mechanism as the rest of the Surge HTTP API. Since Prometheus does not send custom authentication headers by default, the API key can also be supplied through the x-key query parameter:

scrape_configs:
  - job_name: surge
    metrics_path: /v1/metrics
    params:
      x-key: ["<your-http-api-key>"]
    static_configs:
      - targets: ["192.168.1.1:6171"]

## 2026-08-10 [post 1707](https://t.me/SurgeTestFlight/1707)

Group-Level Proxy Chaining

Surge now supports the group-level underlying-proxy parameter, allowing you to configure a proxy chain for an entire policy group in one place. Every member of the group will connect through the specified policy, including members imported via policy-path, include-all-proxies, and include-other-group.

Chained members are represented as derived policies such as Name (via Relay), each with its own independent latency test result. This means automatic policy groups can select the best node based on its actual performance through the complete proxy chain, rather than the performance of the node alone.

The new option is also fully integrated into the policy group editor UI.

Previously, similar behavior could be achieved with external-policy-modifier="underlying-proxy=...", but that approach only applied to members loaded through policy-path. The new group-level parameter works with members from all sources, provides explicit misconfiguration reporting, and is available as a first-class option in the UI. The existing external-policy-modifier syntax remains supported for backward compatibility.

Please refer to the manual for a detailed comparison and configuration examples:
https://manual.nssurge.com/policy-groups/parameters.html https://manual.nssurge.com/policy-groups/parameters.html

## 2026-08-10 [post 1706](https://t.me/SurgeTestFlight/1706)

Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP for UDP datagrams.
- Added UDP relay support to HTTP/2 CONNECT proxies with udp-relay=true.
- Added HTTP/3 transport support to TrustTunnel with h3=true.

## 2026-08-10 [post 1705](https://t.me/SurgeTestFlight/1705)

New Surge Beta Feed on X
We’ve launched @SurgeBeta, a new X account for detailed updates on the latest Surge Beta releases. It will stay in sync with our existing Telegram Channel.

Follow @SurgeBeta to keep up with the latest Beta changes and improvements.

## 2026-08-10 [post 1704](https://t.me/SurgeTestFlight/1704)

Surge CLI Updates

As Surge CLI becomes a key foundation for integrating AI capabilities with Surge, we are continuing to expand and refine it.

The interactive CLI now supports command history and auto-completion, making it significantly more convenient for both everyday use and exploratory workflows.

We’ve also added a new set of useful commands, including rule match and rule explain, which let Surge answer a common debugging question without generating any real traffic: “Why would this request go through that policy?”

rule match

rule match performs a dry-run evaluation against the active rule set and reports the matched rule and final policy.

All relevant matching attributes — including hostname or URL, port, process path, source address, client MAC, protocol, and more — can be supplied as key=value options. This makes it possible to reproduce exactly how a specific request or client would be routed.

Combined with --raw, it can also be used in scripts to audit an entire list of domains against your current rules.

rule explain

rule explain goes a step further by showing why a particular policy was selected.

It traces the complete policy-group resolution path and reports every decision along the way, including manual selections, automatic test results, overrides, load-balancing decisions, Smart Group selections, the underlying proxy chain, DNS evaluation notes, and timing information.

Use rule match for quick checks and scripting, and rule explain when you need to inspect the complete decision path.

And there’s more coming: starting with the next iOS TestFlight build, Surge CLI will be able to operate Surge directly on iOS. Stay tuned.

## 2026-08-10 [post 1703](https://t.me/SurgeTestFlight/1703)



## 2026-08-09 [post 1698](https://t.me/SurgeTestFlight/1698)

The corresponding iOS version is still awaiting Apple’s review, while the tvOS version has completed review and is now available on the App Store.

## 2026-08-09 [post 1697](https://t.me/SurgeTestFlight/1697)

Surge Mac 6.8.0
Surge Mac 6.8.0 has been officially released. This is one of our most substantial updates yet, combining major new capabilities with extensive improvements throughout the networking stack.

Highlights include:

- Initial adaptation for macOS 27
- Interactive Tailscale sign-in and automatic routing
- MTProto server mode for Telegram
- Built-in Snell v6 server support
- A significantly expanded Surge CLI and new AI Skills
- Reworked ECN handling across QUIC, WireGuard, Tailscale, Ponte, and nested UDP tunnels
- DNS-over-TCP and improved IPv4/IPv6 connection establishment
- UDP-aware Smart Group policy selection
- Major improvements to Gateway Mode, Ponte, profiles, cloud sync, external resources, and diagnostics

The release also delivers wide-ranging security, correctness, and reliability enhancements across core components—covering everything from malformed-data handling and connection recovery to memory usage, concurrency, and long-running stability.

Read the full release notes:  
https://nssurge.com/support/mac/release-notes https://nssurge.com/support/mac/release-notes

## 2026-08-07 [post 1694](https://t.me/SurgeTestFlight/1694)

Snell v6.0.0 RC2
When ipv6=false, return a clearer error message when the client explicitly accesses an IPv6 address.
https://kb.nssurge.com/surge-knowledge-base/release-notes/snell https://kb.nssurge.com/surge-knowledge-base/release-notes/snell

## 2026-08-05 [post 1692](https://t.me/SurgeTestFlight/1692)

Surge Manual Updates

The Surge Manual has undergone a comprehensive review and rewrite.

Every configuration option has been audited against the latest version of Surge. Outdated settings, deprecated behaviors, and obsolete documentation have been removed to ensure the manual accurately reflects the current implementation.

In addition, we’ve expanded the documentation with many new configuration examples, making it easier to understand how different features work and how they can be combined in real-world scenarios.

Highlights
• Comprehensive review and rewrite of the entire manual.
• Audited every configuration option against the latest Surge behavior.
• Removed deprecated settings and obsolete documentation.
• Improved consistency and accuracy throughout the documentation.
• Added many new examples to demonstrate practical configurations.

This update ensures that the manual stays aligned with the current version of Surge and provides a more reliable reference for both new and experienced users.

https://manual.nssurge.com/ https://manual.nssurge.com/

## 2026-08-03 [post 1691](https://t.me/SurgeTestFlight/1691)

Elpass 正式版更新 v2.0.0

AppStore https://apps.apple.com/us/app/elpass/id1488616799

Passkey Support
- Passkeys are now supported.
- Implemented passkey import and export functionality on iOS.

AutoFill Login Save
- Elpass can now automatically save logins through the new API in iOS 26.2.

UI Refresh
- Numerous UI detail optimizations and updates.

#AppStore

## 2026-08-03 [post 1688](https://t.me/SurgeTestFlight/1688)

Surge CLI Updates
https://nssurge.com/blog/surge-cli-updates/ https://nssurge.com/blog/surge-cli-updates/

Surge CLI has been significantly expanded into a comprehensive command-line management and diagnostics interface, with the following new commands:

## New Commands

- Added status to display the active profile and its full path, outbound mode, feature states, uptime, and version information.
- Added version to display Surge, Core, Controller protocol, operating system, and device versions.
- Added dump summary to provide a passive overview of the current network environment, including interfaces, IP addresses, default router, DNS servers, cellular or Wi-Fi information, and configuration warnings.
- Added mode to view or switch between Rule, Direct, and Global Proxy modes.
- Added global-policy to view or change the policy used in Global Proxy mode.
- Added policy-group to list policy groups, inspect their current selections, manually select a policy, or clear an automatic-group override.
- Added profile to list, inspect, validate, and switch profiles. Profile listing and validation are available on macOS.
- Added module to list modules and enable or disable multiple modules in one operation.
- Added feature to inspect and control MitM, Rewrite, Scripting, HTTP Capture, Packet Capture, and Cellular Mode. On macOS, it also supports System Proxy and Enhanced Mode.
- Added device to list Gateway Mode devices or inspect an individual device by identifier or MAC address on macOS.
- Added reconnect-device to reconnect a specified access-point client from the command line on macOS.
- Added script list to display configured scripts and script run to execute a cron script by name, including disabled scripts, while returning its output or exception.
- Added log to retrieve up to 10,000 recent log lines from either the persistent log file or the more detailed in-memory log.
- Added log watch to continuously stream newly generated, unfiltered logs.
- Added logbook to display recent structured Logbook records.
- Added script-log to retrieve the log from a specific script execution.
- Added benchmark encryption to measure the encryption and decryption performance of the device running Surge, with correctness, integrity, and tamper-detection checks.

## Diagnostic Improvements

Existing diagnostic commands have also been improved:

- proxy-runtime-status now provides detailed runtime information for Tailscale and WireGuard, including traffic, recent errors, peer handshakes, DERP connections, Exit Node state, peer paths, and MagicDNS information.
- Query and diagnostic commands now produce structured, human-readable terminal output by default, while --raw remains available for automation.
- Commands that change settings now return the resulting state and properly report failures. System Proxy and Enhanced Mode commands wait for the actual state transition to complete.
- Remote Controller passwords can now be supplied through a secure terminal prompt, SURGE_CLI_PASSWORD, or --password-stdin, avoiding exposure in the process command line.
- Remote connections now support bracketed IPv6 addresses and include timeouts for stalled connections and finite operations.
- Interactive mode now supports quoted arguments and backslash escaping.

## Availability

The above updates apply to Surge Mac 6.8.0, Surge iOS 5.21.0, and Surge tvOS 5.21.0. Please notice surge-cli can operate remote instances via --remote.

The corresponding updates have also been added to the AI Skills documentation. After the update, AI Agents can automatically gain the new capabilities.

## 2026-08-03 [post 1687](https://t.me/SurgeTestFlight/1687)

iPerf - Speed Test Tool 正式版更新 v3.0.0

AppStore https://apps.apple.com/us/app/iperf-speed-test-tool/id951598770 US$1.99

This release introduces a major architecture upgrade for iOS 26:

- Updated the iPerf3 core to version 3.21.
- Migrated iPerf execution to the new ExtensionFoundation framework.
- Isolated test sessions in a separate process for improved stability.
- Fixed a main-thread crash when a test session finished.
- Fixed UITableView update warnings and related UI issues.
- Improved state synchronization for client, server, and test results.
- Removed legacy compatibility code and deprecated dependencies.
- Improved overall code quality, performance, and UI behavior.

This version requires iOS 26 or later.

#AppStore

## 2026-07-27 [post 1678](https://t.me/SurgeTestFlight/1678)

macOS 27 Beta 4 Local Network Issue

A small number of users running macOS 27 Beta 4 have reported that Surge may fail to access services on the local network, returning a “No route to host” error.

After investigation, we have confirmed that this is caused by an issue with the system’s Local Network permission database.

If the problem persists, you can try resetting the Local Network permission database by running: tccutil reset LocalNetwork

or wait for a future macOS beta update, as the issue appears to be a system bug.

## 2026-07-27 [post 1677](https://t.me/SurgeTestFlight/1677)

Surge Ponte Service Notice

Over the past three days, a small number of users have reported that Surge Ponte is unable to access iCloud, resulting in synchronization failures.

After investigation, we have confirmed that this is caused by a server-side issue with Apple’s CloudKit service rather than Surge itself. The issue has been reported to Apple and can only be resolved by Apple. If you are affected, please allow Apple a few days to resolve the issue.

Most affected users are using iCloud China (operated by GCBD), although we have also received a small number of reports from users on the international iCloud service.

To reduce our dependency on a single cloud provider, we have also started designing a general Bring Your Own Storage (BYOS) mechanism. Once available, users will be able to use their preferred cloud storage service for both configuration synchronization and Surge Ponte data synchronization.

We will share more details as development progresses.

## 2026-07-23 [post 1674](https://t.me/SurgeTestFlight/1674)

More Details About the Tailscale Update

* The new version will automatically add the user’s MagicDNS domain as a highest-priority DOMAIN-SUFFIX rule, such as DOMAIN-SUFFIX,tail123456.ts.net. Therefore, when using MagicDNS for access, there is no need to manually configure the rule.

* Surge’s default policy for Tailscale is to start on demand. If there are no active requests for 600 seconds, it will automatically disconnect to avoid unnecessary resource consumption. If you want to stay continuously online like the official client and avoid additional waiting during initialization, you can configure idle-keepalive = -1.

## 2026-07-23 [post 1672](https://t.me/SurgeTestFlight/1672)

New Feature: Surge as MTProto Server

Surge now can operate as an incoming MTProto proxy server for Telegram. 

Please read manual for more information: https://manual.nssurge.com/ https://manual.nssurge.com/

TL;DR
Using MTProto instead of SOCKS or VIF to take over Telegram can:

1. Telegram has a notorious SOCKS5 bug in which it can put an IPv6 destination address into an IPv4 request. The malformed destination causes a large number of invalid connection attempts to be sent to Surge. MTProto avoids this path entirely.

2. Force connections to Telegram servers over IPv6. Telegram’s IPv4 servers have a bug that can easily cause the connection to hang without responding. IPv6 nodes do not have this issue, and MTProto allows the intermediary proxy to determine the specific DC service address. Therefore, setting ipv6=true can resolve this persistent problem. (The proxy server must support IPv6 forwarding.)

## 2026-07-21 [post 1668](https://t.me/SurgeTestFlight/1668)

TLS

- Fixed a potential crash caused by reentrant TLS cleanup while pending BIO data was being flushed, particularly with nested TLS connections.

DNS

- Local DNS mappings can now specify multiple upstream DNS servers using a comma-separated list. (Fixed the issue where the previous version did not take effect correctly.)

SSH

- Strengthened server host-key verification when server-fingerprint is configured. A one-time security warning is now emitted when connecting without a configured fingerprint.
- Fixed compatibility with fragmented identification banners, pre-banner lines, small channel windows, non-ASCII credentials, and modern RSA/SHA-2 authentication.
- Added complete bidirectional rekey support and corrected key-switching, deferred channel operations, and connection cleanup during rekey.
- Added strict validation and size limits for transport packets, key-exchange fields, signatures, channel parameters, and cryptographic values.
- Fixed channel read/write timeouts, completion reporting, malformed-key handling, and several memory and resource leaks.

HTTP & HTTP/3

- Added strict and consistent parsing for request and response headers, Content-Length, Transfer-Encoding, chunked coding, trailers, request targets, and status-specific body semantics.
- Ambiguous or malformed framing, including conflicting Content-Length and Transfer-Encoding values, is now rejected consistently.
- Fixed HTTP/1.1 pipelining boundaries so request bodies are forwarded strictly according to their declared length.
- Improved HTTP/2 request and response rewriting, including correct handling of empty header values, UTF-8 header lengths, forbidden connection-specific fields, and decoded bodies processed by scripts.
- Added input and buffering limits to protocol detection, the HTTP controller, JSVM server endpoints, script body processing, proxy responses, and HTTP/3 full-response tasks such as DoH3.
- Improved HTTP/3 stream reset, connection close, callback completion, and shutdown behavior to prevent stalled requests and reentrant teardown.
- Improved handling of HEAD, 204, 205, and 304 responses and made script/rewrite header mutations transactional to prevent inconsistent wire framing.

Policy Selection

- Fixed potential crashes and inconsistent routing decisions when policy lookups occurred concurrently with a configuration reload.
- Improved Smart Group concurrency handling and fixed site history or runtime data potentially being lost during configuration updates.
- Fixed an issue where the “most used” policy score could become incorrect after an extended idle period.
- Fixed several rule-evaluation paths that could stall indefinitely, reuse a canceled evaluation, or produce results from an outdated configuration.
- Added safeguards against unexpected policy-group reference loops.
- Fixed URL-Test groups ignoring an explicitly configured tolerance=0.

Surge Ponte

- Added strict validation for device PSKs and encrypted payloads, preventing invalid or damaged iCloud device records from causing a crash.
- Improved dual-stack connection handling: if one IPv4 or IPv6 connector fails during setup, Ponte can continue using the remaining connector.
- Fixed IPv6 server channels failing to recover automatically when a previously unavailable network interface becomes available.
- Failed channels no longer publish stale external addresses to other devices.
- Serialized CloudKit device-record updates to prevent duplicated, lost, or conflicting updates.
- Fixed legacy configuration migration and several server startup edge cases involving duplicate direct channels and unavailable STUN addresses.

TCP Connection Establishment

- Fixed an unreachable cached “previously successful” address preventing fallback to other available addresses after a network change.
- Improved connection-attempt error handling so every attempt reaches a definite success or failure state.
- Corrected TCP connection statistics collection for sockets that never completed establishment.

Connection Management

- Fixed memory growth and journal performance degradation on long-lived multiplexed connections such as SSH, Hysteria, TUIC, Vector, and HTTP/2.
- Fixed a race where an idle master connection could close immediately after being assigned to a new request.
- Improved connector abort handling to ensure cleanup and policy failure reporting occur only once.
- Fixed TCP packet-loss statistics not being collected during common disconnection paths.
- Improved thread safety when recording recent proxy errors and accessing connector state across queues.
- When a local DNS mapping contains multiple candidates, one result is now used consistently throughout a logical connection while still allowing a new result after connector reuse or configuration updates.
- Connector pools now remove empty entries and stop unnecessary maintenance timers.
- Fixed underlying proxy groups resolving to DIRECT taking an unnecessary intermediate connector path.
- Improved general connection cleanup and error propagation across HTTP, HTTP/3, TLS, and internal HTTP clients.

UDP Reliability

- Improved synchronization of local address and destination state across socket queues.
- UDP receive backpressure now takes effect immediately instead of continuing to deliver additional batches after reads are paused.
- Moved large batched receive buffers off the worker-thread stack, reducing the risk of stack exhaustion under heavy UDP traffic.
- Fixed UDP packets with IPv6 scope differences being incorrectly rejected on metadata-enabled send paths.

Network Testing & Diagnostics

- Fixed proxy tests continuing to run or remaining permanently marked as active when canceled before deferred startup completed.
- UDP tests now reliably report invalid parameters, timeouts, cancellation, and connector failures to every caller.
- Added a 64 KB response-header limit to URL tests.
- Fixed Direct diagnostics incorrectly reporting a failed connection as a successful 0ms result.
- Improved ICMP parsing for IPv4 responses containing IP options.
- Throughput tests now wait for all concurrent tasks before producing the final result.
- Upload throughput tests now use genuinely independent concurrent connections, including with HTTP/1 servers.
- Improved Ponte diagnostics concurrency and completion handling.

Other Improvements

- Fix the operational issue with drag-and-drop sorting of policy groups.
- Fixed a Surge Dashboard crash on macOS 27 that could occur when opening a remote connection immediately after closing a window containing the system text-completion interface.
- Fixed a potential macOS crash when presenting a modal sheet while the system text-completion interface was active.

Please refer to the Mac version Beta Release Note: https://nssurge.com/support/mac/release-notes?beta=1 https://nssurge.com/support/mac/release-notes?beta=1

Official Channel: @SurgeTestFlightFeed

## 2026-07-21 [post 1665](https://t.me/SurgeTestFlight/1665)

Snell v6.0.0 RC1
Fix the issue where the first few UDP packets may be truncated when forwarding starts.
https://kb.nssurge.com/surge-knowledge-base/release-notes/snell https://kb.nssurge.com/surge-knowledge-base/release-notes/snell

## 2026-07-10 [post 1650](https://t.me/SurgeTestFlight/1650)

Tailscale Engine Rewrite

In previous beta versions, Surge’s Tailscale implementation was based on the official experimental tailscale-rs library. Because its feature set and performance did not fully meet Surge’s requirements, this release replaces that integration with a new proprietary implementation built directly into Surge’s networking engine. The new implementation provides broader functionality, significantly better performance, and richer runtime diagnostics.

1. Direct peer-to-peer connectivity, including NAT traversal and path discovery, is now supported. Surge automatically prefers a direct connection when available and falls back to DERP when necessary. The new derp-only option can be used to force all peer traffic through DERP.

2. Single-threaded data-plane throughput has been significantly improved, reaching up to approximately 1.5 Gbps in our lab tests—comparable to the official Tailscale client under the same test conditions.

3. Exit node support has been added. A Tailscale policy can now route Surge-selected traffic through a configured exit node and can therefore be used as a regular outbound policy. This affects only traffic assigned to that policy by Surge and does not change the device-wide default route.

4. Routes advertised by authorized Tailscale subnet routers are now supported. MagicDNS is now better supported.

5. Surge now uses Tailscale-aware latency testing. When exit node isn't configured, Surge performs a native Tailscale connectivity probe against an online peer. If no suitable peer is available, the home DERP server is tested instead. When exit node or test-url is configured, the standard HTTP test process is used. Additional initialization time is allowed for control-plane setup and the initial WireGuard handshake.

6. Extensive Tailscale runtime diagnostics have been added to the UI, including control connection state, assigned addresses, exit node status, DERP regions, direct-versus-relay peer paths, peer latency, active connections, endpoints, and MagicDNS information.

7. Existing Tailscale profiles and persisted node identities remain compatible; no profile migration is required.

We plan to add inbound access over WireGuard and Tailscale in a future version, allowing remote devices to connect to Surge and use it as a network gateway.

Notice: Due to the core engine replacement, Tailscale needs to be registered again. If you did not previously enable the reuse option for the auth key, you must generate a new auth key to complete the new device registration process.

Please check the manual for more information: https://manual.nssurge.com/policy/tailscale.html https://manual.nssurge.com/policy/tailscale.html

## 2026-07-07 [post 1645](https://t.me/SurgeTestFlight/1645)

Abort Assert Log

Surge includes a number of assert checks in its code. Assert checks are a common development and debugging mechanism used to detect situations where the program reaches a state that is different from what the developers expected.

Seeing an assert message does not necessarily mean that Surge has crashed or other issues. In many cases, the app can continue working normally, and the assert simply serves as a signal for the developers to review that part of the code.

When an assert is triggered, Surge may automatically save certain temporary logs that were previously held in memory into a log file. This is done to help developers understand what happened before the assert was triggered. This behavior is expected and should not be interpreted as abnormal memory usage or a memory leak.

Assert triggers may be seen more often in beta versions, because beta builds are designed to help identify and diagnose potential issues before a stable release. 

If Surge continues to work normally, the message can usually be ignored. If you notice repeated crashes, broken functionality, or other reproducible problems together with this message, please report the issue with the relevant logs so we can investigate further

## 2026-06-24 [post 1626](https://t.me/SurgeTestFlight/1626)

Licensing System Update

You can now deactivate an inactive device directly from the license management page on the Surge website for both Surge Mac and Surge iOS, without performing a full license reset.

* A device is considered inactive if it has not connected to the internet for more than 72 hours.
* Each license may perform this inactive-device deactivation operation once every 7 days.
* Regular device deactivation is not affected by this limitation.

## 2026-06-15 [post 1606](https://t.me/SurgeTestFlight/1606)

Snell 6.0 beta 2

Snell v6 beta 3 has added a mode setting. 
1. mode=default Default mode, enables traffic obfuscation and AES encryption.
2. mode=unshaped Disables obfuscation and uses only AES encryption. Compared with the default mode, throughput performance can be improved by about 10%. This mode is equivalent to Snell v3, where the encrypted traffic appears completely random.
3. unsafe-raw Disables encryption and obfuscation, forwarding all traffic in plaintext. It should only be used in secure network environments, such as an intranet or under another secure tunnel.

Please note that the server mode and client mode must be consistent.

## 2026-06-12 [post 1603](https://t.me/SurgeTestFlight/1603)

Snell 6.0 beta 2

* Fixed an issue where performance unexpectedly dropped significantly
* Fixed an issue with external dynamic dependency libraries

Please note that this version adjusts the protocol profile, so Surge Mac also needs to be updated to the latest version.

## 2026-06-11 [post 1601](https://t.me/SurgeTestFlight/1601)

Snell v6 Beta

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

## 2026-06-05 [post 1597](https://t.me/SurgeTestFlight/1597)

Surge Mac Beta 6.7.0 now supports Tailscale as a proxy policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

## 2026-06-01 [post 1590](https://t.me/SurgeTestFlight/1590)

A Brief Update on Surge

The Surge team has recently gone through several internal changes, and we would like to share a few updates with our users.

Support Operations

We have expanded our support operations by adding dedicated customer support staff and technical specialists.

This allows us to respond to inquiries more efficiently while keeping our engineering team focused on product development.

Communication Channels

We are currently reorganizing our external communication channels.

As part of this effort, we have launched a new official blog to share technical details about Surge and insights from our development process.

SOC 2 Alignment

We have begun aligning our internal processes with SOC 2 requirements.

This work reflects our continued investment in improving operational maturity, security practices, and overall reliability. It is especially relevant for enterprise customers with strict security and compliance expectations.

Product Development

We know many users are most interested in what’s next for Surge.

Since the official release of Surge Mac v6 on July 1, 2025, we have shipped 428 beta builds, 14 stable releases, and nearly one hundred improvements and optimizations in less than a year. The full release history is available in our release notes: https://nssurge.com/support/mac/release-notes https://nssurge.com/support/mac/release-notes.

At the same time, we are actively working on Tailscale integration. While we are not ready to provide a formal ETA, we expect an early beta to be available soon.

As always, our focus remains on shipping features only when they meet the standards of quality and system-level integration that users expect from Surge.

Thank you for your continued support and patience. More updates will be shared as work progresses.

https://nssurge.com/blog/a-brief-update-on-surge/ https://nssurge.com/blog/a-brief-update-on-surge/

## 2026-05-25 [post 1578](https://t.me/SurgeTestFlight/1578)

Surge Mac Tips
由于现在很多应用程序包内存在多个二进制文件，因此传统 PROCESS-NAME 规则配置需要多条才能完全匹配。
自 Surge Mac 6.0 版本开始，PROCESS-NAME 规则的用法就已经扩展，当以 / 结尾时将进行前缀匹配，如 PROCESS-NAME,/Applications/ChatGPT.app/ 可匹配 ChatGPT.app http://ChatGPT.app/ 应用包内所有二进制。
详见：https://manual.nssurge.com/rule/process.html https://manual.nssurge.com/rule/process.html

## 2026-05-25 [post 1576](https://t.me/SurgeTestFlight/1576)

Surge iOS & Mac Beta 版本更新日志
• Surge Mac 版本现在可以通过 UI 编辑策略组图标，同时除了 URL 图标，也可以使用 Emoji、Surge 内置图标库和 SF Symbols。
• 策略组图标现在直接写入配置。
• iOS 版本的图标配置存储逻辑调整，现在在配置文件可编辑的情况下，将优先写入配置，以保证和 Mac 版本互通。仅当配置为只读配置时，使用独立的 UI 配置文件存储。

## 2026-05-18 [post 1565](https://t.me/SurgeTestFlight/1565)

Surge iOS & Mac Beta 版本更新日志
- HTTP/2 CONNECT 和 TrustTunnel 代理现在支持 multiplex，由于过多子链接复用同一个 TCP 连接，可能产生性能问题，因此默认只允许最多 3 个子连接，可通过配置策略参数 max-streams 调整。

## 2026-05-15 [post 1563](https://t.me/SurgeTestFlight/1563)

关于部分历史协议维护状态的调整

以下历史协议后续将进入维护冻结状态：

* AEAD 版本之前的旧版 Shadowsocks
* TUIC v4
* VMess

相关协议的核心代码和兼容能力仍会保留，现有配置不会受到影响；但后续版本中，对应的 UI 配置入口将逐步移除。

## 2026-05-15 [post 1560](https://t.me/SurgeTestFlight/1560)

Surge iOS & Mac Beta 版本更新日志

- 新增 HTTP/2 CONNECT 代理支持，可通过 h2-connect 类型配置基于 HTTP/2 的 CONNECT 代理连接。
- HTTP, HTTPS, HTTP/2 CONNECT, TrustTunnel 代理现支持自定义请求头，可在代理配置中使用 headers= 添加额外 header，例如：

Proxy = http, example.com, 8080, headers=X-Client:Surge;X-Token:abc
Proxy = h2-connect, example.com, 443, headers=X-Padding:<random-string(16-32)>

自定义 header 支持 <random-string(n)> 与 <random-string(min-max)> 占位符，连接时会自动生成 URL-safe 随机字符串，适用于需要动态 padding 或请求特征扰动的场景。

## 2026-05-15 [post 1559](https://t.me/SurgeTestFlight/1559)

关于 Surge iOS 功能更新订阅机制的调整

自 Surge iOS 推出功能更新订阅机制以来，我们一直希望在「持续演进产品能力」与「保障长期使用体验」之间保持合理的平衡。经过评估，我们决定进行如下调整：

1. 未来新增的所有代理协议兼容支持，将不再纳入功能更新订阅范围，所有用户均可直接使用。
2. 现已实验性支持的 TrustTunnel，也不会存在订阅限制，可以直接使用。

我们认为，协议兼容性应当作为长期稳定提供的基础能力，而不是阶段性的增量功能。这意味着，未来用户无需因为订阅状态，而担心基础协议支持的可用性；新的协议兼容能力也能够更直接、更持续地向所有用户开放。

调整后，订阅更新将更聚焦于新的高级功能，而协议兼容性本身，则会作为产品的长期基础能力持续维护。

与此同时，代理协议生态本身也始终处于持续变化之中。一些协议会不断演进，也有一些协议会逐渐退出主流使用场景。为了保证 Surge 长期稳定的代码库维护与整体产品质量，我们也会结合实际使用情况，对部分历史协议进入维护冻结状态，或在未来逐步结束支持。

我们会尽可能谨慎地处理相关调整，并提前进行说明，以减少对现有用户配置与使用体验的影响。

感谢大家一直以来的支持与反馈。

## 2026-05-10 [post 1556](https://t.me/SurgeTestFlight/1556)

关于 Surge 用户交流群的说明

近期，我们多次收到与部分 Surge 用户交流群相关的邮件，包括请求协助处理群内争议、解除封禁等事项。对此，我们希望再次说明：

* 各平台上的 Surge 用户交流群均由用户自发创建和维护，Surge 团队从未参与其管理，也不具备任何控制权。

* 部分交流群中的热心用户会整理社区反馈，并转达给我们参考。这是我们了解用户意见和建议的渠道之一。但除此之外，Surge 团队与相关交流群不存在其他合作或管理关系，群内用户及管理员的言论也不代表 Surge 团队立场。

* Surge 官方讨论社区为：https://community.nssurge.com/ https://community.nssurge.com/ 。该社区仅用于技术相关的讨论与交流。该 Telegram 频道则为唯一官方公告渠道。

感谢各位的理解。

## 2026-05-06 [post 1549](https://t.me/SurgeTestFlight/1549)

Surge iOS 5.18.0 版本已提交 App Store 审核，更新日志：

新的订阅功能：Logbook 日志簿，用于持久化记录发生的各种事件，
- 目前包含引擎启动和停止、网络切换、脚本启动和停止、脚本超时等事件
- 日志簿为脚本调试进行了特别优化，可以轻松查看脚本的输入、输出和日志。同时，脚本可以使用 $surge.logbook("content") 主动写入内容到日志本
- Surge Mac 的 Surge Dashboard 可读取远程 Surge 实例的日志簿内容，包含脚本的运行细节均可以远程直接访问

其他改进
- 为所有 TLS 相关功能（如代理协议，MITM，DoH/DoT/DoH3）新增对 X25519MLKEM768 后量子混合密钥交换组的支持
- 优化 $persistentStore 管理页面，新增搜索、导入导出、全部删除等操作
- 重构 QUIC 协议的内存管理，解决在特定情况下，QUIC-based 协议可能出现突发内存占用过高导致 Surge 被系统停止的问题
- 修正使用 Trust Tunnel 时出现的内存泄露问题
- 修正极低概率下出现的一个崩溃问题
- 修正开启 HTTP API TLS 时，API 请求可能卡住的问题
- 修正 UI 上的一些细节问题

## 2026-04-28 [post 1541](https://t.me/SurgeTestFlight/1541)

脚本远程调试功能得到了进一步强化

## 2026-04-27 [post 1537](https://t.me/SurgeTestFlight/1537)

Surge iOS/macOS Beta 更新日志
Logbook 日志簿功能现已在 Surge Mac 和 iOS 版本中加入，Logbook 用于持久化的记录事件，在 Surge 关闭后也不会丢失。（现在版本默认只保留最近 7 的事件）

- Surge Dashboard 支持读取远程实例的 Logbook 内容，同时支持查阅脚本类型记录的输入输出，以及日志输出。对端可以是 Surge iOS 或 Mac，所有内容均支持远程载入。
- Mac 版本已加入配置重载、网络切换、崩溃恢复、更新、DHCP 相关的 Logbook 写入。更多日志信息将在更新中持续加入。

## 2026-04-17 [post 1524](https://t.me/SurgeTestFlight/1524)

已完成订阅展期

## 2026-04-17 [post 1523](https://t.me/SurgeTestFlight/1523)

使用提示
Surge Mac 6.5.0 新增了对 `compatibility-mode = 5`，非 default 路由的工作方式的支持。用于解决特定的兼容性问题（如 HomeKit Camera）。

该模式下由于 Surge VPN Interface 并非首选 Interface，因此不会修改系统的默认 DNS，但是会通过 Split DNS 机制进行 DNS 劫持。不过该机制仅对 GUI 程序有效，对 CLI 和部分 GUI 程序无效。

如果希望在该模式下依然完整劫持 DNS，请先将首选的 Interface（如 WiFi）的 DNS 修改为任意公网地址（不可使用 LAN 地址），同时再配置 hijack-dns 参数进行劫持即可。

## 2026-04-16 [post 1522](https://t.me/SurgeTestFlight/1522)

Telegram 客户端已内置“简体中文”和“繁体中文”语言

更改语言： 
   * Settings → Language → Chinese
   * 设置 → 语言 → 中文

Telegram 官方客户端和第三方客户端均已热更新👍

• Telegram 知识库
   * Telegram 知识库: https://t.me/tgcnz/954
   * Telegram 知识库: https://t.me/tgcnxz/51
   * Telegram 知识库: https://t.me/tgcnx/6390526

• 谨防盗号！谨防盗号！谨防盗号！
   * 谨防盗号
   * 谨防盗号
   * 谨防盗号

#TG (?q=%23TG) #Telegram (?q=%23Telegram) #电报 (?q=%23%E7%94%B5%E6%8A%A5)

✅️ 群组 @tgcnx
✅️ 频道 @tgcnz

## 2026-04-16 [post 1519](https://t.me/SurgeTestFlight/1519)

关于 Surge iOS 版本的功能订阅更新

我们了解到部分用户对近期 Surge iOS 的订阅功能更新不够频繁表示失望，因此对该问题进行说明和解决。

Surge iOS 自发布起已超过了十年，我们曾经的很多想法都已经被一个个的实现，因此，对于现在 Surge iOS 来说，想出一个新的功能并不容易。同时，为了保证用户体验，一些小型的新功能，也不会放入到订阅限制中。

对于我们的研发精力来说，其实有大量的精力放在了原有功能的改进与优化上，比如说最近更新加入的 X25519 + ML-KEM-768 后量子（混合）密钥交换支持，就要求我们从原本的 OpenSSL 实现切换至 BoringSSL，这涉及到大量的重构和测试。或是像去年跟随 Surge Mac v6 同步更新的最新 Surge VIF 引擎实现。这些都耗费了我们大量的研发精力，但是并没有纳入到订阅更新点中。

当然，由于 Surge iOS 的功能订阅，同时具备时间维度上向前与向后的延伸，我们充分理解连续订阅用户关于订阅功能点更新不够频繁的失望。因此我们建议所有用户取消自动续订开关，仅在 Surge iOS 提供了你所需要的新功能时，再进行订阅，这也是我们推出该订阅模式的初衷。即使不进行订阅，你依然可以免费享受到改进型更新，只需要为有需求的功能付费。

同时，由于我们研发人员的精力分配和开发进度的关系，我们也很难保证订阅更新的功能点可以稳定地推出，有时可能一个月就会有两个新功能，有时可能长时间都没有。因此我们现在推出一项改进，如果 Surge iOS 连续 90 天都没有推出新功能，那么在这期间存在订阅期的用户，订阅期将自动延期 90 天。

（举例来说，目前上一次订阅功能更新日是 2025 年 12 月 11 日，假如授权有效期是到 2026 年 2 月 1 日，那么订阅将自动被延期到 2026 年 5 月 1 日。）

我们将在未来数日更新授权系统进行展期，感谢您的支持和理解。

## 2026-04-14 [post 1516](https://t.me/SurgeTestFlight/1516)

关于 VLESS 协议的说明

我们长期收到用户关于支持 VLESS 代理协议的请求。鉴于围绕该协议存在较多争议，我们过去倾向于避免公开回应，以免引发不必要的讨论与争端。然而，持续的沉默本身也被部分解读为一种态度，甚至产生了一些误解与猜测。基于这一现实情况，我们决定对相关问题进行一次正式说明。

（由于 vless / vision / xtls 等名称本身缺乏统一且明确的定义，下文将以「VLESS」作为整个协议族的统称。）

加密代理协议社区始终保持着高度活跃。从早期的 Shadowsocks，到后来的 Trojan、ShadowTLS、TUIC、Hysteria、AnyTLS 等项目，不同开发者持续提出新的设计思路，并在开放讨论与相互借鉴中推动技术演进。许多项目均由开发者无偿投入时间与精力完成，对整个生态产生了积极影响。

因此，当新的项目具备成熟度与稳定性时，我们通常乐于进行支持与适配。尽管 Surge 本身并未直接参与开源代理协议项目，但我们与部分协议作者保持着良好的私下沟通，也会就实现细节与 issue 进行技术层面的交流。我们对此一直保持开放性态度。

然而对于 VLESS 协议，由于其设计改变了传统 TLS 的分层边界。若要实现支持，需要对上游 TLS 库（如 OpenSSL/BoringSSL）进行定制化修改，这意味着后续无法直接跟随上游更新，增加整体 TLS 子系统的复杂性与安全评估成本。

此外，XTLS 将 TLS 从传统的端到端数据保护层重新定位为一种会话引导机制，把原本由标准协议层提供的完整性保障，部分转移到应用自行定义的数据路径之上。这种跨层设计虽然带来了某些特性，但降低了安全边界的可验证性。

相比之下，Trojan、TUIC、Hysteria、TrustTunnel 等协议均建立在标准 TLS 实现之上。标准化 TLS 经过长期实践验证，是目前应用最广泛且成熟度最高的加密隧道。

事实上，针对用户的需求，我们早已完成了一份 VLESS 协议的实验性实现。然而，代码的完成并不代表产品的就绪。正如前文所述，由于该协议目前需对底层 TLS 库进行非标准修改。如果现在将其合并进主分支，意味着我们要把巨大的维护风险和潜在的不稳定性带给所有 Surge 用户，这不符合我们对产品稳定性的要求。

除此之外，VLESS 协议的特性更新非常频繁，缺乏稳定且可依赖的文档和 specification，我们对这种探索性精神表示支持，但对于产品化来说，这种频繁的变动和复杂的参数配置，将对用户体验带来巨大的挑战。

所以我们依然在观察支持 VLESS 协议的必要性，如果最终确实被广泛采纳使用，或者产生了比其他 TLS 类协议的明显优势，或者有了完整的协议 specification，我们会第一时间重新评估合并事宜。

为了避免产生更多的误解和猜疑，我们在此承诺，如果未来 Surge iOS 版本决定加入 VLESS 协议支持，将作为一项免费更新推出，所有用户均可直接使用。以此表明我们绝非因为商业原因而故意延后支持。（Surge Mac 版本用户可以通过 External Proxy Program 机制进行使用）

希望您可以理解我们的决定，我们对造成的不便感到歉意。

## 2026-03-20 [post 1502](https://t.me/SurgeTestFlight/1502)

Surge Mac Beta 更新日志
现在已支持像 iOS 版本一样为策略组配置一个图标。需手动配置 icon-url 字段。目前没有 UI 设置页面。

## 2026-03-17 [post 1499](https://t.me/SurgeTestFlight/1499)



## 2026-03-17 [post 1498](https://t.me/SurgeTestFlight/1498)

Surge Mac Beta 更新日志
• Surge 现已完全支持 AI agent 的技能操作。我们已内置了如何使用 surge-cli 操作 Surge 的说明，并已完全开放 surge-cli 的全部能力。请将以下内容告知支持技能的 agent 以便使用：

安装 /Applications/Surge.app/Contents/Resources/Skills/ 目录中的 skill，使用符号链接进行安装，以确保该技能可随应用程序包一同更新。

• Skill 已完成对 codex 的 metadata 适配
• 目前 skil 中尚未包含关于配置修改的能力

## 2026-03-10 [post 1491](https://t.me/SurgeTestFlight/1491)

关于带宽测试功能失效与 Surge Mac 维护更新订阅制的说明

Surge Mac 在 2025 年 10 月 5 日的一次更新中，加入了一项便捷功能，允许用户直接测试代理的带宽。由于当时该功能还处于初级阶段，我们直接 hardcode 了 Cloudflare 的测试地址作为测试节点。

2026 年 2 月开始，由于 Cloudflare 测试 URL 不再允许外部访问，导致 Surge 的带宽测试功能突然失效。为此我们发布了新的 Surge Mac 版本，更换了测试地址并完善了相关逻辑，加入了更全面的测试设置，同时也允许用户自定义测试地址，以彻底避免类似问题再次发生。

由于 Surge Mac 采用维护更新订阅制，如果用户的维护期正好在 1 月底前结束，将无法获取到新版本，从而面临功能突然失效的困扰。我们对受此影响的用户表示诚挚的歉意，也完全理解大家因此产生的愤怒与不满。

关于维护更新订阅制

我们想借此机会解释一下，Surge Mac 版本使用的是“维护更新订阅制”。在 Mac 生态中，这并非 Surge 首创，而是目前很常见的一种授权模式（如 DEVONthink、Sketch、TablePlus 等知名软件均采用此模式）。

我们认为在这种订阅模式下，能较好地平衡开发者与用户的需求。所有软件都需要持续维护，无论是适配新版 macOS 系统，还是跟进外部服务依赖的变化，都需要开发者投入精力，才能保证各项功能的长期正常运转，这正是维护更新订阅的核心意义。同时，用户也可以根据自己的实际需求决定是否续费。

此次测速功能失效，属于该模式下可能遇到的一种极端情况。通常情况下，收到 Bug 报告后我们都会尽快在更新中修复；如果是严重 Bug，我们也会主动调整版本的解锁期，以确保不影响旧版用户的使用。

解决方案与致歉

由于 iOS App Store 的机制限制，Surge iOS 采用的是“功能解锁订阅制”，并承诺所有已解锁功能终身维护。部分双端用户可能并不完全了解两者的区别，误以为 Mac 版本也与 iOS 版本一样享有单一功能的终身维护。

在近期的客服沟通中，我们的工作人员过多地着重于向用户解释“功能订阅”与“维护订阅”的区别，而未能充分照顾到用户面对功能突然失效时的焦躁感受与实际情况，从而引发了更多不满，对此我们深表歉意。

为了妥善解决该问题，我们现已将当前的 Surge Mac 正式版本（6.4.4）的解锁时间调整为 2025 年 10 月 5 日，以保证所有受到该问题影响的用户都可以直接获取更新。

同时，我们也会吸取此次教训，在未来的开发中尽量降低对外部单点服务的依赖，并提供更多可自定义的参数，避免重蹈覆辙。

感谢大家一直以来的理解与支持。

## 2026-03-10 [post 1490](https://t.me/SurgeTestFlight/1490)

Surge iOS 5.17.1 已提交 App Store 审核，汇总更新日志：

新增
- 实验性支持 Trust Tunnel 协议
- 新增用于配置文件切换的 Intent；你现在可以在“快捷指令”中直接切换当前 Surge 配置文件
- 在 Ponte 页面新增“调试信息”开关；启用后，在 Ponte 连接过程中将显示详细的连接状态信息
- 支持直接引用托管的配置文件，而无需先将托管配置文件添加为本地配置文件（即 macOS 上的“关联配置文件”功能）
- 企业/团队 license 现在可用于 tvOS 版本

改进
- 吞吐量测试的所有参数现在都可自定义
- 新增一个变通方案，用于解决较新 iOS 版本上的一个问题：长脚本运行一段时间后，setTimeout 会因系统的资源节省机制被限流，最多每 2 秒只能触发一次
- Policy 组不再校验子 policy 名称的有效性。如果引用的子 policy 不存在，运行时会自动隐藏不存在的选项。include-other-group 参数也做了类似调整。注意：在 [Rule] 中使用不存在的 policy 仍会触发配置文件的严重错误提示。

修复
- 修复 AnyTLS 与部分服务器之间的兼容性问题（启用 reuse 时，如果前一次请求失败，后续请求可能会卡住）
- 修复在使用 QUIC 类型协议或 h3 DNS 时偶发的崩溃问题
- 修复只有小卡片视图才能显示“更新外部资源”菜单项的问题

## 2026-03-01 [post 1480](https://t.me/SurgeTestFlight/1480)



## 2026-02-26 [post 1477](https://t.me/SurgeTestFlight/1477)

由于此项改动涉及的细节问题较多，与部分用户的习惯相冲突，我们在新版本中撤销此项改动。

同时，在新版本中，策略组不再校验子策略名的有效性，如果引用的子策略不存在，那么将在运行时自动隐去不存在的选项。include-other-group 参数也同样进行了修改。

不过请注意，在 [Rule] 中使用不存在策略，依然会触发硬性配置错误提示。

## 2026-02-25 [post 1471](https://t.me/SurgeTestFlight/1471)

请注意，配置文件 [Proxy] 和 [Proxy Group] 中以 # 开头的注释，由于该特性，可能因为各种原因导致配置检查报错。请将注释开头改为 ## 来绕过该问题。

我们还在对该功能进行梳理以自动避免这些检查问题

## 2026-02-25 [post 1470](https://t.me/SurgeTestFlight/1470)

最新的 Surge Mac 加入了一项实验性改动，现在 [Proxy] 和 [Proxy Group] 段，支持使用 # 注释整行将一个项目标记为未启动了。

相比原本直接注释掉不生效，被禁用掉的策略不会触发配置检查的错误。先前版本在其他规则、策略组中引用了一个不存在的策略，会直接导致 Surge 无法启动。

禁用掉的策略，如果是被其他策略组使用，或者以 include-other-group 或 include-all-proxies 被引用，则不会出现在该组的可选项中。

如果使用规则或其他方式直接使用了被禁用的策略，那该策略将会被 SUBSTITUTE 策略（DIRECT 策略的别名）取代。

## 2026-02-21 [post 1464](https://t.me/SurgeTestFlight/1464)

吞吐量测试的各项参数，现在可以自定义了，也支持提供模块写入

[Testing]
download-url = 
upload-url =
download-url-proxy = // 未提供时使用 download-url
upload-url-proxy = // 未提供时使用 upload-url
download-concurrency = // 默认为 4
upload-concurrency = // 默认为 4
download-duration-limit = // 默认为 10 秒
upload-size-limit = // 默认为 1GB
upload-duration-limit =  // 默认为 10 秒

## 2026-01-27 [post 1459](https://t.me/SurgeTestFlight/1459)

Build 10450 Trust Tunnel 存在严重的上传卡住问题，Build 10460 已修正。

## 2026-01-27 [post 1458](https://t.me/SurgeTestFlight/1458)

Surge Mac 更新日志
试验性支持 Trust Tunnel 代理协议，该协议是由 AdGuard 所开发并维护的代理协议。（虽然项目中宣传 Trust Tunnel 是一种 VPN 协议，然而其实际上是一种代理协议。）
- 该协议基于 TLS，因此所有 TLS 参数均可配置使用
- 目前仅支持基于 HTTP/2(TCP) 的工作模式
- 尚未完成 UDP 转发支持。

配置样例：`proxy = trust-tunnel, 192.168.20.62 http://192.168.20.62/, 443, username=test, password=test`

## 2026-01-21 [post 1449](https://t.me/SurgeTestFlight/1449)

Surge 官方服务（beta）已上线，目前可用于检查 Surge 配置是否合法，API 节点为：

[POST] https://services.nssurge.com/v1/config/validate

使用方法：可直接 POST 整个配置文件，也可以在 Content-Type: application/json 时，使用 JSON 字段 profile 传入配置内容。
返回结果为 JSON，字段 valid 表示配置是否合法，当配置不合法时，`error` 字段将给出错误的描述。

处于用户隐私安全考虑，该 API 没有配置任何日志系统，所有上传的内容均不会被保存。如果还是担心隐私问题，可在使用前将配置中的服务器地址、用户名密码等敏感字段，先进行脱敏化处理替换，再进行验证。

## 2026-01-20 [post 1447](https://t.me/SurgeTestFlight/1447)

我们已完成官方的 llms.txt，用于给 AI Agent 提供全面的 Surge 文档和知识库数据：https://nssurge.com/llms.txt https://nssurge.com/llms.txt

通过引用该文件，可以让 AI 更准确地回答 Surge 配置的相关问题。

## 2026-01-13 [post 1438](https://t.me/SurgeTestFlight/1438)

Surge Mac 更新日志
可以使用 surge-cli -c profile.conf 命令来验证配置文件有效性了

## 2026-01-12 [post 1436](https://t.me/SurgeTestFlight/1436)

Surge Mac/iOS Beta 更新日志
• 所有代理协议的 QUIC block 行为，现在均默认调整为阻止。
即使通过基于 UDP 的协议对 QUIC 流量进行转发，由于 QUIC 的流量控制机制对中间节点不可见，代理服务器无法像转发 TCP 流量那样引入额外的中间缓冲区。在链路质量不佳的情况下，其整体稳定性往往明显弱于基于 TCP 的协议。
因此，放行 QUIC 流量可能导致显著的使用体验下降，仅建议具有明确需求的用户手动启用。

## 2026-01-08 [post 1428](https://t.me/SurgeTestFlight/1428)

Surge iOS 2025 订阅功能更新回顾

* 2025-02-26: DNS over TLS
* 2025-06-30: Snell v5
* 2025-09-05: 主动探测
* 2025-12-11: AnyTLS(v2)

Official Channel: @SurgeTestFlightFeed

## 2026-01-08 [post 1427](https://t.me/SurgeTestFlight/1427)

Surge iOS 2024 订阅功能更新回顾

* 2024-03-12: Always Capture
* 2024-03-16: Body Rewrite
* 2024-05-07: 规则分析
* 2024-07-02: 自定义策略组图标
* 2024-10-15: Shadowsocks2022
* 2024-10-18: Pre-matching
* 2024-10-24: 支持 JQ 表达式
* 2024-12-21: 端口转发 Port Forwarding

Official Channel: @SurgeTestFlightFeed

## 2026-01-02 [post 1418](https://t.me/SurgeTestFlight/1418)

Surge Mac Beta 更新日志
按住 Option 键点击 Surge 主菜单时，现在会显示隐藏的策略组。

## 2025-12-17 [post 1395](https://t.me/SurgeTestFlight/1395)

Dashboard 改进：现在 IP 地址请求可以按照 AS 分组查看了

## 2025-12-16 [post 1393](https://t.me/SurgeTestFlight/1393)

DNS 映射新增 force-syslib 关键字
  - 原 system 和 syslib 关键字效果完全一致，在未开启增强模式时，将调用系统库进行解析，在开启增强模式时，将使用系统的 DNS 服务器，由 Surge 进行解析。
  - 使用 force-syslib 关键字时，无论是否开启了增强模式，均由系统库进行解析。请注意这可能导致循环请求问题，该选项是为了 mDNS 等特殊域名所设计，请勿为一般域名配置该参数。（无需为 .local 域名配置，已经默认包含特别处理）

## 2025-12-11 [post 1380](https://t.me/SurgeTestFlight/1380)

iOS TF 版本也已经加入支持

## 2025-12-11 [post 1378](https://t.me/SurgeTestFlight/1378)

UDP 支持已在 Build 9860 中完成

## 2025-12-11 [post 1374](https://t.me/SurgeTestFlight/1374)

Surge Mac Beta 更新
兼容代理协议 AnyTLS(v2)
- 已完全实现 AnyTLS 的 padding scheme，支持服务端动态更新
- 已完全实现 AnyTLS 的 reuse 机制，根据 AnyTLS spec 要求，reuse 默认开启，可以使用 reuse=false 关闭
- 暂未完成 UDP 转发支持

## 2025-11-21 [post 1360](https://t.me/SurgeTestFlight/1360)

最近发现某次 Steam 更新后，由 Surge 接管的 Steam 下载时可能会卡住，经过排查发现，是因为 Fake IP 机制和 lancache.steamcontent.com http://lancache.steamcontent.com/ 产生冲突所致。增加配置 always-real-ip = lancache.steamcontent.com http://lancache.steamcontent.com/ 即可解决。

我们已将该配置加入 HTTP Download Optimization 官方模块，重启 Surge、进入模块页面、或者等待一段时间后，均可自动完成更新。
（可以双击官方模块，查看模块的具体配置内容）

## 2025-11-20 [post 1359](https://t.me/SurgeTestFlight/1359)

知识库新增 UDP Fast Path 的 Technote：https://kb.nssurge.com/surge-knowledge-base/zh/technotes/udp-fast-path https://kb.nssurge.com/surge-knowledge-base/zh/technotes/udp-fast-path

## 2025-11-19 [post 1357](https://t.me/SurgeTestFlight/1357)

Snell v5.0.1
- 修正了一处因断言低概率出现的崩溃问题

https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-armv7l.zip

## 2025-10-23 [post 1310](https://t.me/SurgeTestFlight/1310)

Surge 十岁了 🎉

2015 年 10 月 23 日，Surge iOS 1.0 正式上架 App Store。光阴荏苒，Surge 已经走过整整十年。

这十年的发展离不开广大用户的支持与喜爱，在此向所有用户致以最诚挚的感谢。

我们最近正在重新梳理 Surge 的功能逻辑与文案介绍。值此十周年之际，也借此机会回顾一下 Surge 这十年的发展历程。

⸻

[首创] 规则分流系统

2015 年，Surge 首次设计并实现了代理分流规则系统（包括 DOMAIN、DOMAIN-SUFFIX 等规则，以及策略与策略组）。
该系统依托于完整的 HTTP 代理服务器与用户态 TCP 栈实现。当时业界尚无类似方案，主流仍是基于路由表或浏览器 PAC 的原始分流方式。
如今，这套设计已成为事实上的行业标准。

⸻

[首创] 增强模式

Surge 1.0 仅具备 HTTP/HTTPS 代理功能，无法接管未设置代理的 App 网络请求。
在 2.0 版本中，我们基于 Fake IP 与 用户态 TCP 协议栈 实现了增强模式（Surge VIF），从而能够强制接管所有网络流量。
这一机制如今也成为同类软件的标配方案。

⸻

MITM、HTTP 捕获与 Rewrite

Surge 首次在代理软件中引入了 HTTP 捕获 和 Rewrite 等修改功能，以满足开发者的轻度调试需求。
在这一阶段，我们曾考虑进一步强化开发者工具属性，但出于性能与稳定性的权衡，最终决定将其定位为轻量级调试辅助功能。

⸻

[首创] 脚本处理引擎

在原有的 HTTP 修改功能基础上，Surge 首次集成了 JavaScript 执行引擎。
用户可以通过脚本对 HTTP 请求与响应进行灵活修改，大幅提升了可扩展性与社区创造力。

⸻

[首创] 模块系统

Surge 首创了 模块（Module） 概念，使用户可以将部分配置独立出来单独控制开关，或分享至社区供他人使用。
这一设计极大地提升了配置的可复用性与协作性。

⸻

[首创] Surge DHCP

Surge Mac 的增强模式支持以旁路由模式接管局域网内其他设备的网络流量。
在此基础上，我们进一步集成了 DHCP Server，让用户仅需几次点击即可完成接管配置。

⸻

[首创] Surge Ponte

Surge Ponte 是目前最为易用的内网穿透方案之一。
用户只需简单配置，即可实现所有 Surge 客户端间的组网。整个系统无需中心节点，且实现了端到端强加密。
在今年的 Ponte 2.0 升级中，我们进一步引入了多通路自动选择与灾备切换等企业级高可用特性。

⸻

[首创 & 独占] Smart Group

在 Surge 1.0 中，我们首次实现了 url-test 策略组，将代理线路选择从手动操作变成自动化过程。
然而，传统 url-test 机制在线路故障时存在重测试延迟，也无法实现线路与目标的精准匹配。
因此我们重新设计了 Smart 策略组，由自主研发的算法引擎驱动，实现真正的零感知动态切换。
用户几乎无需手动干预，即可享受始终稳定的连接体验。

⸻

[首创 & 独占] Surge Gateway VM

由于增强模式依赖系统 utun 机制，其性能与灵活性受到一定限制。
在 Surge Mac 6 中，我们推出了 Gateway VM，以二层网络设备的方式直接接入 LAN。
该架构不仅显著提升了性能，也为更多高级功能奠定了基础。

这一特性虽然不易被用户直接感知，但实际上 Surge 已经实现了完整的 ARP、IPv6 NDP、NAT 等子系统。
Surge 的网络协议栈复杂度如今已与操作系统内核网络栈相当。

⸻

[首创 & 独占] IPv6 Override

这是基于 Gateway VM 的第一个衍生功能。
Surge 实现了对 IPv6 网络的非侵入式独立接管，并与 DHCP 功能整合，让用户可以一键接管局域网内的所有 IPv6 设备。

⸻

[首创 & 独占] UDP Fast Path

这是 Gateway VM 的第二个衍生功能。
在传统四层旁路由或透明代理场景中，P2P 流量的高连接数常导致性能瓶颈，一般只能靠路由表等方式强行绕过。
Surge 通过实现 UDP Fast Path，可智能地将 P2P 流量下沉至三层处理，从而避免此问题。

⸻

性能优化：对极致的不懈追求

性能一直是我们最为关注的方向。过去十年间，我们投入了大量时间与精力，在各个层面持续优化 Surge 的性能，只为让它在真实使用中表现得更快、更稳、更强。

例如，在去年的版本中，我们引入了规则预编译引擎，使得在处理海量规则集时，匹配性能实现了数量级的提升。
而在今年的 Surge Mac 6 中，我们对 userspace TCP 协议栈进行了彻底重构，使用纯 C 实现了全链路 zero-copy，大幅提升了最大吞吐量表现。

因此，无论是在规则匹配效率、连接延迟、吞吐量还是 PPS等关键指标上，Surge 始终保持在同类软件的最优水平。

还有许多原创功能未能一一列出。在下一个十年，我们将继续探索并实现更多有趣且有意义的网络技术。

我们深知，Surge 无法满足所有用户的全部需求。在功能取舍之间，或许难免有所遗憾。对此，我们也真诚地表示歉意。

## 2025-10-14 [post 1286](https://t.me/SurgeTestFlight/1286)

Build 8970 已完成 IPv6 的 UDP Fast Path 支持，现在 IPv6 UDP 也可以经由 NAT66 完成 Fast path 处理

## 2025-10-10 [post 1278](https://t.me/SurgeTestFlight/1278)

Surge Mac 6.4.0 更新：Surge VM UDP Fast Path

目前当使用 Surge 网关模式接管设备时，如果在设备上使用 P2P 类应用（如 BT 下载、游戏安装器、观看直播等），可能导致 Dashboard 中出现大量连接，拖慢整体速度，如果连接数极高甚至可能导致系统资源耗尽 Surge 被迫重启。

产生这个问题的原因是，Surge 是工作在四层的代理，对于每一个四元对不相同的 UDP 数据包，均需要按照是一个新连接的方式进行处理。对于一般应用来说，即使使用 UDP 也一般只会产生几个逻辑上的连接，所以开销完全可以接受。但是对于 P2P 应用，可能在数秒内就产生近千个逻辑连接。

因此在该版本加入了 UDP Fast Path 防御机制，当某个客户端在短时间内发出了大量的 UDP 连接时（1s 内 10 个或者 10s 内 30 个），则对该客户端启用 UDP Fast Path，降至 L3 处理 UDP 数据包。该模式下性能极高，远超物理网卡速度上限，不必再担心资源消耗问题。

另外：
1. UDP Fast Path 下的数据包将被直接转发，无法经过代理。
2. 对于目标端口号小于 1024 的 UDP 包，将始终按照一般的处理模式转发，以避免影响正常应用。
3. 该功能必须配合 Surge Gateway VM 使用

## 2025-09-26 [post 1259](https://t.me/SurgeTestFlight/1259)

下载测试改为了并发 4 线程

## 2025-09-26 [post 1257](https://t.me/SurgeTestFlight/1257)

将在下个版本同步至 Surge iOS

## 2025-09-26 [post 1256](https://t.me/SurgeTestFlight/1256)

Surge Mac Beta 的代理诊断工具新增上传与下载带宽测试功能，可直接测试代理策略的带宽。

## 2025-09-22 [post 1253](https://t.me/SurgeTestFlight/1253)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2025-09-17 [post 1244](https://t.me/SurgeTestFlight/1244)

Surge iOS 更新了系统版本的兼容性：iOS 最低要求是 iOS 16，此前是 iOS 15

iPhone
设备需装有 iOS 16.0 或更高版本。

iPad
设备需装有 iPadOS 16.0 或更高版本。

Mac
需要 macOS 13.0 或更高版本以及装有 Apple M1 或更高版本芯片的 Mac。

Apple TV
设备需装有 Apple tvOS 17.0 或更高版本。

Apple Vision
设备需装有 visionOS 1.0 或更高版本。

说明：iOS < 16.0 的系统可以继续使用旧版，不影响旧版本的使用，只是不能更新新版了。而且卸载也能重新安装，AppStore 会自动下载兼容的版本，不影响卸载重装。

#兼容性 (?q=%23%E5%85%BC%E5%AE%B9%E6%80%A7)

Official Channel: @SurgeTestFlightFeed

## 2025-09-16 [post 1241](https://t.me/SurgeTestFlight/1241)

已适配 iOS 26 UI 的新版本 Surge iOS 5.16.0，由于近期 App Store 审核工作量较大，依然在排队等待审核中。

## 2025-08-16 [post 1217](https://t.me/SurgeTestFlight/1217)



## 2025-08-13 [post 1210](https://t.me/SurgeTestFlight/1210)

知识库新增关于 IPv6 RA Override 的 technotes：https://kb.nssurge.com/surge-knowledge-base/zh/technotes/ipv6-ra https://kb.nssurge.com/surge-knowledge-base/zh/technotes/ipv6-ra

## 2025-08-12 [post 1207](https://t.me/SurgeTestFlight/1207)

beta 6 已经修正了该问题

## 2025-08-06 [post 1200](https://t.me/SurgeTestFlight/1200)

用户报告的 workaround：再建立 VPN Profile 时，先临时关闭锁屏密码，即可绕过问题。

## 2025-08-06 [post 1198](https://t.me/SurgeTestFlight/1198)

iOS 26 Beta 5 警告
接到用户报告，在 beta 5 下无法创建 Surge 的 VPN Profile，经过确认为 iOS 系统问题，目前暂无 workaround 方案。
因此请 beta 5 避免操作删除 Surge 或 Surge 的 VPN profile，将导致 Surge 无法开启，只能降级至先前的 beta 完成配置后再重新升级。

## 2025-07-29 [post 1172](https://t.me/SurgeTestFlight/1172)

Surge Mac 6.2.0 Beta 更新说明：
核心改进
- 策略的 interface 参数现在可以对 DNS 查询也生效了，命中该策略的请求的 DNS 将使用该 interface 进行查询。（如果在规则匹配阶段就触发了 DNS，则不会使用特定 interface）
- 网络质量检测子系统重写，使用了更完备的检查逻辑，在网络不稳定时不再频繁触发通知。

Ponte 服务端升级
- 可选开启灾备模式，当 Surge 检查到主网络 interface 不可用一段时间后，会自动将 Ponte 切换至另一个 interface（如 5G USB 网卡、多 WAN 等场景），同时保证 iCloud 临时使用该 interface 进行请求以完成新地址宣告。
- IPv6 可配置生效的 interface，或者对所有 interface 开启，适合拥有多 WAN 的场景。
- 支持跨网段的内网连接，如多个 VLAN。

## 2025-07-24 [post 1164](https://t.me/SurgeTestFlight/1164)

知识库新增了两篇指南：
- Surge 故障排除指南：https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/troubleshooting https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/troubleshooting
- Surge Mac 网关模式配置指南：https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/gateway https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/gateway

Surge Ponte 在下个版本还会进行一次重要更新，知识库文章将在下一次再同步更新

## 2025-07-24 [post 1162](https://t.me/SurgeTestFlight/1162)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2025-07-22 [post 1147](https://t.me/SurgeTestFlight/1147)

Surge Mac 6.1 Beta
- 新增规则类型 `MAC-ADDRESS`，用于直接使用 MAC 地址匹配特定的客户端。
- [MITM] 的 client-source-address 参数现在支持指定 MAC 地址，以解决客户端 IPv6 请求地址变化的问题。

## 2025-07-21 [post 1140](https://t.me/SurgeTestFlight/1140)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2025-07-18 [post 1128](https://t.me/SurgeTestFlight/1128)

请注意，Surge Gateway VM 模式无法于 Wi-Fi 网络上使用。Wi-Fi 下请使用传统的增强模式接管。

## 2025-07-18 [post 1123](https://t.me/SurgeTestFlight/1123)

我们发现在发布 Surge Mac 5.10.4 版本时，关于 macOS 26 菜单文字颜色的一个修正被意外回滚了，现已更新 5.10.5 beta 版本重新修正该问题。

## 2025-07-18 [post 1121](https://t.me/SurgeTestFlight/1121)

提示：今日是 Surge Mac 早鸟八折活动的最后一天

## 2025-07-18 [post 1119](https://t.me/SurgeTestFlight/1119)

Surge Mac 6.1 Beta
Surge Gateway VM 和 DHCP 功能已经解除绑定，现在可以在不开启 DHCP 的情况下开启 Gateway VM。同时网关模式的配置页面也已经重做，现在可以直接修改配置。

## 2025-07-13 [post 1100](https://t.me/SurgeTestFlight/1100)

Snell 5.0 beta 3 版本已经作为正式版本发布，URL 更新为：
https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v5.0.0-linux-armv7l.zip

## 2025-07-13 [post 1098](https://t.me/SurgeTestFlight/1098)

关于 Surge Mac 6.0 的 IPv6 RA Override 兼容性问题
使用 IPv6 RA Override 功能，需要保证路由器的 IPv6 RA 广播的 DNS 地址，不为 fe80::/10 的 link-local 地址，也不可以为路由器自身的 IPv6 地址。 绝大多数路由可以自定义 IPv6 RA DNS 地址，将其置空或者修改为任意公网 DNS 即可。少数路由不支持修改，已知不兼容的路由为：
- ASUS 全系（可通过更换 Merlin/OpenWRT 固件解决）

## 2025-07-13 [post 1097](https://t.me/SurgeTestFlight/1097)

Mac v5 正式版用户现已可以通过自动更新升级到 v6，由于处理 bug 比原计划延误了几天，早鸟优惠结束日推迟到 7 月 18 日。

## 2025-07-11 [post 1086](https://t.me/SurgeTestFlight/1086)

Mac v5 beta 版本用户现已可以通过自动更新升级到 6.0.1

## 2025-07-09 [post 1078](https://t.me/SurgeTestFlight/1078)

Surge Mac 6.0 现已正式发布：https://dl.nssurge.com/mac/v6/Surge-latest.zip https://dl.nssurge.com/mac/v6/Surge-latest.zip
- 8 折早鸟优惠截止日期确认为 7 月 16 日。
- 配置兼容的 Surge iOS & tvOS 版本将于今日提交更新审核。
- 将在明日向 Surge Mac v5 beta 用户推送 v6 更新，一周后向所有 v5 用户推送更新

## 2025-07-08 [post 1071](https://t.me/SurgeTestFlight/1071)

Surge Mac 6.0 Build 7200 为 6.0 正式版 RC1，如果没有再发现问题，将在明日作为正式版本发布。

## 2025-07-07 [post 1054](https://t.me/SurgeTestFlight/1054)

Snell 5.0 更新到 beta3，对于 libsystemd 的依赖修改为动态依赖，避免在旧发行版无法运行的问题
https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b3-linux-armv7l.zip

## 2025-07-06 [post 1045](https://t.me/SurgeTestFlight/1045)

Snell 5.0 beta 2 已发布，修正上个版本在 QUIC Mode 下可能出现的几处崩溃：
https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v5.0.0b2-linux-armv7l.zip

## 2025-07-04 [post 1024](https://t.me/SurgeTestFlight/1024)

Surge Mac 6.0 现已进入 RC 阶段，如果还有遇到问题，请反馈至 support@nssurge.com

## 2025-07-01 [post 999](https://t.me/SurgeTestFlight/999)

我们也完成了 Snell v5 的性能表现测试（包含 QUIC 模式），Snell 同样享有最优性能保证。包含 Surge 在内，上述保证同时包含吞吐量和延迟两大指标。

## 2025-07-01 [post 998](https://t.me/SurgeTestFlight/998)

这是 Surge 各版本在 M4 Mac Mini 上的测试结果

## 2025-07-01 [post 997](https://t.me/SurgeTestFlight/997)

最优性能保证

Surge Mac 6.0 中的一项重要更新为 VIF 性能优化，我们已经完成对几乎所有同类型软件的性能测试，确认在同等条件下，Surge VIF 的性能在各项指标上均具有明显优势，最高可达 45 倍差距。

为避免引起不必要的争议，我们不方便公布具体测试结果。但是所有测试结果均可自行测试复现获得。

我们发现有些测试报告中，因为操作错误实则对比的是在流量未经任何软件处理情况下的吞吐量。iperf3 测试必须通过 fake IP 访问方可使得流量被接管，部分软件由于默认未开启 fake IP 导致测试流量根本不会被接管处理。（即 iperf3 打印的目标 IP 不可是 127.0.0.1）

为了打消用户的疑虑，我们在此做出最优性能保证，如果在购买 Surge 后，发现 Surge 性能指标在同等条件下劣于其他软件，在购买 30 天内都可以以此申请全额退款。

## 2025-07-01 [post 1003](https://t.me/SurgeTestFlight/1003)

有部分 Surge Mac 更新订阅尚未到期的用户，希望可以提前续费以享受 Early Brid 优惠。现已调整了订阅系统限制，现在过期时间在一年以内，都可以进行续费。

## 2025-07-01 [post 1000](https://t.me/SurgeTestFlight/1000)

我们在进行数据迁移时，意外导致最近两天开始测试 Surge Mac 用户的测试期被取消，如果需要继续试用请联系 support@nssurge.com 进行处理。

## 2025-06-30 [post 977](https://t.me/SurgeTestFlight/977)

iOS 版本存在严重问题，现已撤回，正在修复中

## 2025-06-30 [post 975](https://t.me/SurgeTestFlight/975)

Surge Mac v6 版本现已正式开始测试，下载链接：https://dl.nssurge.com/mac/v6/Surge-6.0.0-6500-31cec2279a8d3bb1795bad95d1412e46.zip https://dl.nssurge.com/mac/v6/Surge-6.0.0-6500-31cec2279a8d3bb1795bad95d1412e46.zip

文档说明已更新 Snell v5 版本，相应的 Surge iOS 版本已在 TestFlight 发布。

## 2025-06-27 [post 962](https://t.me/SurgeTestFlight/962)

Surge Mac 6.0 目前已经完成了开发，正在最后的测试阶段。预计 7 月 1 日可以正式开始测试。

从 6.0 开始，Surge Mac 转为目前 macOS App 中最常见的更新订阅制，详情请参考：https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6。2024 https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6%E3%80%822024 年 7 月 1 日后购买 Surge Mac 5 的用户均可免费获得本次更新。

6.0 版本包含了众多更新内容，发布日志请参考：https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note

## 2025-06-10 [post 960](https://t.me/SurgeTestFlight/960)

macOS 26 beta 1 中 Dark Mode 下菜单文字颜色错误问题已修正

## 2025-06-10 [post 957](https://t.me/SurgeTestFlight/957)

已发布 Surge iOS 26 UI 体验版，不建议其他 iOS 版本用户使用。仅初步适配了 iOS 26 UI 风格，还存在诸多问题，仅供体验，无需进行 bug 回报。

## 2025-06-10 [post 956](https://t.me/SurgeTestFlight/956)

同样问题也影响了 Surge Mac 在 macOS 26 beta 1 的使用，5.10.4 beta 版本已经发布

## 2025-06-10 [post 955](https://t.me/SurgeTestFlight/955)

已发布

## 2025-06-10 [post 953](https://t.me/SurgeTestFlight/953)

已确认 Surge iOS 的 ShadowTLS 在 iOS 26 beta 1 中会出现崩溃，我们将尽快发出 TF 修正版本，如有急需请先禁用相关功能。

## 2025-05-22 [post 952](https://t.me/SurgeTestFlight/952)

Surge iOS & Mac Beta 更新说明

我们已经开始 Surge Mac 6.0 的开发，所以这段时间将不会有 Mac 与 iOS 版本的测试版本，请谅解。

另外，在 6.0 发布日期前一年内，购买 Surge Mac v5 的用户均可免费升级至 v6.0，具体细节将在之后给出。

## 2025-04-30 [post 935](https://t.me/SurgeTestFlight/935)

#!name=Github 429
#!desc=解除 Github 429 限制

[Header Rewrite]
http-request (raw|gist).githubusercontent.com http://githubusercontent.com/ header-replace Accept-Language en-us

[MITM]
hostname = %APPEND% raw.githubusercontent.com http://raw.githubusercontent.com/,gist.githubusercontent.com http://gist.githubusercontent.com/

## 2025-04-23 [post 927](https://t.me/SurgeTestFlight/927)

在最新的 iOS 版本中，为 Surge 的托管配置、外部资源和模块 HTTP 请求，新增了 X-Surge-Unlocked-Features 字段，用于服务器判定 Surge 已解锁的功能以区分返回结果，如：

Surge-Unlocked-Features: proxy-chain, wireguard, ssh, encrypted-dns, body-rewrite, smart-group, load-balance, vmess, trojan, snell-v4, egress-control, response-header-rewrite, doh, shadow-tls-v3, tuic-v5, hysteria, ecn, ss-2022, rule-pre-matching, body-rewrite-jq, port-forwarding, dot

## 2025-04-02 [post 908](https://t.me/SurgeTestFlight/908)

Apple TestFlight 系统故障，iOS 版本暂时无法推送更新

## 2025-04-02 [post 907](https://t.me/SurgeTestFlight/907)

Surge iOS & Mac 更新日志

新增 [General] 参数 `block-quic`，该参数用于全局覆盖是否阻止 QUIC 流量的行为，可设置为

- per-policy`：由策略的 `block-quic 参数决定，默认值，即当前版本的行为。
- all-proxy`：覆盖代理策略的 `block-quic 参数，全部阻止
- all`：覆盖所有策略的 `block-quic 参数，全部阻止，包括 DIRECT 策略
- always-allow`：覆盖代理策略的 `block-quic 参数，全部允许

## 2025-03-18 [post 893](https://t.me/SurgeTestFlight/893)

Technotes 新增对 NAT 类型的讲解：https://kb.nssurge.com/surge-knowledge-base/zh/technotes/nat-type https://kb.nssurge.com/surge-knowledge-base/zh/technotes/nat-type

## 2025-02-28 [post 884](https://t.me/SurgeTestFlight/884)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2025-02-26 [post 878](https://t.me/SurgeTestFlight/878)

关于加密 DNS 的选择
由于部分用户的需求，Surge 最近版本中加入了对 DNS over TLS 的支持，至此 Surge 已完成对所有标准 DNS 协议的支持。

（除了 DNS over TCP，其本质就是 DNS over TLS 的加密前明文，但是测试中发现大多数服务商的 DNS over TCP 都存在严重问题，不具备实用性，故未开放配置）

根据用户反馈和实际测试发现，tls://223.5.5.5 服务端未实现并发查询，使用时可能会出现严重卡顿，不推荐使用。tls://1.12.12.12、tls://8.8.8.8、tls://1.1.1.1 http://1.1.1.1/ 均完整支持并发查询。

具体对比目前支持的所有加密 DNS 协议：
- DNS over HTTP3 和 DNS over QUIC 的表现几乎完全一致，但是由于协议较新，服务端支持经常出现各种问题。且由于基于 UDP 但并非 53 端口，有可能遭遇 QoS 问题。
- DNS over HTTP3/QUIC 在理论上比 DoH 有一点点微弱的优势（丢包时仅影响对应的 stream），但实践中很难体现。
- DNS over HTTPS 比 DNS over TLS 在请求构造和解析上存在微弱优势，但是对于现代计算设备来说完全可以忽略不计。
- DNS over HTTPS 的使用目前最为广泛，服务端兼容性与稳定性高。

综上所述，DNS over HTTPS 是最优选择。不过如果不存在 ISP 污染，依然推荐使用非加密的传统 DNS，以获得最佳性能。

## 2025-02-26 [post 872](https://t.me/SurgeTestFlight/872)

Surge iOS & Mac 更新日志
- DNS over TLS 支持，配置样例 dot://223.5.5.5
- [Mac] 优化通过 Dashboard 新建规则的各种细节

## 2025-02-21 [post 865](https://t.me/SurgeTestFlight/865)

Surge Mac 更新日志
- Surge Dashboard 现在可以远程操作目标 Surge 实例的临时规则了。

## 2025-02-19 [post 856](https://t.me/SurgeTestFlight/856)

Surge iOS & Mac 更新日志
- 优化正则匹配的性能表现
- 修正在触发脚本时，HTTP Request Body 有可能未能被正确捕获保存的问题

## 2025-02-18 [post 852](https://t.me/SurgeTestFlight/852)

Surge iOS & Mac 更新日志
- 现在在开启 HTTP 捕获开关时，将强制打断所有活跃连接，以确保不会因为已存在的长链接导致错过请求。
- 优化与部分 QUIC 客户端的兼容性，如飞书。
- 修正当使用脚本或其他机制修改请求 HTTP 后，统计中的下载数据计量有误的问题。
- 调整了关于 QUIC 转发时处理逻辑的优先级，现在对于一个不支持 UDP 转发的代理策略，将优先考虑 QUIC Block，再考虑回退至 DIRECT 或 REJECT。
- [Mac] 修正绑定出口 interface 时无法使用 utun 设备的问题
- [Mac] 修正 Ponte Server 失败重试时可能不断产生重复的通知的问题
- [Mac] 修复了在特定网络下，Surge Ponte 转发的某一个请求可能被卡住的问题。

## 2025-01-17 [post 837](https://t.me/SurgeTestFlight/837)

Surge Mac Beta 更新日志
我们在先前的版本中将 STUN 服务器更换为了 stun.cloudflare.com，最近的测试中意外发现，该服务器并未完整实现 Surge 检测 NAT 类型所需要的命令，导致 Surge Ponte 配置时，会将所有网络类型报告为 Full Cone NAT (A)。
新版本修正了该问题，如果更新后发现 Ponte 报告 NAT 类型错误无法启动，说明当前网络确实不是 A 类，无法使用直接穿透模式。

## 2025-01-16 [post 831](https://t.me/SurgeTestFlight/831)

Surge Mac & iOS Beta 更新日志

[Host] 段支持使用 DOMAIN-SET 和 RULE-SET 进行配置以提高匹配效率。用例：

[Host]
DOMAIN-SET:https://example.com/domains.txt = https://223.5.5.5/dns-query
RULE-SET:https://example.com/rules.txt = https://223.5.5.5/dns-query

该功能仅为一些特别的需求所设计，绝大部分用户不需要考虑 DNS 区分解析，详见：https://kb.nssurge.com/surge-knowledge-base/zh/technotes/dns https://kb.nssurge.com/surge-knowledge-base/zh/technotes/dns

## 2025-01-16 [post 827](https://t.me/SurgeTestFlight/827)

用例：
DOMAIN,reject.com http://reject.com/,REJECT #!MACOS-ONLY

## 2025-01-16 [post 826](https://t.me/SurgeTestFlight/826)

配置行尾注释 #!REQUIREMENT 升级
- 现在提供 #!IOS-ONLY, #!MACOS-ONLY, #!TVOS-ONLY 三个简单写法
- 被该行尾注释禁用的内容，可以正常在 UI 显示和编辑了，在不满足条件时会显示为禁用状态，若开启将自动移除限制

## 2024-12-25 [post 801](https://t.me/SurgeTestFlight/801)

Surge Mac Beta 更新日志
新增选项 icmp-forwarding，默认开启
在开启增强模式时，为了降低对用户的干扰，Surge 会对所有 ICMP 数据包进行直接转发，这样不影响用户使用 ping 等工具。
但是这可能导致部分极端追求隐私保护的用户产生 IP 泄露，因此新增 icmp-forwarding 选项，可用于关闭该行为。

## 2024-12-25 [post 800](https://t.me/SurgeTestFlight/800)

关于 DNS 泄露

我们之前已经科普过 IP 泄露相关知识，近期又收到很多关于 “DNS 泄露” 与 “DNS ECS” 的问题。由于 “DNS 泄露” 在业界并没有一个统一且严格的定义，这里先归纳出两种常见情形，并分别说明其成因和应对措施：

所谓 DNS 泄露可以指：

1. 指的是在使用传统明文 DNS 时，链路中的运营商、防火墙、公共 Wi-Fi 提供者等都可能直接截获或监视你的 DNS 查询数据包，得知你访问的网站域名。

解决方法：
- 使用加密的 DNS 服务器（如 DoH）
- 使用全局代理模式，或者优先匹配的代理规则，使得不在本地进行 DNS 解析即可。

虽然理论上存在风险，然而实践中由于现在 app 存在大量网络请求，同时云服务器交叠复用，除非涉及的网站域名十分小众，否则也很难从 DNS 请求记录中获得有效信息。

2. 指的是访问的目标网站或者使用的 App自身通过技术手段，检测访问者的真实 IP。

具体技术原理是，构造一个随机的二级域名，通过 DNS 查询中的 ECS 机制，获取到查询者的 IP 地址，以此突破访问者的代理保护获得其实际 IP 地址。

但是，这种检测方法存在诸多不确定性，即使成功，也只能获取到用户的区域，而非真实 IP。

解决方法：
- 使用全局代理模式，或者优先匹配的代理规则，使得不在本地进行 DNS 解析即可。
- 使用不支持 ECS 的 DNS 服务器，如 CloudFlare 的 1.1.1.1。
- 自定义 DNS ECS 字段，提供虚假的 IP 地址也可以解决这个问题，但可能导致 CDN 调度混乱，出现解析错误、访问缓慢或完全连不上的情况。

## 2024-12-25 [post 799](https://t.me/SurgeTestFlight/799)



## 2024-12-23 [post 797](https://t.me/SurgeTestFlight/797)

我们在 iOS 3415 / macOS 3160 build 中，加入了一项针对 Snell V4 的优化，有望解决 Telegram 偶尔出现卡顿的问题，待观察是否确实有效。

## 2024-12-20 [post 787](https://t.me/SurgeTestFlight/787)

命名已调整为更合适的 Port Forwarding

## 2024-12-20 [post 786](https://t.me/SurgeTestFlight/786)

Surge Mac Beta 更新日志
新功能：透明代理 Transparent proxy
配置样例

[Transparent Proxy]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

其中，policy 参数选填，如果不填的话将使用标准代理匹配决定策略

该功能常见于使用 SSH 连接服务器 MariaDB 等开发调试场景。

## 2024-12-12 [post 763](https://t.me/SurgeTestFlight/763)

Surge iOS & Mac Beta 更新日志
优化了使用 Smart Group 作为 underlying-proxy （代理链）的表现，在先前的版本中由于架构问题，使用 Smart Group 作为一个代理策略的 underlying-proxy 时，Smart Group 无法发挥全部特性（如动态备用策略切换）。新版本中已经完全解决了这些问题。

注：部分用户询问 Snell 的 reuse 机制在 Smart Group 组中无法使用的问题，请注意特意进行的限制，因为 reuse 机制启动的情况下，Smart Group 无法准确评估该代理的表现，同时会导致备用策略切换无法正常运作。

## 2024-12-08 [post 758](https://t.me/SurgeTestFlight/758)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2024-12-05 [post 750](https://t.me/SurgeTestFlight/750)

最近的版本中我们暂停了新功能的开发，着重于处理一些遗留的低概率崩溃和内存泄露问题。目前最新的版本中相关问题都已得到了修正，是目前最稳健的一个版本，将于近日发布正式版本。

什么是内存泄露

简单说就是应用因为任何原因，向系统申请了一段内存未正确释放，导致应用所使用的内存越来越高。

对于 Surge iOS，如果出现持续的泄露，内存占用会不断逼近系统限制，导致被终止重启。对于 Surge Mac，可以观察到内存占用不断提高。

内存泄露问题在计算机科学上一直是一个难题，即使是 iOS/macOS 的系统程序和内置应用，也经常会出现内存泄露的现象。这次修正的数个内存泄露问题也都十分隐蔽，比如当脚本使用 $httpClient 请求数据时，如果 H2 服务端在发送了部分数据后主动中断了该 stream，那可能会导致缓存的部分数据未能被正确释放，这种问题几乎只会在请求特定服务器时才会发生，所以难以被发现。

为此我们重新设计了新的内存泄露检测系统，用于分析这些低概率泄露问题，目前的表现相当良好，崩溃报告系统的数据显示，自 Mac 5.9.2 版本开始已经没有任何用户在遇到过可观测的内存泄露。

## 2024-11-26 [post 738](https://t.me/SurgeTestFlight/738)

我们依然经常会收到关于 Surge iOS 电耗问题的问询，再次解释一下该问题

1. 除非频繁触发脚本，否则 Surge 不会对电量消耗产生明显的影响。
2. 系统的电耗统计，对于 NE 类程序是不准确的，不应该以此作为参考。
3. 除开不准确，部分用户会因为电耗统计中 Surge 所占用百分比很高而认为 Surge 非常耗电。请注意该统计中的百分比，指的是这段时间内的电量消耗中 Surge 的占比，而非表示 Surge 消耗了如此多的电量。由于 Surge NE 常驻后台，如果这段时间内没有几乎没有使用过设备，那即使 Surge 只消耗了极少的电量，也会被统计为 100%。

我们也会定期测试最新版本 Surge 是否存在电量异常的情况，使用 5.14.1 版本在 iPhone 12 mini 上反复进行测试（仅 Wi-Fi），从剩余电量 100% 开始 24 小时后，无论 Surge 是否开启，剩余电量均为 72-74%，几乎属于测量误差范围。

## 2024-11-11 [post 693](https://t.me/SurgeTestFlight/693)

关于空密码的提示
接到部分用户反馈关于在代理协议中使用空密码的问询，为此对该问题进行一定说明：
1. “空密码”可以指代密码不存在（即为 null），或者是一个空字符串（即 '/0'）。目前对应的 Surge 配置语法为，不配置 password 字段，或者 password=""。
2. 除了少数特例，绝大多数加密协议都不支持 null 密码，但是几乎所有协议都支持空字符串密码（因为密钥派生允许空字符串输入）。但是即使使用空字符串密码，也不会略过加密流程，性能与使用其他密码一致，等同于一个弱安全性密码。
3. 大部分协议都没有对这种情况进行特别注明。且在 UI 进行编辑时，并没有办法区分这两种情况。

因此，Surge 将在后续版本中统一关于空密码的处理行为，仅在部分明确不使用加密的协议中支持 null 密码（如 SS 的 none 模式），不再支持空字符串密码，请注意。

## 2024-11-08 [post 650](https://t.me/SurgeTestFlight/650)



## 2024-11-08 [post 649](https://t.me/SurgeTestFlight/649)

Surge Mac Beta 最新版本在状态栏图标加入了出站模式指示，如果不需要可在外观设置中关闭

## 2024-11-05 [post 635](https://t.me/SurgeTestFlight/635)

提示
我们的客服邮箱 support@nssurge.com 向 @icloud.com 域所回复的邮件，最近几日经常被拒绝，原因不明，如需联系请换用其他邮箱，请见谅。

## 2024-11-04 [post 634](https://t.me/SurgeTestFlight/634)

补充
- HTTP API /scripting/evaluate 新增 argument 参数

## 2024-11-04 [post 632](https://t.me/SurgeTestFlight/632)

Surge iOS Beta 更新日志
- 脚本编辑页面支持传入 $argument
- 在脚本列表页面执行脚本也会传入 $argument 的内容了
- 脚本的 $trigger 参数新增 "editor" 和 "http-api" 两个来源
- 修正 iOS 16 下 WireGuard 可能无法使用的问题
- 修正部分代理协议的流量统计中，未计算上传的 UDP 流量的问题

## 2024-11-01 [post 631](https://t.me/SurgeTestFlight/631)

Surge Mac 5.9.0 版本已正式发布，iOS 与 tvOS 5.14.0 版本已在 App Store 正式发布。

## 2024-10-31 [post 624](https://t.me/SurgeTestFlight/624)

Surge Mac 5.9.0 与 iOS 5.14.0 已进入 RC 阶段，iOS 版本由于审核的一些离谱原因，默认图标更换为了 5.0 图标，如果想使用经典图标请手动修改。

## 2024-10-28 [post 606](https://t.me/SurgeTestFlight/606)

Surge Mac & iOS Beta 更新日志
- 修改 HTTP 脚本的终止逻辑，如果需要打断请求，应使用 $done({abort: true})，除此之外的失败将对请求不做修改而不会终止
- 修正 Body Rewrite 规则的处理逻辑，如果遇到非 UTF-8/非 JSON 请求，行为修改为不做修改而非失败
- 优化 QUIC 流控，降低在上传测速时出现的内存占用

## 2024-10-27 [post 599](https://t.me/SurgeTestFlight/599)

Surge Mac 更新日志
- UDP 整体架构进行重构，UDP 相关功能可能出现问题，如有遇到请回报。
- shadowsocks 协议支持配置 udp-port 参数，用于单独指定 UDP 模式的服务端端口号，可在使用 ShadowTLS 时使用原端口号。

## 2024-10-27 [post 596](https://t.me/SurgeTestFlight/596)

以及 WireGuard

## 2024-10-27 [post 594](https://t.me/SurgeTestFlight/594)

该问题可能影响所有使用 QUIC 类代理协议的用户，同时包含 DoQ 和 DoH3

## 2024-10-27 [post 593](https://t.me/SurgeTestFlight/593)

根据一些用户的回报，我们发现在支持 hysteria2 的端口跳跃时，对 QUIC 在网络切换时进行的优化，可能会在网络切换时触发系统 Bug，导致 Surge iOS 有概率在切网后所有的连接均超时。（系统路由表紊乱）
最新 TF 版本中移除了该优化，请有遇到这类问题的用户测试一下确认问题是否改善。

## 2024-10-24 [post 584](https://t.me/SurgeTestFlight/584)

同时请求 Timing 日志中加入了 Body Rewrite 阶段的耗时统计

## 2024-10-24 [post 582](https://t.me/SurgeTestFlight/582)

Surge Mac & iOS Beta 更新日志
- 新的订阅功能
Body Rewrite 支持使用 JQ 表达式对 JSON 进行操作

http-response-jq ^http://httpbingo.org/anything '.headers |= with_entries(select(.key | test("^X-") | not))'

JQ 表达式说明详见：https://jqlang.github.io/jq/ https://jqlang.github.io/jq/

## 2024-10-22 [post 567](https://t.me/SurgeTestFlight/567)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2024-10-21 [post 565](https://t.me/SurgeTestFlight/565)

关于 Pre-matching REJECT 的说明已加入到手册中：https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html

## 2024-10-20 [post 562](https://t.me/SurgeTestFlight/562)

Surge Mac & iOS Beta 更新日志
- 增加 pre-matching 标记规则的校验，在不支持的规则上配置该标记将直接产生配置错误。(请注意 PROTOCOL 语句不可用，逻辑规则的子规则也会被校验，但是 RULE-SET 的子规则若不支持仅会不生效而不会报错)
- 对 TCP RST 拒绝方式增加了全局防御，当 3 秒内触发 100 次后，将临时暂停以避免应用死循环导致 CPU 异常，同时输出日志
-  pre-matching 的请求日志，由每 30 分钟一条，下调至 5 分钟
- [iOS] 为 iOS 18.1 下，Poor Network Quality 无法被从通知中心自动消除的问题加入了一个 workaround

## 2024-10-19 [post 558](https://t.me/SurgeTestFlight/558)

Surge Mac Beta build 2975 已实现该功能

## 2024-10-19 [post 557](https://t.me/SurgeTestFlight/557)

REJECT-NO-DROP 改进
接到部分用户回报，在用于去广告等用途时，如果 DNS 返回 NXDOMAIN 可能导致应用等待，而返回 127.0.0.1 http://127.0.0.1/ 会使得应用立刻认为请求失败。

出现该区别的原因，是因为应用开发者对于不同错误的处理逻辑不同。然而在 DNS 中返回 127.0.0.1 http://127.0.0.1/ 进行屏蔽，是一项非常不标准的行为，本质是将请求导向了回环网络 lo0，由本地系统产生一个 TCP refused 响应拒绝请求。

1. 如果本地系统上正好监听了访问的端口，会导致对应监听服务收到该请求，产生非预期结果。
2. 如果被屏蔽的应用重试逻辑非常暴力，由于 connect 127.0.0.1 http://127.0.0.1/ 会被系统极快的拒绝，可能导致 CPU 占用 100%。（即手机发热）

为此 Surge 提供了一个全新的解决方案，对于使用 REJECT-NO-DROP 的请求，Surge DNS 将固定返回特殊 IP 地址 198.18.0.244。对于该地址的所有 TCP 请求，将由 Surge VIF 产生 TCP refused，同时当发现往该地址的 TCP SYN 极高时，进行丢包处理以避免引发高 CPU 占用。 

这种处理方式既保留了返回 127.0.0.1 http://127.0.0.1/ 的优点，同时消灭了可能导致的副作用。如果在使用 REJECT 时，出现了 app 等待过长的问题，可尝试使用 REJECT-NO-DROP。

## 2024-10-19 [post 554](https://t.me/SurgeTestFlight/554)

更新中加入了对代理模式接管的请求的 pre-matching 处理，REJECT 行为是进行 TCP RST，DROP 行为是将 socket 挂起。

## 2024-10-19 [post 553](https://t.me/SurgeTestFlight/553)

关于 Pre-Matching 功能的一些补充说明：
Pre-Matching 规则的 REJECT 策略依然有意义，对于 REJECT/REJECT-NO-DROP 策略，TCP 请求会在 SYN 时立刻收到 TCP RST（客户端表现为 Connection refused），DNS 请求会收到 NXDOMAIN 响应。
而对于 REJECT-DROP 策略，TCP 的 SYN 包与 DNS 查询包将被直接丢弃，不做任何响应。
REJECT 同样会在一定频次后（30 秒内 50 次触发），自动升级为 REJECT-DROP。
除有明确的特殊需求外，建议使用默认的 REJECT，没必要主动使用 REJECT-DROP。

## 2024-10-19 [post 549](https://t.me/SurgeTestFlight/549)

相比最初版本进行了修订，不再限制 DOMAIN 类型不带有 extended-matching 标记， 不再限制 IP 类型一定需要 no-resolve 标记。
Surge Mac Beta Build 2971 已经可以开始测试该机制。

## 2024-10-18 [post 548](https://t.me/SurgeTestFlight/548)

新的订阅功能 Pre-matching
（Mac 版本不需要订阅）

用于描述使用 REJECT 策略的规则，如 

[Rule]
DOMAIN,ad.com http://ad.com/,REJECT,pre-matching

被标记了 pre-matching 的规则，将在正常的规则匹配流程前就提前生效，因此该规则相当于拥有最高优先级。

该功能的意义是，由于 Surge 的规则系统可判断的内容非常多，所以规则判定需要在收到首个 TCP 数据包后才可以进行，对于应对风暴请求或者去广告需求，产生了过多不必要的开销。

所有被标记了 pre-matching 的规则将会被提取出来进行优先匹配，在 DNS 解析与 TCP SYN 阶段就执行判断。若 DNS 域名命中，则直接返回 NXDOMAIN，若 TCP SYN 阶段命中，将直接产生 ICMP REFUSED 响应，大量请求时升级至丢包，UDP 同样处理。

同时，对于每条规则，每 30 分钟仅会在最近请求列表中出现一次，避免因为大量请求刷屏。

可以使用 pre-matching 标记的规则类型有：

- DOMAIN 类型：DOMAIN,DOMAIN-SUFFIX,DOMAIN-KEYWORD,DOMAIN-SET,DOMAIN-WILDCARD。与 DOMAIN 类型联用时，不可以同时配置 extended-matching。
- IP 类型：IP-CIDR,IP-CIDR6,GEOIP,IP-ASN。与 IP 类型联用时，必须同时配置 no-resolve。
- 逻辑规则：AND,OR,NOT
- 其他：SUBNET,DEST-PORT,IN-PORT,SRC-PORT,SRC-IP

RULSET 也可以使用，但是其内容同样受到上述限制。

举例来说，对于最近米家 App 的疯狂请求，就可以靠配置

[Rule]
DEST-PORT,5222,pre-matching

在低开销的情况下进行屏蔽。

--------------
以上内容为设计草案，有待修改。

## 2024-10-18 [post 546](https://t.me/SurgeTestFlight/546)

根据用户报告和反复测试，仅配置 2000::/3 路由对该特定 app 的 IPv6 请求问题的没有作用，下个版本将回滚代码取消该参数。
请尽量不要使用 ipv6-vif=always

## 2024-10-18 [post 543](https://t.me/SurgeTestFlight/543)

加入了一项 workaround，现在 ipv6-vif-route-mode 参数可以正确产生作用了

## 2024-10-18 [post 541](https://t.me/SurgeTestFlight/541)

由于一些 NE 的系统限制，ipv6-vif-route-mode 参数未能按预期工作，下个版本将提供其他替代参数

## 2024-10-18 [post 540](https://t.me/SurgeTestFlight/540)

有用户询问新参数与 ipv6-vif 参数的关系，ipv6-vif 参数控制是否开启 Surge VIF 的 IPv6，而 ipv6-vif-route-mode 控制在开启 IPv6 VIF 后的路由配置模式。
也就是说只有在，ipv6-vif=auto/always 下，ipv6-vif-route-mode 参数才有意义。

## 2024-10-18 [post 537](https://t.me/SurgeTestFlight/537)

Surge Mac & iOS Beta 更新日志
新增参数 `ipv6-vif-route-mode`，可选值为 auto、default、gua、manual

- default
配置 Surge VIF 为 default 路由，即先前版本中的工作模式。
- gua
仅配置 2000::/3 的路由，即只对公网 IPv6 地址生效。
- manual
应配合 tun-included-routes 参数使用，Surge 默认不再加入任何路由
- auto （默认选项）
让 Surge 自己决定工作模式

增加该选项的原因是因为，部分用户希望使用 IPv6 VIF 接管一些特定的请求，因此配置了 ipv6-vif=always，但是这会导致微信和其他一些应用认为当前系统存在有效的 IPv6 因此优先尝试，但是由于实际上本地并不存在有效的 IPv6 网络，需要等待出现错误后再回退到 IPv4。

配置为 gua 工作模式，由于不存在 IPv6 的 default 路由，所以不会让这类软件判定 IPv6 可用，但是依然能正确接管 IPv6 请求。

## 2024-10-16 [post 528](https://t.me/SurgeTestFlight/528)

Surge iOS Beta 更新日志
- 新增 HTTP Capture 的控制中心开关
- 支持使用 Ponte 策略作为 underlying-proxy

## 2024-10-16 [post 524](https://t.me/SurgeTestFlight/524)

Surge iOS Beta 更新日志
- 策略组列表视图支持配置自定义图标
- 修正带行尾注释的 DNS Mapping 项目无法在 UI 显示的问题
- 在全局模式下，若原选中策略不存在，将回退至第一个代理，而非 DIRECT

## 2024-10-15 [post 519](https://t.me/SurgeTestFlight/519)

Surge Mac & iOS Beta 更新日志
修改  SIP023 Identity 参数的配置方式为在 password 中使用 : 分隔，不再使用 identity 字段，与其他客户端相一致

## 2024-10-15 [post 518](https://t.me/SurgeTestFlight/518)

关于 Shadowsocks 2022 的性能表现：
- 在延迟上，与原版完全相同
- 在吞吐量上，原版中限制单个 AEAD 加密 chunk 最大长度为 16383（0x3FFF），与 TLS 协议的 record 最大长度一致，而 SS-2022 为 0xFFFF。这导致在进行 iperf 等极端压力测试的情况下，SS-2022 的表现会更好。但是 chunk 长度过大可能导致解密延迟（因为必须接收完毕整个 chunk 的数据才可以开始解密）。不过在正常使用中，基本都属于可以忽略不计的区别。

## 2024-10-15 [post 514](https://t.me/SurgeTestFlight/514)

Surge Mac & iOS Beta 更新日志
新的订阅功能：Shadowsocks 2022 加密协议支持
- 支持 2022-blake3-aes-256-gcm 与 2022-blake3-aes-128-gcm 两种模式
- UDP 转发同样需要配置 udp-relay=true
- 可配置 identity 参数以使用 SIP023 Shadowsocks 2022 Extensible Identity Headers，目前仅支持配置一层

## 2024-10-10 [post 502](https://t.me/SurgeTestFlight/502)

Surge 配置提示
在协助部分用户排查问题时，发现用户配置了过多的 DNS 记录（13000+）。如此多的内容会导致内存与性能问题。
由于 [Host] 段内容支持通配符且有先后顺序，无法进行索引优化，所以匹配的性能很低，因此并不建议在这里配置过多内容，也没有必要。（百条量级的话开销可忽略不计）
如果是为了区分解析，请参考白皮书，应正确配置规则系统确保解析在代理服务器发生，而非在本地进行解析。
如果是为了广告屏蔽，请使用 REJECT 规则。

## 2024-10-10 [post 499](https://t.me/SurgeTestFlight/499)

Surge Mac & iOS Beta 更新日志
- 部分用户的网络存在异常，IPv6 的路由会被不断配置与清除，导致在 ipv6-vif=auto 的情况下 Surge 需要不断重新配置 VPN。该版本加入了一个 workaround，在同一个网络下，如果 IPv6 路由在存在的情况下又被清除，也不再重置 VIF 状态。
- 优化了加密 DNS 的错误处理逻辑，在遇到错误时将立刻进行重试

## 2024-10-09 [post 494](https://t.me/SurgeTestFlight/494)

Surge iOS Beta 更新日志
- 优化了策略组图标的显示效果
- 优化 HTTP 引擎对非标准请求的兼容性
- 修正有时控制中心/桌面小组件在 Surge 已关闭时依然显示开启的问题
- 在没有网络时开启 Surge 将给出更明确的错误提示

## 2024-09-25 [post 486](https://t.me/SurgeTestFlight/486)

Surge iOS 使用提示
最近几周接到若干用户回报，米家 app 开启时会产生大量请求，可能导致 Surge 因瞬时内存占用过高导致 Surge 被停止。确认该问题为米家 app 死循环请求所致。
部分用户产生用 tun-excluded-routes 和兼容模式参数绕过，这其实是不合适的，即使不开启 Surge，系统仍然会因为米家 app 的疯狂请求而严重发热与大幅消耗电量。
目前的最佳解决方案是配置对应的 REJECT-DROP 规则。由于访问的 IP 是动态解析结果，我们无法提供具体的规则，需要自己根据请求列表结果配置，一个例子：`IP-CIDR,106.120.178.9/32,REJECT-DROP,no-resolve` http://106.120.178.9/32,REJECT-DROP,no-resolve%60
请向米家 app 团队反馈该问题。

## 2024-09-24 [post 479](https://t.me/SurgeTestFlight/479)

4.1.1 RC1 版本已作为正式版本发布，二进制已更新，修正了日志中版本号未更新的问题，除此之外无变化。

## 2024-09-23 [post 474](https://t.me/SurgeTestFlight/474)

Surge Mac & iOS Beta 更新日志
新增参数 proxy-restricted-to-lan/gateway-restricted-to-lan

目前发现部分用户由于不太了解网络安全知识，意外将代理和网关服务暴露于公网（如配置了 DMZ），因此增加了这两个参数，将限制代理和网关服务仅接受来自当前子网下的设备。

这两个参数为默认开启。

## 2024-09-21 [post 466](https://t.me/SurgeTestFlight/466)

Snell Server 版本更新 v4.1.1 RC1
- 修正 UDP 转发时可能出现的一个崩溃

https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-armv7l.zip

## 2024-09-16 [post 442](https://t.me/SurgeTestFlight/442)

Surge Mac 5.8.0 和 iOS 5.13.0 已进入 RC 阶段，如果有问题请尽快反馈

## 2024-09-15 [post 436](https://t.me/SurgeTestFlight/436)

Surge Mac & iOS Beta 更新日志
- [Mac] 本地 DNS 映射的 syslib 关键字可以在增强模式下使用了，但是非增强模式下是完全交给系统完成解析，增强模式下是读取系统的 DNS 地址后由 Surge 解析。
- 新增 [General] 参数 `show-error-page`，用于控制在出现错误时，是否显示 Surge 的 HTTP错误页

## 2024-09-11 [post 426](https://t.me/SurgeTestFlight/426)

由于新 macOS 系统中需要授权的内容太多，为此新增了一个专门的页面用于管理系统授权

## 2024-09-06 [post 401](https://t.me/SurgeTestFlight/401)



## 2024-09-06 [post 400](https://t.me/SurgeTestFlight/400)

Surge Mac Beta 5.8.0 重要版本更新

由于传统的 utun 接管方案在新版系统下会产生众多问题，从 Surge Mac 5.8.0 版本开始，Surge Mac 将使用 Network Extension 作为增强模式接管系统网络。

- Surge Mac 的最低系统版本需求调整至 macOS 12
- 由于需要的权限不同，更新后需要手动进行授权操作
- vif-mode 参数将不再生效
- 增强模式现在可以和网络共享功能协同使用了，即可以直接创建出由 Surge 接管的 Wi-Fi（需要有线网络提供外网）
- 相比旧方案，新方案的最大吞吐量略有下降，我们会在之后给出具体数据。（非万兆网络忽略不计）

最近版本可能有诸多小问题，如果希望稳定请先暂缓更新。

## 2024-09-05 [post 398](https://t.me/SurgeTestFlight/398)

Surge Mac Beta 技术细节说明
在 macOS 15 Sequoia 中，部分系统服务（如 iMessage）的安全策略进行了调整，系统会无视路由表强制跳过 utun 设备访问，而且在访问时使用了主网卡的 DNS 地址。
由于 Surge 增强模式需要劫持系统 DNS，所以会将主网卡 DNS 地址设置为虚拟地址 198.18.0.2，这导致在新版系统下，部分系统服务会尝试使用真实网卡访问该虚拟地址，导致无法联通。
为解决该问题，Surge Mac 新版本中使用真实的 DNS 1.0.0.1 http://1.0.0.1/ 作为劫持地址，以保证系统服务在无视 utun 设备时，也可以正常完成解析。

## 2024-09-04 [post 394](https://t.me/SurgeTestFlight/394)

Surge Dashboard 新增维护菜单，用于便捷管理远程设备

## 2024-09-03 [post 387](https://t.me/SurgeTestFlight/387)

Surge iOS & Mac Beta 更新日志
- 修正开启端口跳越后，数据统计出现的一些问题
- 调整端口跳越配置参数的分隔符为 ;
- [Mac] 适配 macOS Sequoia，解决了增强模式下的一些兼容性问题

## 2024-09-02 [post 386](https://t.me/SurgeTestFlight/386)

Snell 4.1.0 RC1 版本已作为正式版本发布，URL 已调整

https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.0-linux-armv7l.zip

## 2024-09-02 [post 383](https://t.me/SurgeTestFlight/383)

Surge iOS & tvOS Beta 更新日志
Hysteria2 与 TUIC 协议支持端口跳越，用于改善 ISP 对 UDP 的 QoS 问题。详见服务端说明。

Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping=1234,5000-6000,7044,8000-9000, port-hopping-interval=30

配置 port-hopping 参数后，配置前方的主端口号不再生效。

参数
- `port-hopping`：用于配置端口范围，逗号分隔，支持以-配置范围
- `port-hopping-interval`：变换端口号的时间间隔，默认为 30s

## 2024-08-29 [post 380](https://t.me/SurgeTestFlight/380)

Snell Server 版本更新 v4.1.0 RC1
- 调整日志输出，将 broken pipe 错误输出降低到 verbose 级别

https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.0rc1-linux-armv7l.zip

## 2024-08-28 [post 379](https://t.me/SurgeTestFlight/379)

Snell Server 版本更新 v4.1.0 beta 3
- 更新 libuv 至 v1.48.0，修正在特定系统下，访问 IPv6 地址时可能会出现的崩溃

https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b3-linux-armv7l.zip

## 2024-08-27 [post 378](https://t.me/SurgeTestFlight/378)

Snell Server 版本更新 v4.1.0 beta 2
- 完善了 DNS 错误时的日志信息
- 修正某种特定的 DNS 无线记录会导致崩溃的问题

https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b2-linux-armv7l.zip

## 2024-08-27 [post 374](https://t.me/SurgeTestFlight/374)

Snell Server 版本更新 v4.1.0 beta 1

- 更新 DNS 库 c-ares 至最新版本，以解决和特定 DNS 记录的兼容问题
- 在启动时新增当前使用的 DNS 服务器输出
- 新增 dns 参数，用于自定义 DNS 服务器地址，支持配置多个地址，如

[snell-server]
dns = 1.1.1.1, 8.8.8.8, 2001:4860:4860::8888

https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-amd64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-i386.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-aarch64.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-armv7l.zip https://dl.nssurge.com/snell/snell-server-v4.1.0b1-linux-armv7l.zip

## 2024-08-26 [post 372](https://t.me/SurgeTestFlight/372)

Surge Mac & iOS Beta 更新日志
- 提高与服务端 quic-go v0.46.0 的兼容性

相关技术细节
QUIC 协议内置了 Idle Timeout 的机制，同时约定了 max_idle_timeout 参数用于服务端和客户端协商空闲超时的具体时间，根据 RFC 9000，该值为 0 的时候表示不使用该机制。（Section 18.2）

Surge 目前版本该参数会指定为 0，因为 Surge 不依赖 QUIC 的 Idle Timeout 机制。然而最新版本 quic-go 重写后，错误将值 0 作为了超时时间，在第一个 stream 结束后，立刻认为闲置时间超时关闭了连接。

更糟糕的是，quic-go 也没有完成 stateless reset 机制，对于 Surge 后续发出的数据包，直接予以丢弃而不产生 stateless reset 响应，导致 Surge 需等待一定时间超时后，才会认为连接失效而重新建立连接。

最新版本为规避该问题，将 max_idle_timeout 参数调整为 30s。

## 2024-08-12 [post 362](https://t.me/SurgeTestFlight/362)

Surge iOS Beta 更新日志
- 新增 Ponte 诊断功能，用于快速定位 Ponte 相关问题，从 Ponte 设备页面进入
- 修正 subnet 组无法配置自定义图标的问题
- 修正当存在名为 Global 组时，使用全局模式可能出现的问题

## 2024-08-07 [post 360](https://t.me/SurgeTestFlight/360)

Surge iOS & tvOS 5.12.0 App Store 版本更新已发布
- 新的订阅功能：自定义策略组图标
- 使用 CloudKit 重构 Surge tvOS 配置部署流程，稳定性得到大幅提升。请注意需要将 iOS 和 tvOS 都升级至最新版本后才可以使用配置部署功能，且 tvOS 版本需要先启动一次完成注册
- 在请求列表里使用增加规则功能时，可以选择加入已存在的规则集。（支持本地规则文件和 inline 规则集）
- 模块支持配置 client-source-address 参数
- 修正导出 HAR 时的一些问题
- UI 恢复兼容模式（接管模式）设置并增加详细描述
- 优化 No Default Route 模式下开启 IPv6 VIF 时的行为
- 修正 UI 编辑规则时的一些细节问题，如开启状态和注释
- 优化在外部资源页面查看巨型资源时的表现
- 其他细节优化与问题修正

## 2024-08-05 [post 355](https://t.me/SurgeTestFlight/355)

Surge iOS & tvOS Beta 更新日志
- 同步 Mac 版本关于 DNS 转发系统的修改
- 使用 CloudKit 重写 Surge tvOS 配置部署流程，稳定性得到大幅提升。请注意需要将 iOS 和 tvOS 都升级至最新版本后才可以使用配置部署功能，且 tvOS 版本需要先启动一次完成注册

## 2024-08-04 [post 354](https://t.me/SurgeTestFlight/354)

但是鉴于绝大多数情况下，往公网 DNS 发送 .home.arpa 的 PTR 查询都是不合理的，新版 Surge 内置了阻断逻辑，将只向 LAN IP Block 转发此类请求。如果该 hardcode 行为与你的需求产生了冲突，请在社区提出，我们会考虑为该功能增加开关。

## 2024-08-04 [post 353](https://t.me/SurgeTestFlight/353)

关于 PTR 请求的转发
我们收到部分用户回报，Surge 中配置的上游 DNS 收到了大量的 PTR 请求，是否是 Surge 的问题。
Surge 本身并不会产生任何 PTR 请求，Surge 的 DNS 转发器只是将收到的请求转发至所配置的 DNS 服务器。

关于 .home.arpa 等内部 DNS 请求是否应该被转发
Surge 增强模式的 DNS 转发器核心是作为 hijack 系统 DNS 解析的用途，所以对于非 A/AAAA 查询，应该遵循系统逻辑单纯的将捕获的 DNS 请求转发给上游，Surge DNS 并不适用于 RFC 8375 的描述。

从另一个角度所，即使在系统中直接配置公网 DNS，系统也会将 .home.arpa 的请求直接发往公网 DNS，产生这个问题的原因，一是没有文档约束 DNS 客户端设备对于此类请求的行为，二是客户端其实没有办法判定配置的 DNS 是否为内网 DNS，依据 LAN IP Block 判定是一种不完备的方案。

## 2024-08-04 [post 352](https://t.me/SurgeTestFlight/352)

Surge Mac Beta 更新
- DNS 转发子系统优化
  - 当处理的 DNS 请求的域名为不应向公网转发的域名时（如 .home.arpa，1.0.168.192.in-addr.arpa），将自动判断上游的 DNS 地址，仅向 LAN DNS 转发。
  - 现在 Surge 可以正确的应答 fake IP 的 PTR 请求了，即使用 dig -x 198.18.23.87 命令可用于确定 fake IP 对应的域名。
  - DNS 转发器现在将依据 [Host] 段配置转发 DNS 请求到特定上游服务器。
  - 对针对 Fake IP 的 DNS-SD 请求直接响应 NOTIMP，不再进行转发。

## 2024-07-11 [post 339](https://t.me/SurgeTestFlight/339)

Surge Mac 设计调整提示：新版本中如果选择了在菜单中显示 Top Clients，即使客户端/进程数量不足，也会显示占位行，以避免突然增加的项目导致菜单变化导致误点击（it's a feature not bug）

## 2024-07-10 [post 336](https://t.me/SurgeTestFlight/336)

Surge Mac 现已支持 iOS 版本的 Panel 功能

## 2024-07-02 [post 327](https://t.me/SurgeTestFlight/327)

Surge iOS Beta 更新日志

新的订阅功能：自定义策略组图标
（仅 Lucid 主题下可用）

- 可通过 UI 进行编辑，增加外部图标库，支持搜索，图标库索引文件定义如下：
{
    "name": "Icon Set Name",
    "icons": [
     { "name": "Icon1", "url": "https://…"},
     { "name": "Icon2", "url": "https://…"},
    ]
}

配置后写入策略组的 icon-url 参数，也可以直接配置该参数。

- 可在动态资源页面中，清理图标缓存。

## 2024-06-27 [post 324](https://t.me/SurgeTestFlight/324)

新版本中已统一 Dashboard 中快速增加规则的面板，同样可以使用该新特性

## 2024-06-27 [post 322](https://t.me/SurgeTestFlight/322)



## 2024-06-27 [post 320](https://t.me/SurgeTestFlight/320)

Surge Mac Beta 更新日志
- 为网页增加规则时，可以选择加入已存在的规则集。

## 2024-06-21 [post 308](https://t.me/SurgeTestFlight/308)

tvOS 版本已在 App Store 更新

## 2024-06-21 [post 301](https://t.me/SurgeTestFlight/301)

Surge tvOS TF 版本更新将在 5 分钟后可用，今日提交商店版本

## 2024-06-21 [post 299](https://t.me/SurgeTestFlight/299)

由于 Surge Ponte 所依赖的一个公共 STUN 服务器突然关闭，导致 Surge Ponte 功能不可用，我们已进行紧急替换，请更新 Surge Mac 至最新版本。同时将在未来自建 STUN 服务器以避免这类问题。

## 2024-06-12 [post 275](https://t.me/SurgeTestFlight/275)

Surge iOS Beta 更新日志
- 支持在始终开启开关打开的情况下，通过小组件/控制中心/捷径关闭 Surge
- 支持在 Surge VPN Profile 未被选中的情况下（其他 VPN 运行时），通过小组件/控制中心/捷径开启 Surge

## 2024-06-11 [post 273](https://t.me/SurgeTestFlight/273)

Surge iOS Beta 更新日志
- 支持在 iOS 18 beta 下在控制中心里直接开关 Surge

## 2024-06-03 [post 257](https://t.me/SurgeTestFlight/257)

Surge Mac Beta 更新日志
所有主机名列表参数类型新增关键字 <simple-hostname>，用于匹配不带 . 的主机名，如

always-real-ip = -<simple-hostname>

（上述配置可以用来在增强模式中使用 NetBIOS 主机名连接 SMB 服务器）

## 2024-06-01 [post 254](https://t.me/SurgeTestFlight/254)

最新版本与 Tailscale 联合使用的配置样例

[Host]
*.ts.net = server:100.100.100.100

[Rule]
IP-CIDR,100.64.0.0/10,DIRECT,no-resolve

## 2024-06-01 [post 253](https://t.me/SurgeTestFlight/253)

新版本已完成 TCP 的路由自动判定，现在对于这种情况规则只需要使用 DIRECT 即可，会遵循系统路由表。

## 2024-05-21 [post 234](https://t.me/SurgeTestFlight/234)

Surge iOS & Mac Beta 更新日志
- 根据用户反馈和更多测试，允许 QUIC 流量带来的弊端会更大，该版本恢复了 block-quic 参数。（ChatGPT 的 Voice Mode 问题经反复测试确认为因 QUIC 和 HTTP/2 连接的服务器不同可能导致的行为不一致，实际上不管是否允许  QUIC 流量均有可能失败）
- 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
- Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
- 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
- [iOS] 优化了请求详情页的 IP 地址展示
- [iOS] 编辑策略组时不再可以将自身作为子策略加入

## 2024-05-20 [post 230](https://t.me/SurgeTestFlight/230)

关于 QUIC 流量的代理转发
先前我们已经进行过有关的科普，为什么在基于 TCP 的代理上进行 QUIC 流量转发不是一个好主意，因为在网络环境差时会导致 QUIC over TCP 的重发风暴。

除此之外，即使由 over UDP 的代理转发 QUIC，也还会遇到另一个性能问题：流控的链路过长。在转发 TCP 数据流时，Client <-> Proxy 与 Proxy <-> Server 两段链路间有着独立的流控和缓冲区，大部分情况下这是性能的最优解。但是如果使用的是 QUIC 协议，由于流控的相关信息也是加密的，所以只能由 Client <-> Server 间直接完成流控。在网络质量较差时的表现可能远不如前者。

因此我们一直推荐屏蔽 QUIC 流量以逼迫App/浏览器回退到 HTTP/2，这是最合适于代理的工作模式。副作用就是当遇到无法正常回退的 App 时会导致异常。

针对这样的问题我们暂时无法给出比较通用的推荐配置，我们会继续研究更好的解决方案。

## 2024-05-08 [post 203](https://t.me/SurgeTestFlight/203)

Surge iOS TestFlight 更新日志
- 优化规则集索引，现在规则集中的 IP-ASN 规则也可以被索引优化，测试中约 5000 条 ASN  规则的规则集，在旧版中需耗时 4ms，新版只需要 0.001ms
- 修正不正确的 cron 表达式会导致脚本被持续触发的问题

## 2024-05-07 [post 201](https://t.me/SurgeTestFlight/201)

已知问题
当模块中包含含有注释行的 [Rule] 时，会导致无法崩溃。
修正版本等待 TestFlight 处理中

## 2024-05-07 [post 199](https://t.me/SurgeTestFlight/199)

Surge iOS TestFlight 更新日志
- 新的订阅功能：规则分析，目前包含两个子功能：
   1. 规则使用计数，会记录规则的匹配次数。（只统计主规则集中的条目，各类规则集和逻辑规则的子规则不会被统计，统计时会忽略规则参数）
   2. 当前规则集性能测试
以上功能可在规则配置页面找到

## 2024-04-30 [post 197](https://t.me/SurgeTestFlight/197)

Surge iOS & Mac 更新日志
- 优化脚本执行 WebView 引擎管理流程
  - 不再复用出现异常的引擎，以避免有问题的脚本导致后续脚本也出现问题。
  - 加快了引擎回收的速度，以避免造成不必要的内存开销。（该内存占用并不计算在 Surge 引擎内，但是会占用系统空余内存）
- 修正 Smart 组在初始化阶段，使用频率标签未能全部屏蔽的问题
- 修正 Subnet 策略组在网络切换前未能正确选择策略的问题
- [Mac] 修正永久在 Dock 隐藏图标选项未能正确工作的问题
- [Mac] 修正在未开启折叠策略组选项时，菜单中 Smart 组标签显示位置可能不正确的问题
- [Mac] 修正每次进入配置升级页面，Smart 组的开关都处于开启状态的问题
- [iOS] 修正脚本编辑器保存时，如果配置中不存在任何本地脚本，会导致崩溃的问题

## 2024-04-29 [post 189](https://t.me/SurgeTestFlight/189)

之后我们使用了一整个 C 段 IP（/24）给单个设备作为代理使用 Telegram 进行测试，一周内该设备从未再遇到过异常，进一步验证了这个猜测。

## 2024-04-28 [post 169](https://t.me/SurgeTestFlight/169)

SURGE PRO NEWS pinned «🐔 Surge 唯一 Telegram 官方频道 👉»

## 2024-04-27 [post 160](https://t.me/SurgeTestFlight/160)

Surge iOS 5.11.1 & Mac 5.7.1 更新日志 (Preview)

- 优化小型规则集的匹配性能，在旧型号 CPU 上效果尤为明显
- 外置资源更新页面可以显示规则集处理产生的错误信息
- 自动忽略规则集中的无效空行
- 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题
- 修正在 Smart 组内使用 Ponte 策略时，如果目标设备是自身，未能自动转换为 DIRECT 策略的问题
- 修正 Ponte 设备请求在请求日志中显示的时间错误的问题
- 修正在外部策略组内容发生变化时，有低概率出现的崩溃
- 在 Smart 组初始化阶段，不再显示最常使用标签，以避免产生误解
- [iOS] 修正本地脚本文件被编辑后无法被自动重载的问题
- [iOS] 优化大型规则集的索引流程
- [Mac] 修正在建立策略组时，如果勾选了外部策略但是没有填写 URL，会导致崩溃的问题
- [Mac] 修正密钥库管理页面，进行移动操作后的项目未能正确显示存储位置的问题

## 2024-04-25 [post 146](https://t.me/SurgeTestFlight/146)

Smart Group 补充 FAQ：

Q: 为什么对于同一个域名，Smart Group 依然会尝试不同的策略连接
A: 当通过一个代理访问某个网站时，如果该网站的响应速度远低于该代理访问其他网站的速度，则推测该代理对此目标网站不友好，所以在后续连接中会尝试其他线路，在一段时间的数据收集后，最终会收敛稳定到一个策略上。

Q: 为什么某个代理明明已经故障了，但是界面上还是标记为最常使用
A: Smart Group 界面上显示的“最常使用”，指的是最近一段时间内最常被使用的策略，当某个策略突然故障后，虽然他已经不再是首选策略，他可能依然是最近一段时间最常被使用的策略。

## 2024-04-25 [post 137](https://t.me/SurgeTestFlight/137)

Surge iOS & Mac 更新日志
- 崩溃修正
- 修正本地大型规则集被更新后，需要冷启动主程序才能触发重索引的问题
- 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题

## 2024-04-25 [post 136](https://t.me/SurgeTestFlight/136)

已知问题
确认该版本在更新外部资源时会出现崩溃，新版本发布中。

## 2024-04-25 [post 134](https://t.me/SurgeTestFlight/134)

Surge iOS & Mac 更新日志
- 优化小型规则集的匹配性能（1000 条规则以下为小型，优化前单次匹配耗时约为 0.025 ms，优化后 0.001 ms）
- 修正本地脚本文件被编辑后无法被自动重载的问题
- 优化索引系统，对于需要打开主程序进行索引的规则集，现在在进行重索引前，将沿用已存在的索引（旧版本也有这样的设计，但仅限远程资源，且重启后会失效）

## 2024-04-22 [post 103](https://t.me/SurgeTestFlight/103)

Surge iOS 5.11.0 & Mac 5.70 更新日志 (Preview)

### Smart Group

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（url/load-balance/fallback），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

详情请见：https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group

### 规则系统
- 规则系统整体性能优化。
- 大幅优化大型域名规则集中的索引算法，对于十万条以上的规则集，检索效率提高了十倍以上。
- 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题
- 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 * 匹配域名
- DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题

### IPv6
- ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
- 为 ipv6-vif=always 参数增加了警告
- 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）

### 其他优化
- $notification.post http://notification.post/ 增强，新增媒体资源支持、声音提示和自动消除。
- 优化 WireGuard 失败处理
- 降低 TUIC 协议在休眠时对电量的消耗
- 请求日志系统时间统计精度提高，现在可精确到 µs 级
- 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
- 优化外部资源的缓存系统
- 新增配置文件行命令 #!REQUIREMENT
- [iOS] 在发现当前网络由 Surge Mac Gateway 所接管时，现在将自动暂停 Surge iOS。（可通过 auto-suspend 选项调整行为，默认开启）
- [iOS] 优化 TUN 接管和特定 app 的性能兼容性问题
- [iOS] 优化了内存占用，不常用和巨大的脚本现在将不会被缓存至内存
- [iOS] 网络诊断页新增 SSID/BSSID，增加复制功能
- [iOS] 现在在日志界面执行日志上传时，将自动为当前运行的引擎生成最近的 verbose 日志（新版本在内存缓存了 256KB 的日志），这样在汇报问题时，直接执行上传即可，无需再使用 verbose 模式复现。
- [iOS] 对于策略组与脚本类型的外部资源，现在限制最大大小为 2MB，避免当错误配置时，导致的内存超限。

### 细节调整
- [iOS] 提高内存警告的阈值到 45MB，原为 40MB。
- 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
- 默认 UDP 测试目标改为 1.0.0.1 http://1.0.0.1/
- 在脚本中使用 API 时如果传入了错误类型的字段，将产生脚本异常
- 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

### 问题修正
- [Mac] 修正 Dashboard 查看远端设备时，无法读取截取的 HTTP Body 的问题
- [iOS] 修正在 Surge iOS 主程序和引擎都开启时，iCloud 内容发生变化可能无法被主程序所检测的问题
- 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
- 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
- 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

## 2024-04-20 [post 98](https://t.me/SurgeTestFlight/98)

Surge iOS & Mac 更新日志
- 规则系统整体性能优化
- µs 时间改为 ms 的小数方式表示
- iOS 版本同步 Mac 版本的新巨型规则集索引系统，由于建立索引的内存开销较大，现在 RULE-SET 和 DOMAIN-SET 必须由主程序进行更新（主程序同样会自动执行更新）
- 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题

## 2024-04-20 [post 96](https://t.me/SurgeTestFlight/96)

注：由于实际使用时存在线程调度等开销，最终的 Rule Evaluating 时间依然为 1ms 左右

## 2024-04-20 [post 95](https://t.me/SurgeTestFlight/95)

Surge Mac 更新日志
大幅优化大型域名规则集中的索引算法，测试环境下，对包含 310000 条规则的规则集进行测试（50% hit rate）
旧版本：2.167 ms
新版本：0.058 ms

## 2024-04-20 [post 94](https://t.me/SurgeTestFlight/94)

Surge Mac 更新日志
- 大幅优化大型域名规则集中的索引算法，测试环境下，对包含 310000 条规则的规则集进行测试（50% hit rate）
旧版本：约 2ms

## 2024-04-20 [post 92](https://t.me/SurgeTestFlight/92)

已知的 Bug
新版本的时间统计中，显示的 µs 值有误，实际应为显示值 x1000。如 0.7µs 为 700µs。

## 2024-04-20 [post 90](https://t.me/SurgeTestFlight/90)

Surge iOS & Mac 更新日志
- 优化 WireGuard 失败处理
- 降低 TUIC 协议在休眠时对电量的消耗
- 请求日志系统时间统计精度提高，现在可精确到 µs 级（1s=1000ms,1ms=1000µs）

## 2024-04-19 [post 82](https://t.me/SurgeTestFlight/82)

Surge iOS & Mac 更新日志
- 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 * 匹配域名
- 放开了 fallback 组使用 Smart Group 的限制，允许在 fallback 组内使用 Smart Group 作为子策略
- 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
- UI 细节调整

## 2024-04-19 [post 80](https://t.me/SurgeTestFlight/80)

Surge iOS & Mac 更新日志
- DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题
- 在锁屏/休眠状态下不再触发策略组的自动重测
- 修正 IPv6 相关的一些日志错误
- 传统 DNS 现在将校验响应的服务端 IP，用于处理特定网络下的 DNS 抢答

## 2024-04-19 [post 79](https://t.me/SurgeTestFlight/79)

🐔 Surge 唯一 Telegram 官方频道 👉

## 2024-04-18 [post 62](https://t.me/SurgeTestFlight/62)

Surge iOS & Mac 更新日志
- [Mac] 修正 Dashboard 查看远端设备时，无法读取截取的 HTTP Body 的问题
- ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
- 为 ipv6-vif=always 参数增加了警告
- 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）
- 文案完善

## 2024-04-17 [post 58](https://t.me/SurgeTestFlight/58)

关于该功能的完整描述已更新到文档：https://manual.nssurge.com/others/managed-profile.html https://manual.nssurge.com/others/managed-profile.html

## 2024-04-17 [post 54](https://t.me/SurgeTestFlight/54)

- 新增配置功能自动升级机制，可自动将配置中的 url-test/load-balance，自动升级为 smart 组。   - 对于一般配置，改动会自己写入配置中   - 对于托管配置和企业配置，会在加载配置时自动应用（企业配置不会进行询问，将自动完成升级） 如果不希望托管配置或企业配置被自动升级所修改，可增加配置描述 #!FORBIDDEN-UPGRADE smart-group （未来会增加更多自动升级的关键字） - 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

## 2024-04-17 [post 52](https://t.me/SurgeTestFlight/52)

- 新增配置功能自动升级机制，可自动将配置中的 url-test/load-balance，自动升级为 smart 组。
  - 对于一般配置，改动会自己写入配置中
  - 对于托管配置和企业配置，会在加载配置时自动应用（企业配置不会进行询问，将自动完成升级）
如果不希望托管配置或企业配置被自动升级所修改，可增加配置描述
#!FORBIDDEN-UPGRADE smart-group
（未来会增加更多自动升级的关键字）
- 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

## 2024-04-17 [post 50](https://t.me/SurgeTestFlight/50)

Surge iOS & Mac 更新日志
- 新增配置文件行命令 #!REQUIREMENT

#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB

也可以用在行尾

Group = url, policyA, policyB //!REQUIREMENT CORE_VERSION<22

## REQUIREMENT 表达式

可用作判断的变量有 CORE_VERSION, SYSTEM, SYSTEM_VERSION, DEVICE_MODEL, LANGUAGE

可使用的操作符有 =,==,>=,=>,<=,=<,>,<,!=,<>,AND,&&,OR,||,NOT,!,BEGINSWITH,CONTAINS,ENDSWITH,LIKE,MATCHES

一个典型的变量值样例：
CORE_VERSION: 22
SYSTEM: iOS
SYSTEM_VERSION: System Version 17.4.1 (Build 21E236)
DEVICE_MODEL: iPhone16,1
LANGUAGE: zh-Hans

当表达式包含空格时，应该使用 "" 包裹整个表达式。

#!REQUIREMENT "CORE_VERSION>=22 AND SYSTEM==iOS" Group = smart, policyA, policyB

## 提示

1. 表达式在 UI 配置写入时会丢失，所以该功能主要用于托管配置和企业配置。

2. 由于先前版本并不支持该表达式，因此提供了行末和行首两种写法，可灵活利用该机制完成对旧版本的支持，比方说，希望为支持 Smart 组的客户端使用 Smart 组，那么可以写为 

#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB
Group = url, policyA, policyB //!REQUIREMENT CORE_VERSION<22

由于第一行在旧版本中会被当作一条单纯的注释，所以不会产生效果，而第二行的行末注释也仅仅会被当做一般的注释处理。

## 2024-04-16 [post 43](https://t.me/SurgeTestFlight/43)

Surge iOS & Mac 更新日志
- 修正当存在类似 RULE-SET,,DIRECT 的规则时会导致的异常和崩溃
- 修正部分代理错误未能被 Smart 组正确识别的问题
- 修正部分情况下，代理策略的统计数据中，上传数据量被漏计的问题
- 修正使用 Smart 组作为 underlying-proxy 的情况下，在特定错误的情况下会无法自动切换策略的问题
- 优化外部资源的缓存系统
- 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

## 2024-04-15 [post 36](https://t.me/SurgeTestFlight/36)

Surge iOS & Mac 更新日志
- 修正在 Surge iOS 主程序和引擎都开启时，iCloud 内容发生变化可能无法被主程序所检测的问题
- 修改了 Smart 组统计使用率的计算方法，现在最近的使用情况将更快的影响使用率标签。（当策略出现异常后，依然需要一段时间后才会被取消掉最常使用标签，该标签的意义是最近一段时间内最常使用的策略）
- 优化了内存占用，不常用和巨大的脚本现在将不会被缓存至内存
- 提高内存警告的阈值到 45MB，原为 40MB。
- 修改了策略组页面的一些显示细节
- 网络诊断页新增 SSID/BSSID，增加复制功能
- 新增对 QUIC 类协议的丢包率统计，先前版本中由于未计算 QUIC 类协议的丢包率，在 Smart 组中可能导致 QUIC 类策略被高估。
- 其他问题修正

## 2024-04-14 [post 32](https://t.me/SurgeTestFlight/32)

Surge iOS & Mac 更新日志
- 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
- 在发现当前网络由 Surge Mac Gateway 所接管时，现在将自动暂停 Surge iOS。（可通过 auto-suspend 选项调整行为，默认开启）
- 现在在日志界面执行日志上传时，将自动为当前运行的引擎生成最近的 verbose 日志（新版本在内存缓存了 256KB 的日志），这样在汇报问题时，直接执行上传即可，无需再使用 verbose 模式复现。
- 对于策略组与脚本类型的外部资源，现在限制最大大小为 2MB，避免当错误配置时，导致的内存超限。
- 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
- 细节问题修正

技术细节调整：
- Surge iOS 新版中自动设置的系统 DNS 由 198.18.0.2 http://198.18.0.2/ 变为 198.18.0.4，Mac 版本继续使用 198.18.0.2，同时支持使用任意 198.18.0.2-255 的地址作为 DNS

## 2024-04-12 [post 26](https://t.me/SurgeTestFlight/26)

Surge iOS & Mac 更新日志
- 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
- 修正了初始化日志中的一些错误输出
- 修正了配置 Ponte client proxy 为 Smart Group 时无法连接的问题
- Smart Group 支持 evaluate-before-use 参数了
- 默认 UDP 测试目标改为 1.0.0.1 http://1.0.0.1/
- 其他细节问题修正

