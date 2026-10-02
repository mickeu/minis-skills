# URL Rewrite

Surge can rewrite a request's URL transparently, return a redirect response, or reject the request entirely, based on regular expression matching against the URL.

Example:

```
[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
^http://yachen\.com https://yach.me 302
^http://ad\.com/ad\.png _ reject
```

Each rule consists of three parts: a regular expression, a replacement, and a type. If the type is omitted, `header` is used.

The regular expression is matched against the full request URL. The replacement supports capture group references such as `$1`.

{% hint style='info' %}
URL Rewrite only applies to requests handled by the HTTP engine. HTTPS requests can only be rewritten if [MITM](mitm.md) is enabled for the hostname. See [HTTP Processing](overview.md) for details.
{% endhint %}

### Header Mode

Surge modifies the request in place and redirects it to another host if necessary. The client does not notice the rewrite.

The `Host` field in the request header is modified to match the new URL.

```
[URL Rewrite]
^http://www\.google\.cn http://www.google.com header
```

If multiple header-mode rules match a request, only the first one is applied. The rewritten URL must be a valid `http`, `https`, or `ws` URL, otherwise the rewrite is discarded.

### 302 Mode

Surge returns a 302 redirect response to the client, with the replacement as the `Location`.

```
[URL Rewrite]
^http://yachen\.com https://yach.me 302
```

### 307 Mode

Same as 302 mode, but returns a 307 redirect response. Unlike 302, a 307 redirect requires the client to keep the original request method and body when following the redirect.

```
[URL Rewrite]
^http://yachen\.com https://yach.me 307
```

In 302 and 307 modes, the replacement may contain the placeholder {% raw %}`{{{GATEWAY_ADDRESS}}}`{% endraw %}, which is substituted with the default router address of the current outgoing network interface.

### Reject Mode

Reject the request if the pattern is matched. The replacement parameter is ignored; use `_` as a placeholder.

```
[URL Rewrite]
^http://ad\.com/ad\.png _ reject
```

### Matching details

Besides the request-line URL, Surge also tries matching with the URL rebuilt from the `Host` header value and from the underlying connection's hostname. A rule can therefore match even when these differ from the host in the request line.
