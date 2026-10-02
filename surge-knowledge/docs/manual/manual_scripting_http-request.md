# http-request Script

An http-request script inspects and modifies an HTTP request before Surge performs rule matching and sends it upstream. Use it when [URL Rewrite](../http/url-rewrite.md) or [Header Rewrite](../http/header-rewrite.md) cannot express the change you need, or when you want to answer a request with a mock response without any network operation.

```
[Script]
modify-req = type=http-request,pattern=^https?://httpbin\.org,script-path=http-request.js,requires-body=true,max-size=16384
```

Like other HTTP processing features, the script only sees requests that go through Surge's HTTP engine. HTTPS requests require [MITM](../http/mitm.md) to be enabled for the host. See [HTTP Processing Overview](../http/overview.md).

## Trigger

The script runs when the full request URL matches the `pattern` regex. The URL is also tested with the host component replaced by the `Host` header value and by the SNI hostname, so a pattern written against the logical hostname still matches.

At most one script runs per request: the first enabled http-request script in the profile whose pattern matches wins.

## Parameters

These parameters apply to http-request (and http-response) script lines, in addition to the [common script parameters](overview.md).

#### pattern

Required, regular expression

The regex matched against the request URL. The line is invalid if the regex does not compile.

#### requires-body

Optional, true/false, default false

Buffers the entire request body and passes it to the script, allowing the script to replace it. This is expensive — the whole body is held in memory — so only enable it when necessary.

#### max-size

Optional, bytes, default 1 MB on iOS, 10 MB on macOS

The maximum body size buffered for the script. If a request body exceeds this limit, the connection is rejected with an error. Use `-1` for no limit (a hard cap of 32 MB for request bodies still applies).

#### binary-body-mode

Optional, true/false, default false

Passes the body to the script as a `Uint8Array` instead of a UTF-8 decoded string, and accepts a `Uint8Array` back. Use it for non-text bodies. The current mode is exposed to the script as `$script.binaryBodyMode`.

#### full-header-mode

Optional, true/false, default false

Delivers `$request.headers` as an array of `{field, value}` objects instead of a plain object, preserving duplicate fields and their order. The `headers` value returned to `$done()` may then also be either form.

## Input

The script receives the request as the `$request` global:

| Field | Type | Description |
| --- | --- | --- |
| `$request.url` | String | Request URL. |
| `$request.method` | String | Request HTTP method. |
| `$request.headers` | Object | Request HTTP headers. An array of `{field, value}` objects in full-header-mode. |
| `$request.body` | String or Uint8Array | Request body. Only present when `requires-body=true` and the body is not empty. `Uint8Array` in binary-body-mode. |
| `$request.id` | String | A unique ID for the request, stable between the http-request script and the paired http-response script. |

## Result

The script must finish by calling `$done()` with an object. The object may contain:

* `url<String>`: Replace the request URL. Unlike URL Rewrite, this does not update the `Host` header field; return a modified `headers` object as well if necessary.
* `headers<Object or Array>`: Replace all request headers. Do not produce headers inconsistent with the actual body framing (such as a wrong `Content-Length`); Surge rejects the request if the resulting framing is ambiguous.
* `body<String or Uint8Array>`: Replace the request body. Only works when `requires-body=true`.
* `response<Object>`: If this object exists, Surge returns an HTTP response directly without any network operation. The object may contain:
    * `status<Number>`: Response HTTP status code. (Optional. Default: 200)
    * `headers<Object or Array>`: Response HTTP headers. (Optional)
    * `body<String or Uint8Array>`: Response HTTP body. (Optional)
* `abort<Boolean>`: If true, Surge aborts the request and closes the connection.

Calling `$done({})` — or `$done()` with no argument — continues the request untouched. To abort a request, use `$done({abort: true})`; a bare `$done()` does not abort it.

```
// Reject requests from a specific client
if ($request.headers['User-Agent'] === 'BadBot') {
    $done({abort: true});
} else {
    $done({});
}
```

## Limitations

* The request body may not be overwritten when the request uses chunked transfer encoding.
* The request body may not be overwritten when an `Expect: 100-continue` header exists.

In both cases the script may still run for header modification, but body changes are not applied.

## Example

```
let headers = $request.headers;
headers['X-Modified-By'] = 'Surge';

$done({headers});
```

A mock response without a network request:

```
$done({
    response: {
        status: 200,
        headers: {'Content-Type': 'application/json'},
        body: '{"result": "ok"}'
    }
});
```
