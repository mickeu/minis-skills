# Domain Rules

Domain rules match the hostname of a request. They are the most common rule types and never trigger a DNS lookup, so they should generally be placed before [IP rules](ip.md).

```
[Rule]
DOMAIN,www.apple.com,Proxy
DOMAIN-SUFFIX,apple.com,DIRECT
DOMAIN-KEYWORD,google,Proxy
```

## Matching Semantics

All domain rule types test the hostname of the request. Matching is case-insensitive, and a trailing root dot in the hostname (`example.com.`) is ignored.

By default only the requested hostname is tested. With the extended-matching parameter described below, the TLS SNI and the HTTP Host header are tested as well.

## Rule Types

#### DOMAIN

```
DOMAIN,www.apple.com,Proxy
```

Matches if the hostname equals the value exactly.

#### DOMAIN-SUFFIX

```
DOMAIN-SUFFIX,apple.com,Proxy
```

Matches the domain itself and all of its subdomains. For example, `DOMAIN-SUFFIX,google.com` matches `google.com`, `www.google.com`, and `mail.google.com`, but does **not** match `content-google.com`.

#### DOMAIN-KEYWORD

```
DOMAIN-KEYWORD,google,Proxy
```

Matches if the hostname contains the value as a substring. Wildcard characters are not interpreted; the value is treated literally.

#### DOMAIN-WILDCARD

```
DOMAIN-WILDCARD,api-*.example.com,Proxy
```

Matches the hostname against a wildcard pattern:

- `*` matches any number of characters, including none. It also crosses dots, so `*.example.com` matches `a.b.example.com`.
- `?` matches exactly one character.
- `[...]` character classes are supported.

Matching is case-insensitive. Use `DOMAIN-WILDCARD` when `DOMAIN-SUFFIX` and `DOMAIN-KEYWORD` are not precise enough, e.g. to match a naming pattern like `cdn?.example.com`.

#### DOMAIN-SET

```
DOMAIN-SET,https://example.com/adblock.txt,REJECT
DOMAIN-SET,my-domains.txt,Proxy
```

Matches the hostname against an external list of domains. Designed for very large lists (such as ad-blocking lists): sets are preprocessed into an index that supports fast lookup for hundreds of thousands of entries. A single set may contain up to 1,000,000 entries.

The value is either a URL (`http://` or `https://`) or a local file path, absolute or relative to the profile directory.

### DOMAIN-SET File Format

The file is plain text with one entry per line:

```
# Exact hostname
example.com

# Leading dot: matches ads.example.org and all of its subdomains
.ads.example.org
```

- A plain line matches the hostname exactly, like a `DOMAIN` rule.
- A line starting with `.` matches the domain itself and all subdomains, like a `DOMAIN-SUFFIX` rule.
- Lines starting with `#` or `//` are comments; blank lines are ignored.
- Invalid lines are skipped with a warning; they do not invalidate the set.

The `DOMAIN-SET` line accepts the `update-interval=<seconds>` parameter to control how often a URL-based set is re-downloaded (default 86400 seconds; a negative value disables auto-updating). Local files are watched and reloaded automatically when changed.

{% hint style='info' %}
If you need to mix domain entries with other rule types in one external file, use [RULE-SET](ruleset.md) instead. The same URL or file cannot be used both as a RULE-SET and as a DOMAIN-SET in one profile.
{% endhint %}

## Parameters

#### extended-matching {{ book.VER | replace("%TEXT%", "iOS 5.8.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.0+") }}

```
DOMAIN-SUFFIX,example.com,Proxy,extended-matching
```

When this parameter is enabled, the rule also tries to match the TLS SNI and the HTTP Host header (or `:authority`). This helps when a client connects to an IP address directly, so the requested hostname alone would not reveal the destination domain.

The parameter is available for `DOMAIN`, `DOMAIN-SUFFIX`, `DOMAIN-KEYWORD`, and `DOMAIN-WILDCARD` rules. To apply it to every entry of a set, append the parameter to the corresponding `DOMAIN-SET` or `RULE-SET` line.

#### pre-matching {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

All domain rule types support the `pre-matching` parameter with REJECT-family policies, allowing requests to be rejected at the DNS and TCP-handshake stages. See [REJECT Policy](../policies/reject.md).
