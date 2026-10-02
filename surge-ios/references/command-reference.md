# Surge CLI / Controller Command Reference (for AI Agents)

This document provides a complete operational reference for AI agents, including advanced commands not shown by `-h`.

## 1. CLI Usage

> Minis adaptation: this command catalog is synchronized from the Surge-bundled Skill. In Minis, `/usr/local/bin/surge-cli` connects directly to Surge iOS External Controller. Use this section's adapted invocation rules; the remaining command semantics are upstream documentation and platform restrictions still apply.

### 1.1 Basic format

```bash
surge-cli [--remote host:port] [--password-stdin] [--raw] <command> [args...]
```

Executable location in Minis:

```bash
/usr/local/bin/surge-cli
```

- `--raw`: output raw JSON (recommended for agents).
- `--remote` / `-r`: connect to another Controller; the Minis default is `127.0.0.1:6170`.
- Authentication comes from `--password-stdin`, `SURGE_CLI_PASSWORD`, or a secure prompt. Never put the password in `--remote`; the Minis CLI does not use password files.
- `--check <path>` / `-c <path>` is unavailable because it requires Surge's bundled macOS profile parser.
- `--help` / `-h`: print help.
- If no command is provided, the Minis implementation prints help rather than entering an interactive terminal.
- Command keywords are handled by the connected Controller.

### 1.2 Response envelope

Responses are JSON and usually include:

- `result`: success text
- `error`: error text
- payload fields (for example `requests`, `environment`)
- `hasMore` for streaming commands (`true` means more chunks follow)

## 2. Full Command Catalog

The table below is the full top-level command set handled by the controller (not just the subset shown in `-h`).

| Command | Args | Description | Notes |
|---|---|---|---|
| `watch` | `[event ...]` | subscribe to events; without args unsubscribes | `watch request` is common |
| `dump` | `<type> [extra]` | dump runtime state data | see 3.2 |
| `test` | `<type>` | environment diagnostics | see 3.3 |
| `environment` | none | return current environment dictionary | |
| `set` | `<key>=<value> ...` | update environment | see 4 |
| `set-log-level` | `<level>` | change runtime log level | does not write profile |
| `stop` | none | stop Surge | |
| `kill` | `<connection-id>` | terminate a connection | |
| `test-group` | `<group-name>` | retest a policy group immediately | |
| `test-all-policies` | none | retest all policies | |
| `test-policy` | `<policy...>` | test one or more policies | |
| `test-policy-udp` | `<policy...>` | UDP policy test | |
| `test-policy-external-ip` | `<policy>` | probe external IP via a policy | STUN-based |
| `test-policy-nat-type` | `<policy>` | probe NAT type via a policy | STUN-based |
| `test-policy-bandwidth` | `<download\|upload> <policy>` | run bandwidth diagnostics via a policy | streaming output |
| `benchmark` | `encryption [data-size-mib]` \| `rule-matching` | benchmark local encryption throughput or rule matching speed | encryption is streaming, see 3.3.1; rule-matching see 3.12 |
| `rule` | `<match\|explain> <host\|url> [port] [key=value ...]` | evaluate the rule set without creating a connection | see 3.9 |
| `dns` | `<lookup\|trace> <domain> [interface=<bsd-name>]` | resolve via Surge's DNS with optional resolver trace | see 3.10 |
| `geoip` | `<ip-address>` | look up the local GeoIP/ASN databases | see 3.10 |
| `http` | `probe <url> [policy]` | send an HTTP HEAD request and report status, timing, route, and headers | rule-set routing when policy omitted |
| `security` | `ban <list\|clear>` | inspect or clear unauthorized-access bans | |
| `vmnet` | `<status\|arp\|ndp\|ra>` | inspect the VMNET virtual interface (gateway mode) | macOS only, see 3.13 |
| `flush` | `<type>` | flush data | currently only `dns` |
| `reload` | none | reload main profile | |
| `show-policy` | `<policy-name>` | show policy details | |
| `retrieve-data` | `<record-id> <request\|response> [replica-dir]` | fetch captured request/response body | data-channel command |
| `test-network` | none | network delay test | returns `time` |
| `script` | `evaluate <base64-js> [mockType] [timeout] [engine] [argument]` | evaluate script | CLI has a convenience wrapper, see 3.4 |
| `diagnostics` | none | start diagnostics event stream | pair with `stop-diagnostics` |
| `stop-diagnostics` | none | stop diagnostics event stream | |
| `get-resource` | `device-icon <id...>` | fetch device icons (Base64) | |
| `set-dhcp-device` | `<mac> <type> [value]` | set DHCP device parameters | macOS only, see 3.5 |
| `remove-device-record` | `<identifier...>` | remove device records | macOS only |
| `switch-profile` | `<profile-name>` | switch to another profile | |
| `managed-profile` | `update` | update and reload the active managed profile | macOS only |
| `update-profile` | `<base64-rule-section>` | update Rule section | macOS only |
| `proxy-runtime-status` | `<line-hash>` | inspect one proxy's live runtime and recent errors | essential for Tailscale/WireGuard diagnosis, see 3.1 |
| `add-temp-rule` | `<rule>` | add temporary rule | |
| `del-temp-rule` | `<rule>` | delete temporary rule | |
| `update-temp-rule` | `<rule> <new-policy>` | change policy of temporary rule | |
| `flush-temp-rule` | none | clear all temporary rules | |
| `unattended-upgrade` | none | unattended upgrade | macOS only |
| `provider-message` | `<base64-data>` | send message to Packet Tunnel Provider | unsupported on macOS |
| `external-resource` | `list \| update <key\|all>` | external resource listing and update | |
| `test-ponte` | `<device-ponte-name>` | Ponte diagnostics | streaming output |

