# event Script

An event script runs when a specific Surge event occurs. Use it to react to environment changes — for example, adjusting a policy group when the network changes.

```
[Script]
on-network-changed = type=event,event-name=network-changed,script-path=network-changed.js
```

## Parameters

#### event-name

Required, event name string

The name of the event to hook. If the parameter is missing, the script is never triggered. Four events are available:

* `network-changed`: Triggered when the system network changes. No event data.
* `notification`: Triggered whenever Surge posts a notification. The script receives the message even if the notification's category is turned off in the settings.
* `engine-started`: Triggered once after the Surge engine finishes starting, when the Network Extension and the active profile are fully initialized, so `$network` is ready to read. No event data. {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}
* `profile-reloaded`: Triggered after the active profile is reloaded at runtime. The initial profile load at engine startup does not count as a reload; hook `engine-started` for that. No event data. {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

## Input

| Field | Type | Description |
| --- | --- | --- |
| `$event.name` | String | The event name. |
| `$event.data` | Object | Event data; contents depend on the event type. |

For the `notification` event, `$event.data` contains the notification's `title`, `subtitle`, `body`, and `identifier` fields (absent fields are omitted). If the notification was posted by a script via `$notification.post`, the options object passed to it is echoed back as the `script-options` field.

## Result

The script must call `$done()` to complete. The result object is ignored; a bare `$done()` is enough.

## Constraints

* A script hooked to the `notification` event may not call `$notification.post` itself. This restriction prevents infinite notification loops; violating it aborts the script with an exception.
* Event scripts can also be triggered manually (for example via the Shortcuts app on iOS); in that case `$event.name` is `manually`.

## Examples

Post a notification with the current DNS servers when the network changes:

```
// on-network-changed = type=event,event-name=network-changed,script-path=network-changed.js

$notification.post('DNS Update', $network.dns.join(', '));

$done();
```

Log the network state once the engine is up:

```
// on-start = type=event,event-name=engine-started,script-path=start.js

console.log(JSON.stringify($network));

$done();
```

Log every notification Surge posts:

```
// log-notifications = type=event,event-name=notification,script-path=notification.js

console.log($event.data);

$done();
```
