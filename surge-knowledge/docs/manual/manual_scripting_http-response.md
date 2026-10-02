# http-response Script

An http-response script inspects and modifies an HTTP response before Surge delivers it to the client. Use it to rewrite response status, headers, or body in ways that the static rewrite features cannot express.

```
[Script]
modify-resp = type=http-response,pattern=^https?://www\.example\.com/test,script-path=test.js,requires-body=true,max-size=16384
```

Like other HTTP processing features, the script only sees requests that go through Surge's HTTP engine. HTTPS requests require [MITM](../http/mitm.md) to be enabled for the host. See [HTTP Processing Overview](../http/overview.md).

## Trigger

The script runs when the response arrives for a request whose URL matches the `pattern` regex. At most one script runs per response: the first enabled http-response script in the profile whose pattern matches wins.

## Parameters

These parameters apply to http-response (and http-request) script lines, in addition to the [common script parameters](overview.md). See the [http-request page](http-request.md) for the full descriptions.

#### pattern

Required, regular expression

The regex matched against the request URL.

#### requires-body

Optional, true/false, default false

Buffers the entire response body (decompressed) and passes it to the script, allowing the script to replace it. Without `requires-body`, the script runs as soon as the response header arrives and must not return a `body` in its result.

#### max-size

Optional, bytes, default 1 MB on iOS, 10 MB on macOS

The maximum body size buffered for the script. If the response body exceeds this limit, Surge falls back to passthrough mode: the script is skipped for this request and a note is attached to the request record. Use `-1` for no limit.

#### binary-body-mode

Optional, true/false, default false

Passes the body as a `Uint8Array` instead of a UTF-8 decoded string, and accepts a `Uint8Array` back.

#### full-header-mode

Optional, true/false, default false

Delivers headers as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields such as `Set-Cookie`.

{% hint style='info' %}
Scripting with `requires-body` requires Surge to load the entire response body into memory. On iOS, the system limits the memory a Network Extension may use, so a huge response body can cause problems. Keep patterns narrow and only enable body access for the URLs that need it.
{% endhint %}

## Input

The script receives both the request and the response:

| Field | Type | Description |
| --- | --- | --- |
| `$request.url` | String | Request URL. |
| `$request.method` | String | Request HTTP method. |
| `$request.headers` | Object | Request HTTP headers. |
| `$request.id` | String | A unique ID for the request, stable between the http-request script and the paired http-response script. |
| `$response.status` | Number | Response HTTP status code. |
| `$response.headers` | Object | Response HTTP headers. An array of `{field, value}` objects in full-header-mode. |
| `$response.body` | String or Uint8Array | Response HTTP body, decoded to a string with UTF-8 unless binary-body-mode is set. Only present when `requires-body=true` and the body is not empty. |

## Result

The script must finish by calling `$done()` with an object. The object may contain:

* `status<Number>`: Replace the status code.
* `headers<Object or Array>`: Replace all response headers.
* `body<String or Uint8Array>`: Replace the response body. Only works when `requires-body=true`. A script running without `requires-body` must not return a body; doing so aborts the connection.
* `abort<Boolean>`: If true, Surge aborts the connection instead of delivering the response.

Calling `$done({})` — or `$done()` with no argument — delivers the response untouched.

## Example

```
let headers = $response.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});
```
