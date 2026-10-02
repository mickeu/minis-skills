# Gateway Mode {{ book.VER | replace("%TEXT%", "Mac Only") }}

Surge Mac can operate as a layer-3 gateway, handling the traffic of other devices in the local network. Point another device's gateway (and DNS) at the Mac running Surge, and its traffic goes through the same rule and policy pipeline as local traffic. This lets devices that cannot run Surge themselves — game consoles, TVs, or other computers — benefit from Surge's rules, policies, and DNS handling.

Gateway Mode is enabled from the Surge Mac app UI; the profile does not carry a switch for it. Surge can also act as the DHCP server for the network, assigning addresses and announcing itself as the gateway and DNS server automatically. See [DHCP](dhcp.md) for lease configuration.

## Device Management

Devices handled by the gateway appear in the device list, where you can inspect their traffic and adjust per-device settings such as a custom device name. The device list is available in the Surge Mac app and the Surge Dashboard, and can also be inspected with the `device` command of [surge-cli](../tools/cli.md).

## Per-Device Policies

To apply different rules to different client devices, use the `SRC-IP`, `DEVICE-NAME`, and `MAC-ADDRESS` rule types. See [Source and Port Rules](../rules/source-and-port.md).

```
DEVICE-NAME,Apple-TV,Proxy
SRC-IP,192.168.1.100,DIRECT
```

## Access Restriction

By default, the gateway service only accepts devices from the current subnet, so a misconfiguration (such as a DMZ setup) does not expose it to the Internet. This is controlled by the [`gateway-restricted-to-lan`](../profile/general.md) option, which is enabled by default.

## UDP Fast Path {{ book.VER | replace("%TEXT%", "Mac 6.4.0+") }}

When Surge Mac operates in Gateway VM mode, devices that create thousands of short-lived UDP flows (such as P2P downloaders or online games) can exhaust the standard layer-4 proxy engine. The UDP Fast Path feature automatically downgrades those high-connection clients to a lightweight L3 forwarding mode whenever they exceed the threshold (10 connections within 1 second or 30 within 10 seconds).

- Packets forwarded via the fast path bypass the proxy engine entirely and therefore cannot be matched by rules or MITM.
- Destination ports below 1024 stay in normal mode to preserve compatibility with common services.
- You can toggle the fast path for each client device from the Dashboard/Device list if you need to pin a client to either behavior.
