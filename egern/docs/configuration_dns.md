# DNS
Egern's DNS subsystem supports multiple protocols (UDP, DoT, DoH, DoQ, DoH3) and lets you route different domains to different upstream DNS groups via Forward rules. Egern has two internal resolution paths:
  * **Default DNS** : resolves domain names for user traffic. Goes through Forward rules and falls back to Bootstrap on no-match. Connections to upstreams follow the proxy rules.
  * **Proxy DNS** : used by proxy servers to resolve destination domains. Connections to upstreams are forced to be direct, avoiding a DNS → proxy → DNS dependency loop. When `proxy_nameservers` is configured, every proxy-DNS query is forced through that list (**Forward rules are bypassed**); when unset, the proxy DNS shares the Forward rules with the default DNS and falls back to Bootstrap on no-match.
## Resolution Flow​
Each query goes through these stages in order:
  1. **Hosts** : if a local mapping matches, return the IP directly, or continue resolving the mapped domain as an alias.
  2. **Forward** : rules are evaluated in order; the first matching rule selects the upstream. SSID/BSSID/Cellular rules depend on current network state, and the matching cache is cleared when the network changes. The proxy DNS skips this stage entirely when `proxy_nameservers` is configured — every query goes straight to that list.
  3. **Default upstream** : used when no Forward rule matches — the default DNS falls back to Bootstrap; the proxy DNS also falls back to Bootstrap when `proxy_nameservers` is not configured.
  4. **Block IPs** : records in the response matching `block_ips` are filtered out; if all records are filtered, the resolution is treated as failed.
## Bootstrap (Startup DNS)​
`bootstrap` configures the DNS servers used during startup. It only supports plain UDP (port 53) and never goes through proxy rules — traffic is always direct. It serves two purposes:
  1. Resolve the hostnames of encrypted DNS servers in `upstreams` (`tls://`, `https://`, etc.).
  2. Act as the final DNS fallback (see "Resolution Flow" above).
Supported values:
  * An IP or `IP:port`, e.g. `1.1.1.1`, `8.8.8.8:53`.
  * The special value `system`, which merges in system DNS servers (the ones provisioned by Wi-Fi/cellular).
If unset or unparsable, Egern automatically falls back to the system DNS servers.
    dns:  
      bootstrap:  
        - system        # merge system DNS  
        - 223.5.5.5     # plus a custom server  
## Upstreams (DNS Server Groups)​
Defines named groups of encrypted DNS servers, referenced by Forward rules via the group name. Servers within a group race in parallel; the fastest response wins.
Supported server formats:
Format| Protocol| Default Port  
---|---|---  
`1.1.1.1` or `1.1.1.1:53`| Plain UDP| 53  
`udp://1.1.1.1`| Plain UDP| 53  
`tls://1.1.1.1`| DNS over TLS| 853  
`https://8.8.8.8/dns-query`| DNS over HTTPS| 443  
`quic://dns.adguard-dns.com`| DNS over QUIC| 853  
`h3://dns.example.com/dns-query`| DNS over HTTP/3| 443  
`bootstrap`| Expands to all Bootstrap servers| —  
`system`| Expands to all system DNS servers| —  
A Forward rule's `value` may reference a group name from `upstreams`. The default DNS always honors Forward rules, so it can use any of these groups; the proxy DNS only reaches them via Forward when `proxy_nameservers` is unset (Forward is skipped once `proxy_nameservers` is configured).
    dns:  
      upstreams:  
        google:  
          - https://8.8.8.8/dns-query  
          - https://8.8.4.4/dns-query  
        adguard:  
          - quic://dns.adguard-dns.com  
## Forward (DNS Forwarding Rules)​
Rules are evaluated in declaration order; the first matching rule routes the query to its upstream. The default DNS always uses these rules; the proxy DNS only goes through Forward when `proxy_nameservers` is unset (otherwise it bypasses Forward and goes straight to `proxy_nameservers`).
Supported match types:
Type| Description  
---|---  
`domain`| Exact match on the full domain  
`domain_keyword`| Substring match on the domain  
`domain_suffix`| Suffix match aligned on `.` boundaries: `match: cn` matches `cn` and `example.cn`, but not `examplecn`  
`domain_wildcard`| Glob pattern (`*` / `?`), case-insensitive. e.g. `*.google.com`  
`domain_regex`| PCRE2 regex, `find`-style — any substring hit counts  
`proxy_rule_set`| Reference to a precompiled remote rule set  
`ssid`| Glob match against the current Wi-Fi SSID  
`bssid`| Glob match against the current Wi-Fi BSSID  
`cellular`| Glob match against the current cellular radio type, e.g. `LTE`, `NR`  
Fields per rule:
  * **match** (string), required
The match condition; semantics depend on the rule type.
  * **value** (string), required
The target upstream. May be:
    * A group name defined in `upstreams`.
    * A single DNS server address, e.g. `tls://1.1.1.1` (an implicit upstream — equivalent to a group containing just that one address).
    * The special value `bootstrap` — use the Bootstrap DNS.
    * The special value `system` — use the system DNS.
    * The special value `reject` — refuse the query and return an empty response.
  * **disabled** (bool), optional
