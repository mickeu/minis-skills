# Fallback Group

A `fallback` group selects an available policy by priority. Availability is checked with the same URL test as an [automatic testing group](url-test.md), but a fallback group only cares whether a policy is available, not its exact latency. Policies listed earlier have higher priority.

```
FallbackGroup = fallback, ProxySOCKS5, ProxySOCKS5TLS
```

Surge walks the members in declared order and picks the first one whose latest test succeeded (and whose latency is below `timeout`, if set). If no member qualifies, the first member is used regardless, so traffic is never left without a policy.

When the selected policy changes, Surge posts a notification unless `no-alert` is set.

## Temporary Override

You can temporarily override the result of automatic testing by manually selecting a policy. See [Temporary Override](parameters.md#temporary-override).

## Parameters

#### `interval`

Optional, in seconds, default: 600

How long an availability result stays valid. When the group is used and the result is older than this interval, Surge retests in the background. A network change also invalidates the result.

#### `timeout`

Optional, in seconds, no default

Treat a member as unavailable if its tested latency is not below this value. This is separate from the per-test connection timeout (`test-timeout`, default 5 seconds) — see [Common Group Parameters](parameters.md).

#### `evaluate-before-use`

Optional, Boolean, default: false

If enabled, when the group is used for the first time, Surge waits for the first test round to finish instead of using the first member while testing in the background.
