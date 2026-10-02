# JavaScript API

This page documents the JavaScript API available to Surge scripts. The input globals and result shapes specific to each script type are documented on the corresponding type pages ([http-request](http-request.md), [http-response](http-response.md), [rule](rule.md), [dns](dns.md), [event](event.md), [cron](cron.md), [generic](generic.md)).

## Globals

The following globals are injected into every script, regardless of type.

#### `$environment`

An object describing the runtime environment:

- `$environment.system<String>`: The OS name, such as iOS or macOS.
- `$environment["surge-build"]<String>`: The build number of Surge.
- `$environment["surge-version"]<String>`: The short version number of Surge.
- `$environment.language<String>`: The current UI language of Surge.
- `$environment["device-model"]<String>`: The current device model. {{ book.VER | replace("%TEXT%", "iOS 5.9.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}

Keys containing hyphens require bracket access.

#### `$script`

Information about the script being evaluated:

- `$script.name<String>`: The script name.
- `$script.type<String>`: The script type.
- `$script.startTime<Number>`: The time when the current run started, as UNIX epoch seconds.
- `$script.sessionID<String>`: A short random ID identifying this run; it prefixes the script's log lines.
- `$script.binaryBodyMode<Boolean>`: Whether the `binary-body-mode` parameter is enabled.

#### `$network`

An object describing the current network environment: `wifi` (`ssid`, `bssid`), `v4` (`primaryAddress`, `primaryInterface`, `primaryRouter`), `v6` (`primaryAddress`, `primaryInterface`), `dns` (an array of the current DNS servers), and on iOS `cellular-data` (`carrier`, `radio`).

#### `$argument`

The string given by the `argument` parameter in the script declaration. Only present if the parameter is configured.

#### `$trigger`

Present only for some launch paths, describing how the script was started: `"editor"` (script editor), `"http-api"` (`POST /v1/scripting/evaluate`), `"intent"` (Shortcuts), `"button"` (panel tap), or `"auto-interval"` (periodic panel refresh). Not set for normal HTTP, rule, dns, event, or cron-timer triggers.

#### `$intent`

Present when the script is triggered from the system Shortcuts app. `$intent.parameter` contains the parameter passed by the shortcut.

#### `$input`

Present when the script is invoked by a panel: `{purpose: "panel", position, panelName}`. See the [Information Panel](../tools/panel.md) page for the panel result contract.

Type-specific input globals — `$request`, `$response`, `$domain`, `$event`, `$cronexp` — are documented on the type pages.

## $done

Every script must call `$done()` exactly once to indicate completion, even scripts that do not produce a result. If `$done()` is never called, the session ends by timeout with a warning. Extra calls are ignored.

- `$done()` and `$done({})` are equivalent for `http-request` and `http-response` scripts: the request/response continues untouched.
- `$done({abort: true})` terminates the connection (`http-request` and `http-response` scripts).
- For other types, the accepted result shapes are documented on each type page. For `cron` and `event` scripts the result is ignored.

An uncaught exception aborts the session and the script has no effect.

## $httpClient

#### `$httpClient.get(options<String|Object>, callback<Function>)`

Performs an HTTP request. The same signature is available for all methods: `$httpClient.get`, `$httpClient.post`, `$httpClient.put`, `$httpClient.delete`, `$httpClient.head`, `$httpClient.options`, `$httpClient.patch`.

The first parameter can be a URL string or an options object:

```
{
  url: "http://www.example.com/",
  headers: {
    "Content-Type": "application/json"
  },
  body: "{}",
  timeout: 5
}
```

`url` is required and must be an HTTP(S) URL. If the `headers` field exists, it overwrites all existing header fields. `body` can be a string, an object (encoded to a JSON string, with `Content-Type` set to `application/json`), or a TypedArray.

Options:

- `timeout`: The request timeout in seconds. The default is 5 seconds.
- `policy`: Perform the request with an existing policy, given by name.
- `policy-descriptor`: Perform the request with a temporary policy, given by a full policy descriptor string. Takes precedence over `policy`.
- `insecure`: If true, HTTPS requests do not verify the server certificate. {{ book.VER | replace("%TEXT%", "iOS 5.9.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}
- `auto-redirect`: Controls whether 30x HTTP status codes are followed automatically, enabled by default. {{ book.VER | replace("%TEXT%", "iOS 5.9.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}
- `auto-cookie`: Controls whether Cookie-related fields are processed and stored automatically, enabled by default. If turned off, the Cookie header is passed as a normal field. {{ book.VER | replace("%TEXT%", "iOS 5.9.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}
- `binary-mode`: If true, the response data is delivered as a `Uint8Array` instead of a string. {{ book.VER | replace("%TEXT%", "iOS 5.4.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.0.1+") }}
- `full-header-mode`: If true, the response headers are delivered as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields.

Callback: `callback(error<String>, response<Object>, data<String|Uint8Array>)`. When successful, `error` is null and the response object contains `status` and `headers`.

Requests made by scripts appear in the traffic viewer. At most 20 concurrent requests are allowed per script run; request and response bodies are capped at 32 MB on iOS and 256 MB on Mac.

## $httpAPI

#### `$httpAPI(method<String>, path<String>, body<Object>, callback<Function>(result<Object>))`

Calls Surge's own [HTTP API](../tools/http-api.md) to control Surge's functions. No authentication parameters are required. For a GET request, the body object is converted to a query string. The callback receives the parsed JSON result.

## $persistentStore

Simple persistent key-value storage. If the key is omitted, scripts with the same `script-path` share the same storage entry; use an explicit key to share data among different scripts. Keys must be plain names without path separators.

#### `$persistentStore.write(data<String>, [key<String>])`

Saves data permanently. Only a string is allowed; returns true on success. Passing `null` as the data deletes the entry. The maximum value size is 4 MB on iOS and 32 MB on Mac.

#### `$persistentStore.read([key<String>])`

Returns the saved string, or null if the entry does not exist.

Tips: Surge Mac writes the $persistentStore data to the directory `~/Library/Application Support/com.nssurge.surge-mac/SGJSVMPersistentStore/`. You may edit the files here directly for debugging.

## $notification

#### `$notification.post(title<String>, subtitle<String>, body<String>[, options<Object>])`

Posts a system notification.

Available options: {{ book.VER | replace("%TEXT%", "iOS 5.11.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.7.0+") }}

- `action`: The operation performed after the user opens Surge by tapping the notification.
  - `open-url`: Opens a URL, provided by the `url` option.
  - `clipboard`: Copies content to the clipboard (confirmed by the user), provided by the `text` option.
- `url`: The URL for the `open-url` action. Providing `url` without `action` implies `open-url`.
- `text`: The string for the `clipboard` action.
- `media-url`: Attaches media content, such as an image, fetched from an HTTP(S) URL.
- `media-base64`: Same as above, but the content is provided directly as base64. Requires the MIME type via the `media-base64-mime` option.
- `auto-dismiss`: Boolean; automatically dismisses the notification after a period of time (usually 10 s).
- `sound`: Boolean; plays the default notification sound.

A script hooked to the `notification` event may not call `$notification.post`, to prevent notification loops.

## $utils

#### `$utils.geoip(ip<String>)`

Performs a GeoIP lookup. Returns the ISO 3166 country code.

#### `$utils.ipasn(ip<String>)`

Looks up the AS number of the IP address, or null if unknown. The WebView engine may return the number as a numeric string.

#### `$utils.ipaso(ip<String>)`

Looks up the AS organization name of the IP address.

#### `$utils.ungzip(binary<Uint8Array>)`

Decompresses gzip data. Returns a `Uint8Array`, or null on failure. The output size is capped at 16 MB on iOS and 128 MB on Mac.

## $surge

The `$surge` module controls Surge itself. All setters return a Boolean indicating success.

#### `$surge.setSelectGroupPolicy(groupName<String>, policyName<String>)`

Changes the selected policy of a select policy group. The policy must be one of the group's sub-policies.

#### `$surge.selectGroupDetails()`

Returns an object describing all select groups: `{groups: {groupName: [subPolicyNames]}, decisions: {groupName: selectedPolicy}}`.

#### `$surge.retestGroup(groupName<String>, callback<Function>(result<Object>))`

Forces a retest of an automatic testing group. The callback result contains `availablePolicyNames`.

#### `$surge.setOutboundMode(mode<String>)`

Sets the outbound mode: `"direct"`, `"global-proxy"`, or `"rule"`.

#### `$surge.setHTTPCaptureEnabled(enabled<Boolean>)`

Toggles HTTP capture.

#### `$surge.setRewriteEnabled(enabled<Boolean>)`

Toggles the rewrite feature.

#### `$surge.setEnhancedModeEnabled(enabled<Boolean>)` {{ book.VER | replace("%TEXT%", "Mac Only") }}

Toggles Enhanced Mode.

#### `$surge.setCellularModeEnabled(enabled<Boolean>)` {{ book.VER | replace("%TEXT%", "Mac Only") }}

Toggles cellular data mode.

#### `$surge.logbook(content<String>)`

Writes a line into Surge's [Logbook](../tools/logbook.md) (Recent Events) under the script's name.

## Miscellaneous

#### `console.log(message)`

Logs a message to the script's log file. Objects are JSON-stringified. In debug mode, the output of `http-request`/`http-response` scripts also appears in the request's notes. Log lines are truncated at 512 KB.

#### `setTimeout(function[, delay])`

Same as `setTimeout` in browsers, with limits: the maximum delay is 24 hours, and at most 64 timers may be pending at once. `clearTimeout` is available only under the WebView engine. All pending timers are cancelled when the script run completes.

Under the WebView engine, scripts additionally have access to the standard WebAPI (fetch, TextDecoder, crypto, etc.). If a script relies on WebAPI, declare `engine=webview` explicitly; see the Script Engine section in the [Scripting Overview](overview.md).
