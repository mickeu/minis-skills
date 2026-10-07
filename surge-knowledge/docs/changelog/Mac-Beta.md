# Surge Mac-Beta 更新日志

来源频道: https://t.me/SurgeTestFlight

## 2026-10-06 [post 1780](https://t.me/SurgeTestFlight/1780)

#Mac #Beta

Version 6.10.0-12460 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12460-a422c031be675a7c43e79135149ec6c3.zip

### VS Code Extension
Added support for the Surge Language Support extension for VS Code, providing syntax highlighting and real-time diagnostics for profiles, modules, and rule sets. Includes automatic file detection and validation of policy references in detached configurations when the main profile is open. 

This extension must depend on the main Surge application package, requiring Surge Mac 6.10.0 or later, so profile parsing will automatically be updated as Surge is upgraded.

https://marketplace.visualstudio.com/items?itemName=SurgeNetworks.surge-language-support https://marketplace.visualstudio.com/items?itemName=SurgeNetworks.surge-language-support
      
### IP Rewrite
- Added the [IP Rewrite] section, which handles packets entering Surge VIF at the IP layer based on their destination address, before they reach any rule or policy. Available actions:
  - reflect: Swaps the source and destination addresses and sends the packet back to its sender.
  - reject: Responds with a TCP RST to connection attempts and with an ICMP administratively prohibited message to other packets, so the sender fails immediately.
  - drop: Silently discards the packet.

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.
- Added a new option to proactively update the configuration associated with a linked profile.

Official Channel: @SurgeTestFlightFeed

## 2026-10-05 [post 1779](https://t.me/SurgeTestFlight/1779)

#Mac #Beta

Version 6.10.0-12430 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12430-cbf2cfb47f361b7039523f1c56fd9a32.zip

      
### New Features - IP Rewrite
- Added the [IP Rewrite] section, which handles packets entering Surge VIF at the IP layer based on their destination address, before they reach any rule or policy. Available actions:
  - reflect: Swaps the source and destination addresses and sends the packet back to its sender.
  - reject: Responds with a TCP RST to connection attempts and with an ICMP administratively prohibited message to other packets, so the sender fails immediately.
  - drop: Silently discards the packet.

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.
- Added a new option to proactively update the configuration associated with a linked profile.

Official Channel: @SurgeTestFlightFeed

## 2026-10-02 [post 1776](https://t.me/SurgeTestFlight/1776)

#Mac #Beta

Version 6.10.0-12420 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12420-0efa3b1c8e971f360a7f8329a3baccb2.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.
- Added a new option to proactively update the configuration associated with a linked profile.

Official Channel: @SurgeTestFlightFeed

## 2026-10-01 [post 1775](https://t.me/SurgeTestFlight/1775)

#Mac #Beta

Version 6.10.0-12410 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12410-e460c6fd8c9716952c2ac51f3a44d875.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.
- Added a new option to proactively update the configuration associated with a linked profile.

Official Channel: @SurgeTestFlightFeed

## 2026-09-30 [post 1772](https://t.me/SurgeTestFlight/1772)

#Mac #Beta

Version 6.10.0-12400 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12400-4c29d5a6bb74a9434ec09ff1d0c71d19.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.
- Added a new option to proactively update the configuration associated with a linked profile.

Official Channel: @SurgeTestFlightFeed

## 2026-09-28 [post 1770](https://t.me/SurgeTestFlight/1770)

#Mac #Beta

Version 6.9.2-12390 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12390-c3af2a4146b4c1c99018baabce9e74a1.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.
- Optimized Tailscale and WireGuard behavior when switching networks.

Official Channel: @SurgeTestFlightFeed

## 2026-09-25 [post 1766](https://t.me/SurgeTestFlight/1766)

#Mac #Beta

Version 6.10.0-12380 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12380-10bdc5ee143182aac62cdb0397937666.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.

Official Channel: @SurgeTestFlightFeed

## 2026-09-23 [post 1765](https://t.me/SurgeTestFlight/1765)

#Mac #Beta

Version 6.10.0-12370 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12370-25d9734746765f838691f2eb5cb4d5c7.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.

Official Channel: @SurgeTestFlightFeed

## 2026-09-22 [post 1764](https://t.me/SurgeTestFlight/1764)

#Mac #Beta

Version 6.10.0-12360 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12360-e9aabb0dded655a471fb8d62a8550806.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.
- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.

Official Channel: @SurgeTestFlightFeed

## 2026-09-21 [post 1762](https://t.me/SurgeTestFlight/1762)

#Mac #Beta

Version 6.10.0-12350 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12350-efaa67903e023fd38ca31a1ad2ca8367.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.

Official Channel: @SurgeTestFlightFeed

## 2026-09-18 [post 1760](https://t.me/SurgeTestFlight/1760)

#Mac #Beta

Version 6.10.0-12330 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12330-fbe4ab6efad275a27c68cb56a52ca770.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.

Official Channel: @SurgeTestFlightFeed

## 2026-09-17 [post 1757](https://t.me/SurgeTestFlight/1757)

#Mac #Beta

Version 6.10.0-12320 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12320-01f2c94b01a34e1613afe5021bd2a887.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.
- Add a workaround for a system bug in macOS 27.2 beta to prevent Dashboard from crashing.

Official Channel: @SurgeTestFlightFeed

## 2026-09-15 [post 1756](https://t.me/SurgeTestFlight/1756)

#Mac #Beta

Version 6.10.0-12300 https://dl.nssurge.com/mac/v6/Surge-6.10.0-12300-e92f7fef23b1f951614288ae8c9077b6.zip

### Improvements
- A category parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All test-url parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.

Official Channel: @SurgeTestFlightFeed

## 2026-09-09 [post 1748](https://t.me/SurgeTestFlight/1748)

#Mac #Beta

Version 6.9.1-12290 https://dl.nssurge.com/mac/v6/Surge-6.9.1-12290-fb384eba25d82267269116bf821f4643.zip

### Improvements
- The macOS logical rule editor now supports Pre-Matching for AND, OR, and NOT rules using a reject policy, and identifies unsupported sub-rules before saving.

### Fixes
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Fixed dark menu text becoming unreadable on macOS 26 and improved menu bar icon colors when the system appearance changes.
- Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.
- Fixed Hysteria UDP traffic failing with servers where HTTP/3 Datagram negotiation interfered with UDP forwarding.
- Fixed macOS Smart policy group context menus showing outdated usage or incorrect priority adjustments.

Official Channel: @SurgeTestFlightFeed

## 2026-09-08 [post 1747](https://t.me/SurgeTestFlight/1747)

#Mac #Beta

Version 6.9.1-12280 https://dl.nssurge.com/mac/v6/Surge-6.9.1-12280-b62bf7a83844d82eca7b322b8ea1f29b.zip

### Improvements
- The macOS logical rule editor now supports Pre-Matching for AND, OR, and NOT rules using a reject policy, and identifies unsupported sub-rules before saving.

### Fixes
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Fixed dark menu text becoming unreadable on macOS 26 and improved menu bar icon colors when the system appearance changes.
- Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.
- Fixed Hysteria UDP traffic failing with servers where HTTP/3 Datagram negotiation interfered with UDP forwarding.
- Fixed macOS Smart policy group context menus showing outdated usage or incorrect priority adjustments.

Official Channel: @SurgeTestFlightFeed

## 2026-09-07 [post 1745](https://t.me/SurgeTestFlight/1745)

#Mac #Beta

Version 6.9.1-12270 https://dl.nssurge.com/mac/v6/Surge-6.9.1-12270-2558ec95ae9da4d75f75c38ba992918c.zip

### Fixes
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Fixed dark menu text becoming unreadable on macOS 26 and improved menu bar icon colors when the system appearance changes.
- Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.

Official Channel: @SurgeTestFlightFeed

## 2026-09-05 [post 1743](https://t.me/SurgeTestFlight/1743)

#Mac #Beta

Version 6.9.1-12260 https://dl.nssurge.com/mac/v6/Surge-6.9.1-12260-179446c644c232304d1da39938f5e612.zip

### Fixes
- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Fixed dark menu text becoming unreadable on macOS 26 and improved menu bar icon colors when the system appearance changes.
- Fixed unnecessary Surge Helper installation or upgrade alerts at startup when the enabled features do not require the helper.

Official Channel: @SurgeTestFlightFeed

## 2026-08-12 [post 1718](https://t.me/SurgeTestFlight/1718)

#Mac #Beta

Version 6.9.0-12090 https://dl.nssurge.com/mac/v6/Surge-6.9.0-12090-f4eb90ad1cb7854996d58a834937dad0.zip

### Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP datagrams.
- HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
- TrustTunnel can now use HTTP/3 transport with h3=true.

### Poilcy Group

- Added group-level proxy chaining. A policy group can specify an underlying proxy, and all concrete proxy members in that group will connect through it. This can be configured with underlying-proxy or Through Another Proxy in the group editor view.

### VM Gateway
- Improved Gateway Mode IPv6 takeover: Fixed an issue where takeover could suddenly fail on some devices.
- IPv6 RDNSS in Surge has now been restored under IPv6 takeover mode.
- Updated the IPv6 fake IP range to avoid unnecessary browser local network permission prompts, with compatibility for previously cached addresses.

### HTTP API

- Added a Prometheus-compatible /metrics endpoint to the HTTP Controller, exposing build information, uptime, memory usage, active requests, DNS cache size, security bans, interface traffic, and per-policy traffic.

### DNS

- Host rules now support specifying a dedicated DNS server for domain aliases, for example: foo.com http://foo.com/ = bar.com http://bar.com/, server:https://example/dns-query.

### Surge CLI

- The CLI’s interactive mode now supports features such as auto-completion and command history.
- Added profile diff to compare the original profile with the effective profile after modules have been applied.
- Added rule match to evaluate the active rule set without creating a real connection. Hostname, URL, process, source address, client device, protocol, and other matching attributes can be supplied.
- Added rule explain to show why a request selected a particular policy, including the matched rule, each policy-group decision, Smart Group selection, and underlying proxy chain.
- Added rule temp commands to list, add, remove, modify, or clear temporary rules.
- Added dns lookup to resolve a domain through Surge’s DNS pipeline and report the result, responding server, interface, route, timing, and cache lifetime.
- Added dns trace to include the complete resolver trace, with optional lookup through a specified network interface.
- Added geoip to query the local GeoIP and ASN databases used by GEOIP and IP-ASN rules.
- Added http probe to perform an HTTP HEAD request through a specified policy or the active rule system, reporting status, latency, selected policy, matched rule, and response headers.
- Added dump performance to inspect engine memory usage, uptime, active requests, DNS cache entries, virtual IP entries, temporary rules, and security bans.
- Added dump rule-usage to inspect per-rule match counters without clearing them.
- Added targeted dump virtual-ip queries by IP address or domain substring.
- Added benchmark rule-matching to measure the matching performance of the active rule set.
- Added watch speed to continuously display real-time upload and download speeds.
- Added security ban list and security ban clear to inspect or reset Controller unauthorized-access bans.
- Improved CLI help output with command categories and detailed help for individual commands.

## Fixed

- Fixed an issue where DNS-over-HTTP/3 and DNS-over-QUIC servers specified in local DNS mappings could fail bootstrap resolution.
- Fixed an issue where multiple macOS users on the same device had to reactivate Surge.
- Fixed long-running VMess connections being terminated after the chunk counter wrapped.

Official Channel: @SurgeTestFlightFeed

## 2026-08-12 [post 1715](https://t.me/SurgeTestFlight/1715)

#Mac #Beta

Version 6.9.0-12080 https://dl.nssurge.com/mac/v6/Surge-6.9.0-12080-a77f92fcfeae4346935b1569d293f251.zip

### Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP datagrams.
- HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
- TrustTunnel can now use HTTP/3 transport with h3=true.

### Poilcy Group

- Added group-level proxy chaining. A policy group can specify an underlying proxy, and all concrete proxy members in that group will connect through it. This can be configured with underlying-proxy or Through Another Proxy in the group editor view.

### VM Gateway
- Improved Gateway Mode IPv6 takeover: Fixed an issue where takeover could suddenly fail on some devices.
- IPv6 RDNSS in Surge has now been restored under IPv6 takeover mode.
- Updated the IPv6 fake IP range to avoid unnecessary browser local network permission prompts, with compatibility for previously cached addresses.

### HTTP API

- Added a Prometheus-compatible /metrics endpoint to the HTTP Controller, exposing build information, uptime, memory usage, active requests, DNS cache size, security bans, interface traffic, and per-policy traffic.

### DNS

- Host rules now support specifying a dedicated DNS server for domain aliases, for example: foo.com http://foo.com/ = bar.com http://bar.com/, server:https://example/dns-query.

### Surge CLI

- The CLI’s interactive mode now supports features such as auto-completion and command history.
- Added profile diff to compare the original profile with the effective profile after modules have been applied.
- Added rule match to evaluate the active rule set without creating a real connection. Hostname, URL, process, source address, client device, protocol, and other matching attributes can be supplied.
- Added rule explain to show why a request selected a particular policy, including the matched rule, each policy-group decision, Smart Group selection, and underlying proxy chain.
- Added rule temp commands to list, add, remove, modify, or clear temporary rules.
- Added dns lookup to resolve a domain through Surge’s DNS pipeline and report the result, responding server, interface, route, timing, and cache lifetime.
- Added dns trace to include the complete resolver trace, with optional lookup through a specified network interface.
- Added geoip to query the local GeoIP and ASN databases used by GEOIP and IP-ASN rules.
- Added http probe to perform an HTTP HEAD request through a specified policy or the active rule system, reporting status, latency, selected policy, matched rule, and response headers.
- Added dump performance to inspect engine memory usage, uptime, active requests, DNS cache entries, virtual IP entries, temporary rules, and security bans.
- Added dump rule-usage to inspect per-rule match counters without clearing them.
- Added targeted dump virtual-ip queries by IP address or domain substring.
- Added benchmark rule-matching to measure the matching performance of the active rule set.
- Added watch speed to continuously display real-time upload and download speeds.
- Added security ban list and security ban clear to inspect or reset Controller unauthorized-access bans.
- Improved CLI help output with command categories and detailed help for individual commands.

## Fixed

- Fixed an issue where DNS-over-HTTP/3 and DNS-over-QUIC servers specified in local DNS mappings could fail bootstrap resolution.
- Fixed an issue where multiple macOS users on the same device had to reactivate Surge.
- Fixed long-running VMess connections being terminated after the chunk counter wrapped.

Official Channel: @SurgeTestFlightFeed

## 2026-08-11 [post 1714](https://t.me/SurgeTestFlight/1714)

#Mac #Beta

Version 6.9.0-12070 https://dl.nssurge.com/mac/v6/Surge-6.9.0-12070-1163c33c05dd09bb04dcf94e246d2c51.zip

### Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP datagrams.
- HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
- TrustTunnel can now use HTTP/3 transport with h3=true.

### Poilcy Group

- Added group-level proxy chaining. A policy group can specify an underlying proxy, and all concrete proxy members in that group will connect through it. This can be configured with underlying-proxy or Through Another Proxy in the group editor view.

### VM Gateway
- Improved Gateway Mode IPv6 takeover: Fixed an issue where takeover could suddenly fail on some devices.
- IPv6 RDNSS in Surge has now been restored under IPv6 takeover mode.

### HTTP API

- Added a Prometheus-compatible /metrics endpoint to the HTTP Controller, exposing build information, uptime, memory usage, active requests, DNS cache size, security bans, interface traffic, and per-policy traffic.

### Surge CLI

- The CLI’s interactive mode now supports features such as auto-completion and command history.
- Added profile diff to compare the original profile with the effective profile after modules have been applied.
- Added rule match to evaluate the active rule set without creating a real connection. Hostname, URL, process, source address, client device, protocol, and other matching attributes can be supplied.
- Added rule explain to show why a request selected a particular policy, including the matched rule, each policy-group decision, Smart Group selection, and underlying proxy chain.
- Added rule temp commands to list, add, remove, modify, or clear temporary rules.
- Added dns lookup to resolve a domain through Surge’s DNS pipeline and report the result, responding server, interface, route, timing, and cache lifetime.
- Added dns trace to include the complete resolver trace, with optional lookup through a specified network interface.
- Added geoip to query the local GeoIP and ASN databases used by GEOIP and IP-ASN rules.
- Added http probe to perform an HTTP HEAD request through a specified policy or the active rule system, reporting status, latency, selected policy, matched rule, and response headers.
- Added dump performance to inspect engine memory usage, uptime, active requests, DNS cache entries, virtual IP entries, temporary rules, and security bans.
- Added dump rule-usage to inspect per-rule match counters without clearing them.
- Added targeted dump virtual-ip queries by IP address or domain substring.
- Added benchmark rule-matching to measure the matching performance of the active rule set.
- Added watch speed to continuously display real-time upload and download speeds.
- Added security ban list and security ban clear to inspect or reset Controller unauthorized-access bans.
- Improved CLI help output with command categories and detailed help for individual commands.

## Fixed

- Fixed an issue where DNS-over-HTTP/3 and DNS-over-QUIC servers specified in local DNS mappings could fail bootstrap resolution.
- Fixed an issue where multiple macOS users on the same device had to reactivate Surge.
- Fixed long-running VMess connections being terminated after the chunk counter wrapped.

Official Channel: @SurgeTestFlightFeed

## 2026-08-10 [post 1702](https://t.me/SurgeTestFlight/1702)

#Mac #Beta

Version 6.9.0-12040 https://dl.nssurge.com/mac/v6/Surge-6.9.0-12040-9d92fa3bf09db415800d344632f609cd.zip

### Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP datagrams.
- HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
- TrustTunnel can now use HTTP/3 transport with h3=true.

### Poilcy Group

- Added group-level proxy chaining. A policy group can specify an underlying proxy, and all concrete proxy members in that group will connect through it. This can be configured with underlying-proxy or Through Another Proxy in the group editor view.

### HTTP API

- Added a Prometheus-compatible /metrics endpoint to the HTTP Controller, exposing build information, uptime, memory usage, active requests, DNS cache size, security bans, interface traffic, and per-policy traffic.

### Surge CLI

- The CLI’s interactive mode now supports features such as auto-completion and command history.
- Added profile diff to compare the original profile with the effective profile after modules have been applied.
- Added rule match to evaluate the active rule set without creating a real connection. Hostname, URL, process, source address, client device, protocol, and other matching attributes can be supplied.
- Added rule explain to show why a request selected a particular policy, including the matched rule, each policy-group decision, Smart Group selection, and underlying proxy chain.
- Added rule temp commands to list, add, remove, modify, or clear temporary rules.
- Added dns lookup to resolve a domain through Surge’s DNS pipeline and report the result, responding server, interface, route, timing, and cache lifetime.
- Added dns trace to include the complete resolver trace, with optional lookup through a specified network interface.
- Added geoip to query the local GeoIP and ASN databases used by GEOIP and IP-ASN rules.
- Added http probe to perform an HTTP HEAD request through a specified policy or the active rule system, reporting status, latency, selected policy, matched rule, and response headers.
- Added dump performance to inspect engine memory usage, uptime, active requests, DNS cache entries, virtual IP entries, temporary rules, and security bans.
- Added dump rule-usage to inspect per-rule match counters without clearing them.
- Added targeted dump virtual-ip queries by IP address or domain substring.
- Added benchmark rule-matching to measure the matching performance of the active rule set.
- Added watch speed to continuously display real-time upload and download speeds.
- Added security ban list and security ban clear to inspect or reset Controller unauthorized-access bans.
- Improved CLI help output with command categories and detailed help for individual commands.

## Improvements

- Proxy and policy-group editors now more clearly distinguish selecting a group as an underlying proxy from selecting one of its current members.
- Saved and favorite requests are now consistently sorted by their actual start time.
- HTTP proxy requests now preserve the original Host header when the absolute-form request target uses a different authority.
- Reduced encryption benchmark memory usage by processing data in bounded batches.
- Updated Simplified Chinese localizations for the new proxy, Terminal, and diagnostic features.

## Fixed

- Fixed an issue where DNS-over-HTTP/3 and DNS-over-QUIC servers specified in local DNS mappings could fail bootstrap resolution.

Official Channel: @SurgeTestFlightFeed

## 2026-08-10 [post 1700](https://t.me/SurgeTestFlight/1700)

#Mac #Beta

Version 6.8.1-12030 https://dl.nssurge.com/mac/v6/Surge-6.8.1-12030-69f4be88db9663476f31a6b264109f0b.zip

- Fixed an issue where the Host field could be unexpectedly rewritten when handling requests in HTTP mode.
- Fixed an issue in Gateway VM mode where unsolicited UDP packets sent to the gateway's own IP (such as NAT-PMP and unicast mDNS requests) could create excessive UDP sessions, causing high CPU usage.

Official Channel: @SurgeTestFlightFeed

## 2026-07-30 [post 1685](https://t.me/SurgeTestFlight/1685)

#Mac #Beta

Version 6.8.0-11920 https://dl.nssurge.com/mac/v6/Surge-6.8.0-11920-a5028198e907c2a725be7b3b4e9d7cd1.zip

macOS 27

- Began adapting the Surge interface for macOS 27 and added workarounds for macOS system bugs that could cause crashes when opening remote connections or presenting modal sheets while the system text-completion interface was active.

Surge as MTProto Server

- Surge now can operate as an incoming MTProto proxy server for Telegram.
- Please read manual for more information: https://manual.nssurge.com/others/mtproto.html https://manual.nssurge.com/others/mtproto.html

Core Version Alignment

- Starting with Surge Mac 6.8.0 and Surge iOS 5.21.0, the Core Version is derived directly from the corresponding Surge Mac version, eliminating the need to maintain a separate Core Version number. Please check the manual for more information: https://manual.nssurge.com/ https://manual.nssurge.com/

Other Improvements

Official Channel: @SurgeTestFlightFeed

## 2026-07-21 [post 1667](https://t.me/SurgeTestFlight/1667)

#Mac #Beta

Version 6.8.0-11790 https://dl.nssurge.com/mac/v6/Surge-6.8.0-11790-3fdb5f4ea64aa271f4f4026f8b1e75ad.zip

Snell v6 Server

- Added Snell v6 support to the built-in Snell proxy server. Use version=6 in the [Snell Server] section to enable it. Existing configurations continue to use Snell v1 by default.
- Supports default, unshaped, and unsafe-raw modes through the mode parameter.
- Supports reusable encrypted TCP transports and UDP tunneling.
- Improved Snell handshake validation, connection lifecycle handling, EOF processing, and malformed UDP packet handling.

DHCP

- Statically assigned IP addresses are now automatically excluded from the dynamic address pool, preventing duplicate allocation.
- Upgraded the ISC DHCP server to version 4.4.3-P1.

TLS

- Added server-cert-verify-name to independently specify the hostname used for proxy server certificate verification without changing SNI. This parameter applies to all TLS- and QUIC-based proxy protocols.

ECN

- Reworked ECN configuration and packet handling across QUIC, WireGuard, Tailscale, Ponte, and nested UDP tunnels.
- Correctly preserves ECN and DSCP/TOS metadata across IPv4 and IPv6 encapsulation and decapsulation.
- For QUIC-based proxy protocols, when ECN is enabled, anomalies will be automatically detected and fallback to non-ECN handling.
- ECN is now enabled by default for QUIC-based proxy protocols on supported systems. WireGuard and Tailscale remain disabled by default. Use ecn=false or ecn=true to override the default explicitly.
- Surge Ponte now also has ECN enabled by default, and the client-use-ecn parameter has been removed.

DNS

- Optimized TCP connection establishment for prefer-v4 and prefer-v6. In earlier versions, these two parameters indicated which record to use when a domain name had both A and AAAA records. Now, during the TCP handshake, A or AAAA records are used preferentially; if the handshake cannot be completed within 3 seconds, other records will start to be tried.

Tailscale

- Tailscale can now begin handling traffic as soon as a valid network map is received, without waiting for the home DERP connection to be established.
- Improved recovery after network changes and control-server reconnections by preserving the last known home DERP region and retrying peer handshakes at the appropriate time.
- Aligned DERP measurement and selection behavior with official Tailscale client, improving compatibility with custom DERP maps, STUN-only nodes, fallback probes, and temporarily unavailable control connections.
- Sensitive values such as authentication keys and authorization URLs are now redacted from verbose Tailscale control logs.

Codebase Refactoring

After more than a decade of development, the Surge codebase has grown into a large and complex project. To further improve reliability, we have introduced AI-assisted code review across the entire codebase.

Every code change is independently reviewed by Fable 5, GPT-5.6 Sol, and a human developer before being merged, helping us identify potential security issues, rare crash scenarios, and subtle correctness problems.

## 2026-07-17 [post 1663](https://t.me/SurgeTestFlight/1663)

#Mac #Beta

Version 6.8.0-11780 https://dl.nssurge.com/mac/v6/Surge-6.8.0-11780-d6a4943026d79020e4386efc0d700409.zip

### DHCP
- Upgrade ISC DHCP server to version 4.4.3-P1.
- Patched the default behavior of ISC DHCP: IPs that have already been manually statically assigned will no longer be used by the dynamic IP pool.

### Tailscale
- Optimize control logic
- Optimize support for custom DERP servers.

### TLS
- Added server-cert-verify-name to independently specify the hostname used for proxy server certificate verification. Valid for all TLS protocols.
      
### Codebase Refactoring - SSH & HTTP & HTTP3

