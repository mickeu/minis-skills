# Common Policy Parameters

These parameters can be appended as `key=value` pairs to any policy line, regardless of the proxy protocol. Protocol-specific parameters are documented on each protocol page; parameters shared by TLS-based protocols are on the [TLS Parameters](tls.md) page, and UDP-related parameters on the [UDP Relay](udp.md) page.

The egress and testing parameters below apply to both proxy policies and [built-in policy aliases](built-in.md#alias), except where noted.

## Egress Parameters

#### interface

Optional, network interface name, default: automatic.

Force the policy to use a specified outgoing network interface:

```
ProxyHTTP = http, 1.2.3.4, 443, username, password, interface = en2
```

A direct policy alias supports the `interface` parameter like a proxy policy:

```
[Proxy]
Corp-VPN = direct, interface = utun0
WiFi = direct, interface = en2, allow-other-interface=true
```

Make sure the interface has a valid route table for the destination address. WireGuard and Tailscale policies do not support interface binding.

#### allow-other-interface

Optional, boolean, default: false.

When true, if the desired interface is unavailable, Surge is allowed to use the default interface to bind the connection. Otherwise, the connection fails directly.

```
ProxyHTTP = http, 1.2.3.4, 443, username, password, interface = en2, allow-other-interface=true
```

#### dns-follow-interface {{ book.VER | replace("%TEXT%", "iOS 5.15.2+") }} {{ book.VER | replace("%TEXT%", "Mac 5.2.0+") }}

Optional, boolean, default: false.

Make the `interface` parameter of the policy also take effect for DNS queries; DNS requests that match the policy will use this interface for queries. (If DNS is triggered during the rule matching stage, a specific interface will not be used.)

#### no-error-alert

Optional, boolean, default: false. Proxy policies only.

Do not show error alerts for this policy.

#### ip-version

Optional, `dual` / `v4-only` / `v6-only` / `prefer-v4` / `prefer-v6`, default: `dual`.

Choose the behavior between IPv4 and IPv6 protocols. The option only affects the connection to the proxy server, so it only makes sense when the proxy server's hostname is a domain. If an [underlying proxy](#proxy-chain) is configured, this option has no effect since the DNS resolution happens remotely.

- `dual`: use the fastest link.
- `v4-only` / `v6-only`: use only the specified address family.
- `prefer-v4` / `prefer-v6`: prefer the specified address family.

Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, `prefer-v4` and `prefer-v6` use the preferred address family first during TCP connection establishment. If a connection cannot be established within 3 seconds, Surge also starts trying addresses from the other family. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

#### hybrid {{ book.VER | replace("%TEXT%", "iOS Only") }}

Optional, `auto` / `on` / `off`, default: `auto`.

Set up the connection with cellular data and Wi-Fi simultaneously, then use the faster link. When omitted (`auto`), the connection follows the global All Hybrid setting; `on` and `off` force the behavior for this policy. `true`/`false` are also accepted.

#### tfo

Optional, boolean, default: false.

Enable TCP Fast Open.

#### tos

Optional, 0–255 in decimal or `0x` hexadecimal, default: 0.

Customize the IP TOS value.

#### ecn {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

Optional, `auto` / `on` / `off`, default: `auto`. Proxy policies only.

Enable ECN (Explicit Congestion Notification) support. It can improve bandwidth performance in high packet loss environments, but enabling it in unsupported network environments may result in connection failure. The parameter takes effect for QUIC-based protocols and WireGuard/Tailscale policies; it has no effect on plain TCP protocols.

On supported systems, ECN is enabled by default for QUIC-based proxy protocols starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. These protocols automatically fall back to non-ECN handling when an anomaly is detected. WireGuard and Tailscale policies remain disabled by default. Use `ecn=true` or `ecn=false` to override the applicable default explicitly. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

#### block-quic {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

Optional, `auto` / `on` / `off`, default: `auto`.

Forwarding QUIC traffic through a proxy may cause performance issues. Enabling this option blocks QUIC traffic, causing the client to fall back to the traditional HTTPS/TCP protocol.

- `auto`: automatically decide based on whether the policy is suitable for forwarding QUIC traffic.
- `on`: block QUIC traffic.
- `off`: do not block QUIC traffic.

If this parameter is omitted, proxy policies block QUIC by default, while DIRECT and other built-in policies do not. {{ book.VER | replace("%TEXT%", "Mac 6.4.3+") }}

## Testing Parameters

#### test-url

Optional, HTTP(S) URL, default: the global `proxy-test-url`/`internet-test-url` setting.

Override the global testing URL for this policy. The URL is used for availability and latency testing by performing an HTTP HEAD request. HTTPS URLs are supported; see `internet-test-url` in the [\[General\] section reference](../profile/general.md) for how the latency is measured over TLS. {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }}

```
Proxy = snell, 1.2.3.4, 8000, psk=pwd, version=5, test-url=http://google.com
```

#### test-timeout

Optional, in seconds, default: the global `test-timeout` setting.

Override the global testing timeout for this policy.

#### test-udp

Optional, `hostname@ipv4`, default: the global `proxy-test-udp` setting.

Override the global `proxy-test-udp` setting for this policy. The UDP relay is tested by performing a DNS lookup of the hostname via the given server. See [UDP Relay](udp.md#udp-testing).

```
Proxy = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd, udp-relay=true, test-udp=google.com@1.1.1.1
```

## Proxy Chain

#### underlying-proxy

Optional, the name of another proxy policy or policy group. Proxy policies only.

Use a proxy to connect to another proxy, aka proxy chain. Surge first establishes a connection to the underlying policy, then connects to the target proxy server through it.

```
[Proxy]
Entry = https, entry.example.com, 443, username, password
Exit = snell, exit.example.com, 443, psk=pwd, version=5, underlying-proxy=Entry
```

With this configuration, traffic sent to the `Exit` policy is relayed through `Entry`: client → Entry → Exit → destination.

Notes:

* The value may also be a policy group name, so the entry node can be selected dynamically.
* When an underlying proxy is configured, DNS resolution of the target proxy's hostname happens remotely, so the `ip-version` parameter has no effect.
* `underlying-proxy` cannot be combined with the `port-hopping` parameter of QUIC-based protocols.
* To chain every member of a policy group at once — including members imported from a subscription — use the group-level [`underlying-proxy` parameter](../policy-groups/parameters.md#underlying-proxy) instead of editing individual policies.
