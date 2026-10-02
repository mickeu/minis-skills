# Quick Start

Surge is controlled by a profile: a plain-text file that describes how traffic is captured, how requests are matched, and which outbound policy is used. This page builds a minimal working profile.

Most setups only need four sections:

```
[General]
dns-server = system, 1.1.1.1, 8.8.8.8

[Proxy]
ProxyA = https, proxy.example.com, 443, username, password

[Proxy Group]
Proxy = select, ProxyA, DIRECT

[Rule]
DOMAIN-SUFFIX,example.com,Proxy
GEOIP,CN,DIRECT
FINAL,Proxy
```

## How to Read This Profile

- `[General]` contains global options such as DNS servers, testing URLs, and takeover behavior. This example uses the system DNS servers plus 1.1.1.1 and 8.8.8.8, queried concurrently.
- `[Proxy]` defines outbound policies. `ProxyA` forwards traffic to an HTTPS proxy server; a policy can also connect directly or use any other [supported protocol](../policies/overview.md).
- `[Proxy Group]` lets you choose among multiple policies. The `select` group named `Proxy` is switched manually in the app UI between `ProxyA` and the built-in `DIRECT` policy.
- `[Rule]` matches requests from top to bottom; the first matched rule decides the policy. Here, `example.com` and its subdomains go through the `Proxy` group, destinations with a Chinese GeoIP result connect directly, and everything else falls to the `FINAL` rule.

Load the profile, start Surge, and check the request list in the UI or [Dashboard](../tools/dashboard.md) to confirm traffic is being captured and matched as expected.

## Where to Go Next

- To understand the profile file format, read [Profile Format](../profile/format.md).
- To write matching logic, read [Rules Overview](../rules/overview.md).
- To configure proxy servers, read [Policies Overview](../policies/overview.md).
- To choose among proxies automatically, read [Policy Groups](../policy-groups/overview.md).
- To customize DNS behavior, read [DNS Server](../dns/dns-server.md) and [Local DNS Mapping](../dns/local-dns-mapping.md).
- To modify HTTP requests and responses, read [HTTP Processing](../http/overview.md) and [Scripting](../scripting/overview.md).
