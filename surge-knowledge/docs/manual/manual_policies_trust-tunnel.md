# Trust Tunnel {{ book.VER | replace("%TEXT%", "Mac 6.4.4+") }}

Trust Tunnel is a TLS-based proxy protocol developed and maintained by AdGuard. Surge relays TCP connections as multiplexed streams over an HTTP/2 connection, or over HTTP/3 with the `h3` parameter. UDP forwarding is not supported.

```
[Proxy]
Proxy-TrustTunnel = trust-tunnel, 192.168.20.62, 443, username=test, password=test
```

## Parameters

#### username

Required. The username for authentication.

#### password

Required. The password for authentication.

#### headers {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }}

Optional. Add custom request headers to proxy handshake requests, with the same syntax and `<random-string>` placeholder support as for HTTP proxies. See [HTTP proxy parameters](http.md) for the full description.

```
Proxy = trust-tunnel, example.com, 443, username=test, password=test, headers=X-Padding:<random-string(16-32)>
```

#### max-streams {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }}

Optional. Default: 3. The maximum number of multiplexed sub-connections over the same TCP connection. See [HTTP proxy parameters](http.md) for details.

#### h3 {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

Optional, Boolean, default: false.

Run the tunnel over HTTP/3 (QUIC) instead of HTTP/2 over TLS. The server must support the HTTP/3 transport.

```
Proxy = trust-tunnel, example.com, 443, username=test, password=test, h3=true
```

Cannot be combined with the `ws` (WebSocket) parameter.

## Notes

* Trust Tunnel always encrypts traffic with TLS; all shared TLS parameters apply.
* UDP relay is not supported. See [UDP Relay](udp.md) for how Surge handles UDP requests matched to a policy without UDP support.

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.
* [TLS Parameters](tls.md) — shared TLS parameters such as `skip-cert-verify`, `sni`, `alpn`, and certificate pinning.
* [UDP Relay](udp.md)
