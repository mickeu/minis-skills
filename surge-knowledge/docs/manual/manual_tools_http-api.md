# HTTP API {{ book.VER | replace("%TEXT%", "iOS 4.4.0+") }} {{ book.VER | replace("%TEXT%", "Mac 4.0.0+") }}

You may use the HTTP API to control Surge programmatically.

## Configuration

```
[General]
http-api = examplekey@0.0.0.0:6171
http-api-tls = false
http-api-web-dashboard = false
```

Setting `http-api-web-dashboard = true` enables a web dashboard served on the same listener, so you can control Surge from a web browser. See the [\[General\] section reference](../profile/general.md) for these options.

## Authentication

The API key must be filled in the `X-Key` header for all requests.

```
GET /v1/events
X-Key: examplekey
Accept: */*
```

In some specific situations, if it is not convenient to set the header, you can also pass it through the URL query. For example, directly downloading the CA certificate through a browser.

```
http://127.0.0.1:6171/v1/mitm/ca?x-key=examplekey
```

## HTTPS (TLS)

Setting `http-api-tls = true` enables HTTPS support for the HTTP API service. Surge will use the CA certificate of [MITM](../http/mitm.md) to generate the server certificate for the corresponding access address. You need to install the certificate on the client device manually.

## Basic Constraints

Surge only uses GET and POST methods.

* For the GET method, use URL queries to send parameters.
* For the POST method, use a JSON body to send parameters.

Surge always returns a JSON body as the response.

## Paths

### Toggle Capabilities

* GET /v1/features/mitm
* POST /v1/features/mitm
* GET /v1/features/capture
* POST /v1/features/capture
* GET /v1/features/rewrite
* POST /v1/features/rewrite
* GET /v1/features/scripting
* POST /v1/features/scripting
* GET /v1/features/system_proxy (Surge Mac Only)
* POST /v1/features/system_proxy (Surge Mac Only)
* GET /v1/features/enhanced_mode (Surge Mac Only)
* POST /v1/features/enhanced_mode (Surge Mac Only)

Use the GET method to obtain the state of a capability.

GET Response example:

```
{"enabled":true}
```

Use the POST method to adjust the state of a capability.

POST Request example:

```
{"enabled":true}
```

### Outbound Mode

* GET /v1/outbound
* POST /v1/outbound

Use GET to obtain the outbound mode, and use POST to change it.

GET Response example:

```
{"mode":"rule"}
```
POST Request example:

```
{"mode":"rule"}
```

Possible modes: direct, proxy, rule

* GET /v1/outbound/global
* POST /v1/outbound/global

Obtain or change the default policy for global outbound mode.

GET Response example:

```
{"policy":"ProxyA"}
```
POST Request example:

```
{"policy":"ProxyB"}
```

### Proxy Policy

* GET /v1/policies

List all policies.

* GET /v1/policies/detail?policy_name=ProxyNameHere

Obtain the detail of a policy.

* POST /v1/policies/test

Test policies with a URL.

Request example:

```
{"policy_names": ["ProxyA", "ProxyB"], "url": "http://bing.com"}
```

* GET /v1/policy_groups

List all policy groups and their options.

* GET /v1/policy_groups/test_results

Obtain the test result of a url-test/fallback/load-balance group.

* GET /v1/policy_groups/select?group_name=GroupNameHere

Obtain the option of a select group.

Response example:

```
{"policy": "ProxyA"}
```

* POST /v1/policy_groups/select

Change the option of a select group.

Request example:

```
{"group_name": "GroupA", "policy": "ProxyA"}
```

* POST /v1/policy_groups/test

Test a group immediately.

Request example:

```
{"group_name": "GroupA"}
```

Response example:

```
{
    "available": [
        "ProxyA",
        "ProxyB"
    ]
}
```

### Requests

* GET /v1/requests/recent

List recent requests.

* GET /v1/requests/active

List all active requests.

* POST /v1/requests/kill

Kill an active request.

Request example:

```
{"id": 100}
```

### Profiles

* GET /v1/profiles/current?sensitive=0

Obtain the text content of the current profile. If `sensitive` is false, all password fields are masked.

* POST /v1/profiles/reload

Execute profile reloading immediately.

* POST /v1/profiles/switch (Surge Mac Only)

Request example:

```
{"name": "Profile2"}
```

Switch to another profile.

* GET /v1/profiles {{ book.VER | replace("%TEXT%", "Mac Only 4.0.6+") }}

Get all available profile names.

