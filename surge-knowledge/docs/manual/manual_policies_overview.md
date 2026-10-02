# Policies

A policy tells Surge how to handle a request once a rule has matched it: connect directly, reject it, or forward it to a proxy server. Every rule ends with a policy name, and the [FINAL rule](../rules/final.md) picks the policy for all unmatched requests.

There are three kinds of policies:

* **Built-in policies**: predefined policies such as `DIRECT` and `REJECT`. See [Built-in Policies](built-in.md) and the [REJECT family](reject.md).
* **Proxy policies**: forward the request to a proxy server. Declared in the `[Proxy]` section.
* **Policy groups**: select one policy from a set of policies, manually or automatically. See [Policy Groups](../policy-groups/overview.md).

## The [Proxy] Section

Each line in the `[Proxy]` section declares one proxy policy:

```
Name = <type>, <arguments...>, key1=value1, key2=value2
```

For all server-based proxy types, the first two arguments are the server hostname and port. The remaining parameters are written as `key=value` pairs. Quote a value if it contains commas.

```
[Proxy]
ProxyHTTPS = https, 1.2.3.4, 443, username, password
ProxySS = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd
ProxySnell = snell, 1.2.3.4, 8000, psk=pwd, version=5
```

## Referencing Policies

A policy name can be used anywhere a policy is accepted:

* As the target of a rule: `DOMAIN-SUFFIX,example.com,ProxySS`
* As a member of a [policy group](../policy-groups/overview.md): `Group = select, ProxySS, ProxySnell, DIRECT`
* As the value of the [`underlying-proxy` parameter](parameters.md#proxy-chain) to build a proxy chain.

## Supported Proxy Protocols

| Type keyword | Protocol | Notes |
| --- | --- | --- |
| `http` / `https` | [HTTP / HTTPS](http.md) | HTTPS = HTTP proxy over TLS |
| `h2-connect` | [HTTP/2 CONNECT](http.md) | {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }} |
| `socks5` / `socks5-tls` | [SOCKS5 / SOCKS5-TLS](socks5.md) | |
| `ss` | [Shadowsocks](shadowsocks.md) | |
| `snell` | [Snell](snell.md) | Versions 1–6 |
| `vmess` | [VMess](vmess.md) | |
| `trojan` | [Trojan](trojan.md) | |
| `tuic` / `tuic-v5` | [TUIC](tuic.md) | QUIC-based |
| `hysteria2` | [Hysteria 2](hysteria2.md) | QUIC-based {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }} |
| `masque` | [MASQUE](masque.md) | QUIC-based {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }} |
| `anytls` | [AnyTLS](anytls.md) | {{ book.VER | replace("%TEXT%", "iOS 5.17.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.4.3+") }} |
| `trust-tunnel` | [Trust Tunnel](trust-tunnel.md) | {{ book.VER | replace("%TEXT%", "Mac 6.4.4+") }} |
| `ssh` | [SSH](ssh.md) | |
| `wireguard` | [WireGuard](wireguard.md) | L3 VPN as proxy |
| `tailscale` | [Tailscale](tailscale.md) | {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }} |
| `external` | [External Proxy Program](external.md) | {{ book.VER | replace("%TEXT%", "Mac Only") }} |

The built-in type keywords `direct`, `reject`, `reject-drop`, `reject-no-drop`, and `reject-tinygif` may also appear in the `[Proxy]` section to define aliases of the built-in policies. See [Built-in Policies](built-in.md#alias).

## Shared Parameters

Besides the protocol-specific parameters documented on each protocol page, several parameter groups are shared across policy types:

* [Common Policy Parameters](parameters.md): egress control (`interface`, `ip-version`, `tfo`, ...), testing (`test-url`, ...), and proxy chaining (`underlying-proxy`).
* [TLS Parameters](tls.md): parameters shared by TLS- and QUIC-based protocols, plus Shadow TLS obfuscation.
* [UDP Relay](udp.md): UDP protocol support matrix and related parameters.
