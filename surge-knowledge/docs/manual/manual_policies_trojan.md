# Trojan

Surge supports the Trojan protocol, a proxy protocol that disguises traffic as ordinary TLS connections. Trojan always connects over TLS, so it pairs naturally with a real certificate on port 443.

```
[Proxy]
Proxy-Trojan = trojan, 192.168.20.6, 443, password=password1
```

Declaration syntax:

```
Name = trojan, <host>, <port>, password=<password>[, parameter=value, ...]
```

Trojan supports UDP relay. No parameter is required; UDP forwarding is available automatically.

### Parameters

#### password

Required.

The password. It must match the server's setting.

#### ws

Optional, Boolean, default: false.

Use the WebSocket transport layer.

#### ws-path

Optional, default: `/`.

The path used for the WebSocket handshake. It must start with `/`.

#### ws-headers

Optional.

Extra headers for the WebSocket handshake, as pipe-separated `Header:Value` pairs, for example `ws-headers=Host:example.com|X-Token:abc`.

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Since Trojan always connects over TLS, the [TLS parameters](tls.md) also apply, such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see [UDP Relay](udp.md).
