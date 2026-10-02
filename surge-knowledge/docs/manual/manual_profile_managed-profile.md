# Managed Profile

Surge can automatically update a profile from a URL. A managed profile starts with:

```
#!MANAGED-CONFIG http://test.com/surge.conf interval=60 strict=true
```

The profile can only be updated while the main Surge app is running.

{% hint style='tip' %}

Ensure the new remote profile also includes the `#!MANAGED-CONFIG` line. Without it, the profile reverts to a standard profile.

{% endhint %}

## Parameters

#### interval

Optional, in seconds, default: 86400

Set the update interval for the profile. This is the shortest time before an update may be triggered; Surge does not necessarily update immediately after the interval passes.

#### strict

Optional, Boolean, default: false

If `strict` is true, Surge requires a successful update after the interval arrives. Otherwise, if the update fails, the user may continue using the outdated profile.

> Note: Even when `strict` is true, the user can still start Surge from a widget or the VPN switch in Settings.

## REQUIREMENT Statement

The `!REQUIREMENT` statement can be used at the beginning or end of a profile line to limit the line's effect to specific environments:

```
#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB
Group = url-test, policyA, policyB //!REQUIREMENT CORE_VERSION<22
```

Since requirement expressions are lost when a profile is modified in the UI, this feature is mainly used in managed and enterprise profiles. It lets one managed profile serve clients on different platforms and Surge versions.

See [Line Requirement](requirement.md) for the expression syntax, available variables and operators, Core Version values, and the simplified notations (`#!IOS-ONLY`, `#!MACOS-ONLY`, `#!TVOS-ONLY`).

## FORBIDDEN-AUTO-UPGRADE Statement

Starting with Surge iOS 5.11.0 and Mac 5.7.0, Surge can automatically optimize profiles during upgrades so managed profiles can use newer features when possible.

If you do not want the profile to apply certain automatic optimizations, use the `FORBIDDEN-AUTO-UPGRADE` expression.

Example:

```
#!FORBIDDEN-AUTO-UPGRADE smart-group
```

Currently available optimization keywords include

- `smart-group`: automatically upgrades `url-test/load-balance` groups to [`smart`](../policy-groups/smart.md) groups.
