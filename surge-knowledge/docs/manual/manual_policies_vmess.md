# VMess

Surge supports the VMess protocol, the proxy protocol of the V2Ray project, including the AEAD handshake, optional TLS, and WebSocket transport.

```
[Proxy]
Proxy-VMess = vmess, 1.2.3.4, 8000, username=0233d11c-15a4-47d3-ade3-48ffca0ce119
```

Declaration syntax:

```
Name = vmess, <host>, <port>, username=<UUID>[, parameter=value, ...]
```

VMess supports UDP relay. No parameter is required; UDP forwarding is available automatically.

### Parameters

#### username

Required.

The VMess user ID. It must be a valid UUID.

#### encrypt-method

Optional, `aes-128-gcm` or `chacha20-ietf-poly1305`, default: `aes-128-gcm`.

The data encryption method.

#### vmess-aead

Optional, Boolean, default: false.

Use the VMess AEAD handshake instead of the legacy handshake. It must match the server's setting.

#### tls

Optional, Boolean, default: false.

Connect to the server over TLS. When enabled, the [TLS parameters](tls.md) also apply.

#### ws

Optional, Boolean, default: false.

Use the WebSocket transport layer.

#### ws-path

Optional, default: `/`.

The path used for the WebSocket handshake. It must start with `/`.

#### ws-headers

Optional.

Extra headers for the WebSocket handshake, as pipe-separated `Header:Value` pairs:

```
Proxy-VMess = vmess, 1.2.3.4, 8000, username=0233d11c-15a4-47d3-ade3-48ffca0ce119, ws=true, ws-path=/v2, ws-headers=Host:example.com|X-Token:abc
```

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. With `tls=true`, the [TLS parameters](tls.md) apply, such as `sni`, `skip-cert-verify`, and `client-cert`. For details on UDP forwarding behavior, see [UDP Relay](udp.md).