## 3. Subcommand Details

### 3.1 Tailscale and WireGuard diagnostics: `proxy-runtime-status`

```bash
surge-cli dump policy
surge-cli proxy-runtime-status <line-hash>
surge-cli --raw proxy-runtime-status <line-hash>
```

`proxy-runtime-status` is the primary per-proxy diagnostic command and is
especially important for Tailscale and WireGuard. General status, summary, and
connectivity-test commands do not expose the tunnel's internal runtime state.
Use `dump policy` to find the proxy's `line-hash`, shown in square brackets in
human-readable output, then pass it to this command.

The common response includes traffic and speed, UDP relay support, test
capability, runtime details, and recent connection errors. WireGuard adds the
effective underlying policy, active TCP/UDP connection counts, and each peer's
handshake state. Tailscale adds session and error state, local addresses, Exit
Node selection, DERP connections and reachability, peer paths, and MagicDNS or
other runtime peer details when available.

For a Tailscale or WireGuard connection, routing, relay, Exit Node, or handshake
problem, collect this command before broad log searches. Prefer `--raw` for
automation and support bundles so the nested tunnel payload remains intact.

### 3.2 `dump <type>`

Supported `type` values:

- `active`
- `recent`
- `request`
- `dns`
- `traffic`
- `auto-test-group-result`
- `policy`
- `rule`
- `map-remote`
- `map-local`
- `profile`
- `event`
- `policy-group-sub-policies`
- `traffic-stat` (optional second arg: `prefix`)
- `traffic-stat-host`
- `temp-rule`
- `summary`
- `virtual-ip-db`
- `virtual-ip <ip|domain-substring>` (targeted query, see 3.11)
- `smart-group-info`
- `performance` (see 3.11)
- `rule-usage` (see 3.11)

`surge-cli -h` shows only a subset.

For profile display mode in CLI:

```bash
surge-cli dump profile original
surge-cli dump profile effective
```

### 3.3 `test <type>`

Supported `type` values:

- `v4-router`
- `dns`
- `encrypted-dns`
- `external-ip`
- `nat-type`

Note: `test-policy*` commands are separate top-level commands, not part of `test <type>`.

### 3.3.1 Encryption throughput benchmark

```bash
surge-cli benchmark encryption
surge-cli benchmark encryption 25
surge-cli --raw benchmark encryption 100
```

