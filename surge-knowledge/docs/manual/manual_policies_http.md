# HTTP, HTTPS, and HTTP/2 CONNECT Proxy

Surge supports the standard HTTP proxy family: plain HTTP proxy (`http`), HTTP proxy over TLS (`https`), and HTTP/2 CONNECT proxy (`h2-connect`). Use these types when connecting to a standard proxy server such as Squid, TinyProxy, or another Surge-compatible HTTP proxy endpoint.

```
[Proxy]
ProxyHTTP = http, 1.2.3.4, 443, username, password
ProxyHTTPS = https, 1.2.3.4, 443, username, password
ProxyH2 = h2-connect, example.com, 443
```

Declaration syntax:

```
Name = http, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = https, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = h2-connect, <host>, <port>[, parameter=value, ...]
```

The `https` and `h2-connect` {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }} types always connect over TLS. HTTP/2 CONNECT multiplexes multiple requests over a single TCP connection.

The `http` and `https` types do not support UDP relay. The `h2-connect` type supports it with the opt-in `udp-relay` parameter. {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

### Parameters

#### username / password

Optional.

Credentials for proxy authentication. They may be given positionally after the port, or as named parameters:

```
ProxyH2 = h2-connect, example.com, 443, username=user, password=pass
```

#### always-use-connect

Optional, Boolean, default: false.

Always use the HTTP CONNECT method to relay the request, even for plain HTTP requests. Applies to `http` and `https` only.

#### headers {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }}

Optional.

Add custom request headers to proxy handshake requests. Multiple headers are separated by semicolons.

```
Proxy = http, example.com, 8080, headers=X-Client:Surge;X-Token:abc
Proxy = h2-connect, example.com, 443, headers=X-Padding:<random-string(16-32)>
```

The value supports `<random-string(n)>` and `<random-string(min-max)>` placeholders. Surge generates a URL-safe random string when connecting, which can be used for dynamic padding or request fingerprint perturbation.

For HTTP and HTTPS proxy policies, a configured header replaces an original field with the same name, including the `Host` field. {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

#### max-streams {{ book.VER | replace("%TEXT%", "Mac 6.6.0+") }}

Optional, default: 3.

For `h2-connect` only. Control the maximum number of multiplexed sub-connections over the same TCP connection. A large value may hurt performance in some environments.

#### udp-relay {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

Optional, Boolean, default: false.

For `h2-connect` only. Relay UDP packets through the proxy using the standard CONNECT-UDP protocol (RFC 9298) over HTTP/2 extended CONNECT (RFC 8441), with UDP payloads carried as capsules on the stream (RFC 9297).

```
ProxyH2 = h2-connect, example.com, 443, udp-relay=true
```

Since most plain HTTP/2 CONNECT servers do not implement extended CONNECT, the feature is off by default; enable it only when the server supports it. The server must advertise extended CONNECT support in its HTTP/2 settings, which Surge verifies when the connection is established.

Unlike QUIC-based protocols, HTTP/2 runs over TCP, so relayed UDP packets are delivered reliably and in order. Packet loss on the path to the proxy is repaired by TCP retransmission instead of being surfaced to the application, which may affect protocols that rely on native UDP loss behavior.

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since `https` and `h2-connect` connect over TLS, they also accept the [TLS parameters](tls.md), such as `sni`, `skip-cert-verify`, and `client-cert`.
