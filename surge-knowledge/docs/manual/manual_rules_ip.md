# IP Rules

IP rules match the destination IP address of a request. There are four IP-based rule types: `IP-CIDR`, `IP-CIDR6`, `GEOIP`, and `IP-ASN`.

```
[Rule]
IP-CIDR,192.168.0.0/16,DIRECT
GEOIP,US,DIRECT
IP-ASN,13335,Proxy
```

## IP Rules and DNS

IP rules need a resolved address to work:

- If the request targets an IP literal, the rule matches it directly; `GEOIP` and `IP-ASN` perform their database lookup without a DNS query.
- If the request targets a domain, Surge performs a DNS lookup when evaluation reaches the first IP-based rule, then resumes evaluation with the result. `IP-CIDR` and `GEOIP`/`IP-ASN` lookups test the first IPv4 record of the result (falling back to the IPv6 record for `GEOIP`/`IP-ASN`); `IP-CIDR6` tests the first IPv6 record.
- If the DNS lookup fails, rule evaluation aborts and the request fails with a DNS error, unless the FINAL rule carries the [dns-failed](final.md) parameter.

To avoid the lookup, append the [no-resolve](#no-resolve) parameter.

## Rule Types

#### IP-CIDR

```
IP-CIDR,192.168.0.0/16,DIRECT
IP-CIDR,10.0.0.0/8,DIRECT
IP-CIDR,172.16.0.0/12,DIRECT
IP-CIDR,127.0.0.0/8,DIRECT
```

Matches if the destination IPv4 address falls in the specified range.

Since Surge Mac 6.0.0, you may also provide a single IPv4 address without the `/` mask. It is treated as `/32`:

```
IP-CIDR,8.8.8.8,Proxy
```

#### IP-CIDR6

```
IP-CIDR6,2001:db8:abcd:8000::/50,DIRECT
```

Matches if the destination IPv6 address falls in the specified range.

Single IPv6 addresses are supported too — writing `IP-CIDR6,2404:6800::`, for example, is equivalent to `/128`.

#### GEOIP

```
GEOIP,US,DIRECT
```

Matches if the destination IP address belongs to the specified country, according to the GeoIP database. The value is an ISO country code and is case-insensitive.

#### IP-ASN

```
IP-ASN,13335,Proxy
```

Matches if the destination IP address belongs to the specified autonomous system. The value is a decimal ASN; an `AS` prefix is also accepted (`IP-ASN,AS13335,Proxy`).

## Unknown Database Results {{ book.VER | replace("%TEXT%", "iOS 5.102.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.1+") }}

Use `UNKNOWN` (case-insensitive) to match a destination IP for which the database lookup returns no country or ASN:

```
GEOIP,UNKNOWN,Proxy
IP-ASN,UNKNOWN,Proxy
```

`GEOIP,UNKNOWN` matches an empty country result; `IP-ASN,UNKNOWN` matches an empty ASN result. Both forms also work in rule sets, where the policy is omitted.

These rules require a destination IP. An unresolved domain is not an unknown database result: normal DNS resolution and `no-resolve` behavior still apply.

## Parameters

#### no-resolve

```
GEOIP,US,DIRECT,no-resolve
IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
```

With this parameter, the rule is skipped for requests targeting a domain whose address has not been resolved yet, instead of triggering a DNS lookup. The rule still matches requests that target IP literals.

{% hint style='info' %}
If some domains cannot be resolved by the local DNS server, make sure no IP-based rule without `no-resolve` appears before the rule that matches those domains. Otherwise rule evaluation fails with a DNS error. Adding `no-resolve` to the IP-based rules, or adding [dns-failed](final.md) to the FINAL rule, avoids the issue.
{% endhint %}

#### pre-matching {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

All four IP rule types support the `pre-matching` parameter with REJECT-family policies. See [REJECT Policy](../policies/reject.md).

## GeoIP and ASN Databases

#### GeoIP country database

`GEOIP` rules use a MaxMind GeoLite2 country database. A copy is bundled with Surge, and Surge periodically downloads updates. Two `[General]` settings control this (see [General Settings](../profile/general.md)):

- `geoip-maxmind-url`: the download URL for database updates. The default is `https://nssurge.com/resource/geoip-database.tar.gz`. You may point it to another source; both a `.tar.gz` archive containing `GeoLite2-Country.mmdb` and a raw `.mmdb` file are accepted.
- `disable-geoip-db-auto-update`: set to `true` to disable automatic updates. You can still update the database manually from the app UI.

#### ASN database

`IP-ASN` rules use a bundled GeoLite2 ASN database, which is updated together with app updates. There is no configuration key for it and no separate download mechanism.
