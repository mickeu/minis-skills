# Scripting

You may use JavaScript to extend the abilities of Surge. Scripting requires Surge iOS 4 or Surge Mac 3.3.0. Scripts are declared in the `[Script]` section of the profile and are triggered by HTTP traffic, rule matching, DNS resolution, system events, cron timers, or manual invocation.

```
[Script]
script1 = type=http-response,pattern=^http://www.example.com/test,script-path=test.js,requires-body=true
script2 = type=cron,cronexp="* * * * *",script-path=fired.js
script3 = type=dns,script-path=dns.js
```

There are seven script types:

* [http-request](http-request.md) — modify or short-circuit an HTTP request
* [http-response](http-response.md) — modify an HTTP response
* [rule](rule.md) — implement a custom rule with the `SCRIPT` rule type
* [dns](dns.md) — implement a custom DNS resolver via a `[Host]` entry
* [event](event.md) — react to system events such as network changes
* [cron](cron.md) — run on a schedule
* [generic](generic.md) — run only when invoked manually, from Shortcuts, or from a panel

## Declaration

Each line takes the form `name = comma-separated key=value parameters`:

```
name = type=http-response,pattern=^http://example.com,script-path=test.js,requires-body=true
```

The `script-path` parameter is mandatory; a line without it is rejected.

A legacy form is still parsed for compatibility:

```
<type> <value> <parameters>
```

For example, `http-response ^http://example.com script-path=x.js,requires-body=true`. The `<value>` maps to `pattern` (http-request/http-response), `cronexp` (cron), `event-name` (event), or the script name (rule/dns/generic). If no name is given, the script name defaults to the last path component of `script-path`. Use the modern form for new profiles.

### Parameters

#### `type`: Optional, default: generic

One of the seven script types listed above. An unknown type string rejects the line. Always declare the type explicitly.

#### `script-path`: Required

The path of the script: a relative path (resolved against the profile directory), an absolute path, or an HTTP(S) URL. Remote scripts are downloaded and cached automatically.

#### `script-update-interval`: Optional, in seconds, default: 86400

The auto-update interval when `script-path` is a URL.

#### `timeout`: Optional, in seconds, default: 5

The longest-running time for the script. If the script does not call `$done()` before the timeout, the session is terminated with a timeout warning. With the JSC engine, the timeout also terminates runaway synchronous JavaScript; the WebView engine enforces the timeout with a wall-clock timer only.

#### `argument`: Optional

An arbitrary string exposed to the script as the `$argument` global.

#### `engine`: Optional, auto/jsc/webview, default: auto

Selects the script engine. See the Script Engine section below.

#### `debug`: Optional, Boolean, default: false

Enables debug mode, which has two effects:

1. The script is reloaded from the filesystem before every run instead of using the cache (local script paths only).
2. For `http-request` and `http-response` scripts, `console.log()` output also appears in the request's notes in the traffic viewer.

#### `pattern`: Required for http-request and http-response, regex

The regex pattern to match the request URL. Only the first enabled matching script in profile order runs for a request; at most one `http-request` and one `http-response` script run per request.

#### `requires-body`: Optional, Boolean, default: false

Buffers the entire request/response body and passes it to the script, allowing the script to replace the body. This behavior is expensive; only enable it when necessary.

#### `max-size`: Optional, in bytes, default: 1 MB (iOS) / 10 MB (Mac)

The maximum allowed size for the request/response body when `requires-body` is enabled. If a response body exceeds the limit, Surge falls back to passthrough mode and skips the script for that request. If a request body exceeds the limit, the connection is terminated. A value of `-1` removes the limit (up to a hard cap).

#### `binary-body-mode`: Optional, Boolean, default: false

The raw binary body data is passed to the script as a `Uint8Array` instead of a string, and the script may return a `Uint8Array` body. The setting is exposed to the script as `$script.binaryBodyMode`.

#### `full-header-mode`: Optional, Boolean, default: false

