# Policy Including

A policy group can build its member list from sources other than the literal names on its line: an external file or URL (`policy-path`), all proxies in the profile (`include-all-proxies`), or the members of another group (`include-other-group`).

## Include External Policies

A policy group may import policies defined in an external file or from a URL.

```
egroup = select, policy-path=proxies.txt
```

The resource may be either of:

- A **policy list**: one policy line per line, in the same format as the `[Proxy]` section. Blank lines and lines starting with `#` or `//` are ignored. Invalid lines are logged and skipped; policies whose names duplicate an existing policy are skipped with a warning.
- A **complete Surge profile**: if the content contains a `[Proxy]` section, the policies in that section are used.

```
Proxy-A = https, example1.com, 443
Proxy-B = https, example2.com, 443
```

Remote resources are cached on disk and re-downloaded periodically.

#### `update-interval`

Optional, in seconds, default: 86400

The update interval for a remote `policy-path`. Only meaningful when the path is a URL.

#### `policy-regex-filter`

Optional, regex

Only use the policies whose name matches the regex. It applies to members from `policy-path`, `include-all-proxies`, and `include-other-group`, but not to explicitly listed members. The value must be a valid regular expression.

#### `external-policy-modifier`

Optional, quoted `key=value` list

Modify the parameters of every imported external policy. The listed parameters override those in the imported policy lines.

For example, enabling TFO and changing the testing URL:

```
external-policy-modifier="test-url=http://apple.com/,tfo=true"
```

{% hint style='tip' %}
This parameter only affects members imported via `policy-path`. To set up a proxy chain for the whole group regardless of where its members come from, use the group-level [`underlying-proxy` parameter](parameters.md#underlying-proxy) instead of `external-policy-modifier="underlying-proxy=..."`.
{% endhint %}

#### `external-policy-name-prefix`

Optional

Add a prefix to the policy names of the sub-policies in this external policy group to facilitate differentiation when multiple different external policy groups are used simultaneously. The prefix must not contain the `=` character.

Imported policies are processed in this order: `policy-regex-filter` → `external-policy-name-prefix` → `external-policy-modifier`.

## Include Existing Policies {{ book.VER | replace("%TEXT%", "iOS 4.12.0+") }} {{ book.VER | replace("%TEXT%", "Mac 4.5.0+") }}

You can use `include-all-proxies` and `include-other-group` to include all proxies or reuse existing definitions from another group.

#### `include-all-proxies`

Optional, Boolean, default: false

The parameter `include-all-proxies=true` includes all proxy policies defined in the `[Proxy]` section (built-in policies and groups are not included). It can be used with the `policy-regex-filter` parameter for filtering.

#### `include-other-group`

Optional, comma-separated list of group names (quotable)

Parameter `include-other-group="group1,group2"` includes the resolved member policies from other policy groups; multiple groups can be listed separated by commas. Inclusion is recursive, and it can be used with the `policy-regex-filter` parameter for filtering.

## Ordering

Members are assembled in this order: explicitly listed members (in declared order), then `include-other-group` members (in the listed group order), then `include-all-proxies` members, then `policy-path` externals. Duplicate names keep the first occurrence.

{% hint style='tip' %}
* `include-all-proxies`, `include-other-group`, and `policy-path` parameters are allowed to be used in a single policy group at the same time. The `policy-regex-filter` parameter applies to all three.
* When precise member ordering matters (e.g., fallback groups), prefer nesting policy groups with `include-other-group` instead of relying on the assembly order of mixed sources.
{% endhint %}
