# Surge iOS HTTP API Reference

Official manual: <https://manual.nssurge.com/tools/http-api.html>

Requires Surge iOS 4.4.0+. Send `X-Key` on every request. GET uses query parameters; POST uses a JSON body; responses are JSON unless noted.

## Engine-state preflight (all tasks)

Before tasks that depend on Surge networking, and again after unexpected EOF/timeouts, check the target instance with `surge-cli --raw status` and `surge-cli --raw environment`. Follow the general Suspend workflow in `../SKILL.md`: a responsive Controller/HTTP API does not prove that the engine is processing traffic. A suspended engine may cause networking operations to fail, but EOF/timeouts alone prove neither suspension nor a bad node. If the state cannot be confirmed from available output, ask the user to check Suspend and VPN/engine state in the Surge UI. Do not silently resume/restart the engine or switch hosts; after an authorized recovery, recheck state and retry the original operation.

## iOS endpoints

### Features
- `GET|POST /v1/features/mitm` — `{ "enabled": true }`
- `GET|POST /v1/features/capture`
- `GET|POST /v1/features/rewrite`
- `GET|POST /v1/features/scripting`

### Outbound and policies
- `GET|POST /v1/outbound` — modes: `direct`, `proxy`, `rule`
- `GET|POST /v1/outbound/global` — `{ "policy": "ProxyA" }`
- `GET /v1/policies`
- `GET /v1/policies/detail?policy_name=...`
- `POST /v1/policies/test` — `{ "policy_names": [...], "url": "http://bing.com" }`
- `GET /v1/policy_groups`
- `GET /v1/policy_groups/test_results`
- `GET /v1/policy_groups/select?group_name=...`
- `POST /v1/policy_groups/select` — `{ "group_name": "GroupA", "policy": "ProxyA" }`
- `POST /v1/policy_groups/test` — `{ "group_name": "GroupA" }`

### Requests
- `GET /v1/requests/recent`
- `GET /v1/requests/active`
- `POST /v1/requests/kill` — `{ "id": 100 }`

### Profile, DNS, and modules
- `GET /v1/profiles/current?sensitive=0`
- `POST /v1/profiles/reload`
- `POST /v1/dns/flush`
- `GET /v1/dns`
- `POST /v1/test/dns_delay`
- `GET /v1/modules`
- `POST /v1/modules` — module-name-to-boolean map

### Scripting
- `GET /v1/scripting`
- `POST /v1/scripting/evaluate` — `script_text`, `mock_type`, `timeout`
- `POST /v1/scripting/cron/evaluate` — `{ "script_name": "script1" }`

### Test an unconfigured node with `policy-descriptor`

`POST /v1/policies/test` only accepts configured policy names. To probe a new node without editing or reloading the Profile, evaluate a cron script whose `$httpClient` request includes a complete Surge policy line as `policy-descriptor`. This option takes precedence over `policy`.

Use the bundled helper; the descriptor is read from a file or stdin so credentials do not enter shell history:

```sh
chmod 600 /tmp/node.policy
# /tmp/node.policy contains exactly one line, for example:
# Temp = trojan, example.com, 443, password=..., sni=example.com

SURGE_HTTP_API_BASE=http://127.0.0.1:6171 \
  python3 /var/minis/skills/surge-ios/scripts/test_policy_descriptor.py \
  --descriptor-file /tmp/node.policy \
  --url http://checkip.amazonaws.com
rm -f /tmp/node.policy
```

The helper reads the API key only from `SURGE_HTTP_API_KEY`, calls `/v1/scripting/evaluate`, and reports the probe status, response body, latency, and error without printing the descriptor. To use a user-specified active Mac/iOS Surge instance, set `SURGE_HTTP_API_BASE=http://<trusted-host>:6171`; do not silently switch to another host.

Apply the engine-state preflight above before interpreting `$httpClient` probe failures; Suspend is a general networking diagnostic consideration, not a `policy-descriptor`-specific limitation.

### Metrics (iOS 5.22.0+)
- `GET /v1/metrics` — Prometheus text exposition; it is not JSON and still requires the `X-Key` header.

Use the helper instead of printing the API key in a curl command:

```sh
python3 /var/minis/skills/surge-ios/scripts/surge_ios.py metrics
```

The formal iOS 5.22.0 build 3830 was verified to expose build info, uptime, memory, active request/DNS-cache/ban gauges, and per-interface/per-policy traffic counters. The official manual confirms the HTTP Controller route is `/v1/metrics`; bare `/metrics` is not an API route.

The official manual notes that traffic counters reset when the engine restarts; PromQL `rate()` and `increase()` handle counter resets. Prometheus cannot normally add `X-Key`, so an actual scrape configuration may pass the API key as the `x-key` query parameter. Do not place that key in chat, logs, or a shared config file.

### Miscellaneous
- `POST /v1/stop`
- `GET /v1/events`
- `GET /v1/rules`
- `GET /v1/traffic`
- `POST /v1/log/level` — `{ "level": "verbose" }`
- `GET /v1/mitm/ca` — DER certificate, not JSON

## 5.23.0 新增端点（iOS 3862 实测记录，2026-10-07）

官方手册已收录以下端点并标注 `iOS 5.23.0+ / Mac 6.10.0+`：

- `GET /v1/external_resources` — 列出当前 Profile 及已启用模块引用的所有外部资源（规则集、域名集、脚本、策略组列表）。响应含 `defines` 数组：`path/type/key/local/ready/updatedAt/updating/fromModule/error`。
- `POST /v1/external_resources/update` — 立即更新外部资源。Body: `{"key": "..."}` 更新单个，`{"key": "all"}` 更新全部。
- `GET /v1/geoip?ip=1.1.1.1` — 查询 IP 归属（国家/ASN/AS 组织），与 GEOIP/IP-ASN 规则及脚本 API 同一数据库。

**实测结论（Surge iOS 5.102.0 build 3862 = 5.23.0 RC1）**：以上三个端点在 3862 上全部返回 `{"error":"unknown path"}`（HTTP API 正常，`/v1/traffic` 等可用）。内置 Web Dashboard v2.0.9 亦无「外部资源」入口，其 JS 未调用相关端点。即：**iOS 3862 尚未实装这些新端点**，官方文档或超前于该 build；外部资源管理在 External Controller 协议（`surge-cli external-resource list/update`）中早已可用。预期后续 build / 正式版实装后可复测。

## Excluded macOS-only endpoints

Do not use these for this iOS Skill: `system_proxy`, `enhanced_mode`, profile listing/switch/check, and device management endpoints documented as Mac Only.

This reference was refreshed against the official manual and Surge iOS 5.22.0 build 3830 on 2026-09-02. Consult the official URL before adding or changing endpoints.
