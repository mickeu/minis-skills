# Testing

Surge uses testing URLs for internet connectivity checks, proxy latency tests, and throughput tests.

## Connectivity and Latency Testing

* `internet-test-url` in `[General]` sets the URL used for internet connectivity checks; it is also the test URL for the DIRECT policy.
* `proxy-test-url` in `[General]` sets the default test URL for proxy policies. A policy can override it with its own `test-url` parameter.
* Both HTTP and HTTPS testing URLs are accepted. {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }} With an HTTPS URL the latency figure is measured on a second HEAD request over the established TLS connection, so the TLS handshake itself is not counted.
* `test-timeout` in `[General]` sets the default timeout for connectivity tests. A policy can override it with its own `test-timeout` parameter.

See the [\[General\] section reference](../profile/general.md) for these options, and [Common Group Parameters](../policy-groups/parameters.md) for how policy groups resolve testing URLs and timeouts.

## Throughput Test Parameters {{ book.VER | replace("%TEXT%", "Mac 6.4.4+") }}

The `[Testing]` section customizes the download and upload parameters used by the throughput test.

```
[Testing]
download-url =
upload-url =
download-url-proxy =
upload-url-proxy =
download-concurrency = 4
upload-concurrency = 4
download-duration-limit = 10s
upload-size-limit = 1GB
upload-duration-limit = 10s
```

#### `download-url`

Optional, URL

The URL used for the download throughput test.

#### `upload-url`

Optional, URL

The URL used for the upload throughput test.

#### `download-url-proxy`

Optional, URL

The URL used for the download throughput test through proxy policies. If this parameter is omitted, Surge uses `download-url`.

#### `upload-url-proxy`

Optional, URL

The URL used for the upload throughput test through proxy policies. If this parameter is omitted, Surge uses `upload-url`.

#### `download-concurrency`

Optional, integer, default: 4

The number of concurrent download connections.

#### `upload-concurrency`

Optional, integer, default: 4

The number of concurrent upload connections.

#### `download-duration-limit`

Optional, duration, default: 10s

The maximum duration of the download test.

#### `upload-size-limit`

Optional, size, default: 1GB

The maximum amount of data uploaded during the upload test.

#### `upload-duration-limit`

Optional, duration, default: 10s

The maximum duration of the upload test.
