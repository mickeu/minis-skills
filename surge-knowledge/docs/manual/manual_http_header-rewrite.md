# Header Rewrite

Surge can rewrite the headers of HTTP requests before they are forwarded to the server, and the headers of HTTP responses before they are returned to the client.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-add DNT 1
http-request ^http://example.com header-del Cookie
http-request ^http://example.com header-replace User-Agent Unknown
http-response ^http://example.com header-replace-regex Date 2022 2023
```

Each rule consists of several parts:

1. HTTP direction: `http-request` or `http-response`. Old versions only supported modifying the request, so this part can be omitted, which means `http-request`:

    ```
    [Header Rewrite]
    ^http://example.com header-add DNT 1
    ```

2. URL regular expression
3. Action type
4. Header field
5. Value (not used by `header-del`)
6. Replace template (only for `header-replace-regex`)

{% hint style='info' %}
Header Rewrite only applies to requests handled by the HTTP engine. HTTPS requests can only be modified if [MITM](mitm.md) is enabled for the hostname. See [HTTP Processing](overview.md) for details.
{% endhint %}

### header-add

Append a new header line to the header, even if the header field already exists.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-add DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
```

### header-del

Delete a header line from the header.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-del DNT

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
```

### header-replace

Replace a header value in the header. If the header field doesn't exist, nothing happens.

Example:

```
[Header Rewrite]
http-request ^http://example.com header-replace DNT 1

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 1
```

If you would like to add a header line, or replace it whenever the field exists, use `header-del` and `header-add` together:

```
[Header Rewrite]
^http://example.com header-del DNT
^http://example.com header-add DNT 1
```

### header-replace-regex

Replace a header value with a regular expression and a template. If the header field doesn't exist, nothing happens.

```
[Header Rewrite]
http-request ^http://example.com header-replace-regex User-Agent Safari Chrome

Before:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0

After:
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Chrome/603.1.30
Accept-Language: en-us
Accept-Encoding: gzip, deflate
DNT: 0
```

### Limitations

Header Rewrite cannot change the message framing. If a rewrite changes the `Content-Length` or `Transfer-Encoding` headers, the modification is rejected and the request fails.