Headers are delivered to the script as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields such as `Set-Cookie`. The script's returned `headers` may be either a plain object or an array of `{field, value}` objects.

#### `cronexp`: Required for cron

The cron expression, in standard 5-field form or 6-field form with a leading seconds field. Quote the value since it contains spaces, e.g. `cronexp="0 8 * * *"`. A cron script firing more than 10 times per hour triggers a battery-consumption warning.

#### `event-name`: Required for event

The name of the event to hook. Available events: `network-changed`, `notification`, `engine-started` and `profile-reloaded`. An event script without `event-name` never runs.

#### `wake-system`: Optional, Boolean, default: false {{ book.VER | replace("%TEXT%", "iOS Only") }}

For cron scripts on iOS: schedules a silent local notification at the next fire time so the system wakes Surge to run the script.

## Script Engine {{ book.VER | replace("%TEXT%", "iOS 5.9.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}

Surge contains two JavaScript engines.

### JavaScriptCore (`engine=jsc`)

- Advantages:
  1. The engine initializes quickly, and the overhead when calling is low (low latency).
- Disadvantages:
  1. Since JSC runs inside the NE process on iOS, it increases the memory usage of the Surge NE process significantly, possibly leading to system termination due to exceeding memory limits.

At most 2 JSC sessions run in parallel; additional sessions are queued.

### WebView (`engine=webview`)

- Advantages:
  1. The WebView runs in a separate independent process, so script execution has almost no impact on the memory usage of the NE process and will not cause the Surge NE process to be terminated due to memory usage issues.
  2. The WebView JavaScript environment can use JIT, which greatly improves execution efficiency for complex or CPU-intensive scripts.
  3. WebAPI (fetch, crypto, TextDecoder, etc.) can be used.
- Disadvantages:
  1. The engine's initialization time overhead is slightly higher.
  2. Transferring a large amount of data between the script and Surge crosses process boundaries, which is less efficient. This is most apparent when using `binary-body-mode` to process large bodies.

At most 3 WebView sessions run in parallel; additional sessions are queued.

### Usage Recommendations

1. For small, frequently called, simple scripts, such as rule and dns type scripts, JSC is recommended.
2. For complex, high-memory scripts (such as parsing an MB-level HTTP body as JSON), WebView is recommended.
3. If a script uses WebAPI, explicitly configure `engine=webview` so that users are prompted when the script runs in an environment without WebView support.

### Configuration

Add the `engine` parameter to the script line: `auto`, `jsc`, or `webview`. The default is `auto`, which always uses WebView where available.

### Engine Availability

- iOS: JSC and WebView
- macOS
  - macOS 10.15 and below: only JSC
  - macOS 11.0 and above: JSC and WebView
- tvOS: only JSC

## Performance Constraints

Scripting with `requires-body` requires Surge to load the entire body into memory. A huge response body may cause Surge iOS to crash since the iOS system limits the maximum amount of memory the Network Extension can occupy. Write `pattern` regexes as narrowly as possible and only enable body access for necessary URLs.

Sessions beyond the parallel engine limits are queued; a session that cannot start within the timeout window completes as a timeout.

## Debugging

- Enable the `debug` parameter to reload the script from disk on every run and mirror `console.log()` output into the request notes for HTTP scripts.
- `console.log()` output is written to a per-script log file. You can view the logs on the device, or remotely with [Logbook](../tools/logbook.md).
- The built-in script editor in both apps can evaluate a script immediately with mock input; the script receives `$trigger = "editor"`.
- On Surge iOS, you can manually trigger a script by long-pressing on it, or with the system Shortcuts app. A Shortcuts invocation may pass a parameter, available to the script as `$intent.parameter`.
- The [HTTP API](../tools/http-api.md) provides endpoints to evaluate scripts: `POST /v1/scripting/evaluate` evaluates arbitrary script text with mock input, and `POST /v1/scripting/cron/evaluate` runs a configured cron script by name.
