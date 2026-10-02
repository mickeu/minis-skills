# Policy Groups

A policy group contains multiple policies and exposes them as a single policy name. Rules can then reference the group instead of a concrete policy, so you can change how traffic is routed without touching the rules. A group may contain built-in policies, proxy policies, or other policy groups.

Policy groups are declared in the `[Proxy Group]` section:

```
[Proxy Group]
Proxy = select, ProxyA, ProxyB, DIRECT
Auto = url-test, ProxyA, ProxyB
Smart = smart, ProxyA, ProxyB
```

Each line follows the pattern `Name = type, member1, member2, ..., key=value, ...`. Components containing `=` are parameters; all other components are member policy names.

## Group Types

| Type | Behavior |
|---|---|
| [`select`](select.md) | Manually choose a policy in the UI. |
| [`url-test`](url-test.md) | Automatically choose the policy with the best latency test result. |
| [`fallback`](fallback.md) | Choose the first available policy by declared priority. |
| [`load-balance`](load-balance.md) | Distribute requests among available policies. |
| [`smart`](smart.md) | Dynamically select a policy using observed connection quality and site history. |
| [`subnet`](subnet.md) | Choose a policy according to the current network. |

The legacy keyword `ssid` is still accepted as an alias of `subnet` for compatibility.

## Nesting Groups

A group may include other groups as members. This works for all group types except `smart`, which silently ignores nested groups and built-in policies among its members.

When a nested group is tested, it contributes its own effective result: a nested `select` group is tested through its currently selected policy, while other nested groups are tested through their whole member set.

Group references must not form a loop. If a loop is detected (for example, `A` includes `B` and `B` includes `A`), Surge logs a warning and the affected group temporarily behaves as a reject policy (shown as `FAILED` in logs). If a group ends up with no usable member at all, Surge falls back to `DIRECT` (shown as `SUBSTITUTE` in logs) and raises a one-time warning.

## How Testing Works

The automatic group types (`url-test`, `fallback`, `load-balance`, `smart`) rely on latency tests: Surge sends an HTTP HEAD request to a testing URL through each member policy and records the result. Testing is lazy — Surge retests when a group is used and the previous result has expired or the network has changed.

The testing URL and timeout are resolved per policy: an explicit `test-url` policy parameter wins; otherwise the global `proxy-test-url` (for proxies) or `internet-test-url` (for direct-type policies) from `[General]` is used. See [Common Group Parameters](parameters.md) for details, and [Policy Parameters](../policies/parameters.md) for the per-policy testing options.
