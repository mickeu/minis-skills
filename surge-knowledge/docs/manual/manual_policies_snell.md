# Snell

Snell is a lean encrypted proxy protocol designed by the Surge team for maximum performance and simplicity. Surge supports protocol versions 1 through 6. See the [Snell knowledge base](https://kb.nssurge.com/surge-knowledge-base/release-notes/snell) for server downloads and release notes.

```
[Proxy]
Proxy-Snell = snell, 1.2.3.4, 8000, psk=password, version=4
```

Declaration syntax:

```
Name = snell, <host>, <port>, psk=<psk>, version=<n>[, parameter=value, ...]
```

Surge Mac also ships a [built-in Snell server](../features/snell-server.md) that accepts incoming Snell connections.

### Parameters

#### psk

Required.

The pre-shared key. It must match the server's setting.

#### version

Optional, 1–6, default: 1.

The Snell protocol version. It must match the server version. Always declare it explicitly; when omitted, Surge assumes the legacy v1 protocol.

#### reuse

Optional, Boolean, default: false.

Enable connection reuse. Only meaningful for v4 and later; Snell v2 always reuses connections, and v1/v3 never do.

#### obfs

Optional.

Enable traffic obfuscation. Availability depends on the protocol version:

* v1–v3: `http` or `tls`
* v4 and v5: `http` only
* v6: obfuscation is not supported

#### obfs-host

Optional.

The hostname used in the obfuscation handshake.

#### obfs-uri

Optional.

The URI used in the obfuscation request. Only meaningful with `obfs=http`.

#### udp-port

Optional.

When performing UDP forwarding, use another server port number. This can be used when the server's TCP and UDP services do not listen on the same port.

#### mode

Optional, `default` | `unshaped` | `unsafe-raw`, default: `default`. Snell v6 only.

Select the transport mode. The value must match the `mode` setting of the Snell v6 server:

* `default`: The standard mode with encryption and PSK-derived traffic shaping. Use it for normal deployments.
* `unshaped`: Keep encryption but disable traffic shaping.
* `unsafe-raw`: Disable both traffic shaping and encryption. As the name suggests, this mode provides no confidentiality; only use it for debugging or inside an already-secured tunnel.

Setting `mode` on a policy with a version lower than 6 is a profile error.

### UDP Relay

Snell supports UDP relay with protocol version 3 and later. No parameter is required; UDP forwarding is available automatically.

With `version=5`, Surge automatically uses QUIC Proxy Mode when relaying QUIC traffic, which converts the QUIC transport instead of tunneling it datagram by datagram. This is a runtime behavior with no profile parameter.

### Snell v6 {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

Set `version=6` to use Snell v6:

```
Proxy-Snell-v6 = snell, 1.2.3.4, 8000, psk=password, version=6
```

Snell v6 derives a deployment-specific protocol profile from the PSK automatically, so no obfuscation parameters need to be configured on the client; traffic shaping is derived automatically. The optional `mode` parameter described above can switch the transport to `unshaped` or `unsafe-raw` when the server is configured accordingly. Unlike Snell v5, v6 does not support QUIC Proxy Mode.

The Snell v6 server adds two server-side network controls. These are Snell server configuration items, not Surge proxy-policy parameters:

* `dns-ip-preference`: Controls address-family selection for DNS results. The available values are `default`, `prefer-ipv4`, `prefer-ipv6`, `ipv4-only`, and `ipv6-only`.
* `listen`: Accepts multiple comma-separated listening addresses, for example `listen = 0.0.0.0:7177,[::]:7177`.

Snell v6 is currently in beta and may receive incompatible protocol changes. Keep both the Surge client and the Snell server updated to compatible beta versions. See [Introducing Snell v6](https://nssurge.com/blog/snell-v6/) for design details and the [Snell knowledge base](https://kb.nssurge.com/surge-knowledge-base/release-notes/snell) for server downloads.

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. Snell is also a common companion for [Shadow TLS](tls.md#shadow-tls) obfuscation. For details on UDP forwarding behavior, see [UDP Relay](udp.md).
