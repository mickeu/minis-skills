# Common Group Parameters

These parameters are available on all group types, with one exception: subnet groups support only `hidden`, `icon-url` and `category` (see [Subnet Group](subnet.md)). The parameters for importing members (`policy-path`, `include-all-proxies`, `include-other-group`, and their companions) are documented on the [Policy Including](policy-including.md) page.

#### `no-alert`

Optional, Boolean, default: false

Do not show the policy change notification for this group. The "Group has a new optimal option" notification is only posted by `url-test` and `fallback` groups, so this parameter has no effect on other group types — `load-balance`, `smart`, and `select` groups never notify.

#### `hidden`

Optional, Boolean, default: false

Do not show the group in the menu (Surge Mac) and the policy selection view (Surge iOS).

#### `icon-url` {{ book.VER | replace("%TEXT%", "Mac 6.5.0+") }}

Optional

Configure an icon for a policy group for display in the policy selection interface. This parameter currently needs to be edited manually in the profile.

Example:

```
Group = select, ProxyA, ProxyB, icon-url=https://example.com/icon.png
```

#### `category` {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }}

Optional

Assign the group to a category for display purposes:

* Surge iOS: when at least one group declares a category, the policy group view shows a category switcher at the top and only lists the groups of the selected category. Groups without a category are collected under the trailing "…" tab, which only appears when such groups exist. The parameter can also be edited in the group editor.
* Surge Mac: groups sharing a category are folded into a submenu named after the category in the status bar menu. Groups without a category stay at the top level, followed by these submenus.

The parameter has no effect on routing.

Example:

```
[Proxy Group]
Streaming = select, ProxyA, ProxyB, category=Media
Gaming = url-test, ProxyA, ProxyB, category=Games
Fallback = select, ProxyA, DIRECT
```

#### `underlying-proxy` {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

Optional, the name of another proxy policy or policy group. Not available on subnet groups.

Set up a proxy chain for the whole group: every proxy member connects through the given policy, as if each of them carried the per-policy [`underlying-proxy` parameter](../policies/parameters.md#underlying-proxy). It applies to members from every source — explicitly listed members, `policy-path`, `include-all-proxies`, and `include-other-group` — and can also be configured in the group editor UI.

Example — always reach the subscription nodes through a relay:

```
[Proxy]
Relay = snell, relay.example.com, 443, psk=pwd, version=5

[Proxy Group]
Subscription = url-test, policy-path=https://example.com/nodes, underlying-proxy=Relay
```

Notes:

* Each affected member appears as a derived policy named `Name (via Relay)` with its own latency test results, so the measured latency reflects the real performance through the chain and the group selects the best member accordingly.
* Members that are themselves policy groups are not affected; a nested group may declare its own `underlying-proxy`. Built-in policies like DIRECT and REJECT also pass through unchanged.
* If a member policy already carries its own `underlying-proxy` parameter, the group-level value overrides it.

{% hint style='tip' %}
To chain only some members of a group, wrap them in a nested group. No copy of the policy declaration is needed:

```
[Proxy Group]
NodeB-Chained = select, NodeB, underlying-proxy=Relay
Group = select, NodeA, NodeB-Chained
```
{% endhint %}

**Comparison with `external-policy-modifier`**

Before this parameter existed, the closest workaround was [`external-policy-modifier`](policy-including.md#external-policy-modifier)`="underlying-proxy=Relay"`. The group-level parameter differs from it in several ways:

* **Coverage**: `external-policy-modifier` only rewrites policies imported via `policy-path`; explicitly listed members and members from `include-all-proxies` / `include-other-group` are left out of the chain. The group-level `underlying-proxy` covers members from all sources.
* **Configuration**: `external-policy-modifier` is a generic text-rewrite mechanism with no UI. The group-level parameter can be configured in the group editor, and misconfigurations — a group chaining through itself, or a chain target that doesn't exist — are reported explicitly.
* **Visibility**: policies modified by `external-policy-modifier` keep their original names, making the chained and unchained variants indistinguishable in the UI and in traffic statistics. Members chained by the group-level parameter are clearly labeled `Name (via Relay)` and tracked separately.

The old form keeps working for compatibility. If both are present, the group-level `underlying-proxy` takes precedence over an `underlying-proxy` set through `external-policy-modifier`. For other parameter overrides (`test-url`, `tfo`, etc.), `external-policy-modifier` remains the right tool.

## Testing URL and Timeout

The automatic group types test their members with an HTTP HEAD request. For each member policy, the testing URL is resolved as follows:

1. The policy's own `test-url` parameter, if set.
2. Otherwise, a global option from `[General]`: `internet-test-url` for direct-type policies, `proxy-test-url` for proxy policies. Both default to `http://bing.com/`.

The per-test timeout is resolved similarly: the policy's `test-timeout` parameter, then the global `test-timeout` option, then 5 seconds by default (10 seconds for direct-type policies).

These per-policy parameters are documented in [Policy Parameters](../policies/parameters.md). Do not confuse the per-test `test-timeout` with the `timeout` parameter of `url-test`/`fallback` groups, which filters candidates by their measured latency.

## Temporary Override

The automatic group types — `url-test`, `fallback`, `load-balance`, `subnet`, and `smart` — can be temporarily overridden by manually selecting a policy:

* In Surge Mac, you can find the override option in the corresponding group in the main menu.

* In Surge iOS, you can find the override option by long-pressing on the corresponding policy's menu in the policy group view.

While an override is active, the group always uses the selected policy and automatic testing for the group is no longer triggered by use. Overrides for groups that no longer exist are cleared when the profile reloads.
