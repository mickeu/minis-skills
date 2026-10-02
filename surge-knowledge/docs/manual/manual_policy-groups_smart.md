# Smart Group {{ book.VER | replace("%TEXT%", "iOS 5.11.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.7.0+") }}

A Smart Group dynamically selects a policy using the observed quality of real connections, and can retry another policy when the selected one is unavailable or performs poorly. Use it when you want hands-off selection that adapts to actual traffic rather than periodic latency tests alone.

```
[Proxy Group]
Smart = smart, ProxyA, ProxyB
```

Only proxy policies can be members of a Smart Group: nested policy groups and built-in policies (such as `DIRECT`) are silently ignored.

## How Selection Works

Each member policy gets a continuously updated delay score:

- The base of the score is a time-weighted moving average of the first-response latency of real connections — the time from connecting until the first response byte arrives. URL test results also feed into the same score.
- A packet-loss penalty is added based on the observed TCP retransmission ratio (roughly 50 ms per 1% of loss).
- The optional `policy-priority` factor is applied as a multiplier.

When a request comes in, policies whose score is close to the best one form the preferred set; one of them is used. The remaining healthy policies and then the failed ones form an ordered retry list, so if the chosen policy fails, the connection can fall back to the next candidate.

Failure handling: a connection that dies before receiving any data sharply worsens the policy's score, and a policy whose average delay grows too large is marked as failed until later tests or traffic recover it.

Starting with Surge iOS 5.21.0 and Surge Mac 6.8.0, Smart Groups also use UDP response latency and silent relay failures when scoring policies. A connection that receives no response data within 3 seconds is treated as failed so another policy can be tried sooner. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

### Per-site Memory

The group remembers, per site, which policies recently succeeded or failed. A policy known to work well for a site is preferred for that site unless it has become much slower than the best candidate; a policy that recently failed for the site is demoted. This memory expires after about one hour.

### Testing

A Smart Group retests its members on a fixed 5-minute schedule; the `interval` parameter has no effect on Smart Groups. When the group has many members (more than 12), regular rounds test only a subset — the most-used policies plus the least-recently-tested ones — while a manually triggered test always tests every member.

The `evaluate-before-use` parameter is supported and works the same way as for an [automatic testing group](url-test.md).

The policy displayed as the group's current selection is the most-used one in the recent period, not necessarily the one every new connection will use.

## Temporary Override

You can temporarily pin the group to a specific member. See [Temporary Override](parameters.md#temporary-override).

## Parameters

#### `policy-priority`

Optional, quoted list of `regex:factor` pairs separated by `;`, default: 1.0 for all policies

Applies a multiplier to the score of policies whose names match an expression; the first matching expression wins. Values below `1` increase preference and values above `1` reduce preference:

```
Smart = smart, ProxyA, ProxyB, policy-priority="Premium:0.9;Backup:1.3"
```

Priority values must be positive. Zero and negative values are rejected starting with Surge iOS 5.21.0 and Surge Mac 6.8.0. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}
