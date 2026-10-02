# DNS Servers

Surge uses the DNS server addresses from the operating system by default. Use the `dns-server` parameter in the `[General]` section to override them.

```
[General]
dns-server = 8.8.8.8, 8.8.4.4
```

## Syntax

The value is a comma-separated list of servers. Each item is one of:

- An IPv4 or IPv6 address, optionally with a port: `1.1.1.1`, `192.0.2.53:5353`, `::1`. The default port is 53. Hostnames are not allowed.
- The keyword `system`, which includes the current system DNS servers together with the other listed servers. Duplicate servers are ignored.

```
[General]
dns-server = system, 8.8.8.8, 8.8.4.4
```

If `dns-server` is not set at all, Surge uses the system DNS servers.

When `ipv6 = false`, IPv6 server addresses are dropped from the list.

All listed servers are queried concurrently and the first answer wins; see [DNS Overview](overview.md) for the full query behavior.

## DNS over TCP {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Prefix a server with `tcp://` to send traditional (unencrypted) DNS queries over TCP with a persistent connection. A hostname may be used in the URL, and the port is optional (default 53).

```
[General]
dns-server = tcp://dns.example.com, tcp://192.0.2.53:5353
```

{% hint style='info' %}
Internally, `tcp://` servers are handled by the same subsystem as encrypted DNS servers. As a result, once any `tcp://` server is configured, plain UDP servers listed alongside it are no longer used for ordinary domains — they are only used to resolve the hostname of the `tcp://` server itself. See [Encrypted DNS](encrypted-dns.md) for details.
{% endhint %}

## Per-Network Overrides

You can use a different set of DNS servers on a specific Wi-Fi network or subnet with the `dns-server` and `encrypted-dns-server` parameters in the `[SSID Setting]` section. These replace the global values while connected to that network. See [SSID Setting](../features/subnet-settings.md).

```
[SSID Setting]
SSID:MyHome dns-server=192.168.1.1
```
