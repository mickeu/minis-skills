> For the complete documentation index, see [llms.txt](https://kb.nssurge.com/surge-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://kb.nssurge.com/surge-knowledge-base/guidelines/proxy-provider.md).

# Using Proxies from a Third-Party Provider

If you subscribe to a third-party proxy service and want to use its proxies with Surge, this guide explains the available options.

## Configuration Modes

### A. Managed Profile

Most providers offer a complete Surge managed profile for an out-of-the-box setup. This is the easiest way to get started: the provider presets and maintains all general settings and traffic routing rules. However, this also means that you cannot edit those settings or rules locally.

### B. Linked Profile

A Linked Profile creates an editable local profile based on a managed profile. Selected sections in the local profile continue tracking changes from the managed profile, providing a balance between automatic profile updates and local customization.

For most users, we recommend tracking the `[Proxy]` and `[Proxy Group]` sections from the managed profile while managing the other sections, such as general settings and rules, locally.

### C. External Policy Group

This is the recommended option for advanced Surge users. It gives you complete control over the profile and enables highly flexible customization through external resources, but requires a deeper understanding of Surge features.

Example:

`Proxy-Provider = select, policy-path=https://airport.com/surge.conf`

The URL specified by `policy-path` can point either to a plain list of proxy policies, with one proxy policy declaration per line, or to a complete Surge profile. When given a complete profile, Surge automatically imports the contents of its `[Proxy]` section.

## Common Use Cases

Surge provides extensive flexibility for complex requirements. Refer to the official manual for details about individual parameters. The following examples cover several recommended configurations and common scenarios.

<details>

<summary><mark style="color:purple;">Use Case #1:</mark> Group proxies by region</summary>

If your provider offers proxies in multiple regions and you want to select a specific region either manually or automatically, first create an external policy group that imports all proxies from the provider:

```
Airport-All = select, policy-path=https://airport.com/surge.conf, hidden=true
```

Set `hidden=true` because this group serves only as a resource pool and will not be used directly in the UI.

Next, create child policy groups and use regular-expression filters to select proxies from specific regions:

```
Airport-US = smart, include-other-group=Airport-All, policy-regex-filter=US
Airport-UK = smart, include-other-group=Airport-All, policy-regex-filter=UK
```

Because the specific proxy used within a region is usually unimportant, we recommend using the `smart` group type. Surge will automatically test the proxies and select the best one. If a proxy fails, Surge can switch seamlessly as long as another proxy in the group remains available.

You can then use `Airport-US` or `Airport-UK` directly in the `[Rule]` section to select a region.

{% hint style="success" %}
If you want to switch regions at any time, create an additional manual selection group:

```
Booster = select, Airport-US, Airport-UK
```

{% endhint %}

</details>

<details>

<summary><mark style="color:purple;">Use Case #2:</mark> Combine resources from multiple providers</summary>

Suppose you subscribe to both Awesome and Fantastic and want to organize their proxies by region as in Use Case #1. You can combine their resources as follows:

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-name-prefix=Awesome-
Airport-Fantastic = select, policy-path=https://fantastic.com/surge.conf, hidden=true, external-policy-name-prefix=Fantastic-

Airport-US = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=US
Airport-UK = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=UK
```

The `external-policy-name-prefix` parameter adds a prefix to the names of the policies imported into the group. Providers commonly name proxies using only a region and number, such as `US-01`. Adding a prefix, such as `Awesome-US-01`, makes it easy to identify the provider currently in use in the request list and logs.

{% hint style="warning" %}
When specifying multiple policy groups with `include-other-group`, enclose the parameter value in quotation marks (`""`).
{% endhint %}

</details>

<details>

<summary><mark style="color:purple;">Use Case #3:</mark> Relay proxy (proxy chain)</summary>

If you need to connect to a provider's proxies through a relay proxy, there are two ways to set it up.

**Option A: the `external-policy-modifier` parameter (all versions)**

Use the `external-policy-modifier` parameter to dynamically add an `underlying-proxy` parameter to the imported policies:

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-modifier="underlying-proxy=Airport-Fantastic"
```

This creates the following proxy chain: Client -> Airport-Fantastic (relay) -> Airport-Awesome (egress) -> destination server.

**Option B: the group-level `underlying-proxy` parameter (Surge Mac 6.9.0+ / iOS 5.22.0+)**

Newer Surge versions support declaring the relay directly on the policy group:

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, underlying-proxy=Airport-Fantastic
```

The resulting proxy chain is the same, but the two options differ in coverage and presentation. Consider a group that mixes a manually declared proxy with imported ones:

```
[Proxy]
NodeA = snell, a.example.com, 443, psk=pwd, version=5

[Proxy Group]
Mixed = select, NodeA, policy-path=https://awesome.com/surge.conf, external-policy-modifier="underlying-proxy=Airport-Fantastic"
```

* With **Option A**, only the policies imported via `policy-path` are chained — `NodeA` still connects directly, because `external-policy-modifier` never touches manually listed members (or members from `include-all-proxies` / `include-other-group`). The modified policies keep their original names, so a chained `US-01` looks identical to the unchained one in the UI and traffic statistics.
* With **Option B** (`underlying-proxy=Airport-Fantastic` in place of the modifier), every member of the group is chained, including `NodeA`. Chained members appear as derived policies named like `US-01 (via Airport-Fantastic)` with independent latency test results, so automatic group types select the best node based on the actual performance through the relay. The parameter can also be configured in the policy group editor UI.

We recommend Option B when your Surge version supports it; keep Option A if the profile must remain compatible with older versions.

{% hint style="info" %}
With either option, you can define a `select` group containing the `DIRECT` policy in advance and use that group as the `underlying-proxy`. This lets you enable or disable relay mode from the dashboard at any time.
{% endhint %}

{% hint style="info" %}
`external-policy-modifier` remains the right tool for other adjustments to imported policies, such as enabling TCP Fast Open.
{% endhint %}

</details>
