# rule Script

A rule script implements a custom rule condition in JavaScript. A [SCRIPT rule](../rules/script.md) in the [Rule] section refers to the script by name; the script inspects the request and reports whether it matches.

```
[Script]
ssid-rule = type=rule,script-path=ssid-rule.js

[Rule]
SCRIPT,ssid-rule,DIRECT
```

Profile verification fails if a SCRIPT rule references a script name that does not exist.

## Trigger

The script runs when rule evaluation reaches the SCRIPT rule line. The result is cached for the rest of the evaluation of the same request, so referencing the same script from multiple rules does not run it repeatedly.

If the script is missing or scripting is disabled, the rule is treated as not matched.

{% hint style='info' %}
Rule scripts run in the hot path of connection handling. Keep them small and fast, and avoid asynchronous operations where possible. The JSC engine is recommended for rule scripts; see [Script Engine](overview.md).
{% endhint %}

## Input

The request details are provided as the `$request` global. Fields that are unavailable for a particular request are `null`.

| Field | Type | Description |
| --- | --- | --- |
| `$request.hostname` | String | Target hostname (a domain or an IP address). |
| `$request.destPort` | Number | Target port. |
| `$request.sourcePort` | Number | Source port of the client connection. {{ book.VER | replace("%TEXT%", "iOS 5.8.4+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.4+") }} |
| `$request.protocol` | String | Protocol of the request: `HTTP`, `HTTPS`, `TCP`, `UDP`, `QUIC`, or `STUN`. {{ book.VER | replace("%TEXT%", "iOS 5.8.4+") }} {{ book.VER | replace("%TEXT%", "Mac 5.4.4+") }} |
| `$request.processPath` | String | Path of the process that initiated the request (Surge Mac). |
| `$request.userAgent` | String | User-Agent of the request, if available. |
| `$request.url` | String | Request URL, if the request is an HTTP request handled by the HTTP engine. |
| `$request.sourceIP` | String | Source IP address of the client. |
| `$request.listenPort` | Number | The Surge listen port that accepted the request. |
| `$request.dnsResult` | Object | DNS resolution result: `{v4Addresses: [String], v6Addresses: [String]}`. Only populated with the `requires-resolve` option. |

## DNS Resolution

By default, a SCRIPT rule does not trigger a DNS lookup, behaving like other rules with the `no-resolve` flag: for a domain-based request, `$request.dnsResult` is empty. Use the `requires-resolve` option on the rule line to make Surge resolve the hostname first:

```
SCRIPT,ssid-rule,DIRECT,requires-resolve
```

The result then appears in `$request.dnsResult`.

## Result

The script must finish by calling `$done()` with an object containing a `matched` boolean:

```
$done({matched: true});   // the rule matches; use its policy
$done({matched: false});  // continue with the next rule
```

## Example

Match a hostname only when connected to a specific Wi-Fi network:

```
var hostnameMatched = ($request.hostname === 'home.com');
var ssidMatched = ($network.wifi.ssid === 'My Home');

$done({matched: (hostnameMatched && ssidMatched)});
```
