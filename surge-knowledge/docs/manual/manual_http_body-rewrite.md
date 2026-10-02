# Body Rewrite {{ book.VER | replace("%TEXT%", "iOS 5.10.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.6.0+") }}

Surge can rewrite the body of an HTTP request or response, replacing the original content with regular expressions or manipulating a JSON body with jq expressions.

Example:

```
[Body Rewrite]
http-request ^http(s)?://example\.com value abc
http-response ^http(s)?://example\.com documents Surge
```

{% hint style='info' %}
Body Rewrite only applies to requests handled by the HTTP engine. HTTPS bodies can only be modified if [MITM](mitm.md) is enabled for the hostname. See [HTTP Processing](overview.md) for details.
{% endhint %}

### Syntax

Each line contains a rewrite rule, with parameters separated by spaces, starting with `http-request` or `http-response`. The second parameter is the regular expression for the URL to take effect. The third parameter is the regular expression for replacement, and the fourth parameter is the content of replacement.

`http-response ^https?://example\.com/ regex replacement`

You may continue adding regular expressions and replacement content afterwards for consecutive replacements:

```
http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2
http-response ^https?://example\.com/ regex1 replacement1 regex2 replacement2 regex3 replacement3
…
```

The replacement supports capture group references such as `$1`. The `^` and `$` anchors match at the beginning and end of each line of the body.

{% hint style='tip' %}
1. If a request hits multiple body rewrite rules, they are executed in sequence.
2. Even if the original request does not contain a body, new content may still be generated through body rewrite, such as using the `^$` expression.
{% endhint %}

The body must be valid UTF-8 text for regex-based rewriting. If it is not, the rule is skipped and a note is added to the request journal.

### JQ Body Rewrite {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

You can use jq expressions to manipulate a JSON body:

```
http-request-jq url-pattern jq-expression
http-response-jq url-pattern jq-expression
```

For example:

```
http-response-jq ^http://httpbingo.org/anything '.headers |= with_entries(select(.key | test("^X-") | not))'
```

Notes:

* The body must be valid JSON; otherwise, the rule is skipped and a note is added to the request journal.
* If the jq expression produces empty output, the original body is kept.
* An invalid jq expression produces a warning and the rule is skipped.

### Interaction with scripts

If both a body rewrite rule and an HTTP script match the same request or response, the body rewrite is applied first, and the script receives the rewritten body.

### Limitations

* Body rewrite requires buffering the full body. A request body may be buffered up to 32 MB; if it exceeds the limit, the connection is dropped.
* A response body may be modified only up to 1 MB on iOS and 10 MB on macOS. If the response exceeds the limit, Surge gives up the modification and streams the response through unmodified.
* Request body rewrite is not supported when the request uses `Transfer-Encoding: chunked` or `Expect: 100-continue`. Surge logs a warning and forwards the request unmodified.
* When the body is modified, Surge normalizes the related headers automatically: the body is decompressed first if necessary, and `Content-Length` is recalculated.
