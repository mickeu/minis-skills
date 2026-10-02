# MASQUE {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

MASQUE is a standardized proxy mechanism built on HTTP/3 (RFC 9298). Surge relays TCP connections as HTTP/3 CONNECT tunnels multiplexed over a single QUIC connection, and forwards UDP packets with the CONNECT-UDP protocol using HTTP Datagrams (RFC 9297). Any standards-compliant MASQUE server can be used.

```
[Proxy]
Proxy-MASQUE = masque, example.com, 443, username=user, password=pass
```

Declaration syntax:

```
Name = masque, <host>, <port>[, parameter=value, ...]
```

## Parameters

#### username / password

Optional. Credentials for proxy authentication, sent as HTTP Basic authorization with each CONNECT request. When omitted, no authorization header is sent.

#### port-hopping

Optional.

Configure a list of ports or ranges, separated by semicolons (for example `1234;5000-6000`). Surge periodically rotates among them instead of using the main port. When this parameter is set, the primary port in the declaration is ignored.

Port hopping cannot be combined with the `underlying-proxy` parameter.

#### port-hopping-interval

Optional. In seconds. Default: 30.

The interval for rotating among the configured ports.

## Notes

* UDP relay is supported without any extra parameter. The server must advertise support for extended CONNECT and HTTP Datagrams; Surge verifies this when the connection is established. See [UDP Relay](udp.md).
* The default ALPN value is `h3`; use the `alpn` parameter to override it.
* As a QUIC-based protocol, MASQUE enables ECN by default on supported systems. See the `ecn` parameter in [Common Policy Parameters](parameters.md).
* Shadow TLS cannot be combined with QUIC-based protocols.

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `test-url`, and `underlying-proxy`.
* [TLS Parameters](tls.md) — shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.
* [UDP Relay](udp.md)
