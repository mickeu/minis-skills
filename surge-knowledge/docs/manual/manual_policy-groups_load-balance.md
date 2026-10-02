# Load Balance Group

A `load-balance` group distributes requests among its available members. Use it to spread traffic over several servers instead of always using a single one.

```
Balance = load-balance, ProxyA, ProxyB, ProxyC
```

## Behavior

Availability is determined by the same URL test as an [automatic testing group](url-test.md): the available set contains the members whose latest test succeeded (and whose latency is below `timeout`, if set). The set is rebuilt after every test round.

- Without `persistent`, each request picks a uniformly random policy from the available set.
- If no member is currently available, all members are used as candidates.
- The testing parameters `interval`, `timeout`, and `evaluate-before-use` work the same way as for an automatic testing group.
- A load-balance group never posts policy change notifications.
- When nested inside another group, the group's own test score is the mean score of its available members.

## Temporary Override

You can temporarily pin the group to a single member, which skips balancing. See [Temporary Override](parameters.md#temporary-override).

## Parameters

#### `persistent`

Optional, Boolean, default: false

When `persistent=true`, the same policy is used for the same target hostname: the policy is chosen by hashing the target hostname over the available members. This helps avoid triggering risk controls on the target site due to changing egress IPs. The selection may still change when the available set changes.
