# AnyTLS {{ book.VER | replace("%TEXT%", "iOS 5.17.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.4.3+") }}

AnyTLS is a TLS-based proxy protocol designed to mitigate TLS-in-TLS fingerprinting by using flexible traffic padding. Surge supports the AnyTLS v2 protocol.

```
[Proxy]
Proxy-AnyTLS = anytls, 192.168.20.6, 443, password=pwd
```

## Parameters

#### password

Required. The authentication password, which must match the server's setting.

#### reuse

Optional. Boolean. Default: true.

According to the AnyTLS specification, connection reuse is enabled by default. Set `reuse=false` to disable it.

## Notes

* AnyTLS always encrypts traffic with TLS; all shared TLS parameters apply.
* UDP relay is supported (UDP over TCP); no extra parameter is needed. See [UDP Relay](udp.md).

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.
* [TLS Parameters](tls.md) — shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.
* [UDP Relay](udp.md)
