# Advanced DNS Topics

This page describes how DNS behaves when the Surge virtual network interface (VIF) is active — in [Enhanced Mode](../features/enhanced-mode.md), the iOS VPN tunnel, or gateway mode — and the options that control it.

## The Fake-IP DNS Responder

When the VIF is active, Surge runs its own DNS responder, and the system (or the client devices in gateway mode) is configured to use it. The responder listens on designated addresses:

- macOS: `198.18.0.2` (also advertised via DHCP in gateway mode)
- iOS: `198.18.0.4`
- IPv6: `fd00:6152::2`

Any query sent to an address in the range `198.18.0.2`–`198.18.0.9` is treated as addressed to Surge's DNS responder.

For ordinary A and AAAA questions, the responder does not perform a real lookup. Instead, it instantly answers with a **fake IP address** from the reserved block `198.18.0.0/15` (IPv4 pool `198.18.1.1`–`198.19.255.254`; IPv6 fake addresses use a dedicated prefix under `fd00:6152::`). Surge remembers the fake IP ⇄ domain mapping persistently. When a connection to a fake IP arrives through the VIF, Surge converts it back to the original domain for rule matching and outbound handling. This design means:

- No DNS latency is added before the connection starts; the real lookup happens only if the matched policy actually needs an IP address.
- Rules always see the original domain, even for clients that resolve addresses themselves.

Fake answers use a short TTL (5 seconds on iOS, 30 seconds on macOS) so that clients re-query frequently and stale mappings disappear quickly. A query only receives fake addresses for the address family it arrived over: an AAAA question arriving over IPv4 gets an empty answer, and vice versa, so clients only get fake IPs they can actually route to Surge.

Queries that are not simple A/AAAA questions (such as TXT or MX) are forwarded to the upstream DNS servers, using the same server configuration as the [internal DNS client](overview.md). [Local DNS Mapping](local-dns-mapping.md) `server:` items are honored for forwarded queries as well.

## hijack-dns

By default, only queries sent to the designated Surge DNS addresses are answered with fake IPs; queries sent to a standard DNS server pass through normally.

Some devices or software always use a hardcoded DNS server (for example, Google speakers always use 8.8.8.8). Use the `hijack-dns` parameter in `[General]` to intercept those queries so they also receive fake addresses:

```
[General]
hijack-dns = 8.8.8.8:53, 8.8.4.4:53
```

Each entry is an IPv4 address or `*`, with an optional port (default 53). Use `hijack-dns = *:53` to hijack all DNS queries. Only packets that parse as valid DNS queries are hijacked; other traffic to the listed destinations passes through unaffected.

## always-real-ip

Some scenarios require the client to receive a real, routable IP address instead of a fake one — for example, NAT-type detection for game consoles, or hostnames used by VPN clients. The `always-real-ip` parameter exempts domains from the fake-IP mechanism:

```
[General]
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

The value is matched against the query domain with wildcard support; it is a Host List parameter, see [Host List Parameter Type](../profile/host-list.md) for the detailed rules. Matching queries are forwarded to the upstream DNS servers and the real answer is returned to the client.

For exempted domains, `[Host]` IP mappings are answered authoritatively by the responder. For all other domains, the client still receives a fake IP, and any `[Host]` mapping takes effect later when Surge establishes the real connection.

## allow-dns-svcb

Optional, Boolean, default: false

Modern systems may perform an SVCB/HTTPS (type 65) record lookup instead of a standard A record lookup. Such answers can carry IP hints, which would bypass the fake-IP mechanism. By default, Surge rejects these queries as not-implemented, forcing the client to fall back to a standard A record lookup. Enable this option only if you need SVCB/HTTPS records to pass through.

## REJECT at DNS Time

Domain-based rules flagged `pre-matching` with a REJECT-family policy are enforced by the DNS responder itself: a matching query is answered with no record (REJECT), silently dropped (REJECT-DROP), or answered with the special sink address `198.18.0.244` (REJECT-NO-DROP), so the request is blocked before any connection is attempted. See [REJECT Policy](../policies/reject.md) for details.

## Related Options

- **`dns-follow-interface`** — a policy parameter that binds the DNS lookup for a connection to the same network interface as the connection itself. See [Policy Parameters](../policies/parameters.md).
- **`no-resolve`** — a flag on IP-based rules that prevents them from triggering DNS lookups during rule evaluation. See [IP-Based Rules](../rules/ip.md).
- **`dns-failed`** — a flag on the FINAL rule that controls behavior when rule evaluation cannot finish due to a DNS failure. See [FINAL](../rules/final.md).

{% hint style='info' %}
The responder answers the canary domain `use-application-dns.net` with NXDOMAIN, which tells Firefox to disable its built-in DNS over HTTPS and keep using the system resolver, so that Surge can continue to see the domains being requested.
{% endhint %}
