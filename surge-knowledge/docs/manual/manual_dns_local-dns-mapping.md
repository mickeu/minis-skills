# Local DNS Mapping

Surge supports local DNS mapping with the `[Host]` section. It is similar to `/etc/hosts`, but with more powerful features, including wildcards, aliases, per-domain DNS server assignment, and script-based resolution.

```
[Host]
abc.com = 1.2.3.4
*.dev = 6.7.8.9
foo.com = bar.com
bar.com = server:8.8.8.8
```

Items are evaluated top to bottom, and the first matching item wins. Local DNS mapping applies to Surge's internal DNS client and to the fake-IP DNS responder in [Enhanced Mode](advanced.md). The hostnames of your proxy servers are never matched against `[Host]` items, to avoid resolution loops.

## IP Address Mapping

Map a hostname to a fixed IP address. Surge answers the mapping authoritatively without querying any upstream server.

```
[Host]
abc.com = 1.2.3.4
```

Multiple addresses may be given as a comma-separated list, and IPv4 and IPv6 addresses may be mixed:

```
[Host]
abc.com = 1.2.3.4, 5.6.7.8, ::1
```

## Wildcards

Patterns may use the wildcards `*` (any sequence of characters) and `?` (a single character). Surge uses simple string matching against the whole hostname. For example, `*google.com` matches `google.com`, `foo.google.com`, and `bargoogle.com`. `*.google.com` does **not** match `google.com`.

```
[Host]
*.dev = 6.7.8.9
```

## Alias

An alias works like a CNAME record: the value is another hostname, and the lookup is restarted with that name.

```
[Host]
foo.com = bar.com
```

## Assigning DNS Servers

You can assign specific DNS servers to one or more domains with a `server:` value.

```
[Host]
bar.com = server:8.8.8.8
```

Each server is an IP address with an optional port (default 53) or an encrypted DNS URL ([any supported scheme](encrypted-dns.md)):

```
[Host]
example.com = server:https://cloudflare-dns.com/dns-query
```

Multiple DNS servers can be specified as a comma-separated list. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

```
[Host]
bar.com = server:8.8.8.8,1.1.1.1
```

### System Resolution

Since Surge has its own DNS client implementation, some special hostnames may fail to resolve. Use `server:system` to hand the lookup over to the system:

```
[Host]
Macbook = server:system
```

`server:syslib` is an alias of `server:system`; the two values behave identically. The actual behavior depends on the working mode:

- In normal (proxy) mode, the lookup is performed by the system resolver library.
- In enhanced mode, the query stays inside Surge but is forwarded to the DNS servers currently configured in the operating system, since the traditional system resolver might be bypassed.

`server:force-syslib` always uses the system resolver library, even in enhanced mode. This is intended for special domains such as mDNS names. Do not use it for general domains, because it may cause recursive requests. {{ book.VER | replace("%TEXT%", "Mac 6.4.3+") }}

By default, all hostnames with the `.local` suffix are resolved by the system.

## Script-Based Resolution

Use `script:<name>` to resolve a domain with a DNS script, which may return addresses directly or redirect the query to other servers:

```
[Host]
example.com = script:dnspod
*.example.com = script:dnspod
```

The name refers to a `type=dns` script defined in the `[Script]` section. See [DNS Script](../scripting/dns.md) for the script interface and a complete example.

## Referencing Rule Sets {{ book.VER | replace("%TEXT%", "Mac 5.10.0+") }}

When you already maintain large rule sets or domain sets, reproducing the same list in `[Host]` is tedious. Surge allows binding an entire `DOMAIN-SET` or `RULE-SET` to a DNS mapping entry so that the upstream or IP mapping is shared automatically.

```
[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.example.com/dns-query
RULE-SET:https://example.com/rules.txt = 10.0.0.10
```

`DOMAIN-SET:` expects a domain list, while `RULE-SET:` uses the standard rule set format. Since the matching happens before any DNS resolution, only domain-based entries in a rule set can match; IP-based entries are ignored. This syntax follows the same remote file format described in [Rule Set](../rules/ruleset.md) and is especially helpful for encrypted DNS assignments that need to stay aligned with a managed list.

## /etc/hosts (macOS)

On macOS, Surge reads the entries in `/etc/hosts` and appends them after the profile's `[Host]` items, so profile items take precedence. The file is watched and reloaded automatically when it changes. Set `read-etc-hosts = false` in `[General]` to disable this behavior (it is enabled by default).

## Use Local DNS Items for Proxied Requests

```
[General]
use-local-host-item-for-proxy = true
```

By default, DNS resolution for proxied requests happens on the remote proxy server, because Surge sends proxy requests with the original domain names, and `[Host]` items are bypassed.

After enabling this option, for requests whose target domain matches a local DNS mapping record, Surge sends the proxy request with the mapped IP address instead of the domain. If the record has multiple addresses, one is chosen at random.

It only works for local DNS mapping records using IP addresses; `server:` and `script:` items are not affected.
