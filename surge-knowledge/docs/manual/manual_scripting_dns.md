# dns Script

A dns script implements a custom DNS resolver in JavaScript. A [Local DNS Mapping](../dns/local-dns-mapping.md) entry in the [Host] section refers to the script by name; the script resolves the domain, either by returning addresses directly or by delegating to specific upstream DNS servers.

```
[Script]
dnspod = type=dns,script-path=dnspod.js

[Host]
example.com = script:dnspod
*.example.com = script:dnspod
```

Wildcard patterns are allowed on the domain, as with other [Host] entries. Profile verification fails if a [Host] entry references a script name that does not exist.

## Trigger

The script runs when Surge needs to resolve a domain that matches the [Host] entry.

{% hint style='info' %}
DNS scripts run in the hot path of connection handling. Keep them small and fast. The JSC engine is recommended for dns scripts; see [Script Engine](overview.md).
{% endhint %}

## Input

| Field | Type | Description |
| --- | --- | --- |
| `$domain` | String | The domain name to resolve. |

## Result

The script must finish by calling `$done()` with an object containing **one** of the following:

* `address<String>`: Use this IP address as the result. It must be a valid IPv4/IPv6 address in string form.
* `addresses<Array>`: Use multiple IP addresses as the result.
* `server<String>`: Ask Surge to look up the domain via a specified upstream DNS server. It must be a valid IPv4/IPv6 address in string form.
* `servers<Array>`: Ask Surge to look up the domain via multiple specified upstream DNS servers.

When returning `address` or `addresses`, an additional `ttl<Number>` may also be returned to add the result to the DNS cache and avoid repeated lookups. The unit is seconds.

Calling `$done({})` makes Surge fall back to standard DNS resolution for the domain.

## Example

Use the public HTTP DNS API of DNSPod as a resolver:

```
$httpClient.get('http://119.29.29.29/d?dn=' + $domain, function(error, response, data){
  if (error) {
    $done({}); // Fallback to standard DNS query
  } else {
    $done({addresses: data.split(';'), ttl: 600});
  }
});
```
