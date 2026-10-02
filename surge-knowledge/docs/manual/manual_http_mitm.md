# HTTPS Decryption (MITM)

Surge can decrypt HTTPS traffic with a man-in-the-middle (MITM) attack, so that the [HTTP processing features](overview.md) can work on HTTPS requests. See the [Wikipedia article](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) for background on the technique.

A minimal configuration looks like this:

```
[MITM]
ca-p12 = MIIJtQ.........
ca-passphrase = password
hostname = *.google.com
h2 = true
```

Surge only decrypts traffic to hosts declared in `hostname`.

## CA certificate

To perform MITM, Surge needs a CA certificate that the system trusts.

The certificate generator can generate a new CA certificate for debugging and make it trusted by the system. It is available in Surge Dashboard (Mac version) and the Surge iOS Config Editor. The certificate is generated locally and saved only in your profile and the system Keychain. The key of the new certificate is generated randomly using OpenSSL.

You can also use an existing CA certificate. Export the certificate to PKCS#12 format (.p12) with a passphrase. The passphrase cannot be empty due to system limitations. Use the `base64` command to encode the certificate, then set `ca-p12` and `ca-passphrase` in the profile.

{% hint style='info' %}
Some applications use certificate pinning and refuse any certificate not issued by the expected CA. Enabling decryption for these hosts breaks their connections. If a client completes the TLS handshake but disconnects without sending a request, Surge logs a hint that the host is likely protected by certificate pinning.
{% endhint %}

## Parameters

#### `hostname`: Host List

The list of hosts to decrypt. This parameter is of the [Host List parameter type](../profile/host-list.md); the default port is 443:

* Wildcards `*` and `?` are supported.
* Use the `-` prefix to exclude a host. Items are matched in order, so put exclusions first: `hostname = -*.apple.com, -*.icloud.com, *` decrypts everything except Apple and iCloud hosts.
* A bare `example.com` entry matches port 443 only. Use `example.com:8443` to match another port, or `example.com:0` to match all ports.
* For TLS or QUIC connections identified by the sniffed SNI, a bare entry matches regardless of the connection's actual port. So a plain `example.com` entry still decrypts TLS traffic to that host on non-standard ports as long as the SNI is visible.
* Special tokens like `<ip-address>` and `<simple-hostname>` are available; see the [Host List](../profile/host-list.md) reference.

An invalid entry in the list produces a profile warning instead of a parse error, so a single typo does not prevent the profile from loading.

#### `hostname-disabled`: Optional, Host List

Entries in this list are removed from the effective `hostname` list. Surge's UI uses this key to temporarily disable a hostname without deleting it from the profile; you may also edit it manually.

#### `ca-p12`: Optional, string

The CA certificate and private key in PKCS#12 format, base64-encoded.

#### `ca-passphrase`: Optional, string

The passphrase of the PKCS#12 data. It cannot be empty due to system limitations.

#### `ca-keystore-name`: Optional, string

Use a certificate stored in the [Keystore section](../profile/keystore.md) instead of an inline `ca-p12`. The value is the name of a Keystore item of p12 type. When set, it takes precedence over `ca-p12`.

#### `skip-server-cert-verify`: Optional, Boolean, default: false

Do not verify the certificate of the remote server while performing MITM. This relaxes verification of the real server only; the client side still receives the Surge-generated certificate.

#### `h2`: Optional, Boolean, default: false

MITM over HTTP/2: decrypt HTTPS traffic with MITM over the HTTP/2 protocol, which can improve the performance of concurrent requests.

#### `client-source-address`: Optional, list

Enable the MITM function for specific client devices only.

* This is a list parameter using commas as the separator.
* You may specify a single IP address or use a CIDR block. Both IPv4 and IPv6 are supported.
* You may use the `-` prefix to exclude some clients, e.g. `client-source-address = -192.168.1.2, 0.0.0.0/0`.
* If the parameter is not set, MITM is enabled for all clients. This is equivalent to `client-source-address = 0.0.0.0/0, ::/0`.
* `127.0.0.1` should be included if you want to enable MITM for the current device.
* Since Surge Mac version 6.1.0, this parameter can use MAC addresses to match specific clients.

#### `auto-quic-block`: Optional, Boolean, default: true {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

When a QUIC connection (i.e. HTTP/3) hits the MITM hostname list, Surge automatically blocks that QUIC connection, causing the client to fall back to HTTP/2 or HTTP/1.1 so the traffic can be intercepted by MITM.
