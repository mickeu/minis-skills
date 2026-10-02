# UDP Relay

Surge processes UDP traffic with the same rule system as TCP. When UDP traffic matches a rule that resolves to a proxy policy, the policy must support UDP relay to forward it. This page lists which protocols support UDP relay and the related parameters.

## Protocol Support

| Protocol | UDP relay |
| --- | --- |
| SOCKS5 / SOCKS5-TLS | Yes, requires `udp-relay=true` |
| Shadowsocks | Yes, requires `udp-relay=true` |
| Snell | Yes, version 3 and above (automatic) |
| VMess | Yes |
| Trojan | Yes |
| TUIC | Yes |
| Hysteria 2 | Yes |
| MASQUE | Yes |
| AnyTLS | Yes |
| WireGuard | Yes |
| Tailscale | Yes |
| External Proxy Program (Mac) | Yes, requires `udp-relay=true` |
| HTTP / HTTPS | No |
| HTTP/2 CONNECT | Yes, requires `udp-relay=true` {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }} |
| Trust Tunnel | No |
| SSH | No |

The built-in DIRECT and REJECT policy families always handle UDP traffic.

## Parameters

#### udp-relay

Optional, boolean, default: false. Applies to SOCKS5, SOCKS5-TLS, Shadowsocks, External Proxy Program, and HTTP/2 CONNECT policies.

Since UDP relay is an optional feature for these servers, it must be enabled explicitly:

```
[Proxy]
ProxySOCKS5 = socks5, 1.2.3.4, 1080, username, password, udp-relay=true
ProxySS = ss, 1.2.3.4, 8388, encrypt-method=chacha20-ietf-poly1305, password=pwd, udp-relay=true
ProxyH2 = h2-connect, example.com, 443, udp-relay=true
```

For HTTP/2 CONNECT policies, UDP is relayed with the standard CONNECT-UDP protocol; see [the `udp-relay` parameter in HTTP proxy parameters](http.md#udp-relay) for the server requirements. {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

#### udp-port {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

Optional, port number, default: the main server port. Applies to Shadowsocks and Snell policies.

Use another server port when performing UDP forwarding. This can be used when the server's TCP and UDP services do not listen on the same port, for example when [Shadow TLS](tls.md#shadow-tls) occupies the TCP port.

## Behavior for Unsupported Policies

When UDP traffic matches a policy that does not support UDP relay, the fallback behavior is controlled by the `udp-policy-not-supported-behaviour` option in the [\[General\] section](../profile/general.md). Possible values are `DIRECT` and `REJECT`. Starting from Surge Mac 6.0.0, the default is `REJECT` to avoid leaking traffic unknowingly.

## UDP Testing

Latency tests only measure the TCP path. To test a policy's UDP relay, Surge performs a DNS lookup through the relay, configured as `hostname@server-ip`:

* The global default endpoint is set by `proxy-test-udp` in the [\[General\] section](../profile/general.md), e.g. `proxy-test-udp = apple.com@8.8.8.8`.
* The per-policy [`test-udp` parameter](parameters.md#test-udp) overrides the global setting, e.g. `test-udp=google.com@1.1.1.1`.
