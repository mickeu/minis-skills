# Tailscale {{ book.VER | replace("%TEXT%", "iOS 5.20.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.7.0+") }}

The `tailscale` policy type joins a tailnet as a node and exposes that tailnet as a Surge outbound policy, supporting both TCP and [UDP relay](../policies/udp.md). Surge registers the node with the control server, receives the peer, route, DNS, and DERP configuration, creates [WireGuard](../policies/wireguard.md) tunnels to authorized peers, uses direct UDP paths where possible and DERP relays otherwise, routes each packet to the best-matching peer, and resolves MagicDNS names inside the policy — all without installing a separate system VPN.

{% hint style='info' %}
A Tailscale policy is an application-level outbound policy, not a replacement for the system Tailscale client: only traffic selected by Surge rules or an explicit policy choice uses the tailnet. Interactive sign-in, automatic MagicDNS and peer-address routing, and the always-on session default require Surge iOS 5.21.0 or Surge Mac 6.8.0. Earlier versions require an auth key and explicit routing rules, and tear down an idle session after 600 seconds by default. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}
{% endhint %}

A complete configuration has two parts: a policy line in `[Proxy]` and a matching `[Tailscale <section-name>]` section.

## Quick Start

```
[Proxy]
My Tailnet = tailscale, section-name=my-tailnet

[Tailscale my-tailnet]
auth-key = tskey-auth-example
hostname = surge-mac
```

`section-name` must exactly match the section suffix. As an alternative to `auth-key`, open the Tailscale policy editor in Surge and complete interactive sign-in; Surge then saves the section with `interactive-login = true`. The two login methods are mutually exclusive, and copying an `interactive-login` line to another device does not copy the locally stored identity.

Automatic routing is enabled by default: after the session discovers the tailnet, Surge routes its MagicDNS suffix and the individual IPv4/IPv6 addresses of visible peers to this policy. You can still select the policy directly or add explicit rules for subnet routes or broader ranges:

```
[Rule]
DOMAIN-SUFFIX,example-tailnet.ts.net,My Tailnet
IP-CIDR,100.64.0.0/10,My Tailnet,no-resolve
```

The actual MagicDNS suffix and address ranges are assigned by the control plane — use the values shown by your tailnet. Set `auto-add-magic-dns-rule = false` if all routing should be controlled by explicit rules.

## Prerequisites and Limitations

You need a Tailscale (or compatible) control server account, plus either an auth key that can register a node without interactive login or access to Surge's policy editor for interactive sign-in, and any required ACL, subnet-route, or exit-node approvals in the control plane. Treat auth keys as secrets: a valid reusable key can add a node to the tailnet, subject to its server-side restrictions.

- The policy handles outbound traffic selected by Surge. It does not advertise this device as a subnet router or exit node, and does not expose inbound services to the tailnet.
- The control server still determines ACLs, peer visibility, routes, DNS settings, exit-node availability, and node authorization. A route advertised by a peer is usable only when the control plane delivers it to this node.

## Policy Line

```
[Proxy]
Office Tailnet = tailscale, section-name=office, test-timeout=8
```

[Common policy parameters](../policies/parameters.md) apply, with L3-specific exceptions: `interface` binding and the `shadow-tls-*` parameters are not supported.

#### `section-name`

Required.

Name of the `[Tailscale <name>]` section used by this policy. The referenced section must exist and configure exactly one login method: `auth-key` or `interactive-login = true`.

#### `underlying-proxy`

Optional, policy or group name, default: DIRECT.

By default, DERP, STUN, and direct peer-path traffic originate through DIRECT. When `underlying-proxy` is configured, DERP relay connections use that policy and direct physical UDP sockets are disabled, so peer traffic uses DERP relay transport only. This prevents accidental bypass of the requested policy, but means a chained Tailscale policy usually has higher latency and depends on DERP availability. A policy group is evaluated to its current final policy. Avoid dependency loops in which the underlying policy eventually selects the same Tailscale policy.