`benchmark encryption [data-size-mib]` runs the encryption benchmark on the
device where Surge is running. With a remote Controller connection, it measures
the remote Surge device rather than the `surge-cli` host. The command streams
throughput and correctness results for supported stream and AEAD encryption
implementations; it does not measure network or proxy bandwidth.

The data size defaults to 100 MiB and accepts integers from 1 to 1024 MiB. Raw
chunks use `type` values `start`, `line`, and `complete`. Interrupting or
disconnecting the CLI cancels the benchmark after the active primitive call.

### 3.4 `script evaluate` (CLI convenience form)

Common CLI form:

```bash
surge-cli script evaluate <script-js-path> [mock-script-type] [timeout] [engine] [argument]
```

CLI reads `<script-js-path>`, converts it to Base64, and sends it to controller `script evaluate`.

Supported `mock-script-type` strings:

- `http-request`
- `http-response`
- `cron`
- `event`
- `rule`
- `dns`
- `generic`

Supported `engine` strings:

- `auto`
- `jsc`
- `webview`

### 3.5 `set-dhcp-device` subtypes (macOS only)

```text
set-dhcp-device <mac> takeover [0|1]
set-dhcp-device <mac> disable-udp-fast-path [0|1]
set-dhcp-device <mac> address [ipv4-or-empty]
set-dhcp-device <mac> name [display-name-or-empty]
set-dhcp-device <mac> icon [icon-name-or-empty]
```

### 3.6 `external-resource`

- `external-resource list`
- `external-resource update <hash-key>`
- `external-resource update all`

`list` includes `ready`, and remote resources may include `updatedAt`.

### 3.7 `managed-profile`

- `managed-profile update`

The command forcibly checks the active managed profile, waits for download,
validation, and file replacement, and schedules a profile reload when the
content changed. It returns `updated` or `unchanged`.

### 3.8 `watch` event types

Supported event names:

- `real-time-speed`
- `auto-test-group`
- `traffic`
- `request`
- `request-update`
- `summary`
- `environment`
- `dns`
- `diagnostics`
- `reload`
- `shutdown`
- `device-name-map`
- `policy-benchmark`
- `device-info`
- `dns-flush`

Examples:

```bash
surge-cli watch request
surge-cli watch summary environment traffic
surge-cli watch speed        # CLI alias of real-time-speed, rendered as ↓/↑ rates
surge-cli watch              # unsubscribe
```

### 3.9 `rule match` / `rule explain` and temporary rules

```bash
surge-cli rule match example.com 443
surge-cli rule match https://example.com process-path=/usr/bin/curl
surge-cli --raw rule explain https://example.com
```

Both evaluate the active rule set without creating a connection and return the
matched rule and final policy. `rule explain` additionally walks the
policy-group resolution: every group hop with its decision reason, the current
smart group pick, the underlying proxy chain, and the evaluation notes — use it
to answer "why did this request go through that policy".

A bare hostname defaults to TCP port 443; an HTTP(S) URL supplies URL, HTTP
Host, SNI, protocol, and port. `key=value` options override individual
descriptor fields: `hostname`, `dest-port` (alias `port`), `process-path`,
`user-agent`, `url`, `sni`, `http-host`, `source-address`, `source-port`,
`is-local` (alias `local`), `client-mac`, `listen-port`, `protocol`,
`device-name`. An empty value (for example `sni=`) clears an optional field.

Temporary rules: the CLI form `rule temp <list|add|remove|set-policy|flush>`
maps onto the controller commands `dump temp-rule`, `add-temp-rule`,
`del-temp-rule`, `update-temp-rule`, and `flush-temp-rule`. Temporary rules
take effect immediately, precede all profile rules, and are discarded when
Surge stops. Quote a rule that contains spaces:

```bash
surge-cli rule temp add "DOMAIN-SUFFIX,example.com,Proxy"
```

### 3.10 `dns lookup` / `dns trace` / `geoip`

```bash
surge-cli --raw dns lookup example.com
surge-cli --raw dns trace example.com interface=en0
surge-cli --raw geoip 8.8.8.8
```

`dns lookup` resolves through Surge's DNS pipeline and reports A/AAAA records,
the answering server, interface, path, timing, and cache expiry. `dns trace`
additionally includes the resolver trace log. `interface=<bsd-name>` forces the
lookup through one network interface and fails when it is unavailable.

