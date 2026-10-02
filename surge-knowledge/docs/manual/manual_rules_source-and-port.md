# Source and Port Rules

These rule types match where a request comes from — the client's address, port, device name, or MAC address — and which ports are involved. Port rules are useful on any setup; source-based rules matter mainly when other devices send traffic through Surge.

```
[Rule]
DEST-PORT,22,DIRECT
SRC-IP,192.168.20.0/24,Proxy
DEVICE-NAME,Kids-iPad,REJECT
```

## When Source-Based Rules Make Sense

Requests originating from apps on the local device all share the same local source, so `SRC-IP`, `DEVICE-NAME`, and `MAC-ADDRESS` are only meaningful when Surge handles traffic from other devices:

- Surge Mac running in [Gateway Mode](../features/gateway.md) as the router for a LAN.
- LAN devices using Surge as their HTTP or SOCKS5 proxy.
- Devices with names assigned by the built-in [DHCP server](../features/dhcp.md).
- Remote devices connected through [Surge Ponte](../features/ponte.md).

Use them to apply different policies per device, for example giving a set-top box a dedicated proxy or blocking traffic from a specific device.

## Port Expressions

`DEST-PORT`, `SRC-PORT`, and `IN-PORT` share the same value grammar:

- A plain port number: `IN-PORT,6153`
- A closed range: `DEST-PORT,10000-20000`
- The operators `>`, `<`, `>=`, `<=`: `SRC-PORT,>=50000` {{ book.VER | replace("%TEXT%", "iOS 5.8.4+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.4+") }}

## Rule Types

#### DEST-PORT

```
DEST-PORT,80-81,DIRECT
```

Matches if the destination port of the request matches.

#### SRC-PORT {{ book.VER | replace("%TEXT%", "iOS 5.8.4+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.4+") }}

```
SRC-PORT,>=50000,DIRECT
```

Matches if the client's source port number matches.

#### IN-PORT

```
IN-PORT,6152,DIRECT
```

Matches if the Surge listen port that accepted the request matches. Useful when Surge listens on multiple ports and you want different behavior per port.

#### SRC-IP

```
SRC-IP,192.168.20.100,DIRECT
```

Matches if the client IP address of the request matches. Both IPv4 and IPv6 addresses are supported.

The value may also be a CIDR range:

```
SRC-IP,192.168.20.0/24,DIRECT
```

A single address matches exactly; a CIDR value matches any client address in the range.

#### DEVICE-NAME

```
DEVICE-NAME,Kids-iPad,REJECT
```

Matches if the client's device name matches. Wildcard characters `*` and `?` are supported; matching is case-sensitive.

- For [Surge Ponte](../features/ponte.md) access, the device name is the device name configured in the client device's system settings.
- If [Surge DHCP](../features/dhcp.md) is enabled, LAN devices can be matched by the custom device name shown in the device view.

#### MAC-ADDRESS {{ book.VER | replace("%TEXT%", "Mac 6.1.0+") }}

```
MAC-ADDRESS,A4:83:E7:11:22:33,Proxy
```

Matches the MAC address of the accessing device. This only works for devices on the same local area network; if the request was forwarded by a gateway, the MAC address cannot be obtained.
