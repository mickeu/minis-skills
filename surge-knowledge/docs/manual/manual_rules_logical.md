# Logical Rules

Logical rules combine multiple sub-rules with the operators AND, OR, and NOT for conditions that no single rule type can express, such as "this domain, but only from this client" or "everything except this network".

```
AND,((SRC-IP,192.168.1.110),(DOMAIN-SUFFIX,example.com)),DIRECT
```

## Syntax

```
AND,((Rule1),(Rule2),...),Policy
OR,((Rule1),(Rule2),...),Policy
NOT,((Rule1)),Policy
```

Each sub-rule is written in parentheses, without a policy of its own — the same form used inside [rule set files](ruleset.md). Sub-rule values containing commas may be quoted.

- `AND` matches if all sub-rules match.
- `OR` matches if any sub-rule matches. Evaluation short-circuits in both cases.
- `NOT` inverts the result of its sub-rule. It takes exactly one sub-rule.

## Nesting

A logical rule may contain other logical rules, up to a maximum nesting depth of 10.

```
AND,((NOT,((SRC-IP,192.168.1.110))),(DOMAIN-SUFFIX,example.com)),DIRECT
```

Any rule type that is valid inside a rule set can be used as a sub-rule, including `RULE-SET` and `SCRIPT`. `FINAL` cannot be a sub-rule.

## Examples

Route a domain through a proxy only when on cellular:

```
AND,((DOMAIN-SUFFIX,example.com),(SUBNET,TYPE:CELLULAR)),Proxy
```

Reject QUIC traffic to a set of domains:

```
AND,((PROTOCOL,UDP),(RULE-SET,https://example.com/streaming.list)),REJECT
```

Send everything except LAN destinations from a specific client through a proxy:

```
AND,((SRC-IP,192.168.1.120),(NOT,((RULE-SET,LAN)))),Proxy
```

## Flags on logical rules

- Sub-rules may carry their own `no-resolve` and `extended-matching` flags, with the same meaning as on top-level rules.
- The `pre-matching` flag cannot be placed on a sub-rule, but the whole logical rule may be flagged `pre-matching` if every sub-rule type supports pre-matching and the policy is a REJECT-family policy. See the [flags table in the rules overview](overview.md).

```
AND,((DOMAIN-SUFFIX,tracker.example.com),(DEST-PORT,443)),REJECT,pre-matching
```
