# Hysteria 2 {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

Hysteria 2 is a proxy protocol built on QUIC, designed for high throughput on lossy networks. It always encrypts traffic with TLS over QUIC and supports both TCP and UDP relay with connection multiplexing.

```
[Proxy]
Proxy-Hysteria = hysteria2, 192.168.20.6, 443, password=pwd, download-bandwidth=100
```

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

#### salamander-password {{ book.VER | replace("%TEXT%", "Mac 6.4.3+") }}

Optional. Enable Salamander obfuscation using the specified password.

Cannot be combined with `gecko-password`; the two obfuscation modes are mutually exclusive.

#### gecko-password {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

Optional. Enable Gecko obfuscation using the specified password.

Cannot be combined with `salamander-password`; the two obfuscation modes are mutually exclusive.

## Notes

* UDP relay is always supported; no extra parameter is needed. See [UDP Relay](udp.md).
* The default ALPN value is `h3`; use the `alpn` parameter to override it.
* As a QUIC-based protocol, Hysteria 2 enables ECN by default on supported systems. See the `ecn` parameter in [Common Policy Parameters](parameters.md).

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.
* [TLS Parameters](tls.md) — shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.
* [UDP Relay](udp.md)
