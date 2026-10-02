# Enhanced Mode

Some applications do not follow the system proxy settings. Enhanced Mode ensures Surge handles the traffic of all applications: Surge creates a virtual network interface (VIF) and registers it as the default route, capturing raw traffic regardless of proxy settings.

On Surge iOS, the VIF is part of the VPN-based takeover and is enabled by default. On Surge Mac, Enhanced Mode must be started manually.

## How the VIF Works

While the VIF is active, Surge answers all DNS queries with a virtual (fake) IP address in the `198.18.0.0/15` block. When a connection to a fake IP arrives on the VIF, Surge maps it back to the original domain name for rule matching and establishes the real connection itself. See [Advanced DNS Topics](../dns/advanced.md) for details on fake-IP behavior and related options such as `always-real-ip` and `hijack-dns`.

## Limitations

The Surge VIF can only process TCP, UDP, and ICMP traffic. Other protocols cannot pass through the VIF, so only enable this feature when necessary.

ICMP traffic cannot be proxied. Surge forwards ICMP packets directly and the VIF returns responses itself, so tools like ping keep working. Privacy-conscious users can disable this behavior with the [`icmp-forwarding`](../profile/general.md) option.

## Related [General] Options

These options in the [\[General\] section](../profile/general.md) tune the VIF behavior:

- `tun-excluded-routes`: bypass specific IP ranges from the VIF, letting all traffic in those ranges pass through untouched.
- `tun-included-routes`: publish additional smaller routes on the VIF so they take priority over interface-local routes.
- `ipv6-vif`: control whether the VIF is set up with IPv6.
- `icmp-forwarding`: control the ICMP forwarding behavior described above.

## Implementation Note

Starting from Surge Mac 5.8.0, Enhanced Mode is powered by Apple's Network Extension framework instead of the legacy utun driver. Existing configuration parameters such as `vif-mode` stay in the profile for backward compatibility but no longer affect the runtime behavior.
