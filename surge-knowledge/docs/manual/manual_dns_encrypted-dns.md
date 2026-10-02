# Encrypted DNS

Surge can send DNS queries over encrypted transports (DoH, DoH3, DoQ, DoT) instead of plain UDP. Configure the `encrypted-dns-server` parameter in the `[General]` section with one or more server URLs.

```
[General]
encrypted-dns-server = https://8.8.8.8/dns-query
```

You may specify multiple servers, separated by commas. All of them are queried concurrently and the first answer wins.

If encrypted DNS is configured, traditional DNS servers are only used to test connectivity and to resolve the hostnames in the encrypted DNS URLs themselves; all other domains are resolved through the encrypted servers. This bootstrap exemption also covers hostnames in encrypted DNS URLs used by `[Host]` `server:` items.

## Supported Protocols

| URL scheme | Protocol | Default port |
|---|---|---|
| `https://` | DNS over HTTPS (DoH) | 443 |
| `h3://` | DNS over HTTP/3 (DoH3) | 443 |
| `quic://` | DNS over QUIC (DoQ) | 853 |
| `tls://` | DNS over TLS (DoT) | 853 |
| `tcp://` | Traditional DNS over TCP | 53 |

{% hint style='info' %}
`tcp://` is **not** encrypted — it sends plain DNS queries over a persistent TCP connection. It is handled by the same subsystem as the encrypted transports, so all options on this page apply to it as well. A `tcp://` URL may only contain a host and an optional port. See also [DNS Servers](dns-server.md).
{% endhint %}

The special value `off` disables encrypted DNS. It is mainly useful in per-network overrides: the `[SSID Setting]` section accepts an `encrypted-dns-server` parameter to replace or disable the global value on a specific network. See [SSID Setting](../features/subnet-settings.md).

```
[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=off
```

## Use Encrypted DNS for Specified Domains

You can assign an encrypted DNS server to specific domains with a `server:` mapping in the `[Host]` section, while other domains keep using the normal servers.

```
[Host]
example.com = server:https://cloudflare-dns.com/dns-query
```

See [Local DNS Mapping](local-dns-mapping.md) for the full `[Host]` syntax.

## Parameters

#### encrypted-dns-skip-cert-verification

Optional, Boolean, default: false

Skip the server certificate verification for all encrypted DNS connections. This is insecure; use it only for testing.

#### encrypted-dns-follow-outbound-mode

Optional, Boolean, default: false

By default, encrypted DNS connections always use the DIRECT policy and bypass the rule system.

When enabled, encrypted DNS connections follow the outbound mode settings and are matched against the rules like normal requests. You can then configure a rule for the DNS server's hostname to use a proxy, or match the connections with a [PROTOCOL rule](../rules/protocol-and-network.md):

- `PROTOCOL,DOH` — DNS over HTTPS (`https://`)
- `PROTOCOL,DOH3` — DNS over HTTP/3 (`h3://`)
- `PROTOCOL,DOQ` — DNS over QUIC (`quic://`)
- `PROTOCOL,DOT` — DNS over TLS (`tls://`)
- `PROTOCOL,DNS` — DNS over TCP (`tcp://`)

{% hint style='info' %}
If an encrypted DNS connection matches a proxy policy whose server is itself configured with a domain name, resolving that domain would require DNS and create a loop. Surge logs a warning and falls back to DIRECT for the DNS connection in this case. To avoid the fallback, use an IP address as the proxy's server address, or add a `[Host]` IP mapping for the proxy's domain.
{% endhint %}