We have completed a comprehensive review of Surge’s core functionality and resolved numerous implementation issues, edge cases, and long-standing inconsistencies.

This ongoing refactoring effort improves maintainability and helps provide a more robust foundation for future development.

Official Channel: @SurgeTestFlightFeed

## 2026-07-16 [post 1662](https://t.me/SurgeTestFlight/1662)

#Mac #Beta

Version 6.8.0-11770 https://dl.nssurge.com/mac/v6/Surge-6.8.0-11770-3399f5e3b4f90d7af7bf6e0df9e82c60.zip

### DHCP
- Upgrade ISC DHCP server to version 4.4.3-P1.
- Patched the default behavior of ISC DHCP: IPs that have already been manually statically assigned will no longer be used by the dynamic IP pool.
      
### Codebase Refactoring - SSH & HTTP & HTTP3

We have completed a comprehensive review of Surge’s core functionality and resolved numerous implementation issues, edge cases, and long-standing inconsistencies.

This ongoing refactoring effort improves maintainability and helps provide a more robust foundation for future development.

Official Channel: @SurgeTestFlightFeed

## 2026-07-15 [post 1658](https://t.me/SurgeTestFlight/1658)

#Mac #Beta

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

## 2026-07-09 [post 1649](https://t.me/SurgeTestFlight/1649)

#Mac #Beta

