# WireGuard

The `wireguard` policy type turns a layer-3 WireGuard tunnel into a regular Surge outbound policy. Surge maintains an internal IP stack for each WireGuard policy, encrypts each packet for the peer selected by `allowed-ips`, and sends the encrypted UDP datagrams either directly or through another policy. Both TCP and [UDP relay](../policies/udp.md) are supported.

{% hint style='info' %}
A WireGuard policy is an application-level outbound policy. It does not install a system-wide WireGuard VPN: only connections selected by Surge rules, policy groups, or manual selection enter the tunnel. The device's global route table is not changed.
{% endhint %}

A complete configuration has two parts: a policy line in `[Proxy]` and a matching `[WireGuard <section-name>]` section. The section may be placed in a [detached profile section](../profile/format.md).

## Quick Start

A peer-to-peer policy that reaches a private subnet by IP:

```
[Proxy]
Office WG = wireguard, section-name=office-wg

[WireGuard office-wg]
private-key = <client-private-key>
self-ip = 10.20.0.2
mtu = 1280
peer = (public-key = <server-public-key>, allowed-ips = "10.20.0.0/24, 192.168.50.0/24", endpoint = vpn.example.com:51820)

[Rule]
IP-CIDR,192.168.50.0/24,Office WG,no-resolve
```

A general proxy policy that routes Internet traffic through a WireGuard gateway:

```
[Proxy]
WG Gateway = wireguard, section-name=wg-gateway

[WireGuard wg-gateway]
private-key = <client-private-key>
self-ip = 10.30.0.2
dns-server = 10.30.0.1
mtu = 1280
peer = (public-key = <server-public-key>, allowed-ips = 0.0.0.0/0, endpoint = gateway.example.com:51820, keepalive = 25)
```

The presence of `dns-server` decides the policy's role:

- **Peer-to-peer policy** (no `dns-server`): intended for IP-based access to specific peers or private routes. Destination names cannot normally be resolved through the policy; use IP-based rules. The default latency test is a native WireGuard RTT probe.
- **General proxy policy** (one or more `dns-server` values): treated as a normal outbound proxy and tested with the standard URL test.

This classification is static and only selects the default test mechanism and the tests offered in the runtime UI. Actual reachability is always determined by peer `allowed-ips`, server-side routing, and server-side forwarding/NAT. `allowed-ips = 0.0.0.0/0` only selects a peer inside Surge; the server must still forward the traffic and normally perform source NAT for Internet access.

## Prerequisites and Limitations

Prepare in advance: a client private key, at least one peer public key, a unique client tunnel IPv4/IPv6 address, the peer endpoint host and UDP port, and the destination prefixes routed to each peer. For a general proxy policy, also a DNS resolver reachable inside the tunnel and a peer route covering it.

- Surge acts as a WireGuard client only; it does not expose a WireGuard server.
- Key distribution, address assignment, and server configuration are outside the WireGuard protocol and must be prepared separately.
- WireGuard returns no descriptive authentication or routing errors. Invalid keys, blocked UDP, missing routes, and missing server-side NAT all commonly appear as timeouts.
- The main supported payloads are TCP and UDP. Surge only answers ICMP/ICMPv6 echo requests sent to the configured local tunnel address.
- The graphical editor supports one peer; configure multiple peers in profile text.
- Treat private and preshared keys as secrets; they are masked when Surge exports a profile without sensitive data. Reusing the same private key or tunnel address on simultaneously active devices can cause route conflicts, handshake instability, or traffic delivery to the wrong device.

## Policy Line

```
[Proxy]
Office WG = wireguard, section-name=office, test-timeout=8, ecn=true
```

[Common policy parameters](../policies/parameters.md) apply, with L3-specific exceptions: `interface` binding and the `shadow-tls-*` parameters are not supported for WireGuard policies.

#### `section-name`

Required.

Name of the `[WireGuard <name>]` section used by this policy. It must exactly match the section suffix. The referenced section must contain a private key, at least one local tunnel address, and at least one complete peer. Section names are profile identifiers only; they are not sent to the peer.

#### `underlying-proxy`

Optional, policy or group name, default: DIRECT.

Transports the encrypted WireGuard UDP datagrams through another Surge policy. Without it, Surge resolves peer endpoint hostnames with the normal Surge DNS resolver and sends datagrams directly from the selected physical interface. With it:

- encrypted datagrams are carried by a Surge UDP connector through the selected policy;
- endpoint hostname resolution can occur through that connector rather than locally;
- a policy group is evaluated to its current final policy, and a change of the effective policy resets the WireGuard transport sockets.

Avoid dependency loops in which the underlying policy eventually selects the same WireGuard policy. `underlying-proxy` only affects transport to the peer endpoint; it is unrelated to `dns-server`, which resolves destination names inside the tunnel.

#### `test-url`

Optional, plain `http://` URL.

