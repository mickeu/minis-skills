# TLS Parameters

All proxy protocols carried over TLS or QUIC share a common set of TLS parameters: HTTPS, SOCKS5-TLS, HTTP/2 CONNECT, Trust Tunnel, Trojan, TUIC, Hysteria 2, AnyTLS, and VMess with `tls=true`. This page also covers the Shadow TLS obfuscation layer, which can wrap most TCP-based protocols.

```
[Proxy]
Proxy = https, example.com, 443, sni=cdn.example.com, server-cert-verify-name=example.com
```

## Parameters

#### skip-cert-verify

Optional, boolean, default: false.

If enabled, Surge does not verify the server's certificate. Use with caution: it allows man-in-the-middle attacks on the proxy connection.

#### sni

Optional, hostname or `off`, default: the proxy hostname.

Customize the Server Name Indication (SNI) sent during the TLS handshake. By default, Surge sends the SNI using the hostname like most browsers. Use `sni=off` to turn off SNI completely.

#### server-cert-verify-name {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Optional, hostname.

Specify the hostname used to verify the proxy server certificate independently from SNI. This is useful when the TLS endpoint needs one SNI value but its certificate must be verified against another name. It applies to all TLS- and QUIC-based proxy protocols.

#### server-cert-fingerprint-sha256

Optional, SHA-256 fingerprint (64 hexadecimal characters).

Use a pinned server certificate instead of the standard X.509 validation.

#### alpn {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

Optional, comma-separated protocol list (quote the value if it contains multiple entries).

Customize the ALPN value used during the TLS handshake. It must match a protocol supported by the proxy server. When unset, TUIC and Hysteria 2 use `h3` by default.

#### client-cert

Optional, the name of a `[Keystore]` item.

Use a client certificate for mutual TLS authentication. The certificate is stored in the [\[Keystore\] section](../profile/keystore.md):

```
[Proxy]
Proxy = https, example.com, 443, client-cert=cert1

[Keystore]
cert1 = base64=<P12 base64 string here>, password=123456
```

## Shadow TLS

[Shadow TLS](https://github.com/ihciah/shadow-tls) is a proxy obfuscator that can wrap TCP-based proxy protocols. Starting from Surge iOS 5.2.0 and Surge Mac 4.10.0, Surge supports the Shadow TLS v2 protocol. Append `shadow-tls-password` to a proxy declaration to enable it:

```
[Proxy]
STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2
```

Starting from Surge iOS 5.5.0 and Surge Mac 5.0.3, Surge supports the Shadow TLS v3 protocol:

```
STLS-SNELL = snell, 1.2.3.4, 443, psk=pwd1, version=4, reuse=true, shadow-tls-password=pwd2, shadow-tls-version=3, shadow-tls-sni=example.com
```

Shadow TLS cannot be combined with TUIC, WireGuard, or Tailscale policies; attempting to do so is a configuration error. As a TCP-based wrapper, it is also not meaningful for other QUIC-based protocols.

#### shadow-tls-password

Required. It must match the server's setting.

#### shadow-tls-sni

Optional, hostname. Required when `shadow-tls-version=3`.

The SNI sent to the server during the Shadow TLS handshake in plain text. If not set, no SNI is sent.

#### shadow-tls-version

Optional, `2` or `3`, default: 2.

The Shadow TLS protocol version.
