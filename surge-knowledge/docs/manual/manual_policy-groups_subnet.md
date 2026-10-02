# Subnet Group

A `subnet` group automatically selects a policy based on the current network environment, such as the connected Wi-Fi network or the network type.

```
Subnet Group = subnet, default = ProxyHTTP, SSID:MyHome = ProxySOCKS5, TYPE:WIFI = ProxyHTTP
```

{% hint style='info' %}
Starting from Surge iOS 4.12.0 and Surge Mac 4.5.0, the SSID group was renamed to Subnet Group.
The legacy SSID Group syntax is still supported. You may use the group type keyword `subnet` or `ssid` for compatibility.
{% endhint %}

## Conditions

Each entry of the form `<subnet expression> = Policy` maps a network condition to a policy. The [SUBNET rule](../rules/protocol-and-network.md) page is the canonical reference for subnet expressions. In summary:

- `SSID:value` — match the Wi-Fi SSID; wildcard characters are allowed.
- `BSSID:value` — match the Wi-Fi BSSID; wildcard characters are allowed.
- `ROUTER:value` — match the router (default gateway) IP address.
- `TYPE:WIFI` / `TYPE:WIRED` / `TYPE:CELLULAR` — match the network type.
- `MCCMNC:value` — match the cellular carrier MCC+MNC code; only matches when Wi-Fi is not connected.
- A bare value without a prefix matches SSID/BSSID/router IP, for legacy compatibility.

Conditions are evaluated in the declared order and the first match wins; if no condition matches, the `default` policy is used. The result is re-evaluated whenever the network changes.

Subnet groups do not support the other common group parameters (`policy-path`, `include-*`, `policy-regex-filter`, `no-alert`, ...); only `hidden`, `icon-url` and `category` are available besides the entries below.

You can also temporarily override the group with a manually selected policy, just like other automatic groups — see [Common Group Parameters](parameters.md).

## Parameters

#### `default`

Required

The policy used when no subnet expression matches.

#### `cellular`

Optional (Deprecated, use a `TYPE:CELLULAR` condition instead)

The policy for cellular networks. If set, it takes precedence over the condition entries when the device is on a cellular network. If it is not provided, the condition list and then the default policy apply.
