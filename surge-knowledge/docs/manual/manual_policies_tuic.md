# TUIC

TUIC is a proxy protocol built on QUIC. It always encrypts traffic with TLS over QUIC and supports both TCP and UDP relay with connection multiplexing.

Surge supports two protocol versions with different type keywords:

* `tuic` — TUIC v4, which authenticates with a token.
* `tuic-v5` — TUIC v5, which authenticates with a UUID and password pair.

Use the keyword that matches your server's protocol version: v4 servers use `token`, and v5 servers use `uuid` + `password`. The two versions are not interchangeable.

```
[Proxy]
Proxy-TUIC = tuic, 192.168.20.6, 443, token=pwd, alpn=h3
Proxy-TUIC-v5 = tuic-v5, 192.168.20.6, 443, uuid=0233d11c-15a4-47d3-ade3-48ffca0ce119, password=pwd, alpn=h3
```

## Parameters

#### token

Required for `tuic` (v4). The authentication token, which must match the server's setting. Not used by `tuic-v5`.

#### uuid

Required for `tuic-v5`. The user UUID, in the standard hyphenated form. Not used by `tuic` (v4).

#### password

Required for `tuic-v5`. The password paired with the UUID. Not used by `tuic` (v4).

#### alpn

Optional. Default: h3.

Customize the ALPN value used during the QUIC-TLS handshake. It must match the server's ALPN setting.

#### port-hopping

Optional. Rotate among a list of ports or ranges instead of the main port. Behaves the same as for [Hysteria 2](hysteria2.md#port-hopping).

Port hopping cannot be combined with the `underlying-proxy` parameter.

#### port-hopping-interval

Optional. In seconds. Default: 30. The interval for rotating among the configured ports — see [Hysteria 2](hysteria2.md#port-hopping).

## Notes

* UDP relay is always supported; no extra parameter is needed. See [UDP Relay](udp.md).
* As a QUIC-based protocol, TUIC enables ECN by default on supported systems. See the `ecn` parameter in [Common Policy Parameters](parameters.md).
* Shadow TLS cannot be used with TUIC policies.

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.
* [TLS Parameters](tls.md) — shared TLS parameters such as `skip-cert-verify`, `sni`, and certificate pinning.
* [UDP Relay](udp.md)