Forces the standard URL test even when the policy has no `dns-server` and would otherwise use the native RTT probe. Only plain HTTP URLs are accepted. The host must be resolvable and routable through the WireGuard policy — for a peer-to-peer configuration, use an IP-literal or internal URL reachable through the configured routes.

#### `test-timeout`

Optional, in seconds, default: global `test-timeout`, otherwise 5.

Limits the actual RTT probe or HTTP test. Surge additionally allows up to 10 seconds for L3 initialization (endpoint resolution, socket setup, first handshake), so `test-timeout=5` can take up to about 15 seconds when the session must first be initialized.

## WireGuard Section

```
[WireGuard office]
private-key = <client-private-key>
self-ip = 10.20.0.2
peer = (public-key = <peer-public-key>, allowed-ips = 10.20.0.0/24, endpoint = vpn.example.com:51820)
```

#### `private-key`

Required.

Client private key, in standard WireGuard Base64 encoding or as a 64-character hexadecimal representation of the 32-byte key.

#### `self-ip`

Conditional: at least one of `self-ip` and `self-ip-v6` is required.

Client IPv4 tunnel address. This is a plain address, not a CIDR prefix, and must match the client address expected by the remote configuration. Each simultaneously active client should use a unique address.

#### `self-ip-v6`

Conditional: at least one of `self-ip` and `self-ip-v6` is required.

Client IPv6 tunnel address. The configured address families also determine which tunneled DNS resolver families are usable: an IPv4 DNS server requires `self-ip`; an IPv6 DNS server requires `self-ip-v6`.

#### `dns-server`

Optional, comma-separated resolvers.

DNS resolvers used inside the tunnel, e.g. `dns-server = 10.20.0.1, fd00:20::1`. Accepted entries are plain IPv4/IPv6 addresses, supported IP-and-port forms, and `system`. IPv4 multicast addresses and encrypted-DNS URLs are not accepted.

Queries to these resolvers travel through the WireGuard session, so each resolver needs a matching `allowed-ips` route and must be reachable on the remote network. The presence of this field also classifies the policy as a general proxy policy (see Quick Start).

The `dns-server` field does **not** resolve the peer's `endpoint` hostname. Endpoint lookup uses normal Surge DNS when transport is direct, or the underlying connector when `underlying-proxy` is configured.

#### `prefer-ipv6`

Optional, Boolean, default: false.

When both local address families are configured and a destination name returns both A and AAAA records, prefer IPv6. It does not create IPv6 routes or reachability by itself.

#### `mtu`

Optional, 576–1420, default: 1280.

Layer-3 tunnel MTU. Surge drops an outbound packet that exceeds it. Too large a value may produce stalls or black holes on paths with extra encapsulation (lower it if large transfers stall); an unnecessarily small value increases overhead.

#### `peer`

Required, one or more peer definitions.

Each peer is a parenthesized field list; multiple peers are separated by commas, and multiple `peer =` lines accumulate:

```
peer = (public-key = <peer-a-key>, allowed-ips = 10.10.0.0/16, endpoint = a.example.com:51820), (public-key = <peer-b-key>, allowed-ips = 10.20.0.0/16, endpoint = b.example.com:51820)
```

## Peer Fields

#### `public-key`

Required.

The remote peer's public key, Base64 or 32-byte hexadecimal.

#### `allowed-ips`

Required, comma-separated IPv4/IPv6 CIDRs (quote the value if it contains commas).

Defines which outbound destination prefixes select this peer. Surge builds separate IPv4 and IPv6 route tables from all peers' `allowed-ips` and uses the most specific matching prefix; a narrow route on one peer overrides a broader route on another (e.g. a `10.0.0.0/8` peer wins over a `0.0.0.0/0` peer for those addresses). If no route matches, Surge logs the missing route and drops the packet — unmatched traffic is never sent directly as a fallback.

A default route (`0.0.0.0/0`, `::/0`) only makes all addresses select the peer; it neither proves the peer forwards Internet traffic nor changes the policy classification.

#### `endpoint`

Required, host and UDP port.

The peer address, e.g. `vpn.example.com:51820`. IPv4 addresses, IPv6 addresses in supported host-and-port syntax (e.g. `[2001:db8::10]:51820`), and domain names are accepted. Surge periodically re-resolves domain endpoints and updates the transport address if the result changes; if the address family changes, transport sockets are rebuilt.

#### `preshared-key`

Optional.

An additional 32-byte symmetric key added to the handshake. It must match the peer configuration exactly.

#### `keepalive`

Optional, in seconds, 0–65535, default: 0 (disabled).

WireGuard persistent keepalive interval, commonly used when the client is behind NAT and the mapping must stay active. Avoid unnecessarily short intervals; they increase background traffic and power use.

#### `client-id` {{ book.VER | replace("%TEXT%", "iOS 5.3.1+") }} {{ book.VER | replace("%TEXT%", "Mac 4.10.3+") }}

