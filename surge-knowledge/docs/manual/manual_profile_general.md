# The [General] Section

The `[General]` section holds Surge's global settings: logging, DNS, the virtual network interface (VIF), proxy service listeners, remote control, connectivity testing, and traffic processing behavior. All keys are optional `key = value` lines; keys are case-insensitive.

```
[General]
loglevel = notify
dns-server = 223.5.5.5, 114.114.114.114
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, localhost, *.local
test-timeout = 5
```

This page lists every user-facing key. Some subjects have dedicated chapters with full details:

* DNS keys are covered in depth in the [DNS chapter](../dns/overview.md).
* MITM options live in the [MITM section](../http/mitm.md), not in `[General]`.
* Per-network overrides of some keys are available via [Subnet Settings](../features/subnet-settings.md).

As the options change frequently, you may look up the most up-to-date explanation for the `[General]` section options within the app:

* Surge Mac: Main Window Menu -> Help -> Profile Syntax
* Surge iOS: More Tab -> Help -> Profile Syntax

Several keys take the Host List parameter type; see [Host List Parameter Type](host-list.md) for the matching rules.

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

These keys configure Surge's DNS client. See the [DNS chapter](../dns/overview.md) for how Surge resolves names and the [Encrypted DNS](../dns/encrypted-dns.md) page for DoH/DoQ/DoT details.

#### dns-server

Optional, comma-separated IP addresses (optionally `ip:port`), or `system`

The IP addresses of upstream DNS servers. The literal value `system` uses the system resolver. See [DNS Servers](../dns/dns-server.md) for the full syntax.

If an encrypted DNS URL is found in this key, Surge automatically moves it to `encrypted-dns-server` when loading the profile (legacy support).

#### encrypted-dns-server

Optional, comma-separated URLs

The URLs of the encrypted DNS servers. If encrypted DNS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the encrypted DNS URL.

Supported protocols:

* DNS over HTTPS: `https://example.com`
* DNS over HTTP/3: `h3://example.com`
* DNS over QUIC: `quic://example.com`
* DNS over TLS: `tls://example.com`
* DNS over TCP: `tcp://example.com` — plain, unencrypted DNS over TCP on port 53 by default; use it only with trusted servers.

The legacy key `doh-server` is accepted and rewritten to this key on save. See [Encrypted DNS](../dns/encrypted-dns.md).

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

By default, DNS lookup is always performed on the remote server if a proxy policy is used. After enabling this option, Surge uses the IP address instead of the domain to set up the proxy connection if the local DNS mapping result of the target domain exists. See [Local DNS Mapping](../dns/local-dns-mapping.md).

#### hijack-dns

Optional, comma-separated `ip[:port]` entries or `*[:port]`, default port: 53

By default, Surge only returns fake IP addresses for DNS queries sent to the Surge DNS address (`198.18.0.2`). Queries sent to a standard DNS server are forwarded.

Some devices or software always use a hardcoded DNS server. (For example, Google Speakers always use 8.8.8.8.) You may use this option to hijack the query to get a fake address. Each entry is either an IPv4 address (optionally with a port) or `*`; use `hijack-dns = *:53` to hijack all DNS queries.

The fake DNS responder listens on `198.18.0.2` (IPv4) and `fd00:6152::2` (IPv6), so even pure IPv6 networks can point their clients to Surge. See [Advanced DNS Topics](../dns/advanced.md).

#### always-real-ip

Optional, Host List

This option asks Surge to return a real IP address instead of a fake IP address when Surge VIF handles a DNS question. The DNS packet is forwarded to upstream DNS servers.

This parameter is of the Host List type; for detailed rules see [Host List Parameter Type](host-list.md). See also [Advanced DNS Topics](../dns/advanced.md).

### GeoIP Database

See [IP-Based Rules](../rules/ip.md) for how the GeoIP database is used.

#### geoip-maxmind-url

Optional, URL

The URL of the GeoIP database for updating.

#### disable-geoip-db-auto-update

Optional, Boolean, default: false

Disable the auto-updating for the GeoIP database.

### IPv6 & Virtual Network Interface

See [Enhanced Mode](../features/enhanced-mode.md) for the VIF concept.

#### ipv6

Optional, Boolean, default: false

Enable full IPv6 support. After enabling this option, Surge queries AAAA records when accessing domain names. Even if this option is not enabled, you can still access IPv6 sites by using IPv6 addresses directly. Enabling it may increase DNS latency; turn it on only when needed.

#### ipv6-vif

Optional, `disabled` | `auto` | `always`, default: `disabled`

Allow IPv6 through Surge VIF. Useful when you want Surge to handle raw TCP connections connecting to IPv6 addresses.

