# Map Local

You may mock an HTTP server and return a static response without sending the request upstream. This feature is also called Mock or API Mocking. If you want to return a response dynamically, try [scripting](../scripting/overview.md).

Example:

```
[Map Local]
^http://surgetest\.com/json data-type=text data="{}" status-code=500
^http://surgetest\.com/gif data-type=tiny-gif status-code=200
^http://surgetest\.com/file data-type=file data="data/map-local.json" header="a:b|foo:bar"
^http://surgetest\.com/base64 data="dGVzdA==" data-type=base64
```

When a rule matches, Surge builds the response locally and skips the upstream request entirely.

{% hint style='info' %}
Map Local only applies to requests handled by the HTTP engine, and only when the Rewrite feature is enabled. HTTPS requests can only be matched if [MITM](mitm.md) is enabled for the hostname. See [HTTP Processing](overview.md) for details.
{% endhint %}

### Parameters

#### URL Pattern

Each line is defined by multiple parameters, separated by spaces, the first of which is a regular expression for the URL. If an HTTP request (or a decrypted HTTPS request) matches this expression, the rule is applied.

#### `data-type`: Optional, default: file

Surge currently supports four types of data:

- `file`: Returns the content of a specific file or URL.
- `text`: Returns the text of the data field, encoded in UTF-8. {{ book.VER | replace("%TEXT%", "iOS 5.9.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.1+") }}
- `tiny-gif`: Returns a 1px GIF. {{ book.VER | replace("%TEXT%", "iOS 5.9.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.1+") }}
- `base64`: Returns binary data encoded in base64. {{ book.VER | replace("%TEXT%", "iOS 5.9.1+") }} {{ book.VER | replace("%TEXT%", "Mac 5.5.1+") }}

If `data-type` is omitted, `file` is used.

#### `data`

- For `file` type, this field should be the path to the data file, with relative paths being relative to the profile's directory. On macOS, absolute paths can also be used. A URL may also be used; the resource is downloaded and cached. On iOS and tvOS, the file size is limited to 15 MB.

- For `text` type, this field is the content itself.

- For `tiny-gif` type, this field is meaningless.

- For `base64` type, this field should contain valid base64 data.

{% hint style='tip' %}
You can use `data-type=text data=""` to return an empty result.
{% endhint %}

#### `header`: Optional

Customize the HTTP headers of the returned response. Use `|` to separate multiple key-value pairs, e.g. `header="a:b|foo:bar"`.

The value may also be a base64-encoded string of newline-separated header lines. If the value contains no `:`, Surge treats it as base64.

#### `status-code`: Optional, 200–999, default: 200

The HTTP status code of the returned response. Values outside 200–999 are invalid. The upper bound of 999 allows mocking non-standard status codes.

### About Content-Type

You can use the `header` parameter to control the `Content-Type` of the returned response. If not provided, Surge tries to complete it automatically:

- For `file` type, Surge tries to convert the file extension to a MIME type. If it fails, `application/octet-stream` is used.

- For `text` type, `text/plain` is used by default.

- For `tiny-gif` type, `image/gif` is used by default.

- For `base64` type, `application/octet-stream` is used by default.
