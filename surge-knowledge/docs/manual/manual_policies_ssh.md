# SSH

Surge can use the SSH protocol as a proxy policy, an equivalent to `ssh -D`. Surge multiplexes requests as channels over a single SSH session.

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw
```

## Authentication

Either `password` or `private-key` must be provided.

* Password authentication:

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw
```

* Public key authentication, with the private key stored in the [Keystore](../profile/keystore.md) section:

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, private-key=key1

[Keystore]
key1 = type=openssh-private-key, base64=[The base64 encoded content of the private key file]
```

You must use base64 to encode the entire private key file again, even though the private key file uses the base64 encoding itself.

All four types of private keys, RSA/ECDSA/ED25519/DSA, are supported. ECDSA P-521 private keys can be imported starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

## Parameters

#### username

Required. The SSH login user.

#### password

The password for authentication. Required unless `private-key` is used.

#### private-key

The name of an item in the [Keystore](../profile/keystore.md) section containing an OpenSSH private key. Required unless `password` is used.

#### idle-timeout

Optional. In seconds. Default: 180.

Tear down the SSH connection after it has been idle for this long.

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180
```

#### server-fingerprint

Optional. Pin the server's public key fingerprint. See [Pinning the Server Fingerprint](#pinning-the-server-fingerprint) below.

## Algorithm Requirements

Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. It means that the SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)

## Pinning the Server Fingerprint

To cope with MITM attacks, you can specify the server's public key fingerprint with `server-fingerprint`, which ensures that only legitimate servers are connected.

Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, Surge emits a one-time security warning when connecting without a configured fingerprint. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

```
[Proxy]
proxy = ssh, 1.2.3.4, 22, username=root, password=pw, idle-timeout=180, server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz"
```

As there may be multiple public keys for a server, the `server-fingerprint` parameter supports configuring multiple fingerprints, separated by commas.

```
server-fingerprint = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBk2No6KBq2m9VTCcHXXJBX4/A3RNr+L+yDBl5+TF9qz,ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7aoFCymj8NJL+xMqYzRLGpIfVd2sebgtnD3cplG7/lrvPGYIpRAOkKqdUBOkRd2x68JFe0u+gBHQxFkv8o81Saqr6qxcrq4mPiyqxOTRkvDMtYrjJ4AJZE26nCzHRCC7Ji6Mq2OtepTJcC9uk2LLcRrF3G05qu6ToeK1LgXgqc+b2RLOQJ1AXEeNgn0NIXWlBv4AhQRJ6fFQi4HO/jkxpFNfzKY+dPDx6P3VAazYa2nl8wpLbXt+tq6SBv8RctwDuYszAbjSCPPJq7ToX/Svqqbl82qtOLOofcQ8/f8809i4RQ0yuEpVLnVVWd7cZx5h45vt+/I1Ifr2pS7BqhLL/,ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLdhR3D2BvyD7FTXfx0CrjZF2tVgoVRFi1poGKoX0eXc9OlpiaqNos4niiN0GWyoT4mL724cgvaL+vHW8sTZE5A="
```

{% hint style="info" %}
If the server's sshd supports ed25519, only the fingerprint of ssh-ed25519 is needed.
{% endhint %}

You may obtain the server fingerprint from the `~/.ssh/known_hosts` file. Or you may use the command `ssh-keyscan example.com` in a trusted network environment to fetch it. Remove the hostname at the front of the line before copying it to Surge.

## Notes

* UDP relay is not supported. See [UDP Relay](udp.md) for how Surge handles UDP requests matched to a policy without UDP support.

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, `test-url`, and `underlying-proxy`.
* [Keystore](../profile/keystore.md) — storing private keys and certificates.
* [UDP Relay](udp.md)
