# Platform Differences

Surge Mac and Surge iOS share the same core engine and profile format, and most options behave identically. This page consolidates the differences: features exclusive to one platform and where each is documented.

Surge tvOS is included with the Surge iOS app and generally behaves like Surge iOS; features marked iOS-only usually apply to tvOS as well unless noted on the feature's page.

## Surge Mac Only

| Feature | Notes | Documentation |
|---|---|---|
| Enhanced Mode toggle | The VIF must be enabled manually on Mac; on iOS it is part of the VPN takeover and enabled by default. | [Enhanced Mode](../features/enhanced-mode.md) |
| Gateway Mode | Operate as a layer-3 gateway handling traffic for other LAN devices. | [Gateway Mode](../features/gateway.md) |
| DHCP server | Provide DHCP service for gateway-managed devices, with the `[DHCP]` section for lease tuning. | [DHCP](../features/dhcp.md) |
| Ponte server role | Any Surge device can act as a Ponte client, but only Surge Mac can serve as the Ponte server (home network access point). | [Surge Ponte](../features/ponte.md) |
| External Proxy Program | Launch and manage an external proxy executable as a policy. Surge iOS treats `external` policies as REJECT. | [External Proxy Program](../policies/external.md) |
| PROCESS-NAME rule | Match traffic by the originating process. Surge iOS ignores these rules. | [Process Rules](../rules/process.md) |
| MAC-ADDRESS rule | Match LAN client devices by MAC address. | [Source and Port Rules](../rules/source-and-port.md) |
| surge-cli | Command-line tool for controlling local and remote instances. | [CLI](../tools/cli.md) |
| Surge Dashboard app | The Dashboard app ships with Surge Mac; it can also connect to remote Surge iOS instances over network or USB. | [Dashboard](../tools/dashboard.md) |
| Mac-only `[General]` keys | `http-listen`, `socks5-listen`, `read-etc-hosts`, `set-system-socks-proxy`, `subnet-exp-wifi-always-match`. | [General Section](../profile/general.md) |

### Metered Network Mode

Surge Mac can restrict which applications and processes may access the Internet, which is useful on metered connections such as a phone hotspot. The allowed application list is configured in the Surge Mac interface. The mode can be turned on automatically for specific networks with the `cellular-mode` parameter in [Subnet Settings](../features/subnet-settings.md).

## Surge iOS Only

| Feature | Notes | Documentation |
|---|---|---|
| Works on cellular | Surge iOS runs as a Network Extension VPN, so all functions work on Wi-Fi and cellular networks alike. | [How Surge Works](how-surge-works.md) |
| `compatibility-mode` | Selects the takeover mode (proxy takeover, VIF takeover, or combinations) to work around app-specific issues. | [General Section](../profile/general.md) |
| CELLULAR policy family | `CELLULAR`, `CELLULAR-ONLY`, `HYBRID`, `NO-HYBRID` built-in policies for controlling interface usage. | [Built-in Policies](../policies/built-in.md) |
| `hybrid` policy parameter | Set up proxy connections over Wi-Fi and cellular simultaneously. | [Policy Parameters](../policies/parameters.md) |
| CELLULAR-RADIO / CELLULAR-CARRIER rules | Match by radio access technology or carrier (also available on tvOS). | [Protocol and Network Rules](../rules/protocol-and-network.md) |
| Cellular Fallback subnet setting | Per-network override of Wi-Fi Assist / All-Hybrid behavior. | [Subnet Settings](../features/subnet-settings.md) |
| URL scheme start/stop actions | `start`, `stop`, and `toggle` URL scheme actions are iOS-only. | [URL Scheme](../tools/url-scheme.md) |
| iOS-only `[General]` keys | `allow-wifi-access`, `allow-hotspot-access`, `wifi-access-http-port`, `wifi-access-socks5-port`, `wifi-access-http-auth`, `wifi-assist`, `all-hybrid`, `hide-vpn-icon`, `include-all-networks`, `include-local-networks`, `include-apns`, `include-cellular-services`, `auto-suspend`. | [General Section](../profile/general.md) |

{% hint style='info' %}
Platform-specific keys are simply ignored on the other platform, so a single profile can be shared between Surge Mac and Surge iOS. To restrict individual profile lines to one platform, use [line requirement expressions](../profile/requirement.md) such as `#!MACOS-ONLY`.
{% endhint %}
