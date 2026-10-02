# MTProto Proxy Server {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Surge can operate as an incoming MTProto proxy server for Telegram. A Telegram client connects to a listening port on Surge and identifies the Telegram data center (DC) it needs. Surge authenticates the proxy transport, maps the requested DC to a current production endpoint, evaluates the connection with the normal rule system, and relays the stream to Telegram.

{% hint style='info' %}
MTProto proxy is a Telegram-specific proxy protocol. It is not a general-purpose proxy such as HTTP or SOCKS5, and it cannot be used by arbitrary applications or to reach arbitrary destinations.
{% endhint %}

{% hint style='info' %}
An MTProto proxy—including Surge—does not possess the client's Telegram authorization keys and cannot decrypt message contents, alter authenticated messages, or impersonate Telegram's servers. Surge handles only the proxy transport layer; the relayed MTProto payload keeps Telegram's normal client-to-DC encryption. For details, see Telegram's [MTProxy](https://core.telegram.org/proxy) and [MTProto](https://core.telegram.org/mtproto) documentation.
{% endhint %}

## Why MTProto Instead of SOCKS5

Telegram clients also support SOCKS5, but a native MTProto listener has important advantages for Telegram traffic:

- Telegram has a notorious SOCKS5 bug in which it can put an IPv6 destination address into an IPv4 request, flooding Surge with invalid connection attempts. MTProto avoids this path entirely.
- Telegram's IPv4 servers have a bug that can easily cause connections to hang without responding; IPv6 nodes do not. Because MTProto lets the proxy choose the concrete DC address, setting `ipv6=true` resolves this persistent problem. (The outbound proxy must support IPv6 forwarding.)
- An MTProto client requests a Telegram DC ID rather than a concrete server address, so Surge controls the DC-to-endpoint mapping instead of depending on an address chosen by the client.
- Telegram taken over via SOCKS5 or via VIF can easily get stuck on "Updating" after switching networks. With MTProto, DC IP selection is handled by Surge, which greatly reduces the chance of getting stuck.
- A DC can have multiple production endpoints. If one address fails, Surge marks it and uses the next eligible address for a subsequent connection to the same DC.
- The DC mapping source can be overridden with `dc-config-url` when a deployment requires different endpoint selection or update control.

All resulting DC connections still pass through Surge's normal rule system.

## Quick Start

Add the following section to the profile:

```
[MTProto]
interface = 127.0.0.1
port = 5753
secret = 0123456789abcdef0123456789abcdef
ipv6 = true
```

Generate a random secret with:

```sh
openssl rand -hex 16
```

After applying the profile, configure Telegram with:

- Server: an address that reaches the configured `interface`.
- Port: `5753` in this example.
- Secret: the exact secret from the profile.

Telegram also accepts proxy links in these forms:

```text
tg://proxy?server=proxy.example.com&port=5753&secret=<secret>
https://t.me/proxy?server=proxy.example.com&port=5753&secret=<secret>
```

Do not publish a proxy link unless everyone who receives it is intended to use the server.

## Configuration

Only one `[MTProto]` section and one listener are supported in a profile.

#### `interface`: Required, IPv4 or IPv6 address

The local address on which Surge listens. Use `127.0.0.1` when Telegram runs on the same device and no remote client should connect; bind a specific LAN address (e.g. `192.168.1.10`) for a client on the same LAN. `0.0.0.0` exposes the listener on all available IPv4 interfaces — convenient, but protect the port with host and network firewalls. For public access behind a router, forward the external TCP port to the Surge device's listening address and port, and put the public hostname in Telegram rather than the private LAN address.

{% hint style='working' %}
Configuring 0.0.0.0 in Surge iOS is invalid; it will be automatically rewritten as 127.0.0.1.
{% endhint %}

#### `port`: Required, 1–65535

The TCP port accepted by Surge. It must not conflict with another Surge listener or another process. If a router maps a different public port to this internal port, use the public port in Telegram and keep the internal port in the Surge profile.

#### `secret`: Required, 32 hexadecimal characters

The 16-byte MTProxy secret, the only client authentication credential. It is not a Telegram account password, bot token, or API key, and knowing it does not grant access to a Telegram account — but anyone who knows it and can reach the listener can use the proxy and consume its bandwidth.

Accepted forms are the bare 32-character hex secret, or the same secret with the Telegram `dd` transport prefix:

```
secret = 0123456789abcdef0123456789abcdef
secret = dd0123456789abcdef0123456789abcdef
```

When `dd` is used, keep the prefix when entering the secret in Telegram or constructing a proxy link. The Fake TLS `ee...` secret format is not supported. Surge masks this field when exporting a profile without sensitive data.

#### `ipv6`: Optional, Boolean, default: false

The address family used for Surge's outgoing connections to Telegram DCs: with the default value Surge selects only IPv4 endpoints, with `ipv6=true` only IPv6 endpoints. Make sure the Surge device and every outbound proxy in the selected policy path can carry IPv6 destinations. This setting does not control the listener address (`interface`), and Surge does not switch it automatically based on the current system IPv6 availability.

#### `dc-config-url`: Optional, HTTP or HTTPS URL

Overrides the URL used to update the production DC mapping JSON. The default is:

```text
https://raw.githubusercontent.com/surge-networks/MTProtoDCConfigGenerator/refs/heads/main/mtproto-dc-config.json
```

This is the supported mechanism for overriding the DC ID-to-address mapping. The URL must provide a complete mapping document; individual DC/IP pairs are not declared inline in the Surge profile.

Changing this URL invalidates the update timestamp associated with the previous source. The next MTProto connection continues using the current mapping and starts a non-blocking update from the new URL.

## Rule Evaluation and Outbound Policies

After resolving the requested DC, Surge creates a standard TCP request whose target is the selected Telegram IP address and port. The normal rule system then chooses the outbound policy.

- Use the [`PROTOCOL,MTProto` rule](../rules/protocol-and-network.md) to match all Telegram traffic.
- The target is normally an IP address, not a Telegram hostname. IP-based rules, ASN rules, and a Telegram ruleset containing the mapped addresses are the most reliable choices.
- A local Telegram process may provide process metadata. A client connecting from another device cannot provide the remote process identity to Surge.
- The source client address and the mapped Telegram destination remain distinct in the request record.
- If a selected Telegram endpoint fails, the next incoming connection for that DC uses the next compatible endpoint. Telegram may also retry by opening another MTProto connection.

## Telegram DC Resolution

Each production DC can have multiple IPv4, IPv6, general, media, and transport-specific endpoints, so a DC ID is not a one-to-one mapping to a single IP address.

The Telegram client writes a signed DC ID into the MTProxy initialization payload: a positive value such as `2` requests a general endpoint for DC 2; a negative value such as `-2` requests a media endpoint. Surge uses the absolute value as the DC number and retains the general/media distinction while selecting an endpoint. It:

1. Excludes options that require an unsupported `tcpo_only` or per-endpoint secret transport.
2. Excludes media-only options for a general request.
3. Prefers media-only options for a media request when they are available.
4. Prefers Telegram options marked `static`.
5. Selects only IPv4 candidates by default, or only IPv6 candidates when `ipv6=true`.
6. Selects the first remaining endpoint in the order provided by the DC configuration.
7. Marks an endpoint as failed if the backend connection cannot be established or closes before returning any data. A subsequent connection for the same signed DC ID selects the next remaining endpoint.
8. Clears the failure marks after every eligible endpoint has failed, then starts again from the first endpoint.

It is normal for an account whose home DC is DC 5 to create connections to DC 2 or another DC — Telegram uses other DCs for configuration, media, migration, and service operations — so Surge honors the DC requested by each connection rather than forcing all traffic to the account's home DC.

## DC Configuration, Cache, and Updates

The Surge application bundle includes a production DC mapping snapshot generated from Telegram's `help.getConfig`, so the first MTProto connection does not depend on network access to the update URL.

The update flow is:

1. Surge loads a valid persistent JSON mapping into memory if one exists; otherwise it loads the bundled mapping.
2. Each connection is resolved immediately from the in-memory mapping.
3. If no persistent file exists, or its modification date is older than 30 days, the next access starts one non-blocking HTTP update. The triggering connection does not wait for the download, and repeated connections do not start parallel updates.
4. A valid response replaces both the in-memory and persistent mapping.
5. A download error, non-200 response, or invalid JSON leaves the existing mapping untouched. Surge keeps serving from the current mapping and can retry after the core is restarted, because the stale on-disk timestamp is not replaced.

The JSON `expires` value returned by Telegram is preserved as metadata but does not control Surge's refresh schedule; Surge uses the local persistent file's modification date and the 30-day interval.

The update request is made by Surge's standard HTTP client and follows normal outbound rule evaluation. Make sure the update host is reachable through the selected policy.

## Hosting a Custom DC Configuration

A custom `dc-config-url` should publish the production result generated from Telegram's `help.getConfig`; do not scrape source code arrays or combine production, test, and IPv6 test tables manually.

The response must be HTTP 200, valid JSON, no larger than 256 KiB, and contain a `version` value of `1` plus at least one valid option. A simplified example:

```json
{
  "version": 1,
  "date": 1784605659,
  "expires": 1784609827,
  "this_dc": 2,
  "options": [
    {
      "id": 2,
      "ip": "149.154.167.41",
      "port": 443,
      "flags": 16
    }
  ]
}
```

Each option contains:

| Field | Required | Description |
| --- | --- | --- |
| `id` | Yes | Positive production DC ID. |
| `ip` | Yes | IPv4 or IPv6 endpoint string. |
| `port` | Yes | TCP port from 1 through 65535. |
| `flags` | No | Telegram `dcOption` flag bitset; omitted means zero. |
| `secret` | No | Base64-encoded per-endpoint transport secret. Such endpoints are currently not selected for raw relay. |

Relevant flag values are `1` for IPv6, `2` for media-only, `4` for `tcpo_only`, `8` for CDN, `16` for static, `32` for `this_port_only`, and `1024` for an endpoint secret. Values can be combined.

`date`, `expires`, and `this_dc` are useful source metadata but are not required for endpoint lookup. Surge adds an internal source-URL marker to its persistent copy; publishers do not need to provide that field.

## Request Records and Traffic Statistics

A successfully mapped connection appears as a normal TCP request, for example `149.154.167.41:443 (Telegram DC 2 Static)`; other suffixes include `Media` and `IPv6`. The request details also contain a connection note similar to:

```text
Incoming proxy protocol: MTProto, DC ID: 2 (general), mapped address: 149.154.167.41:443
```

The suffix is descriptive only. The actual target hostname, port, remote host, and rule evaluation use the mapped endpoint without the annotation.

Traffic directions are shown from the incoming client's perspective: upload is bytes sent by Telegram through Surge toward the DC; download is bytes returned by the DC to Telegram. A short-lived connection can legitimately have traffic in only one direction, especially during probing, retry, or a remote close. A large number of repeated upload-only connections usually indicates that the selected DC path or outbound policy is being closed before Telegram receives a response.

## Connection Lifecycle and Performance

Telegram decides how many MTProto connections to open and which DC each uses. Surge preserves that model:

- One incoming TCP connection creates one outgoing DC connection.
- Connections for different DCs remain separate; backend DC connections are not pooled or multiplexed across clients.
- The connection passes through the same rule and connector pipeline as other Surge TCP requests.
- MTProxy AES-CTR processing is streamed through the connection and does not alter payload length.

Opening several short connections is not inherently an error: Telegram can probe endpoints, switch DCs, recover from network changes, and maintain separate general and media paths.

## Complete Examples

Same-device proxy:

```
[MTProto]
interface = 127.0.0.1
port = 5753
secret = <32 random hexadecimal characters>
```

LAN or public listener with a custom update mirror:

```
[MTProto]
interface = 0.0.0.0
port = 5753
secret = dd<32 random hexadecimal characters>
dc-config-url = https://example.com/telegram/mtproto-dc-config.json
```

When exposing this example publicly, also configure the operating-system firewall, router/NAT mapping, and public hostname. The Surge profile alone does not publish the port to the Internet.
