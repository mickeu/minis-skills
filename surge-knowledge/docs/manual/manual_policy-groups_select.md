# Manual Selection Group

A `select` group lets you choose which policy is used from the user interface. It is the most common group type: rules point to the group, and you switch the actual policy manually.

```
SelectGroup = select, ProxyHTTP, ProxyHTTPS, DIRECT, REJECT
```

The selection is persisted per profile. If no selection has been made yet, or the previously selected policy is no longer a member of the group, the first member is used.

{% hint style='info' %}
In Surge iOS, you may use the widget to quickly switch the policy for manual selection groups. <br />In Surge Mac, you may switch the policy in the menu bar.
{% endhint %}

A `select` group is often combined with external policy lists — see [Policy Including](policy-including.md) for `policy-path`, `include-all-proxies`, and `include-other-group`.

For parameters shared by all group types (`hidden`, `icon-url`, ...), see [Common Group Parameters](parameters.md).
