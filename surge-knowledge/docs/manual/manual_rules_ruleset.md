# Rule Set

The RULE-SET rule references a bundle of rules — built into Surge, embedded in the profile, or loaded from a file or URL — and applies one policy to every request matched by any rule in the set. Use it to keep long rule lists out of the main profile and to share lists between profiles.

```
RULE-SET,https://example.com/streaming.list,Proxy
RULE-SET,LAN,DIRECT
```

The value is resolved in this order:

1. An internal rule set name (`SYSTEM` or `LAN`).
2. An inline rule set: the name of a `[Ruleset <name>]` section in the profile.
3. An external resource: an `http://`/`https://` URL, or a local file path (absolute, or relative to the profile directory).

## Internal Rule Sets

Surge provides two built-in rule sets.

{% hint style='info' %}
The internal rule set contents may change between Surge versions. The listings below reflect the current version; check the rule set details in the app for the authoritative list.
{% endhint %}

### SYSTEM

```
RULE-SET,SYSTEM,DIRECT
```

Matches most requests sent by macOS and iOS itself. Requests from the App Store, iTunes, and other content services are not included. Current contents:

```
DOMAIN,api.smoot.apple.com
DOMAIN,captive.apple.com
DOMAIN,xp.apple.com
DOMAIN,configuration.apple.com
DOMAIN,guzzoni.apple.com
DOMAIN,smp-device-content.apple.com
DOMAIN,aod.itunes.apple.com
DOMAIN,mesu.apple.com
DOMAIN,api.smoot.apple.cn
DOMAIN,gs-loc.apple.com
DOMAIN,mvod.itunes.apple.com
DOMAIN,streamingaudio.itunes.apple.com
DOMAIN-SUFFIX,ess.apple.com
DOMAIN-SUFFIX,push-apple.com.akadns.net
DOMAIN-SUFFIX,push.apple.com
DOMAIN-SUFFIX,lcdn-locator.apple.com
DOMAIN-SUFFIX,lcdn-registration.apple.com
DOMAIN-SUFFIX,ls.apple.com
PROCESS-NAME,trustd
PROCESS-NAME,netbiosd
```

### LAN

```
RULE-SET,LAN,DIRECT
```

Matches private and special-purpose IP ranges and the `.local` suffix. Note that this rule set triggers a DNS lookup for domain hostnames (unless `no-resolve` is added to the RULE-SET line). Current contents:

```
DOMAIN-SUFFIX,local
IP-CIDR,0.0.0.0/8
IP-CIDR,10.0.0.0/8
IP-CIDR,100.64.0.0/10
IP-CIDR,127.0.0.0/8
IP-CIDR,169.254.0.0/16
IP-CIDR,172.16.0.0/12
IP-CIDR,192.0.0.0/24
IP-CIDR,192.0.2.0/24
IP-CIDR,192.168.0.0/16
IP-CIDR,224.0.0.0/4
IP-CIDR6,::1/128
IP-CIDR6,fc00::/7
IP-CIDR6,fe80::/10
```

## Inline Rule Sets {{ book.VER | replace("%TEXT%", "Mac 5.3.1+") }}

Instead of hosting the list externally, you can embed the rules directly in the profile as a `[Ruleset <name>]` section and reference the section name:

```
[Ruleset Streaming]
DOMAIN-SUFFIX,netflix.com
DOMAIN-SUFFIX,netflix.net
DOMAIN,netflixdnstest0.com

[Rule]
RULE-SET,Streaming,StreamingProxy
```

Inline rule sets use the same line syntax as external files and benefit from the same preprocessing optimizations. Modules can also contribute inline rule sets.

Starting with Surge Mac 6.9.0 and Surge iOS 5.22.0, inline rule sets and local file rule sets can be created and edited directly from the rule editor UI, including reordering and toggling individual rules.

## External Rule Sets

The rule set file is a plain text file with one rule per line, written without the policy component:

```
# Comment lines start with #, // or ;
DOMAIN-SUFFIX,example.com
DOMAIN,cdn.example.org,extended-matching
IP-CIDR,203.0.113.0/24,no-resolve
IP-ASN,13335
```

- Per-line options such as `no-resolve` and `extended-matching` are allowed.
- `FINAL` and the `pre-matching` flag are not allowed inside a rule set file.
- Invalid lines are skipped with a warning; they do not invalidate the whole set.
- A set may contain at most 1,000,000 entries.

External rule sets are downloaded and cached. Local files are watched and reloaded automatically when they change. The same URL or file path cannot be used as both a RULE-SET and a DOMAIN-SET in one profile.

## Nested Rule Sets {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

An inline `[Ruleset <name>]` section may itself contain `RULE-SET` and `DOMAIN-SET` lines, referencing another inline section, a built-in set, or an external file or URL. External sets referenced this way are downloaded and cached like those referenced from `[Rule]`.

```
[Ruleset Media]
RULE-SET,Streaming
RULE-SET,https://example.com/music.list
DOMAIN-SUFFIX,video.example

[Ruleset Streaming]
DOMAIN-SUFFIX,stream.example
```

Circular references between inline rule sets are rejected when the profile is loaded. Nesting is limited to 8 levels; deeper chains are treated as a mismatch.

## Options on the RULE-SET Line

Options on the RULE-SET line apply to the whole set:

#### no-resolve

Removes the set's DNS requirement and forces `no-resolve` on every sub-rule. IP-based sub-rules are then skipped for domain hostnames that have not been resolved yet, instead of triggering a DNS lookup.

#### extended-matching

Forces extended matching on every sub-rule: domain rules in the set also match against the TLS SNI and HTTP Host header. Note that if any domain rule inside the set file already carries the flag, it is applied to all domain rules of that set.

#### update-interval

Optional, seconds, default 86400 (24 hours).

Re-download interval for URL-based rule sets. Set a negative value (e.g. `-1`) to disable automatic updates.

```
RULE-SET,https://example.com/social.list,Proxy,no-resolve,extended-matching,update-interval=43200
```

#### pre-matching

A RULE-SET rule may be flagged `pre-matching` if the policy is a REJECT-family policy; the whole set then participates in the pre-matching phase. See [Rules Overview](overview.md) for how pre-matching works.

## Performance

Rule sets are preprocessed into indexes when loaded, so even very large sets match efficiently:

- DOMAIN and DOMAIN-SUFFIX entries are compiled into a domain index; sets with more than 1000 domain entries use an on-disk database instead of an in-memory tree.
- If a set contains more than 50 IP-CIDR (or IP-CIDR6) entries, they are compiled into a binary IP database.
- IP-ASN entries are checked in constant time.
- All other rule types are evaluated linearly.

When a sub-rule matches, the log records it as `Sub-rule matched: <rule> (in <set name>)`.

## RULE-SET vs. DOMAIN-SET

A [DOMAIN-SET](domain.md) file is a plain list of hostnames (one per line, with an optional leading dot for suffix matching) and can only match domains. A RULE-SET file contains full rule declarations of any type valid in a set. For pure domain lists, DOMAIN-SET files are simpler to maintain; RULE-SET is required as soon as the list mixes rule types.

The `[Host]` section also accepts `RULE-SET:` and `DOMAIN-SET:` prefixes as match keys for DNS mapping; see [Local DNS Mapping](../dns/local-dns-mapping.md).