* `disabled`: Never set up the Surge VIF with IPv6. (The legacy value `off` is also accepted.)
* `auto`: Only set up the Surge VIF with IPv6 if the local network has a valid IPv6 network.
* `always`: Always set up the Surge VIF with IPv6. This may break apps on networks without IPv6 connectivity, and Surge warns about it during profile verification.

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

#### icmp-forwarding {{ book.VER | replace("%TEXT%", "iOS 5.14.3+") }} {{ book.VER | replace("%TEXT%", "Mac 5.10.0+") }}

Optional, Boolean, default: true

When the enhanced mode is enabled, to reduce interference with users, Surge will directly forward all ICMP packets so as not to affect the use of tools like ping.

However, this may lead to IP leakage for some users who are extremely privacy-conscious. Disable this option to stop ICMP forwarding; ping will no longer work through Surge.

### System Proxy Bypass

#### skip-proxy

Optional, Host List

In the iOS version, this option forces connections to these domain/IP ranges to be handled by Surge VIF instead of Surge proxy. In the macOS version, these settings are applied to the system when "Set as System Proxy" is enabled. This option is used to fix compatibility problems with some apps; it is not a way to keep requests off a proxy policy.

* To specify a single domain, enter the domain name - for example, apple.com.
* To specify all websites on a domain, use an asterisk before the domain name - for example, `*apple.com`.
* To specify a specific part of a domain, specify each part - for example, store.apple.com.
* To specify hosts or networks by IP addresses, enter a specific IP address such as 192.168.2.11 or an address range, such as `192.168.2.*` or 192.168.2.0/24.

Notice: If you enter an IP address or address range, you are only able to bypass the proxy when you connect to that host using that address, not when you connect to the host by a domain name that resolves to that address.

For the general matching rules see [Host List Parameter Type](host-list.md).

#### exclude-simple-hostnames

Optional, Boolean, default: false

Just like the `skip-proxy` parameter. This option lets requests using simple hostnames (without a dot) be handled by Surge VIF instead of Surge proxy.

### Proxy Services & Remote Access

#### proxy-restricted-to-lan {{ book.VER | replace("%TEXT%", "iOS 5.13.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.8.1+") }}

Optional, Boolean, default: true

#### gateway-restricted-to-lan {{ book.VER | replace("%TEXT%", "iOS 5.13.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.8.1+") }}

Optional, Boolean, default: true

It has been found that some users, due to a lack of understanding of network security knowledge, accidentally expose proxy and gateway services to the Internet (e.g., configured DMZ). Therefore, these two parameters have been added to restrict proxy and [gateway](../features/gateway.md) services to only accept devices from the current subnet. Both are enabled by default.

#### external-controller-access

Optional, `key@ip:port`

This option allows an external controller to control Surge, such as Surge Dashboard (macOS) and Surge iOS Remote Controller (iOS). E.g.: `key@0.0.0.0:6165`. See [Dashboard](../tools/dashboard.md).

#### http-api

Optional, `key@ip:port`

This option allows using HTTP APIs to control Surge. E.g.: `key@0.0.0.0:6166`. See [HTTP API](../tools/http-api.md).

#### http-api-tls

Optional, Boolean, default: false

Use HTTPS protocol instead of HTTP for the HTTP API. The MITM CA certificate must be configured first. You need to install the certificate on the client's device manually.

#### http-api-web-dashboard

Optional, Boolean, default: false

You may control Surge via a web browser after enabling this. The web dashboard is served on the `http-api` listener.

### Connectivity Testing

See [Testing](../tools/testing.md) for latency and throughput testing details, and [Common Policy Parameters](../policies/parameters.md) for per-policy overrides.

#### internet-test-url

Optional, HTTP(S) URL, default: `http://bing.com/`

The URL for the Internet connectivity testing. Also, the testing URL for the DIRECT policy.

HTTPS URLs are supported. {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }} The TLS handshake is performed before the HEAD request, and the server certificate is verified; the reported latency is still measured on a second HEAD request over the established connection, so it excludes the TLS handshake.

#### proxy-test-url

Optional, HTTP(S) URL, default: `http://bing.com/`

The default testing URL for proxy policies. HTTPS URLs are supported the same way as `internet-test-url`. {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }}

#### test-timeout

Optional, in seconds, default: 5

The default connectivity testing timeout for proxy policies. (Tests for the DIRECT policy use a 10-second timeout.)

#### proxy-test-udp

Optional, `hostname@ipv4`

The default UDP test parameter for proxies. E.g.: `apple.com@8.8.8.8`. The test query is sent to the given IPv4 address on port 53.

### Traffic Processing

#### force-http-engine-hosts

