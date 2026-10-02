# Keystore

The `[Keystore]` section stores certificates and private keys used elsewhere in the profile. Other sections and policies reference a keystore item by its name, keeping the key material in one place.

```
[Keystore]
cert1 = type=p12, base64=<P12 base64 string here>, password=123456
key1 = type=openssh-private-key, base64=<base64 encoded private key file>
```

Each line defines one item: `name = key=value, key=value, ...`

#### type

Optional, `p12` or `openssh-private-key`

The item type. If omitted, an item with a `password` is treated as `p12`; an item without one is treated as `openssh-private-key`.

#### base64

Required, Base64 string

The Base64-encoded content of the certificate or key file: a PKCS#12 (.p12) file for `p12` items, or an OpenSSH private key file for `openssh-private-key` items.

#### password

Optional, string

The password of the PKCS#12 file.

## Client Certificate for TLS Proxy

A `p12` item can act as the client certificate of a TLS-based proxy, referenced with the `client-cert` parameter:

```
[Proxy]
Proxy = https, example.com, 443, client-cert=cert1

[Keystore]
cert1 = base64=<P12 base64 string here>, password=123456
```

See [TLS parameters](../policies/tls.md) for details.

## MITM CA Certificate

A `p12` item can provide the CA certificate and key for HTTPS decryption, referenced with the `ca-keystore-name` parameter in the `[MITM]` section, as an alternative to the inline `ca-p12` parameter. See [MITM](../http/mitm.md).

## SSH Private Key

An `openssh-private-key` item provides the private key for an [SSH policy](../policies/ssh.md), referenced with the `private-key` parameter:

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, private-key=key1

[Keystore]
key1 = type=openssh-private-key, base64=[The base64 encoded content of the private key file]
```

You must Base64-encode the entire private key file again, even though the private key file uses Base64 encoding itself. RSA, ECDSA, ED25519, and DSA keys are supported; see the [SSH policy page](../policies/ssh.md) for details.