Access to `control-url` is a separate case: Surge handles it through the standard outbound mode and the normal rule system, and `underlying-proxy` has no effect on it (see [`control-url`](#control-url)).

#### `test-url`

Optional, plain `http://` URL (HTTPS is not accepted).

Always selects the standard URL test. If no exit node or advertised route can reach the URL, the test fails even when tailnet peer connectivity works. For a policy without an exit node, either omit `test-url` to use the native connectivity probe, or use a URL hosted on an address reachable through the tailnet.

#### `test-timeout`

Optional, in seconds, default: global `test-timeout`, otherwise 5.

Limits the actual probe or HTTP test. Surge additionally allows up to 10 seconds for Tailscale initialization (control registration, netmap acquisition, DERP setup, first WireGuard handshake), so `test-timeout=5` may take up to about 15 seconds overall.

## Tailscale Section

Use only the documented fields below. The parser may ignore an unrecognized key, but this is not a supported extension mechanism; a malformed line or invalid value for a recognized key makes the profile invalid.

#### `auth-key`

One login method required; cannot be combined with `interactive-login`.

Auth key sent during node registration. A key that requires interactive approval cannot complete auth-key registration; use interactive sign-in instead. Recommended server-side restrictions: short expiration, single use unless reuse is required, preauthorization, and appropriate tags and ACLs. The key is omitted or masked when Surge exports a profile without sensitive data.

Surge stores the Tailscale machine identity in a local state file selected by a SHA-256 hash of the auth key, so reusing the same key and profile preserves the identity across restarts; changing the key normally creates a different node identity.

#### `interactive-login` {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

One login method required, Boolean, default: false; cannot be combined with `auth-key`.

Uses an identity authorized through Surge's interactive Tailscale sign-in (macOS and iOS). Start sign-in from the policy editor and open the authorization URL supplied by the control server; Surge then stores the machine and node identity locally and writes `interactive-login = true` instead of an auth key.

The line is only a reference to local login state — it contains no transferable credentials and does not start a browser login by itself. If the local state is missing or damaged, Surge asks you to sign in again from the policy editor. The state is associated with the section name, so renaming the section may require signing in again.

#### `control-url`

Optional, URL, default: `https://controlplane.tailscale.com`.

Control server URL, for the standard Tailscale control plane or a compatible service such as a privately operated control server. HTTPS is strongly recommended; the initial server-key retrieval is protected with HTTPS even when an `http` URL is supplied, while subsequent transport follows the configured URL.

Surge accesses this URL through the standard outbound mode and the normal rule system; `underlying-proxy` does not participate. Configure the desired route with rules — and make sure the matching rule does not select this Tailscale policy, directly or through a policy group. That recursive selection deadlocks: the policy waits for the control connection, while the control connection waits for the policy.

#### `hostname`

Optional, default: a platform-derived name such as `surge-macos`.

Node hostname sent during registration, normalized to lowercase. The DNS name displayed by MagicDNS may include an additional tailnet suffix assigned by the control plane.

#### `derp-only`

Optional, Boolean, default: false.

Forces all encrypted peer traffic through DERP relays even when the effective underlying policy is DIRECT. In DERP-only mode, no physical peer-to-peer UDP sockets are opened; STUN netcheck, direct endpoint discovery, discovery pings, and direct-path heartbeats are disabled; and previously learned direct-path state is not used. DERP connections still use the effective underlying policy, and control-plane connections continue to follow the rule system.

A non-DIRECT `underlying-proxy` already makes the transport DERP-only; this field is useful when the surrounding connections should remain direct but peer-to-peer UDP must not be attempted.

#### `auto-add-magic-dns-rule` {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Optional, Boolean, default: true.

Once Surge receives the tailnet's network map and DNS configuration, it automatically routes the discovered MagicDNS domain suffix and each visible peer's individual IPv4 and IPv6 tailnet addresses to this policy, refreshing the routes as the map changes. The option name is retained for compatibility, but it controls both the MagicDNS suffix rule and the peer-address rules.

Advertised subnet routes, exit-node traffic, and other broader destinations still require explicit rules or manual policy selection. When enabled, Surge starts the session right after loading the profile so the required information can be discovered before matching traffic arrives.

#### `exit-node`

Optional, default: `none`.

- `none`: disable exit-node routing; default routes from all peers are ignored while more specific routes remain usable. If default-route traffic is attempted while usable exit nodes exist, Surge drops the packet and reports a one-time warning naming the available nodes, so a missing setting is not mistaken for a connectivity failure.
- `auto`: select an exit node only when exactly one usable candidate exists. With zero or with two or more candidates, none is selected — the ambiguity is intentional, because an arbitrary choice could change egress location or trust boundaries; a warning lists the candidates when default-route traffic is attempted.
- An explicit selector: match one peer by stable ID, full DNS name, short DNS name (the first label), or tailnet IPv4/IPv6 address. Matching is case-insensitive and ignores a trailing dot. The match must be unique and the peer usable; a missing, offline, or ambiguous match produces no exit-node route and no fallback.

```
exit-node = office-exit.example-tailnet.ts.net
```

An exit-node candidate is a peer advertising an IPv4 or IPv6 default route; it is usable only while present, online, and with an allocated tunnel. Only the selected node's default routes are installed, so overlapping exit nodes never compete in the route table. Even with an exit node, Surge does not change the device's global default route — the node receives only the connections Surge assigned to this policy.

#### `idle-keepalive` {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Optional, in seconds, default: always on.

Controls how long an unused session stays alive after its last TCP connection or UDP mapping closes. A positive value tears down networking after that many idle seconds (the idle monitor checks periodically, so teardown may occur slightly late); omitted, `0`, or `-1` keeps the session running continuously. Idle teardown closes control and DERP connections and releases peer tunnels and routes, but preserves the local key state; the next connection restarts networking, so the first operation after teardown pays control, route, and handshake latency. Use a positive value such as `600` only when reducing background network and memory usage matters more than restart latency.

#### `prefer-ipv6`

Optional, Boolean, default: false.

Prefer IPv6 for the layer-3 session and DNS result selection when both families are available. It does not create IPv6 connectivity by itself.

#### `dns-server`

Optional, comma-separated resolvers, default: resolvers from the control plane.

Overrides the resolver list received from the control plane. Accepted entries are plain IPv4/IPv6 addresses or an IP with a port in Surge's supported address-and-port syntax; IPv4 multicast addresses are rejected, and encrypted-DNS (DoH/DoQ/DoT) URLs do not belong here. Control-provided search domains and locally synthesized MagicDNS records are still applied.

The resolver must be reachable through this policy's route table — a resolver at a tailnet IP requires an authorized peer route for that IP; an unroutable resolver causes lookup failures.

#### `mtu`

Optional, 576–1420, default: 1280.

Layer-3 MTU; larger packets are dropped. The conservative default works well across direct UDP, DERP, IPv4, and IPv6 paths. Increase it only when the entire path supports it; lower it when diagnosing fragmentation or black-hole behavior.

## More Examples

An explicit exit node — only traffic assigned to the policy uses it:

```
[Proxy]
Tailnet Exit = tailscale, section-name=tailnet-exit, test-timeout=8

[Tailscale tailnet-exit]
auth-key = tskey-auth-example
hostname = surge-exit-client
exit-node = office-exit.example-tailnet.ts.net
```

A custom control server with a custom resolver:

```
[Tailscale private-tailnet]
auth-key = tskey-auth-example
control-url = https://control.example.com
hostname = surge-private
dns-server = 100.64.0.53
```

Chained through another policy (peer traffic uses DERP over the upstream; direct UDP is disabled):

```
[Proxy]
Tailnet via Proxy = tailscale, section-name=chained-tailnet, underlying-proxy=Upstream
```

A test URL inside the tailnet — the URL must resolve and route through it:

```
[Proxy]
Office Tailnet = tailscale, section-name=office, test-url=http://health.office.example-tailnet.ts.net/, test-timeout=8
```

## Routing and Transport

Each authorized peer arrives with a set of allowed IP prefixes. Surge builds separate IPv4 and IPv6 route tables and uses the most specific matching route for each outbound packet: a `100.x.y.z/32` route reaches an individual node, a subnet route such as `10.20.0.0/16` reaches the authorized subnet router advertising it, and a default route represents exit-node capability (handled per `exit-node`). If no route matches, the packet cannot be delivered — Surge never bypasses the policy and sends it directly.

Surge creates a WireGuard tunnel per usable peer, may proactively handshake online peers, advances the WireGuard timers on a shared schedule, and rehandshakes expired tunnels that active connections depend on. Encrypted packets are handed to MagicSock, which chooses a direct endpoint or DERP relay path.

**Direct UDP paths.** When the effective underlying policy is DIRECT and `derp-only` is disabled, Surge opens physical UDP sockets bound to the primary physical interface (so Tailscale's own transport packets do not loop back into the Surge virtual interface). An IPv6 socket is opened only when the network provides IPv6 connectivity; its absence does not prevent IPv4 direct paths or DERP.

**DERP relay.** DERP provides a relay path when direct connectivity is unavailable or not yet discovered — a valid working state, just with higher latency. Surge picks a provisional DERP region, later refined by netcheck latency measurements; the home DERP connection is established during startup, other regions are opened lazily, and home-region reconnects use increasing backoff.

**Netcheck and discovery.** After the DERP map and sockets are ready, Surge runs network checks at most about once per minute: it probes STUN endpoints for public reflexive addresses, measures DERP reachability, and reports updated endpoints and the preferred region to the control plane. When no trusted direct path exists, traffic flows through DERP while rate-limited peer endpoint discovery probes candidates and exchanges endpoint information via DERP. A responsive direct endpoint is trusted for a short interval, active paths receive heartbeats, unanswered pings expire, and an alternative endpoint replaces the current best one only when meaningfully faster, avoiding path flapping. Runtime peer status shows whether the current path is `direct` or `relay`, with the endpoint and measured latency.

## DNS and MagicDNS

Surge picks resolvers in order: `dns-server` from the section, then resolvers delivered by the control plane. The list is private to this policy; it does not replace the device's system DNS.

When MagicDNS is enabled, Surge synthesizes local DNS records from the local node's DNS name and addresses, each visible peer's DNS name and addresses, and extra records supplied by the control plane. Names are normalized to lowercase without a trailing dot; both IPv4 and IPv6 records may be present, with `prefer-ipv6` steering the choice. Control-plane search domains are applied to the policy DNS client, though fully qualified names remain the clearest choice in profiles and diagnostics.

DNS queries themselves travel through the Tailscale policy, so an upstream resolver address needs a matching peer route. If names appear in runtime status but external tailnet DNS queries time out, verify the resolver address and its authorized route.

## Lifecycle

The session has four runtime states: `idle` (networking not running), `starting`, `ready`, and `failed` (terminal startup or authorization error). By default the session starts after profile load and stays active even when unused, keeping control and relay state warm; with a positive `idle-keepalive` it may stop and restart on demand.

Persistent machine, node, and network-lock key material lives in application-support storage (state file named from the auth-key hash or, for interactive login, the section name; the path-discovery key is ephemeral). This lets a session restart without replacing its cryptographic identity — protect that storage as you would the auth key. Registration requests a non-ephemeral node: Surge fetches the control server key, establishes a Noise-based control transport, registers over HTTP/2 with the machine/node/network-lock keys, hostname, endpoints, and credentials, then starts the streaming map request. Runtime control stages appear as `idle`, `fetching-key`, `connecting`, `registering`, `map-streaming`, or `closed`.

The control stream delivers full maps (which rebuild peer and route state, reusing tunnels whose node keys are unchanged) and incremental changes. If no map frame arrives for about 150 seconds, Surge reconnects the stream; transient control errors retry with increasing delay from roughly 100 milliseconds up to 30 seconds, preserving the data plane where possible. An authorization failure is terminal for the current attempt: Surge tears down networking, reports the error, and fails new operations quickly; corrected configuration, a fresh sign-in, or a network change permits a new attempt (the network-change retry also covers false authorization symptoms from captive portals or TLS interception). The session becomes ready as soon as it has a valid network map and usable data plane — it does not wait for the home DERP connection.

A network change invalidates old sockets; control and transport state are rebuilt, peer data is refreshed from the new netmap, and always-on sessions warm up again without waiting for traffic.

## Policy Testing

The test mode is decided statically from the configuration, not from live session state:

- **No configured exit node and no explicit `test-url`** — the policy is treated as peer-to-peer, and Surge measures tunnel reachability with the native Tailscale connectivity probe: it prepares the session, then probes a bounded set of eligible online peers with Tailscale discovery ping (preferring peers with a trusted direct path), or pings the home DERP connection when no eligible peer is available. The result indicates whether the measured path is direct or relay; the reported RTT excludes session initialization time.
- **A configured exit node (`auto` or explicit) or an explicit `test-url`** — the policy is expected to provide Internet egress, so Surge uses the standard URL test: an HTTP `HEAD` request through the policy. When the server permits connection reuse, a subsequent request yields a latency less dominated by connection setup. If a configured exit node is not currently usable (offline, ambiguous, or unmatched), the URL test runs and fails rather than silently falling back to the peer probe, surfacing the misconfiguration.

Both modes add up to 10 extra seconds for initialization and handshake work on top of the effective test timeout; the allowance and the probe budget share a single deadline rather than being applied twice.

The runtime status view shows the session state and control stage, hostname and control URL, local addresses and MagicDNS name, effective underlying policy and transport mode, connection counts, exit-node selector/candidates/selection, DERP regions, UDP ports and reported endpoints, last netcheck age, DNS configuration and synthesized records, and per-peer online state, path type, latency, and exit-node eligibility. The offered test controls follow the same static classification: a peer-to-peer policy exposes only the RTT test (throughput, UDP, and NAT-type tests require Internet egress), while an exit-node policy exposes the full set. The comprehensive network diagnostics follows it too: a peer-to-peer policy is covered by the RTT probe and reported as skipped in the UDP relay step, and `test-policy-udp` fails immediately with a not-applicable error instead of timing out. A policy torn down by `idle-keepalive` may show little peer or transport information until something restarts it — this is expected.

## Troubleshooting

- **Registration fails immediately.** Check for a missing/expired/revoked/malformed auth key, a consumed single-use key, both or neither login method configured, missing interactive-login state, a key that requires interactive authorization, a server-side rejection of the hostname/tags/registration, or clock, TLS-interception, or captive-portal problems. Replace the key or sign in again from the policy editor; a network change permits a retry after a captive-portal failure.
- **The policy remains in `starting`.** Read the control stage: `fetching-key`/`connecting` point to control URL, DNS, TLS, or rule-selected outbound issues; `registering` to auth or authorization issues; `map-streaming` means Surge may still be waiting for an address, DERP map, or usable data plane. Verify the ControlURL rule does not recursively select this policy, and that any `underlying-proxy` group resolves to a working final policy.
- **The session has no local address.** The control plane assigns tailnet addresses; confirm the node is authorized and the netmap includes them.
- **A peer is visible but unreachable.** Verify the peer is online, ACLs permit the traffic, the destination is within the peer's delivered routes, any subnet route is approved, the packet fits the MTU, and the service is listening. A `relay` path is slower but should work; if nothing works, inspect handshake and DERP status.
- **Direct connectivity is never established.** Expected with `derp-only = true` or a non-DIRECT `underlying-proxy`; otherwise restrictive NAT, firewalls, blocked UDP, or missing IPv6 may force DERP relay.
- **`exit-node = auto` selects nothing.** More than one candidate is online (configure an explicit selector) or none is usable (verify default-route advertisement and approval). An explicit selector must uniquely match an online candidate — check spelling, suffix, stable ID, address, and approval; there is no fallback.
- **MagicDNS names do not resolve.** Check that MagicDNS is enabled in runtime DNS status, the name appears in synthesized records, the expected search domain was delivered, a custom `dns-server` is not overriding the intended resolver, and the resolver IP has a route through the policy. Try the FQDN and the tailnet IP to separate DNS from routing problems.
- **A URL test fails while tailnet connections work.** Without an exit node, a public URL is usually not routed through the policy: remove `test-url` to use the native probe, or use a tailnet-reachable URL. With an exit node, confirm it is selected and online. A first test may take the timeout plus the 10-second initialization allowance.
- **First use after inactivity is slow.** Occurs with a positive `idle-keepalive`: the session must restart networking and handshake again. Remove the option (or set `0`/`-1`) for always-on behavior.
- **Large transfers stall.** The configured MTU may exceed the path MTU; return to `mtu = 1280` or lower while testing.

Operational guidance: prefer HTTPS control URLs; limit auth-key lifetime, reuse, tags, and ACLs; remember an exit node can observe and egress the traffic assigned to it, so select it explicitly when multiple candidates exist; treat a custom control server and DERP infrastructure as part of the trust boundary; review control-plane ACLs and route approvals rather than relying only on Surge rules.

---

Tailscale is a trademark of Tailscale Inc. This document describes Surge's compatible policy implementation and its behavior; it does not describe every feature of the standalone Tailscale client or control service.
