# Subnet Settings

Subnet settings apply specific parameters only while the device is on a matching network. Each line consists of a [subnet expression](../rules/protocol-and-network.md) followed by comma-separated `key=value` parameters.

> For compatibility reasons, the subnet settings section is named `[SSID Setting]` in the profile.

```
[SSID Setting]
SSID:MyHome suspend=true
```

The subnet expression may use the `SSID:`, `BSSID:`, `ROUTER:`, and `TYPE:` forms; see [Subnet Expressions](../rules/protocol-and-network.md) for the full syntax.

## Parameters

#### suspend

Optional, Boolean

Suspend Surge temporarily under the matching networks.

```
[SSID Setting]
SSID:MyHome suspend=true
```

#### cellular-fallback {{ book.VER | replace("%TEXT%", "iOS Only") }}

Optional, `default` | `off` | `wifi-assist` | `hybrid`

Control the Wi-Fi Assist and Hybrid Network behavior for the matching networks.

```
[SSID Setting]
SSID:MyHome cellular-fallback=off
```

- `cellular-fallback=default`
  Use the global Wi-Fi Assist and Hybrid Network settings.
- `cellular-fallback=off`
  Turn off Wi-Fi Assist and Hybrid Network for the network.
- `cellular-fallback=hybrid`
  Turn on Hybrid Network for the network.
- `cellular-fallback=wifi-assist`
  Turn on Wi-Fi Assist for the network.

#### cellular-mode {{ book.VER | replace("%TEXT%", "Mac Only") }}

Optional, Boolean

Treat the matching networks as metered networks. While connected to such a network, Surge Mac automatically turns on Metered Network Mode: only the applications on the allowed list may access the Internet, and connections from other processes are rejected. Configure the allowed applications in the Surge Mac UI. See [Platform Differences](../getting-started/platform-differences.md) for an overview of Metered Network Mode.

```
[SSID Setting]
SSID:PhoneHotspot cellular-mode=true
```

#### tfo-behaviour

Optional, `auto` | `force-enabled` | `force-disabled`

Override the TCP Fast Open behavior for the matching networks.

```
[SSID Setting]
SSID:MyHome tfo-behaviour=force-enabled
```

- `tfo-behaviour=auto`
  Use the default TFO behavior.
- `tfo-behaviour=force-disabled`
  Disable TFO for the network completely.
- `tfo-behaviour=force-enabled`
  Forcibly enable TFO for the network. This option makes Surge ignore the system TFO blackhole detection mechanism.

#### dns-server

Optional, comma-separated IP addresses or `system`

#### encrypted-dns-server

Optional, comma-separated URLs or `off`

Override the DNS settings for the matching networks.

```
[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=https://1.1.1.1/
```

If encrypted DNS is configured in the global DNS settings, you must explicitly set `encrypted-dns-server=off` to use traditional DNS on the matching network.

```
[SSID Setting]
SSID:MyHome dns-server=8.8.8.8,encrypted-dns-server=off
```
