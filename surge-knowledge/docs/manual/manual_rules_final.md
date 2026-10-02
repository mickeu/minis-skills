# Final Rule

The FINAL rule defines the default policy for requests not matched by any other rule. Write it after all other rules; the [Rule] section must end with a FINAL rule.

```
[Rule]
DOMAIN-SUFFIX,company.com,ProxyA
DOMAIN-KEYWORD,google,DIRECT
GEOIP,US,DIRECT
IP-CIDR,192.168.0.0/16,DIRECT
FINAL,ProxyB
```

A FINAL rule always matches, so any rules written below it never take effect. If several enabled FINAL rules are present, the last one is the effective one. FINAL is not allowed inside [rule set](ruleset.md) files or as a sub-rule of a [logical rule](logical.md).

## Options

#### dns-failed

If a DNS lookup fails while evaluating an IP-based rule, the request normally fails with an error. With the `dns-failed` option, Surge uses the FINAL rule's policy instead:

```
FINAL,ProxyB,dns-failed
```

This option only makes sense with a non-DIRECT policy — a direct connection to a hostname that cannot be resolved would fail anyway, while a proxy can perform the DNS resolution remotely.

Like other rules, FINAL also accepts the `notification-text` and `notification-interval` options; see [Rules Overview](overview.md).

## Relationship to Outbound Mode

The FINAL rule is the default only within Rule-Based Proxy outbound mode. In Direct or Global Proxy outbound mode, the rule system — including FINAL — is bypassed entirely: all traffic goes direct or to the selected global policy.
