# SOCKS5 Proxy

Surge supports the standard SOCKS5 proxy protocol (`socks5`) and SOCKS5 over TLS (`socks5-tls`). SOCKS5 is a simple, widely supported protocol; use `socks5-tls` when the server wraps the SOCKS5 session in TLS for transport security.

```
[Proxy]
ProxySOCKS5 = socks5, 1.2.3.4, 443, username, password
ProxySOCKS5TLS = socks5-tls, 1.2.3.4, 443, username, password, skip-cert-verify=false
```

Declaration syntax:

```
Name = socks5, <host>, <port>[, <username>, <password>][, parameter=value, ...]
Name = socks5-tls, <host>, <port>[, <username>, <password>][, parameter=value, ...]
```

### Parameters

#### username / password

Optional.

Credentials for SOCKS5 username/password authentication. They may be given positionally after the port, or as named parameters.

#### udp-relay

Optional, Boolean, default: false.

Enable UDP relay with the SOCKS5 UDP ASSOCIATE command. Since UDP relay is an optional feature of the SOCKS5 protocol and the server may not support it, you must enable it explicitly.

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since `socks5-tls` connects over TLS, it also accepts the [TLS parameters](tls.md), such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see [UDP Relay](udp.md).
