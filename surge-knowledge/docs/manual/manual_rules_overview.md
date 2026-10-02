# Rules Overview

Surge decides how to handle every request by testing it against the rule list in the `[Rule]` section of the profile. Each rule pairs a matching condition with a policy: forward the request to a proxy, connect directly, or reject it.

```
[Rule]
DOMAIN-SUFFIX,company.com,ProxyA
DOMAIN-KEYWORD,google,DIRECT
GEOIP,US,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
FINAL,ProxyB
```

## Composition

Each rule consists of three parts: a rule type, a value to match, and a policy.

```
           TYPE,          VALUE,          POLICY
Example:   DOMAIN-SUFFIX, apple.com,      DIRECT
           IP-CIDR,       192.168.0.0/16, ProxyA
```

- **TYPE**: one of the rule types listed in the [index below](#rule-type-index).
- **VALUE**: what the rule matches against. The `FINAL` rule has no value. If a value contains commas (e.g. a regex), wrap it in double or single quotes.
- **POLICY**: the name of a [proxy policy](../policies/overview.md), a [policy group](../policy-groups/overview.md), a [built-in policy](../policies/built-in.md) such as `DIRECT` or the [REJECT family](../policies/reject.md), or a `DEVICE:<name>` policy targeting a [Surge Ponte](../features/ponte.md) device.

Optional parameters may be appended after the policy, separated by commas:

```
IP-CIDR,192.168.0.0/16,DIRECT,no-resolve
```

Inline comments starting with `//`, `#`, or `;` are allowed at the end of a rule line.

The rule list must end with an enabled [FINAL rule](final.md), which defines the default policy for requests that match nothing else.

## Evaluation Order

Rules are evaluated strictly from top to bottom. The first rule that matches decides the policy; all later rules are ignored. Order your rules from most specific to most general.

Two things bypass the normal top-to-bottom evaluation:

- Rules tagged with `pre-matching` are extracted and checked before everything else (see [Pre-matching](#pre-matching)).
- When the outbound mode is set to Direct or Global instead of Rule-Based, the rule list is not consulted at all.

## Rules and DNS

Domain-based rules only inspect the requested hostname, so they never require a DNS lookup. IP-based rules (`IP-CIDR`, `IP-CIDR6`, `GEOIP`, `IP-ASN`) match against the resolved IP address:

- If the request already targets an IP literal, IP-based rules match it directly, and `GEOIP`/`IP-ASN` look it up without a DNS query.
- If the request targets a domain, evaluation pauses at the first IP-based rule, Surge performs the DNS lookup, and evaluation resumes at the same rule. The result is cached, so at most one lookup is performed per request.
- With the `no-resolve` parameter, an IP-based rule is simply skipped for requests whose address has not been resolved, instead of triggering a lookup.

If the DNS lookup fails, rule evaluation aborts and the request fails with a DNS error — unless the FINAL rule carries the [dns-failed](final.md) parameter, in which case the FINAL policy is used instead.

{% hint style='tip' %}
Place domain-based rules before IP-based rules. Requests decided by a domain rule skip DNS resolution entirely, which reduces latency and avoids failures for domains that cannot be resolved locally.
{% endhint %}

## Pre-matching

Normally a rule decision happens only after Surge receives the first packet of a connection. Rules tagged with `pre-matching` and using a REJECT-family policy are additionally evaluated at the DNS-query and TCP-handshake stages, so unwanted requests are rejected with minimal overhead:

```
DOMAIN,ad.example.com,REJECT,pre-matching
```

Pre-matched rules have the highest priority. Only certain rule types support the tag, and the policy must be one of the REJECT family. See [REJECT Policy](../policies/reject.md) for the full behavior details and the list of supported types.

## Rule Parameters

The following optional parameters can be appended to rule lines. Each rule page documents the parameters relevant to its types in detail.

| Parameter | Form | Applies to | Effect |
| --- | --- | --- | --- |
| `no-resolve` | flag | IP-CIDR, IP-CIDR6, GEOIP, IP-ASN, RULE-SET, DOMAIN-SET | Skip the rule for unresolved domain requests instead of triggering a DNS lookup. On RULE-SET, applies to every sub-rule. |
| `dns-failed` | flag | FINAL only | Use the FINAL policy when a DNS lookup fails during rule evaluation. |
| `extended-matching` | flag | DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-WILDCARD, URL-REGEX, RULE-SET, DOMAIN-SET | Also match the TLS SNI and the HTTP Host header (or `:authority`). On RULE-SET/DOMAIN-SET, applies to every entry. |
| `pre-matching` | flag | Domain types, IP types, SRC-IP, DEST-PORT, SRC-PORT, SUBNET, CELLULAR-CARRIER, CELLULAR-RADIO, logical rules, RULE-SET, DOMAIN-SET | Evaluate the rule in the pre-matching phase. Top-level rules only; the policy must be a REJECT-family policy. See [REJECT Policy](../policies/reject.md). |
| `notification-text=<text>` | key=value | Any rule, including FINAL | Post a user notification with the given text when the rule matches. |
| `notification-interval=<seconds>` | key=value | Any rule, including FINAL | Minimum interval between notifications for the same rule. Default: 300 seconds. |
| `update-interval=<seconds>` | key=value | RULE-SET, DOMAIN-SET | Re-download interval for the external resource. Default: 86400 (24 hours). A negative value disables auto-updating. |
| `requires-resolve` | flag | SCRIPT only | Perform a DNS lookup before running the rule script, so the script can access the resolved addresses. |
| `always-capture=<session-name>` | key=value | Any rule, including FINAL | Force-enable HTTP capture for connections matched by the rule, recorded under the named capture session. Intended for debugging. |

Unknown parameters are silently ignored.

### notification-text and notification-interval

Use these parameters to get notified when a specific rule fires:

```
DOMAIN-SUFFIX,example.com,Proxy,notification-text=Example matched,notification-interval=600
```

Notifications for the same rule are throttled to one per `notification-interval` seconds (default 300).

## Rule Type Index

| Type | Matches | Page |
| --- | --- | --- |
| `DOMAIN` | Exact hostname | [Domain Rules](domain.md) |
| `DOMAIN-SUFFIX` | Hostname and its subdomains | [Domain Rules](domain.md) |
| `DOMAIN-KEYWORD` | Hostname containing a substring | [Domain Rules](domain.md) |
| `DOMAIN-WILDCARD` | Hostname against a wildcard pattern | [Domain Rules](domain.md) |
| `DOMAIN-SET` | Hostname against an external domain list | [Domain Rules](domain.md) |
| `IP-CIDR` | IPv4 address range | [IP Rules](ip.md) |
| `IP-CIDR6` | IPv6 address range | [IP Rules](ip.md) |
| `GEOIP` | Country of the destination IP | [IP Rules](ip.md) |
| `IP-ASN` | Autonomous system number of the destination IP | [IP Rules](ip.md) |
| `USER-AGENT` | HTTP User-Agent header | [HTTP Rules](http.md) |
| `URL-REGEX` | Request URL against a regex | [HTTP Rules](http.md) |
| `PROCESS-NAME` | Originating process (Mac only) | [Process Rules](process.md) |
| `DEST-PORT` | Destination port | [Source and Port Rules](source-and-port.md) |
| `SRC-PORT` | Client source port | [Source and Port Rules](source-and-port.md) |
| `IN-PORT` | Surge listen port the request arrived on | [Source and Port Rules](source-and-port.md) |
| `SRC-IP` | Client IP address | [Source and Port Rules](source-and-port.md) |
| `DEVICE-NAME` | Client device name | [Source and Port Rules](source-and-port.md) |
| `MAC-ADDRESS` | Client MAC address | [Source and Port Rules](source-and-port.md) |
| `PROTOCOL` | Connection protocol | [Protocol and Network Rules](protocol-and-network.md) |
| `HOSTNAME-TYPE` | Form of the hostname (domain/IP literal) | [Protocol and Network Rules](protocol-and-network.md) |
| `SUBNET` | Current network (SSID, BSSID, router, type) | [Protocol and Network Rules](protocol-and-network.md) |
| `CELLULAR-RADIO` | Current cellular radio technology (iOS only) | [Protocol and Network Rules](protocol-and-network.md) |
| `CELLULAR-CARRIER` | Current cellular carrier (iOS only) | [Protocol and Network Rules](protocol-and-network.md) |
| `AND` | All sub-rules match | [Logical Rules](logical.md) |
| `OR` | Any sub-rule matches | [Logical Rules](logical.md) |
| `NOT` | Sub-rule does not match | [Logical Rules](logical.md) |
| `SCRIPT` | Result of a JavaScript rule script | [Script Rules](script.md) |
| `RULE-SET` | A bundle of rules from a file, URL, or inline section | [Rule Sets](ruleset.md) |
| `FINAL` | Everything (default policy) | [Final Rule](final.md) |