Optional.

Some services — such as Cloudflare WARP — use bytes 1–3 of the WireGuard packet's reserved area as a client or routing ID. Surge writes these bytes on outbound packets and clears them on inbound packets before WireGuard processing. Accepted forms: slash-separated decimals (`client-id = 83/12/235`), three-byte hexadecimal, or four-character Base64. Leave it unset for standard WireGuard deployments.

```
[WireGuard warp]
private-key = <client-private-key>
self-ip = 172.16.0.2
self-ip-v6 = 2606:4700:110:0000::2
dns-server = 1.1.1.1, 2606:4700:4700::1111
peer = (public-key = <peer-public-key>, allowed-ips = "0.0.0.0/0, ::/0", endpoint = engage.cloudflareclient.com:2408, client-id = 83/12/235)
```

## Lifecycle

WireGuard sessions are prepared at profile load; sockets and handshakes start on demand. Surge builds the route tables, resolves endpoints, evaluates `underlying-proxy`, creates one UDP transport per peer, and forces initial handshakes; the session is ready once a peer returns a valid WireGuard packet. Surge then advances the WireGuard timers for retransmission, rekeying, keepalive, and expiration, and requests a new handshake when traffic needs an expired peer.

A network change or an effective underlying-policy change invalidates the sockets and triggers reconstruction. Incoming fragments can be reassembled before delivery.

## Policy Testing {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

The test mode is selected statically from the profile:

- no `dns-server` and no explicit `test-url`: native WireGuard RTT probe;
- one or more `dns-server` values, or an explicit `test-url`: standard URL test.

**Native RTT probe**: Surge starts or resumes the session, forces a handshake to every configured peer, and completes when the first peer returns a valid WireGuard packet, reporting the round-trip time and responding endpoint. The result measures peer reachability and handshake RTT only — it does not prove that routes, DNS, or Internet egress work. With multiple peers, the fastest peer completes the test.

**Standard URL test**: the same HTTP test path as normal proxies, covering destination resolution, routing, WireGuard transport, remote forwarding, and the HTTP response. A failure can therefore mean a handshake failure, a missing `allowed-ips` route, an unreachable tunnel DNS server, missing remote forwarding/NAT, a blocked destination, or an HTTP timeout. An explicit `test-url` can point at a service inside the private network to test a peer-to-peer policy against a specific application.

Both modes allow an extra 10 seconds for L3 initialization on top of `test-timeout`. The first test after a network change or long inactivity may be slower because endpoint DNS, sockets, and handshakes must be recreated.

The runtime detail view shows the effective underlying policy, active TCP/UDP counts, peer endpoints and handshake states, and recent errors. For a peer-to-peer policy, only the RTT test is offered (the comprehensive network diagnostics likewise reports its UDP relay test as skipped); a general proxy policy keeps the standard latency, DNS, UDP, and external-address tests.

## ECN and DSCP

ECN {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }} is a policy-line option, not a section field, and is disabled by default for WireGuard policies:

```
[Proxy]
WG Gateway = wireguard, section-name=wg-gateway, ecn=true
```

On supported OS versions, Surge preserves ECN information for tunneled traffic and applies RFC 6040-style merging on received markings. Disable it if it causes connectivity problems on an incompatible network. See [Common Policy Parameters](../policies/parameters.md).

Following the WireGuard protocol recommendation, Surge marks handshake packets with DSCP `0x88` (AF41) to improve handshake success on networks that honor this class. Regular tunnel packets are not automatically marked.

## Troubleshooting

- **The RTT test times out.** Check keys (including any preshared key), endpoint host/port, firewalls, UDP reachability on the current network, `underlying-proxy` UDP support, duplicate client keys or addresses, and whether any peer is online. Because WireGuard produces no descriptive remote errors, most configuration mistakes appear as timeouts.
- **Handshake works but a private address is unreachable.** Verify the destination is covered by the intended peer's `allowed-ips`, then remote routing and firewall policy. A handshake proves only that the peers can exchange authenticated packets.
- **URL test fails but RTT works.** Check `dns-server` reachability through `allowed-ips`, default or destination routes, remote IP forwarding, source NAT, the test URL, and IPv4/IPv6 family compatibility.
- **Domain names do not resolve.** Confirm `dns-server` is present, uses a family with a configured local address, is covered by `allowed-ips`, and permits queries from the client. Only IP addresses working is expected behavior for a peer-to-peer policy without `dns-server`.
- **One of several peers never receives traffic.** Inspect overlapping `allowed-ips`; longest-prefix matching may always select another peer.
- **Large transfers stall.** Lower `mtu` and retest; encapsulation through another proxy or a small-MTU path can black-hole large packets while handshakes still work.

For a Tailscale-managed WireGuard mesh, see the [Tailscale policy](../policies/tailscale.md).
