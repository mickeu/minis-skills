# Surge iOS-TestFlight 更新日志

来源频道: https://t.me/SurgeTestFlight

## 2026-10-07 [post 1784](https://t.me/SurgeTestFlight/1784)

#iOS #TestFlight 

Surge 5 5.102.0 (3862) is ready to test on iOS.

What to Test

5.23.0 Release Candidate 1
- External resource management and some other helper APIs have been added to the HTTP API.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-10-06 [post 1782](https://t.me/SurgeTestFlight/1782)

#iOS #TestFlight 

Surge 5 5.102.0 (3861) is ready to test on iOS.

What to Test

- Ready for iPhone Duo
- Add device communication takeover option for include all mode
- Other minor improvements

Official Channel: @SurgeTestFlightFeed

## 2026-10-05 [post 1778](https://t.me/SurgeTestFlight/1778)

#iOS #TestFlight 

Surge 5 5.102.0 (3859) is ready to test on iOS.

What to Test

### New Features
- Added the `[IP Rewrite]` section, which handles packets entering Surge VIF at the IP layer based on their destination address, before they reach any rule or policy. Available actions:
  - `reflect`: Swaps the source and destination addresses and sends the packet back to its sender.
  - `reject`: Responds with a TCP RST to connection attempts and with an ICMP administratively prohibited message to other packets, so the sender fails immediately.
  - `drop`: Silently discards the packet.
  
For example, you can use the following modules to make Surge work as LocalDevVPN, allowing you to use certain developer toolchains on iOS devices.

```
#!name=Local Device Loopback
#!desc=Reflect 10.7.0.1 http://10.7.0.1/ back to this device for on-device developer tools.
[General]
ipv6-vif = disabled // Some tools only recognize utun interfaces without an IPv6 address.
tun-included-routes = %INSERT% 10.7.0.1/32 http://10.7.0.1/32

[IP Rewrite]
10.7.0.1 http://10.7.0.1/ = reflect
```

Official Channel: @SurgeTestFlightFeed

## 2026-09-30 [post 1773](https://t.me/SurgeTestFlight/1773)

#iOS #TestFlight 

Surge 5 5.102.0 (3855) is ready to test on iOS.

What to Test

- Updates can now be triggered manually when using URL-based linked profiles.
- Fixed other minor issues.

Official Channel: @SurgeTestFlightFeed

## 2026-09-29 [post 1771](https://t.me/SurgeTestFlight/1771)

#iOS #TestFlight 

Surge 5 5.102.0 (3854) is ready to test on iOS.

What to Test

- Fixed a compatibility issue in the scripting engine
- Other minor optimizations and fixes

Official Channel: @SurgeTestFlightFeed

## 2026-09-28 [post 1769](https://t.me/SurgeTestFlight/1769)

#iOS #TestFlight 

Surge 5 5.102.0 (3853) is ready to test on iOS.

What to Test

- Optimized Tailscale and WireGuard behavior when switching networks
- Fixed some extremely rare crashes

Official Channel: @SurgeTestFlightFeed

## 2026-09-25 [post 1767](https://t.me/SurgeTestFlight/1767)

#iOS #TestFlight 

Surge 5 5.102.0 (3852) is ready to test on iOS.

What to Test

- When attempting to use the Ponte policy in a policy group, an error notification about Ponte is no longer displayed.
- Other issue fixes

Official Channel: @SurgeTestFlightFeed

## 2026-09-22 [post 1763](https://t.me/SurgeTestFlight/1763)

#iOS #TestFlight 

Surge 5 5.102.0 (3851) is ready to test on iOS.

What to Test

- Inline rule sets with the same name now merge across the main profile and modules instead of replacing one another, preserving rules contributed by each source.

Official Channel: @SurgeTestFlightFeed

## 2026-09-21 [post 1761](https://t.me/SurgeTestFlight/1761)

#iOS #TestFlight 

Surge 5 5.102.0 (3850) is ready to test on iOS.

What to Test

- Made global adjustments to the UI layout logic and optimized details for iPhone Duo support.
- Fixed horizontal scrolling in the iOS policy group category selector when categories exceed the available width.
- Improved UDP test diagnostics for peer-to-peer Tailscale and WireGuard policies without Internet egress, reporting unsupported tests instead of waiting for a timeout.
- Fixed logical rules incorrectly parsing policy names containing parentheses.

Official Channel: @SurgeTestFlightFeed

## 2026-09-18 [post 1759](https://t.me/SurgeTestFlight/1759)

#iOS #TestFlight 

Surge 5 5.102.0 (3848) is ready to test on iOS.

What to Test

- Performance and memory usage optimizations
- Optimized the Add Rule page. Domain rules can now also be added for SNI sniffing requests, and rule-specific additional configurations can be selected directly.

Official Channel: @SurgeTestFlightFeed

## 2026-09-14 [post 1755](https://t.me/SurgeTestFlight/1755)

#iOS #TestFlight 

Surge 5 5.102.0 (3842) is ready to test on iOS.

What to Test

- A `category` parameter has been added to policy groups for grouped display. It can be used when there are many policy groups.
- All `test-url` parameters now support configuring HTTPS URLs for testing. The test result remains the latency of a single HTTP RTT, but due to the TLS handshake, the test duration may increase significantly when there are many policies.
- In the previous version, MITM security was strengthened by generating a separate key pair for each distinct domain name. This caused noticeable delays when performing MITM concurrently on a large number of different domains. After evaluation, this change has been reverted.

Official Channel: @SurgeTestFlightFeed

## 2026-09-10 [post 1750](https://t.me/SurgeTestFlight/1750)

#iOS #TestFlight 

Surge 5 5.102.0 (3837) is ready to test on iOS.

What to Test

5.22.1 Release Candidate 2

- Compiled with the iOS 27 SDK
- Policy group Widgets support the extra-large size on iOS 27

Official Channel: @SurgeTestFlightFeed

## 2026-09-09 [post 1749](https://t.me/SurgeTestFlight/1749)

#iOS #TestFlight 

Surge 5 5.102.0 (3836) is ready to test on iOS.

What to Test

5.22.1 Release Candidate 1

- Added UNKNOWN support to GEOIP and IP-ASN rules, allowing you to match destination IP addresses with no corresponding country or ASN database entry. Supported in both individual rules and rule sets.
- Fixed a bug that caused results to fall short of expectations under extreme upload throughput performance testing.
- Fixed an issue where a failed cellular backup connection in Wi-Fi Assist or Hybrid mode could prematurely abort an ongoing Wi-Fi connection attempt, including connections to local network destinations.
- Fixed Pre-Matching remaining enabled after switching a rule to a non-reject policy or an unsupported rule type in the iOS and macOS rule editors.

Official Channel: @SurgeTestFlightFeed

## 2026-09-08 [post 1746](https://t.me/SurgeTestFlight/1746)

#iOS #TestFlight 

Surge 5 5.102.0 (3835) is ready to test on iOS.

What to Test

- Added a medium-sized iOS widget that combines start/stop controls, running status, and one-tap switching between Rule-Based Proxy, Direct Outbound, and Global Proxy.
- Fixed Hysteria UDP traffic failing with servers where HTTP/3 Datagram negotiation interfered with UDP forwarding.
- Fixed SF Symbol policy group icons on iOS not adapting correctly to appearance changes.
- Fixed a bug that caused results to fall short of expectations under extreme throughput performance testing.

Official Channel: @SurgeTestFlightFeed

## 2026-09-05 [post 1744](https://t.me/SurgeTestFlight/1744)

#iOS #TestFlight 

Surge 5 5.102.0 (3833) is ready to test on iOS.

What to Test

- Fixed missing traffic statistics for UDP connections through proxies and tunnels, including WireGuard and Tailscale.
- Fixed a rare issue where a UDP proxy connection closing during packet reception could stall other traffic handled by Surge.
- Improved resource updates on iOS: pending automatic updates resume when the app becomes active, duplicate downloads are avoided, and outdated errors clear after a successful background refresh.

Official Channel: @SurgeTestFlightFeed

## 2026-08-31 [post 1737](https://t.me/SurgeTestFlight/1737)

#iOS #TestFlight 

Surge 5 5.102.0 (3830) is ready to test on iOS.

What to Test

5.22.0 Release Candidate 3

- Fixed issues that may occur when filenames contain certain special emojis.
- Optimized the handling logic for low-memory mode.

Official Channel: @SurgeTestFlightFeed

## 2026-08-26 [post 1736](https://t.me/SurgeTestFlight/1736)

#iOS #TestFlight 

Surge 5 5.102.0 (3829) is ready to test on iOS.

What to Test

5.22.0 Release Candidate 2

- Crash fixes

Official Channel: @SurgeTestFlightFeed

## 2026-08-25 [post 1735](https://t.me/SurgeTestFlight/1735)

#iOS #TestFlight 

Surge 5 5.102.0 (3828) is ready to test on iOS.

What to Test

5.22.0 Release Candidate 1

- Minor bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-08-24 [post 1734](https://t.me/SurgeTestFlight/1734)

#iOS #TestFlight 

Surge 5 5.102.0 (3825) is ready to test on iOS.

What to Test

### Improved

- Nested rulesets now work reliably: inline rulesets can reference other inline rulesets or external `RULE-SET` and `DOMAIN-SET` sources. Circular references are rejected with a clear reference chain instead of causing recursive matching.
- The local ruleset editor now preserves blank lines, standalone and trailing comments, and disabled rules more accurately. Invalid entries report their source file and line number, while comment rows use the same readable presentation as the main rule editor.
- Virtual IP records and search results on iOS now use self-sizing rows, preventing longer domains and usage details from being clipped.

### Fixed

- Fixed rules added inside a ruleset or logical rule on iOS incorrectly retaining a hidden policy value when saved.

Official Channel: @SurgeTestFlightFeed

## 2026-08-21 [post 1732](https://t.me/SurgeTestFlight/1732)

#iOS #TestFlight 

Surge 5 5.102.0 (3824) is ready to test on iOS.

What to Test

- Fixed long-running Ponte and Vector sessions eventually failing to open new relayed connections after handling many connections over the same QUIC session.
- Other bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-08-20 [post 1731](https://t.me/SurgeTestFlight/1731)

#iOS #TestFlight 

Surge 5 5.102.0 (3823) is ready to test on iOS.

What to Test

- Tailscale can now establish peer-relay paths through eligible tailnet devices when a direct connection is unavailable, with Direct > Peer Relay > DERP path priority. Runtime details identify Peer Relay connections and display their latency.
- Local-file and inline rulesets can now be edited graphically on macOS and iOS. Add or modify standard rules, logical rules, nested rulesets, and comments, then reorder or remove entries as needed. Create new inline rulesets directly from the rule editor and store them as named `[Ruleset ...]` sections in the profile.
- The previously added mixed use of `#include (?q=%23include)` will no longer affect UI write-back for the corresponding sections. Surge will automatically select the write-back target as accurately as possible based on the changes.

Official Channel: @SurgeTestFlightFeed

## 2026-08-19 [post 1729](https://t.me/SurgeTestFlight/1729)

#iOS #TestFlight 

Surge 5 5.102.0 (3822) is ready to test on iOS.

What to Test

### Profile Diagnostics

- WireGuard and Tailscale policies now produce a clear warning when their referenced configuration section is missing.
- The warning also explains that a named `#!include` loads only the identically named section from the included file.

### Modules and Cloud Sync

- Module installation information is no longer governed by iCloud data, in order to avoid various issues caused by iCloud. iCloud is only used to synchronize installation information across devices.
- Cloud synchronization now excludes `.git` and `node_modules` directories and no longer interprets their absence in the cloud as a request to delete local content.

### iOS

- Fixed policy-group icon changes sometimes being lost after the profile reloaded.
- Refined module menus on iOS 26 to avoid overlapping context-menu animations and improve Liquid Glass presentation.

Official Channel: @SurgeTestFlightFeed

## 2026-08-18 [post 1728](https://t.me/SurgeTestFlight/1728)

#iOS #TestFlight 

Surge 5 5.102.0 (3821) is ready to test on iOS.

What to Test

### Profile System Updates

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

Note: When using this feature in the [Rule] section, keep in mind that a FINAL rule immediately terminates rule matching. Any rules included or defined after it will therefore never be evaluated.### Tailscale

- Improved compatibility with the Tailscale administration console. Surge devices are no longer incorrectly reported as using an outdated client, enabling version-gated operations such as editing the device IP address.

### iOS

- Fixed managed-profile `icon-url` icons being hidden by automatically generated placeholder icons.
- Custom policy-group icons now behave consistently across Lucid and Gradient themes, with a **Default** option available in both.
- Module download, parsing, file-writing, and installation-information failures are now reported instead of failing silently.
- Refined the Script Editor toolbar and file-selection layout on iOS 26.
- Improved context-menu previews on iOS 26 by following the system’s native corner styling.

Official Channel: @SurgeTestFlightFeed

## 2026-08-17 [post 1725](https://t.me/SurgeTestFlight/1725)

#iOS #TestFlight 

Surge 5 5.102.0 (3820) is ready to test on iOS.

What to Test

### Smart Group

- Added a graphical Policy Priority editor for Smart Groups on.

### Tailscale

- Interactive sign-in now supports tailnets that require administrator device approval. Surge clearly indicates when sign-in has completed but the device is still awaiting approval.
- Fixed Tailscale traffic becoming unavailable when the control server assigned the device a new tailnet address.
- Improved recovery after network changes by retrying temporarily failed UDP bindings and refreshing direct-connect endpoints.
- Improved WireGuard and Tailscale handling of multiple peers and expired connections.

### Profile and Automation

- On iOS, profile changes made on disk or received through iCloud now reload automatically. If the updated profile is invalid, Surge keeps the working configuration active and reports the error.
- Event scripts can now respond to `engine-started` and `profile-reloaded`, in addition to `network-changed`.

### Notifications

- Added notification controls for new proxy clients, script notifications, and rule-matched notifications.
- Local and remote notification category settings now correctly apply to dynamically generated alerts.
- Disabling policy-group change notifications now also suppresses temporary group-override alerts.

### Fixed

- Improved MITM certificate generation by using separate keys for generated leaf certificates and correcting the transmitted certificate chain.
- Fixed QUIC connections potentially stalling after receive-side backpressure.
- Fixed rare deadlocks involving cron-script shutdown and Vector UDP connections, including Ponte traffic.
- Improved stability under heavy connection churn and local-port exhaustion.
- Other small UI issues.

Official Channel: @SurgeTestFlightFeed

## 2026-08-14 [post 1721](https://t.me/SurgeTestFlight/1721)

#iOS #TestFlight 

Surge 5 5.102.0 (3819) is ready to test on iOS.

What to Test

### Profile Format

- Added wildcard detached-section includes for `[Ruleset *]`, `[WireGuard *]`, and `[Tailscale *]`. A single `#!include` can now load all matching named sections from another local or remote profile file.
- Added `DEVICE_NAME` to the profile environment, enabling device-specific conditions in `#!REQUIREMENT`.
- Fixed `[General]` values containing `#`, `//`, or `;` being truncated or changed after the profile was saved and reloaded.

### Tailscale

- Improved interactive Tailscale sign-in reliability. Interrupted or silently disconnected login sessions now reconnect and continue the existing browser authorization flow instead of becoming stuck.

### Fixed

- Fixed a rare crash when an HTTP/3 or other QUIC session closed synchronously while pending data was being processed.
- Other fixes

Official Channel: @SurgeTestFlightFeed

## 2026-08-13 [post 1720](https://t.me/SurgeTestFlight/1720)

#iOS #TestFlight 

Surge 5 5.102.0 (3818) is ready to test on iOS.

What to Test

### UI

- When navigating to a new page, the bottom tab bar is no longer hidden. This change was made to avoid triggering known UIKit UI glitches that can occur when the tab bar is hidden during push transitions.
- The Script Editor now opens in a dedicated modal interface, with an updated toolbar, close action, and improved keyboard layout.
- Remote Controller and Ponte Diagnostics are now available for all Ponte devices, including devices shared by another iCloud account.
- Other UI improvements.

### Other Improvements

- Updated the IPv6 fake-IP range to avoid unnecessary browser local-network permission prompts, while retaining compatibility with previously cached addresses.
- Proxy connections closed during the protocol handshake now provide a clearer error message, with guidance to verify credentials, encryption methods, and protocol settings.
- Fixed rare crashes that could occur when proxy connections were synchronously closed while data was being written.
- Fixed recursive HTTP/3 timer processing that could cause a stack overflow under certain conditions.

Official Channel: @SurgeTestFlightFeed

## 2026-08-12 [post 1717](https://t.me/SurgeTestFlight/1717)

#iOS #TestFlight 

Surge 5 5.102.0 (3815) is ready to test on iOS.

What to Test

- Fix the issue where groups configured with an underlying proxy cannot be operated in the UI.
- [Host] rules now support specifying a dedicated DNS server for domain aliases, for example: foo.com http://foo.com/ = bar.com http://bar.com/, server:https://example/dns-query.

Official Channel: @SurgeTestFlightFeed

## 2026-08-11 [post 1712](https://t.me/SurgeTestFlight/1712)

#iOS #TestFlight 

Surge 5 5.102.0 (3813) is ready to test on iOS.

What to Test

We’ve launched https://x.com/SurgeBeta https://x.com/SurgeBeta, a new X account for detailed updates on the latest Surge Beta releases. It will stay in sync with our existing Telegram Channel. Follow to keep up with the latest Beta changes and improvements.

--------------
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

### Protocol Updates

- Added MASQUE proxy support, using HTTP/3 CONNECT for multiplexed TCP tunnels and CONNECT-UDP datagrams.
- HTTP/2 CONNECT proxies can now relay UDP traffic with udp-relay=true.
- TrustTunnel can now use HTTP/3 transport with h3=true.

### Poilcy Group

- Added group-level proxy chaining. A policy group can specify an underlying proxy, and all concrete proxy members in that group will connect through it. This can be configured with underlying-proxy or Through Another Proxy in the group editor view.

### HTTP API

- Added a Prometheus-compatible /metrics endpoint to the HTTP Controller, exposing build information, uptime, memory usage, active requests, DNS cache size, security bans, interface traffic, and per-policy traffic.

PS：新的订阅功能：
        * Pulse 图标
        * Terminal 终端

Official Channel: @SurgeTestFlightFeed

## 2026-08-10 [post 1699](https://t.me/SurgeTestFlight/1699)

#iOS #TestFlight 

Surge 5 5.102.0 (3811) is ready to test on iOS.

What to Test

5.21.1 Release Candidate
Fixed an issue where the Host field could be unexpectedly rewritten when handling requests in HTTP mode.

Official Channel: @SurgeTestFlightFeed

## 2026-08-06 [post 1693](https://t.me/SurgeTestFlight/1693)

#iOS #TestFlight 

Surge 5 5.102.0 (3806) is ready to test on iOS.

What to Test

5.21.0 Release Candidate 3

* Fixed an issue where users were unable to accept Ponte shares due to behavioral changes in iCloud China (GCBD)
* Fixed an issue where UDP traffic was not correctly tagged with the interface traffic statistics marker, resulting in blank entries
* Fixed an issue where WireGuard did not correctly use an MTU of 1280 when no MTU value was explicitly specified

Official Channel: @SurgeTestFlightFeed

## 2026-08-03 [post 1689](https://t.me/SurgeTestFlight/1689)

#iOS #TestFlight 

Surge 5 5.102.0 (3800) is ready to test on iOS.

What to Test

5.21.0 Release Candidate 2

- Optimized content usage when a large number of modules are enabled
- Removed strict validation for modules; invalid lines no longer invalidate the entire module
- Relaxed some HTTP engine validations to improve compatibility with non-standard HTTP services
- HTTP header fields that are not modified by scripts are now forwarded directly in their original binary form to improve compatibility.
- Other small fixes and improvements.

Official Channel: @SurgeTestFlightFeed

## 2026-07-31 [post 1686](https://t.me/SurgeTestFlight/1686)

#iOS #TestFlight 

Surge 5 5.102.0 (3797) is ready to test on iOS.

What to Test

5.21.0 Release Candidate

- Further trimmed unused code and resources, reducing the application package size.
- Fixed the issue where GeoIP database could not be updated.
- Improved the reliability of tunnel startup, environment changes, Always-On settings, widgets, and App Intent operations.
- Fixed several Safari extension issues that could cause the extension to hang when processing invalid pages or when loading or saving a profile failed.
- Fixed crashes when opening an empty packet capture session or inspecting malformed capture data.
- Fixed text editor crashes with empty content, missing discard confirmations, and read-only files remaining editable.
- Improved remote device management, temporary rules, policy changes, profile reloads, and SSID editing so that local state is updated only after the remote operation succeeds.
- Improved error handling for network and Ponte diagnostics, including restoring the restart controls after a failed test.
- Fixed concurrency and stale-result issues in traffic statistics, live log viewing, device icon loading, and network-change handling.
- Fixed Picture in Picture resource leaks and cleanup issues.
- Improved compatibility with profiles containing sections introduced by newer versions by suppressing unnecessary warnings for unrecognized sections.
- Improved profile, module, script, local mapping, external resource, and keystore editing to preserve user input and report an error when saving fails.
- Fixed an issue where a failed profile write could start the tunnel using an outdated configuration.
- Hardened archive extraction against unsafe paths.
- Fixed Vector UDP setup, teardown, and error-reporting races affecting both Ponte and regular Vector connections.
- Improved QUIC stream handling to prevent unexpected callback re-entry.
- Fixed Ponte diagnostics resources not being released when a test was cancelled.

Official Channel: @SurgeTestFlightFeed

## 2026-07-30 [post 1683](https://t.me/SurgeTestFlight/1683)

#iOS #TestFlight 

Surge 5 5.102.0 (3793) is ready to test on iOS.

What to Test

## Networking and Compatibility

- Added compatibility with clients that send unbracketed IPv6 addresses in HTTP `CONNECT` requests.
- MTProto Server now warns when Telegram IPv6 connections repeatedly fail, suggesting an incompatible proxy or the use of `ipv6 = false`.
- Improved TCP protocol robustness and excluded local tunnel peers from unnecessary TCP pacing.
- Updated the MaxMind database library for improved compatibility and reliability.

## Profile Management

- Profile imports, replacements, upgrades, and backups are now performed atomically on macOS and iOS, reducing the risk of partial or corrupted files.
- Improved managed-profile updates with stricter response validation and safer replacement behavior.
- Profile name collisions are now detected more reliably, including case-insensitive collisions on iOS.
- Fixed profile renaming or switching storage providers potentially losing files or disrupting cloud synchronization.
- Ruleset and managed-profile cache write failures are now reported instead of being silently ignored.
- Downloaded profile responses are now validated before installation.

## iOS Improvements

- Installing a module from an external URL now requires explicit user confirmation.
- Improved tunnel preference updates, provider-message validation, error reporting, and handling of tunnel-extension memory termination.
- Fixed UI settings potentially being lost when a policy group was renamed.
- Improved Home card state restoration, configurable card validation, dismissal persistence, and presentation reliability.

## Script
- Relax the single-line log length limit from 64 KB to 512 KB.

Official Channel: @SurgeTestFlightFeed

## 2026-07-29 [post 1682](https://t.me/SurgeTestFlight/1682)

#iOS #TestFlight 

Surge 5 5.102.0 (3792) is ready to test on iOS.

What to Test

## New Features

- Added UDP-aware Smart Group scoring. Surge now learns from UDP response latency and silent relay failures to improve policy selection for UDP traffic.
- Added `\"` and `\\` escape sequences inside double-quoted profile values, allowing values containing quotes to be saved and reloaded safely.
- Core Version Alignment: Starting with Surge Mac 6.8.0 and Surge iOS 5.21.0, Core Version is derived directly from the corresponding Surge Mac version, eliminating the need to maintain a separate Core Version number. Check manual for more information.

## Networking Improvements

- Reworked TCP pacing to adapt to connection latency and reduce traffic bursts on Gateway Mode and WireGuard-based connections.
- Improved MITM hostname matching for TLS and QUIC traffic on nonstandard ports while continuing to respect exclusion rules.
- Improved HTTP/1 and HTTP/2 response handling, including interim responses, lowercase `HEAD` requests, and simultaneous `GOAWAY` shutdown.
- Fixed Hysteria response-header validation rejecting or mishandling certain responses.
- Fixed Ponte connections entering an incorrect state when IPv4 and IPv6 setup operations completed synchronously.
- Enforced the WebSocket message-size limit while data is being received, preventing oversized messages from consuming excessive memory.

## Security and Compatibility

- Removed unsupported legacy Shadowsocks ciphers including `bf-cfb`, `camellia-*-cfb`, `cast5-cfb`, `des-cfb`, `idea-cfb`, `rc2-cfb`, and `seed-cfb`.
- Hardened downloaded profile names and GeoIP archive extraction against unsafe paths.
- Improved license refresh and device identifier stability, especially when the Keychain is temporarily unavailable.
- Added support for importing SSH P-521 keys and improved errors for unsupported elliptic curves.
- Policy priorities must now be positive values; zero and negative values are rejected during profile validation.

## Profiles and Cloud Sync

- Fixed iCloud synchronization potentially deadlocking, dropping pending uploads, or deleting profiles that had not yet synchronized.
- Fixed Dropbox synchronization potentially overwriting newer local profile edits with an older remote copy.
- Improved retry behavior and completion reporting when Dropbox synchronization encounters persistent errors.
- Managed profiles are now protected from local writes that would accidentally remove their managed status.
- Improved CloudKit synchronization for Ponte and remote-device information.
- Settings storage failures are now reported instead of silently losing pending changes.

## Logbook and UI

- Improved Logbook search performance and fixed records disappearing when identifiers were duplicated.
- Script timeout and exception records now display their result details correctly.
- Fixed Dashboard potentially closing when sorting remote records with missing timestamps.
- Fixed “Copy as cURL” output for URLs, headers, methods, or request bodies containing apostrophes.
- Fixed missing or corrupted SSID History entries during concurrent app and tunnel-extension access.
- Fixed the iOS color picker saving invalid values when selecting black or white.
- Fixed option-selection screens showing a stale checkmark after changing the selected value.
- Improved icon caching and added safeguards against excessively large downloaded images.

Official Channel: @SurgeTestFlightFeed

## 2026-07-28 [post 1681](https://t.me/SurgeTestFlight/1681)

#iOS #TestFlight 

Surge 5 5.102.0 (3791) is ready to test on iOS.

What to Test

## New Features

* Added automatic routing for Tailscale peer IPv4 and IPv6 addresses (IP-CIDR/IP-CIDR6 rules are inserted automatically.). Routes are kept synchronized as the tailnet changes.
* Tailscale sessions now remain active by default. An omitted `idle-keepalive`, `0`, or `-1` keeps the session active; use a positive value to enable idle teardown.
* Invalid entries in external rule sets are now skipped with warnings, allowing the remaining valid rules to continue working.

## Improvements

* Smart Group connections that receive no response data within three seconds are now marked as failed, allowing faster fallback to another policy.
* Improved configuration validation and diagnostics for policies, rules, modules, scripts, panels, MITM, port forwarding, WireGuard, Tailscale, MTProto, and Snell server settings.
* Surge now warns when a quoted profile value cannot be safely preserved during serialization.
* Improved DNS, IP, UDP, ruleset, and MMDB processing to handle malformed input safely without disrupting the tunnel.
* Improved MITM certificate and keystore validation and lifecycle reliability.
* Improved tvOS profile deployment so modules are filtered and evaluated using the correct tvOS environment.

## Bug Fixes

* Fixed rewrite rules containing quotes or spaces potentially becoming corrupted after saving and reloading the profile.
* Fixed values containing ` #`, ` //`, or ` ;` inside quotes being incorrectly treated as inline comments.
* Fixed profiles with invalid text encoding potentially being interpreted as an empty profile and subsequently overwritten.
* Fixed policy comments, group state, local-mapping payloads, subnet values, and other metadata potentially being lost during profile editing or copying.
* Fixed malformed CIDR masks potentially being interpreted as `/0` and matching all traffic.
* Fixed underlying-proxy loops not always being detected during configuration validation.
* Fixed false port-conflict warnings for listeners bound to different network addresses.
* Fixed sensitive values not being consistently redacted when exporting profiles, including WireGuard preshared keys and port-forwarding credentials.
* Fixed redacted MTProto and other secret placeholders potentially being rejected or lost during remote profile editing.
* Fixed several malformed DNS or network packets potentially causing the tunnel process to terminate.

Official Channel: @SurgeTestFlightFeed

## 2026-07-27 [post 1679](https://t.me/SurgeTestFlight/1679)

#iOS #TestFlight 

Surge 5 5.102.0 (3789) is ready to test on iOS.

What to Test

## New Features

- Added interactive Tailscale sign-in on iOS and macOS. Resolve the issue where some enterprise users are unable to obtain the auth key.
- DNS lookup results now display the network interface used on iOS, macOS Dashboard, and the command-line interface.

## Improvements

- Fixed an issue where the Surge UI might not be displayed when using secondary screen output on iOS.
- Improved TLS 1.3 connection reliability and prevented session reuse across incompatible SNI, ALPN, or certificate verification settings.
- Improved Smart Group recovery following transient failures on reusable AnyTLS and Snell connections.
- Fixed potential memory growth in Snell v6 UDP relay when the receiving client is slow or unresponsive.
- Fixed Snell v6 incorrectly using the QUIC proxy mode intended only for Snell v5.
- Fixed inaccurate traffic statistics under concurrent, high-volume requests.
- Fixed pending traffic data potentially being lost during daily or monthly statistics rollover.
- Fixed Logbook record-type filters not being applied correctly.
- Fixed the iOS Tailscale `idle-keepalive` field not reliably accepting `-1`.
- Improved the reliability and security of AnyTLS, Snell, Shadowsocks, VMess, Hysteria, TUIC, Vector, ShadowTLS, Trojan, TrustTunnel, WebSocket, and SOCKS5 connections.
- Connections abandoned while waiting in the reuse pool now automatically retry with a new connection, reducing intermittent failures after network changes or idle periods.
- Improved handling of fragmented protocol responses, preventing valid connections from being incorrectly rejected or left waiting indefinitely.
- Added stricter limits and validation for UDP fragmentation and protocol buffering to reduce excessive memory usage.
- Fixed a serious AnyTLS connection reuse issue that could route data to an incorrect logical stream.
- Fixed several AnyTLS and Snell connection reuse issues that could return terminated connections to the pool or cause requests to hang.
- Fixed TrustTunnel connections occasionally stalling or losing the end of a response under multiplexed or slow-transfer conditions.
- Fixed SOCKS5 UDP relay failures caused by fragmented responses, multi-address DNS results, and domain-form response addresses.
- Fixed Hysteria, TUIC, and Vector connections incorrectly rejecting valid fragmented handshake responses.
- Fixed UDP proxy handling for internationalized domain names.
- Fixed malformed proxy responses potentially causing the Surge tunnel process to terminate.
- Fixed several cases where malformed or incomplete proxy data could cause connections to hang or consume excessive memory.

Official Channel: @SurgeTestFlightFeed

## 2026-07-24 [post 1675](https://t.me/SurgeTestFlight/1675)

#iOS #TestFlight 

Surge 5 5.102.0 (3788) is ready to test on iOS.

What to Test

### Suspend

- Optimized access to the Ponte management page. It can now be used even when Surge is in the Suspend state.
- Added manual suspension controls to the Start context menu:
  - Suspend: forces Surge into suspended mode. In the suspended state, Surge only refrains from configuring VIF interception; all other functions, including scripts and HTTP/SOCKS5/MTProto proxy servers, work normally.
  - Bypass Suspension: temporarily overrides automatic suspension caused by the current Wi-Fi network or Surge Gateway detection. 

You can long-press the Start Page tab or the Start button in the upper-right corner of the Cards page to access this menu.

### Senll Server

- Snell proxy servers can now be configured and used on iOS and tvOS.

### DNS

- Added DNS-over-TCP support. DNS server settings now accept tcp://hostname[:port].

### MTProto & Proxy Services

- Modules can now include an [MTProto] section, using the same validation rules as the main profile.
- The MTProto server now supports using 0.0.0.0 http://0.0.0.0/ to provide services to LAN devices.

### Misc

- Editing a proxy or policy group now preserves line conditions such as #!IOS-ONLY and #!MACOS-ONLY.
- JavaScript sessions now execute user code in a scoped block, preventing top-level declarations from leaking into subsequent executions.

Official Channel: @SurgeTestFlightFeed

## 2026-07-23 [post 1673](https://t.me/SurgeTestFlight/1673)

#iOS #TestFlight 

Surge 5 5.102.0 (3786) is ready to test on iOS.

What to Test

### New Feature: Surge as MTProto Server

Surge now can operate as an incoming MTProto proxy server for Telegram. 

Please read manual for more information: https://manual.nssurge.com/others/mtproto.html https://manual.nssurge.com/others/mtproto.html

TL;DR
Using MTProto instead of SOCKS or VIF to take over Telegram can:

1. Telegram has a notorious SOCKS5 bug in which it can put an IPv6 destination address into an IPv4 request. The malformed destination causes a large number of invalid connection attempts to be sent to Surge. MTProto avoids this path entirely.

2. Force connections to Telegram servers over IPv6. Telegram’s IPv4 servers have a bug that can easily cause the connection to hang without responding. IPv6 nodes do not have this issue, and MTProto allows the intermediary proxy to determine the specific DC service address. Therefore, setting ipv6=true can resolve this persistent problem. (The proxy server must support IPv6 forwarding.)

### Tailscale

- Added automatic MagicDNS routing. Surge can discover the tailnet’s MagicDNS suffix and automatically route matching domains through the corresponding Tailscale policy.
- Automatic MagicDNS routing is enabled by default for newly created policies and can be disabled with auto-add-magic-dns-rule = false.
- Improved Tailscale session warm-up and recovery. Sessions now retry MagicDNS discovery after startup failures and network changes without requiring matching traffic to arrive first.
- Changed idle-keepalive semantics: 0 now uses the default value of 600 seconds, while -1 keeps the Tailscale session always active.

### External Resources

- External resource pages on macOS and iOS now display live updating, ready, and failure states more accurately.
- Remote-device management now reports the current update state and detailed errors for each external resource.
- “Update All” now reports actual failures instead of completing successfully when one or more resources could not be updated.
- HTTP error responses are no longer accepted as external resource content.
- Ruleset and domain-set indexes are now generated transactionally. If downloaded content cannot be parsed or indexed, the last working index is preserved.
- Active resources referenced by the current profile are no longer removed by age-based cache cleanup.
- Fixed custom update intervals being lost when the same resource was referenced from multiple profile sections.
- Profiles now reject using the same external resource as both a RULE-SET and a DOMAIN-SET.

### Configuration & Proxy Policies

- Fixed multi-value ALPN settings being corrupted or partially lost when proxy policies were copied or serialized.
- Improved configuration parsing for quoted separators, empty quoted values, Unicode text, and limited-component splitting.

### Stability & Correctness

- Fixed a potential crash when the GeoIP database was reloaded while traffic was being processed.
- Improved DDNS synchronization and error reporting, including complete CloudKit pagination and correct handling when the public IP address cannot be obtained.
- Fixed potential crashes caused by malformed RDAP responses or missing/corrupted icon bundle data.
- Improved WHOIS/RDAP support for internationalized domains and reduced bootstrap loading time by downloading missing datasets concurrently.
- Fixed route-table diagnostics potentially terminating the app or leaking memory when system route information could not be read.
- Fixed stale incoming-proxy ban records not being cleaned up correctly and potentially weakening repeated-failure blocking.
- Fixed several correctness issues affecting official module updates, HAR export status text and progress, RDAP CIDR rendering, network-quality notifications, and log upload callbacks.

Official Channel: @SurgeTestFlightFeed

## 2026-07-22 [post 1671](https://t.me/SurgeTestFlight/1671)

#iOS #TestFlight 

Surge 5 5.102.0 (3784) is ready to test on iOS.

What to Test

Fix the issue where MITM cannot load the CA certificate

Official Channel: @SurgeTestFlightFeed

## 2026-07-22 [post 1670](https://t.me/SurgeTestFlight/1670)

#iOS #TestFlight 

Surge 5 5.102.0 (3783) is ready to test on iOS.

What to Test

- Improved QUIC reliability on lossy networks by preventing legitimate duplicate retransmissions from triggering the protocol abuse limiter.
- Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-07-21 [post 1669](https://t.me/SurgeTestFlight/1669)

#iOS #TestFlight 

Surge 5 5.102.0 (3782) is ready to test on iOS.

What to Test

Fix a crash related to Ponte

Official Channel: @SurgeTestFlightFeed

## 2026-07-21 [post 1666](https://t.me/SurgeTestFlight/1666)

#iOS #TestFlight 

Surge 5 5.102.0 (3781) is ready to test on iOS.

What to Test

System

* The minimum system version requirement has been raised to iOS 17.0.
* iOS Intent support (Shortcuts) has been reworked.
* NE/VPN start/stop-related logic optimization and bug fixes.

TLS

* Added server-cert-verify-name to independently specify the hostname used for proxy server certificate verification without changing SNI. This parameter applies to all TLS- and QUIC-based proxy protocols.

ECN

* Reworked ECN configuration and packet handling across QUIC, WireGuard, Tailscale, Ponte, and nested UDP tunnels.
* Correctly preserves ECN and DSCP/TOS metadata across IPv4 and IPv6 encapsulation and decapsulation.
* For QUIC-based proxy protocols, when ECN is enabled, anomalies will be automatically detected and fallback to non-ECN handling.
* ECN is now enabled by default for QUIC-based proxy protocols on supported systems. WireGuard and Tailscale remain disabled by default. Use ecn=false or ecn=true to override the default explicitly.
* Surge Ponte now also has ECN enabled by default, and the client-use-ecn parameter has been removed.

DNS

* Optimized TCP connection establishment for prefer-v4 and prefer-v6. In earlier versions, these two parameters indicated which record to use when a domain name had both A and AAAA records. Now, during the TCP handshake, A or AAAA records are used preferentially; if the handshake cannot be completed within 3 seconds, other records will start to be tried.

Tailscale

* Tailscale can now begin handling traffic as soon as a valid network map is received, without waiting for the home DERP connection to be established.
* Improved recovery after network changes and control-server reconnections by preserving the last known home DERP region and retrying peer handshakes at the appropriate time.
* Aligned DERP measurement and selection behavior with official Tailscale client, improving compatibility with custom DERP maps, STUN-only nodes, fallback probes, and temporarily unavailable control connections.
* Sensitive values such as authentication keys and authorization URLs are now redacted from verbose Tailscale control logs.

Codebase Refactoring

Due to the large number of changes, the content exceeds the length limit for the TestFlight update notes. Please refer to the Mac version Beta Release Note; all changes have been synced to the iOS version.

https://nssurge.com/support/mac/release-notes?beta=1 https://nssurge.com/support/mac/release-notes?beta=1

Official Channel: @SurgeTestFlightFeed

## 2026-07-15 [post 1659](https://t.me/SurgeTestFlight/1659)

#iOS #TestFlight 

Surge 5 5.102.0 (3779) is ready to test on iOS.

What to Test

* Restore support for passing string parameters to the JS setTimeout function to avoid compatibility issues.
* Other minor fixes.

5.20.0 Release Candidate 5

Official Channel: @SurgeTestFlightFeed

## 2026-07-14 [post 1657](https://t.me/SurgeTestFlight/1657)

#iOS #TestFlight 

Surge 5 5.102.0 (3771) is ready to test on iOS.

What to Test

Optimize the compatibility of Tailscale's DNS Client with the peer OS system (macOS)

5.20.0 Release Candidate 4

Official Channel: @SurgeTestFlightFeed

## 2026-07-13 [post 1656](https://t.me/SurgeTestFlight/1656)

#iOS #TestFlight 

Surge 5 5.102.0 (3770) is ready to test on iOS.

What to Test

Optimize Tailscale during network switching and in bad network environments

Official Channel: @SurgeTestFlightFeed

## 2026-07-13 [post 1655](https://t.me/SurgeTestFlight/1655)

#iOS #TestFlight 

Surge 5 5.102.0 (3769) is ready to test on iOS.

What to Test

Enable the keep-alive mechanism for all QUIC-based protocols

5.20.0 Release Candidate 3

Official Channel: @SurgeTestFlightFeed

## 2026-07-12 [post 1653](https://t.me/SurgeTestFlight/1653)

#iOS #TestFlight 

Surge 5 5.102.0 (3767) is ready to test on iOS.

What to Test

* Access to Tailscale's control plane API no longer follows the handling of the underlying-proxy parameter; it now uses the standard rule system. If special handling is needed, you can configure rules to specify a policy.
* Supports the InsecureForTests parameter for custom DERP servers.
* Fixed the issue where download speed tests could not be performed.
* Other minor fixes.

5.20.0 RC2

Official Channel: @SurgeTestFlightFeed

## 2026-07-11 [post 1652](https://t.me/SurgeTestFlight/1652)

#iOS #TestFlight 

Surge 5 5.102.0 (3766) is ready to test on iOS.

What to Test

# Tailscale
* Fix the issue where Tailscale's Home region is always selected as nyc
* Optimize Tailscale's node probing and transition logic

# Codebase Refactoring
We have completed a comprehensive review of Surge’s core functionality and resolved numerous implementation issues, edge cases, and long-standing inconsistencies.
This ongoing refactoring effort improves maintainability and helps provide a more robust foundation for future development.

Official Channel: @SurgeTestFlightFeed

## 2026-07-10 [post 1651](https://t.me/SurgeTestFlight/1651)

#iOS #TestFlight 

Surge 5 5.102.0 (3765) is ready to test on iOS.

What to Test

#### Tailscale Engine Rewrite

In previous beta versions, Surge’s Tailscale implementation was based on the official experimental `tailscale-rs` library. Because its feature set and performance did not fully meet Surge’s requirements, this release replaces that integration with a new proprietary implementation built directly into Surge’s networking engine. The new implementation provides broader functionality, significantly better performance, and richer runtime diagnostics.

1. Direct peer-to-peer connectivity, including NAT traversal and path discovery, is now supported. Surge automatically prefers a direct connection when available and falls back to DERP when necessary. The new `derp-only` option can be used to force all peer traffic through DERP.

2. Single-threaded data-plane throughput has been significantly improved, reaching up to approximately 1.5 Gbps in our lab tests—comparable to the official Tailscale client under the same test conditions.

3. Exit node support has been added. A Tailscale policy can now route Surge-selected traffic through a configured exit node and can therefore be used as a regular outbound policy. This affects only traffic assigned to that policy by Surge and does not change the device-wide default route.

4. Routes advertised by authorized Tailscale subnet routers are now supported. MagicDNS is now better supported.

5. Surge now uses Tailscale-aware latency testing. When exit node isn't configured, Surge performs a native Tailscale connectivity probe against an online peer. If no suitable peer is available, the home DERP server is tested instead. When exit node or `test-url` is configured, the standard HTTP test process is used. Additional initialization time is allowed for control-plane setup and the initial WireGuard handshake.

6. Extensive Tailscale runtime diagnostics have been added to the UI, including control connection state, assigned addresses, exit node status, DERP regions, direct-versus-relay peer paths, peer latency, active connections, endpoints, and MagicDNS information.

7. Existing Tailscale profiles and persisted node identities remain compatible; no profile migration is required.

We plan to add inbound access over WireGuard and Tailscale in a future version, allowing remote devices to connect to Surge and use it as a network gateway.

** Notice: Due to the core engine replacement, Tailscale needs to be registered again. If you did not previously enable the reuse option for the auth key, you must generate a new auth key to complete the new device registration process.**

Please check the manual for more information: https://manual.nssurge.com/policy/tailscale.html https://manual.nssurge.com/policy/tailscale.html

### WireGuard

WireGuard policies now use a dedicated native RTT test when no DNS server is configured, making them suitable for peer-to-peer access without requiring a reachable test URL. When a DNS server is configured, the policy is treated as a standard outbound proxy and continues to use the regular URL test process. WireGuard runtime information and diagnostics have also been updated to reflect the applicable testing mode.

Official Channel: @SurgeTestFlightFeed

## 2026-07-08 [post 1648](https://t.me/SurgeTestFlight/1648)

#iOS #TestFlight 

Surge 5 5.102.0 (3764) is ready to test on iOS.

What to Test

5.20.0 Release Candidate 1

Official Channel: @SurgeTestFlightFeed

## 2026-07-07 [post 1647](https://t.me/SurgeTestFlight/1647)

#iOS #TestFlight 

Surge 5 5.102.0 (3763) is ready to test on iOS.

What to Test

Bug fix

### Abort Assert Log

Surge includes a number of assert checks in its code. Assert checks are a common development and debugging mechanism used to detect situations where the program reaches a state that is different from what the developers expected.

Seeing an assert message does not necessarily mean that Surge has crashed. In many cases, the app can continue working normally, and the assert simply serves as a signal for the developers to review that part of the code.

When an assert is triggered, Surge may automatically save certain temporary logs that were previously held in memory into a log file. This is done to help developers understand what happened before the assert was triggered. This behavior is expected and should not be interpreted as abnormal memory usage or a memory leak.

Assert triggers may be seen more often in beta versions, because beta builds are designed to help identify and diagnose potential issues before a stable release. 

If Surge continues to work normally, the message can usually be ignored. If you notice repeated crashes, broken functionality, or other reproducible problems together with this message, please report the issue with the relevant logs so we can investigate further

Official Channel: @SurgeTestFlightFeed

## 2026-07-06 [post 1644](https://t.me/SurgeTestFlight/1644)

#iOS #TestFlight 

Surge 5 5.102.0 (3762) is ready to test on iOS.

What to Test

Bug fix

Official Channel: @SurgeTestFlightFeed

## 2026-07-03 [post 1642](https://t.me/SurgeTestFlight/1642)

#iOS #TestFlight 

Surge 5 5.102.0 (3761) is ready to test on iOS.

What to Test

Bug fix

Official Channel: @SurgeTestFlightFeed

## 2026-07-03 [post 1640](https://t.me/SurgeTestFlight/1640)

#iOS #TestFlight 

Surge 5 5.102.0 (3760) is ready to test on iOS.

What to Test

* Bug fixes and performance optimization

Official Channel: @SurgeTestFlightFeed

## 2026-07-02 [post 1638](https://t.me/SurgeTestFlight/1638)

#iOS #TestFlight 

Surge 5 5.102.0 (3759) is ready to test on iOS.

What to Test

Crash fix

Official Channel: @SurgeTestFlightFeed

## 2026-07-01 [post 1637](https://t.me/SurgeTestFlight/1637)

#iOS #TestFlight 

Surge 5 5.102.0 (3758) is ready to test on iOS.

What to Test

Optimize Tailscale's performance in IPv4-only networks

Official Channel: @SurgeTestFlightFeed

## 2026-06-30 [post 1635](https://t.me/SurgeTestFlight/1635)

#iOS #TestFlight 

Surge 5 5.102.0 (3756) is ready to test on iOS.

What to Test

* The Smart Group algorithm has been reviewed and upgraded, fixing several potential issues
* Other minor bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-06-29 [post 1633](https://t.me/SurgeTestFlight/1633)

#iOS #TestFlight 

Surge 5 5.102.0 (3755) is ready to test on iOS.

What to Test

* Tailscale: IPv6 DERP servers are now automatically disabled based on network conditions
* The external resource update page will no longer pop up repeatedly
* Fixed some issues when configuring Snell v6 via the UI
* Other minor fixes and updates

Official Channel: @SurgeTestFlightFeed

## 2026-06-26 [post 1630](https://t.me/SurgeTestFlight/1630)

#iOS #TestFlight 

Surge 5 5.102.0 (3754) is ready to test on iOS.

What to Test

* When a massive amount of data (over 10,000 entries) exists in the Logbook, it may prevent access to the Logbook view. Additionally, when Surge attempts to automatically clean up data at midnight, it exceeds the memory limit and is terminated by the system. This version optimizes memory usage during cleanup and limits the maximum number of records to 10,000.
* Other bug and crash fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-06-25 [post 1628](https://t.me/SurgeTestFlight/1628)

#iOS #TestFlight 

Surge 5 5.102.0 (3753) is ready to test on iOS.

What to Test

* Crash fixes
* Fixed an issue where IPv6 UDP packets could not be correctly reassembled when fragments were present

Official Channel: @SurgeTestFlightFeed

## 2026-06-24 [post 1625](https://t.me/SurgeTestFlight/1625)

#iOS #TestFlight 

Surge 5 5.102.0 (3752) is ready to test on iOS.

What to Test

* Fixed an issue where, when using Smart Group with the Snell protocol, target host errors could not be correctly incorporated into the smart algorithm.

Official Channel: @SurgeTestFlightFeed

## 2026-06-23 [post 1622](https://t.me/SurgeTestFlight/1622)

#iOS #TestFlight 

Surge 5 5.102.0 (3748) is ready to test on iOS.

What to Test

* All TLS proxy protocols now support customizing ALPN using the `alpn` field.
* When local DNS mapping is specified using server, multiple DNS servers can now be configured.
* Other bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-06-22 [post 1620](https://t.me/SurgeTestFlight/1620)

#iOS #TestFlight 

Surge 5 5.102.0 (3744) is ready to test on iOS.

What to Test

QUIC performance parameter tuning

Official Channel: @SurgeTestFlightFeed

## 2026-06-22 [post 1618](https://t.me/SurgeTestFlight/1618)

#iOS #TestFlight 

Surge 5 5.102.0 (3743) is ready to test on iOS.

What to Test

* Optimized QUIC performance on high-RTT network. If you still encounter issues where QUIC-like protocols perform worse than expected, please reproduce the issue in verbose mode and send the log to bug-report@nssurge.com
* Fixed compatibility issues between DoH3 and some servers.
* Added Gecko obfuscation support for Hysteria2, configured using the gecko-password parameter.
* Updated Snell v6 to beta4, fixing the issue where UDP did not work in unshaped and unsafe-raw modes.

Official Channel: @SurgeTestFlightFeed

## 2026-06-19 [post 1616](https://t.me/SurgeTestFlight/1616)

#iOS #TestFlight 

Surge 5 5.102.0 (3741) is ready to test on iOS.

What to Test

Completed the tuning of the QUIC protocol, comprehensively optimizing QUIC’s performance across various network environments.

Official Channel: @SurgeTestFlightFeed

## 2026-06-18 [post 1614](https://t.me/SurgeTestFlight/1614)

#iOS #TestFlight 

Surge 5 5.102.0 (3740) is ready to test on iOS.

What to Test

* Crash fixes and performance optimizations

Official Channel: @SurgeTestFlightFeed

## 2026-06-18 [post 1613](https://t.me/SurgeTestFlight/1613)

#iOS #TestFlight 

Surge 5 5.102.0 (3734) is ready to test on iOS.

What to Test

* Crash fixes and performance optimizations

Recent updates include extensive architectural changes, which may cause instability. Please note that you can roll back to a previous version at any time through the TestFlight app.

You can also manage push notifications and emails for new builds through the TestFlight app. These emails are sent by Apple, so contacting us will not cancel them.

Official Channel: @SurgeTestFlightFeed

## 2026-06-17 [post 1610](https://t.me/SurgeTestFlight/1610)

#iOS #TestFlight 

Surge 5 5.102.0 (3733) is ready to test on iOS.

What to Test

* Optimize QUIC-related performance
* Bug fix

Official Channel: @SurgeTestFlightFeed

## 2026-06-16 [post 1608](https://t.me/SurgeTestFlight/1608)

#iOS #TestFlight 

Surge 5 5.102.0 (3732) is ready to test on iOS.

What to Test

* Completely rewrote QUIC flow control, resolving memory usage and performance issues that could occur with the Hysteria2 and TUIC protocols under certain network conditions. Due to the scale of the changes, issues may occur. If you encounter any problems, please reproduce them in verbose mode and send the logs to bug-report@nssurge.com
* Surge Ponte throughput performance has also been improved. However, we are still conducting further optimization to achieve higher goals.
* Fixed an issue where the policy group page might fail to correctly display the latest status when there are too much cells.

Official Channel: @SurgeTestFlightFeed

## 2026-06-12 [post 1604](https://t.me/SurgeTestFlight/1604)

#iOS #TestFlight 

Surge 5 5.102.0 (3730) is ready to test on iOS.

What to Test

# Tailscale Support (Beta, New Subscription Feature)

Surge now supports Tailscale as a policy.

With this feature, Surge can join your Tailscale tailnet directly and route selected traffic through Tailscale peers using the existing Surge rule system. You can use Tailscale IPs, and tailnet-only services together with Surge policies, policy groups, DNS handling, traffic logging, and rule-based routing.

Please check Surge Knowledge Base for more information: https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale https://kb.nssurge.com/surge-knowledge-base/guidelines/tailscale

# Snell v6 (No Subscription Required)

Introduced Snell v6, featuring PSK-derived deployment-level protocol diversity that generates unique traffic characteristics for each deployment, reducing reliance on a single protocol fingerprint while preserving Snell’s core goals of performance, deployment simplicity, accurate error reporting, and full TCP semantics. Snell v6 also adds new IPv4/IPv6 network stack controls including dns-ip-preference and multi-address listen support, and is currently available for beta testing.

Please check our blog for more information: https://nssurge.com/blog/snell-v6/ https://nssurge.com/blog/snell-v6/

# Other
* The UI configuration interface has been completed for the recently added proxy protocol parameters, including Tailscale.
* The `header` parameter for the HTTP proxy type can now override original fields, including Host field.
* Fixed an issue where the `header` parameter did not take effect in HTTP/1.1 CONNECT mode.

Official Channel: @SurgeTestFlightFeed

## 2026-06-04 [post 1595](https://t.me/SurgeTestFlight/1595)

#iOS #TestFlight 

Surge 5 5.101.0 (3725) is ready to test on iOS.

What to Test

5.19.0 RC6
-------------
Bug fix

Official Channel: @SurgeTestFlightFeed

## 2026-06-04 [post 1594](https://t.me/SurgeTestFlight/1594)

#iOS #TestFlight 

Surge 5 5.101.0 (3723) is ready to test on iOS.

What to Test

5.19.0 RC5
-------------
Fixed a potential sudden spike in memory usage that could occur when executing specific scripts on iOS 26.4 & 26.5.

Official Channel: @SurgeTestFlightFeed

## 2026-06-04 [post 1593](https://t.me/SurgeTestFlight/1593)

#iOS #TestFlight 

Surge 5 5.101.0 (3718) is ready to test on iOS.

What to Test

5.19.0 RC4
----------
Bug fix

Official Channel: @SurgeTestFlightFeed

## 2026-06-03 [post 1592](https://t.me/SurgeTestFlight/1592)

#iOS #TestFlight 

Surge 5 5.101.0 (3715) is ready to test on iOS.

What to Test

5.19.0 RC3
---------
* Fixed the issue where the two most recent subscription update features were not displayed correctly in the list.
* Fix the issue where policy group icons cannot be modified under managed configuration

Official Channel: @SurgeTestFlightFeed

## 2026-06-02 [post 1591](https://t.me/SurgeTestFlight/1591)

#iOS #TestFlight 

Surge 5 5.101.0 (3709) is ready to test on iOS.

What to Test

5.18.1 RC2
---------
* Fix the issue where policy group icons cannot be modified under managed configuration

Official Channel: @SurgeTestFlightFeed

## 2026-06-01 [post 1589](https://t.me/SurgeTestFlight/1589)

#iOS #TestFlight 

Surge 5 5.101.0 (3706) is ready to test on iOS.

What to Test

5.18.1 RC1

Full Release Note
-----
* The storage logic for icon configuration in the iOS version has been adjusted. Now, when the profile is editable, it will preferentially be written into the profile to ensure interoperability with the Mac version. Only when the profile is read-only will a separate UI profile be used for storage.
* Fixed an issue where sending SNI did not strictly comply with RFC6066. Now, when an IP address is used as the hostname, the IP address will not be sent as SNI.
* Fixed an issue where crashes could occur when using ShadowTLS with certain servers.
* Fixed an issue where, when the Logbook contained a very large amount of data, it could not be viewed remotely via the Dashboard.
* Other performance optimization and minor enhancements.

Official Channel: @SurgeTestFlightFeed

## 2026-05-28 [post 1585](https://t.me/SurgeTestFlight/1585)

#iOS #TestFlight 

Surge 5 5.101.0 (3704) is ready to test on iOS.

What to Test

Fix possible crashes in the script system

Official Channel: @SurgeTestFlightFeed

## 2026-05-27 [post 1582](https://t.me/SurgeTestFlight/1582)

#iOS #TestFlight 

Surge 5 5.101.0 (3703) is ready to test on iOS.

What to Test

* Fixed an issue where sending SNI did not strictly comply with RFC6066. Now, when an IP address is used as the hostname, the IP address will not be sent as SNI.
* Fixed an issue where crashes could occur when using ShadowTLS with certain servers.

Official Channel: @SurgeTestFlightFeed

## 2026-05-25 [post 1577](https://t.me/SurgeTestFlight/1577)

#iOS #TestFlight 

Surge 5 5.101.0 (3702) is ready to test on iOS.

What to Test

* The storage logic for icon configuration in the iOS version has been adjusted. Now, when the profile is editable, it will preferentially be written into the profile to ensure interoperability with the Mac version. Only when the profile is read-only will a separate UI profile be used for storage.
* Bug fixes.

Official Channel: @SurgeTestFlightFeed

## 2026-05-24 [post 1574](https://t.me/SurgeTestFlight/1574)

#iOS #TestFlight 

Surge 5 5.101.0 (3701) is ready to test on iOS.

What to Test

Optimize the script engine’s memory spikes on the new iOS system.

Official Channel: @SurgeTestFlightFeed

## 2026-05-23 [post 1573](https://t.me/SurgeTestFlight/1573)

#iOS #TestFlight 

Surge 5 5.101.0 (3699) is ready to test on iOS.

What to Test

* Fixed an issue where, when the Logbook contained a very large amount of data, it could not be viewed remotely via the Dashboard.
* Other minor optimizations.

Official Channel: @SurgeTestFlightFeed

## 2026-05-21 [post 1572](https://t.me/SurgeTestFlight/1572)

#iOS #TestFlight 

Surge 5 5.101.0 (3698) is ready to test on iOS.

What to Test

Performance optimization and minor enhancements

Official Channel: @SurgeTestFlightFeed

## 2026-05-19 [post 1570](https://t.me/SurgeTestFlight/1570)

#iOS #TestFlight 

Surge 5 5.101.0 (3696) is ready to test on iOS.

What to Test

- 优化脚本引擎表现

Official Channel: @SurgeTestFlightFeed

## 2026-05-18 [post 1568](https://t.me/SurgeTestFlight/1568)

#iOS #TestFlight 

Surge 5 5.101.0 (3693) is ready to test on iOS.

What to Test

- 重写 JS WebKit 引擎调度器，解决一些内存突发占用问题

Official Channel: @SurgeTestFlightFeed

## 2026-05-18 [post 1566](https://t.me/SurgeTestFlight/1566)

#iOS #TestFlight 

Surge 5 5.101.0 (3691) is ready to test on iOS.

What to Test

- HTTP/2 CONNECT 和 TrustTunnel 代理现在支持 multiplex，由于过多子链接复用同一个 TCP 连接，可能产生性能问题，因此默认只允许最多 3 个子连接，可通过配置策略参数 max-streams 调整。

Official Channel: @SurgeTestFlightFeed

## 2026-05-15 [post 1562](https://t.me/SurgeTestFlight/1562)

#iOS #TestFlight 

Surge 5 5.101.0 (3690) is ready to test on iOS.

What to Test

关于 Surge iOS 功能更新订阅机制的调整

自 Surge iOS 推出功能更新订阅机制以来，我们一直希望在「持续演进产品能力」与「保障长期使用体验」之间保持合理的平衡。经过评估，我们决定进行如下调整：

1. 未来新增的所有代理协议兼容支持，将不再纳入功能更新订阅范围，所有用户均可直接使用。
2. 现已实验性支持的 TrustTunnel，也不会存在订阅限制，可以直接使用。

我们认为，协议兼容性应当作为长期稳定提供的基础能力，而不是阶段性的增量功能。这意味着，未来用户无需因为订阅状态，而担心基础协议支持的可用性；新的协议兼容能力也能够更直接、更持续地向所有用户开放。

调整后，订阅更新将更聚焦于新的高级功能，而协议兼容性本身，则会作为产品的长期基础能力持续维护。

与此同时，代理协议生态本身也始终处于持续变化之中。一些协议会不断演进，也有一些协议会逐渐退出主流使用场景。为了保证 Surge 长期稳定的代码库维护与整体产品质量，我们也会结合实际使用情况，对部分历史协议进入维护冻结状态，或在未来逐步结束支持。

我们会尽可能谨慎地处理相关调整，并提前进行说明，以减少对现有用户配置与使用体验的影响。

感谢大家一直以来的支持与反馈。

----------------------

- 新增 HTTP/2 CONNECT 代理支持，可通过 h2-connect 类型配置基于 HTTP/2 的 CONNECT 代理连接。
- HTTP, HTTPS, HTTP/2 CONNECT, TrustTunnel 代理现支持自定义请求头，可在代理配置中使用 headers= 添加额外 header，例如：

Proxy = http, example.com http://example.com/, 8080, headers=X-Client:Surge;X-Token:abc
Proxy = h2-connect, example.com http://example.com/, 443, headers=X-Padding:

- 自定义 header 支持  与  占位符，连接时会自动生成 URL-safe 随机字符串，适用于需要动态 padding 或请求特征扰动的场景。

Official Channel: @SurgeTestFlightFeed

## 2026-05-13 [post 1558](https://t.me/SurgeTestFlight/1558)

#iOS #TestFlight 

Surge 5 5.101.0 (3689) is ready to test on iOS.

What to Test

- 修正 JS WebView 引擎在新版系统下，在高并发时可能需要冷启动问题

Official Channel: @SurgeTestFlightFeed

## 2026-05-05 [post 1548](https://t.me/SurgeTestFlight/1548)

#iOS #TestFlight 

Surge 5 5.101.0 (3684) is ready to test on iOS.

What to Test

- 细节问题修正

5.18.0 RC1

Official Channel: @SurgeTestFlightFeed

## 2026-04-29 [post 1545](https://t.me/SurgeTestFlight/1545)

#iOS #TestFlight 

Surge 5 5.101.0 (3683) is ready to test on iOS.

What to Test

- 修正 Logbook 进入脚本详情页后可能出现的数据错乱问题
- 优化 $persistentStore 管理页面，新增搜索、导入导出、全部删除等操作

Official Channel: @SurgeTestFlightFeed

## 2026-04-28 [post 1544](https://t.me/SurgeTestFlight/1544)

#iOS #TestFlight 

Surge 5 5.101.0 (3682) is ready to test on iOS.

What to Test

- 优化 Logbook 数据量极大时的加载和搜索性能
- 大幅优化查看脚本类事件时的展示

Official Channel: @SurgeTestFlightFeed

## 2026-04-28 [post 1543](https://t.me/SurgeTestFlight/1543)

#iOS #TestFlight 

Surge 5 5.101.0 (3681) is ready to test on iOS.

What to Test

- 修正一处 Logbook 崩溃问题

Official Channel: @SurgeTestFlightFeed

## 2026-04-27 [post 1538](https://t.me/SurgeTestFlight/1538)

#iOS #TestFlight 

Surge 5 5.101.0 (3680) is ready to test on iOS.

What to Test

Logbook 日志簿功能现已在 Surge Mac 版本中加入，Surge Dashboard 可读取远程实例的 Logbook 内容，同时支持查阅脚本类型记录的输入输出，以及日志输出。对端可以是 Surge iOS 或 Mac，所有内容均支持远程载入。

Official Channel: @SurgeTestFlightFeed

## 2026-04-25 [post 1535](https://t.me/SurgeTestFlight/1535)

#iOS #TestFlight 

Surge 5 5.101.0 (3679) is ready to test on iOS.

What to Test

- 优化 QUIC 的 buffer 控制逻辑，应对更严苛环境下的突发内存占用

Official Channel: @SurgeTestFlightFeed

## 2026-04-24 [post 1534](https://t.me/SurgeTestFlight/1534)

#iOS #TestFlight 

Surge 5 5.101.0 (3678) is ready to test on iOS.

What to Test

- 重构 QUIC 协议的内存管理，解决在特定情况下，QUIC-based 协议可能出现突发内存占用过高导致 Surge 被系统停止的问题

Official Channel: @SurgeTestFlightFeed

## 2026-04-23 [post 1533](https://t.me/SurgeTestFlight/1533)

#iOS #TestFlight 

Surge 5 5.101.0 (3677) is ready to test on iOS.

What to Test

- 修正部分脚本会导致 Logbook 崩溃的问题
- 脚本执行异常会计入 Logbook 了

Official Channel: @SurgeTestFlightFeed

## 2026-04-21 [post 1531](https://t.me/SurgeTestFlight/1531)

#iOS #TestFlight 

Surge 5 5.101.0 (3672) is ready to test on iOS.

What to Test

- 修正日志乱码问题
- 修正部分脚本可能产生多条日志的问题
- 如果脚本产生了日志，则优先展示日志

Official Channel: @SurgeTestFlightFeed

## 2026-04-21 [post 1530](https://t.me/SurgeTestFlight/1530)

#iOS #TestFlight 

Surge 5 5.101.0 (3670) is ready to test on iOS.

What to Test

- 修正 Logbook 显示脚本类型时，有时无法合并显示的问题
- 现在可以显示脚本类型了
- 可以搜索脚本的触发 URL 和脚本类型了
- 脚本日志页面支持带换行日志的展示
- 其他优化

Official Channel: @SurgeTestFlightFeed

## 2026-04-20 [post 1529](https://t.me/SurgeTestFlight/1529)

#iOS #TestFlight 

Surge 5 5.101.0 (3668) is ready to test on iOS.

What to Test

优化 Logbook 关于脚本的展示
- 现在同时存在开始和停止记录时，将合并为一条记录
- 详情页面将同时显示 Input/Output/Log
- 列表中展示 HTTP 类型脚本的触发 URL

Official Channel: @SurgeTestFlightFeed

## 2026-04-18 [post 1528](https://t.me/SurgeTestFlight/1528)

#iOS #TestFlight 

Surge 5 5.101.0 (3667) is ready to test on iOS.

What to Test

- 修正中文语言下 Logbook 记录的网络切换事件异常的问题

Official Channel: @SurgeTestFlightFeed

## 2026-04-17 [post 1527](https://t.me/SurgeTestFlight/1527)

#iOS #TestFlight 

Surge 5 5.101.0 (3666) is ready to test on iOS.

What to Test

- 修正 Logbook 搜索状态无法下无法查看日志的问题
- 区分 Logbook 中脚本的日志显示，现在仅会显示该 Session 的日志内容（仅限更新新版本后再执行的脚本）

Official Channel: @SurgeTestFlightFeed

## 2026-04-17 [post 1526](https://t.me/SurgeTestFlight/1526)

#iOS #TestFlight 

Surge 5 5.101.0 (3665) is ready to test on iOS.

What to Test

- Logbook 新增脚本聚焦模式，大幅优化脚本相关功能，现在可以直接查看脚本输入、输出、日志等信息了

Official Channel: @SurgeTestFlightFeed

## 2026-04-17 [post 1525](https://t.me/SurgeTestFlight/1525)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.101.0 (3664) is ready to test on iOS.

What to Test

（由于自上次订阅功能更新时间过长，现已将功能订阅到期日在 2025 年 12 月 11 日以后的所有用户，免费展期 3 个月，详见：https://community.nssurge.com/d/4142-surge-ios https://community.nssurge.com/d/4142-surge-ios ）

新的订阅功能：Logbook 日志本

用于持久化记录发生的各种事件，目前包含：引擎启动和停止、网络切换、脚本启动和停止、脚本超时等，后续将加入更多事件类型。

同时，脚本可以使用 $surge.logbook("content") 主动写入内容到日志本。

Official Channel: @SurgeTestFlightFeed

## 2026-04-12 [post 1513](https://t.me/SurgeTestFlight/1513)

#iOS #TestFlight 

Surge 5 5.101.0 (3663) is ready to test on iOS.

What to Test

- 修正使用 Trust Tunnel 时出现的内存泄露问题
- 修正极低概率下出现的一个崩溃问题
- 修正开启 HTTP API TLS 时，API 请求可能卡主的问题
- 修正 UI 上的一些细节问题

Official Channel: @SurgeTestFlightFeed

## 2026-03-11 [post 1495](https://t.me/SurgeTestFlight/1495)

#iOS #TestFlight 

Surge 5 5.101.0 (3661) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-03-10 [post 1489](https://t.me/SurgeTestFlight/1489)

#iOS #TestFlight 

Surge 5 5.101.0 (3656) is ready to test on iOS.

What to Test:

为所有 TLS 相关功能（如代理协议，MITM，DoH/DoT/DoH3）新增对 X25519MLKEM768 后量子混合密钥交换组的支持

Official Channel: @SurgeTestFlightFeed

## 2026-03-04 [post 1484](https://t.me/SurgeTestFlight/1484)

#iOS #TestFlight 

Surge 5 5.101.0 (3654) is ready to test on iOS.

What to Test:

Ponte 页面中新增 Debug 消息开关，开启后可在 Ponte 连接过程中给出具体的连接状态消息

Official Channel: @SurgeTestFlightFeed

## 2026-03-03 [post 1482](https://t.me/SurgeTestFlight/1482)

#iOS #TestFlight 

Surge 5 5.101.0 (3653) is ready to test on iOS.

What to Test:

- 增加一项 workaround，解决新版 iOS 系统下，长脚本执行一段时间后，setTimeout 因系统节约资源最多 2s 触发一次的问题

Official Channel: @SurgeTestFlightFeed

## 2026-02-26 [post 1478](https://t.me/SurgeTestFlight/1478)

#iOS #TestFlight 

Surge 5 5.101.0 (3652) is ready to test on iOS.

What to Test:

- 新增配置切换的 Intent，可以在 Shortcuts 中直接切换当前的 Surge 配置了

- 撤销了策略禁用的机制，因为此项改动涉及的细节问题较多，与部分用户的习惯相冲突。
同时，在新版本中，策略组不再校验子策略名的有效性，如果引用的子策略不存在，那么将在运行时自动隐去不存在的选项。include-other-group 参数也同样进行了修改。
不过请注意，在 [Rule] 中使用不存在策略，依然会触发硬性配置错误提示。

Official Channel: @SurgeTestFlightFeed

## 2026-02-25 [post 1476](https://t.me/SurgeTestFlight/1476)

#iOS #TestFlight 

Surge 5 5.101.0 (3650) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2026-02-25 [post 1472](https://t.me/SurgeTestFlight/1472)

#iOS #TestFlight 

Surge 5 5.101.0 (3649) is ready to test on iOS.

What to Test:

一项实验性改动，现在 [Proxy] 和 [Proxy Group] 段，支持使用 # 注释整行将一个项目标记为未启动了。

相比原本直接注释掉不生效，被禁用掉的策略不会触发配置检查的错误。先前版本在其他规则、策略组中引用了一个不存在的策略，会直接导致 Surge 无法启动。

禁用掉的策略，如果是被其他策略组使用，或者以 include-other-group 或 include-all-proxies 被引用，则不会出现在该组的可选项中。

如果使用规则或其他方式直接使用了被禁用的策略，那该策略将会被 SUBSTITUTE 策略（DIRECT 策略的别名）取代。

Official Channel: @SurgeTestFlightFeed

## 2026-02-22 [post 1469](https://t.me/SurgeTestFlight/1469)

#iOS #TestFlight 

Surge 5 5.101.0 (3646) is ready to test on iOS.

What to Test:

- 修正 AnyTLS 与部分服务端的兼容性问题（reuse 开启时，若之前的请求失败，会导致后续请求卡死）

Official Channel: @SurgeTestFlightFeed

## 2026-02-21 [post 1465](https://t.me/SurgeTestFlight/1465)

#iOS #TestFlight 

Surge 5 5.101.0 (3644) is ready to test on iOS.

What to Test:

- 吞吐量测试的各项参数，现在可以自定义了，也支持通过模块写入
[Testing]
download-url = 
upload-url download-url-proxy = // 未提供时使用 download-url
upload-url-proxy = // 未提供时使用 upload-url
download-concurrency = // 默认为 4
upload-concurrency = // 默认为 4
download-duration-limit = // 默认为 10 秒
upload-size-limit = // 默认为 1GB
upload-duration-limit =  // 默认为 10 秒

- iOS 26.4 beta 下部分脚本可能出现内存问题，增加了一个 workaround
- 新增 TrustTunnel 协议支持，由于尚未完成，暂未加入到订阅限制中

Official Channel: @SurgeTestFlightFeed

## 2026-01-23 [post 1455](https://t.me/SurgeTestFlight/1455)

#iOS #TestFlight 

Surge 5 5.101.0 (3642) is ready to test on iOS.

What to Test:

- 支持直接使用 #!include  引用托管配置，无需先添加托管配置为本地配置。（即 Mac 版本的 Linked Profile 功能）

Official Channel: @SurgeTestFlightFeed

## 2026-01-23 [post 1453](https://t.me/SurgeTestFlight/1453)

#iOS #TestFlight 

Surge 5 5.101.0 (3641) is ready to test on iOS.

What to Test:

- 修正使用 QUIC 类型协议或者 h3 DNS 时，低概率出现的崩溃问题
- 企业/团队授权，可以使用 tvOS 版本了
- 修正只有小卡片视图可以显示更新外部资源菜单项的问题

Official Channel: @SurgeTestFlightFeed

## 2026-01-12 [post 1437](https://t.me/SurgeTestFlight/1437)

#iOS #TestFlight 

Surge 5 5.101.0 (3635) is ready to test on iOS.

What to Test:

5.17.0 RC3

- 修正黑暗模式下的一些问题
- 所有代理协议的 QUIC block 行为，现在均默认调整为阻止。
即使通过基于 UDP 的协议对 QUIC 流量进行转发，由于 QUIC 的流量控制机制对中间节点不可见，代理服务器无法像转发 TCP 流量那样引入额外的中间缓冲区。在链路质量不佳的情况下，其整体稳定性往往明显弱于基于 TCP 的协议。
因此，放行 QUIC 流量可能导致显著的使用体验下降，仅建议具有明确需求的用户手动启用。

Official Channel: @SurgeTestFlightFeed

## 2026-01-09 [post 1434](https://t.me/SurgeTestFlight/1434)

#iOS #TestFlight 

Surge 5 5.101.0 (3634) is ready to test on iOS.

What to Test:

5.17.0 RC2
- 因用户反馈容易误触，取消了再次点击进行开关的设计
- 修正部分设备上长按菜单弹出的行为错误的问题
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2026-01-09 [post 1433](https://t.me/SurgeTestFlight/1433)

#iOS #TestFlight 

Surge 5 5.101.0 (3628) is ready to test on iOS.

What to Test:

5.17.0 RC1

- 在 iOS 26 中恢复了长按 tab bar 的快捷菜单

Official Channel: @SurgeTestFlightFeed

## 2026-01-09 [post 1429](https://t.me/SurgeTestFlight/1429)

#iOS #TestFlight 

Surge 5 5.101.0 (3627) is ready to test on iOS.

What to Test:

- 再次点击开始页面的 tab bar 图标，可以直接开关 Surge（也可以直接双击触发）
- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2026-01-08 [post 1426](https://t.me/SurgeTestFlight/1426)

#iOS #TestFlight 

Surge 5 5.101.0 (3625) is ready to test on iOS.

What to Test:

- 优化 UI 细节

Official Channel: @SurgeTestFlightFeed

## 2026-01-07 [post 1425](https://t.me/SurgeTestFlight/1425)

#iOS #TestFlight 

Surge 5 5.101.0 (3624) is ready to test on iOS.

What to Test:

- 修正 iPad 上出现的各种问题

Official Channel: @SurgeTestFlightFeed

## 2026-01-06 [post 1423](https://t.me/SurgeTestFlight/1423)

#iOS #TestFlight 

Surge 5 5.101.0 (3622) is ready to test on iOS.

What to Test:

- 修正将一般 UDP 流量识别为 QUIC 的问题
- 开始页面为 iOS 26 进行了优化

Official Channel: @SurgeTestFlightFeed

## 2026-01-05 [post 1421](https://t.me/SurgeTestFlight/1421)

#iOS #TestFlight 

Surge 5 5.101.0 (3621) is ready to test on iOS.

What to Test:

- 优化 QUIC 的 SNI 提取，支持从不完整的 initial 包中提取 SNI

Official Channel: @SurgeTestFlightFeed

## 2026-01-04 [post 1420](https://t.me/SurgeTestFlight/1420)

#iOS #TestFlight 

Surge 5 5.101.0 (3619) is ready to test on iOS.

What to Test:

- 支持 Hysteria 2 的 Salamander 混淆模式，配置参数 `salamander-password`
- 策略组页面长按一个配置有 policy-path 的策略组时，可以直接进行策略组更新
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-12-29 [post 1411](https://t.me/SurgeTestFlight/1411)

#iOS #TestFlight 

Surge 5 5.101.0 (3618) is ready to test on iOS.

What to Test:

- 修正使用 AnyTLS 时可能出现的一些问题

Official Channel: @SurgeTestFlightFeed

## 2025-12-25 [post 1405](https://t.me/SurgeTestFlight/1405)

#iOS #TestFlight 

Surge 5 5.101.0 (3617) is ready to test on iOS.

What to Test:

- 细节问题优化

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1390](https://t.me/SurgeTestFlight/1390)

#iOS #TestFlight 

Surge 5 5.101.0 (3616) is ready to test on iOS.

What to Test:

- Bug fix

Official Channel: @SurgeTestFlightFeed

## 2025-12-12 [post 1387](https://t.me/SurgeTestFlight/1387)

#iOS #TestFlight 

Surge 5 5.101.0 (3615) is ready to test on iOS.

What to Test:

- AnyTLS 相关问题修正
- 修正 HTTPS 代理协议无法工作的问题
- 修正 iPad 下的一些界面问题

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1382](https://t.me/SurgeTestFlight/1382)

#iOS #TestFlight 

Surge 5 5.101.0 (3614) is ready to test on iOS.

What to Test:

- 修正使用 TUIC v5 时可能出现的崩溃

Official Channel: @SurgeTestFlightFeed

## 2025-12-11 [post 1381](https://t.me/SurgeTestFlight/1381)

#iOS #TestFlight 

Surge 5 5.101.0 (3613) is ready to test on iOS.

What to Test:

新的订阅功能：兼容代理协议 AnyTLS(v2)
- 已完全实现 AnyTLS 的 padding scheme，支持服务端动态更新
- 已完全实现 AnyTLS 的 reuse 机制，根据 AnyTLS spec 要求，reuse 默认开启，可以使用 reuse=false 关闭

Official Channel: @SurgeTestFlightFeed

## 2025-12-08 [post 1372](https://t.me/SurgeTestFlight/1372)

#iOS #TestFlight 

Surge 5 5.101.0 (3609) is ready to test on iOS.

What to Test:

5.16.3 RC1
- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-12-08 [post 1371](https://t.me/SurgeTestFlight/1371)

#iOS #TestFlight 

Surge 5 5.101.0 (3608) is ready to test on iOS.

What to Test:

- 重做了卡片页面的弹出菜单，以解决 26.2 系统下可能出现的一些问题

Official Channel: @SurgeTestFlightFeed

## 2025-12-07 [post 1369](https://t.me/SurgeTestFlight/1369)

#iOS #TestFlight 

Surge 5 5.101.0 (3607) is ready to test on iOS.

What to Test:

- 修正一处因 SS2022 服务端畸形数据导致的崩溃
- 优化企业授权管理机制，且改名为团队版本

Official Channel: @SurgeTestFlightFeed

## 2025-11-13 [post 1350](https://t.me/SurgeTestFlight/1350)

#iOS #TestFlight 

Surge 5 5.101.0 (3605) is ready to test on iOS.

What to Test:

- 优化策略组页面展开模式下的加载逻辑，避免极大量策略组情况下的卡顿
- 其他问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-11-08 [post 1346](https://t.me/SurgeTestFlight/1346)

#iOS #TestFlight 

Surge 5 5.101.0 (3604) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-11-08 [post 1344](https://t.me/SurgeTestFlight/1344)

#iOS #TestFlight 

Surge 5 5.101.0 (3603) is ready to test on iOS.

What to Test:

- 修正低版本 iPadOS 上崩溃的问题

Official Channel: @SurgeTestFlightFeed

## 2025-11-06 [post 1339](https://t.me/SurgeTestFlight/1339)

#iOS #TestFlight 

Surge 5 5.101.0 (3602) is ready to test on iOS.

What to Test:

- 修正 iPadOS 上一些 UI 问题
- 远程控制菜单页新增图标

Official Channel: @SurgeTestFlightFeed

## 2025-10-30 [post 1327](https://t.me/SurgeTestFlight/1327)

#iOS #TestFlight 

Surge 5 5.101.0 (3600) is ready to test on iOS.

What to Test:

- 修正特定故障的 Hysteria 2 节点会导致崩溃的问题
- 其他低概率崩溃问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-10-23 [post 1309](https://t.me/SurgeTestFlight/1309)

#iOS #TestFlight 

Surge 5 5.101.0 (3593) is ready to test on iOS.

What to Test:

- 修正一些低概率崩溃
- 优化特定情况下的突发内存占用

Official Channel: @SurgeTestFlightFeed

## 2025-10-20 [post 1294](https://t.me/SurgeTestFlight/1294)

#iOS #TestFlight 

Surge 5 5.101.0 (3588) is ready to test on iOS.

What to Test:

修正 HTTP 引擎在特定情况下时可能卡住的问题

5.16.2 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-10-10 [post 1277](https://t.me/SurgeTestFlight/1277)

#iOS #TestFlight 

Surge 5 5.101.0 (3584) is ready to test on iOS.

What to Test:

- 修正使用 Snell v3 承载 UDP 会导致崩溃的问题

Official Channel: @SurgeTestFlightFeed

## 2025-10-09 [post 1274](https://t.me/SurgeTestFlight/1274)

#iOS #TestFlight 

Surge 5 5.101.0 (3583) is ready to test on iOS.

What to Test:

修正 HTTP 引擎在处理连续请求的时候，可能卡主的问题

Official Channel: @SurgeTestFlightFeed

## 2025-10-04 [post 1271](https://t.me/SurgeTestFlight/1271)

#iOS #TestFlight 

Surge 5 5.101.0 (3582) is ready to test on iOS.

What to Test:

- 修正使用 TLS 类代理协议时，可能出现的内存泄露的问题

Official Channel: @SurgeTestFlightFeed

## 2025-09-30 [post 1266](https://t.me/SurgeTestFlight/1266)

#iOS #TestFlight 

Surge 5 5.101.0 (3578) is ready to test on iOS.

What to Test:

- 修正查看远程设备代理信息时，执行带宽测试实际是对本地 Surge 进行测试的问题
- 文案补全

5.16.1 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-09-29 [post 1265](https://t.me/SurgeTestFlight/1265)

#iOS #TestFlight 

Surge 5 5.101.0 (3577) is ready to test on iOS.

What to Test:

- 修正对代理测速时，实际是对 DIRECT 执行的测试

Official Channel: @SurgeTestFlightFeed

## 2025-09-29 [post 1263](https://t.me/SurgeTestFlight/1263)

#iOS #TestFlight 

Surge 5 5.101.0 (3576) is ready to test on iOS.

What to Test:

- 上个版本的外部 IP 探测和 NAT 类型探测功能，订阅功能名修改为「主动探测」，功能解锁时间不变
- 主动探测新增上传与下载带宽测试，可针对当前网络或者代理策略直接测试带宽
- 优化脚本编辑器执行页面

Official Channel: @SurgeTestFlightFeed

## 2025-09-17 [post 1243](https://t.me/SurgeTestFlight/1243)

#iOS #TestFlight 

Surge 5 5.101.0 (3575) is ready to test on iOS.

What to Test:

- 修正非 iOS 26 下卡片自定义页面背景问题
- 修正 Subnet Suspend 功能下，SSID 表达式可能无效的问题

Official Channel: @SurgeTestFlightFeed

## 2025-09-13 [post 1239](https://t.me/SurgeTestFlight/1239)

#iOS #TestFlight 

Surge 5 5.101.0 (3572) is ready to test on iOS.

What to Test:

- 细节优化与修正

5.16.0 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-09-12 [post 1238](https://t.me/SurgeTestFlight/1238)

#iOS #TestFlight 

Surge 5 5.101.0 (3571) is ready to test on iOS.

What to Test:

- 修正卡片自定义页面的问题
- Widget 全面适配 iOS 26 的各种风格选项

Official Channel: @SurgeTestFlightFeed

## 2025-09-12 [post 1237](https://t.me/SurgeTestFlight/1237)

#iOS #TestFlight 

Surge 5 5.101.0 (3570) is ready to test on iOS.

What to Test:

- 重做请求页过滤器系统，以适配 iOS 26
- 其他细节修正

Official Channel: @SurgeTestFlightFeed

## 2025-09-11 [post 1236](https://t.me/SurgeTestFlight/1236)

#iOS #TestFlight 

Surge 5 5.101.0 (3569) is ready to test on iOS.

What to Test:

- 全面细节优化
- 卡片页开始按钮新增长按菜单，作为 iOS 26 上的 tab bar 菜单替代

Official Channel: @SurgeTestFlightFeed

## 2025-09-10 [post 1234](https://t.me/SurgeTestFlight/1234)

#iOS #TestFlight 

Surge 5 5.101.0 (3568) is ready to test on iOS.

What to Test:

- 使用 iOS 26 SDK 编译，全面适配 iOS 26 UI。
原本我们打算借机重新设计 Surge iOS 的 UI，但是进度较慢，预计要到年末完成，因此目前先在当前 UI 上进行 iOS 26 的适配工作。
（图标尚未适配）

- 优化 HTTP 引擎的兼容性

Official Channel: @SurgeTestFlightFeed

## 2025-09-07 [post 1229](https://t.me/SurgeTestFlight/1229)

#iOS #TestFlight 

Surge 5 5.101.0 (3567) is ready to test on iOS.

What to Test:

- 外部 IP 展示新增 ASN/ASO 信息

Official Channel: @SurgeTestFlightFeed

## 2025-09-06 [post 1228](https://t.me/SurgeTestFlight/1228)

#iOS #TestFlight 

Surge 5 5.101.0 (3566) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-09-06 [post 1225](https://t.me/SurgeTestFlight/1225)

#iOS #TestFlight 

Surge 5 5.101.0 (3565) is ready to test on iOS.

What to Test:

- 完成代理的外部 IP 检查功能和 NAT 类型测试
- [Host] 段正式支持 IP 地址请求的映射（先前版本仅支持代理模式下的映射，现在同时支持直连情况下的映射）
- 修正 timeout 相关参数，写入配置时无法保留小数的问题

Official Channel: @SurgeTestFlightFeed

## 2025-09-05 [post 1221](https://t.me/SurgeTestFlight/1221)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.101.0 (3562) is ready to test on iOS.

What to Test:

新的订阅功能：外部 IP 与 NAT 类型查看
- 可在网络诊断页面查看当前网络的外部 IPv4 地址和 NAT 类型
- 该功能稍后将扩充至代理线路的外部 IPv4 地址和 NAT 类型查看

- 修正在开启状态下清除统计数据会导致日志持续报错的问题
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-08-15 [post 1215](https://t.me/SurgeTestFlight/1215)

#iOS #TestFlight 

Surge 5 5.101.0 (3561) is ready to test on iOS.

What to Test:

- 修正 [General] 段注释处理的一些问题

Official Channel: @SurgeTestFlightFeed

## 2025-08-12 [post 1208](https://t.me/SurgeTestFlight/1208)

#iOS #TestFlight 

Surge 5 5.101.0 (3557) is ready to test on iOS.

What to Test:

5.15.2 RC

Official Channel: @SurgeTestFlightFeed

## 2025-08-06 [post 1197](https://t.me/SurgeTestFlight/1197)

#iOS #TestFlight 

Surge 5 5.101.0 (3551) is ready to test on iOS.

What to Test:

- 修正通过 Ponte 使用 MITM 时，有可能卡住的问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1178](https://t.me/SurgeTestFlight/1178)

#iOS #TestFlight 

Surge 5 5.101.0 (3550) is ready to test on iOS.

What to Test:

- 修正 Ponte 连接时可能出现的问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-29 [post 1175](https://t.me/SurgeTestFlight/1175)

#iOS #TestFlight 

Surge 5 5.101.0 (3548) is ready to test on iOS.

What to Test:

核心改进
- 策略的 interface 参数现在可以对 DNS 查询也生效了，命中该策略的请求的 DNS 将使用该 interface 进行查询。（如果在规则匹配阶段就触发了 DNS，则不会使用特定 interface）
- 网络质量检测子系统重写，使用了更完备的检查逻辑，在网络不稳定时不再频繁触发通知。

Ponte 客户端改进
- 支持跨网段的内网连接，如多个 VLAN。
- 诊断工具在诊断模式下，将打印所有通道的响应结果。用于确认通道可用性。

Official Channel: @SurgeTestFlightFeed

## 2025-07-23 [post 1158](https://t.me/SurgeTestFlight/1158)

#iOS #TestFlight 

Surge 5 5.101.0 (3546) is ready to test on iOS.

What to Test:

- 修正特定 gQUIC 版本识别上的一些问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-23 [post 1156](https://t.me/SurgeTestFlight/1156)

#iOS #TestFlight 

Surge 5 5.101.0 (3545) is ready to test on iOS.

What to Test:

- 优化 QUIC 和 gQUIC 协议的识别，不再强制依赖 443 端口号
- Snell v5 QUIC Mode 支持 gQUIC 协议
- 其他细节优化

Official Channel: @SurgeTestFlightFeed

## 2025-07-21 [post 1142](https://t.me/SurgeTestFlight/1142)

#iOS #TestFlight 

Surge 5 5.101.0 (3542) is ready to test on iOS.

What to Test:

- 修正与新版本 hysteria 2 服务端的兼容性问题，导致大型 UDP 数据包无法正确转发

Official Channel: @SurgeTestFlightFeed

## 2025-07-19 [post 1135](https://t.me/SurgeTestFlight/1135)

#iOS #TestFlight 

Surge 5 5.101.0 (3541) is ready to test on iOS.

What to Test:

- 修正 Ponte 在纯 IPv6 数据网络下出现的问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-19 [post 1134](https://t.me/SurgeTestFlight/1134)

#iOS #TestFlight 

Surge 5 5.101.0 (3539) is ready to test on iOS.

What to Test:

- 修正 Ponte 在开启了 IPv6 通道时，如果在没有 IPv6 的网络环境进行连接，会因为无 IPv6 立刻失败而不尝试 v4 通道的问题
- 修正数据网络的 IPv6 地址未能正确显示的问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1113](https://t.me/SurgeTestFlight/1113)

#iOS #TestFlight 

Surge 5 5.101.0 (3535) is ready to test on iOS.

What to Test:

- 调整了 DIRECT 统计合并的策略，现在带有 interface 或 hybrid 参数的别名不再会被合并计算

5.15.1 RC3

Official Channel: @SurgeTestFlightFeed

## 2025-07-15 [post 1111](https://t.me/SurgeTestFlight/1111)

#iOS #TestFlight 

Surge 5 5.101.0 (3534) is ready to test on iOS.

What to Test:

- 所以 DIRECT 的别名，现在在统计时均记为 DIRECT 的流量
- 其他细节修正

5.15.1 RC2

Official Channel: @SurgeTestFlightFeed

## 2025-07-14 [post 1108](https://t.me/SurgeTestFlight/1108)

#iOS #TestFlight 

Surge 5 5.101.0 (3533) is ready to test on iOS.

What to Test:

- 细节问题修正

5.15.1 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-07-14 [post 1104](https://t.me/SurgeTestFlight/1104)

#iOS #TestFlight 

Surge 5 5.101.0 (3532) is ready to test on iOS.

What to Test:

- 修正最近版本出现的 HTTP 引擎下性能下降的问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-12 [post 1092](https://t.me/SurgeTestFlight/1092)

#iOS #TestFlight 

Surge 5 5.101.0 (3528) is ready to test on iOS.

What to Test:

- 恢复了对 Snell v2/v3 的支持

Official Channel: @SurgeTestFlightFeed

## 2025-07-10 [post 1079](https://t.me/SurgeTestFlight/1079)

#iOS #TestFlight 

Surge 5 5.101.0 (3522) is ready to test on iOS.

What to Test:

5.15.0 RC2
- 修正纯 IPv6 数据网络下 subnet 表达式的一些问题

Official Channel: @SurgeTestFlightFeed

## 2025-07-09 [post 1076](https://t.me/SurgeTestFlight/1076)

#iOS #TestFlight 

Surge 5 5.101.0 (3519) is ready to test on iOS.

What to Test:

5.15.0 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-07-03 [post 1019](https://t.me/SurgeTestFlight/1019)

#iOS #TestFlight 

Surge 5 5.100.0 (3516) is ready to test on iOS.

What to Test:

 - 修正 iOS 26 下无法触发 LAN 访问权限的问题
 - 修正 Snell 在 Smart Group 中无法按预期使用 reuse 的问题
 - 修正 Vmess 在 Smart Group 中永远无法被优先使用的问题
 - 其他问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-07-02 [post 1006](https://t.me/SurgeTestFlight/1006)

#iOS #TestFlight 

Surge 5 5.100.0 (3515) is ready to test on iOS.

What to Test:

- 修正 Snell 的 reuse 机制部分情况下未能正确生效的问题
- 其他问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 984](https://t.me/SurgeTestFlight/984)

#iOS #TestFlight 

Surge 5 5.100.0 (3514) is ready to test on iOS.

What to Test:

- 修正 auto-suspend 功能无法工作的问题
- 由于还在使用 Snell v2/v3 的用户量极低，新版本中已经移除了支持。同时去除了 v4 版本的订阅功能限制，以方便未订阅用户迁移

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 981](https://t.me/SurgeTestFlight/981)

#iOS #TestFlight 

Surge 5 5.100.0 (3513) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 980](https://t.me/SurgeTestFlight/980)

#iOS #TestFlight 

Surge 5 5.100.0 (3512) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 979](https://t.me/SurgeTestFlight/979)

#iOS #TestFlight 

Surge 5 5.100.0 (3509) is ready to test on iOS.

What to Test:

- 修正几处 UI 崩溃与其他问题

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 978](https://t.me/SurgeTestFlight/978)

#iOS #TestFlight 

Surge 5 5.100.0 (3508) is ready to test on iOS.

What to Test:

使用 Surge v6 版本核心编译，同步 Surge Mac 6.0 新功能，包含：

- Surge VIF Engine 性能大幅提升（免费更新）
- Surge Smart Group 改进（已解锁用户免费更新）
- Surge Ponte 2.0 - Multiple Channels（需配合 Surge Mac 6.0 使用）
- Snell v5（需要功能订阅）

细节请参见 Surge Mac 6.0 测试版更新日志：https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note

Official Channel: @SurgeTestFlightFeed

## 2025-06-30 [post 976](https://t.me/SurgeTestFlight/976)

#iOS #TestFlight 

Surge 5 5.100.0 (3507) is ready to test on iOS.

What to Test:

使用 Surge v6 版本核心编译，同步 Surge Mac 6.0 新功能，包含：

- Surge VIF Engine 性能大幅提升（免费更新）
- Surge Smart Group 改进（已解锁用户免费更新）
- Surge Ponte 2.0 - Multiple Channels（需配合 Surge Mac 6.0 使用）
- Snell v5（需要功能订阅）

细节请参见 Surge Mac 6.0 测试版更新日志：https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note https://kb.nssurge.com/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note

Official Channel: @SurgeTestFlightFeed

## 2025-06-10 [post 958](https://t.me/SurgeTestFlight/958)

#iOS #TestFlight 

Surge 5 5.100.0 (3502) is ready to test on iOS.

What to Test:

该版本为 iOS 26 UI 体验版，不建议其他 iOS 版本用户使用。

仅初步适配了 iOS 26 UI 风格，还存在诸多问题，仅供体验，无需进行 bug 回报。

Official Channel: @SurgeTestFlightFeed

## 2025-06-10 [post 954](https://t.me/SurgeTestFlight/954)

#iOS #TestFlight 

Surge 5 5.100.0 (3501) is ready to test on iOS.

What to Test:

- 修正 ShadowTLS/AdaptiveTLSFingerprint 在 iOS 26 beta 上崩溃的问题

Official Channel: @SurgeTestFlightFeed

## 2025-05-09 [post 947](https://t.me/SurgeTestFlight/947)

#iOS #TestFlight 

Surge 5 5.100.0 (3495) is ready to test on iOS.

What to Test:

- Bug fixes

5.14.6 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-05-09 [post 946](https://t.me/SurgeTestFlight/946)

#iOS #TestFlight 

Surge 5 5.100.0 (3491) is ready to test on iOS.

What to Test:

- 流量统计新增导出功能
- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-05-08 [post 944](https://t.me/SurgeTestFlight/944)

#iOS #TestFlight 

Surge 5 5.100.0 (3490) is ready to test on iOS.

What to Test:

- 重构流量统计功能，现在即使长期未进主程序，也不会在进入流量统计页面时需要长时间等待了
- 开始按钮页点击卡片可进入流量统计
- 其他细节优化

Official Channel: @SurgeTestFlightFeed

## 2025-05-02 [post 938](https://t.me/SurgeTestFlight/938)

#iOS #TestFlight 

Surge 5 5.100.0 (3486) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-05-02 [post 937](https://t.me/SurgeTestFlight/937)

#iOS #TestFlight 

Surge 5 5.100.0 (3485) is ready to test on iOS.

What to Test:

- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2025-04-23 [post 928](https://t.me/SurgeTestFlight/928)

#iOS #TestFlight 

Surge 5 5.100.0 (3484) is ready to test on iOS.

What to Test:

- 为 Surge 的托管配置、外部资源和模块 HTTP 请求，新增了 X-Surge-Unlocked-Features 字段，用于服务器判定 Surge 已解锁的功能以区分返回结果
- 调整了 QUIC 类协议的流控参数，优化在特定情况下的内存占用表现
- 修正了 WireGuard 无法自动检测 DNS 解析结果变化的问题
- 修正列表模式下 subnet 组无法进行测试的问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-19 [post 925](https://t.me/SurgeTestFlight/925)

#iOS #TestFlight 

Surge 5 5.100.0 (3482) is ready to test on iOS.

What to Test:

- 修正 JSC 引擎脚本执行 HTTP Body 操作会失败的问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-17 [post 923](https://t.me/SurgeTestFlight/923)

#iOS #TestFlight 

Surge 5 5.100.0 (3481) is ready to test on iOS.

What to Test:

- 支持 gQUIC 的 SNI 提取

Official Channel: @SurgeTestFlightFeed

## 2025-04-17 [post 921](https://t.me/SurgeTestFlight/921)

#iOS #TestFlight 

Surge 5 5.100.0 (3480) is ready to test on iOS.

What to Test:

- 再次优化了 HTTP 脚本的极限内存占用，目前最大可处理约 20MB 的 HTTP body
- 修正了与部分脚本的兼容性问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-16 [post 920](https://t.me/SurgeTestFlight/920)

#iOS #TestFlight 

Surge 5 5.100.0 (3477) is ready to test on iOS.

What to Test:

- 修正 HTTP 脚本 binary 模式下的兼容性问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-16 [post 918](https://t.me/SurgeTestFlight/918)

#iOS #TestFlight 

Surge 5 5.100.0 (3476) is ready to test on iOS.

What to Test:

- 进一步优化内存占用
- 修正与部分不标准的脚本的兼容问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-16 [post 917](https://t.me/SurgeTestFlight/917)

#iOS #TestFlight 

Surge 5 5.100.0 (3475) is ready to test on iOS.

What to Test:

- 重写 HTTP 脚本相关实现，现在在处理大型 Body 时性能更好且内存占用更低

Official Channel: @SurgeTestFlightFeed

## 2025-04-10 [post 915](https://t.me/SurgeTestFlight/915)

#iOS #TestFlight 

Surge 5 5.100.0 (3474) is ready to test on iOS.

What to Test:

- 优化请求查看器中的文本与 JSON 浏览器，支持大文件与代码高亮

Official Channel: @SurgeTestFlightFeed

## 2025-04-08 [post 913](https://t.me/SurgeTestFlight/913)

#iOS #TestFlight 

Surge 5 5.100.0 (3473) is ready to test on iOS.

What to Test:

- 修正 WireGuard 在 iOS 18.4 下特定情况可能崩溃的问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-03 [post 911](https://t.me/SurgeTestFlight/911)

#iOS #TestFlight 

Surge 5 5.100.0 (3472) is ready to test on iOS.

What to Test:

- 修正 block-quic 可能不能正确生效的问题

Official Channel: @SurgeTestFlightFeed

## 2025-04-03 [post 910](https://t.me/SurgeTestFlight/910)

#iOS #TestFlight 

Surge 5 5.100.0 (3469) is ready to test on iOS.

What to Test:

新增 [General] 参数 `block-quic`，该参数用于全局覆盖是否阻止 QUIC 流量的行为，可设置为

- per-policy：由策略的 block-quic 参数决定，默认值，即当前版本的行为。
- all-proxy：覆盖代理策略的 block-quic 参数，全部阻止
- all：覆盖所有策略的 block-quic 参数，全部阻止，包括 DIRECT 策略
- always-allow：覆盖代理策略的 block-quic 参数，全部允许

Official Channel: @SurgeTestFlightFeed

## 2025-03-28 [post 904](https://t.me/SurgeTestFlight/904)

#iOS #TestFlight 

Surge 5 5.100.0 (3466) is ready to test on iOS.

What to Test:

- 修正搜索请求时会崩溃的问题
- 修正搜索高亮只会高亮第一个命中结果的问题
- 微调 Header 显示样式

Official Channel: @SurgeTestFlightFeed

## 2025-03-27 [post 902](https://t.me/SurgeTestFlight/902)

#iOS #TestFlight 

Surge 5 5.100.0 (3465) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-03-27 [post 901](https://t.me/SurgeTestFlight/901)

#iOS #TestFlight 

Surge 5 5.100.0 (3464) is ready to test on iOS.

What to Test:

- 调整了同时进行 AAAA 解析时遇到 CNAME 响应的处理逻辑
- 优化了 HTTP header 的显示
- 对最新的 Mac 设备进行了 Ponte 图标映射

Official Channel: @SurgeTestFlightFeed

## 2025-03-25 [post 898](https://t.me/SurgeTestFlight/898)

#iOS #TestFlight 

Surge 5 5.100.0 (3456) is ready to test on iOS.

What to Test:

5.14.4 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-03-17 [post 892](https://t.me/SurgeTestFlight/892)

#iOS #TestFlight 

Surge 5 5.100.0 (3452) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-03-13 [post 890](https://t.me/SurgeTestFlight/890)

#iOS #TestFlight 

Surge 5 5.100.0 (3451) is ready to test on iOS.

What to Test:

- 修正条件配置的一些相关问题
- 热点代理不再需要重启 Surge 后生效了

Official Channel: @SurgeTestFlightFeed

## 2025-03-06 [post 888](https://t.me/SurgeTestFlight/888)

#iOS #TestFlight 

Surge 5 5.100.0 (3450) is ready to test on iOS.

What to Test:

- 新增 Shortcuts 操作，可强制更新所有外部资源

Official Channel: @SurgeTestFlightFeed

## 2025-02-27 [post 883](https://t.me/SurgeTestFlight/883)

#iOS #TestFlight 

Surge 5 5.100.0 (3449) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 879](https://t.me/SurgeTestFlight/879)

#iOS #TestFlight 

Surge 5 5.100.0 (3448) is ready to test on iOS.

What to Test:

-  修正加密 DNS 的一些兼容问题

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 875](https://t.me/SurgeTestFlight/875)

#iOS #TestFlight 

Surge 5 5.100.0 (3447) is ready to test on iOS.

What to Test:

- 修改 DNS over TLS 配置前缀为 tls://
- 修正一处崩溃

Official Channel: @SurgeTestFlightFeed

## 2025-02-26 [post 873](https://t.me/SurgeTestFlight/873)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3446) is ready to test on iOS.

What to Test:

- 新的订阅功能：DNS over TLS
配置样例 dot://223.5.5.5

Official Channel: @SurgeTestFlightFeed

## 2025-02-25 [post 868](https://t.me/SurgeTestFlight/868)

#iOS #TestFlight 

Surge 5 5.100.0 (3445) is ready to test on iOS.

What to Test:

- 修正当 DoQ 使用含大写字母的域名时会无法使用的问题

Official Channel: @SurgeTestFlightFeed

## 2025-02-24 [post 867](https://t.me/SurgeTestFlight/867)

#iOS #TestFlight 

Surge 5 5.100.0 (3444) is ready to test on iOS.

What to Test:

- 临时规则页面可以调整已存在规则的策略了
- 优化在纯 IPv6 网络下 NAT64 的行为

Official Channel: @SurgeTestFlightFeed

## 2025-02-21 [post 864](https://t.me/SurgeTestFlight/864)

#iOS #TestFlight 

Surge 5 5.100.0 (3443) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-02-20 [post 860](https://t.me/SurgeTestFlight/860)

#iOS #TestFlight 

Surge 5 5.100.0 (3439) is ready to test on iOS.

What to Test:

5.14.4 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-02-19 [post 859](https://t.me/SurgeTestFlight/859)

#iOS #TestFlight 

Surge 5 5.100.0 (3438) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-02-19 [post 857](https://t.me/SurgeTestFlight/857)

#iOS #TestFlight 

Surge 5 5.100.0 (3437) is ready to test on iOS.

What to Test:

- 优化正则匹配的性能表现
- 修正在触发脚本时，HTTP Request Body 有可能未能被正确捕获保存的问题

Official Channel: @SurgeTestFlightFeed

## 2025-02-18 [post 853](https://t.me/SurgeTestFlight/853)

#iOS #TestFlight 

Surge 5 5.100.0 (3435) is ready to test on iOS.

What to Test:

- 现在在开启 HTTP 捕获开关时，将强制打断所有活跃连接，以确保不会因为已存在的长链接导致错过请求。
- 优化与部分 QUIC 客户端的兼容性，如飞书。
- 修正当使用脚本或其他机制修改请求 HTTP 后，统计中的下载数据计量有误的问题。
- 调整了关于 QUIC 转发时处理逻辑的优先级，现在对于一个不支持 UDP 转发的代理策略，将优先考虑 QUIC Block，再考虑回退至 DIRECT 或 REJECT。

Official Channel: @SurgeTestFlightFeed

## 2025-01-19 [post 841](https://t.me/SurgeTestFlight/841)

#iOS #TestFlight 

Surge 5 5.100.0 (3429) is ready to test on iOS.

What to Test:

5.14.3 RC2

Official Channel: @SurgeTestFlightFeed

## 2025-01-17 [post 839](https://t.me/SurgeTestFlight/839)

#iOS #TestFlight 

Surge 5 5.100.0 (3428) is ready to test on iOS.

What to Test:

5.14.3 RC1

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 835](https://t.me/SurgeTestFlight/835)

#iOS #TestFlight 

Surge 5 5.100.0 (3427) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 832](https://t.me/SurgeTestFlight/832)

#iOS #TestFlight 

Surge 5 5.100.0 (3425) is ready to test on iOS.

What to Test:

[Host] 段支持使用 DOMAIN-SET 和 RULE-SET 进行配置以提高匹配效率。

用例：
[Host]
DOMAIN-SET:https://example.com/domains.txt https://example.com/domains.txt = server:https://223.5.5.5/dns-query https://223.5.5.5/dns-query
RULE-SET:https://example.com/rules.txt https://example.com/rules.txt = server:https://223.5.5.5/dns-query https://223.5.5.5/dns-query

该功能仅为一些特别的需求所设计，绝大部分用户不需要考虑 DNS 区分解析，详见：https://kb.nssurge.com/surge-knowledge-base/zh/technotes/dns https://kb.nssurge.com/surge-knowledge-base/zh/technotes/dns

Official Channel: @SurgeTestFlightFeed

## 2025-01-16 [post 828](https://t.me/SurgeTestFlight/828)

#iOS #TestFlight 

Surge 5 5.100.0 (3423) is ready to test on iOS.

What to Test:

配置行尾注释 #!REQUIREMENT 升级
- 现在提供 #!IOS-ONLY, #!MACOS-ONLY, #!TVOS-ONLY 三个简单写法
- 被该行尾注释禁用的内容，可以正常在 UI 显示和编辑了，在不满足条件时会显示为禁用状态，若开启将自动移除限制

用例：
DOMAIN,reject.com http://reject.com/,REJECT #!MACOS-ONLY

Official Channel: @SurgeTestFlightFeed

## 2025-01-14 [post 824](https://t.me/SurgeTestFlight/824)

#iOS #TestFlight 

Surge 5 5.100.0 (3421) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2025-01-09 [post 821](https://t.me/SurgeTestFlight/821)

#iOS #TestFlight 

Surge 5 5.100.0 (3420) is ready to test on iOS.

What to Test:

- 细节优化

Official Channel: @SurgeTestFlightFeed

## 2024-12-31 [post 808](https://t.me/SurgeTestFlight/808)

#iOS #TestFlight 

Surge 5 5.100.0 (3417) is ready to test on iOS.

What to Test:

- 优化 Smart 组的使用标签生成逻辑，现在会更快的生成标签，且在策略组页面会自动更新数据，无需手动切换页面刷新

Official Channel: @SurgeTestFlightFeed

## 2024-12-30 [post 806](https://t.me/SurgeTestFlight/806)

#iOS #TestFlight 

Surge 5 5.100.0 (3416) is ready to test on iOS.

What to Test:

- 细节优化
- 同步 Mac 版本 icmp-forwarding 参数

Official Channel: @SurgeTestFlightFeed

## 2024-12-23 [post 798](https://t.me/SurgeTestFlight/798)

#iOS #TestFlight 

Surge 5 5.100.0 (3415) is ready to test on iOS.

What to Test:

- 细节问题修正
- 优化通过 Snell V4 使用 Telegram 时的表现

Official Channel: @SurgeTestFlightFeed

## 2024-12-21 [post 791](https://t.me/SurgeTestFlight/791)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3414) is ready to test on iOS.

What to Test:

新的订阅功能：端口转发 Port Forwarding
配置样例
[Port Forwarding]
0.0.0.0:6841 http://0.0.0.0:6841/ localhost:3306 policy=SQL-Server-Proxy

第一个参数为本地监听地址与端口（iOS 仅支持 127.0.0.1 http://127.0.0.1/ 或 0.0.0.0），第二个参数为转发目标，policy 参数选填，如果不填的话将使用标准代理匹配决定策略。该功能暂无 UI 配置。

该功能常见于使用 SSH 连接服务器 MariaDB 等开发调试场景。

Official Channel: @SurgeTestFlightFeed

## 2024-12-17 [post 782](https://t.me/SurgeTestFlight/782)

#iOS #TestFlight 

Surge 5 5.100.0 (3413) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-12-16 [post 780](https://t.me/SurgeTestFlight/780)

#iOS #TestFlight 

Surge 5 5.100.0 (3412) is ready to test on iOS.

What to Test:

- DoH 在服务端无响应时，会更快的重建连接
- Smart 策略组的显示选项，现在会收到优先级参数的影响了（显示的选中选项为测试结果最低的策略，并非实际会被使用的策略，因此在配置了优先级参数时可能产生误导）
- 细节修正

Official Channel: @SurgeTestFlightFeed

## 2024-12-13 [post 771](https://t.me/SurgeTestFlight/771)

#iOS #TestFlight 

Surge 5 5.100.0 (3411) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-12-12 [post 767](https://t.me/SurgeTestFlight/767)

#iOS #TestFlight 

Surge 5 5.100.0 (3410) is ready to test on iOS.

What to Test:

- 修正同时使用 ShadowTLS 和 underlying-proxy 会崩溃的问题
- 修正模块无法自动更新的问题

Official Channel: @SurgeTestFlightFeed

## 2024-12-12 [post 764](https://t.me/SurgeTestFlight/764)

#iOS #TestFlight 

Surge 5 5.100.0 (3409) is ready to test on iOS.

What to Test:

优化了使用 Smart Group 作为 underlying-proxy （代理链）的表现，在先前的版本中由于架构问题，使用 Smart Group 作为一个代理策略的 underlying-proxy 时，Smart Group 无法发挥全部特性（如动态备用策略切换）。新版本中已经完全解决了这些问题。

Official Channel: @SurgeTestFlightFeed

## 2024-12-08 [post 757](https://t.me/SurgeTestFlight/757)

#iOS #TestFlight 

Surge 5 5.100.0 (3404) is ready to test on iOS.

What to Test:

5.14.2 RC2

Official Channel: @SurgeTestFlightFeed

## 2024-12-06 [post 752](https://t.me/SurgeTestFlight/752)

#iOS #TestFlight 

Surge 5 5.100.0 (3399) is ready to test on iOS.

What to Test:

- 使用 iOS 18.2 SDK 编译
- 细节问题修正

5.14.2 RC

Official Channel: @SurgeTestFlightFeed

## 2024-12-05 [post 749](https://t.me/SurgeTestFlight/749)

#iOS #TestFlight 

Surge 5 5.100.0 (3397) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-12-04 [post 745](https://t.me/SurgeTestFlight/745)

#iOS #TestFlight 

Surge 5 5.100.0 (3396) is ready to test on iOS.

What to Test:

- 修正文本编辑器和日志查看器中，使用搜索功能可能会卡主的问题

Official Channel: @SurgeTestFlightFeed

## 2024-12-03 [post 743](https://t.me/SurgeTestFlight/743)

#iOS #TestFlight 

Surge 5 5.100.0 (3395) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-12-02 [post 742](https://t.me/SurgeTestFlight/742)

#iOS #TestFlight 

Surge 5 5.100.0 (3394) is ready to test on iOS.

What to Test:

- 细节问题修正与优化

Official Channel: @SurgeTestFlightFeed

## 2024-11-26 [post 736](https://t.me/SurgeTestFlight/736)

#iOS #TestFlight 

Surge 5 5.100.0 (3393) is ready to test on iOS.

What to Test:

- 修正几个低概率崩溃和内存泄露
- 增加了更多在接近内存限制时的内存占用保护

Official Channel: @SurgeTestFlightFeed

## 2024-11-23 [post 732](https://t.me/SurgeTestFlight/732)

#iOS #TestFlight 

Surge 5 5.100.0 (3392) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-11-21 [post 727](https://t.me/SurgeTestFlight/727)

#iOS #TestFlight 

Surge 5 5.100.0 (3391) is ready to test on iOS.

What to Test:

- 修正数个低概率内存泄露

Official Channel: @SurgeTestFlightFeed

## 2024-11-07 [post 645](https://t.me/SurgeTestFlight/645)

#iOS #TestFlight 

Surge 5 5.100.0 (3373) is ready to test on iOS.

What to Test:

- 修正 Ponte 无法转发 UDP 流量的问题
- 优化在飞行模式下（完全无网）的处理

5.14.1 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-11-05 [post 641](https://t.me/SurgeTestFlight/641)

#iOS #TestFlight 

Surge 5 5.100.0 (3372) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-11-04 [post 633](https://t.me/SurgeTestFlight/633)

#iOS #TestFlight 

Surge 5 5.100.0 (3370) is ready to test on iOS.

What to Test:

- 脚本编辑页面支持传入 $argument
- 在脚本列表页面执行脚本也会传入 $argument 的内容了
- 脚本的 $trigger 参数新增 "editor" 和 "http-api" 两个来源
- 修正 iOS 16 下 WireGuard 可能无法使用的问题
- 修正部分代理协议的流量统计中，未计算上传的 UDP 流量的问题

Official Channel: @SurgeTestFlightFeed

## 2024-10-31 [post 628](https://t.me/SurgeTestFlight/628)

#iOS #TestFlight 

Surge 5 5.100.0 (3366) is ready to test on iOS.

What to Test:

5.14.0 RC2

- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-10-31 [post 623](https://t.me/SurgeTestFlight/623)

#iOS #TestFlight 

Surge 5 5.100.0 (3364) is ready to test on iOS.

What to Test:

5.14.0 RC1
- 细节修正与文案补全

Official Channel: @SurgeTestFlightFeed

## 2024-10-29 [post 616](https://t.me/SurgeTestFlight/616)

#iOS #TestFlight 

Surge 5 5.100.0 (3362) is ready to test on iOS.

What to Test:

- 修正在 iOS 15 下 WireGuard 无法使用的问题
- 其他问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 613](https://t.me/SurgeTestFlight/613)

#iOS #TestFlight 

Surge 5 5.100.0 (3359) is ready to test on iOS.

What to Test:

- 修正通过 Shortcuts 修改策略组设置，如果并发执行多个修改有可能导致 Surge 开关状态重置的问题
- 修正当存在名为 error 的策略组时，可能导致一些功能出现异常的问题
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 610](https://t.me/SurgeTestFlight/610)

#iOS #TestFlight 

Surge 5 5.100.0 (3358) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-10-28 [post 607](https://t.me/SurgeTestFlight/607)

#iOS #TestFlight 

Surge 5 5.100.0 (3357) is ready to test on iOS.

What to Test:

- 修改 HTTP 脚本的终止逻辑，如果需要打断请求，应使用 $done({abort: true})，除此之外的失败将对请求不做修改而不会终止
- 修正 Body Rewrite 规则的处理逻辑，如果遇到非 UTF-8/非 JSON 请求，行为修改为不做修改而非失败
- 优化 QUIC 流控，降低在上传测速时出现的内存占用

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 604](https://t.me/SurgeTestFlight/604)

#iOS #TestFlight 

Surge 5 5.100.0 (3356) is ready to test on iOS.

What to Test:

- UDP 整体架构进行重构，UDP 相关功能可能出现问题，如有遇到请回报。
- shadowsocks 协议支持配置 udp-port 参数，用于单独指定 UDP 模式的服务端端口号，可在使用 ShadowTLS 时使用原端口号。
- 修正在进行大吞吐量 UDP 测试时，测试结果可能出现的异常（如 iperf UDP 模式）

Official Channel: @SurgeTestFlightFeed

## 2024-10-27 [post 595](https://t.me/SurgeTestFlight/595)

#iOS #TestFlight 

Surge 5 5.100.0 (3355) is ready to test on iOS.

What to Test:

根据一些用户的回报，我们发现在支持 hysteria2 的端口跳跃时，对 QUIC 在网络切换时进行的优化，可能会在网络切换时触发系统 Bug，导致 Surge iOS 有概率在切网后所有的连接均超时。（系统路由表紊乱）
该版本中移除了该优化，该问题可能影响所有使用 QUIC 类代理协议的用户，同时包含 DoQ 和 DoH3，请有遇到这类问题的用户测试确认问题是否改善。

Official Channel: @SurgeTestFlightFeed

## 2024-10-25 [post 589](https://t.me/SurgeTestFlight/589)

#iOS #TestFlight 

Surge 5 5.100.0 (3354) is ready to test on iOS.

What to Test:

- 增加 JQ Body Rewrite 的 UI 配置支持
- 其他细节优化

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 587](https://t.me/SurgeTestFlight/587)

#iOS #TestFlight 

Surge 5 5.100.0 (3353) is ready to test on iOS.

What to Test:

- 细节修正与调整

Official Channel: @SurgeTestFlightFeed

## 2024-10-24 [post 583](https://t.me/SurgeTestFlight/583)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3352) is ready to test on iOS.

What to Test:

新的订阅功能
Body Rewrite 支持使用 JQ 表达式对 JSON 进行操作

http-response-jq ^http://httpbingo.org/anything http://httpbingo.org/anything '.headers |= with_entries(select(.key | test("^X-") | not))'

JQ 表达式说明详见：https://jqlang.github.io/jq/ https://jqlang.github.io/jq/

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 578](https://t.me/SurgeTestFlight/578)

#iOS #TestFlight 

Surge 5 5.100.0 (3351) is ready to test on iOS.

What to Test:

Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 576](https://t.me/SurgeTestFlight/576)

#iOS #TestFlight 

Surge 5 5.100.0 (3350) is ready to test on iOS.

What to Test:

- 规则集和逻辑规则 UI 支持配置 pre-matching
- FINAL 规则的 dns-failed 支持使用 UI 配置
- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-10-23 [post 571](https://t.me/SurgeTestFlight/571)

#iOS #TestFlight 

Surge 5 5.100.0 (3349) is ready to test on iOS.

What to Test:

- URL-REGEX 规则支持 extended-matching 标记
- 修改数据网络的切换提示为通讯技术而非 IP
- 支持在 UI 上配置 pre-matching 标记了
- pre-matching 的实现细节优化
- 其他细节调整

Official Channel: @SurgeTestFlightFeed

## 2024-10-20 [post 563](https://t.me/SurgeTestFlight/563)

#iOS #TestFlight 

Surge 5 5.100.0 (3348) is ready to test on iOS.

What to Test:

- 增加 pre-matching 标记规则的校验，在不支持的规则上配置该标记将直接产生配置错误。(请注意 PROTOCOL 语句不可用，逻辑规则的子规则也会被校验，但是 RULE-SET 的子规则若不支持仅会不生效而不会报错)
- 对 TCP RST 拒绝方式增加了全局防御，当 3 秒内触发 100 次后，将临时暂停以避免应用死循环导致 CPU 异常，同时输出日志
-  pre-matching 的请求日志，由每 30 分钟一条，下调至 5 分钟
- 为 iOS 18.1 下，Poor Network Quality 无法被从通知中心自动消除的问题加入了一个 workaround

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 560](https://t.me/SurgeTestFlight/560)

#iOS #TestFlight 

Surge 5 5.100.0 (3347) is ready to test on iOS.

What to Test:

REJECT 规则相关优化，详见频道说明

Official Channel: @SurgeTestFlightFeed

## 2024-10-19 [post 552](https://t.me/SurgeTestFlight/552)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3345) is ready to test on iOS.

What to Test:

新的订阅功能 Pre-matching

用于描述使用 REJECT 策略的规则，如 

[Rule]
DOMAIN,ad.com http://ad.com/,REJECT,pre-matching

被标记了 pre-matching 的规则，将在正常的规则匹配流程前就提前生效，因此该规则相当于拥有最高优先级。

该功能的意义是，由于 Surge 的规则系统可判断的内容非常多，所以规则判定需要在收到首个 TCP 数据包后才可以进行，对于应对风暴请求或者去广告需求，产生了过多不必要的开销。

所有被标记了 pre-matching 的规则将会被提取出来进行优先匹配，在 DNS 解析与 TCP SYN 阶段就执行判断。若 DNS 域名命中，则直接返回 NXDOMAIN，若 TCP SYN 阶段命中，将直接产生 ICMP REFUSED 响应，大量请求时升级至丢包，UDP 同样处理。

同时，对于每条规则，每 30 分钟仅会在最近请求列表中出现一次，避免因为大量请求刷屏。

可以使用 pre-matching 标记的规则类型有：

- DOMAIN 类型：DOMAIN,DOMAIN-SUFFIX,DOMAIN-KEYWORD,DOMAIN-SET,DOMAIN-WILDCARD。
- IP 类型：IP-CIDR,IP-CIDR6,GEOIP,IP-ASN。
- 逻辑规则：AND,OR,NOT
- 其他：SUBNET,DEST-PORT,SRC-PORT,SRC-IP

RULSET 也可以使用，但是其内容同样受到上述限制。

举例来说，对于最近米家 App 的疯狂请求，就可以靠配置

[Rule]
DEST-PORT,5222,REJECT,pre-matching

在低开销的情况下进行屏蔽。

注：未续订的情况下，该标记不会影响 Surge 开启，只是会无法生效，避免造成困扰。

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 544](https://t.me/SurgeTestFlight/544)

#iOS #TestFlight 

Surge 5 5.100.0 (3344) is ready to test on iOS.

What to Test:

- 修正 ipv6-vif-route-mode 参数无法正确生效的问题
- 在 tvOS 设备移除后，不再尝试进行自动配置部署

Official Channel: @SurgeTestFlightFeed

## 2024-10-18 [post 539](https://t.me/SurgeTestFlight/539)

#iOS #TestFlight 

Surge 5 5.100.0 (3343) is ready to test on iOS.

What to Test:

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

Official Channel: @SurgeTestFlightFeed

## 2024-10-17 [post 532](https://t.me/SurgeTestFlight/532)

#iOS #TestFlight 

Surge 5 5.100.0 (3341) is ready to test on iOS.

What to Test:

- 修正小组件显示的状态有时可能不正确的问题

Official Channel: @SurgeTestFlightFeed

## 2024-10-16 [post 529](https://t.me/SurgeTestFlight/529)

#iOS #TestFlight 

Surge 5 5.100.0 (3340) is ready to test on iOS.

What to Test:

- 新增 HTTP Capture 的控制中心开关
- 支持使用 Ponte 策略作为 underlying-proxy

Official Channel: @SurgeTestFlightFeed

## 2024-10-16 [post 525](https://t.me/SurgeTestFlight/525)

#iOS #TestFlight 

Surge 5 5.100.0 (3339) is ready to test on iOS.

What to Test:

- 策略组列表视图支持配置自定义图标
- 修正带行尾注释的 DNS Mapping 项目无法在 UI 显示的问题
- 在全局模式下，若原选中策略不存在，将回退至第一个代理，而非 DIRECT

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 523](https://t.me/SurgeTestFlight/523)

#iOS #TestFlight 

Surge 5 5.100.0 (3337) is ready to test on iOS.

What to Test:

- 修正 SS 2022 UDP 转发时出现的问题

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 521](https://t.me/SurgeTestFlight/521)

#iOS #TestFlight 

Surge 5 5.100.0 (3336) is ready to test on iOS.

What to Test:

修改  SIP023 Identity 参数的配置方式为在 password 中使用 : 分隔，不再使用 identity 字段，与其他客户端相一致

Official Channel: @SurgeTestFlightFeed

## 2024-10-15 [post 517](https://t.me/SurgeTestFlight/517)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3335) is ready to test on iOS.

What to Test:

新的订阅功能：Shadowsocks 2022 加密协议支持
- 支持 2022-blake3-aes-256-gcm 与 2022-blake3-aes-128-gcm 两种模式
- UDP 转发同样需要配置 udp-relay=true
- 可配置 identity 参数以使用 SIP023 Shadowsocks 2022 Extensible Identity Headers，目前仅支持配置一层

Official Channel: @SurgeTestFlightFeed

## 2024-10-13 [post 511](https://t.me/SurgeTestFlight/511)

#iOS #TestFlight 

Surge 5 5.100.0 (3328) is ready to test on iOS.

What to Test:

5.13.1 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-10-12 [post 509](https://t.me/SurgeTestFlight/509)

#iOS #TestFlight 

Surge 5 5.100.0 (3327) is ready to test on iOS.

What to Test:

- 重写了 PiP 相关逻辑，解决 iOS 18 下实时显示功能可能出现的一些问题

Official Channel: @SurgeTestFlightFeed

## 2024-10-11 [post 504](https://t.me/SurgeTestFlight/504)

#iOS #TestFlight 

Surge 5 5.100.0 (3326) is ready to test on iOS.

What to Test:

- 修正加密 DNS 在特定错误下可能会产生内存泄露的问题
- 增加了过多 [Host] 条目的警告信息

Official Channel: @SurgeTestFlightFeed

## 2024-10-10 [post 501](https://t.me/SurgeTestFlight/501)

#iOS #TestFlight 

Surge 5 5.100.0 (3325) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-10-10 [post 500](https://t.me/SurgeTestFlight/500)

#iOS #TestFlight 

Surge 5 5.100.0 (3323) is ready to test on iOS.

What to Test:

- 部分用户的网络存在异常，IPv6 的路由会被不断配置与清除，导致在 ipv6-vif=auto 的情况下 Surge 需要不断重新配置 VPN。该版本加入了一个 workaround，在同一个网络下，如果 IPv6 路由在存在的情况下又被清除，也不再重置 VIF 状态。
- 优化了加密 DNS 的错误处理逻辑，在遇到错误时将立刻进行重试

Official Channel: @SurgeTestFlightFeed

## 2024-10-09 [post 495](https://t.me/SurgeTestFlight/495)

#iOS #TestFlight 

Surge 5 5.100.0 (3322) is ready to test on iOS.

What to Test:

- 优化了策略组图标的显示效果
- 优化 HTTP 引擎对非标准请求的兼容性
- 修正有时控制中心/桌面小组件在 Surge 已关闭时依然显示开启的问题
- 在没有网络时开启 Surge 将给出更明确的错误提示

Official Channel: @SurgeTestFlightFeed

## 2024-09-26 [post 492](https://t.me/SurgeTestFlight/492)

#iOS #TestFlight 

Surge 5 5.100.0 (3321) is ready to test on iOS.

What to Test:

- Bug fixes

Official Channel: @SurgeTestFlightFeed

## 2024-09-25 [post 488](https://t.me/SurgeTestFlight/488)

#iOS #TestFlight 

Surge 5 5.100.0 (3320) is ready to test on iOS.

What to Test:

- 细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-09-23 [post 476](https://t.me/SurgeTestFlight/476)

#iOS #TestFlight 

Surge 5 5.100.0 (3315) is ready to test on iOS.

What to Test:

- 新增参数 proxy-restricted-to-lan 将限制代理仅接受来自同子网下的设备
- 更新多个依赖库至最新版本，以解决一些低概率崩溃问题
- 优化外置资源请求的 ETag 处理，解决和部分服务端的兼容性问题
- 处理搜索域主机名时强制使用系统 DNS

Official Channel: @SurgeTestFlightFeed

## 2024-09-19 [post 463](https://t.me/SurgeTestFlight/463)

#iOS #TestFlight 

Surge 5 5.100.0 (3313) is ready to test on iOS.

What to Test:

- 适配 iOS 18 的图标模式
- 更新外部资源时将记录与发送 ETag，在资源未变化时不会再触发重下载
- DNS 支持根据系统配置的查找域工作
- 修正新图标的订阅周期约束错误的问题
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 453](https://t.me/SurgeTestFlight/453)

#iOS #TestFlight 

Surge 5 5.100.0 (3309) is ready to test on iOS.

What to Test:

- 修正上个版本可能意外提示请求数过多的问题

Official Channel: @SurgeTestFlightFeed

## 2024-09-17 [post 452](https://t.me/SurgeTestFlight/452)

#iOS #TestFlight 

Surge 5 5.100.0 (3307) is ready to test on iOS.

What to Test:

- 优化了遇到巨量请求时的检测逻辑，确保警告消息可以被显示

5.13.0 RC2

Official Channel: @SurgeTestFlightFeed

## 2024-09-16 [post 441](https://t.me/SurgeTestFlight/441)

#iOS #TestFlight 

Surge 5 5.100.0 (3305) is ready to test on iOS.

What to Test:

- 文案完善
- 新增端口跳跃的 UI 配置
- 新增 [General] 参数 `show-error-page`，用于控制在出现错误时，是否显示 Surge 的 HTTP错误页，该参数默认为开启，行为与先前版本一致

5.13.0 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-09-10 [post 420](https://t.me/SurgeTestFlight/420)

#iOS #TestFlight 

Surge 5 5.100.0 (3304) is ready to test on iOS.

What to Test:

- 使用 iOS 18 SDK 编译，Control Widget 已恢复使用
- 优化了 QUIC 协议和 DoQ 在网络切换时的表现

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 407](https://t.me/SurgeTestFlight/407)

#iOS #TestFlight 

Surge 5 5.100.0 (3303) is ready to test on iOS.

What to Test:

- 修正上个版本 vmess 协议出错的问题

Official Channel: @SurgeTestFlightFeed

## 2024-09-07 [post 405](https://t.me/SurgeTestFlight/405)

#iOS #TestFlight 

Surge 5 5.100.0 (3302) is ready to test on iOS.

What to Test:

- 修正使用了 WebSocket 的代理出向流量统计时会被计算两次的问题
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-09-05 [post 396](https://t.me/SurgeTestFlight/396)

#iOS #TestFlight 

Surge 5 5.100.0 (3301) is ready to test on iOS.

What to Test:

- 远程控制器新增维护菜单，可执行配置重载和更新操作（仅支持 Surge Mac）
- 新增图标 Sapphire

Official Channel: @SurgeTestFlightFeed

## 2024-09-04 [post 391](https://t.me/SurgeTestFlight/391)

#iOS #TestFlight 

Surge 5 5.100.0 (3300) is ready to test on iOS.

What to Test:

- 修正 UDP 连接统计相关的问题

Official Channel: @SurgeTestFlightFeed

## 2024-09-03 [post 389](https://t.me/SurgeTestFlight/389)

#iOS #TestFlight 

Surge 5 5.100.0 (3299) is ready to test on iOS.

What to Test:

- 修正开启端口跳越后，数据统计出现的一些问题
- 调整端口跳越配置参数的分隔符为 ;

Official Channel: @SurgeTestFlightFeed

## 2024-09-02 [post 385](https://t.me/SurgeTestFlight/385)

#iOS #TestFlight 

Surge 5 5.100.0 (3297) is ready to test on iOS.

What to Test:

Hysteria2 与 TUIC 协议支持端口跳越，用于改善 ISP 对 UDP 的 QoS 问题。详见服务端说明。

`Proxy = hysteria2, 1.2.3.4 http://1.2.3.4/, 443, password=pwd, port-hopping 34,5000-6000,7044,8000-9000, port-hopping-interval0`

配置 `port-hopping` 参数后，配置前方的主端口号不再生效。

参数
- `port-hopping`：用于配置端口范围，逗号分隔，支持以-配置范围
- `port-hopping-interval`：变换端口号的时间间隔，默认为 30s

Official Channel: @SurgeTestFlightFeed

## 2024-08-26 [post 373](https://t.me/SurgeTestFlight/373)

#iOS #TestFlight 

Surge 5 5.100.0 (3296) is ready to test on iOS.

What to Test:

- 提高与服务端 quic-go v0.46.0 的兼容性

相关技术细节
QUIC 协议内置了 Idle Timeout 的机制，同时约定了 max_idle_timeout 参数用于服务端和客户端协商空闲超时的具体时间，根据 RFC 9000，该值为 0 的时候表示不使用该机制。（Section 18.2）

Surge 目前版本该参数会指定为 0，因为 Surge 不依赖 QUIC 的 Idle Timeout 机制。然而最新版本 quic-go 重写后，错误将值 0 作为了超时时间，在第一个 stream 结束后，立刻认为闲置时间超时关闭了连接。

更糟糕的是，quic-go 也没有完成 stateless reset 机制，对于 Surge 后续发出的数据包，直接予以丢弃而不产生 stateless reset 响应，导致 Surge 需等待一定时间超时后，才会认为连接失效而重新建立连接。

最新版本为规避该问题，将 max_idle_timeout 参数调整为 30s。

Official Channel: @SurgeTestFlightFeed

## 2024-08-19 [post 370](https://t.me/SurgeTestFlight/370)

#iOS #TestFlight 

Surge 5 5.100.0 (3295) is ready to test on iOS.

What to Test:

- 修正 UI 配置的一些问题
- 修正数个因配置错误可能导致的崩溃

Official Channel: @SurgeTestFlightFeed

## 2024-08-14 [post 366](https://t.me/SurgeTestFlight/366)

#iOS #TestFlight 

Surge 5 5.100.0 (3293) is ready to test on iOS.

What to Test:

- 由于 iOS 18 Beta 阶段反复调整 Control Widget 相关 API，导致更新 iOS beta 后多次出现 Widget 相关问题，该版本开始恢复使用 iOS 17 SDK 编译，等待 iOS 18 GM 版本后再提供 Control Widget

Official Channel: @SurgeTestFlightFeed

## 2024-08-13 [post 364](https://t.me/SurgeTestFlight/364)

#iOS #TestFlight 

Surge 5 5.100.0 (3289) is ready to test on iOS.

What to Test:

- 优化 MITM CA 证书有效性检测，修正使用中间证书进行签名时，UI 层会认为系统未信任证书

Official Channel: @SurgeTestFlightFeed

## 2024-08-12 [post 363](https://t.me/SurgeTestFlight/363)

#iOS #TestFlight 

Surge 5 5.100.0 (3288) is ready to test on iOS.

What to Test:

- 新增 Ponte 诊断功能，用于快速定位 Ponte 相关问题，从 Ponte 设备页面进入
- 修正 subnet 组无法配置自定义图标的问题
- 修正当存在名为 Global 组时，使用全局模式可能出现的问题

Official Channel: @SurgeTestFlightFeed

## 2024-08-06 [post 358](https://t.me/SurgeTestFlight/358)

#iOS #TestFlight 

Surge 5 5.100.0 (3280) is ready to test on iOS.

What to Test:

5.12.0 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-08-05 [post 356](https://t.me/SurgeTestFlight/356)

#iOS #TestFlight 

Surge 5 5.100.0 (3279) is ready to test on iOS.

What to Test:

- 同步 Mac 版本关于 DNS 转发系统的修改
- 使用 CloudKit 重写 Surge tvOS 配置部署流程，稳定性得到大幅提升。请注意需要将 iOS 和 tvOS 都升级至最新版本后才可以使用配置部署功能，且 tvOS 版本需要先启动一次完成注册

Official Channel: @SurgeTestFlightFeed

## 2024-08-04 [post 350](https://t.me/SurgeTestFlight/350)

#iOS #TestFlight 

Surge 5 5.100.0 (3277) is ready to test on iOS.

What to Test:

- 修正在 visionOS 下可能无法检查到特殊 interface 导致持续等待网络的问题

Official Channel: @SurgeTestFlightFeed

## 2024-07-08 [post 333](https://t.me/SurgeTestFlight/333)

#iOS #TestFlight 

Surge 5 5.100.0 (3276) is ready to test on iOS.

What to Test:

- 修正一些 UI 细节问题

Official Channel: @SurgeTestFlightFeed

## 2024-07-06 [post 331](https://t.me/SurgeTestFlight/331)

#iOS #TestFlight 

Surge 5 5.100.0 (3274) is ready to test on iOS.

What to Test:

- 修正 UI 编辑规则时的一些细节问题，如开启状态和注释
- 优化在外部资源页面查看巨型资源时的表现
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-07-02 [post 330](https://t.me/SurgeTestFlight/330)

#iOS #TestFlight 

Surge 5 5.100.0 (3273) is ready to test on iOS.

What to Test:

- 支持在 Gradient 主题下使用自定义图标
- 修正增加规则页面只会显示首个规则类型的问题

Official Channel: @SurgeTestFlightFeed

## 2024-07-02 [post 328](https://t.me/SurgeTestFlight/328)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3272) is ready to test on iOS.

What to Test:

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

Official Channel: @SurgeTestFlightFeed

## 2024-06-28 [post 326](https://t.me/SurgeTestFlight/326)

#iOS #TestFlight 

Surge 5 5.100.0 (3270) is ready to test on iOS.

What to Test:

- 在请求列表里使用增加规则功能时，可以选择加入已存在的规则集。（支持本地规则文件和 inline 规则集）

Official Channel: @SurgeTestFlightFeed

## 2024-06-26 [post 319](https://t.me/SurgeTestFlight/319)

#iOS #TestFlight 

Surge 5 5.100.0 (3269) is ready to test on iOS.

What to Test:

- 优化 No Default Route 模式下开启 IPv6 VIF 时的行为
- 其他细节优化

使用 iOS 18 beta 2 SDK 编译

Official Channel: @SurgeTestFlightFeed

## 2024-06-24 [post 317](https://t.me/SurgeTestFlight/317)

#iOS #TestFlight 

Surge 5 5.100.0 (3268) is ready to test on iOS.

What to Test:

- 细节问题修正
- UI 恢复兼容模式（接管模式）设置并增加详细描述

Official Channel: @SurgeTestFlightFeed

## 2024-06-17 [post 289](https://t.me/SurgeTestFlight/289)

#iOS #TestFlight 

Surge 5 5.100.0 (3263) is ready to test on iOS.

What to Test:

- 模块支持配置 client-source-address 参数
- 修正导出 HAR 时的一些问题
- 使用 iOS 18 SDK 编译，包含控制中心开关

Official Channel: @SurgeTestFlightFeed

## 2024-06-13 [post 279](https://t.me/SurgeTestFlight/279)

#iOS #TestFlight 

Surge 5 5.100.0 (3258) is ready to test on iOS.

What to Test:

- 修正如果开启了始终开启功能，通过小组件开启时未能正确生效的问题

（该版本使用 iOS 17 SDK 编译，不支持控制中心插件）
5.11.3 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-06-12 [post 277](https://t.me/SurgeTestFlight/277)

#iOS #TestFlight 

Surge 5 5.100.0 (3257) is ready to test on iOS.

What to Test:

- 修正 iOS 17 下无法新增桌面小组件的问题

Official Channel: @SurgeTestFlightFeed

## 2024-06-12 [post 276](https://t.me/SurgeTestFlight/276)

#iOS #TestFlight 

Surge 5 5.100.0 (3256) is ready to test on iOS.

What to Test:

- 支持在始终开启开关打开的情况下，通过小组件/控制中心/捷径关闭 Surge
- 支持在 Surge VPN Profile 未被选中的情况下（其他 VPN 运行时），通过小组件/控制中心/捷径开启 Surge

Official Channel: @SurgeTestFlightFeed

## 2024-06-11 [post 274](https://t.me/SurgeTestFlight/274)

#iOS #TestFlight 

Surge 5 5.100.0 (3254) is ready to test on iOS.

What to Test:

- 支持在 iOS 18 beta 下在控制中心里直接开关 Surge

Official Channel: @SurgeTestFlightFeed

## 2024-06-11 [post 272](https://t.me/SurgeTestFlight/272)

#iOS #TestFlight 

Surge 5 5.100.0 (3251) is ready to test on iOS.

What to Test:

- 修正 iOS 18 beta 下卡片页 UI 可能出现的错位

Official Channel: @SurgeTestFlightFeed

## 2024-06-10 [post 271](https://t.me/SurgeTestFlight/271)

#iOS #TestFlight 

Surge 5 5.100.0 (3249) is ready to test on iOS.

What to Test:

- 修正规则集中包含重复的 DOMAIN 与 DOMAIN-SUFFIX 规则时，可能导致 DOMAIN-SUFFIX 失效的问题
- 发现有用户因为配置了过于频繁的 cron 脚本（10s 一次）导致电量消耗激增。该版本增加了 cron 脚本运行频率的自动计算，当单脚本超过每小时 10 次时给于警告

Official Channel: @SurgeTestFlightFeed

## 2024-06-05 [post 261](https://t.me/SurgeTestFlight/261)

#iOS #TestFlight 

Surge 5 5.100.0 (3248) is ready to test on iOS.

What to Test:

- 在 No Default Route 模式下不再配置系统代理，以避免产生问题

Official Channel: @SurgeTestFlightFeed

## 2024-06-05 [post 260](https://t.me/SurgeTestFlight/260)

#iOS #TestFlight 

Surge 5 5.100.0 (3247) is ready to test on iOS.

What to Test:

- 优化 No Default Route 模式的实现，现在 Surge Fake IP DNS 可以正确生效了。
（该模式使用了一种特殊的方法配置路由，以此绕过在开启 VPN 时 HomeKit Camera 无法连接的问题）

Official Channel: @SurgeTestFlightFeed

## 2024-06-05 [post 259](https://t.me/SurgeTestFlight/259)

#iOS #TestFlight 

Surge 5 5.100.0 (3246) is ready to test on iOS.

What to Test:

细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-05-27 [post 247](https://t.me/SurgeTestFlight/247)

#iOS #TestFlight 

Surge 5 5.100.0 (3241) is ready to test on iOS.

What to Test:

- 修正在列表配置中，禁用项目后如果取消，再次进入列表依然保持了项目 UI 的取消状态。
- 文案补全

5.11.2 RC2

Official Channel: @SurgeTestFlightFeed

## 2024-05-27 [post 245](https://t.me/SurgeTestFlight/245)

#iOS #TestFlight 

Surge 5 5.100.0 (3240) is ready to test on iOS.

What to Test:

5.11.2 RC1

Official Channel: @SurgeTestFlightFeed

## 2024-05-26 [post 242](https://t.me/SurgeTestFlight/242)

#iOS #TestFlight 

Surge 5 5.100.0 (3239) is ready to test on iOS.

What to Test:

- 再次优化进行 QUIC Block 的一些细节

Official Channel: @SurgeTestFlightFeed

## 2024-05-21 [post 235](https://t.me/SurgeTestFlight/235)

#iOS #TestFlight 

Surge 5 5.100.0 (3238) is ready to test on iOS.

What to Test:

- 根据用户反馈和更多测试，允许 QUIC 流量带来的弊端会更大，该版本恢复了 block-quic 参数。（ChatGPT 的 Voice Mode 问题经反复测试确认为因 QUIC 和 HTTP/2 连接的服务器不同可能导致的行为不一致，实际上不管是否允许 QUIC 流量均有可能失败）
- 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
- Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
- 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
- 优化了请求详情页的 IP 地址展示
- 编辑策略组时不再可以将自身作为子策略加入

Official Channel: @SurgeTestFlightFeed

## 2024-05-20 [post 231](https://t.me/SurgeTestFlight/231)

#iOS #TestFlight 

Surge 5 5.100.0 (3237) is ready to test on iOS.

What to Test:

- 部分应用在 QUIC 流量被阻止的情况下，无法正确回退到 HTTP/2（如 ChatGPT 的 Voice Mode），预计随着 QUIC 的流行，这种情况可能会越来越多。从该版本起，我们取消了策略的 quic-block 参数，不再对 QUIC 进行自动阻止。交给用户由规则自行决定。
- 优化了 DNS 的请求日志，现在会显示更多的信息，且在规则系统未触发 DNS 时，如果是 DIRECT 策略直连也可以显示 DNS 的相关日志了
- 在删除策略时，如果该策略被策略组所使用，现在允许直接删除并将自动从所有策略组移除
- 建立 Subnet 策略组时，现在可以使用 Subnet 表达式的编辑向导

Official Channel: @SurgeTestFlightFeed

## 2024-05-17 [post 228](https://t.me/SurgeTestFlight/228)

#iOS #TestFlight 

Surge 5 5.100.0 (3236) is ready to test on iOS.

What to Test:

- 请求日志系统优化
- 细节问题调整和修正

Official Channel: @SurgeTestFlightFeed

## 2024-05-16 [post 223](https://t.me/SurgeTestFlight/223)

#iOS #TestFlight 

Surge 5 5.100.0 (3235) is ready to test on iOS.

What to Test:

- 多项细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-05-15 [post 219](https://t.me/SurgeTestFlight/219)

#iOS #TestFlight 

Surge 5 5.100.0 (3231) is ready to test on iOS.

What to Test:

- 过滤器设置不再影响通过 HTTP API 获取的 active 请求列表
- 修正在使用 Smart Group 时，有时手动切换策略后不会打断原有连接的问题
- 修正使用 Body Rewrite 时可能产生的一个错误

Official Channel: @SurgeTestFlightFeed

## 2024-05-13 [post 215](https://t.me/SurgeTestFlight/215)

#iOS #TestFlight 

Surge 5 5.100.0 (3230) is ready to test on iOS.

What to Test:

- 请求日志中将显示匹配到的 Rule/Rewrite/Script 规则的来源模块名
- 优化日志查看器和脚本编辑器
- 可以使用 UI 编辑 HOSTNAME-TYPE 规则了
- 支持导出未成功的请求到 har
- 其他细节问题修正

Official Channel: @SurgeTestFlightFeed

## 2024-05-12 [post 214](https://t.me/SurgeTestFlight/214)

#iOS #TestFlight 

Surge 5 5.100.0 (3229) is ready to test on iOS.

What to Test:

- 新增规则类型 HOSTNAME-TYPE，用于判断请求的主机名的类型，可选值有：IPv4, IPv6, DOMAIN, SIMPLE。（SIMPLE 指的是不包含 . 的主机名，如 localhost）
- 修正规则集索引建立过程可能是会阻塞 UI 的问题

Official Channel: @SurgeTestFlightFeed

## 2024-05-08 [post 204](https://t.me/SurgeTestFlight/204)

#iOS #TestFlight 

Surge 5 5.100.0 (3224) is ready to test on iOS.

What to Test:

- 优化规则集索引，现在规则集中的 IP-ASN 规则也可以被索引优化，测试中约 5000 条 ASN  规则的规则集，在旧版中需耗时 4ms，新版只需要 0.001ms
- 修正不正确的 cron 表达式会导致脚本被持续触发的问题

Official Channel: @SurgeTestFlightFeed

## 2024-05-07 [post 202](https://t.me/SurgeTestFlight/202)

#iOS #TestFlight 

Surge 5 5.100.0 (3223) is ready to test on iOS.

What to Test:

- 修正崩溃
- 当模块中包含的规则使用了一个不存在的策略时会弹出警告

Official Channel: @SurgeTestFlightFeed

## 2024-05-07 [post 200](https://t.me/SurgeTestFlight/200)

#iOS #TestFlight #订阅功能 (?q=%23%E8%AE%A2%E9%98%85%E5%8A%9F%E8%83%BD)

Surge 5 5.100.0 (3222) is ready to test on iOS.

What to Test:

- 新的订阅功能：规则分析，目前包含两个子功能：
   1. 规则使用计数，会记录规则的匹配次数。（只统计主规则集中的条目，各类规则集和逻辑规则的子规则不会被统计，统计时会忽略规则参数）
   2. 当前规则集性能测试
以上功能可在规则配置页面找到

Official Channel: @SurgeTestFlightFeed

## 2024-04-30 [post 198](https://t.me/SurgeTestFlight/198)

#iOS #TestFlight 

Surge 5 5.100.0 (3219) is ready to test on iOS.

What to Test:

- 优化脚本执行 WebView 引擎管理流程
  - 不再复用出现异常的引擎，以避免有问题的脚本导致后续脚本也出现问题。
  - 加快了引擎回收的速度，以避免造成不必要的内存开销。（该内存占用并不计算在 Surge 引擎内，但是会占用系统空余内存）
- 修正 Smart 组在初始化阶段，使用频率标签未能全部屏蔽的问题
- 修正 Subnet 策略组在网络切换前未能正确选择策略的问题
- 修正脚本编辑器保存时，如果配置中不存在任何本地脚本，会导致崩溃的问题

Official Channel: @SurgeTestFlightFeed

## 2024-04-28 [post 177](https://t.me/SurgeTestFlight/177)

#iOS #TestFlight 

Surge 5 5.21.0 (3207) is ready to test on iOS.

What to Test:

- 外部资源页面文案细节修正

5.11.1 RC4

Official Channel: @SurgeTestFlightFeed

## 2024-04-28 [post 171](https://t.me/SurgeTestFlight/171)

#iOS #TestFlight 

Surge 5 5.21.0 (3199) is ready to test on iOS.

What to Test:

- 限制 iCloud 后台自动同步的最大文件数量为 200，避免产生内存占用问题
- 修正通过远程控制器调整策略时，UI 可能显示不正确的问题
- 修正当外部策略组产生变化时，可能导致的崩溃
- 修正配置升级功能未能对托管配置和企业配置正确生效的问题

5.11.1 RC3

Official Channel: @SurgeTestFlightFeed

## 2024-04-27 [post 156](https://t.me/SurgeTestFlight/156)

#iOS #TestFlight 

Surge 5 5.21.0 (3193) is ready to test on iOS.

What to Test:

- 细节问题修正

5.11.1 RC2

Official Channel: @SurgeTestFlightFeed

## 2024-04-26 [post 147](https://t.me/SurgeTestFlight/147)

#iOS #TestFlight 

Surge 5 5.21.0 (3190) is ready to test on iOS.

What to Test:

5.11.1 RC1

## 2024-04-25 [post 144](https://t.me/SurgeTestFlight/144)

#iOS #TestFlight 

Surge 5 5.21.0 (3189) is ready to test on iOS.

What to Test:

- 修正最近两个版本 DOMAIN-SUFFIX 未能匹配到域名本身的问题

## 2024-04-25 [post 142](https://t.me/SurgeTestFlight/142)

#iOS #TestFlight 

Surge 5 5.21.0 (3188) is ready to test on iOS.

What to Test:

- Bug fixes

## 2024-04-25 [post 138](https://t.me/SurgeTestFlight/138)

#iOS #TestFlight 

Surge 5 5.21.0 (3187) is ready to test on iOS.

What to Test:

- 崩溃修正
- 修正本地大型规则集被更新后，需要冷启动主程序才能触发重索引的问题
- 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题

## 2024-04-25 [post 135](https://t.me/SurgeTestFlight/135)

#iOS #TestFlight 

Surge 5 5.21.0 (3184) is ready to test on iOS.

What to Test:

- 优化小型规则集的匹配性能（1000 条规则以下为小型，优化前单次匹配耗时约为 0.025 ms，优化后 0.001 ms）
- 修正本地脚本文件被编辑后无法被自动重载的问题
- 优化索引系统，对于需要打开主程序进行索引的规则集，现在在进行重索引前，将沿用已存在的索引（旧版本也有这样的设计，但仅限远程资源，且重启后会失效）

## 2024-04-24 [post 130](https://t.me/SurgeTestFlight/130)

#iOS #TestFlight 

Surge 5 5.21.0 (3180) is ready to test on iOS.

What to Test:

- 修正脚本内容被修改或更新后，需要重新开启才可生效的问题

5.11.0 RC8

## 2024-04-24 [post 128](https://t.me/SurgeTestFlight/128)

#iOS #TestFlight 

Surge 5 5.21.0 (3179) is ready to test on iOS.

What to Test:

- 为 iOS 17.5 beta 下的 WebView 脚本执行无法超过 5s 的问题加入 workaround
- 修正通过 Smart 组使用 UDP 时，未能判断策略是否支持 UDP 的问题
- WireGuard 的策略详情页中新增现在使用的跳板代理策略名

5.11.0 RC7

## 2024-04-23 [post 127](https://t.me/SurgeTestFlight/127)

#iOS #TestFlight 

Surge 5 5.21.0 (3178) is ready to test on iOS.

What to Test:

- 优化了规则系统的性能，特别是在较旧 CPU 上的表现
- 细节问题修正

5.11.0 RC6

## 2024-04-23 [post 123](https://t.me/SurgeTestFlight/123)

#iOS #TestFlight 

Surge 5 5.21.0 (3171) is ready to test on iOS.

What to Test:

- 修正当本地外部资源被编辑后，可能无法被重新索引的问题
- 修正一些日志错误

5.11.0 RC5

## 2024-04-23 [post 119](https://t.me/SurgeTestFlight/119)

#iOS #TestFlight 

Surge 5 5.21.0 (3167) is ready to test on iOS.

What to Test:

- 修正外部资源相关的一些问题
- 优化日志系统时间机制，不再使用 walltime 以避免系统对时的时钟抖动导致负时间产生
- 修正 subnet 组无法执行测试的问题

5.11.0 RC4

## 2024-04-22 [post 111](https://t.me/SurgeTestFlight/111)

#iOS #TestFlight 

Surge 5 5.21.0 (3164) is ready to test on iOS.

What to Test:

- 修正规则集索引建立的相关问题，现在小于 1MB 的规则集可以不由主程序完成索引

5.11.0 RC3

## 2024-04-22 [post 107](https://t.me/SurgeTestFlight/107)

#iOS #TestFlight 

Surge 5 5.21.0 (3160) is ready to test on iOS.

What to Test:

- 文案补全
- 优化规则集重索引的时机
- 在使用自动配置升级前，备份当前配置

5.11.0 RC2

## 2024-04-22 [post 102](https://t.me/SurgeTestFlight/102)

#iOS #TestFlight 

Surge 5 5.21.0 (3156) is ready to test on iOS.

What to Test:

- 新增低内存模式，在内存用量到达 40MB 以上后将降低减少内存用量，避免超限
- 修正 WireGuard 配置修改后需要重启才可以被应用的问题

5.11.0 RC1

## 2024-04-21 [post 100](https://t.me/SurgeTestFlight/100)

#iOS #TestFlight 

Surge 5 5.21.0 (3155) is ready to test on iOS.

What to Test:

- 优化 TUN 接管和特定 app 的性能兼容性问题
- 修正主程序完成规则集索引后，需要重启 Surge 引擎才可以进行加载的问题
- 其他细节优化

## 2024-04-20 [post 99](https://t.me/SurgeTestFlight/99)

#iOS #TestFlight 

Surge 5 5.21.0 (3151) is ready to test on iOS.

What to Test:

- 规则系统整体性能优化
- µs 时间改为 ms 的小数方式表示
- 大幅优化大型域名规则集中的索引算法，测试环境下，对包含 310000 条规则的规则集进行测试（50% hit rate）
旧版本：2.167 ms
新版本：0.058 ms
- 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题

## 2024-04-20 [post 91](https://t.me/SurgeTestFlight/91)

#iOS #TestFlight 

Surge 5 5.21.0 (3150) is ready to test on iOS.

What to Test:

- 优化 WireGuard 失败处理
- 降低 TUIC 协议在休眠时对电量的消耗
- 请求日志系统时间统计精度提高，现在可精确到 µs 级（1s 00ms,1ms 00µs）

## 2024-04-19 [post 87](https://t.me/SurgeTestFlight/87)

#iOS #TestFlight 

Surge 5 5.21.0 (3148) is ready to test on iOS.

What to Test:

- 修正对于非标准端口号的 HTTP 请求，各种规则匹配时行为不一致的问题，这种情况下匹配的目标 URL 必需包含端口号
- 重新了网络切换时的逻辑
- 其他问题修正

## 2024-04-19 [post 84](https://t.me/SurgeTestFlight/84)

#iOS #TestFlight 

Surge 5 5.21.0 (3146) is ready to test on iOS.

What to Test:

- 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 * 匹配域名
- 放开了 fallback 组使用 Smart Group 的限制，允许在 fallback 组内使用 Smart Group 作为子策略
- 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
- UI 细节调整

## 2024-04-18 [post 64](https://t.me/SurgeTestFlight/64)

#iOS #TestFlight 

Surge 5 5.21.0 (3143) is ready to test on iOS.

What to Test:

- 修正在部分网络上 IPv6 VIF 设置为 auto 时无法开启的问题
- 脚本编辑器支持自定义保存文件名和从不属于配置的 .js 文件中载入

## 2024-04-18 [post 63](https://t.me/SurgeTestFlight/63)

#iOS #TestFlight 

Surge 5 5.21.0 (3142) is ready to test on iOS.

What to Test:

- ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
- 为 ipv6-vif=always 参数增加了警告
- 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）
- 文案完善

## 2024-04-17 [post 57](https://t.me/SurgeTestFlight/57)

#iOS #TestFlight 

Surge 5 5.21.0 (3141) is ready to test on iOS.

What to Test:

- 修正配置升级对一般配置使用时，未能正确写入的问题
- 修正 Smart 组可以使用 include-other-group 参数包含一个策略组作为子策略的问题

## 2024-04-17 [post 56](https://t.me/SurgeTestFlight/56)

#iOS #TestFlight 

Surge 5 5.21.0 (3140) is ready to test on iOS.

What to Test:

- 修正配置升级功能的一些问题
- Hysteria2 的默认 QUIC 行为修改为阻止

## 2024-04-17 [post 55](https://t.me/SurgeTestFlight/55)

#iOS #TestFlight 

Surge 5 5.21.0 (3139) is ready to test on iOS.

What to Test:

- 新增配置文件行命令 #!REQUIREMENT，用法请详见频道说明
- 新增配置功能自动升级机制，可自动将配置中的 url-test/load-balance，自动升级为 smart 组。
  - 对于一般配置，改动会直接写入配置中
  - 对于托管配置和企业配置，会在加载配置时自动应用（企业配置不会进行询问，将自动完成升级）
如果不希望托管配置或企业配置被自动升级所修改，可增加配置描述
#!FORBIDDEN-UPGRADE smart-group
（未来会增加更多自动升级的关键字）
- 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

## 2024-04-16 [post 49](https://t.me/SurgeTestFlight/49)

#iOS #TestFlight 

Surge 5 5.21.0 (3138) is ready to test on iOS.

What to Test:

- 优化了在网络切换时的自动重试机制
- 修正了 JSC 的并发数量限制未正确生效的问题
- 优化了 JSC 脚本的内存控制，现在在脚本结束或超时后，脚本会被立刻打断，避免持续产生内存占用

## 2024-04-16 [post 44](https://t.me/SurgeTestFlight/44)

#iOS #TestFlight 

Surge 5 5.21.0 (3137) is ready to test on iOS.

What to Test:

- 修正当存在类似 RULE-SET,,DIRECT 的规则时会导致的异常和崩溃
- 修正部分代理错误未能被 Smart 组正确识别的问题
- 修正部分情况下，代理策略的统计数据中，上传数据量被漏计的问题
- 修正使用 Smart 组作为 underlying-proxy 的情况下，在特定错误的情况下会无法自动切换策略的问题
- 优化外部资源的缓存系统
- 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

## 2024-04-15 [post 38](https://t.me/SurgeTestFlight/38)

#iOS #TestFlight 

Surge 5 5.21.0 (3135) is ready to test on iOS.

What to Test:

- 修正在 Surge iOS 主程序和引擎都开启时，iCloud 内容发生变化可能无法被主程序所检测的问题
- 修改了 Smart 组统计使用率的计算方法，现在最近的使用情况将更快的影响使用率标签。（当策略出现异常后，依然需要一段时间后才会被取消掉最常使用标签，该标签的意义是最近一段时间内最常使用的策略）
- 优化了内存占用，不常用和巨大的脚本现在将不会被缓存至内存
- 提高内存警告的阈值到 45MB，原为 40MB。
- 修改了策略组页面的一些显示细节
- 网络诊断页新增 SSID/BSSID，增加复制功能
- 新增对 QUIC 类协议的丢包率统计，先前版本中由于未计算 QUIC 类协议的丢包率，在 Smart 组中可能导致 QUIC 类策略被高估。
- 其他问题修正

## 2024-04-14 [post 33](https://t.me/SurgeTestFlight/33)

#iOS #TestFlight 

Surge 5 5.21.0 (3134) is ready to test on iOS.

What to Test:

- 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
- 在发现当前网络由 Surge Mac Gateway 所接管时，现在将自动暂停 Surge iOS。（可通过 auto-suspend 选项调整行为，默认开启）
- 现在在日志界面执行日志上传时，将自动为当前运行的引擎生成最近的 verbose 日志（新版本在内存缓存了 256KB 的日志），这样在汇报问题时，直接执行上传即可，无需再使用 verbose 模式复现。
- 对于策略组与脚本类型的外部资源，现在限制最大大小为 2MB，避免当错误配置时，导致的内存超限。
- 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
- 细节问题修正

## 2024-04-13 [post 31](https://t.me/SurgeTestFlight/31)

#iOS #TestFlight 

Surge 5 5.21.0 (3131) is ready to test on iOS.

What to Test:

- 当因为 JSC 脚本导致的内存占用过高时，将给予直接通知警告
- 修正有时可能无法正确判断系统 IPv6 状态的问题
- 其他修正

## 2024-04-13 [post 30](https://t.me/SurgeTestFlight/30)

#iOS #TestFlight 

Surge 5 5.21.0 (3130) is ready to test on iOS.

What to Test:

- 修正上个版本容易出现内存高占用的问题

## 2024-04-13 [post 29](https://t.me/SurgeTestFlight/29)

#iOS #TestFlight 

Surge 5 5.21.0 (3129) is ready to test on iOS.

What to Test:

- 修正上个版本在使用脚本时容易出现内存高占用的问题

## 2024-04-12 [post 28](https://t.me/SurgeTestFlight/28)

#iOS #TestFlight 

Surge 5 5.21.0 (3127) is ready to test on iOS.

What to Test:

- 细节修正

## 2024-04-12 [post 27](https://t.me/SurgeTestFlight/27)

#iOS #TestFlight 

Surge 5 5.21.0 (3124) is ready to test on iOS.

What to Test:

- 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
- 修正了初始化日志中的一些错误输出
- 修正了配置 Ponte client proxy 为 Smart Group 时无法连接的问题
- Smart Group 支持 evaluate-before-use 参数了
- 默认 UDP 测试目标改为 1.0.0.1 http://1.0.0.1/
- 其他细节问题修正

## 2024-04-12 [post 23](https://t.me/SurgeTestFlight/23)

#iOS #TestFlight 

Surge 5 5.21.0 (3119) is ready to test on iOS.

What to Test:

- 细节问题修正
- 修正 IPv6 开关在调整后需要切换网络或重启才可以生效的问题

## 2024-04-11 [post 19](https://t.me/SurgeTestFlight/19)

#iOS #TestFlight 

Surge 5 5.21.0 (3116) is ready to test on iOS.

What to Test:

- 修正仅修改 DNS 映射后，不重启 Surge 无法生效的问题
- 在脚本中使用 API 传入了错误类型时，将产生脚本异常
- type event 脚本的 notificatino 类型，数据中新增 scriptOptions 字段，包含由脚本触发的通知的 options 字段原始内容
- 其他细节问题修正

## 2024-04-10 [post 15](https://t.me/SurgeTestFlight/15)

#iOS #TestFlight 

Surge 5 5.21.0 (3114) is ready to test on iOS.

What to Test:

- 修正新的 auto-dismiss 参数有时无效的问题
- 完成了 Smart Group 对 Wi-Fi Assist 和 Hybrid 功能的支持
- 其他问题修正

## 2024-04-10 [post 13](https://t.me/SurgeTestFlight/13)

#iOS #TestFlight 

Surge 5 5.21.0 (3112) is ready to test on iOS.

What to Test:

- 修正最近请求可能卡住不更新的问题
- $notification.post http://notification.post/ 增强

$notification.post http://notification.post/(title, subtitle, body, options)
可用参数

- `action`：点击通知打开 Surge 后的操作
  - open-url: 打开一个 URL，具体的 URL 通过 url 参数给出
  - clipboard: 复制一段内容到剪贴板（会经过用户确认），内容通过 text 参数给出
- `media-url`：为通知提供一个媒体内容，如图片。内容为完整的 URL。
- media-base64`：功能同上，但是内容直接由 base64 提供。需要同时提供 `media-base64-mime 参数给出内容的 MIME 类型。
- `auto-dismiss`：在一段指定时间后自动消除该通知，单位为秒，默认为 0，即持续存在。
- `sound`：弹出通知时使用默认推送消息提示音

## 2024-04-09 [post 8](https://t.me/SurgeTestFlight/8)

#iOS #TestFlight 

Surge 5 5.21.0 (3111) is ready to test on iOS.

What to Test:

- 问题修正与细节优化

