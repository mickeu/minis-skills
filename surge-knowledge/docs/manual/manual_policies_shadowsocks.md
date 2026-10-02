# Shadowsocks

Surge supports the Shadowsocks protocol (`ss`), a popular encrypted proxy protocol, including the Shadowsocks 2022 edition and simple-obfs–style obfuscation.

```
[Proxy]
Proxy-SS = ss, 1.2.3.4, 8000, encrypt-method=chacha20-ietf-poly1305, password=abcd1234
```

Declaration syntax:

```
Name = ss, <host>, <port>, encrypt-method=<method>, password=<password>[, parameter=value, ...]
```

### Parameters

#### encrypt-method

Required.

The encryption method. It must match the server's setting. Supported values:

* AEAD 2022: `2022-blake3-aes-128-gcm`, `2022-blake3-aes-256-gcm`
* AEAD: `aes-128-gcm`, `aes-192-gcm`, `aes-256-gcm`, `chacha20-ietf-poly1305`, `xchacha20-ietf-poly1305`
* Stream (legacy, not recommended): `rc4`, `rc4-md5`, `aes-128-cfb`, `aes-192-cfb`, `aes-256-cfb`, `aes-128-ctr`, `aes-192-ctr`, `aes-256-ctr`, `salsa20`, `chacha20`, `chacha20-ietf`
* `none`

#### password

Required.

The pre-shared password. It is required unless `encrypt-method` is `none`.

For Shadowsocks 2022 methods, the password must be a Base64-encoded key of exactly 16 bytes (`2022-blake3-aes-128-gcm`) or 32 bytes (`2022-blake3-aes-256-gcm`). For identity-based multi-user authentication, use the form `serverKey:userKey` with both parts Base64-encoded keys of the same size.

#### udp-relay

Optional, Boolean, default: false.

Enable UDP relay. Since UDP relay is optional for a Shadowsocks server, you must enable it explicitly.

#### udp-port {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

Optional.

When performing UDP forwarding, use another server port number. This can be used when the server's TCP and UDP services do not listen on the same port, for example, when Shadow TLS occupies the TCP port.

#### obfs

Optional, `http` or `tls`.

Enable simple-obfs–style traffic obfuscation. It must match the server's obfuscation setting.

#### obfs-host

Optional.

The hostname used in the obfuscation handshake.

#### obfs-uri

Optional.

The URI used in the obfuscation request. Only meaningful with `obfs=http`.

{% hint style='info' %}
The legacy `custom` policy type from very old configurations is parsed as a Shadowsocks policy; the external module URL in its declaration is ignored. Use the `ss` type instead.
{% endhint %}

### Common Parameters

All proxy policies accept the [common policy parameters](parameters.md), such as `interface`, `tfo`, `test-url`, and `underlying-proxy`. For details on UDP forwarding behavior, see [UDP Relay](udp.md).