Disables this rule. Defaults to `false`.
  * **update_interval** (integer), optional
Rule-set auto-update interval in seconds; only applies to `proxy_rule_set`. Defaults to `86400`. A value `<= 0` disables auto-update.
## Hosts (Host Mapping)​
Maps a hostname (a domain or IP) by glob pattern to one or more IPs/domains. Patterns are matched in declaration order; the first match wins. When a match is found:
  * All values are IPs → return them directly.
  * Any value is a domain → resolve those domains as aliases (going back through Forward).
    dns:  
      hosts:  
        "*.google.com": 142.250.80.46  
        "example.com": www.example.com         # domain → another domain  
        "192.168.1.100": internal.example.com  # reverse-style IP → domain  
        "cdn.example.com":                     # multiple values  
          - 1.2.3.4  
          - 5.6.7.8  
## Proxy Nameservers (Forced Upstream for Proxy DNS)​
When configured, every proxy DNS query is forced through these servers and **Forward rules are bypassed** — this keeps the "DNS used by the proxy" semantic explicit: configuring it acts as a hard override. All connections are direct (never through the proxy chain), avoiding a DNS → proxy → DNS dependency loop. Supports the same protocol formats as Upstreams.
When unset, the proxy DNS shares the same Forward rules as the default DNS and falls back to Bootstrap on no-match.
    dns:  
      proxy_nameservers:  
        - tls://dns.google  
        - https://cloudflare-dns.com/dns-query  
        - quic://dns.adguard-dns.com  
## Block IPs​
Filter matching IPs out of DNS responses (useful against DNS poisoning). Supports IPv4, IPv6 and CIDR:
    dns:  
      block_ips:  
        - 0.0.0.0  
        - 127.0.0.1  
        - 10.0.0.0/8  
        - "::1"  
A resolution is treated as failed only when **all** records are filtered out; otherwise the remaining records are returned.
## Skip TLS Verify​
Skip TLS certificate verification for encrypted DNS upstreams (`tls://`, `https://`, `quic://`, `h3://`). Only enable this when an upstream uses a self-signed certificate (e.g. a self-hosted AdGuardHome). Otherwise leave it disabled.
    dns:  
      skip_tls_verify: true  
## Public IP Lookup URL​
Optional. An HTTP/HTTPS URL that returns the device's public IP as plain text. Egern fetches it periodically and includes the result as an EDNS Client Subnet (ECS) parameter on upstream queries, helping CDNs return geographically closer answers.
    dns:  
      public_ip_lookup_url: https://ifconfig.me/ip  
## Full Example​
    dns:  
      bootstrap:  
        - system  
      upstreams:  
        google:  
          - https://8.8.8.8/dns-query  
          - https://8.8.4.4/dns-query  
        adguard:  
          - quic://dns.adguard-dns.com  
      forward:  
        - domain:  
            match: "internal.example.com"  
            value: "192.168.1.1"  
        - domain_suffix:  
            match: "cn"  
            value: bootstrap  
        - domain_keyword:  
            match: "taobao"  
            value: bootstrap  
        - domain_wildcard:  
            match: "*.cn"  
            value: bootstrap  
        - proxy_rule_set:  
            match: "https://example.com/china-domains.list"  
            value: bootstrap  
            update_interval: 86400  
        - domain_regex:  
            match: "^ad\\..*|^ads\\..*"  
            value: reject  
        - ssid:  
            match: "MyHome*"  
            value: bootstrap  
        - bssid:  
            match: "AA:BB:CC:*"  
            value: bootstrap  
        - cellular:  
            match: "NR"  
            value: google  
        - domain_wildcard:  
            match: "*"  
            value: google  
      hosts:  
        example.com: www.example.com  
        localhost: 127.0.0.1  
        "*.local": 192.168.1.1  
      proxy_nameservers:  
        - tls://dns.google  
        - https://1.1.1.1/dns-query  
      block_ips:  
        - 0.0.0.0  
        - 127.0.0.1  
      skip_tls_verify: false  
      public_ip_lookup_url: https://ifconfig.me/ip  
## FAQ​
**Why is Bootstrap still needed when Upstreams are configured?**
Encrypted DNS entries in `upstreams` (`tls://dns.google`, `https://cloudflare-dns.com/...`) need their hostnames resolved to IPs before a connection can be established — that step uses Bootstrap. Bootstrap therefore must be plain UDP DNS reachable by IP; it cannot itself depend on the encrypted upstreams it is meant to bootstrap.
**Which DNS is used when no Forward rule matches?**
The default DNS falls back to Bootstrap. The proxy DNS depends on `proxy_nameservers`: when unset, it goes through Forward rules and falls back to Bootstrap on no-match; once configured, every proxy DNS query is sent straight to `proxy_nameservers` and never enters Forward matching at all.
**Why must Proxy Nameservers be direct?**
A proxy server (Trojan, Shadowsocks, etc.) needs the destination domain resolved to an IP before it can establish a proxy connection. If the proxy DNS itself went through the proxy, you'd have a dependency loop. Direct connections break that loop.