# Surge iOS HTTP API Reference

Official manual: <https://manual.nssurge.com/others/http-api.html>

Requires Surge iOS 4.4.0+. Send `X-Key` on every request. GET uses query parameters; POST uses a JSON body; responses are JSON unless noted.

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

### Miscellaneous
- `POST /v1/stop`
- `GET /v1/events`
- `GET /v1/rules`
- `GET /v1/traffic`
- `POST /v1/log/level` — `{ "level": "verbose" }`
- `GET /v1/mitm/ca` — DER certificate, not JSON

## Excluded macOS-only endpoints

Do not use these for this iOS Skill: `system_proxy`, `enhanced_mode`, profile listing/switch/check, and device management endpoints documented as Mac Only.

This reference was summarized from the official manual on 2026-07-24. Consult the official URL before adding or changing endpoints.