Version 6.7.0-11650 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11650-13390ebd66d58d645fc3ec93778ee7ae.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-07-07 [post 1646](https://t.me/SurgeTestFlight/1646)

#Mac #Beta

Version 6.7.0-11620 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11620-46d2189bc19d0e38d06b81361e526b7b.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-07-06 [post 1643](https://t.me/SurgeTestFlight/1643)

#Mac #Beta

Version 6.7.0-11610 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11610-7ed8cd4299010e65a01d2f876e85e0d7.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-07-03 [post 1641](https://t.me/SurgeTestFlight/1641)

#Mac #Beta

Version 6.7.0-11600 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11600-29fd7ee7538bcd84f2a19d903314267a.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-07-02 [post 1639](https://t.me/SurgeTestFlight/1639)

#Mac #Beta

Version 6.7.0-11570 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11570-0f2554b2c7677eeeafce8993608b470e.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-07-01 [post 1636](https://t.me/SurgeTestFlight/1636)

#Mac #Beta

Version 6.7.0-11550 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11550-59320383072ca6f4d03a62778c653377.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-30 [post 1634](https://t.me/SurgeTestFlight/1634)

#Mac #Beta

Version 6.7.0-11520 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11520-1c2452b335be75899e0bbee0bd456c12.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.
- URL scheme actions are now supported in Surge Mac. Check manual for more information.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-29 [post 1632](https://t.me/SurgeTestFlight/1632)

#Mac #Beta

Version 6.7.0-11510 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11510-ab7bc59914280d4b46fdb1928585b22f.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

#### Beta Updates

- IPv6 DERP servers are now automatically disabled based on network conditions.

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Dashboard Renovation

Surge Dashboard has received a comprehensive visual upgrade, along with optimized display of detailed request information.

### Minor Improvements
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-26 [post 1631](https://t.me/SurgeTestFlight/1631)

#Mac #Beta

Version 6.7.0-11500 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11500-ffc10d887f180f1f85e06f6a636d55ae.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Minor Improvements
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-25 [post 1629](https://t.me/SurgeTestFlight/1629)

#Mac #Beta

Version 6.7.0-11490 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11490-cfc60f6ddec86678e24a1958dd0eee9b.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Minor Improvements
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-24 [post 1627](https://t.me/SurgeTestFlight/1627)

#Mac #Beta

Version 6.7.0-11480 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11480-59c2e22b86749875d47e439d0cfb0288.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Minor Improvements
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-23 [post 1624](https://t.me/SurgeTestFlight/1624)

#Mac #Beta

Version 6.7.0-11470 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11470-4dcf21c168d53aa5afc7df44f4557a9b.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Minor Improvements
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
- All TLS proxy protocols now support customizing ALPN using the alpn field.
- When local DNS mapping is specified using server, multiple DNS servers can now be configured.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers.

Official Channel: @SurgeTestFlightFeed

## 2026-06-22 [post 1619](https://t.me/SurgeTestFlight/1619)

#Mac #Beta

Version 6.7.0-11460 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11460-ef184201d0a4c250f1ea642df260e9b0.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.
- Fixed compatibility issues between DoH3 and some servers
- Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter

Official Channel: @SurgeTestFlightFeed

## 2026-06-19 [post 1617](https://t.me/SurgeTestFlight/1617)

#Mac #Beta

Version 6.7.0-11450 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11450-2320215726939c53e7fafbb8e9b6f9bc.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-18 [post 1615](https://t.me/SurgeTestFlight/1615)

#Mac #Beta

Version 6.7.0-11440 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11440-20815060522f660d01a1facd9f72e206.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-18 [post 1612](https://t.me/SurgeTestFlight/1612)

#Mac #Beta

Version 6.7.0-11430 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11430-c8aa8383d04dbaeefbe42028a14ee3c4.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-17 [post 1611](https://t.me/SurgeTestFlight/1611)

#Mac #Beta

Version 6.7.0-11420 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11420-4c31c170cfcc007709efae7c8a7a11c0.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-16 [post 1609](https://t.me/SurgeTestFlight/1609)

#Mac #Beta

Version 6.7.0-11400 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11400-45f0a5c4ef956157a0090821b6e159b0.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- Optimize the performance of Surge Ponte.
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-15 [post 1607](https://t.me/SurgeTestFlight/1607)

#Mac #Beta

Version 6.7.0-11390 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11390-e1aaa41bb77c003b9311bc308b8f658a.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 3, and the server must be updated accordingly.

### Other
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-12 [post 1605](https://t.me/SurgeTestFlight/1605)

#Mac #Beta

Version 6.7.0-11380 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11380-dc998e597015e293aa7a5f4fd1297de9.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

Snell server binary has been updated to beta 2, and the server must be updated accordingly.

### Other
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-11 [post 1602](https://t.me/SurgeTestFlight/1602)

#Mac #Beta

Version 6.7.0-11360 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11360-f19b8bb8da2b0570b629ef6d2acbc0a1.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a proxy policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Snell v6

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

### Other
- The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-09 [post 1600](https://t.me/SurgeTestFlight/1600)

#Mac #Beta

Version 6.7.0-11330 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11330-491c9097d384b26572229acb5537c7c8.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a proxy policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Other
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-09 [post 1599](https://t.me/SurgeTestFlight/1599)

#Mac #Beta

Version 6.7.0-11320 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11320-523c42d96bb28d11b6c860ea7f0eb11c.zip

### Tailscale Support (Beta)

Surge now supports Tailscale as a proxy policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

### Other
- The header parameter for the HTTP proxy type can now override original fields, including Host field.
- Fixed an issue where the header parameter did not take effect in HTTP/1.1 CONNECT mode.
- Fix some issues when using SF Symbols for policy group icons.

Official Channel: @SurgeTestFlightFeed

## 2026-06-05 [post 1596](https://t.me/SurgeTestFlight/1596)

#Mac #Beta

Version 6.7.0-11310 https://dl.nssurge.com/mac/v6/Surge-6.7.0-11310-2adcce90868941219a9d6bbfb14b88c9.zip

### Tailscale Support

Surge now supports Tailscale as a proxy policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

Official Channel: @SurgeTestFlightFeed

## 2026-06-01 [post 1587](https://t.me/SurgeTestFlight/1587)

#Mac #Beta

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

## 2026-05-29 [post 1586](https://t.me/SurgeTestFlight/1586)

#Mac #Beta

Version 6.6.0-11260 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11260-ffff4cc319019736888c3bf22ea729da.zip

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

## 2026-05-28 [post 1584](https://t.me/SurgeTestFlight/1584)

#Mac #Beta

Version 6.6.0-11240 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11240-c67c23d6594cde48975367cd7e3745d6.zip

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

## 2026-05-27 [post 1583](https://t.me/SurgeTestFlight/1583)

#Mac #Beta

Version 6.6.0-11230 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11230-83b6a083b4a24a855a84f1fb69d8a76f.zip

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

## 2026-05-26 [post 1581](https://t.me/SurgeTestFlight/1581)

#Mac #Beta

Version 6.6.0-11220 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11220-13dcac97b03f346bc5f1c9062871c06a.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-26 [post 1580](https://t.me/SurgeTestFlight/1580)

#Mac #Beta

Version 6.6.0-11210 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11210-6f79c788b5b3ca63aab560d469bd8ae1.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-25 [post 1579](https://t.me/SurgeTestFlight/1579)

#Mac #Beta

Version 6.6.0-11190 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11190-378b085501cd3e499afe875fe809369d.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-24 [post 1575](https://t.me/SurgeTestFlight/1575)

#Mac #Beta

Version 6.6.0-11160 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11160-84b966bef2a70baf3eca4de76ca9adf0.zip

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

### Agent Skill

- Add a wizard page for Agent Skill usage to the Help menu

Official Channel: @SurgeTestFlightFeed

## 2026-05-20 [post 1571](https://t.me/SurgeTestFlight/1571)

#Mac #Beta

Version 6.6.0-11140 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11140-828899cefcf6e55d189e732db2c7fcea.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-19 [post 1569](https://t.me/SurgeTestFlight/1569)

#Mac #Beta

Version 6.6.0-11130 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11130-56e41522da278c18b7630100e14138ad.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-18 [post 1567](https://t.me/SurgeTestFlight/1567)

#Mac #Beta

Version 6.6.0-11120 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11120-0ec27c69c73c9132d78d0a8f8abca627.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-15 [post 1561](https://t.me/SurgeTestFlight/1561)

#Mac #Beta

Version 6.6.0-11110 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11110-d3e0528ad725d7e99f49346016487d74.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-05-12 [post 1557](https://t.me/SurgeTestFlight/1557)

#Mac #Beta

Version 6.6.0-11090 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11090-ea52a8f8f6bd6ecb5736858b72604965.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-05-09 [post 1555](https://t.me/SurgeTestFlight/1555)

#Mac #Beta

Version 6.6.0-11080 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11080-419095f8d38576f1a4ab5880cbd761da.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-05-07 [post 1553](https://t.me/SurgeTestFlight/1553)

#Mac #Beta

Version 6.6.0-11070 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11070-5278a765cf6e2831b18550eed6ebeb4d.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-05-06 [post 1551](https://t.me/SurgeTestFlight/1551)

#Mac #Beta

Version 6.6.0-11040 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11040-af1432fa415432d3f4c9f44bc5c18796.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-05-05 [post 1547](https://t.me/SurgeTestFlight/1547)

#Mac #Beta

Version 6.6.0-11030 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11030-998fed41c8b18d9c2a9cc26b42f3ea59.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-29 [post 1546](https://t.me/SurgeTestFlight/1546)

#Mac #Beta

Version 6.6.0-11020 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11020-0646541ff7dd703410988fe4f175c019.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-28 [post 1542](https://t.me/SurgeTestFlight/1542)

#Mac #Beta

Version 6.6.0-11010 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11010-916c6c81575e32aac5688139f3eff24b.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-28 [post 1540](https://t.me/SurgeTestFlight/1540)

#Mac #Beta

Version 6.6.0-11000 https://dl.nssurge.com/mac/v6/Surge-6.6.0-11000-14df17a5a106dd1dcaa39e4d4a6a18cb.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-27 [post 1539](https://t.me/SurgeTestFlight/1539)

#Mac #Beta

Version 6.6.0-10980 https://dl.nssurge.com/mac/v6/Surge-6.6.0-10980-0afe1d6f5a801c9d0b89ce0f50318184.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-27 [post 1536](https://t.me/SurgeTestFlight/1536)

#Mac #Beta

Version 6.6.0-10970 https://dl.nssurge.com/mac/v6/Surge-6.6.0-10970-045f2994bd20d05aa0efb1c0c4949589.zip

### Logbook

The Logbook feature has now been added to Surge for Mac and iOS. Logbook is used to persistently record events, and they won’t be lost after Surge is closed. (The current version keeps only the most recent 7 days of events by default.)

- Surge Dashboard supports reading Logbook content from remote instances, and also supports viewing the input/output of script-type records as well as log output. The peer can be Surge iOS or Mac, and all content supports remote loading.

- The Mac version has added Logbook entries for configuration reloads, network switching, crash recovery, updates, and DHCP-related events. More log information will continue to be added in future updates.

Official Channel: @SurgeTestFlightFeed

## 2026-04-15 [post 1517](https://t.me/SurgeTestFlight/1517)

#Mac #Beta

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

## 2026-04-12 [post 1515](https://t.me/SurgeTestFlight/1515)

#Mac #Beta

Version 6.5.0-10940 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10940-9676360eec5dcef73a9dc167b974a1b6.zip

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

## 2026-04-12 [post 1514](https://t.me/SurgeTestFlight/1514)

#Mac #Beta

Version 6.5.0-10930 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10930-45f078f470688e7c5f39783529bf732b.zip

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

## 2026-04-10 [post 1512](https://t.me/SurgeTestFlight/1512)

#Mac #Beta

Version 6.5.0-10900 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10900-f1e94b029707648e3ff4c4550b5c8c5c.zip

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

## 2026-04-09 [post 1511](https://t.me/SurgeTestFlight/1511)

#Mac #Beta

Version 6.5.0-10890 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10890-b105838e5d85aa0f489f07b845389fbd.zip

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

## 2026-04-08 [post 1510](https://t.me/SurgeTestFlight/1510)

#Mac #Beta

Version 6.5.0-10870 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10870-5f31de88b54de4d7d2947b8f68d9109c.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-04-07 [post 1509](https://t.me/SurgeTestFlight/1509)

#Mac #Beta

Version 6.5.0-10860 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10860-cf524fd25a1c0033d5409f038366c0f0.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-04-07 [post 1508](https://t.me/SurgeTestFlight/1508)

#Mac #Beta

Version 6.5.0-10850 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10850-d540eecd5be84fa2102889a4e8133323.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-31 [post 1507](https://t.me/SurgeTestFlight/1507)

#Mac #Beta

Version 6.5.0-10840 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10840-f9247486e710122880301ee612832d2c.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-23 [post 1506](https://t.me/SurgeTestFlight/1506)

#Mac #Beta

Version 6.5.0-10830 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10830-daf1bed20cfdd90d527c42eaec5ff340.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-20 [post 1505](https://t.me/SurgeTestFlight/1505)

#Mac #Beta

Version 6.5.0-10820 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10820-3d32a8a395d2d9f65e002f35d660ed5b.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-20 [post 1504](https://t.me/SurgeTestFlight/1504)

#Mac #Beta

Version 6.5.0-10810 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10810-8f6f78838d5d7027b11907f91d4f4408.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-20 [post 1503](https://t.me/SurgeTestFlight/1503)

#Mac #Beta

Version 6.5.0-10800 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10800-f61e79f5bc94ef4948c3ebd5370d0762.zip

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

Official Channel: @SurgeTestFlightFeed

## 2026-03-19 [post 1501](https://t.me/SurgeTestFlight/1501)

#Mac #Beta

Version 6.5.0-10790 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10790-556225d9490f87a58280c31041d4a4ac.zip

### Agent Skill
- Surge now fully supports AI agent skill operations. We have built in instructions on how to use surge-cli to operate Surge, and have fully exposed all capabilities of surge-cli. Tell the following to your agent that supports skills to use it: 

Install the skill from the /Applications/Surge.app/Contents/Resources/Skills/ directory using a symbolic link to ensure the skill can be updated along with the application bundle.
      
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

Official Channel: @SurgeTestFlightFeed

## 2026-03-17 [post 1500](https://t.me/SurgeTestFlight/1500)

#Mac #Beta

Version 6.5.0-10780 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10780-b45f729447792f80e45f74a99d4ab656.zip

### Agent Skill
- Surge now fully supports AI agent skill operations. We have built in instructions on how to use surge-cli to operate Surge, and have fully exposed all capabilities of surge-cli. Tell the following to your agent that supports skills to use it: 

Install the skill from the /Applications/Surge.app/Contents/Resources/Skills/ directory using a symbolic link to ensure the skill can be updated along with the application bundle.
      
### Other Improvements
- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-17 [post 1497](https://t.me/SurgeTestFlight/1497)

#Mac #Beta

Version 6.5.0-10770 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10770-45a1ff5691cc76d9188763f5f5dae0ea.zip

### Agent Skill
- Surge now fully supports AI agent skill operations. We have built in instructions on how to use surge-cli to operate Surge, and have fully exposed all capabilities of surge-cli. Tell the following to your agent that supports skills to use it: 

Install the skill from the /Applications/Surge.app/Contents/Resources/Skills/ directory using a symbolic link to ensure the skill can be updated along with the application bundle.
      
### Other Improvements
- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-11 [post 1494](https://t.me/SurgeTestFlight/1494)

#Mac #Beta

Version 6.5.0-10750 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10750-09733ed9fdc2afe2e6d9d0b12300249e.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-11 [post 1493](https://t.me/SurgeTestFlight/1493)

#Mac #Beta

Version 6.5.0-10740 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10740-b7d33bae7eb6e59559772ff440640487.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-10 [post 1492](https://t.me/SurgeTestFlight/1492)

#Mac #Beta

Version 6.5.0-10730 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10730-a2979ffebb2166887ba3e4d7d4fcce99.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-09 [post 1488](https://t.me/SurgeTestFlight/1488)

#Mac #Beta

Version 6.5.0-10710 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10710-ddc0ce239bb30640331288c4d3060ca6.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-08 [post 1487](https://t.me/SurgeTestFlight/1487)

#Mac #Beta

Version 6.5.0-10700 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10700-cc1bfb06288af4ba7befcac27acb566e.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-08 [post 1486](https://t.me/SurgeTestFlight/1486)

#Mac #Beta

Version 6.5.0-10690 https://dl.nssurge.com/mac/v6/Surge-6.5.0-10690-906e971c779e6527d8ac4452b2963da2.zip

- Added support for the X25519MLKEM768 post-quantum hybrid key exchange group for all TLS-related features (such as proxy clients and MITM), combining X25519 with ML-KEM-768 for quantum-resistant key exchange.

Official Channel: @SurgeTestFlightFeed

## 2026-03-03 [post 1483](https://t.me/SurgeTestFlight/1483)

#Mac #Beta

Version 6.4.4-10660 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10660-fab7cfc6bfb84df1424f90970adfcd6a.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-03-02 [post 1481](https://t.me/SurgeTestFlight/1481)

#Mac #Beta

Version 6.4.4-10650 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10650-7423881a7437fdf0cda427927d0c3edb.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-26 [post 1479](https://t.me/SurgeTestFlight/1479)

#Mac #Beta

Version 6.4.4-10640 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10640-6cd5452945d98abecd8f8f55e73d7d9f.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-25 [post 1475](https://t.me/SurgeTestFlight/1475)

#Mac #Beta

Version 6.4.4-10620 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10620-a5a44bce7dcc325e60b7daa05384113d.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-25 [post 1474](https://t.me/SurgeTestFlight/1474)

#Mac #Beta

Version 6.4.4-10610 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10610-9e98fec87ffacbe39a885c2d279c272b.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-25 [post 1473](https://t.me/SurgeTestFlight/1473)

#Mac #Beta

Version 6.4.4-10590 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10590-2e2845fd265b4b6110706ef1ad31078a.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-22 [post 1468](https://t.me/SurgeTestFlight/1468)

#Mac #Beta

Version 6.4.4-10530 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10530-8d3fd3de79cfd8f9aedb62ee989c7f5c.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Fixed an issue where AnyTLS could get stuck in reuse mode when used with certain servers.
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-22 [post 1467](https://t.me/SurgeTestFlight/1467)

#Mac #Beta

Version 6.4.4-10520 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10520-9052744fc1eb58a4128d89be27a5c96e.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-21 [post 1466](https://t.me/SurgeTestFlight/1466)

#Mac #Beta

Version 6.4.4-10500 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10500-34478612dfe6188c9fd667bbd60e7767.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
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

      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-02-17 [post 1463](https://t.me/SurgeTestFlight/1463)

#Mac #Beta

Version 6.4.4-10490 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10490-c66c575ce6802afa45745be7f25f16b5.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-27 [post 1462](https://t.me/SurgeTestFlight/1462)

#Mac #Beta

Version 6.4.4-10480 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10480-272f03c25ee5c362b63b13fcbb6203fe.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-27 [post 1461](https://t.me/SurgeTestFlight/1461)

#Mac #Beta

Version 6.4.4-10470 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10470-eaff8be423cf0caf3e0fe7e9da576d1a.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-27 [post 1460](https://t.me/SurgeTestFlight/1460)

#Mac #Beta

Version 6.4.4-10460 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10460-5f6306d5d6025d874e6db8134b67ff2b.zip

### Proxy Protocol
Experimental support for the Trust Tunnel proxy protocol, which is developed and maintained by AdGuard. (Although the project promotes Trust Tunnel as a VPN protocol, it is actually a proxy protocol.)
- This protocol is based on TLS, so all TLS-related parameters can be configured and used.
- Currently, only the HTTP/2 (TCP)-based operating mode is supported.
- UDP forwarding support has not been completed yet.

Configuration example: proxy = trust-tunnel, 192.168.20.62, 443, username=test, password=test
      
### Minor Improvements
- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-23 [post 1454](https://t.me/SurgeTestFlight/1454)

#Mac #Beta

Version 6.4.4-10430 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10430-e8b6d3df192031f900bc487846918938.zip

- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-22 [post 1452](https://t.me/SurgeTestFlight/1452)

#Mac #Beta

Version 6.4.4-10410 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10410-921dd28fc78826c7dadfcc4e6e03f4c2.zip

- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-21 [post 1451](https://t.me/SurgeTestFlight/1451)

#Mac #Beta

Version 6.4.4-10400 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10400-01b6997fea8279610d4cb0b97f214f85.zip

- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-21 [post 1450](https://t.me/SurgeTestFlight/1450)

#Mac #Beta

Version 6.4.4-10390 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10390-9f22a48c86fb2ef82cc6a22e07b5ea8e.zip

- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-20 [post 1448](https://t.me/SurgeTestFlight/1448)

#Mac #Beta

Version 6.4.4-10370 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10370-555cba23b8418251a178e07497c06148.zip

- Support drag-and-drop reordering on the proxy view.
- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-18 [post 1446](https://t.me/SurgeTestFlight/1446)

#Mac #Beta

Version 6.4.4-10350 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10350-1ff9f7d2f400122645c6ce6b1f53204e.zip

- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-17 [post 1445](https://t.me/SurgeTestFlight/1445)

#Mac #Beta

Version 6.4.4-10340 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10340-63fbfad7f6904e7bc45b5722d152e1bd.zip

- Fix the issue where the related statistics for the DIRECT policy were not saved correctly.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-01-17 [post 1444](https://t.me/SurgeTestFlight/1444)

#Mac #Beta

Version 6.4.4-10330 https://dl.nssurge.com/mac/v6/Surge-6.4.4-10330-bf89b626fab6c0ec338be4d99f5d5b2a.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-01-13 [post 1439](https://t.me/SurgeTestFlight/1439)

#Mac #Beta

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

## 2026-01-12 [post 1435](https://t.me/SurgeTestFlight/1435)

#Mac #Beta

Version 6.4.3-10280 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10280-010d9a1471b6488bb93c73dd51861010.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

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

Official Channel: @SurgeTestFlightFeed

## 2026-01-09 [post 1432](https://t.me/SurgeTestFlight/1432)

#Mac #Beta

Version 6.4.3-10260 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10260-f56c5649d79387b4acc485f975f3ea93.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

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

Official Channel: @SurgeTestFlightFeed

## 2026-01-06 [post 1424](https://t.me/SurgeTestFlight/1424)

#Mac #Beta

Version 6.4.3-10250 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10250-afa8a322914c9e90cf630808045961db.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- When you hold down the Option key and click the Surge main menu, hidden policy groups will now be displayed.
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2026-01-05 [post 1422](https://t.me/SurgeTestFlight/1422)

#Mac #Beta

Version 6.4.3-10240 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10240-363e4cbb7f707300ec99c79edae8fc09.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- When you hold down the Option key and click the Surge main menu, hidden policy groups will now be displayed.
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2026-01-02 [post 1419](https://t.me/SurgeTestFlight/1419)

#Mac #Beta

Version 6.4.3-10220 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10220-e10800eedca2c34abb5b06b832643c05.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- When you hold down the Option key and click the Surge main menu, hidden policy groups will now be displayed.
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-31 [post 1417](https://t.me/SurgeTestFlight/1417)

#Mac #Beta

Version 6.4.3-10210 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10210-2bcb4e02bf78717af0219f5087791ba4.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-30 [post 1416](https://t.me/SurgeTestFlight/1416)

#Mac #Beta

Version 6.4.3-10200 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10200-8e3b55fad0f4a5f74475f09c6ee544ea.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-30 [post 1415](https://t.me/SurgeTestFlight/1415)

#Mac #Beta

Version 6.4.3-10190 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10190-ca2103315efbd0bdb186d00755c67a95.zip

      
### Proxy Protocol
- Support for a new proxy protocol: AnyTLS.
- Supports Salamander obfuscation mode of Hysteria 2, with the configuration parameter salamander-password.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-30 [post 1414](https://t.me/SurgeTestFlight/1414)

#Mac #Beta

Version 6.4.3-10180 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10180-158a9d382f10c8e0154955007bed08b4.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-29 [post 1413](https://t.me/SurgeTestFlight/1413)

#Mac #Beta

Version 6.4.3-10170 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10170-2f7dba9709391360e904f7bb73f18730.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-29 [post 1412](https://t.me/SurgeTestFlight/1412)

#Mac #Beta

Version 6.4.3-10160 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10160-fffd9871a107f0187549d30029cac117.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-29 [post 1410](https://t.me/SurgeTestFlight/1410)

#Mac #Beta

Version 6.4.3-10150 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10150-42176d523517abb8b66a743ab6b6fac2.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-27 [post 1409](https://t.me/SurgeTestFlight/1409)

#Mac #Beta

Version 6.4.3-10130 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10130-62acf1fd9762bf4c6a838a44292c2dca.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-26 [post 1408](https://t.me/SurgeTestFlight/1408)

#Mac #Beta

Version 6.4.3-10120 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10120-cdd62c65d3b3d8cddf92d88be4e8c368.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-25 [post 1407](https://t.me/SurgeTestFlight/1407)

#Mac #Beta

Version 6.4.3-10110 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10110-4074dc81cd2830dedb59ff9840e9eaf1.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-25 [post 1406](https://t.me/SurgeTestFlight/1406)

#Mac #Beta

Version 6.4.3-10100 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10100-214278e53141606d726b9865116db93a.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-24 [post 1404](https://t.me/SurgeTestFlight/1404)

#Mac #Beta

Version 6.4.3-10090 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10090-775cddd539e984a1da67878b78066318.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-24 [post 1403](https://t.me/SurgeTestFlight/1403)

#Mac #Beta

Version 6.4.3-10080 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10080-15576961b5db4f0208a0d7ae0bf8f5d3.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-24 [post 1402](https://t.me/SurgeTestFlight/1402)

#Mac #Beta

Version 6.4.3-10070 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10070-77b0ef29cd53e2fbb26dd1092a20c6ba.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-24 [post 1401](https://t.me/SurgeTestFlight/1401)

#Mac #Beta

Version 6.4.3-10060 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10060-7a44e5b079b54d46ce82bd5ff8f20adf.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-23 [post 1400](https://t.me/SurgeTestFlight/1400)

#Mac #Beta

Version 6.4.3-10050 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10050-2c1859dbedc06c9214d918499ba1b190.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-18 [post 1398](https://t.me/SurgeTestFlight/1398)

#Mac #Beta

Version 6.4.3-10040 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10040-d30e379c8b6e8c3e5d979e8f8ea884c8.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### Proxy Editing Improvements
- You can now directly test whether the current proxy parameters are correct during the process of editing the proxy.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-17 [post 1397](https://t.me/SurgeTestFlight/1397)

#Mac #Beta

Version 6.4.3-10030 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10030-8d634f55aa3de68e7c1b3b1bbfd9c151.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-17 [post 1396](https://t.me/SurgeTestFlight/1396)

#Mac #Beta

Version 6.4.3-10020 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10020-aa82f13002fa2689b195cfb65c90ae65.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

### Dashboard Improvements
- Enhanced the Host view of the request list. Now all IP address requests can be viewed grouped by AS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-16 [post 1394](https://t.me/SurgeTestFlight/1394)

#Mac #Beta

Version 6.4.3-10010 https://dl.nssurge.com/mac/v6/Surge-6.4.3-10010-7e4106410b77670b05d1312b8d3c1044.zip

      
### New Proxy Protocol
- Support for a new proxy protocol: AnyTLS.

### New DNS Mapping Keyword
- Added the force-syslib keyword for DNS mapping.
- The original system and syslib keywords have exactly the same effect: when enhanced mode is not enabled, the system library will be used for resolution; when enhanced mode is enabled, Surge will perform resolution using the system's DNS server.
- When using the force-syslib keyword, the system library will be used for resolution regardless of whether enhanced mode is enabled. Please note that this may cause recursive request issues. This option is designed for special domains such as mDNS; do not configure this parameter for general domains.

Official Channel: @SurgeTestFlightFeed

## 2025-12-15 [post 1392](https://t.me/SurgeTestFlight/1392)

#Mac #Beta

Version 6.4.3-9980 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9980-02000b3f874075cd978abb9bc3d14359.zip

- Support for a new proxy protocol: AnyTLS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-14 [post 1391](https://t.me/SurgeTestFlight/1391)

#Mac #Beta

Version 6.4.3-9960 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9960-5a7e6a4f6fe698619f13e0b08f1c24a3.zip

- Support for a new proxy protocol: AnyTLS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1389](https://t.me/SurgeTestFlight/1389)

#Mac #Beta

Version 6.4.3-9940 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9940-65717ff7291c193e0006f80f26bc8c04.zip

- Support for a new proxy protocol: AnyTLS.

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1388](https://t.me/SurgeTestFlight/1388)

#Mac #Beta

Version 6.4.3-9930 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9930-59e7a088cc8e79dbefc69b845df421b1.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1386](https://t.me/SurgeTestFlight/1386)

#Mac #Beta

Version 6.4.3-9920 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9920-d91d673f5ff701165c0720947ea6daae.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1385](https://t.me/SurgeTestFlight/1385)

#Mac #Beta

Version 6.4.3-9900 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9900-f0aa43af50cb302627728fd7a359ab42.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1384](https://t.me/SurgeTestFlight/1384)

#Mac #Beta

Version 6.4.3-9890 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9890-b87298bdb6abd4331a9abd6c492cf099.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1383](https://t.me/SurgeTestFlight/1383)

#Mac #Beta

Version 6.4.3-9880 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9880-85a0db062b265532f6957d189771aad8.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1379](https://t.me/SurgeTestFlight/1379)

#Mac #Beta

Version 6.4.3-9870 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9870-b921bd629a355bd6e3c733fb619d41d7.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1377](https://t.me/SurgeTestFlight/1377)

#Mac #Beta

Version 6.4.3-9860 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9860-0040bcba42e7b8058b41f515e5b9458f.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1376](https://t.me/SurgeTestFlight/1376)

#Mac #Beta

Version 6.4.3-9850 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9850-8205ce1cd27c8f041e6a4c573c6432a3.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1375](https://t.me/SurgeTestFlight/1375)

#Mac #Beta

Version 6.4.3-9840 https://dl.nssurge.com/mac/v6/Surge-6.4.3-9840-ee829ce15d68893362421d7d34bc9551.zip

- Support for a new proxy protocol: AnyTLS. (UDP forwarding support is not yet complete)

Official Channel: @SurgeTestFlightFeed

## 2025-12-07 [post 1370](https://t.me/SurgeTestFlight/1370)

#Mac #Beta

Version 6.4.2-9830 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9830-28a1025189d49a3f938384b58c8f5000.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- IPv6 RA override no longer broadcasts new DNS addresses to ensure maximum compatibility.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-12-06 [post 1368](https://t.me/SurgeTestFlight/1368)

#Mac #Beta

Version 6.4.2-9820 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9820-34d7c00d44c1e26aca3c36112d9520db.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-12-01 [post 1367](https://t.me/SurgeTestFlight/1367)

#Mac #Beta

Version 6.4.2-9810 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9810-b9037f0af18a6d84482c1c9cd3add718.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-12-01 [post 1366](https://t.me/SurgeTestFlight/1366)

#Mac #Beta

Version 6.4.2-9780 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9780-89926b8042ffb1b00a487b9d2ce349bb.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-12-01 [post 1365](https://t.me/SurgeTestFlight/1365)

#Mac #Beta

Version 6.4.2-9770 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9770-c18fecdc5cad4ab45aaa011a928e340c.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-29 [post 1364](https://t.me/SurgeTestFlight/1364)

#Mac #Beta

Version 6.4.2-9750 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9750-6a4c0fc586357469b6eceed4b985999b.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-27 [post 1363](https://t.me/SurgeTestFlight/1363)

#Mac #Beta

Version 6.4.2-9740 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9740-480d1aabfbec8377963608c31fb4975b.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Adjusted the storage mechanism for traffic statistics. In previous versions, changes to a policy's configuration caused the policy's traffic statistics to be reset. Now, traffic statistics rely solely on the policy name (and the policy group name for external policies), so modifying the configuration will no longer result in the loss of statistical data.
- Surge Enterprise is being renamed to Surge Team, which will be used for team licensing and profile management. We will provide more information later.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-25 [post 1362](https://t.me/SurgeTestFlight/1362)

#Mac #Beta

Version 6.4.2-9730 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9730-91d68ee7bc915bf1115021f5e1bf40ed.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-24 [post 1361](https://t.me/SurgeTestFlight/1361)

#Mac #Beta

Version 6.4.2-9720 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9720-7bf7c768eac7feb460a491b791121c54.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-20 [post 1358](https://t.me/SurgeTestFlight/1358)

#Mac #Beta

Version 6.4.2-9710 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9710-c4dc7dbdf8c00b2ae18803f12bbd0e21.zip

- It is now possible to enable or disable the UDP Fast Path feature for individual devices.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-18 [post 1356](https://t.me/SurgeTestFlight/1356)

#Mac #Beta

Version 6.4.2-9700 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9700-a0f71a60a6a2aedfbfa4b29baf3a1cc3.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-17 [post 1355](https://t.me/SurgeTestFlight/1355)

#Mac #Beta

Version 6.4.2-9690 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9690-443d9bb9d36b75512cfe90e8f4afde8d.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-15 [post 1354](https://t.me/SurgeTestFlight/1354)

#Mac #Beta

Version 6.4.2-9680 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9680-ebf0d456c5581eeec880995f6bfe8205.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-15 [post 1353](https://t.me/SurgeTestFlight/1353)

#Mac #Beta

Version 6.4.2-9670 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9670-be6806b07ea3e36e5de65d48826c612e.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-14 [post 1352](https://t.me/SurgeTestFlight/1352)

#Mac #Beta

Version 6.4.2-9650 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9650-f91bf815720aff697296d7c6a9ab4d46.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-13 [post 1351](https://t.me/SurgeTestFlight/1351)

#Mac #Beta

Version 6.4.2-9640 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9640-d8c59f6a10986bf7a9b79c131fa2a7e1.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-12 [post 1349](https://t.me/SurgeTestFlight/1349)

#Mac #Beta

Version 6.4.2-9630 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9630-25e77a0f5c5b851a3534f3c6071e0bdf.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-12 [post 1348](https://t.me/SurgeTestFlight/1348)

#Mac #Beta

Version 6.4.2-9620 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9620-16e439a008b308d1174330b1d1213e32.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-08 [post 1345](https://t.me/SurgeTestFlight/1345)

#Mac #Beta

Version 6.4.2-9610 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9610-d12e7bcf8bb1604aa9ca74d15b7a38df.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-07 [post 1343](https://t.me/SurgeTestFlight/1343)

#Mac #Beta

Version 6.4.2-9590 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9590-62deece0523cd52cfa923cd7559a5b28.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-07 [post 1342](https://t.me/SurgeTestFlight/1342)

#Mac #Beta

Version 6.4.2-9580 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9580-bb16239cac61373a4338d2362a27c9d1.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-07 [post 1341](https://t.me/SurgeTestFlight/1341)

#Mac #Beta

Version 6.4.2-9570 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9570-dc6edaeb695f61c3394edd40518156f3.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-07 [post 1340](https://t.me/SurgeTestFlight/1340)

#Mac #Beta

Version 6.4.2-9560 https://dl.nssurge.com/mac/v6/Surge-6.4.2-9560-00d6733638787c4da5faac3be99a36b8.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-11-05 [post 1337](https://t.me/SurgeTestFlight/1337)

#Mac #Beta

Version 6.4.1-9550 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9550-d5ca6e6585c0a68908898b04d45e846e.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-11-04 [post 1336](https://t.me/SurgeTestFlight/1336)

#Mac #Beta

Version 6.4.1-9540 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9540-ff70b8d06aad8e6c1c8537c3c9f2d3c6.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-11-04 [post 1335](https://t.me/SurgeTestFlight/1335)

#Mac #Beta

Version 6.4.1-9530 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9530-c96af181824999b9dcb529bd528a08c9.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-11-03 [post 1334](https://t.me/SurgeTestFlight/1334)

#Mac #Beta

Version 6.4.1-9520 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9520-1bbbe29cc2489629bb51c6e5ffb3f2a1.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-11-01 [post 1333](https://t.me/SurgeTestFlight/1333)

#Mac #Beta

Version 6.4.1-9500 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9500-cd2e099aed4768e8af294c790bb8af5b.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-11-01 [post 1332](https://t.me/SurgeTestFlight/1332)

#Mac #Beta

Version 6.4.1-9480 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9480-01254dbdb5b0ba1a21dfd51ff5a95de9.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-31 [post 1331](https://t.me/SurgeTestFlight/1331)

#Mac #Beta

Version 6.4.1-9470 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9470-d2d2df4582e8459d0c931c5725e68b97.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-31 [post 1330](https://t.me/SurgeTestFlight/1330)

#Mac #Beta

Version 6.4.1-9460 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9460-bfb4446b7a94ffc5c214faf924bc776f.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-30 [post 1329](https://t.me/SurgeTestFlight/1329)

#Mac #Beta

Version 6.4.1-9450 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9450-7896339640edbe687f08974260053e8f.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-30 [post 1328](https://t.me/SurgeTestFlight/1328)

#Mac #Beta

Version 6.4.1-9440 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9440-d0f0dcbbf91de8fadbf388028e95fc82.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-30 [post 1326](https://t.me/SurgeTestFlight/1326)

#Mac #Beta

Version 6.4.1-9430 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9430-89ae710a6648ff6d359b28e0eb352c6c.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-29 [post 1325](https://t.me/SurgeTestFlight/1325)

#Mac #Beta

Version 6.4.1-9420 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9420-b5a2d38cc952851b0880bcdafd5b73fb.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-29 [post 1324](https://t.me/SurgeTestFlight/1324)

#Mac #Beta

Version 6.4.1-9390 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9390-6f6cb7d6fca05224c12d15320ee14d2f.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-29 [post 1323](https://t.me/SurgeTestFlight/1323)

#Mac #Beta

Version 6.4.1-9380 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9380-cf94425c4185840f32cbf90adacfc80a.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-28 [post 1322](https://t.me/SurgeTestFlight/1322)

#Mac #Beta

Version 6.4.1-9370 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9370-1ca5b5bd7ba7947ef0ab1182e30ed88f.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-28 [post 1321](https://t.me/SurgeTestFlight/1321)

#Mac #Beta

Version 6.4.1-9360 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9360-6fc898399418f121466d7886de2da4e2.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-28 [post 1320](https://t.me/SurgeTestFlight/1320)

#Mac #Beta

Version 6.4.1-9350 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9350-f2db6b63fb9fd18e6fc8c6434be548a7.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-27 [post 1319](https://t.me/SurgeTestFlight/1319)

#Mac #Beta

Version 6.4.1-9340 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9340-297349e122f4ddd068c9372121b587c3.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-27 [post 1318](https://t.me/SurgeTestFlight/1318)

#Mac #Beta

Version 6.4.1-9330 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9330-4c3b5238732c791516ef314cd9701e2f.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-26 [post 1317](https://t.me/SurgeTestFlight/1317)

#Mac #Beta

Version 6.4.1-9320 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9320-329be6f0f4106b2e7931faa5288babe3.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-26 [post 1316](https://t.me/SurgeTestFlight/1316)

#Mac #Beta

Version 6.4.1-9310 https://dl.nssurge.com/mac/v6/Surge-6.4.1-9310-64b0b62301b0c73a8fc2c68d0c4d3395.zip

- Improved the stability of the UDP Fast Path, preventing previous UDP connections from being affected by fast path fallback.

Official Channel: @SurgeTestFlightFeed

## 2025-10-23 [post 1312](https://t.me/SurgeTestFlight/1312)

#Mac #Beta

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

## 2025-10-23 [post 1311](https://t.me/SurgeTestFlight/1311)

#Mac #Beta

Version 6.4.0-9280 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9280-3cf751e5975530b1bf6fb604d1174f0c.zip

      
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

## 2025-10-23 [post 1308](https://t.me/SurgeTestFlight/1308)

#Mac #Beta

Version 6.4.0-9270 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9270-d59aed01a719676611307b8d0dba8966.zip

      
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

## 2025-10-22 [post 1307](https://t.me/SurgeTestFlight/1307)

#Mac #Beta

Version 6.4.0-9260 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9260-a86a86af2a2dee59df62a7c2a6f6a30c.zip

      
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

## 2025-10-22 [post 1306](https://t.me/SurgeTestFlight/1306)

#Mac #Beta

Version 6.4.0-9250 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9250-32cb220675f9a4d0076d73fa3fa71999.zip

      
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

## 2025-10-22 [post 1305](https://t.me/SurgeTestFlight/1305)

#Mac #Beta

Version 6.4.0-9220 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9220-c67115a0eb942e3c108617cec1fa1c40.zip

      
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

## 2025-10-22 [post 1304](https://t.me/SurgeTestFlight/1304)

#Mac #Beta

Version 6.4.0-9200 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9200-09540bed6218b65f1d7cbb3ebcfb2137.zip

      
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

## 2025-10-22 [post 1303](https://t.me/SurgeTestFlight/1303)

#Mac #Beta

Version 6.4.0-9190 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9190-877ff19884ec229a25a760d1ce73c989.zip

      
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

## 2025-10-22 [post 1302](https://t.me/SurgeTestFlight/1302)

#Mac #Beta

Version 6.4.0-9170 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9170-83937451b8f95d2d0dc3944ee0421916.zip

      
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

## 2025-10-22 [post 1301](https://t.me/SurgeTestFlight/1301)

#Mac #Beta

Version 6.4.0-9150 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9150-0b6966dd1f293dcf84df62a49d3932d6.zip

      
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

## 2025-10-22 [post 1300](https://t.me/SurgeTestFlight/1300)

#Mac #Beta

Version 6.4.0-9130 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9130-ff9ef88a1dab22f76e8528be00097597.zip

      
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

## 2025-10-21 [post 1299](https://t.me/SurgeTestFlight/1299)

#Mac #Beta

Version 6.4.0-9120 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9120-56e56646702b107921a207afaefefbcc.zip

      
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

## 2025-10-21 [post 1298](https://t.me/SurgeTestFlight/1298)

#Mac #Beta

Version 6.4.0-9110 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9110-5a6dfa30f3a7ffad601d3dcc2dc5c255.zip

      
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

## 2025-10-21 [post 1297](https://t.me/SurgeTestFlight/1297)

#Mac #Beta

Version 6.4.0-9070 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9070-bfb2951f62fc6a6c8223cf2875fe14a0.zip

      
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

## 2025-10-21 [post 1296](https://t.me/SurgeTestFlight/1296)

#Mac #Beta

Version 6.4.0-9060 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9060-1fe344b430fc92f74b1faa9d9bd4fb26.zip

      
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

## 2025-10-21 [post 1295](https://t.me/SurgeTestFlight/1295)

#Mac #Beta

Version 6.4.0-9050 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9050-53968b6ad894aa45ddaf5e9e4d7c7c24.zip

      
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

## 2025-10-20 [post 1293](https://t.me/SurgeTestFlight/1293)

#Mac #Beta

Version 6.4.0-9030 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9030-b8de8b441724758b5f89fed2f402c3da.zip

      
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

## 2025-10-20 [post 1292](https://t.me/SurgeTestFlight/1292)

#Mac #Beta

Version 6.4.0-9020 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9020-52df71aced1918ac15b3d5d2622c099e.zip

      
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

## 2025-10-17 [post 1291](https://t.me/SurgeTestFlight/1291)

#Mac #Beta

Version 6.4.0-9010 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9010-d514618d040be48b8f2c5c1c950497f5.zip

      
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

## 2025-10-16 [post 1290](https://t.me/SurgeTestFlight/1290)

#Mac #Beta

Version 6.4.0-9000 https://dl.nssurge.com/mac/v6/Surge-6.4.0-9000-ceb9873bcce2e7014918f5121ed39e05.zip

      
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

## 2025-10-15 [post 1289](https://t.me/SurgeTestFlight/1289)

#Mac #Beta

Version 6.4.0-8990 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8990-c98427f189d4213bf4e2cd9ab6a8e4ff.zip

      
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

## 2025-10-15 [post 1288](https://t.me/SurgeTestFlight/1288)

#Mac #Beta

Version 6.4.0-8980 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8980-539d5ef48167b2a43d773f33779d0fd8.zip

      
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

## 2025-10-14 [post 1287](https://t.me/SurgeTestFlight/1287)

#Mac #Beta

Version 6.4.0-8970 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8970-6dbd3dcfbb102df7415ef8b2fb7d8c47.zip

      
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

## 2025-10-13 [post 1285](https://t.me/SurgeTestFlight/1285)

#Mac #Beta

Version 6.4.0-8960 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8960-4399f6542e154fe4542f350711344aab.zip

      
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

## 2025-10-11 [post 1284](https://t.me/SurgeTestFlight/1284)

#Mac #Beta

Version 6.4.0-8940 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8940-58cad7c360d969dc3bf9ee3c2536e980.zip

      
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

## 2025-10-11 [post 1283](https://t.me/SurgeTestFlight/1283)

#Mac #Beta

Version 6.4.0-8930 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8930-6d244fe2102931705e38368a0c1ceacc.zip

      
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

## 2025-10-10 [post 1282](https://t.me/SurgeTestFlight/1282)

#Mac #Beta

Version 6.4.0-8920 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8920-711f940f8c4365db2df92773ec42448e.zip

      
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

## 2025-10-10 [post 1281](https://t.me/SurgeTestFlight/1281)

#Mac #Beta

Version 6.4.0-8910 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8910-d9446957389ace4f075c99a244cbe571.zip

      
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

## 2025-10-10 [post 1280](https://t.me/SurgeTestFlight/1280)

#Mac #Beta

Version 6.4.0-8900 https://dl.nssurge.com/mac/v6/Surge-6.4.0-8900-bd228c5959d502e610ca7c1af69d5f25.zip

      
### Surge Gateway VM UDP Fast Path
      
Currently, when using Surge in gateway mode to take over a device, if P2P applications (such as BT downloads, game installers, live streaming, etc.) are used on the device, it may result in a large number of connections appearing in the Dashboard, slowing down overall speed. If the number of connections is extremely high, it may even exhaust system resources and force Surge to restart.

The cause of this issue is that Surge operates as a layer 4 proxy, and for every UDP packet with a different quadruple, it needs to be handled as a new connection. For most applications, even if UDP is used, only a few logical connections are typically generated, so the overhead is completely acceptable. However, for P2P applications, nearly a thousand logical connections may be generated within a few seconds.

Therefore, this version introduces a UDP Fast Path defense mechanism. When a client initiates a large number of UDP connections in a short period of time (10 within 1 second or 30 within 10 seconds), UDP Fast Path will be enabled for that client, downgrading UDP packet processing to L3. In this mode, performance is extremely high, far exceeding the physical network card speed limit, so there is no longer a need to worry about resource consumption issues.

Additionally:

1. Packets under UDP Fast Path will be forwarded directly and cannot go through the proxy.
2. For UDP packets with a destination port number less than 1024, they will always be forwarded using the normal processing mode to avoid affecting regular applications.

## Bug Fixes

- Fix the issue where the HTTP engine might get stuck when handling consecutive requests.
- Fixed the issue where using Snell v3 to carry UDP traffic could cause a crash.

Official Channel: @SurgeTestFlightFeed

## 2025-10-10 [post 1276](https://t.me/SurgeTestFlight/1276)

#Mac #Beta

Version 6.3.2-8890 https://dl.nssurge.com/mac/v6/Surge-6.3.2-8890-2d31afb9794ea1298f3901402dd1c33e.zip

- Fix the issue where the HTTP engine might get stuck when handling consecutive requests.
- Fixed the issue where using Snell v3 to carry UDP traffic could cause a crash.

Official Channel: @SurgeTestFlightFeed

## 2025-10-09 [post 1275](https://t.me/SurgeTestFlight/1275)

#Mac #Beta

Version 6.3.2-8880 https://dl.nssurge.com/mac/v6/Surge-6.3.2-8880-394ae901028d46e6eef68820a0f44fe9.zip

- Fix the issue where the HTTP engine might get stuck when handling consecutive requests..

Official Channel: @SurgeTestFlightFeed

## 2025-10-05 [post 1272](https://t.me/SurgeTestFlight/1272)

#Mac #Beta

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

## 2025-10-04 [post 1270](https://t.me/SurgeTestFlight/1270)

#Mac #Beta

Version 6.3.1-8850 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8850-337b65abbca1ccfcc9d060bc8fba6103.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-10-04 [post 1269](https://t.me/SurgeTestFlight/1269)

#Mac #Beta

Version 6.3.1-8840 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8840-db658166999d0f4087466fd55366bef4.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-30 [post 1267](https://t.me/SurgeTestFlight/1267)

#Mac #Beta

Version 6.3.1-8830 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8830-ed2d8e2e236d0c73c384380d35b697b4.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-29 [post 1264](https://t.me/SurgeTestFlight/1264)

#Mac #Beta

Version 6.3.1-8810 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8810-9078652a5236b7beb566ed7e41761af3.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-29 [post 1262](https://t.me/SurgeTestFlight/1262)

#Mac #Beta

Version 6.3.1-8790 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8790-6dec2fa590fab8a8a6ad16a5b67cf8dd.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-27 [post 1261](https://t.me/SurgeTestFlight/1261)

#Mac #Beta

Version 6.3.1-8740 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8740-b13dcf4789f69e9c5267dc89548b0ee7.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-26 [post 1260](https://t.me/SurgeTestFlight/1260)

#Mac #Beta

Version 6.3.1-8730 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8730-eb2a897a4324ac013edce3b637fdf963.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-26 [post 1258](https://t.me/SurgeTestFlight/1258)

#Mac #Beta

Version 6.3.1-8720 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8720-97cdfb51d749b2b3babe7bcc6a294670.zip

- The proxy diagnostic tool has added upload and download bandwidth testing.
- According to mainstream operating system conventions, adjust all traffic and statistics from a 1024 base to a 1000 base.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-26 [post 1255](https://t.me/SurgeTestFlight/1255)

#Mac #Beta

Version 6.3.1-8710 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8710-bebec8b1de819a09123105c35059f247.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-23 [post 1254](https://t.me/SurgeTestFlight/1254)

#Mac #Beta

Version 6.3.1-8700 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8700-c57b6cec192b4792dcb3723d88124ebd.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-22 [post 1251](https://t.me/SurgeTestFlight/1251)

#Mac #Beta

Version 6.3.1-8670 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8670-7c895db1ac51ea8e30e82749694a28b5.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-19 [post 1250](https://t.me/SurgeTestFlight/1250)

#Mac #Beta

Version 6.3.1-8630 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8630-e1b76d3a0ac496ff76cd566c068ee15a.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-19 [post 1249](https://t.me/SurgeTestFlight/1249)

#Mac #Beta

Version 6.3.1-8610 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8610-93729cedff2daa166d76665b55879507.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-18 [post 1248](https://t.me/SurgeTestFlight/1248)

#Mac #Beta

Version 6.3.1-8600 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8600-dd9fdda161c4ffde7920fa611aaf74d4.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-18 [post 1247](https://t.me/SurgeTestFlight/1247)

#Mac #Beta

Version 6.3.1-8590 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8590-e11f827a8faf3f5ab9ba2519ca1b00ea.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-17 [post 1246](https://t.me/SurgeTestFlight/1246)

#Mac #Beta

Version 6.3.1-8580 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8580-b8cde36cb8003a9fd8d992acf0733920.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-17 [post 1245](https://t.me/SurgeTestFlight/1245)

#Mac #Beta

Version 6.3.1-8570 https://dl.nssurge.com/mac/v6/Surge-6.3.1-8570-0b351cd235768ecc35c38d72de866f32.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-11 [post 1235](https://t.me/SurgeTestFlight/1235)

#Mac #Beta

Version 6.3.0-8560 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8560-e2722a66aa0ecc9dd60c3e8707aae567.zip

- Preliminary adaptation for macOS 26 completed.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-10 [post 1233](https://t.me/SurgeTestFlight/1233)

#Mac #Beta

Version 6.3.0-8550 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8550-d4baa0435a45d4f6ed944cd46c1e2897.zip

- Preliminary adaptation for macOS 26 completed.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-09 [post 1232](https://t.me/SurgeTestFlight/1232)

#Mac #Beta

Version 6.3.0-8500 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8500-8904e4b30264b6eb1967345dbd1f3bad.zip

- Preliminary adaptation for macOS 26 completed.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-09 [post 1231](https://t.me/SurgeTestFlight/1231)

#Mac #Beta

Version 6.3.0-8460 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8460-b5fa8fbd1b2d9d5ea84a7afafe2c5dd6.zip

- Preliminary adaptation for macOS 26 completed.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-09 [post 1230](https://t.me/SurgeTestFlight/1230)

#Mac #Beta

Version 6.3.0-8450 https://dl.nssurge.com/mac/v6/Surge-6.3.0-8450-e328d2078f6504a68b8891a2835a54cc.zip

- Preliminary adaptation for macOS 26 completed.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-06 [post 1227](https://t.me/SurgeTestFlight/1227)

#Mac #Beta

Version 6.2.1-8440 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8440-fffd43aba0a1fcd032b4cd9426d9e0c0.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-06 [post 1226](https://t.me/SurgeTestFlight/1226)

#Mac #Beta

Version 6.2.1-8430 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8430-8ceb03bf5e5f468cfe133b5bdf697e2e.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-05 [post 1224](https://t.me/SurgeTestFlight/1224)

#Mac #Beta

Version 6.2.1-8420 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8420-cd3e23c3803e1aa28f8171f6500fdb89.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-05 [post 1223](https://t.me/SurgeTestFlight/1223)

#Mac #Beta

Version 6.2.1-8410 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8410-9c1f61715bf4bcade917e596396b2b5f.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-05 [post 1222](https://t.me/SurgeTestFlight/1222)

#Mac #Beta

Version 6.2.1-8400 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8400-693f396c8d5cbdc3991eb43a35242a8c.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-02 [post 1220](https://t.me/SurgeTestFlight/1220)

#Mac #Beta

Version 6.2.1-8380 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8380-ab8e2ee2e94486a72807d168aa1b007c.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-09-02 [post 1219](https://t.me/SurgeTestFlight/1219)

#Mac #Beta

Version 6.2.1-8370 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8370-9ff3d004fa5ece6d3063b8ee0ada6527.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-15 [post 1216](https://t.me/SurgeTestFlight/1216)

#Mac #Beta

Version 6.2.1-8350 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8350-9334c3664590ea46cc1d4bbf4b4be133.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-14 [post 1213](https://t.me/SurgeTestFlight/1213)

#Mac #Beta

Version 6.2.1-8340 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8340-1bcf9d62548f4fc54c7ed6ecbdcb1748.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-12 [post 1209](https://t.me/SurgeTestFlight/1209)

#Mac #Beta

Version 6.2.1-8330 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8330-345b28cb7bde49b2a024d320a3376048.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-11 [post 1205](https://t.me/SurgeTestFlight/1205)

#Mac #Beta

Version 6.2.1-8320 https://dl.nssurge.com/mac/v6/Surge-6.2.1-8320-425ea3dac6f00e5f3c706b972de01245.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-08-07 [post 1201](https://t.me/SurgeTestFlight/1201)

#Mac #Beta

Version 6.2.0-8310 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8310-710082409fef1dc8f4011dd74697969c.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-06 [post 1199](https://t.me/SurgeTestFlight/1199)

#Mac #Beta

Version 6.2.0-8300 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8300-67d9e93ecd229d021746d540dc02ca8c.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-05 [post 1196](https://t.me/SurgeTestFlight/1196)

#Mac #Beta

Version 6.2.0-8290 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8290-4e8c9ad586c09acad5d3750b942af602.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-04 [post 1195](https://t.me/SurgeTestFlight/1195)

#Mac #Beta

Version 6.2.0-8280 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8280-e9e76f1407dc4461dfc5f636b8063556.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-04 [post 1194](https://t.me/SurgeTestFlight/1194)

#Mac #Beta

Version 6.2.0-8270 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8270-2f13e81514068f6dc6b6bc6b4a9a8d8c.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-04 [post 1193](https://t.me/SurgeTestFlight/1193)

#Mac #Beta

Version 6.2.0-8260 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8260-d9de85529b41342b9009942d70fbd398.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-03 [post 1192](https://t.me/SurgeTestFlight/1192)

#Mac #Beta

Version 6.2.0-8250 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8250-bf8ae3d1f90748382c064a1a135129f3.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-03 [post 1191](https://t.me/SurgeTestFlight/1191)

#Mac #Beta

Version 6.2.0-8240 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8240-40d72693bb61c4bdbbb6acff81413bb8.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-02 [post 1190](https://t.me/SurgeTestFlight/1190)

#Mac #Beta

Version 6.2.0-8220 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8220-ea91cf50c2602510a9cd6e209bc84625.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-01 [post 1189](https://t.me/SurgeTestFlight/1189)

#Mac #Beta

Version 6.2.0-8210 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8210-9a19bf76fbd0a4cc1430e4429e8ca616.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-08-01 [post 1188](https://t.me/SurgeTestFlight/1188)

#Mac #Beta

Version 6.2.0-8190 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8190-3d7166b3875f5b1c745530f1377af246.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-31 [post 1187](https://t.me/SurgeTestFlight/1187)

#Mac #Beta

Version 6.2.0-8180 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8180-7723def6a26c3412365eed2fe1399224.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1186](https://t.me/SurgeTestFlight/1186)

#Mac #Beta

Version 6.2.0-8160 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8160-0b9fdfac08cdb0694bfe752679bf86fd.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1185](https://t.me/SurgeTestFlight/1185)

#Mac #Beta

Version 6.2.0-8150 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8150-9dd6038c464a1b36a93d2e576cc266b5.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1184](https://t.me/SurgeTestFlight/1184)

#Mac #Beta

Version 6.2.0-8140 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8140-875ef3b613bb77f93baeb9ad271f7305.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. Enable this feature for the policy configuration dns-follow-interface=true. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1183](https://t.me/SurgeTestFlight/1183)

#Mac #Beta

Version 6.2.0-8130 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8130-6c5d863eef1597a6393dd14e1f149e7b.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1182](https://t.me/SurgeTestFlight/1182)

#Mac #Beta

Version 6.2.0-8120 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8120-fb26035da18d8a586e7e2391aca313ee.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1181](https://t.me/SurgeTestFlight/1181)

#Mac #Beta

Version 6.2.0-8110 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8110-9049b22debcd5c8597be070bb2d81b3e.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-30 [post 1180](https://t.me/SurgeTestFlight/1180)

#Mac #Beta

Version 6.2.0-8100 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8100-2926eb244e0be4e015f7a63740d33939.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1179](https://t.me/SurgeTestFlight/1179)

#Mac #Beta

Version 6.2.0-8090 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8090-f9325c5abd9b81ced85b17c05e3f3304.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1177](https://t.me/SurgeTestFlight/1177)

#Mac #Beta

Version 6.2.0-8080 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8080-d00ed79c4673a8388a5475060d1e76c0.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1176](https://t.me/SurgeTestFlight/1176)

#Mac #Beta

Version 6.2.0-8070 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8070-2b74f73cd518859080760bc3b186b24b.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1174](https://t.me/SurgeTestFlight/1174)

#Mac #Beta

Version 6.2.0-8040 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8040-18f05d801725ea1487cb189f3eb22f7b.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1173](https://t.me/SurgeTestFlight/1173)

#Mac #Beta

Version 6.2.0-8020 https://dl.nssurge.com/mac/v6/Surge-6.2.0-8020-4e73e8754bdf763081b47e3dd063c7fb.zip

### Core Improvements
- The interface parameter in policies can now also take effect on DNS queries. DNS requests that match the policy will use the specified interface for resolution. (If DNS is triggered during the rule matching phase, a specific interface will not be used.)
- The network quality detection subsystem has been rewritten with more comprehensive checking logic, so notifications are no longer triggered frequently when the network is unstable.

### Ponte Server Upgrade
- Optional active standby mode: When Surge detects that the main network interface is unavailable for a period of time, Ponte will automatically switch to another interface (such as 5G USB modem or multi-WAN scenarios). At the same time, iCloud will temporarily use this interface to complete new address announcements.
- IPv6 can be configured to take effect on specific interfaces or enabled for all interfaces, suitable for multi-WAN scenarios.
- Supports cross-subnet intranet connections such as multiple VLANs.

Official Channel: @SurgeTestFlightFeed

## 2025-07-27 [post 1170](https://t.me/SurgeTestFlight/1170)

#Mac #Beta

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

## 2025-07-27 [post 1169](https://t.me/SurgeTestFlight/1169)

#Mac #Beta

Version 6.1.0-8000 https://dl.nssurge.com/mac/v6/Surge-6.1.0-8000-2158f38f63c657bea7646b7d5f3dbe80.zip

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

## 2025-07-26 [post 1168](https://t.me/SurgeTestFlight/1168)

#Mac #Beta

Version 6.1.0-7980 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7980-7ce408dd0db27f067148a578c93a59ac.zip

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

## 2025-07-25 [post 1167](https://t.me/SurgeTestFlight/1167)

#Mac #Beta

Version 6.1.0-7960 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7960-7902c54d94d1bfc699158f8f23c14c0d.zip

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

## 2025-07-25 [post 1166](https://t.me/SurgeTestFlight/1166)

#Mac #Beta

Version 6.1.0-7950 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7950-a3df88c5b9cd48e272d840cdb404c362.zip

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

## 2025-07-25 [post 1165](https://t.me/SurgeTestFlight/1165)

#Mac #Beta

Version 6.1.0-7940 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7940-002548aeb2dc2765a000f1977261676c.zip

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

## 2025-07-24 [post 1163](https://t.me/SurgeTestFlight/1163)

#Mac #Beta

Version 6.1.0-7930 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7930-b133e2644ffbc34c5128d394e7d9a098.zip

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

## 2025-07-24 [post 1161](https://t.me/SurgeTestFlight/1161)

#Mac #Beta

Version 6.1.0-7920 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7920-f4d319f1adf67abe68ef7bab2dd6dda0.zip

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

## 2025-07-23 [post 1160](https://t.me/SurgeTestFlight/1160)

#Mac #Beta

Version 6.1.0-7910 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7910-6389a78efc1b1346b5d12b904047c507.zip

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

## 2025-07-23 [post 1159](https://t.me/SurgeTestFlight/1159)

#Mac #Beta

Version 6.1.0-7900 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7900-81ddfea62a6707fee0e80828def9c916.zip

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

## 2025-07-23 [post 1157](https://t.me/SurgeTestFlight/1157)

#Mac #Beta

Version 6.1.0-7890 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7890-19ebc32cd85fb8c0bc22264de08a21fc.zip

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

## 2025-07-23 [post 1155](https://t.me/SurgeTestFlight/1155)

#Mac #Beta

Version 6.1.0-7880 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7880-d22c40e4e0d6196b97ff99e43ffc5e7b.zip

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

## 2025-07-23 [post 1154](https://t.me/SurgeTestFlight/1154)

#Mac #Beta

Version 6.1.0-7870 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7870-515e713167e6c727109359d1a2c7324d.zip

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

## 2025-07-23 [post 1153](https://t.me/SurgeTestFlight/1153)

#Mac #Beta

Version 6.1.0-7860 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7860-5d7e070e4d171cc82cd348be13c22252.zip

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

## 2025-07-22 [post 1152](https://t.me/SurgeTestFlight/1152)

#Mac #Beta

Version 6.1.0-7850 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7850-4c7d4348d465bc99dbf79cd2634d7e07.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.
- Improve the compatibility of IPv6 RA override with Windows clients.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1151](https://t.me/SurgeTestFlight/1151)

#Mac #Beta

Version 6.1.0-7840 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7840-38a79d8027a676a9fc521c1fd156c1b7.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1150](https://t.me/SurgeTestFlight/1150)

#Mac #Beta

Version 6.1.0-7820 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7820-a40f114373acf84dc220b1af0211f1cb.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1149](https://t.me/SurgeTestFlight/1149)

#Mac #Beta

Version 6.1.0-7810 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7810-3d876bbe811c9223ffec3a8b9f7237cc.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1148](https://t.me/SurgeTestFlight/1148)

#Mac #Beta

Version 6.1.0-7800 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7800-83761e86fd5987d903b3791680cf1d8e.zip

### New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Added a new rule type MAC-ADDRESS for directly matching specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1146](https://t.me/SurgeTestFlight/1146)

#Mac #Beta

Version 6.1.0-7790 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7790-f0039f1f1a131d87f882ffcb1b4cfb92.zip

## New
- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- A new rule type MAC-ADDRESS is used to directly match specific clients using MAC addresses.
- The client-source-address parameter of [MITM] now supports specifying MAC addresses in addition to IPs, to address the issue of client IPv6 request address changes.

### Improvements
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

### Fixes
- Fixed a potential no network issue that could occur under high concurrency.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-22 [post 1145](https://t.me/SurgeTestFlight/1145)

#Mac #Beta

Version 6.1.0-7780 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7780-e3c3771c2e7829f73eb55422783c70f0.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-21 [post 1144](https://t.me/SurgeTestFlight/1144)

#Mac #Beta

Version 6.1.0-7760 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7760-3ca6d7a23cd0c6b54fa0e2d123235616.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-21 [post 1141](https://t.me/SurgeTestFlight/1141)

#Mac #Beta

Version 6.1.0-7740 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7740-541f7328b2ade58e718e363b9014d073.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.
- Fix compatibility issues with large UDP packets in the new version of Hysteria 2.

Official Channel: @SurgeTestFlightFeed

## 2025-07-21 [post 1138](https://t.me/SurgeTestFlight/1138)

#Mac #Beta

Version 6.1.0-7730 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7730-b78e7185f4c2ddf9da7e3f5d2b6afe4d.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

Official Channel: @SurgeTestFlightFeed

## 2025-07-20 [post 1137](https://t.me/SurgeTestFlight/1137)

#Mac #Beta

Version 6.1.0-7710 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7710-b58cf297ebf868ee43f9497e255c0f9f.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

Official Channel: @SurgeTestFlightFeed

## 2025-07-20 [post 1136](https://t.me/SurgeTestFlight/1136)

#Mac #Beta

Version 6.1.0-7700 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7700-fe769dcc3a24b5fffee9f023aebcb230.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

Official Channel: @SurgeTestFlightFeed

## 2025-07-19 [post 1133](https://t.me/SurgeTestFlight/1133)

#Mac #Beta

Version 6.1.0-7690 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7690-4fe6cf03c5d22e0155d5eaf15ce1f7c2.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1132](https://t.me/SurgeTestFlight/1132)

#Mac #Beta

Version 6.1.0-7680 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7680-e886c8412d7a7659419542ae95ac00aa.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.
- Support automatically configuring system proxy settings when only listening with IPv6 interface.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1131](https://t.me/SurgeTestFlight/1131)

#Mac #Beta

Version 6.1.0-7670 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7670-408897fb5f0fcf58ae5bfe96dd1c8738.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1130](https://t.me/SurgeTestFlight/1130)

#Mac #Beta

Version 6.1.0-7660 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7660-66b971e3cb61d99e10f11af55d2662da.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.
- Fixed a potential no network issue that could occur under high concurrency.
- Optimized the behavior of Ponte NAT traversal mode to always use local port 6208 in order to improve the success rate of traversal.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1129](https://t.me/SurgeTestFlight/1129)

#Mac #Beta

Version 6.1.0-7650 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7650-428e5f92af3b36540fe07c0f7894d272.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1127](https://t.me/SurgeTestFlight/1127)

#Mac #Beta

Version 6.1.0-7640 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7640-83512d21af95ab9dd91a95acabb09da5.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1126](https://t.me/SurgeTestFlight/1126)

#Mac #Beta

Version 6.1.0-7630 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7630-ca571942edf1ea5f9e7339e2e85f3af9.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1125](https://t.me/SurgeTestFlight/1125)

#Mac #Beta

Version 6.1.0-7610 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7610-d1eddba36382ff90196c3607768b2ae2.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1124](https://t.me/SurgeTestFlight/1124)

#Mac #Beta

Version 5.10.5-3350 https://dl.nssurge.com/mac/v5/Surge-5.10.5-3350-e93dc85636fe529df08c6e4f80d0e8a9.zip

- Ready for Surge Mac 6.
- Fix the issue of incorrect main menu text color in dark mode on macOS 26 beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1122](https://t.me/SurgeTestFlight/1122)

#Mac #Beta

Version 6.1.0-7580 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7580-479c2957a3a515bcbeb41e5a0274c2f2.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-18 [post 1120](https://t.me/SurgeTestFlight/1120)

#Mac #Beta

Version 6.1.0-7570 https://dl.nssurge.com/mac/v6/Surge-6.1.0-7570-a2efe236dd177967ee30045ab978c45c.zip

- The Surge Gateway VM and DHCP functions have been decoupled, so now the Gateway VM can be enabled without enabling DHCP. Additionally, the configuration page for gateway mode has been redesigned, allowing direct modification of the configuration.

Official Channel: @SurgeTestFlightFeed

## 2025-07-16 [post 1117](https://t.me/SurgeTestFlight/1117)

#Mac #Beta

Version 6.0.2-7560 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7560-e67bf53126620427b01e574242e88dc0.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.
- Fixed some interface layout issues on devices without a connected touchpad.

Official Channel: @SurgeTestFlightFeed

## 2025-07-16 [post 1116](https://t.me/SurgeTestFlight/1116)

#Mac #Beta

Version 6.0.2-7550 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7550-34cb48d926fbd71affce9cedc16383c2.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.
- Fixed some interface layout issues on devices without a connected touchpad.

Official Channel: @SurgeTestFlightFeed

## 2025-07-16 [post 1115](https://t.me/SurgeTestFlight/1115)

#Mac #Beta

Version 6.0.2-7540 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7540-73caa4c723d0e6e848f530e3026fbe67.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1114](https://t.me/SurgeTestFlight/1114)

#Mac #Beta

Version 6.0.2-7530 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7530-7ca10c21a2053ec4d3c6faacaaae6524.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1112](https://t.me/SurgeTestFlight/1112)

#Mac #Beta

Version 6.0.2-7520 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7520-520a2a514a0167835a2515cd08b3607b.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1110](https://t.me/SurgeTestFlight/1110)

#Mac #Beta

Version 6.0.2-7510 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7510-07077a86641b1497d4648b314860fd72.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1109](https://t.me/SurgeTestFlight/1109)

#Mac #Beta

Version 6.0.2-7490 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7490-8abc51d2462ca1bfc572839abdcdc859.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-14 [post 1107](https://t.me/SurgeTestFlight/1107)

#Mac #Beta

Version 6.0.2-7480 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7480-8a2c40b7109b0e397e991f83ff1474bd.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.
- Fixed the issue where the Dashboard device list could not be sorted by MAC address.

Official Channel: @SurgeTestFlightFeed

## 2025-07-14 [post 1106](https://t.me/SurgeTestFlight/1106)

#Mac #Beta

Version 6.0.2-7460 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7460-0e86254f5b18f63f6ee27f313b548cb7.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.
- Fixed a potential unexpected drop in throughput under HTTP mode.

Official Channel: @SurgeTestFlightFeed

## 2025-07-14 [post 1105](https://t.me/SurgeTestFlight/1105)

#Mac #Beta

Version 6.0.2-7450 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7450-9252c538193abc00cb91d140f1a2f8ea.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1103](https://t.me/SurgeTestFlight/1103)

#Mac #Beta

Version 6.0.2-7430 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7430-8823bc910e2b0b3bd1ee3f3aab347cbb.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1102](https://t.me/SurgeTestFlight/1102)

#Mac #Beta

Version 6.0.2-7420 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7420-0765dfbbbbecda1bf404b8c2f24588db.zip

- Improve the compatibility of IPv6 RA override with Windows clients.
- Improve the stability of VMNET on older versions of macOS.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1101](https://t.me/SurgeTestFlight/1101)

#Mac #Beta

Version 6.0.2-7410 https://dl.nssurge.com/mac/v6/Surge-6.0.2-7410-67294ac860c4ef5b4fa4fa9ab89746f5.zip

- Improve the stability of VMNET on older versions of macOS.

Official Channel: @SurgeTestFlightFeed

## 2025-07-13 [post 1095](https://t.me/SurgeTestFlight/1095)

#Mac #Beta

Version 6.0.1-7400 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7400-cb59cf65ab136785580975a82cc49dbd.zip

- Restored support for Snell v2/v3.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-12 [post 1094](https://t.me/SurgeTestFlight/1094)

#Mac #Beta

Version 6.0.1-7390 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7390-259e493cf1b3ec528943b6baf6804715.zip

- Restored support for Snell v2/v3.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-12 [post 1093](https://t.me/SurgeTestFlight/1093)

#Mac #Beta

Version 6.0.1-7370 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7370-491fb38e34acfe36bcd58acb18157afe.zip

- Restored support for Snell v2/v3.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-12 [post 1091](https://t.me/SurgeTestFlight/1091)

#Mac #Beta

Version 6.0.1-7360 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7360-6412b55f7bcb1033b1e81565012014b9.zip

- Restored support for Snell v2/v3.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-11 [post 1090](https://t.me/SurgeTestFlight/1090)

#Mac #Beta

Version 5.10.4-3330 https://dl.nssurge.com/mac/v5/Surge-5.10.4-3330-47c0d46e960e347dcd44f46002d50966.zip

- Ready for Surge Mac 6.
- Fixed issues for macOS 26 beta.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-07-11 [post 1089](https://t.me/SurgeTestFlight/1089)

#Mac #Beta

Version 6.0.1-7350 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7350-8dfccb6e32eb91628535caedca457a08.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-11 [post 1088](https://t.me/SurgeTestFlight/1088)

#Mac #Beta

Version 6.0.1-7340 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7340-da1c5588d4aceb4ce241919865fb3e05.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1085](https://t.me/SurgeTestFlight/1085)

#Mac #Beta

Version 6.0.1-7290 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7290-e99f78de254048cad00541dd006761b1.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1084](https://t.me/SurgeTestFlight/1084)

#Mac #Beta

Version 6.0.1-7270 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7270-dfc84ccbddcf889e42f83415dc0e7b71.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1083](https://t.me/SurgeTestFlight/1083)

#Mac #Beta

Version 6.0.1-7250 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7250-7bf2964ed31ef724f66acdbd15125492.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1082](https://t.me/SurgeTestFlight/1082)

#Mac #Beta

Version 6.0.1-7240 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7240-46b6ff11e2b626a6e743bb06106e04eb.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1081](https://t.me/SurgeTestFlight/1081)

#Mac #Beta

Version 6.0.1-7230 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7230-a4788e1c08f05168cb3ddb187f362987.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1080](https://t.me/SurgeTestFlight/1080)

#Mac #Beta

Version 6.0.1-7220 https://dl.nssurge.com/mac/v6/Surge-6.0.1-7220-95a7f81d48d698118f7285735fb17b2b.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2025-07-09 [post 1074](https://t.me/SurgeTestFlight/1074)

#Mac #Beta

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

## 2025-07-08 [post 1072](https://t.me/SurgeTestFlight/1072)

#Mac #Beta

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

## 2025-07-08 [post 1069](https://t.me/SurgeTestFlight/1069)

#Mac #Beta

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

## 2025-07-08 [post 1067](https://t.me/SurgeTestFlight/1067)

#Mac #Beta

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

## 2025-07-07 [post 1065](https://t.me/SurgeTestFlight/1065)

#Mac #Beta

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

## 2025-07-07 [post 1063](https://t.me/SurgeTestFlight/1063)

#Mac #Beta

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

## 2025-07-07 [post 1061](https://t.me/SurgeTestFlight/1061)

#Mac #Beta

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

## 2025-07-07 [post 1059](https://t.me/SurgeTestFlight/1059)

#Mac #Beta

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

## 2025-07-07 [post 1057](https://t.me/SurgeTestFlight/1057)

#Mac #Beta

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

## 2025-07-07 [post 1055](https://t.me/SurgeTestFlight/1055)

#Mac #Beta

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

## 2025-07-07 [post 1052](https://t.me/SurgeTestFlight/1052)

#Mac #Beta

Version 6.0.0-7100 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7100-403faa55c35e84189ebb5f03199b9ec0.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1050](https://t.me/SurgeTestFlight/1050)

#Mac #Beta

Version 6.0.0-7090 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7090-3fe2013a818c6ceaa46f25531ae3304e.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1048](https://t.me/SurgeTestFlight/1048)

#Mac #Beta

Version 6.0.0-7070 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7070-ab84e895b571d57e920893547fff049f.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-06 [post 1046](https://t.me/SurgeTestFlight/1046)

#Mac #Beta

Version 6.0.0-7060 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7060-30b2b5a3f6adf5e82371f84edbca63bf.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1043](https://t.me/SurgeTestFlight/1043)

#Mac #Beta

Version 6.0.0-7030 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7030-a49742ce9bb67c99f72baf84b62dc7b5.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1041](https://t.me/SurgeTestFlight/1041)

#Mac #Beta

Version 6.0.0-7010 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7010-55620b6f19413f1b92ac6caa309a38d3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1039](https://t.me/SurgeTestFlight/1039)

#Mac #Beta

Version 6.0.0-7000 https://dl.nssurge.com/mac/v6/Surge-6.0.0-7000-4304f05f2019c0acadb3c70601eb3b1c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1037](https://t.me/SurgeTestFlight/1037)

#Mac #Beta

Version 6.0.0-6980 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6980-509b98e167c8fc8f5d356e69c262a7f2.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-05 [post 1035](https://t.me/SurgeTestFlight/1035)

#Mac #Beta

Version 6.0.0-6950 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6950-e9f00c7e424ee9cb74c684f5aa9862df.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1033](https://t.me/SurgeTestFlight/1033)

#Mac #Beta

Version 6.0.0-6930 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6930-e9ad912908f8c3b0747221dea34d5f60.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1031](https://t.me/SurgeTestFlight/1031)

#Mac #Beta

Version 6.0.0-6860 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6860-bcc8a10f6519aed3918c9004dcd0a2b3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1029](https://t.me/SurgeTestFlight/1029)

#Mac #Beta

Version 6.0.0-6850 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6850-2123a9ea85159cb36abe9dd30bb11885.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1027](https://t.me/SurgeTestFlight/1027)

#Mac #Beta

Version 6.0.0-6840 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6840-ef9bf8b23a1d6cb822310832bd6bb155.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-04 [post 1025](https://t.me/SurgeTestFlight/1025)

#Mac #Beta

Version 6.0.0-6830 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6830-34500b67d6e7f6e3298e60fb54b04a08.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-03 [post 1022](https://t.me/SurgeTestFlight/1022)

#Mac #Beta

Version 6.0.0-6810 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6810-6269ecafdbf6fb6bb5671766a02fbb6c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-03 [post 1020](https://t.me/SurgeTestFlight/1020)

#Mac #Beta

Version 6.0.0-6760 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6760-f0029fae2cdc9374c9bf60914f9e4bfb.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1017](https://t.me/SurgeTestFlight/1017)

#Mac #Beta

Version 6.0.0-6700 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6700-402a98b37d9806cdca40951b36e714eb.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1015](https://t.me/SurgeTestFlight/1015)

#Mac #Beta

Version 6.0.0-6690 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6690-222b61553d2df858566ce2b31540a9d7.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1013](https://t.me/SurgeTestFlight/1013)

#Mac #Beta

Version 6.0.0-6680 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6680-c85bb1313c4298261dffb088a2f43075.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1011](https://t.me/SurgeTestFlight/1011)

#Mac #Beta

Version 6.0.0-6670 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6670-c2ac024733216518ffaf50743992ba14.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1009](https://t.me/SurgeTestFlight/1009)

#Mac #Beta

Version 6.0.0-6660 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6660-d346f46d21547c3d905c4c4238f84f85.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1007](https://t.me/SurgeTestFlight/1007)

#Mac #Beta

Version 6.0.0-6650 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6650-2c4cea3d5aa965830307b9713c662329.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 995](https://t.me/SurgeTestFlight/995)

#Mac #Beta

Version 6.0.0-6590 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6590-c6e4026e99a06af4069177d0f6b6944d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 993](https://t.me/SurgeTestFlight/993)

#Mac #Beta

Version 6.0.0-6580 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6580-19cddde88ee943fee08aa9df1387a2c3.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 991](https://t.me/SurgeTestFlight/991)

#Mac #Beta

Version 6.0.0-6570 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6570-d99b4dd607f2a7f1cf170e824b1c6a4d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 989](https://t.me/SurgeTestFlight/989)

#Mac #Beta

Version 6.0.0-6560 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6560-e7156e3e07c271fc7b1c8f50222d0c1c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 1004](https://t.me/SurgeTestFlight/1004)

#Mac #Beta

Version 6.0.0-6610 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6610-d2116e3eed2c9ac9876f579fc28bc310.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-07-01 [post 1001](https://t.me/SurgeTestFlight/1001)

#Mac #Beta

Version 6.0.0-6600 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6600-62817a8be002e0b3a3afef7d88769c5e.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 987](https://t.me/SurgeTestFlight/987)

#Mac #Beta

Version 6.0.0-6550 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6550-935f1a0ce346835da1f9213a52cd5b25.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 985](https://t.me/SurgeTestFlight/985)

#Mac #Beta

Version 6.0.0-6540 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6540-2ad14205d51fcf510fb1ba58a1f90c0d.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 982](https://t.me/SurgeTestFlight/982)

#Mac #Beta

Version 6.0.0-6530 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6530-09ef1aa2eee493b0a05ecc5f0a7104f1.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-29 [post 973](https://t.me/SurgeTestFlight/973)

#Mac #Beta

Version 6.0.0-6480 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6480-f018946bc78c4f4b41664f8be4fa7c69.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-29 [post 971](https://t.me/SurgeTestFlight/971)

#Mac #Beta

Version 6.0.0-6430 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6430-4b32e4c65f8b99e1902e061bde7fc2f8.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 969](https://t.me/SurgeTestFlight/969)

#Mac #Beta

Version 6.0.0-6380 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6380-9e92b45e61db9ef0a53021bde549693c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 967](https://t.me/SurgeTestFlight/967)

#Mac #Beta

Version 6.0.0-6360 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6360-23936e729b2632cd3cef3b3d50470ba8.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 965](https://t.me/SurgeTestFlight/965)

#Mac #Beta

Version 6.0.0-6350 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6350-665c0fd38f72c61e47c1aadacb14580c.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-28 [post 963](https://t.me/SurgeTestFlight/963)

#Mac #Beta

Version 6.0.0-6320 https://dl.nssurge.com/mac/v6/Surge-6.0.0-6320-a11127ff556e409af1a7dabed663eca7.zip

- 6.0.0 Beta.

Official Channel: @SurgeTestFlightFeed

## 2025-06-10 [post 961](https://t.me/SurgeTestFlight/961)

#Mac #Beta

Version 5.10.4-3284 https://dl.nssurge.com/mac/v5/Surge-5.10.4-3284-3da715625562dcf875cc29c652b3e732.zip

- Fixed the issue where using ShadowTLS/AdaptiveTLSFingerprint on macOS 26 would cause a crash.
- Optimized compatibility issues with other VPNs and high-priority routing tables when Enhanced Mode is enabled.      
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-06-10 [post 959](https://t.me/SurgeTestFlight/959)

#Mac #Beta

Version 5.10.4-3282 https://dl.nssurge.com/mac/v5/Surge-5.10.4-3282-a31937748b56e7089aca582a69d96c6c.zip

- Fixed the issue where using ShadowTLS/AdaptiveTLSFingerprint on macOS 26 would cause a crash.
- Optimized compatibility issues with other VPNs and high-priority routing tables when Enhanced Mode is enabled.      
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-05-09 [post 948](https://t.me/SurgeTestFlight/948)

#Mac #Beta

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

## 2025-05-07 [post 943](https://t.me/SurgeTestFlight/943)

#Mac #Beta

Version 5.10.3-3270 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3270-5658351bbc68359453f280f9d0dbd566.zip

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

## 2025-05-07 [post 942](https://t.me/SurgeTestFlight/942)

#Mac #Beta

Version 5.10.3-3269 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3269-bb864816846a211ae43ab342fc5e1d18.zip

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

## 2025-05-06 [post 941](https://t.me/SurgeTestFlight/941)

#Mac #Beta

Version 5.10.3-3266 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3266-863854da6a0cc6f11c67086551abe7a1.zip

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

## 2025-05-06 [post 940](https://t.me/SurgeTestFlight/940)

#Mac #Beta

Version 5.10.3-3265 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3265-c9493d4b71af79d1cf4280ae5aaf313c.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Add integration support for the Dia browser.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-05-03 [post 939](https://t.me/SurgeTestFlight/939)

#Mac #Beta

Version 5.10.3-3262 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3262-4737da9eaea48889ffeaf74f466fd236.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-05-01 [post 936](https://t.me/SurgeTestFlight/936)

#Mac #Beta

Version 5.10.3-3261 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3261-818284226daef93638ddee37700ec0b0.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-29 [post 933](https://t.me/SurgeTestFlight/933)

#Mac #Beta

Version 5.10.3-3260 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3260-1674a37dcbe3370fccca0d56a02a02c5.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-29 [post 932](https://t.me/SurgeTestFlight/932)

#Mac #Beta

Version 5.10.3-3259 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3259-dd40f796080a3419297d5c1fabd31d9a.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-24 [post 930](https://t.me/SurgeTestFlight/930)

#Mac #Beta

Version 5.10.3-3258 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3258-445ba395c42075f9507376c0446dacc3.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-23 [post 929](https://t.me/SurgeTestFlight/929)

#Mac #Beta

Version 5.10.3-3257 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3257-53923732dd1a9a1001c4b2a1dd96f569.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-19 [post 926](https://t.me/SurgeTestFlight/926)

#Mac #Beta

Version 5.10.3-3255 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3255-8a2107263da1d0785a7d97561a8cecd0.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-18 [post 924](https://t.me/SurgeTestFlight/924)

#Mac #Beta

Version 5.10.3-3254 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3254-39b94728f1720b094fdef656d93d5efa.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-17 [post 922](https://t.me/SurgeTestFlight/922)

#Mac #Beta

Version 5.10.3-3252 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3252-c249470849f1d6dcd6dd77ca1f5bf2ae.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-16 [post 919](https://t.me/SurgeTestFlight/919)

#Mac #Beta

Version 5.10.3-3248 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3248-c3260751aa254d44fdaac180e1dbfd7f.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-16 [post 916](https://t.me/SurgeTestFlight/916)

#Mac #Beta

Version 5.10.3-3247 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3247-fd9e5c3e3a8328031df7e9f193f5eb5e.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-08 [post 914](https://t.me/SurgeTestFlight/914)

#Mac #Beta

Version 5.10.3-3243 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3243-0b296baa2391531f6a675ac972ce3805.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-03 [post 912](https://t.me/SurgeTestFlight/912)

#Mac #Beta

Version 5.10.3-3242 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3242-25494d5114aff180bd92ac7689b8c441.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-02 [post 909](https://t.me/SurgeTestFlight/909)

#Mac #Beta

Version 5.10.3-3241 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3241-42b193858e361bd7cab0d06ba81b2829.zip

- Added [General] parameter block-quic, which is used to globally override the behavior of whether to block QUIC traffic. It can be set to:
    - per-policy: Determined by the policy's block-quic parameter, default value, i.e., current version behavior.
    - all-proxy: Overrides the proxy policy's block-quic parameter, blocks all
    - all: Overrides all policies' block-quic parameters, blocks all including DIRECT policy
    - always-allow: Overrides the proxy policy's block-quic parameter, allows all  

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-04-01 [post 906](https://t.me/SurgeTestFlight/906)

#Mac #Beta

Version 5.10.3-3239 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3239-8dc57dfbe3d56c51561e1c42513ddf66.zip

- The adding new rule view can now remember previous options.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-31 [post 905](https://t.me/SurgeTestFlight/905)

#Mac #Beta

Version 5.10.3-3238 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3238-5d1a8b88405b63f697808be54d1b8396.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-27 [post 903](https://t.me/SurgeTestFlight/903)

#Mac #Beta

Version 5.10.3-3237 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3237-a66c304c1cb20b6dad175f49066f4d35.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-27 [post 900](https://t.me/SurgeTestFlight/900)

#Mac #Beta

Version 5.10.3-3236 https://dl.nssurge.com/mac/v5/Surge-5.10.3-3236-8e7bc357c23a4724b28316c211206cb6.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-20 [post 895](https://t.me/SurgeTestFlight/895)

#Mac #Beta

Version 5.10.2-3235 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3235-9255a55c4af59cbf0ed01b245ef86dcc.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-18 [post 894](https://t.me/SurgeTestFlight/894)

#Mac #Beta

Version 5.10.2-3234 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3234-707fc600750ac06739818359f65caec9.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-13 [post 891](https://t.me/SurgeTestFlight/891)

#Mac #Beta

Version 5.10.2-3233 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3233-d8dc0bfcfb2469707e8c9c730a8be572.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-06 [post 889](https://t.me/SurgeTestFlight/889)

#Mac #Beta

Version 5.10.2-3231 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3231-94ca1f8a2f151badf5787c73f7654276.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-04 [post 887](https://t.me/SurgeTestFlight/887)

#Mac #Beta

Version 5.10.2-3230 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3230-52c7060d9c19de5eca96c2e6c5366349.zip

- Accessing the remote Dashboard of Ponte devices no longer requires Enhanced Mode to be enabled.
- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-03-03 [post 886](https://t.me/SurgeTestFlight/886)

#Mac #Beta

Version 5.10.2-3228 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3228-658420aed72a7c0d9bb65bd9d2cbb064.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-28 [post 885](https://t.me/SurgeTestFlight/885)

#Mac #Beta

Version 5.10.2-3227 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3227-057ba08b1a7a3f1aa3ccf79b7738a1f4.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-27 [post 882](https://t.me/SurgeTestFlight/882)

#Mac #Beta

Version 5.10.2-3223 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3223-1d89e68a7c997bc61e1af2ea32a9ccc7.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 880](https://t.me/SurgeTestFlight/880)

#Mac #Beta

Version 5.10.2-3220 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3220-3cc5c298a62b76729e9b7e8f6f31ef2c.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 877](https://t.me/SurgeTestFlight/877)

#Mac #Beta

Version 5.10.2-3219 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3219-790b01f98819ffeae8f5084f91eafe4a.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 876](https://t.me/SurgeTestFlight/876)

#Mac #Beta

Version 5.10.2-3218 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3218-2fbe45998c4f4e30017ce147e640648f.zip

- Added DNS over TLS support, e.g., tls://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 874](https://t.me/SurgeTestFlight/874)

#Mac #Beta

Version 5.10.2-3216 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3216-d8ebae4102cd8d33abecd6ed19cd9d1d.zip

- Added DNS over TLS support, e.g., dot://8.8.8.8
- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-25 [post 871](https://t.me/SurgeTestFlight/871)

#Mac #Beta

Version 5.10.2-3214 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3214-f8870b2fa8a786f92d21481c313ca093.zip

- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-25 [post 870](https://t.me/SurgeTestFlight/870)

#Mac #Beta

Version 5.10.2-3213 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3213-f1a3a21d37f0eddb557247214fe70050.zip

- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-25 [post 869](https://t.me/SurgeTestFlight/869)

#Mac #Beta

Version 5.10.2-3212 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3212-5e1c22a2777ec241a9baa3c536d53c05.zip

- Optimize the process of adding rules through the Dashboard.
- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-21 [post 866](https://t.me/SurgeTestFlight/866)

#Mac #Beta

Version 5.10.2-3209 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3209-169388f1ffba17c77dbfc88e65206b44.zip

- Surge Dashboard can now remotely operate the temporary rules of the target Surge instance.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-21 [post 863](https://t.me/SurgeTestFlight/863)

#Mac #Beta

Version 5.10.2-3208 https://dl.nssurge.com/mac/v5/Surge-5.10.2-3208-599aa9b4788be0b3c593a14c2725bff3.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-20 [post 861](https://t.me/SurgeTestFlight/861)

#Mac #Beta

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

## 2025-02-19 [post 858](https://t.me/SurgeTestFlight/858)

#Mac #Beta

Version 5.10.1-3206 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3206-27fb973e2bc3ed620107d086b4d9c7d8.zip

- When enabling the HTTP capture switch, all active connections will now be forcibly interrupted to ensure that no requests are missed due to existing long connections.
- Optimized compatibility with some QUIC clients, such as Lark.
- Fixed an issue where download data bytes in statistics was incorrect after modifying the request HTTP using scripts or other mechanisms.
- Adjusted the priority of processing logic when forwarding QUIC. Now, for a proxy policy that does not support UDP forwarding, it will prioritize considering QUIC Block before falling back to DIRECT or REJECT.
- Fixed an issue where utun devices could not be used when binding the outbound interface.
- Fixed an issue where repeated notifications might continuously occur during Ponte Server retry failures.
- Resolved an issue where a specific request forwarded by Surge Ponte might get stuck under certain networks.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-18 [post 855](https://t.me/SurgeTestFlight/855)

#Mac #Beta

Version 5.10.1-3205 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3205-e257c20db97b6675d1acc476145fd959.zip

- When enabling the HTTP capture switch, all active connections will now be forcibly interrupted to ensure that no requests are missed due to existing long connections.
- Optimized compatibility with some QUIC clients, such as Lark.
- Fixed an issue where download data bytes in statistics was incorrect after modifying the request HTTP using scripts or other mechanisms.
- Adjusted the priority of processing logic when forwarding QUIC. Now, for a proxy policy that does not support UDP forwarding, it will prioritize considering QUIC Block before falling back to DIRECT or REJECT.
- Fixed an issue where utun devices could not be used when binding the outbound interface.
- Fixed an issue where repeated notifications might continuously occur during Ponte Server retry failures.
- Resolved an issue where a specific request forwarded by Surge Ponte might get stuck under certain networks.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-02-17 [post 850](https://t.me/SurgeTestFlight/850)

#Mac #Beta

Version 5.10.1-3201 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3201-11f2a1993162fe0a873c9079fa38e690.zip

- Fix the issue where Surge Ponte has a probability of getting stuck when forwarding requests under specific networks.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-31 [post 849](https://t.me/SurgeTestFlight/849)

#Mac #Beta

Version 5.10.1-3200 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3200-ec57d005eff8fa404c2628c325e1682b.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-29 [post 848](https://t.me/SurgeTestFlight/848)

#Mac #Beta

Version 5.10.1-3199 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3199-67d9edb70a254b64fcbc95a39eb5b153.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-25 [post 847](https://t.me/SurgeTestFlight/847)

#Mac #Beta

Version 5.10.1-3198 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3198-618ac703ef80d0c386200cec526c5775.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-24 [post 846](https://t.me/SurgeTestFlight/846)

#Mac #Beta

Version 5.10.1-3197 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3197-015b1f255fad868b7fe1644376af4747.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-24 [post 845](https://t.me/SurgeTestFlight/845)

#Mac #Beta

Version 5.10.1-3196 https://dl.nssurge.com/mac/v5/Surge-5.10.1-3196-632757a83ac30f723f91cf253463198e.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-19 [post 842](https://t.me/SurgeTestFlight/842)

#Mac #Beta

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

## 2025-01-18 [post 840](https://t.me/SurgeTestFlight/840)

#Mac #Beta

Version 5.10.0-3194 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3194-5fbbafc8491c29f4b13e5ba658f7886d.zip

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

## 2025-01-17 [post 838](https://t.me/SurgeTestFlight/838)

#Mac #Beta

Version 5.10.0-3193 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3193-426dd4e9b5e54ca7954412145ed5355d.zip

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

## 2025-01-16 [post 836](https://t.me/SurgeTestFlight/836)

#Mac #Beta

Version 5.10.0-3192 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3192-ecc5b1996a2764cae955e6dba158d283.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 834](https://t.me/SurgeTestFlight/834)

#Mac #Beta

Version 5.10.0-3191 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3191-a236e3221b2d06753fe0852ef43f2b3b.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 830](https://t.me/SurgeTestFlight/830)

#Mac #Beta

Version 5.10.0-3190 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3190-bbaec72d8f32cab1706aa4cd3d994515.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 829](https://t.me/SurgeTestFlight/829)

#Mac #Beta

Version 5.10.0-3189 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3189-58d3d8f3a897c3ff335a4495b29825f6.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-14 [post 825](https://t.me/SurgeTestFlight/825)

#Mac #Beta

Version 5.10.0-3187 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3187-c589cc0239d7a83e2061e78a3fc0459c.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-13 [post 823](https://t.me/SurgeTestFlight/823)

#Mac #Beta

Version 5.10.0-3185 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3185-e16962fefc35616252cc40e407068f39.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-09 [post 822](https://t.me/SurgeTestFlight/822)

#Mac #Beta

Version 5.10.0-3184 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3184-a3b5b9f5438a9ffef4652006dcf789f5.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Surge Ponte can now automatically retry to recover after an abnormal NAT type appears.
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-08 [post 820](https://t.me/SurgeTestFlight/820)

#Mac #Beta

Version 5.10.0-3182 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3182-03b4aac159e3cdb540ab2dca82e25a61.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-07 [post 819](https://t.me/SurgeTestFlight/819)

#Mac #Beta

Version 5.10.0-3181 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3181-49d01c4c0580214614b985473b6ece35.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-06 [post 818](https://t.me/SurgeTestFlight/818)

#Mac #Beta

Version 5.10.0-3178 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3178-198b0a1eaeae9bffdaceb7b612ec8e03.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-06 [post 817](https://t.me/SurgeTestFlight/817)

#Mac #Beta

Version 5.10.0-3177 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3177-4d7e0704adf0d72404c3edb866bca01a.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-06 [post 816](https://t.me/SurgeTestFlight/816)

#Mac #Beta

Version 5.10.0-3175 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3175-a8ed70e415b0a27d5444c74861145c5f.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-05 [post 815](https://t.me/SurgeTestFlight/815)

#Mac #Beta

Version 5.10.0-3174 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3174-7c857e223d3e78559757206d75329941.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-04 [post 814](https://t.me/SurgeTestFlight/814)

#Mac #Beta

Version 5.10.0-3173 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3173-a1505fe7bff7f40f68f3f69db3b51192.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-03 [post 813](https://t.me/SurgeTestFlight/813)

#Mac #Beta

Version 5.10.0-3172 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3172-926c2b0389a5b6b8c88febb40ee3fd0e.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2025-01-03 [post 812](https://t.me/SurgeTestFlight/812)

#Mac #Beta

Version 5.10.0-3171 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3171-81e5c7a173958551afd1c9bce7e0da99.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-31 [post 811](https://t.me/SurgeTestFlight/811)

#Mac #Beta

Version 5.10.0-3169 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3169-7c94dacfd5e525b2cecf2cf2c4a5ac89.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-31 [post 810](https://t.me/SurgeTestFlight/810)

#Mac #Beta

Version 5.10.0-3168 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3168-1b6ff1ac5bfb483186c764a21becb7c5.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-31 [post 809](https://t.me/SurgeTestFlight/809)

#Mac #Beta

Version 5.10.0-3166 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3166-6d3bb5d764f562fda043a896de4a38b2.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-30 [post 807](https://t.me/SurgeTestFlight/807)

#Mac #Beta

Version 5.10.0-3165 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3165-73e4bb010aa06c35eb72182baaa3053c.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-26 [post 805](https://t.me/SurgeTestFlight/805)

#Mac #Beta

Version 5.10.0-3164 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3164-ca9bcaa4c31c0e1e663b3307800cb708.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-26 [post 804](https://t.me/SurgeTestFlight/804)

#Mac #Beta

Version 5.10.0-3163 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3163-1a67754ec03c3d22e1c72b3891069dd4.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-25 [post 803](https://t.me/SurgeTestFlight/803)

#Mac #Beta

Version 5.10.0-3162 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3162-8d741dfa225b531554416f62a41d2146.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-25 [post 802](https://t.me/SurgeTestFlight/802)

#Mac #Beta

Version 5.10.0-3161 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3161-53f1098a9ac03d18e43cdc43f1774377.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-23 [post 796](https://t.me/SurgeTestFlight/796)

#Mac #Beta

Version 5.10.0-3160 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3160-d9ae1bf74f00c3833b7b8ceb76816eb8.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-23 [post 795](https://t.me/SurgeTestFlight/795)

#Mac #Beta

Version 5.10.0-3158 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3158-dde8e0ed77f3ed830db81084478b5fdf.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-22 [post 794](https://t.me/SurgeTestFlight/794)

#Mac #Beta

Version 5.10.0-3157 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3157-e48d32b63ff30e18ba146d0c506873eb.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-21 [post 793](https://t.me/SurgeTestFlight/793)

#Mac #Beta

Version 5.10.0-3156 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3156-7d8125c968340620776bbee2be892e1e.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-21 [post 792](https://t.me/SurgeTestFlight/792)

#Mac #Beta

Version 5.10.0-3155 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3155-87e5b3a77184430dfe9b1fd9f46e8544.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-21 [post 790](https://t.me/SurgeTestFlight/790)

#Mac #Beta

Version 5.10.0-3151 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3151-1a39e02dee70cdc38cf50a006d861439.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-20 [post 789](https://t.me/SurgeTestFlight/789)

#Mac #Beta

Version 5.10.0-3150 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3150-c411f755680550cf24d2f71ba8ba11bc.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-20 [post 788](https://t.me/SurgeTestFlight/788)

#Mac #Beta

Version 5.10.0-3149 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3149-dfd336db5ffdb94d52ed1d0d868f5e3b.zip

### New Feature: Port Forwarding 

Example

[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-20 [post 785](https://t.me/SurgeTestFlight/785)

#Mac #Beta

Version 5.10.0-3148 https://dl.nssurge.com/mac/v5/Surge-5.10.0-3148-d2299fdf3aa497d00bd129f429bddf3c.zip

### New Feature: Transparent Proxy

Example

[Transparent Proxy]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy

The policy parameter is optional; if not specified, the standard proxy matching will be used to determine the policy.

This feature is commonly used in development and debugging scenarios such as connecting to servers like MariaDB using SSH.  
    
- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-19 [post 784](https://t.me/SurgeTestFlight/784)

#Mac #Beta

Version 5.9.4-3147 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3147-58cf2e310143066fdf66dd66c9083f83.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-18 [post 783](https://t.me/SurgeTestFlight/783)

#Mac #Beta

Version 5.9.4-3145 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3145-f514cf8b741091a7ae46e70547e25aed.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-17 [post 781](https://t.me/SurgeTestFlight/781)

#Mac #Beta

Version 5.9.4-3144 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3144-09dbe47fdd6d88a2523c1a708f2745cd.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 779](https://t.me/SurgeTestFlight/779)

#Mac #Beta

Version 5.9.4-3140 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3140-863831b6a90971a1254fa538cb69b0ba.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 778](https://t.me/SurgeTestFlight/778)

#Mac #Beta

Version 5.9.4-3138 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3138-f3659d1224c06859690b727ba4d3fafd.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 777](https://t.me/SurgeTestFlight/777)

#Mac #Beta

Version 5.9.4-3137 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3137-baeaee6daf966247473502eb82f4f220.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 776](https://t.me/SurgeTestFlight/776)

#Mac #Beta

Version 5.9.4-3136 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3136-3d1e27197efb997bc339b10c8ac31385.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 775](https://t.me/SurgeTestFlight/775)

#Mac #Beta

Version 5.9.4-3135 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3135-b4a7ed37821d6cc61ccb807be260185e.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 774](https://t.me/SurgeTestFlight/774)

#Mac #Beta

Version 5.9.4-3134 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3134-de7374de68b3acab356932023e2c6746.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-15 [post 773](https://t.me/SurgeTestFlight/773)

#Mac #Beta

Version 5.9.4-3133 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3133-6a2a93e1b7878b09d1a824b44ee2f0e1.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-14 [post 772](https://t.me/SurgeTestFlight/772)

#Mac #Beta

Version 5.9.4-3132 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3132-7827c5f81f78d5feba484e5300952bf5.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-13 [post 770](https://t.me/SurgeTestFlight/770)

#Mac #Beta

Version 5.9.4-3131 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3131-e7cbd8d43d59a16380e0c89516f61519.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-13 [post 769](https://t.me/SurgeTestFlight/769)

#Mac #Beta

Version 5.9.4-3130 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3130-2efbc5c26f1bb2b7ae095750dd5849df.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-12 [post 768](https://t.me/SurgeTestFlight/768)

#Mac #Beta

Version 5.9.4-3127 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3127-e87a6ed3d3510df75d607200b14029ce.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-12 [post 766](https://t.me/SurgeTestFlight/766)

#Mac #Beta

Version 5.9.4-3126 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3126-89d5b9236a3c71f7772df3bc90d397e7.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-12 [post 765](https://t.me/SurgeTestFlight/765)

#Mac #Beta

Version 5.9.4-3125 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3125-24aed8c13970d40f8c1966719a93b69e.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-11 [post 762](https://t.me/SurgeTestFlight/762)

#Mac #Beta

Version 5.9.4-3124 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3124-3f5e3d0805ee6e8665f50a3d9b77695b.zip

- Optimize using Smart policy groups as the underlying proxy. Now, in this usage scenario, the characteristics of Smart policy groups can be fully utilized. 
- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-10 [post 761](https://t.me/SurgeTestFlight/761)

#Mac #Beta

Version 5.9.4-3123 https://dl.nssurge.com/mac/v5/Surge-5.9.4-3123-158478726c1797e7f2f091a4d39e125c.zip

- Bug fixes and other improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-12-08 [post 756](https://t.me/SurgeTestFlight/756)

#Mac #Beta

Version 5.9.3-3122 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3122-0244efc5738b3cebde7c87c556cfddb8.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-08 [post 755](https://t.me/SurgeTestFlight/755)

#Mac #Beta

Version 5.9.3-3121 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3121-6db3a372836f3baec605b95c6c0aceb2.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-06 [post 754](https://t.me/SurgeTestFlight/754)

#Mac #Beta

Version 5.9.3-3120 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3120-d7c0ceda880f3484f79f017591931acd.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-05 [post 751](https://t.me/SurgeTestFlight/751)

#Mac #Beta

Version 5.9.3-3119 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3119-f2f36e317e39164232b1182a42679677.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-05 [post 748](https://t.me/SurgeTestFlight/748)

#Mac #Beta

Version 5.9.3-3118 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3118-866b5f3f756e40f638f83d9ddb47f14a.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-04 [post 747](https://t.me/SurgeTestFlight/747)

#Mac #Beta

Version 5.9.3-3117 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3117-f978eb173c49810b6f9ba38ee2cdefc2.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-04 [post 746](https://t.me/SurgeTestFlight/746)

#Mac #Beta

Version 5.9.3-3116 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3116-17d84f8e75384d4ffec74e80a7b24a14.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-03 [post 744](https://t.me/SurgeTestFlight/744)

#Mac #Beta

Version 5.9.3-3115 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3115-17f0bcd6982c1b37458c9ea6ada059d5.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-12-01 [post 741](https://t.me/SurgeTestFlight/741)

#Mac #Beta

Version 5.9.3-3112 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3112-7c88cbba44a4a7665853a961ca02de1c.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-29 [post 740](https://t.me/SurgeTestFlight/740)

#Mac #Beta

Version 5.9.3-3110 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3110-7ebd097c29492b4bb549d43943c8de06.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-27 [post 739](https://t.me/SurgeTestFlight/739)

#Mac #Beta

Version 5.9.3-3106 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3106-ef354d35939673c0d1b346b1458148ca.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-26 [post 737](https://t.me/SurgeTestFlight/737)

#Mac #Beta

Version 5.9.3-3105 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3105-3a468e3bd76625f27d22f86319176f0f.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-25 [post 735](https://t.me/SurgeTestFlight/735)

#Mac #Beta

Version 5.9.3-3104 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3104-8478aa3d5aa91a5cf176324f1d7b8536.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-25 [post 734](https://t.me/SurgeTestFlight/734)

#Mac #Beta

Version 5.9.3-3103 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3103-e4b196e4a4ba893561df8d955e8d31cd.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-24 [post 733](https://t.me/SurgeTestFlight/733)

#Mac #Beta

Version 5.9.3-3101 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3101-fe77cf8f73c22e423a54436a067ee0fe.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-22 [post 731](https://t.me/SurgeTestFlight/731)

#Mac #Beta

Version 5.9.3-3100 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3100-f1c6adaed3c2cac4c955b82943c23e74.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-22 [post 730](https://t.me/SurgeTestFlight/730)

#Mac #Beta

Version 5.9.3-3099 https://dl.nssurge.com/mac/v5/Surge-5.9.3-3099-cb5eb5fe7ca957b34979d9e36451f5e0.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 728](https://t.me/SurgeTestFlight/728)

#Mac #Beta

Version 5.9.2-3098 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3098-643c195efc1153b6d4993af6bba73a59.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 726](https://t.me/SurgeTestFlight/726)

#Mac #Beta

Version 5.9.2-3097 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3097-9417f0e2a2e8a76f23dbd43289cb11d3.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 725](https://t.me/SurgeTestFlight/725)

#Mac #Beta

Version 5.9.2-3096 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3096-35443110fcb077e5e626a9d7c35fd50b.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 724](https://t.me/SurgeTestFlight/724)

#Mac #Beta

Version 5.9.2-3095 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3095-00e4c1c2359dbabcc6e7d1f6fc953939.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 723](https://t.me/SurgeTestFlight/723)

#Mac #Beta

Version 5.9.2-3094 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3094-f61fd20d61b9d7a4917804e4e82775b6.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 722](https://t.me/SurgeTestFlight/722)

#Mac #Beta

Version 5.9.2-3092 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3092-62919203a4073d73f37c29af6ed36cef.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 721](https://t.me/SurgeTestFlight/721)

#Mac #Beta

Version 5.9.2-3091 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3091-34176b67c871cd09e793ec2c15904771.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 720](https://t.me/SurgeTestFlight/720)

#Mac #Beta

Version 5.9.2-3089 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3089-8acd25256d70a622ace8bd3f7263419c.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 719](https://t.me/SurgeTestFlight/719)

#Mac #Beta

Version 5.9.2-3088 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3088-5d81417c58ab4bbb8833b0f806743486.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 718](https://t.me/SurgeTestFlight/718)

#Mac #Beta

Version 5.9.2-3087 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3087-56e57d8b7991f20a59a8b6c83703f47f.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 717](https://t.me/SurgeTestFlight/717)

#Mac #Beta

Version 5.9.2-3086 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3086-6ebdf63b857d916bfdc1d10bf0b330aa.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 716](https://t.me/SurgeTestFlight/716)

#Mac #Beta

Version 5.9.2-3085 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3085-f3eceaf4d7402a344e1bbe33ee33d0dd.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 714](https://t.me/SurgeTestFlight/714)

#Mac #Beta

Version 5.9.1-3084 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3084-0f0e87ade5af5cc4f1276d1e1d29338e.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 712](https://t.me/SurgeTestFlight/712)

#Mac #Beta

Version 5.9.1-3083 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3083-48fd7ab2061420ad00045a002a28a77e.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-20 [post 710](https://t.me/SurgeTestFlight/710)

#Mac #Beta

Version 5.9.1-3082 https://dl.nssurge.com/mac/v5/Surge-5.9.2-3082-adf11a031da1da86a0c374fe2b711f85.zip

- The menu bar icon can now display the outbound mode.
- Fixed some issues related to Ponte.
- Fixed the issue where error messages on the DHCP configuration page sometimes could not be displayed, preventing further actions.
- Fixed an issue where the Host entry configured for .local domain names might be invalid.
- Optimized the proxy and rule editing pages; parameters that are not editable in the UI will now also be retained.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-11 [post 695](https://t.me/SurgeTestFlight/695)

#Mac #Beta

Version 5.9.1-3049 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3049-e74783f975ae324297af3cff6594f1fc.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-10 [post 655](https://t.me/SurgeTestFlight/655)

#Mac #Beta

Version 5.9.1-3046 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3046-f5f0fd90cf39a6403b2a5df92b3b8191.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-10 [post 654](https://t.me/SurgeTestFlight/654)

#Mac #Beta

Version 5.9.1-3045 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3045-597dc4fe0cee1198755c5ef903be7332.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-10 [post 653](https://t.me/SurgeTestFlight/653)

#Mac #Beta

Version 5.9.1-3043 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3043-acd14514fb51080745df4df464724bec.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-09 [post 652](https://t.me/SurgeTestFlight/652)

#Mac #Beta

Version 5.9.1-3042 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3042-1091a64ff809101151e6d0d770d651db.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-09 [post 651](https://t.me/SurgeTestFlight/651)

#Mac #Beta

Version 5.9.1-3040 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3040-91c430e872d32ebb77e0b22dafa23ac8.zip

- The menu bar icon can now display the outbound mode.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-08 [post 648](https://t.me/SurgeTestFlight/648)

#Mac #Beta

Version 5.9.1-3037 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3037-975bd33ac15904bc401f33978891d6fc.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-08 [post 647](https://t.me/SurgeTestFlight/647)

#Mac #Beta

Version 5.9.1-3036 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3036-67867ea9ac2d6328d6e4c524cc8ef2fe.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-07 [post 644](https://t.me/SurgeTestFlight/644)

#Mac #Beta

Version 5.9.1-3035 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3035-9cd9a1528facbb996a1f4770454aa0df.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-06 [post 643](https://t.me/SurgeTestFlight/643)

#Mac #Beta

Version 5.9.1-3034 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3034-3c39a84dd1c3d36cac20572dd579683d.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-06 [post 642](https://t.me/SurgeTestFlight/642)

#Mac #Beta

Version 5.9.1-3032 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3032-b0fe2b34ca837615aafe51bb98680d52.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 640](https://t.me/SurgeTestFlight/640)

#Mac #Beta

Version 5.9.1-3031 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3031-0e7a79b0320b7f1f3f95e2296a388cf6.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 639](https://t.me/SurgeTestFlight/639)

#Mac #Beta

Version 5.9.1-3030 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3030-4c56dbdd073a81191c0434a52e6f0378.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 638](https://t.me/SurgeTestFlight/638)

#Mac #Beta

Version 5.9.1-3029 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3029-ee16ac472ca6d25c477215ef5913b56f.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 637](https://t.me/SurgeTestFlight/637)

#Mac #Beta

Version 5.9.1-3028 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3028-3394161b09eabda94140e658ab328ce8.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 636](https://t.me/SurgeTestFlight/636)

#Mac #Beta

Version 5.9.1-3027 https://dl.nssurge.com/mac/v5/Surge-5.9.1-3027-493409541d3be18c36c851ac1821919f.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-31 [post 627](https://t.me/SurgeTestFlight/627)

#Mac #Beta

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

## 2024-10-31 [post 626](https://t.me/SurgeTestFlight/626)

#Mac #Beta

Version 5.9.0-3024 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3024-623d6215b0d4d3083ca6820cef21f3ba.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-31 [post 622](https://t.me/SurgeTestFlight/622)

#Mac #Beta

Version 5.9.0-3023 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3023-b8d9ee80ab30b6d9f38924a97f30003f.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-30 [post 621](https://t.me/SurgeTestFlight/621)

#Mac #Beta

Version 5.9.0-3022 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3022-9ab60ea77101ffe445f22029a7c97e64.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-30 [post 620](https://t.me/SurgeTestFlight/620)

#Mac #Beta

Version 5.9.0-3021 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3021-2e127eae297b58ba1a6e73323e5317e3.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-30 [post 619](https://t.me/SurgeTestFlight/619)

#Mac #Beta

Version 5.9.0-3020 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3020-f8cd2242eb4d588997948baf475a8e82.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-30 [post 618](https://t.me/SurgeTestFlight/618)

#Mac #Beta

Version 5.9.0-3019 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3019-e2572c28dff9d8a60c6b1a489b81e428.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-29 [post 617](https://t.me/SurgeTestFlight/617)

#Mac #Beta

Version 5.9.0-3018 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3018-ec00d31e3b271c94b7e72fedf5cf4cb4.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-29 [post 615](https://t.me/SurgeTestFlight/615)

#Mac #Beta

Version 5.9.0-3017 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3017-1fe42ab22718f9722e84fa115cf60810.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 614](https://t.me/SurgeTestFlight/614)

#Mac #Beta

Version 5.9.0-3016 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3016-a0e1acd97ea14faef08f6f5309fdf8bf.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 612](https://t.me/SurgeTestFlight/612)

#Mac #Beta

Version 5.9.0-3015 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3015-13abe31012b23a7a465818e1f2d770f8.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 611](https://t.me/SurgeTestFlight/611)

#Mac #Beta

Version 5.9.0-3014 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3014-737fa6bb86ca25d29b3edfc6fb6e96e7.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 609](https://t.me/SurgeTestFlight/609)

#Mac #Beta

Version 5.9.0-3012 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3012-c85ffdd8dc15af6988ecebc35d90ec84.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 608](https://t.me/SurgeTestFlight/608)

#Mac #Beta

Version 5.9.0-3010 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3010-712f1916c08c63bbbe2c14a6c8ff6dc2.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 605](https://t.me/SurgeTestFlight/605)

#Mac #Beta

Version 5.9.0-3009 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3009-64c42f491b55f2d2b39b7f73b3679f43.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 603](https://t.me/SurgeTestFlight/603)

#Mac #Beta

Version 5.9.0-3008 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3008-5261b8677007285f5f07f13c89e3280c.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 602](https://t.me/SurgeTestFlight/602)

#Mac #Beta

Version 5.9.0-3005 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3005-b74bd22b2581f00a83c656c03ece048d.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 601](https://t.me/SurgeTestFlight/601)

#Mac #Beta

Version 5.9.0-3004 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3004-cecfe550db0ca06ef58d14d1ce10e8a0.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 600](https://t.me/SurgeTestFlight/600)

#Mac #Beta

Version 5.9.0-3002 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3002-593c1fc961d8c3e55f49a0a1b0853026.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 598](https://t.me/SurgeTestFlight/598)

#Mac #Beta

Version 5.9.0-3001 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3001-f047fada558b7fa9ae5af35ac1d88404.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 597](https://t.me/SurgeTestFlight/597)

#Mac #Beta

Version 5.9.0-3000 https://dl.nssurge.com/mac/v5/Surge-5.9.0-3000-9235ddc03744d89736793e905396962b.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 592](https://t.me/SurgeTestFlight/592)

#Mac #Beta

Version 5.9.0-2999 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2999-9faa750057c11bde063f5b57aa3ebcc3.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-26 [post 591](https://t.me/SurgeTestFlight/591)

#Mac #Beta

Version 5.9.0-2998 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2998-28e73320f2b6cbe1e55b4b2d2050216b.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-26 [post 590](https://t.me/SurgeTestFlight/590)

#Mac #Beta

Version 5.9.0-2997 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2997-7160b5df4af64d5861d074eb6232f76d.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-25 [post 588](https://t.me/SurgeTestFlight/588)

#Mac #Beta

Version 5.9.0-2996 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2996-ca5edc11fc92c58e0514ad7bae0e8fcd.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 586](https://t.me/SurgeTestFlight/586)

#Mac #Beta

Version 5.9.0-2995 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2995-a4da8f57526f9c3d5237c086f18468cf.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 585](https://t.me/SurgeTestFlight/585)

#Mac #Beta

Version 5.9.0-2994 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2994-3c97d2dd6f39f3cfe41f5cea58a8ea73.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 581](https://t.me/SurgeTestFlight/581)

#Mac #Beta

Version 5.9.0-2992 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2992-8a3ec43650ab2c30a3a04012009776dd.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 580](https://t.me/SurgeTestFlight/580)

#Mac #Beta

Version 5.9.0-2990 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2990-f5f48fb48dd2015b3b9f4996a8656b68.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 579](https://t.me/SurgeTestFlight/579)

#Mac #Beta

Version 5.9.0-2989 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2989-5e5535c70f7fc945516af7770eb3d5b6.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 577](https://t.me/SurgeTestFlight/577)

#Mac #Beta

Version 5.9.0-2988 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2988-c029b07f32bd2b963261f20122b1846d.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 575](https://t.me/SurgeTestFlight/575)

#Mac #Beta

Version 5.9.0-2987 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2987-bdcb22dd18cf8a51138fd83f6532c307.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 574](https://t.me/SurgeTestFlight/574)

#Mac #Beta

Version 5.9.0-2986 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2986-601a607c0be3de9d23a6300a4acbd030.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 572](https://t.me/SurgeTestFlight/572)

#Mac #Beta

Version 5.9.0-2985 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2985-d3ea2d6b5aa9611ae752e3bf75405ec5.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 570](https://t.me/SurgeTestFlight/570)

#Mac #Beta

Version 5.9.0-2984 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2984-4e1fe0429a29189768f0421aa46d5708.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 569](https://t.me/SurgeTestFlight/569)

#Mac #Beta

Version 5.8.3-2981 https://dl.nssurge.com/mac/v5/Surge-5.9.0-2981-8f65f2a7f6202619c480856bc6296cec.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-22 [post 568](https://t.me/SurgeTestFlight/568)

#Mac #Beta

Version 5.8.3-2980 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2980-4e4ceb3b04c1cebb0b646dcadc297072.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-22 [post 566](https://t.me/SurgeTestFlight/566)

#Mac #Beta

Version 5.8.3-2979 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2979-345fc2aa6d2d5dae1b5addd86fdc9d62.zip

- Added pre-matching feature for low-overhead request rejection. Please refer to the documentation for details. https://manual.nssurge.com/policy/reject.html https://manual.nssurge.com/policy/reject.html
- The URL-REGEX rule now supports extended-matching tags.
- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-21 [post 564](https://t.me/SurgeTestFlight/564)

#Mac #Beta

Version 5.8.3-2978 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2978-51b72489aaee5cb8d8626740fc10c48f.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-20 [post 561](https://t.me/SurgeTestFlight/561)

#Mac #Beta

Version 5.8.3-2977 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2977-b29607c1a7bb870a9459bd2f94c25870.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 559](https://t.me/SurgeTestFlight/559)

#Mac #Beta

Version 5.8.3-2975 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2975-dd844391b171a7c3511e38bce8d0d207.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 556](https://t.me/SurgeTestFlight/556)

#Mac #Beta

Version 5.8.3-2974 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2974-70eeebaf0f3726d45054043807750df8.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 555](https://t.me/SurgeTestFlight/555)

#Mac #Beta

Version 5.8.3-2973 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2973-d1d5ffcb4d3b4763e1fee2635480beba.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 551](https://t.me/SurgeTestFlight/551)

#Mac #Beta

Version 5.8.3-2972 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2972-b3a8d32c63347a94a7589a86061a866c.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 550](https://t.me/SurgeTestFlight/550)

#Mac #Beta

Version 5.8.3-2971 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2971-b067b8db2dbe13634dc3538fa090bd71.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 547](https://t.me/SurgeTestFlight/547)

#Mac #Beta

Version 5.8.3-2970 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2970-1333083e45b2c354d45d34fd2359cfbf.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 545](https://t.me/SurgeTestFlight/545)

#Mac #Beta

Version 5.8.3-2968 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2968-36744890c012c37d57eb607f51080ff5.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.
- Added parameter ipv6-vif-route-mode, with options: auto, default, gua, manual. Please refer to the manual for more information.

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 542](https://t.me/SurgeTestFlight/542)

#Mac #Beta

Version 5.8.3-2967 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2967-2316b9d2c3088002c6c7c9ac73387135.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.
- Added parameter ipv6-vif-route-mode, with options: auto, default, gua, manual. Please refer to the manual for more information.

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 538](https://t.me/SurgeTestFlight/538)

#Mac #Beta

Version 5.8.3-2966 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2966-37043e948ab76b86fea4047ea67b947c.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 536](https://t.me/SurgeTestFlight/536)

#Mac #Beta

Version 5.8.3-2963 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2963-e122f175956da22480fb351a77f47665.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 535](https://t.me/SurgeTestFlight/535)

#Mac #Beta

Version 5.8.3-2959 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2959-b5cc5310bebcb1989247669893e49483.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 534](https://t.me/SurgeTestFlight/534)

#Mac #Beta

Version 5.8.3-2958 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2958-3ca72bb719e85549514bf3e45b9152c7.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 533](https://t.me/SurgeTestFlight/533)

#Mac #Beta

Version 5.8.3-2957 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2957-a1349980ac35db4cd93f5d6d7f423430.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.
- Fix the issue where DNS requests cannot select the correct interface according to the routing table in enhanced mode.

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 531](https://t.me/SurgeTestFlight/531)

#Mac #Beta

Version 5.8.3-2956 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2956-c012daa819e42281fd708f21a9086dde.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.

Official Channel: @SurgeTestFlightFeed

## 2024-10-16 [post 530](https://t.me/SurgeTestFlight/530)

#Mac #Beta

Version 5.8.3-2955 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2955-43c0ea0de85ee5b389e75f523435377c.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.

Official Channel: @SurgeTestFlightFeed

## 2024-10-16 [post 527](https://t.me/SurgeTestFlight/527)

#Mac #Beta

Version 5.8.3-2952 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2952-a2a20f61a2d908de9dfc1aa79c97dc03.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes
- Allow the use of Ponte policy as an underlying proxy.

Official Channel: @SurgeTestFlightFeed

## 2024-10-16 [post 526](https://t.me/SurgeTestFlight/526)

#Mac #Beta

Version 5.8.3-2951 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2951-b4f3405d4e01b1d9804e2c32a18d541d.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 522](https://t.me/SurgeTestFlight/522)

#Mac #Beta

Version 5.8.3-2950 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2950-d21b3411488833acccb283845d751fbb.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 520](https://t.me/SurgeTestFlight/520)

#Mac #Beta

Version 5.8.3-2949 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2949-56693ef5ce9bca24e2633da2b8e51093.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 515](https://t.me/SurgeTestFlight/515)

#Mac #Beta

Version 5.8.3-2948 https://dl.nssurge.com/mac/v5/Surge-5.8.3-2948-301bcc95415c0af198c821d8669e2cee.zip

- The shadowsocks protocol adds support for the 2022-blake3-aes-256-gcm and 2022-blake3-aes-128-gcm encryption modes.

Official Channel: @SurgeTestFlightFeed

## 2024-10-12 [post 510](https://t.me/SurgeTestFlight/510)

#Mac #Beta

Version 5.8.2-2946 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2946-b739968f1d90da3b755d3bf82941e8c2.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-12 [post 508](https://t.me/SurgeTestFlight/508)

#Mac #Beta

Version 5.8.2-2944 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2944-5710edb27c22e45598c01c4549bcd3eb.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-11 [post 507](https://t.me/SurgeTestFlight/507)

#Mac #Beta

Version 5.8.2-2943 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2943-d6371752eea03feb9e8c034049cdb68a.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-11 [post 506](https://t.me/SurgeTestFlight/506)

#Mac #Beta

Version 5.8.2-2941 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2941-25328499f722486f7d047b972316e512.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-11 [post 505](https://t.me/SurgeTestFlight/505)

#Mac #Beta

Version 5.8.2-2940 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2940-d4491b06cbdae3a651f5719467210766.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-11 [post 503](https://t.me/SurgeTestFlight/503)

#Mac #Beta

Version 5.8.2-2939 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2939-a36e9137bf0a939d4f114790ac8a2fc4.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-10 [post 498](https://t.me/SurgeTestFlight/498)

#Mac #Beta

Version 5.8.2-2937 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2937-6e0a120c6e00d3e428795ab239c4cf93.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-09 [post 497](https://t.me/SurgeTestFlight/497)

#Mac #Beta

Version 5.8.2-2936 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2936-72f3d5efe4772611094404863700ad91.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-09 [post 496](https://t.me/SurgeTestFlight/496)

#Mac #Beta

Version 5.8.2-2935 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2935-246f6a015bb1eae4d98e815f48ffd5ea.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-10-08 [post 493](https://t.me/SurgeTestFlight/493)

#Mac #Beta

Version 5.8.2-2934 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2934-55c0551bb24dc974303646d04afe7b46.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-26 [post 491](https://t.me/SurgeTestFlight/491)

#Mac #Beta

Version 5.8.2-2933 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2933-2081744ed8035cab1a2c750f3d463452.zip

- Fix the issue where IPv6 VIF cannot take over requests when the gateway-restricted-to-lan parameter is enabled.
- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-26 [post 490](https://t.me/SurgeTestFlight/490)

#Mac #Beta

Version 5.8.2-2932 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2932-5f3b219b3f960562f5bbd9d81fd8d3c4.zip

- DNS lookup of use-application-dns.net will return NXDOMAIN, causing Firefox to automatically disable application DNS, (i.e., DoH). Using encrypted DNS directly in the browser will prevent Surge from correctly obtaining the requested domain names.
- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-26 [post 489](https://t.me/SurgeTestFlight/489)

#Mac #Beta

Version 5.8.2-2931 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2931-f75c095a65b8573e0900d702d532010d.zip

- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-25 [post 487](https://t.me/SurgeTestFlight/487)

#Mac #Beta

Version 5.8.2-2930 https://dl.nssurge.com/mac/v5/Surge-5.8.2-2930-4bb04738aab41a6a09af5276ce4e5099.zip

- Bug fixes and minor improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-24 [post 483](https://t.me/SurgeTestFlight/483)

#Mac #Beta

Version 5.8.1-2929 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2929-5220af95366dfacec7ca84cb8ddd122c.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-24 [post 482](https://t.me/SurgeTestFlight/482)

#Mac #Beta

Version 5.8.1-2928 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2928-2aaa79a68427b0aec1348bf1ebe8ad3a.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-24 [post 481](https://t.me/SurgeTestFlight/481)

#Mac #Beta

Version 5.8.1-2927 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2927-59bafac8834dab5e88c8bdec0cccf5f1.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-24 [post 480](https://t.me/SurgeTestFlight/480)

#Mac #Beta

Version 5.8.1-2926 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2926-4aeaab96ec9c7252dd6c0196d95453a4.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-24 [post 478](https://t.me/SurgeTestFlight/478)

#Mac #Beta

Version 5.8.1-2925 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2925-756201cb629b4be935c6d94c07ff8eed.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-23 [post 475](https://t.me/SurgeTestFlight/475)

#Mac #Beta

Version 5.8.1-2923 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2923-a084a34077c05dc08b3c938792a0aa73.zip

      
 - New parameters: proxy-restricted-to-lan/gateway-restricted-to-lan
    It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and gateway services to only accept devices from the current subnet. These two parameters are enabled by default.
- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 473](https://t.me/SurgeTestFlight/473)

#Mac #Beta

Version 5.8.1-2922 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2922-ea1af8ef8e6fba8dbe2845d666fd76ac.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 472](https://t.me/SurgeTestFlight/472)

#Mac #Beta

Version 5.8.1-2921 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2921-cebe16473b6cdd99dfcd40d12f28fa98.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 471](https://t.me/SurgeTestFlight/471)

#Mac #Beta

Version 5.8.1-2920 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2920-8ddbc2a0028eb9b19ba7b8aa7ab6bfa0.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 470](https://t.me/SurgeTestFlight/470)

#Mac #Beta

Version 5.8.1-2919 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2919-4d5bda7f7d013837e3899fdd2343a280.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 469](https://t.me/SurgeTestFlight/469)

#Mac #Beta

Version 5.8.1-2917 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2917-7c7e7c467950bf9a82556d06c5e5b88b.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-22 [post 468](https://t.me/SurgeTestFlight/468)

#Mac #Beta

Version 5.8.1-2916 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2916-271ab390a6482219eec326c43e0e1f75.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-21 [post 467](https://t.me/SurgeTestFlight/467)

#Mac #Beta

Version 5.8.1-2915 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2915-ead768eac14631ebe1a446311dc05bd4.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-20 [post 465](https://t.me/SurgeTestFlight/465)

#Mac #Beta

Version 5.8.1-2914 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2914-f137575c7d31d70ee879664039d2c050.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-19 [post 464](https://t.me/SurgeTestFlight/464)

#Mac #Beta

Version 5.8.1-2913 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2913-ffd6b2eabd88b79aae36b4e855a7ae67.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-19 [post 462](https://t.me/SurgeTestFlight/462)

#Mac #Beta

Version 5.8.1-2912 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2912-196c4b9d60212295d3a76fee1019624f.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-19 [post 461](https://t.me/SurgeTestFlight/461)

#Mac #Beta

Version 5.8.1-2911 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2911-f9fa51774e531f687b7c20a6dbc85326.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Surge now supports handling the system's DNS search domain settings.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-19 [post 460](https://t.me/SurgeTestFlight/460)

#Mac #Beta

Version 5.8.1-2910 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2910-6156ff57fdcdc403023b596ba31e56d5.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.
- Other bug fixes and compatibility improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-09-18 [post 458](https://t.me/SurgeTestFlight/458)

#Mac #Beta

Version 5.8.1-2909 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2909-c159c0d700c2c7ecc8fc38f14c61bcfc.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.
- Support using ETag to avoid downloading duplicate data when requesting external resources.

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 457](https://t.me/SurgeTestFlight/457)

#Mac #Beta

Version 5.8.1-2908 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2908-2863e52b66bc6af43caffb242c29792a.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 456](https://t.me/SurgeTestFlight/456)

#Mac #Beta

Version 5.8.1-2907 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2907-8f41538861ee6494507dcc88af7aedc4.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 455](https://t.me/SurgeTestFlight/455)

#Mac #Beta

Version 5.8.1-2905 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2905-118459b5d6df712227ed81ea85f7ee96.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 454](https://t.me/SurgeTestFlight/454)

#Mac #Beta

Version 5.8.1-2903 https://dl.nssurge.com/mac/v5/Surge-5.8.1-2903-53022cd91e240c5505b78a75140217cf.zip

- Fix the compatibility between enhanced mode and PPPoE direct dialing.

Official Channel: @SurgeTestFlightFeed

## 2024-09-16 [post 450](https://t.me/SurgeTestFlight/450)

#Mac #Beta

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

## 2024-09-16 [post 449](https://t.me/SurgeTestFlight/449)

#Mac #Beta

Version 5.8.0-2899 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2899-67ac400c68cc22776ad0428dd5808fc4.zip

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

## 2024-09-16 [post 448](https://t.me/SurgeTestFlight/448)

#Mac #Beta

Version 5.8.0-2898 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2898-64ae683666621c279f08fc64cce76e6a.zip

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

## 2024-09-16 [post 447](https://t.me/SurgeTestFlight/447)

#Mac #Beta

Version 5.8.0-2894 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2894-39931b3ce3d5b344af01644082819d3c.zip

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

## 2024-09-16 [post 446](https://t.me/SurgeTestFlight/446)

#Mac #Beta

Version 5.8.0-2893 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2893-55e032ecfccde3a63b0e112060a6bc2e.zip

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

## 2024-09-16 [post 445](https://t.me/SurgeTestFlight/445)

#Mac #Beta

Version 5.8.0-2892 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2892-5839f95b4a516686ba6e081e6af9ee44.zip

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

## 2024-09-16 [post 444](https://t.me/SurgeTestFlight/444)

#Mac #Beta

Version 5.8.0-2891 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2891-6cdf70ef384b9cf2be4d39ce7f9a38f7.zip

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

## 2024-09-16 [post 443](https://t.me/SurgeTestFlight/443)

#Mac #Beta

Version 5.8.0-2890 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2890-af0b983dd66a83f6f3177aa038b63693.zip

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

## 2024-09-16 [post 440](https://t.me/SurgeTestFlight/440)

#Mac #Beta

Version 5.8.0-2889 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2889-a58c59afc3e3208a76a3111bcbbdef04.zip

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

## 2024-09-16 [post 439](https://t.me/SurgeTestFlight/439)

#Mac #Beta

Version 5.8.0-2888 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2888-6017bbc5aa759ea2080a48670f0be774.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-15 [post 438](https://t.me/SurgeTestFlight/438)

#Mac #Beta

Version 5.8.0-2887 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2887-2ba6c90a2caf4d1996c41db365ed5cb7.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-15 [post 437](https://t.me/SurgeTestFlight/437)

#Mac #Beta

Version 5.8.0-2886 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2886-c79446b965983591b056673af7fc2cf0.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-15 [post 435](https://t.me/SurgeTestFlight/435)

#Mac #Beta

Version 5.8.0-2885 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2885-f66270eb721f45e543e13b56546da57f.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-13 [post 434](https://t.me/SurgeTestFlight/434)

#Mac #Beta

Version 5.8.0-2883 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2883-98d1d38e608c5a6b321dcc0471f62f38.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-13 [post 433](https://t.me/SurgeTestFlight/433)

#Mac #Beta

Version 5.8.0-2882 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2882-e07a471d00b4571f3aa1b08cc88dd540.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-13 [post 432](https://t.me/SurgeTestFlight/432)

#Mac #Beta

Version 5.8.0-2881 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2881-84388a200ad9cb9687609e75592fa032.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-12 [post 431](https://t.me/SurgeTestFlight/431)

#Mac #Beta

Version 5.8.0-2880 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2880-249579a9bdc9ae943410d67cecbdfe18.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-12 [post 430](https://t.me/SurgeTestFlight/430)

#Mac #Beta

Version 5.8.0-2876 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2876-ba6adb4ed1780b97c4ea80a80169d8ef.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-12 [post 429](https://t.me/SurgeTestFlight/429)

#Mac #Beta

Version 5.8.0-2875 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2875-0b47801f34ae34198eb0590951c85486.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-12 [post 428](https://t.me/SurgeTestFlight/428)

#Mac #Beta

Version 5.8.0-2874 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2874-87225c56b65880d71098413b9dd7d2e4.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-12 [post 427](https://t.me/SurgeTestFlight/427)

#Mac #Beta

Version 5.8.0-2873 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2873-58e8130739e93c0c847e3c3151462d59.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-11 [post 425](https://t.me/SurgeTestFlight/425)

#Mac #Beta

Version 5.8.0-2871 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2871-a6d73cb9cc6a7a359601ba12efdf0808.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-10 [post 424](https://t.me/SurgeTestFlight/424)

#Mac #Beta

Version 5.8.0-2870 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2870-4b0fa33bd9dd01f97811471df9ef0d79.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-10 [post 423](https://t.me/SurgeTestFlight/423)

#Mac #Beta

Version 5.8.0-2869 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2869-fa959b3db33419a154b8972a928cb4d9.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-10 [post 422](https://t.me/SurgeTestFlight/422)

#Mac #Beta

Version 5.8.0-2868 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2868-4396f5912cfa3c47e2ef4eda198effcb.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-10 [post 421](https://t.me/SurgeTestFlight/421)

#Mac #Beta

Version 5.8.0-2865 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2865-6e3f9c86fa9e3195cde0381c75559abc.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-09 [post 419](https://t.me/SurgeTestFlight/419)

#Mac #Beta

Version 5.8.0-2864 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2864-aef116e5e8a06895e13342dc2bddf267.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-09 [post 418](https://t.me/SurgeTestFlight/418)

#Mac #Beta

Version 5.8.0-2863 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2863-d3f34620cf20d03298249e1411783f17.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-09 [post 417](https://t.me/SurgeTestFlight/417)

#Mac #Beta

Version 5.8.0-2862 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2862-0ecc20564890cd69a41a8f0bccf1cca7.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-09 [post 416](https://t.me/SurgeTestFlight/416)

#Mac #Beta

Version 5.8.0-2861 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2861-f27dc4da62be06e84cfe2c05afdb18ac.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-08 [post 415](https://t.me/SurgeTestFlight/415)

#Mac #Beta

Version 5.8.0-2860 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2860-86ffe34c920a669a75a1e33f8da511b6.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-08 [post 414](https://t.me/SurgeTestFlight/414)

#Mac #Beta

Version 5.8.0-2859 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2859-9f80092f76a5cba572f4d708ba882fc5.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-08 [post 413](https://t.me/SurgeTestFlight/413)

#Mac #Beta

Version 5.8.0-2858 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2858-ac72f9c3862ef7f5a7da32bceea656b3.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-08 [post 412](https://t.me/SurgeTestFlight/412)

#Mac #Beta

Version 5.8.0-2857 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2857-acc582fe599a8f04d225281625b64aa1.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-08 [post 411](https://t.me/SurgeTestFlight/411)

#Mac #Beta

Version 5.8.0-2855 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2855-04774950d9d2024de012443d9e27b373.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 410](https://t.me/SurgeTestFlight/410)

#Mac #Beta

Version 5.8.0-2854 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2854-b7dd6d71c6fa5a57367c32573cc59921.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 409](https://t.me/SurgeTestFlight/409)

#Mac #Beta

Version 5.8.0-2853 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2853-5ba4c9386d58dea4793122c7f309ad90.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 408](https://t.me/SurgeTestFlight/408)

#Mac #Beta

Version 5.8.0-2852 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2852-77b860b6356f7aed1e1c9b23ff33c39b.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 406](https://t.me/SurgeTestFlight/406)

#Mac #Beta

Version 5.8.0-2851 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2851-cb6e6c6217fafda56a2af124e4645d9e.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 404](https://t.me/SurgeTestFlight/404)

#Mac #Beta

Version 5.8.0-2850 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2850-7f9324778f2fd958bb380e9b83c9af4f.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-06 [post 403](https://t.me/SurgeTestFlight/403)

#Mac #Beta

Version 5.8.0-2848 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2848-120f552faff37c9832f3318b1a3da952.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-06 [post 402](https://t.me/SurgeTestFlight/402)

#Mac #Beta

Version 5.8.0-2846 https://dl.nssurge.com/mac/v5/Surge-5.8.0-2846-400c093650688a9732cec5114260235a.zip

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

Official Channel: @SurgeTestFlightFeed

## 2024-09-05 [post 399](https://t.me/SurgeTestFlight/399)

#Mac #Beta

Version 5.7.6-2838 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2838-88428d555171a036743cfd9287e5326e.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-05 [post 397](https://t.me/SurgeTestFlight/397)

#Mac #Beta

Version 5.7.6-2837 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2837-ab988403bb0ef1369da8043b141c616c.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-04 [post 395](https://t.me/SurgeTestFlight/395)

#Mac #Beta

Version 5.7.6-2836 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2836-c7a541ba54e8cad7cbf085fefb795798.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-04 [post 393](https://t.me/SurgeTestFlight/393)

#Mac #Beta

Version 5.7.6-2835 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2835-5ffcba2a49df4edd76194bb7fbf997d6.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-04 [post 392](https://t.me/SurgeTestFlight/392)

#Mac #Beta

Version 5.7.6-2834 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2834-81be2e1af60ca875affc0a5170a3735b.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-04 [post 390](https://t.me/SurgeTestFlight/390)

#Mac #Beta

Version 5.7.6-2833 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2833-be3bde56b776863520e3c9cca1e32a9f.zip

- Adapted for macOS Sequoia, resolved some compatibility issues in enhanced mode.
- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-03 [post 388](https://t.me/SurgeTestFlight/388)

#Mac #Beta

Version 5.7.6-2832 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2832-a7f201e996ed29365898e6bc6f3e1ade.zip

- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234,5000-6000,7044,8000-9000", port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured in the front will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-09-02 [post 384](https://t.me/SurgeTestFlight/384)

#Mac #Beta

Version 5.7.6-2827 https://dl.nssurge.com/mac/v5/Surge-5.7.6-2827-2309a86552639c18119dc4d5a7f87bcc.zip

- Hysteria2 and TUIC protocol now support port hopping to improve ISP's QoS issues with UDP. See the server documentation for details.

    Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping=1234,5000-6000,7044,8000-9000, port-hopping-interval=30

    After configuring the port-hopping parameter, the primary port number configured earlier will no longer be effective.

    Parameters:

    - port-hopping: Used to configure the range of ports. Separated by commas and supports ranges configured with a hyphen.
    - port-hopping-interval: The interval for changing port numbers. Defaults to 30 seconds

Official Channel: @SurgeTestFlightFeed

## 2024-08-30 [post 381](https://t.me/SurgeTestFlight/381)

#Mac #Beta

Version 5.7.5-2826 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-27 [post 377](https://t.me/SurgeTestFlight/377)

#Mac #Beta

Version 5.7.5-2825 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2825-86a2cf712dd6244511713d2028d50c54.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-27 [post 376](https://t.me/SurgeTestFlight/376)

#Mac #Beta

Version 5.7.5-2824 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2824-9e219fabefc798a7eaefb2743eb2eefd.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-27 [post 375](https://t.me/SurgeTestFlight/375)

#Mac #Beta

Version 5.7.5-2822 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2822-7ec45dcd3d79f8efd6e71a7cf5820cca.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-26 [post 371](https://t.me/SurgeTestFlight/371)

#Mac #Beta

Version 5.7.5-2821 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2821-7a543d39f1e07dd38624d52d65f2a156.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-19 [post 369](https://t.me/SurgeTestFlight/369)

#Mac #Beta

Version 5.7.5-2820 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2820-53f76831b40094b44f0415603b1ec023.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-18 [post 368](https://t.me/SurgeTestFlight/368)

#Mac #Beta

Version 5.7.5-2818 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2818-7be1c0c800360b00aaf1b955c805cb69.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-14 [post 367](https://t.me/SurgeTestFlight/367)

#Mac #Beta

Version 5.7.5-2817 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2817-fa11bdfba49b50410690af89f7663f0e.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-06 [post 359](https://t.me/SurgeTestFlight/359)

#Mac #Beta

Version 5.7.5-2816 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2816-dd9dfd0dbece7298d88763a6df2f5c75.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-08-04 [post 351](https://t.me/SurgeTestFlight/351)

#Mac #Beta

Version 5.7.5-2815 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2815-5cbe01e37d8a5221967f48a4e58e5a8a.zip

- DNS Forwarding Subsystem Optimization

    - When the domain of a DNS query is one that should not be forwarded to the public network (e.g., .home.arpa, 1.0.168.192.in-addr.arpa http://1.0.168.192.in-addr.arpa/), it will automatically determine the upstream DNS address and only forward to LAN DNS servers.
    - Surge can now correctly respond to PTR requests for fake IPs, meaning that using the dig -x 198.18.23.87 command can be used to determine the original domain name corresponding to a fake IP.
    - The DNS forwarder will now forward DNS requests to specific upstream servers based on [Host] section configuration.
    - Directly respond with NOTIMP to unsupported DNS-SD PTR requests for fake IPs, without forwarding.
      
- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-12 [post 341](https://t.me/SurgeTestFlight/341)

#Mac #Beta

Version 5.7.5-2814 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2814-081571e549f84d066c08c549cb81de19.zip

- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-11 [post 340](https://t.me/SurgeTestFlight/340)

#Mac #Beta

Version 5.7.5-2813 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2813-0d6eac8e0d56b337bdccc423d6041fdd.zip

- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-10 [post 338](https://t.me/SurgeTestFlight/338)

#Mac #Beta

Version 5.7.5-2812 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2812-68a529a4b73f3a6541fbfdbba690c5bd.zip

- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-10 [post 337](https://t.me/SurgeTestFlight/337)

#Mac #Beta

Version 5.7.5-2811 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2811-9ef864e8f6b4be937f549dba9d461eb1.zip

- Panel is now available in Surge Mac.
- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-08 [post 332](https://t.me/SurgeTestFlight/332)

#Mac #Beta

Version 5.7.5-2810 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2810-e9aa4e9956bfa4149a51d62d654261e7.zip

- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-07-02 [post 329](https://t.me/SurgeTestFlight/329)

#Mac #Beta

Version 5.7.5-2809 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2809-c913f8017e1892ee4040cbdbca9c0a19.zip

- When adding a rule for the current webpage, you can choose to add to an existing ruleset.
- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-06-27 [post 323](https://t.me/SurgeTestFlight/323)

#Mac #Beta

Version 5.7.5-2808 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2808-7b8ba2161f3d097b14fb913ee4da31b3.zip

- When adding a rule for the current webpage, you can choose to add to an existing ruleset.

Official Channel: @SurgeTestFlightFeed

## 2024-06-27 [post 321](https://t.me/SurgeTestFlight/321)

#Mac #Beta

Version 5.7.5-2807 https://dl.nssurge.com/mac/v5/Surge-5.7.5-2807-047a93db94f7ce00d0d6f2af636fcc70.zip

- When adding a rule for the current webpage, you can choose to add to an existing ruleset.

Official Channel: @SurgeTestFlightFeed

## 2024-06-21 [post 303](https://t.me/SurgeTestFlight/303)

#Mac #Beta

Version 5.7.4-2806 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2806-afe67661ef616b7bbab189dec1473b68.zip

- Due to the sudden shutdown of a public STUN server that Surge Ponte relies on, resulting in the unavailability of Surge Ponte, we have carried out an emergency replacement. Additionally, we will build our own STUN server in the future to avoid such issues.
- Enhance compatibility with VPN and multiple network cards

    In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

    However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

    This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.
    
- Fix an issue where DOMAIN-SUFFIX rules may become invalid if duplicate DOMAIN and DOMAIN-SUFFIX rules are included in the rule set
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-06-21 [post 298](https://t.me/SurgeTestFlight/298)

#Mac #Beta

Version 5.7.4-2805 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2805-bc9f3a083975f73e9d03ae05ee60eda8.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-20 [post 297](https://t.me/SurgeTestFlight/297)

#Mac #Beta

Version 5.7.4-2804 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2804-a78b4540108257f4ca57722295946748.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-19 [post 296](https://t.me/SurgeTestFlight/296)

#Mac #Beta

Version 5.7.4-2803 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2803-3a2e096d2b0847f7a58d40e2c416f214.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-19 [post 295](https://t.me/SurgeTestFlight/295)

#Mac #Beta

Version 5.7.4-2802 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2802-b3d226258867fe1159d41d822e289d5d.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-18 [post 293](https://t.me/SurgeTestFlight/293)

#Mac #Beta

Version 5.7.4-2801 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2801-4e333390b5ac2bbd9c4d12496fc3c967.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-18 [post 292](https://t.me/SurgeTestFlight/292)

#Mac #Beta

Version 5.7.4-2800 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2800-30adf8452fb58da0841a28eb8554c0ce.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-18 [post 291](https://t.me/SurgeTestFlight/291)

#Mac #Beta

Version 5.7.4-2799 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2799-8c441689dc6a378cc7a200cf5769a515.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-17 [post 290](https://t.me/SurgeTestFlight/290)

#Mac #Beta

Version 5.7.4-2796 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2796-b20660cb81eb20f189cb8389c78dea83.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-17 [post 288](https://t.me/SurgeTestFlight/288)

#Mac #Beta

Version 5.7.4-2795 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2795-9385fe8faf831cf8e146c6a75bca635e.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-16 [post 286](https://t.me/SurgeTestFlight/286)

#Mac #Beta

Version 5.7.4-2794 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2794-006d79cc8f47df8704ccad49df2a48c7.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-15 [post 283](https://t.me/SurgeTestFlight/283)

#Mac #Beta

Version 5.7.4-2793 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2793-cfeda06cc6a67476cfe3a79726cc64ac.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-13 [post 278](https://t.me/SurgeTestFlight/278)

#Mac #Beta

Version 5.7.4-2792 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2792-6c9f2a3c7c888d994ba4aeb5ab5042fb.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-10 [post 269](https://t.me/SurgeTestFlight/269)

#Mac #Beta

Version 5.7.4-2791 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2791-11306ce15d092daade6424f9be478a5e.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-06 [post 268](https://t.me/SurgeTestFlight/268)

#Mac #Beta

Version 5.7.4-2790 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2790-b4218202311dd6b8e9d8099d4ef6c773.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-04 [post 258](https://t.me/SurgeTestFlight/258)

#Mac #Beta

Version 5.7.4-2789 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2789-36cdcf215366e3b8572b3ff0e0140186.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-03 [post 256](https://t.me/SurgeTestFlight/256)

#Mac #Beta

Version 5.7.4-2788 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2788-3dbd0a603640eac83fe5be71d9d838f2.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-01 [post 255](https://t.me/SurgeTestFlight/255)

#Mac #Beta

Version 5.7.4-2787 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2787-dd12cb87af672e930de42b15baf1399e.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for TCP/UDP packets if there are higher priority sub-routes present, enhancing compatibility.

Official Channel: @SurgeTestFlightFeed

## 2024-06-01 [post 252](https://t.me/SurgeTestFlight/252)

#Mac #Beta

Version 5.7.4-2786 https://dl.nssurge.com/mac/v5/Surge-5.7.4-2786-4c5edf529df49797930b69dbc9d0345f.zip

In previous versions, if the enhanced mode was enabled, all outgoing packets would be forced to use the primary interface due to Surge overriding the system's routing table. This bypassed the routing table to avoid creating a loop.

However, this also caused issues where packets could not be sent from the correct interface in cases with multiple network cards or other VPNs.

This version improves on that design. Now, in enhanced mode, Surge will automatically check routes and still use standard routing for UDP packets (mainly DNS) if there are higher priority sub-routes present, enhancing compatibility. However, automatic determination for TCP packets is currently not supported and still requires manual configuration through DIRECT policy aliases.

Official Channel: @SurgeTestFlightFeed

## 2024-05-29 [post 250](https://t.me/SurgeTestFlight/250)

#Mac #Beta

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

## 2024-05-27 [post 246](https://t.me/SurgeTestFlight/246)

#Mac #Beta

Version 5.7.3-2783 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2783-ffbb4c2e3aac8b728ffcf2170cc50418.zip

- Now you can see the number of times a rule has been used in the rule list.
- Optimized the implementation method of blocking QUIC traffic to increase the likelihood of clients correctly falling back.
- The Smart group will use the SUBSTITUTE policy (DIRECT) instead of failing directly when there are no sub-policies.
- Fixed an issue where the server-cert-fingerprint-sha256 parameter was not effective for TLS-like protocols with sni=off settings.
- Added a new rule type HOSTNAME-TYPE, used to determine the type of request hostname. Optional values are: IPv4, IPv6, DOMAIN, SIMPLE. (SIMPLE refers to hostnames without a dot, such as localhost)
- Optimized DNS request logs. Now more information is displayed. Additionally, if DIRECT policy connects directly without triggering DNS in the rule system, related DNS logs can still be shown.
- When deleting a policy that is being used by a policy group, it is now allowed to delete it directly and automatically remove it from all policy groups.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-27 [post 243](https://t.me/SurgeTestFlight/243)

#Mac #Beta

Version 5.7.3-2782 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2782-768c4bdb0de547101723ec0834037612.zip

- Now you can see the number of times a rule has been used in the rule list.
- Optimized the implementation method of blocking QUIC traffic to increase the likelihood of clients correctly falling back.
- The Smart group will use the SUBSTITUTE policy (DIRECT) instead of failing directly when there are no sub-policies.
- Fixed an issue where the server-cert-fingerprint-sha256 parameter was not effective for TLS-like protocols with sni=off settings.
- Added a new rule type HOSTNAME-TYPE, used to determine the type of request hostname. Optional values are: IPv4, IPv6, DOMAIN, SIMPLE. (SIMPLE refers to hostnames without a dot, such as localhost)
- Optimized DNS request logs. Now more information is displayed. Additionally, if DIRECT policy connects directly without triggering DNS in the rule system, related DNS logs can still be shown.
- When deleting a policy that is being used by a policy group, it is now allowed to delete it directly and automatically remove it from all policy groups.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-26 [post 241](https://t.me/SurgeTestFlight/241)

#Mac #Beta

Version 5.7.3-2781 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2781-23217438378adcba7bcdb0e55dc68da5.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-24 [post 240](https://t.me/SurgeTestFlight/240)

#Mac #Beta

Version 5.7.3-2780 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2780-27636cafa40ab960631eb2a97b5fc5bf.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-22 [post 236](https://t.me/SurgeTestFlight/236)

#Mac #Beta

Version 5.7.3-2779 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2779-9ba656971504b4c7c9c1c7f095be87ed.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-21 [post 233](https://t.me/SurgeTestFlight/233)

#Mac #Beta

Version 5.7.3-2778 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2778-a6dc14935316b54bb84bfd337325e126.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-21 [post 232](https://t.me/SurgeTestFlight/232)

#Mac #Beta

Version 5.7.3-2777 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2777-c011da50797bda3ae5fd91670a8f918a.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-20 [post 229](https://t.me/SurgeTestFlight/229)

#Mac #Beta

Version 5.7.3-2775 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2775-6eedba7b7d03cb613b81a518d6b05f8e.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-17 [post 227](https://t.me/SurgeTestFlight/227)

#Mac #Beta

Version 5.7.3-2774 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2774-7354c140487e0d192f2761272b45b9c5.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 226](https://t.me/SurgeTestFlight/226)

#Mac #Beta

Version 5.7.3-2773 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2773-19051c283c7e199e78d9a64f6ff75d27.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 225](https://t.me/SurgeTestFlight/225)

#Mac #Beta

Version 5.7.3-2772 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2772-5d06e832d6e3f08e40c825c305ad149e.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 224](https://t.me/SurgeTestFlight/224)

#Mac #Beta

Version 5.7.3-2771 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2771-9521b0af719eb185fbbdd62e31e750af.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 222](https://t.me/SurgeTestFlight/222)

#Mac #Beta

Version 5.7.3-2770 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2770-36276f32d65fbd4068bd526a18d0b680.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 221](https://t.me/SurgeTestFlight/221)

#Mac #Beta

Version 5.7.3-2769 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2769-55bc11557ba1f1a6296d9ae7b705ecc9.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-15 [post 220](https://t.me/SurgeTestFlight/220)

#Mac #Beta

Version 5.7.3-2768 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2768-81df74720509a357170eb45d68dcbb9c.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-15 [post 218](https://t.me/SurgeTestFlight/218)

#Mac #Beta

Version 5.7.3-2767 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2767-538cf60b9cdcb16ac6ad4c4f78d83912.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-14 [post 217](https://t.me/SurgeTestFlight/217)

#Mac #Beta

Version 5.7.3-2766 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2766-c2c20a9d1b5c8da967b88fe53c6071b2.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-13 [post 216](https://t.me/SurgeTestFlight/216)

#Mac #Beta

Version 5.7.3-2765 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2765-bdb21a7cc589703cf9f25d93def335dd.zip

- Now you can see the number of times a rule has been used in the rule list.
- New rule type: HOSTNAME-TYPE.
- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-12 [post 212](https://t.me/SurgeTestFlight/212)

#Mac #Beta

Version 5.7.3-2764 https://dl.nssurge.com/mac/v5/Surge-5.7.3-2764-9a341e0c82ba7d91b56097628c2adfb6.zip

- Bug fixes and other Improvements.

Official Channel: @SurgeTestFlightFeed

## 2024-05-10 [post 210](https://t.me/SurgeTestFlight/210)

#Mac #Beta

Version 5.7.2-2762 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2762-9a963758f386b5da00e7744b2a7f254d.zip

- Optimize the matching performance of ASN rules in the rule set.
- Fix the issue where FINAL rules cannot be edited through UI.
- Fix the problem that invalid cron expressions would cause scripts to be executed repeatedly.
- Optimized the management mechanism of the script engine.
- Other detail issues fixed.

Official Channel: @SurgeTestFlightFeed

## 2024-05-10 [post 208](https://t.me/SurgeTestFlight/208)

#Mac #Beta

Version 5.7.2-2761 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2761-d1600a18bbcc9bd9f6768e1a16a6b9e8.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-05-08 [post 205](https://t.me/SurgeTestFlight/205)

#Mac #Beta

Version 5.7.2-2760 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2760-7afa3b9bd7a9397717cfc9413e46571e.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-04-30 [post 196](https://t.me/SurgeTestFlight/196)

#Mac #Beta

Version 5.7.2-2759 https://dl.nssurge.com/mac/v5/Surge-5.7.2-2759-3c7b8be22712134efb655ad9aa394d21.zip

- Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2024-04-29 [post 194](https://t.me/SurgeTestFlight/194)

#Mac #Beta

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

## 2024-04-29 [post 181](https://t.me/SurgeTestFlight/181)

#Mac #Beta

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

## 2024-04-29 [post 179](https://t.me/SurgeTestFlight/179)

#Mac #Beta

Version 5.7.1-2756 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2756-6ec2956efc688e84031a95d2aace48b8.zip

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

## 2024-04-28 [post 178](https://t.me/SurgeTestFlight/178)

#Mac #Beta

Version 5.7.1-2755 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2755-01f875ad35d2bef900855053f5f2337c.zip

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

## 2024-04-28 [post 175](https://t.me/SurgeTestFlight/175)

#Mac #Beta

Version 5.7.1-2754 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2754-821bab1470abba43cde053fb44ff7308.zip

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

## 2024-04-28 [post 174](https://t.me/SurgeTestFlight/174)

#Mac #Beta

Version 5.7.1-2753 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2753-76fab38988d95ba399d00e7e477c2cda.zip

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

## 2024-04-28 [post 173](https://t.me/SurgeTestFlight/173)

#Mac #Beta

Version 5.7.1-2749 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2749-f5856dce4f458e507cdbee4b90e2ff86.zip

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

## 2024-04-28 [post 170](https://t.me/SurgeTestFlight/170)

#Mac #Beta

Version 5.7.1-2748 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2748-e338e11808caff02a78977dc767bb14e.zip

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

## 2024-04-27 [post 168](https://t.me/SurgeTestFlight/168)

#Mac #Beta

Version 5.7.1-2747 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2747-0db5662fc5458a2e304ce6eec6948fac.zip

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

## 2024-04-27 [post 167](https://t.me/SurgeTestFlight/167)

#Mac #Beta

Version 5.7.1-2746 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2746-d064420d8ce23fcf8a54915afd3bea07.zip

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

## 2024-04-27 [post 166](https://t.me/SurgeTestFlight/166)

#Mac #Beta

Version 5.7.1-2745 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2745-902b3d1e90db38a33fdf0fc65567703d.zip

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

## 2024-04-27 [post 165](https://t.me/SurgeTestFlight/165)

#Mac #Beta

Version 5.7.1-2744 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2744-067328a90ba7ead7cf743fe062141f5f.zip

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

## 2024-04-27 [post 164](https://t.me/SurgeTestFlight/164)

#Mac #Beta

Version 5.7.1-2743 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2743-3f98aeb61a0f1a716fea3ff34b256580.zip

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

## 2024-04-27 [post 163](https://t.me/SurgeTestFlight/163)

#Mac #Beta

Version 5.7.1-2742 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2742-bf207433d9c392aa298d73ba5fcb18d7.zip

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

## 2024-04-27 [post 162](https://t.me/SurgeTestFlight/162)

#Mac #Beta

Version 5.7.1-2740 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2740-4491590d43f12f1d6799e5089ac45242.zip

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

## 2024-04-27 [post 161](https://t.me/SurgeTestFlight/161)

#Mac #Beta

Version 5.7.1-2739 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2739-871f26c998185d3c8ba2cd1b002bbd2c.zip

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

## 2024-04-27 [post 159](https://t.me/SurgeTestFlight/159)

#Mac #Beta

Version 5.7.1-2738 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2738-9025cc3a010d9009adb8140e52777095.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-27 [post 158](https://t.me/SurgeTestFlight/158)

#Mac #Beta

Version 5.7.1-2737 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2737-e45dab2a329c1c98419779f4d7383e45.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 154](https://t.me/SurgeTestFlight/154)

#Mac #Beta

Version 5.7.1-2736 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2736-f268a3758aa39e84853b5c32136356ba.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 153](https://t.me/SurgeTestFlight/153)

#Mac #Beta

Version 5.7.1-2735 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2735-c150cacc412c1a6319c6fffe125ab828.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 152](https://t.me/SurgeTestFlight/152)

#Mac #Beta

Version 5.7.1-2734 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2734-2e5a62492361166cd596802aab58c98c.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 151](https://t.me/SurgeTestFlight/151)

#Mac #Beta

Version 5.7.1-2733 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2733-b4e6bc9b72e624443308fce9f412825e.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 150](https://t.me/SurgeTestFlight/150)

#Mac #Beta

Version 5.7.1-2732 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2732-c517940be1edd43c253eabee29e5e5be.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 149](https://t.me/SurgeTestFlight/149)

#Mac #Beta

Version 5.7.1-2731 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2731-d52b979f4da2774eb355c30e9d0e8767.zip

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-04-25 [post 145](https://t.me/SurgeTestFlight/145)

#Mac #Beta

Version 5.7.1-2730 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2730-46a8a83d1d822db12a1dcceabbbdce18.zip

- Bug fixes

## 2024-04-25 [post 143](https://t.me/SurgeTestFlight/143)

#Mac #Beta

Version 5.7.1-2729 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2729-72ef20cadef610faf240cd18c252fd58.zip

- Bug fixes

## 2024-04-25 [post 141](https://t.me/SurgeTestFlight/141)

#Mac #Beta

Version 5.7.1-2728 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2728-0cd508c215e6bc00431124faa8c10cfb.zip

- Bug fixes

## 2024-04-25 [post 140](https://t.me/SurgeTestFlight/140)

#Mac #Beta

Version 5.7.1-2727 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2727-918941cf28d5715ec418dbe7f6aae4d2.zip

- Bug fixes

## 2024-04-25 [post 139](https://t.me/SurgeTestFlight/139)

#Mac #Beta

Version 5.7.1-2726 https://dl.nssurge.com/mac/v5/Surge-5.7.1-2726-fe13e96a4996f505661f692d5ba89214.zip

- Bug fixes

## 2024-04-24 [post 132](https://t.me/SurgeTestFlight/132)

#Mac #Beta

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

## 2024-04-24 [post 129](https://t.me/SurgeTestFlight/129)

#Mac #Beta

Version 5.7.0-2722 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2722-93bee354a3a34033600265ac798420d5.zip

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

## 2024-04-23 [post 126](https://t.me/SurgeTestFlight/126)

#Mac #Beta

Version 5.7.0-2721 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2721-2ecfc4339197a5262b724b4614fe9d6d.zip

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

## 2024-04-23 [post 125](https://t.me/SurgeTestFlight/125)

#Mac #Beta

Version 5.7.0-2717 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2717-fb5d4a3824bebf4f95a358077d9c858b.zip

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

## 2024-04-23 [post 124](https://t.me/SurgeTestFlight/124)

#Mac #Beta

Version 5.7.0-2716 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2716-5785dc858ccca31de2226cfc2157e81e.zip

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

## 2024-04-23 [post 122](https://t.me/SurgeTestFlight/122)

#Mac #Beta

Version 5.7.0-2715 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2715-288d8268dd3f19662574d5db3cd9aa0c.zip

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

## 2024-04-23 [post 121](https://t.me/SurgeTestFlight/121)

#Mac #Beta

Version 5.7.0-2714 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2714-e9ab57b48d0c968677dcfae26cf0b88d.zip

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

## 2024-04-23 [post 118](https://t.me/SurgeTestFlight/118)

#Mac #Beta

Version 5.7.0-2713 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2713-e0773d6fbba75cc848b68114be25add1.zip

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

## 2024-04-23 [post 117](https://t.me/SurgeTestFlight/117)

#Mac #Beta

Version 5.7.0-2712 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2712-f39d8e40c3c8e3ed6a3f7b98e8ad0625.zip

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

## 2024-04-23 [post 116](https://t.me/SurgeTestFlight/116)

#Mac #Beta

Version 5.7.0-2710 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2710-3ffc3c0d6d0e1490ac951e8aee62109d.zip

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

## 2024-04-22 [post 115](https://t.me/SurgeTestFlight/115)

#Mac #Beta

Version 5.7.0-2708 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2708-a45ab5428d563969332b8ae3be651780.zip

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

## 2024-04-22 [post 114](https://t.me/SurgeTestFlight/114)

#Mac #Beta

Version 5.7.0-2706 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2706-458aad2f8a6f2a4625580ac75a609837.zip

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

## 2024-04-22 [post 113](https://t.me/SurgeTestFlight/113)

#Mac #Beta

Version 5.7.0-2705 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2705-d75018b17ffb4410c71fe4589376ac0e.zip

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

## 2024-04-22 [post 112](https://t.me/SurgeTestFlight/112)

#Mac #Beta

Version 5.7.0-2702 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2702-8ffb49a6cac676484ef119aa08b9dac0.zip

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

## 2024-04-22 [post 109](https://t.me/SurgeTestFlight/109)

#Mac #Beta

Version 5.7.0-2701 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2701-78d1e73bd6699a5890c892118cf0c5e3.zip

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

## 2024-04-22 [post 106](https://t.me/SurgeTestFlight/106)

#Mac #Beta

Version 5.7.0-2699 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2699-c9b3d48444f592afed8b25e6e5e312a7.zip

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

## 2024-04-22 [post 104](https://t.me/SurgeTestFlight/104)

#Mac #Beta

Version 5.7.0-2698 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2698-1626d14e1ae6ce666f158673a50af448.zip

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

## 2024-04-21 [post 101](https://t.me/SurgeTestFlight/101)

#Mac #Beta

Version 5.7.0-2697 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2697-aa6c7a64be17989741b42f4db9b9a8a2.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-20 [post 97](https://t.me/SurgeTestFlight/97)

#Mac #Beta

Version 5.7.0-2695 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2695-7a3dce9b956a35a10fb52d192c755a8f.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-20 [post 93](https://t.me/SurgeTestFlight/93)

#Mac #Beta

Version 5.7.0-2694 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2694-18eb57ea8ee1c2b7e1613d4c539b9c15.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-20 [post 89](https://t.me/SurgeTestFlight/89)

#Mac #Beta

Version 5.7.0-2693 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2693-4f0c8196121d4c8493a9b3bf9e2fc320.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-19 [post 88](https://t.me/SurgeTestFlight/88)

#Mac #Beta

Version 5.7.0-2692 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2692-27a471cbe31c016e4a4b4890bb290e7d.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-19 [post 86](https://t.me/SurgeTestFlight/86)

#Mac #Beta

Version 5.7.0-2691 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2691-4128b114dc1221b10e6f2ef02ea6303b.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-19 [post 85](https://t.me/SurgeTestFlight/85)

#Mac #Beta

Version 5.7.0-2690 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2690-aae1ef5089b0dcc87b3beb5f22dd62d1.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-19 [post 83](https://t.me/SurgeTestFlight/83)

#Mac #Beta

Version 5.7.0-2689 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2689-a3c1d783ad2f7239a095a5df2388d19f.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-19 [post 81](https://t.me/SurgeTestFlight/81)

#Mac #Beta

Version 5.7.0-2687 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2687-fc5127f50777f8fe6987b8ac4210cdfe.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-18 [post 61](https://t.me/SurgeTestFlight/61)

#Mac #Beta

Version 5.7.0-2685 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2685-521f905a1054c648717cbd06fff67735.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-17 [post 60](https://t.me/SurgeTestFlight/60)

#Mac #Beta

Version 5.7.0-2684 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2684-5622642a7f07bf8f5b889adea113c04b.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-17 [post 59](https://t.me/SurgeTestFlight/59)

#Mac #Beta

Version 5.7.0-2682 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2682-33e2e785459d82f2d6e1b0efe135a058.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-17 [post 51](https://t.me/SurgeTestFlight/51)

#Mac #Beta

Version 5.7.0-2681 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2681-6ae8767c8239e7468df04fe95d8a8f7a.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-16 [post 48](https://t.me/SurgeTestFlight/48)

#Mac #Beta

Version 5.7.0-2680 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2680-f07d9d331f671b3445c7b60ec998e694.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-16 [post 45](https://t.me/SurgeTestFlight/45)

#Mac #Beta

Version 5.7.0-2679 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2679-057809ae8ae4874ab74a7b86ae25b0aa.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-16 [post 42](https://t.me/SurgeTestFlight/42)

#Mac #Beta

Version 5.7.0-2678 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2678-aea8695f1b9ea4e045f7e7110da1fdf3.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-16 [post 41](https://t.me/SurgeTestFlight/41)

#Mac #Beta

Version 5.7.0-2677 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2677-b9fea46fab16f792966ba8a5eceb7cd5.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-15 [post 40](https://t.me/SurgeTestFlight/40)

#Mac #Beta

Version 5.7.0-2674 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2674-c1ea849c959adb53e0ecb98944188147.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-15 [post 39](https://t.me/SurgeTestFlight/39)

#Mac #Beta

Version 5.7.0-2673 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2673-7242fe3e6afcc48e7e5f897bb920118c.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-15 [post 37](https://t.me/SurgeTestFlight/37)

#Mac #Beta

Version 5.7.0-2672 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2672-ce7e3c25774036eecb6a84e40a36962a.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-14 [post 35](https://t.me/SurgeTestFlight/35)

#Mac #Beta

Version 5.7.0-2671 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2671-5a93569253d48f65b568534995e06ae4.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-14 [post 34](https://t.me/SurgeTestFlight/34)

#Mac #Beta

Version 5.7.0-2670 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2670-883b45009708288dbbc468cc1542c948.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-12 [post 25](https://t.me/SurgeTestFlight/25)

#Mac #Beta

Version 5.7.0-2669 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2669-286615a28cd7c994ea6b867955ca46bc.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-12 [post 24](https://t.me/SurgeTestFlight/24)

#Mac #Beta

Version 5.7.0-2668 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2668-27dcab9328b80b9c74b8e5cc126617f0.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-12 [post 22](https://t.me/SurgeTestFlight/22)

#Mac #Beta

Version 5.7.0-2667 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2667-0662f54c452f76dc53ca81dc9a246910.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-12 [post 21](https://t.me/SurgeTestFlight/21)

#Mac #Beta

Version 5.7.0-2666 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2666-431bbc078ec78ecb69ee359094a74ebd.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-12 [post 20](https://t.me/SurgeTestFlight/20)

#Mac #Beta

Version 5.7.0-2665 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2665-5e8a48a0604e81ae6af9cf3a88f9cff9.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-11 [post 18](https://t.me/SurgeTestFlight/18)

#Mac #Beta

Version 5.7.0-2664 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2664-4c68341a1364a04a56a3770fcd1e71be.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-11 [post 16](https://t.me/SurgeTestFlight/16)

#Mac #Beta

Version 5.7.0-2663 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2663-2a9c4575cfab9267e2b40f4b5ca88edb.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-10 [post 9](https://t.me/SurgeTestFlight/9)

#Mac #Beta

Version 5.7.0-2658 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2658-816d74932828c47703f252e3cf6420ee.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-10 [post 14](https://t.me/SurgeTestFlight/14)

#Mac #Beta

Version 5.7.0-2662 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2662-a062d86fcd447382b2575e8dc97c9e78.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-10 [post 12](https://t.me/SurgeTestFlight/12)

#Mac #Beta

Version 5.7.0-2661 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2661-c14e34a06d8058299da2a609c54a9d0d.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-10 [post 11](https://t.me/SurgeTestFlight/11)

#Mac #Beta

Version 5.7.0-2660 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2660-5b177c716d4e15b1062f648511623255.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

## 2024-04-10 [post 10](https://t.me/SurgeTestFlight/10)

#Mac #Beta

Version 5.7.0-2659 https://dl.nssurge.com/mac/v5/Surge-5.7.0-2659-f4360f85c358426a357e315f1c5be0d3.zip

### New Feature
- Smart Policy Group. Check the community documentation to learn more: https://community.nssurge.com/d/2536-smart-policy-group https://community.nssurge.com/d/2536-smart-policy-group