Optional, Host List

Make Surge treat TCP connections as HTTP requests. The Surge HTTP engine processes the requests, and advanced features such as capture, rewrite, and scripting become available. See [HTTP Processing Overview](../http/overview.md).

By default, only connections on port 80 are matched. Append `:port` to match another port, `host:0` to match all ports of a host, or `*:0` to match everything. Prefix an entry with `-` to exclude it.

This parameter is of the Host List type; for detailed rules see [Host List Parameter Type](host-list.md).

#### always-raw-tcp-hosts {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

Optional, Host List

Surge will automatically sniff the protocol for TCP requests sent to ports 80 and 443, enabling advanced HTTP/HTTPS features while optimizing performance. However, this may cause some compatibility issues. If you encounter problems, you can add the hostname here, and Surge will not sniff these requests' protocols.

This parameter is of the Host List type; for detailed rules see [Host List Parameter Type](host-list.md).

#### always-raw-tcp-keywords {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}

Optional, comma-separated keywords

Behaves similar to `always-raw-tcp-hosts` but matches by substring rather than a host list. Any hostname containing one of the keywords will skip protocol sniffing and stay in raw TCP mode, which helps when the exact hostname is not predictable.

#### udp-policy-not-supported-behaviour

Optional, `REJECT` | `DIRECT`, default: `REJECT`

The fallback behavior when UDP traffic matches a policy that doesn't support UDP relay. Starting from Surge Mac 6.0.0, the default is `REJECT` to avoid leaking traffic unknowingly. See [UDP Relay](../policies/udp.md).

#### udp-priority

Optional, Boolean, default: true

When enabled, Surge prioritizes UDP packets when the system load is very high and packet processing is delayed. Also known as game mode.

#### block-quic {{ book.VER | replace("%TEXT%", "iOS 5.14.6+") }} {{ book.VER | replace("%TEXT%", "Mac 5.10.3+") }}

Optional, `per-policy` | `all-proxy` | `all` | `always-allow`, default: `per-policy`

This parameter is used to globally override the behavior of whether to block QUIC traffic:

* `per-policy`: Determined by each policy's `block-quic` parameter. This is the default value.
* `all-proxy`: Overrides the proxy policies' `block-quic` parameter, blocking all QUIC traffic through proxies.
* `all`: Overrides all policies' `block-quic` parameters, blocking everything including DIRECT policies.
* `always-allow`: Overrides the proxy policies' `block-quic` parameter, allowing everything.

See the per-policy [`block-quic` parameter](../policies/parameters.md).

### Error Pages

#### show-error-page {{ book.VER | replace("%TEXT%", "Mac 5.8.0+") }}

Optional, Boolean, default: true

Controls whether Surge displays its built-in HTTP error page when a request fails (for example, because a policy rejects it or a proxy cannot be reached). Set it to `false` if you prefer the client to receive the raw network error instead of the Surge error page.

#### show-error-page-for-reject

Optional, Boolean, default: false

Show an error webpage for the REJECT policy if the request is a plain HTTP request.

## Surge iOS Only Parameters

### Working Mode

#### compatibility-mode

Optional, integer 0–5, default: 0

This option is used to control the working mode of Surge iOS.

* 0: Auto. In versions of Surge iOS prior to 5.8.0 this is equivalent to 1; from 5.8.0 it is equivalent to 3.
* 1: Proxy Takeover + VIF. In this mode, proxy takeover has higher priority than VIF takeover, offering the best performance, but some apps may check for proxy settings and refuse to work.
* 2: Proxy Takeover Only.
* 3: VIF Takeover Only. The default working mode of the latest version.
* 4: Proxy Takeover + VIF, but the proxy uses the VIF address instead of the loopback address.
* 5: VIF Takeover Only, but the VIF routing uses multiple smaller routes for takeover and does not configure a default route. Can be used to bypass some special issues (e.g., HomeKit Secure Camera).

#### auto-suspend {{ book.VER | replace("%TEXT%", "iOS 5.11.0+") }}

Optional, Boolean, default: true

Automatically suspend Surge iOS when a network taken over by a Surge Mac [gateway](../features/gateway.md) is detected.

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

Follow local DNS mapping items in `/etc/hosts`. See [Local DNS Mapping](../dns/local-dns-mapping.md).

#### subnet-exp-wifi-always-match

Optional, Boolean, default: true

When enabled, SSID/BSSID [subnet expression](../features/subnet-settings.md) patterns still match even when Wi-Fi is not the primary network interface. Disable it to make these patterns match only when Wi-Fi is the primary interface.

This key replaces the legacy `use-default-policy-if-wifi-not-primary` key, which is accepted and migrated with its meaning inverted.