`geoip` looks up an IP address in the local GeoIP and ASN databases — the same
data `GEOIP` and `IP-ASN` rules match against — and reports the country code,
ASN, AS organization, and both database dates. Fields are `null` when the
address is not present in a database.

### 3.11 `dump performance` / `dump rule-usage` / `dump virtual-ip`

- `dump performance`: engine memory footprint (`memory-bytes`), uptime, active
  request count, DNS cache entries, virtual IP entries, temporary rule count,
  and active ban count. Useful when tracking the iOS Network Extension memory
  limit on a remote device.
- `dump rule-usage`: per-rule match counters accumulated since the app last
  collected them (the apps drain the counters periodically, on iOS every 6
  hours). The dump itself is non-destructive.
- `dump virtual-ip <ip|domain-substring>`: targeted query of the virtual IP
  database — exact match for an IPv4 address, case-insensitive substring match
  for a domain. `dump virtual-ip-db` remains the full dump.

### 3.12 `benchmark rule-matching`

```bash
surge-cli --raw benchmark rule-matching
```

Measures the average matching time of the active rule set using random
hostnames (worst-case full scan; the result is a single response with
`average-ns`, not a stream). Useful for judging the cost of very large rule
sets on the device running Surge.

### 3.13 `vmnet` (macOS only)

```bash
surge-cli vmnet status
surge-cli --raw vmnet arp
surge-cli --raw vmnet ndp
surge-cli --raw vmnet ra
```

Inspects the VMNET virtual interface that backs the enhanced/gateway mode.
`status` always answers (reporting `running: false` when the interface is
down); the table commands error with "The VMNET virtual interface is not
active" when the interface is not running.

- `status`: interface configuration — main interface and MACs, IPv4 self/router
  addresses, IPv6 link-local/global addresses, advertised prefix, IPv6 router,
  MTU, and the sizes of the ARP/NDP/RA tables.
- `arp`: the IPv4 neighbor table learned from gateway clients (`ip`, `mac`,
  `age-seconds`).
- `ndp`: the IPv6 neighbor table in the same shape.
- `ra`: IPv6 RA takeover state — per-client MAC, learned link-local address,
  and time since the last RA sent; known routers with their remaining RA
  lifetimes (these are excluded from takeover while valid); and blacklisted
  clients.

Use `arp`/`ndp` when a gateway client cannot be reached, and `ra` when IPv6
takeover does not appear to affect a device.

## 4. `set` Command and Environment Dictionary (Key Section)

### 4.1 Syntax

```bash
surge-cli set <key-path>=<value> [<key-path>=<value> ...]
```

- Multiple `key=value` pairs are allowed in one command.
- Any argument without `=` fails with `Illegal parameter`.
- `<nil>` and `(null)` are treated as `nil`.

### 4.2 Key-path behavior

- Normal key-paths are applied via key-path assignment.
- Prefix `ProxyGroupSelection.` is handled as map merge for select-group decisions.
- Prefix `AutoPolicyGroupOverride.` is handled as map merge for auto-group overrides.

Examples:

```bash
surge-cli set ProxyMode=2
surge-cli set ProxyGroupSelection.Proxy=HK
surge-cli set AutoPolicyGroupOverride.Streaming=<nil>
surge-cli set RewriteEnabled=0 ScriptingEnabled=1
```

### 4.3 Top-level environment keys

