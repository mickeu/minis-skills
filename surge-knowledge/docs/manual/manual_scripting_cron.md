# cron Script

A cron script runs on a schedule described by a cron expression. Use it for periodic tasks such as switching a policy group by time of day or refreshing data with `$httpClient`.

```
[Script]
nightly = type=cron,cronexp="0 2 * * *",script-path=cron.js
```

## Parameters

#### cronexp

Required, cron expression string

The schedule, as a string of five or six space-separated fields. Quote the value with `"` since it contains spaces.

* A five-field expression is the standard form (minute, hour, day of month, month, day of week); the schedule has minute resolution.
* A six-field expression prepends a seconds field for second-level resolution.

Examples:

* At 2 AM daily: `0 2 * * *`
* At 5 AM and 5 PM daily: `0 5,17 * * *`
* Every minute: `* * * * *`
* Every second: `* * * * * *`
* Every Sunday at 5 PM: `0 17 * * sun`
* Every 10 minutes: `*/10 * * * *`

#### wake-system {{ book.VER | replace("%TEXT%", "iOS Only") }}

Optional, true/false, default false

Schedules a silent local notification at the next fire time so that the system wakes Surge to run the script even when the device is idle. Without it, a fire time may be missed while the app is suspended by the system.

## Input

| Field | Type | Description |
| --- | --- | --- |
| `$cronexp` | String | The cron expression that scheduled this run. |

When the script is triggered manually instead of by the timer, `$trigger` indicates the source (for example `intent` when run from the Shortcuts app, with the optional Shortcuts parameter in `$intent.parameter`).

## Result

The script must call `$done()` to complete. The result object is ignored; a bare `$done()` is enough. If `$done()` is never called, the run ends with a timeout warning after the script `timeout` (default 5 seconds) — set a larger `timeout` parameter if the task legitimately needs more time.

## Manual Triggering

Besides the timer, a cron script can be run on demand:

* Surge iOS: long-press the script, or use the Shortcuts app.
* Surge Mac: run the script from the UI.
* [HTTP API](../tools/http-api.md): `POST /v1/scripting/cron/evaluate` with body `{"script_name": "..."}`.

## Constraints

* A cron script that fires more than 10 times per hour triggers a battery consumption warning. Avoid very frequent schedules on iOS.

## Example

Switch a select group's policy at 2 AM daily, using the [`$surge` API](api.md):

```
// nightly = type=cron,cronexp="0 2 * * *",script-path=cron.js
$surge.setSelectGroupPolicy('Group', 'Proxy');
$done();
```
