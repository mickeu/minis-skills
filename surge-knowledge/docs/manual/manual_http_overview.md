# HTTP Processing

Surge can inspect and modify the HTTP traffic that flows through it: rewriting URLs, headers, and bodies, returning local mock responses, and running JavaScript against requests and responses. This chapter covers the built-in rewrite features; scripting has [its own chapter](../scripting/overview.md).

## Which traffic can be processed

All HTTP processing features require the traffic to be handled by Surge's HTTP engine, which parses the stream as HTTP messages:

* Plain HTTP traffic is handled automatically. When a new TCP connection arrives, Surge sniffs the first bytes; if they look like an HTTP request, the connection is passed to the HTTP engine.
* Cleartext HTTP on non-standard ports may not be detected by sniffing. Use the `force-http-engine-hosts` parameter in the `[General]` section to force connections to specific hosts and ports through the HTTP engine. It only affects cleartext traffic and never decrypts TLS. See [General section](../profile/general.md).
* To exclude hosts from HTTP processing entirely, use the `always-raw-tcp-hosts` parameter in the `[General]` section. Matching connections are forwarded as raw TCP streams without sniffing or parsing.
* HTTPS traffic is an opaque TLS tunnel by default. Surge can only process it after decrypting it with [MITM](mitm.md) for that hostname. Without MITM, none of the rewrite features apply to HTTPS requests.

Both `force-http-engine-hosts` and `always-raw-tcp-hosts` are of the [Host List parameter type](../profile/host-list.md).

## Processing pipeline

When a request passes through the HTTP engine, the modification features run in this order:

1. [Header Rewrite](header-rewrite.md)
2. [URL Rewrite](url-rewrite.md)
3. [Body Rewrite](body-rewrite.md)
4. [Script processing](../scripting/overview.md)

A request or response may be modified by only one script. The rewrite features have no such limit: if multiple rewrite rules match, they take effect in sequence.

[Map Local](map-local.md) is also evaluated in the request path: when a Map Local rule matches, Surge returns the local response directly and skips the upstream request.

## Inspecting the results

Requests handled by the HTTP engine appear as individual HTTP requests in the Dashboard's capture viewer, with full headers and bodies available. This is the easiest way to verify that your rewrite rules match and produce the expected result: the request detail view shows the notes for applied rewrites and scripts.