| Key | Type | Meaning | Example |
|---|---|---|---|
| `ProxyGroupSelection` | `dict<string,string>` | current selection for select groups | `ProxyGroupSelection.<group>=<policy>` |
| `AutoPolicyGroupOverride` | `dict<string,string\|nil>` | override selection for auto groups | `AutoPolicyGroupOverride.<group>=<policy-or-<nil>>` |
| `ProxyMode` | `int` | outbound mode: `0=Direct` `1=Global Proxy` `2=Rule` | `ProxyMode=2` |
| `AllProxyModePolicyNameKey` | `string` | policy name used in global proxy mode | `AllProxyModePolicyNameKey=ProxyA` |
| `MitMEnabled` | `bool` | MITM switch | `MitMEnabled=1` |
| `RewriteEnabled` | `bool` | Rewrite switch | `RewriteEnabled=1` |
| `ScriptingEnabled` | `bool` | Scripting switch | `ScriptingEnabled=1` |
| `Replica` | `bool` | HTTP capture switch | `Replica=1` |
| `ReplicaSessionParameters` | `dict` | HTTP capture session parameters | see 4.4 |
| `InMemoryCaptureFilter` | `dict` | in-memory capture filter params | see 4.5 |
| `OnDiskCaptureFilter` | `dict` | on-disk capture filter params | see 4.5 |
| `PacketCaptureEnabled` | `bool` | packet capture switch | effective on iOS/tvOS |
| `PacketCaptureParameters` | `dict` | packet capture parameters | see 4.6 |
| `SGEnvironmentCellularModeEnabledKey` | `bool` | cellular mode switch | `SGEnvironmentCellularModeEnabledKey=1` |
| `SGEnvironmentCellularModeProcessPathsKey` | `array<string>` | allowed process paths in cellular mode | complex type, see 4.7 |

### 4.4 `ReplicaSessionParameters` fields

| Field | Type | Default |
|---|---|---|
| `sizeLimit` | `int` | `52428800` (50MB) |
| `requestCountLimit` | `int` | `100` |
| `timeLimit` | `int` (seconds) | `180` |
| `mitmOverride` | `bool` | `1` |
| `mitmOverrideHostnames` | `array<string>` | built-in default list |
| `mitmOverrideHostnamesDisabled` | `array<string>` | empty |

Example (scalar updates are straightforward):

```bash
surge-cli set Replica=1 ReplicaSessionParameters.requestCountLimit=200
```

### 4.5 `InMemoryCaptureFilter` / `OnDiskCaptureFilter` fields

| Field | Type | Meaning |
|---|---|---|
| `httpOnly` | `bool` | HTTP-only capture |
| `hideCrashReporterRequest` | `bool` | hide crash reporter traffic (default `1`) |
| `hideAppleRequest` | `bool` | hide Apple traffic |
| `hideUDP` | `bool` | hide UDP traffic |
| `filterType` | `int` | `0=None` `1=Whitelist` `2=Blacklist` `3=Pattern` |
| `keywordFilter` | `array<string>` | keyword list |
| `disabledKeywordFilter` | `array<string>` | disabled keywords |

### 4.6 `PacketCaptureParameters` fields

| Field | Type | Default |
|---|---|---|
| `sizeLimit` | `int` | `1048576` (1MB) |
| `packetCountLimit` | `int` | `100` |
| `timeLimit` | `int` (seconds) | `180` |
| `packetType` | `int` | `0=Unknown` `1=ICMP` `6=TCP` `17=UDP` |

### 4.7 Type handling notes (important for agents)

- CLI sends values as strings; booleans/integers rely on runtime conversion (`boolValue` / `integerValue`).
- Complex arrays/dictionaries are not ideal to set as raw string literals from shell commands.
- Recommended approach:
  - prefer scalar key-path updates;
  - use JSON/SDK path for complex structures when possible;
  - fetch `environment` first, then apply minimal deltas.

### 4.8 Runtime behavior notes

- Successful `set` triggers environment-change notifications.
- If `MitMEnabled=1` is invalid under current runtime conditions, it is auto-corrected to `0`.
- In global proxy mode (`ProxyMode=1`), an invalid `AllProxyModePolicyNameKey` is auto-fallbacked to a valid policy (or `DIRECT`).

## 5. Practical Recommendations for AI Agents

1. Prefer `--raw` and parse JSON directly.
2. Before mutating settings, collect context with `status`, `environment`, and `dump policy`. Run `dump profile` only when necessary and treat its output as sensitive.
3. For streaming commands (`diagnostics`, `test-policy-bandwidth`, `benchmark encryption`, `test-ponte`), handle incremental chunks and end conditions.
4. Check platform capability before using platform-limited commands (`update-profile`, `set-dhcp-device`, `provider-message`).
