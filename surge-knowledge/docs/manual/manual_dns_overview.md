# DNS Overview

Surge uses its own DNS client for all outgoing requests and for rule evaluation. It may behave differently from the DNS client of your operating system, and it is tuned for performance and reliability rather than strict RFC resolver semantics.

Surge's DNS subsystem has two roles:

- **The internal DNS client** resolves domains for connections that Surge itself establishes and for rules that need an IP address (such as `IP-CIDR` and `GEOIP`). Its behavior is described on this page.
- **A DNS responder for the virtual network interface**: when [Enhanced Mode](../features/enhanced-mode.md) or the iOS VPN tunnel is active, DNS queries from the system and other devices are answered by Surge directly, normally with fake IP addresses. See [Advanced DNS Topics](advanced.md).

To customize the upstream servers used by the internal client, see [DNS Servers](dns-server.md) and [Encrypted DNS](encrypted-dns.md). To override results for specific domains, see [Local DNS Mapping](local-dns-mapping.md).

## Concurrent Querying

Surge queries all configured DNS servers simultaneously to improve performance, similar to dnsmasq with the `--all-servers` parameter. The first valid answer wins. Surge iOS and Surge Dashboard show which server responded first.

If no answer arrives within 1 second, Surge resends the query to all servers. After 5 attempts (about 5 seconds in total), the lookup fails with a DNS error.

## A and AAAA Queries

When IPv6 is enabled (`ipv6 = true` in `[General]`) and the current network has IPv6 connectivity, Surge sends both A and AAAA questions in parallel and waits for both answers before completing the lookup. If only one record type has been answered when the retry timer fires, Surge completes the lookup with the partial result.

If 5 consecutive lookups receive an A answer while the AAAA answer times out, Surge concludes that the upstream servers never return AAAA answers on the current network and stops sending AAAA questions. A log event is raised when this happens. AAAA querying resumes after a network change or a DNS cache flush.

## Empty Answers

Some domain names have poorly-performing authoritative name servers, causing upstream DNS servers to return empty answers due to server-side timeout or other connectivity issues. Surge reports an empty DNS answer error only if **all** upstream DNS servers explicitly return empty answers, or if some servers return empty answers and the rest fail to respond in time. An empty answer from a single server never fails the lookup as long as another server returns records.

## Caching

Results are cached according to the TTL of the returned records (the smallest TTL in the record set determines the expiry).

Surge uses optimistic caching: when a cached entry has expired, it is still returned to the caller immediately, while a refresh query runs in the background. This removes DNS latency from repeated connections at the cost of occasionally using a slightly stale address.

The cache holds up to 200 entries on iOS and 2000 entries on macOS, with least-recently-used eviction. The cache is flushed automatically on network changes, and can be flushed manually from the UI, the CLI, or the HTTP API. Identical in-flight lookups are coalesced into a single query.

## Special Hostnames

- **Simple hostnames** (names without a dot, such as `nas`): Surge appends the system's first search domain (`nas` → `nas.example.lan`) and forwards the query to the system DNS servers.
- **Names ending with `.local`**: resolved through the system resolver library by default, so mDNS/Bonjour names keep working. See [Local DNS Mapping](local-dns-mapping.md) for related options.
- **Fully qualified names with a trailing dot** (`example.com.`): the trailing dot is stripped and search-domain rewriting is suppressed.
- **IP literals**: returned as-is without any lookup.