* POST /v1/profiles/check {{ book.VER | replace("%TEXT%", "Mac Only 4.0.6+") }}

Request example:

```
{"name": "Profile2"}
```

Check the profile. If the profile is invalid, an error is returned. Otherwise, the `error` field is null.

### DNS

* POST /v1/dns/flush

Flush the DNS cache.

* GET /v1/dns

Obtain the current DNS cache content.

* POST /v1/test/dns_delay

Test the DNS delay.

### Modules

* GET /v1/modules

List the available and enabled [modules](../profile/module.md).

Response example:

```
{
    "enabled": [
        "router.com"
    ],
    "available": [
        "Game Console SNAT",
        "Google Home Devices",
        "router.com",
        "MitM All Hostnames"
    ]
}
```

* POST /v1/modules

Enable or disable modules.

Request example:

```
{
	"router.com": false,
	"Google Home Devices": true
}
```

### Scripting

* GET /v1/scripting

List all the configured [scripts](../scripting/overview.md).

* POST /v1/scripting/evaluate

Evaluate a script with a mock environment. `script_text` is required; `mock_type` is a script type string such as `http-request` or `cron` (default: cron). The `$trigger` global is set to `http-api` during evaluation.

Request example:

```
{
    "script_text": "The content of JS script",
    "mock_type": "cron",
    "timeout": 5
}
```

* POST /v1/scripting/cron/evaluate

Evaluate a configured cron script immediately by name. Only cron-type scripts are accepted.

Request example:

```
{
    "script_name": "script1"
}
```

### Device Management {{ book.VER | replace("%TEXT%", "Mac Only 4.0.6+") }}

* GET /v1/devices

Obtain the list of the current active and saved devices.

* GET /v1/resources/devices-icon?id={iconID}

Obtain the icon of a device. You may get the iconID from device.dhcpDevice.icon.

* POST /v1/devices

Change the device properties. The `physicalAddress` field is required. You may adjust one or more properties from `name`, `address`, and `shouldHandledBySurge`.

Request example:

```
{
	"physicalAddress":"F0:9F:C2:00:00:00",
	"name": "Computer",
	"address": "192.168.1.200",
	"shouldHandledBySurge": true
}
```

### Misc

* POST /v1/stop

Shutdown the Surge engine. If Always On is enabled on Surge iOS, the Surge engine will restart.

* GET /v1/events

Obtain the content of the event center.

* GET /v1/rules

Obtain the list of rules.

* GET /v1/traffic

Obtain traffic information.

* POST /v1/log/level

Change the log level for the current session.

Request example:

```
{"level": "verbose"}
```

* GET /v1/mitm/ca

Obtain the CA certificate for MITM, in DER binary format. (Certificate only, no private key included)

### Prometheus Metrics {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

* GET /v1/metrics

Expose runtime statistics in the Prometheus text format, so Surge can be monitored with Prometheus and Grafana. This is especially useful for gateway deployments running around the clock. Unlike other endpoints, the response body is plain text instead of JSON.

Exposed metrics:

| Metric | Type | Description |
| --- | --- | --- |
| `surge_build_info{version,build,system}` | gauge | Always `1`; the build information is attached as labels |
| `surge_uptime_seconds` | gauge | Engine uptime |
| `surge_memory_bytes` | gauge | Physical memory footprint of the engine process |
| `surge_active_requests` | gauge | Number of in-flight requests |
| `surge_dns_cache_entries` | gauge | Number of cached DNS results |
| `surge_active_bans` | gauge | Number of active unauthorized-access bans |
| `surge_interface_in_bytes_total{interface}` | counter | Downloaded bytes per network interface since the engine started |
| `surge_interface_out_bytes_total{interface}` | counter | Uploaded bytes per network interface since the engine started |
| `surge_policy_in_bytes_total{policy}` | counter | Downloaded bytes per policy since the engine started |
| `surge_policy_out_bytes_total{policy}` | counter | Uploaded bytes per policy since the engine started |

The traffic counters reset when the engine restarts. PromQL functions such as `rate()` and `increase()` handle counter resets automatically: use `rate()` to derive real-time speeds, and `increase()` to aggregate traffic over any time window.

Since Prometheus does not send custom headers by default, pass the API key as a query parameter in the scrape configuration:

```yaml
scrape_configs:
  - job_name: surge
    metrics_path: /v1/metrics
    params:
      x-key: ["examplekey"]
    static_configs:
      - targets: ["192.168.1.1:6171"]
```
