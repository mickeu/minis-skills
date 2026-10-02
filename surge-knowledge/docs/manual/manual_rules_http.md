# HTTP Rules

HTTP rules match properties of an HTTP request: the User-Agent header and the request URL. They only take effect for requests processed by Surge's HTTP engine; plain TCP or UDP connections are never matched by these rules.

```
[Rule]
USER-AGENT,Instagram*,Proxy
URL-REGEX,^http://example\.com/api/,DIRECT
```

## When HTTP Rules Apply

A request is visible to HTTP rules only when the HTTP engine handles it and the relevant property is available:

- Plain HTTP requests handled by the HTTP engine expose both the URL and the User-Agent header. This includes requests sent to Surge's HTTP proxy port and TCP connections forced into HTTP processing with `force-http-engine-hosts`.
- HTTPS requests expose their full URL and headers only when [MITM decryption](../http/mitm.md) is enabled for the hostname.
- For HTTPS requests that are not decrypted, no URL is available, so `URL-REGEX` cannot match. `USER-AGENT` can only match if the client happens to send a User-Agent header in the proxy CONNECT request.

See [HTTP Processing Overview](../http/overview.md) for how traffic reaches the HTTP engine.

## Rule Types

#### USER-AGENT

```
USER-AGENT,Instagram*,DIRECT
```

Matches if the User-Agent header of the request matches the value. Wildcard characters `*` and `?` are supported. Matching is case-sensitive.

#### URL-REGEX

```
URL-REGEX,^http://google\.com,DIRECT
```

Matches if the complete request URL matches the regular expression. The rule matches when the pattern is found anywhere in the URL; anchor with `^` when you want a prefix match. The regular expression is case-sensitive.

For plain HTTP requests the tested string is the full URL, e.g. `http://example.com/path?query`. For HTTPS requests with MITM enabled, it is the decrypted URL, e.g. `https://example.com/path?query`.

If the value contains commas, wrap it in double quotes:

```
URL-REGEX,"^http://example\.com/(a|b),?c",Proxy
```

##### extended-matching

You can append the `extended-matching` parameter to also test URL variants in which the host part is replaced by the TLS SNI and by the HTTP Host header (or `:authority`), which helps when the request targets an IP address or the Host differs from the URL host:

```
URL-REGEX,^https://example\.com,Proxy,extended-matching
```
