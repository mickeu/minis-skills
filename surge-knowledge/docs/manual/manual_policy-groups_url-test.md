# Automatic Testing Group

A `url-test` group automatically selects the member policy with the best latency test result. Use it when you have several similar proxy servers and always want the fastest one.

```
AutoTestGroup = url-test, ProxySOCKS5, ProxySOCKS5TLS
```

## How Testing Works

Surge tests each member by sending an HTTP HEAD request to the testing URL through that policy. The testing URL comes from the policy's own `test-url` parameter if set, otherwise from the global `proxy-test-url` / `internet-test-url` options in `[General]`. See [Common Group Parameters](parameters.md) for the full resolution rules.

The measurement runs in two rounds: the first HEAD request establishes the connection (DNS, TCP, and proxy handshake), and if the server supports HTTP keep-alive, a second HEAD request is sent on the reused connection. The duration of the second request is the reported score, so the score approximates the pure request round-trip time and excludes handshake overhead. If the testing URL does not support connection reuse, the score is the full first-round time, and Surge logs a one-time warning that the result is inaccurate.

Test results are not refreshed on a fixed schedule. A retest is triggered when the group is used and the previous result is older than `interval`, or the network has changed since the last test. You can also trigger a full test round manually from the UI.

The group selects the member with the lowest score among those that passed the test. When the winner changes, Surge posts a "Group has a new optimal option" notification unless `no-alert` is set.

{% hint style='info' %}
The legacy `url =` parameter on a group line has no effect in current versions. Use the per-policy `test-url` parameter or the global `proxy-test-url` option instead.
{% endhint %}

## Temporary Override

You can temporarily override the result of automatic testing by manually selecting a policy. See [Temporary Override](parameters.md#temporary-override).

## Parameters

#### `interval`

Optional, in seconds, default: 600

How long a test result stays valid. When the group is used and the result is older than this interval, Surge retests in the background. A network change also invalidates the result.

#### `tolerance`

Optional, in milliseconds, default: 100

Switch damping. The selected policy changes only when it failed the test, or when the new best policy is faster than the currently selected one by more than the tolerance. This prevents policies with similar latency from constantly alternating.

An explicit `tolerance=0` is honored and switches to the fastest policy on every result change.

#### `timeout`

Optional, in seconds, no default

Availability filter based on the test score: a member qualifies as a candidate only if its tested latency is below this value. If omitted, no filtering by score is applied.

This is not the connection timeout of the test itself. The per-test timeout is controlled by the per-policy `test-timeout` parameter or the global `test-timeout` option (default 5 seconds) — see [Common Group Parameters](parameters.md).

#### `evaluate-before-use`

Optional, Boolean, default: false

By default, when an automatic testing group is used for the first time, Surge uses the first policy in the group and starts testing in the background.

If this option is enabled, Surge waits for the first test round to finish before handling the request. If the evaluation fails, the request fails with an error.
