# Policy Groups
Policy groups are used to organize and manage multiple proxy nodes, determining which node to use based on different selection strategies. Policy groups can contain proxy servers, other policy groups, or built-in policies, and can also mount subscription sources via `urls`.
Supported policy group types: `select` (manual selection), `auto_test` (automatic latency test), `smart` (smart selection), `fallback` (failover), `load_balance` (load balancing), `external` (external resource), `conditional` (conditional selection).
Built-in policies: `DIRECT` (direct connection), `REJECT` (reject connection).
## Common Fields​
The following fields are common to the five basic policy group types (`select`, `auto_test`, `smart`, `fallback`, `load_balance`):
  * **name** (string), required
Policy group name, must be globally unique.
  * **policies** (string array), optional
List of sub-policies. Can be proxy server names, other policy group names, or built-in policies (`DIRECT`, `REJECT`). May be omitted; a group with only `urls` configured is a pure subscription group.
  * **flatten** (bool), optional
Expand all proxy nodes from nested policy groups. When set to `true`, nodes within sub-policy groups are fully expanded rather than showing only the policy group name. Often used in conjunction with `filter`.
  * **filter** (string), optional
A regular expression filter that retains only nodes whose names match (e.g., `(?i)香港|HK`). Always applies to subscription nodes from `urls`; static sub-policies are filtered only when expanded via `flatten`.
  * **urls** (string array), optional
List of subscription URLs, supporting HTTP/HTTPS URLs or local file paths; nodes from multiple subscriptions are merged. Can be configured together with `policies`: subscription nodes are placed after the static sub-policies and deduplicated by name. See Subscription File Format for the file format.
  * **update_interval** (integer), optional
Subscription update interval in seconds, default 86400 (24 hours). Set to 0 or a negative value to disable automatic updates. Only takes effect when `urls` is configured.
  * **block_quic** (bool), optional
Block the QUIC protocol. When set to `true`, connections using this policy group will not use the QUIC/HTTP3 protocol. Takes priority over the global `block_quic`, but is overridden by the proxy's own `block_quic` setting.
  * **icon** (string), optional
Icon, supports SF Symbols names or icon URLs.
  * **hidden** (bool), optional
Whether to hide this policy group in the UI.
  * **prev_hop** (string), optional
Previous hop proxy, used to build proxy chains. Traffic path: local device → previous hop proxy → current node → destination.
  * **latency_test_url** (string), optional
Per-group latency test / health check URL. Takes precedence over the global `proxy_latency_test_url` and `direct_latency_test_url`; falls back to the global settings when not configured.
For `select`, this is used for manual latency tests from the UI; for `auto_test`, for automatic latency testing; for `fallback` and `load_balance`, for background health checks.
## Manual Selection​
The user manually selects which sub-policy to use.
Uses only the common fields, no additional fields.
    - select:  
        name: "Manual Selection"  
        policies:  
          - HK Node  
          - JP Node  
          - Auto Select  
        icon: globe  
## Auto Test​
Periodically tests the latency of all sub-policies and automatically selects the node with the lowest latency. When a node with lower latency is detected, it decides whether to switch based on `tolerance`.
In addition to the common fields, the following fields are also supported:
  * **interval** (integer), optional
Latency test interval in seconds, default 600. Set to 0 or a negative value to disable automatic latency testing.
  * **tolerance** (integer), optional
Switch tolerance in milliseconds, default 100. A switch occurs only when the new node's latency is faster than the current node by more than this value, preventing frequent switches when latencies are similar.
  * **timeout** (integer), optional
Timeout for a single node's latency test in seconds, default 5, maximum 60.
    - auto_test:  
        name: "Auto Select"  
        policies:  
          - HK Node  
          - JP Node  
        interval: 600  
        tolerance: 100  
        timeout: 5  
## Smart Selection​
Continuously learns the health of each candidate node across probe rounds and picks the most robust one based on a combined score of latency, jitter, and reliability. Runtime failures are also fed back to the health profile so subsequent selections automatically avoid recently unstable nodes.
Differences from `auto_test`:
  * **Not misled by single-round noise** — abnormal samples in one round are smoothed out by EWMA.
  * **Avoids "low latency but unstable" nodes** — success rate is part of the ranking.
  * **Switches with hysteresis** — a candidate must be sufficiently cheaper than the current node and the minimum dwell time must have elapsed before switching.
  * **Adaptive probe cadence** — the probe interval lengthens when stable and shortens after a switch or failure.
Tuning parameters (sample count, hysteresis thresholds, jitter weight, etc.) use empirical defaults and are not configurable.
In addition to the common fields, the following fields are also supported:
  * **priorities** (object), optional
Sub-policy priority coefficients. Keys are regular expressions matched against sub-policy names; values are coefficients multiplied onto the candidate's health score:
    * `< 1` raises priority (score becomes smaller — easier to be selected)
    * `> 1` lowers priority
    * `0` always picks this candidate first; falls back to others when it fails
    * Default `1` (no bias)
Rules are evaluated in declaration order; the first regex that matches a candidate wins. Use `^name$` for an exact name match.
    - smart:  
        name: "Smart Selection"  
        policies:  
          - HK Premium  
          - HK Standard  
          - JP Node  
        priorities:  
          "^HK Premium$": 0.8   # always prefer this node  
          "(?i)HK": 0.9         # other HK nodes are slightly preferred  
          "JP": 1.2             # JP nodes are deprioritized  
## Fallback​
Tries sub-policies in order and selects the first available node. When the current node becomes unavailable, it automatically switches to the next one; when a higher-priority node becomes available again, it automatically switches back.
In addition to the common fields, the following fields are also supported:
  * **interval** (integer), optional
Health check interval in seconds, default 600. Set to 0 or a negative value to disable automatic health checks.
  * **timeout** (integer), optional
Timeout for a single node's health check in seconds, default 5, maximum 60.
    - fallback:  
        name: "Fallback"  
        policies:  
          - Primary Node  
          - Backup Node 1  
          - Backup Node 2  
        interval: 600  
## Load Balance​
Distributes traffic across multiple sub-policies. By default, connections to the same domain or IP are assigned to the same node, while different domains/IPs are distributed across different nodes; set `algorithm` to switch to round-robin rotation.
In addition to the common fields, the following fields are also supported:
  * **algorithm** (string), optional
Load balancing algorithm. Possible values:
    * `hash` (default) — hash by destination. Connections to the same destination domain/IP are assigned to a fixed node, while different destinations are spread across different nodes.
    * `round_robin` — rotation. Each new connection rotates to the next available node in turn. Connections to the same destination are also spread across different nodes, so the egress IP is not fixed, which may affect sites that rely on a stable egress IP.
Both algorithms skip nodes that fail health checks.
    - load_balance:  
        name: "Load Balance"  
        policies:  
          - Node 1  
          - Node 2  
          - Node 3  
        algorithm: round_robin  
## External Resource​
Loads a list of proxy nodes from a remote URL, supporting airport subscription links. Multiple subscription URLs can be configured, and nodes from all subscriptions are merged.
info
External is the legacy subscription-only form, kept for compatibility with existing configurations: it is equivalent to configuring `urls` directly on a policy group of the corresponding `type`, which additionally supports mixing subscriptions with static `policies`. External does not use the `policies` and `flatten` fields.
  * **name** (string), required
Policy group name, must be globally unique.
  * **type** (string), required
Selection strategy after loading nodes. Possible values: `select`, `auto_test`, `smart`, `fallback`, `load_balance`.
  * **urls** (string array), required
List of subscription URLs, supporting HTTP/HTTPS URLs or local file paths. Nodes from multiple subscriptions are merged.
  * **filter** (string), optional
A regular expression filter that retains only nodes whose names match from the subscription (e.g., `(?i)香港|HK`).
  * **interval** (integer), optional
Latency test / health check interval in seconds, only effective for `auto_test` and `fallback` types, default 600.
  * **tolerance** (integer), optional
Switch tolerance in milliseconds, only effective for the `auto_test` type, default 100.
  * **timeout** (integer), optional
Latency test / health check timeout in seconds, default 5, maximum 60.
  * **priorities** (object), optional
Sub-policy priority coefficients, only effective for the `smart` type. See Smart Selection for semantics.
  * **algorithm** (string), optional
Load balancing algorithm, only effective for the `load_balance` type. See Load Balance for semantics.
  * **update_interval** (integer), optional
Subscription update interval in seconds, default 86400 (24 hours). Set to 0 or a negative value to disable automatic updates.
  * **latency_test_url** (string), optional
Per-group latency test / health check URL. Takes precedence over the global `proxy_latency_test_url` and `direct_latency_test_url`; falls back to the global settings when not configured. Used for automatic latency tests when `type: auto_test`, and for health checks when `type: fallback`.
  * **block_quic** (bool), optional
Block the QUIC protocol.
  * **icon** (string), optional
Icon, supports SF Symbols names or icon URLs.
  * **hidden** (bool), optional
Whether to hide this policy group in the UI.
  * **prev_hop** (string), optional
Previous hop proxy.
    - external:  
        name: "Subscription"  
        type: auto_test  
        urls:  
          - "https://example.com/subscribe"  
        filter: "(?i)香港|HK"  
        interval: 600  
        tolerance: 100  
        update_interval: 86400  
### Subscription File Format​
Local or remote subscription files should return a set of proxy server configurations:
    proxies:  
      - trojan:  
          name: HK Node  
          server: hk.example.com  
          port: 443  
          password: password  
          udp_relay: true  
      - shadowsocks:  
          name: JP Node  
          server: jp.example.com  
          port: 8388  
          method: aes-256-gcm  
          password: password  
## Conditional Selection​
Automatically selects a sub-policy based on the current network environment (Wi-Fi SSID, BSSID, cellular network type). Rules are matched in order, and the first matching policy is used; if none match, the default policy is used.
  * **name** (string), required
Policy group name, must be globally unique.
  * **rules** (array), required
List of matching rules, matched in order. Three rule types are supported:
    * **ssid** \- Wi-Fi name matching, supports glob wildcards (e.g., `Home-*`, `Office*`)
    * **bssid** \- Wi-Fi router MAC address matching, supports glob wildcards (e.g., `aa:bb:cc:*`)
    * **cellular** \- Cellular network type matching, supports glob wildcards. Available values: `NR` (5G), `NRNSA` (5G NSA), `LTE` (4G), `WCDMA`, `HSDPA`, `HSUPA`, `CDMA`, `eHRPD`, `EDGE`, `GPRS`
Each rule contains two fields: `match` (glob match pattern) and `policy` (the policy to use when matched).
  * **default_policy** (string), required
Default policy, used when no rules match.
  * **block_quic** (bool), optional
Block the QUIC protocol.
  * **icon** (string), optional
Icon, supports SF Symbols names or icon URLs.
  * **hidden** (bool), optional
Whether to hide this policy group in the UI.
  * **prev_hop** (string), optional
Previous hop proxy.
  * **latency_test_url** (string), optional
Per-group latency test URL. Takes precedence over the global `proxy_latency_test_url` and `direct_latency_test_url`; falls back to the global settings when not configured. Used for manual latency tests of sub-policies from the UI.
    - conditional:  
        name: "Network Environment"  
        rules:  
          - ssid:  
              match: "Home-*"  
              policy: DIRECT  
          - bssid:  
              match: "aa:bb:cc:*"  
              policy: HK Node  
          - cellular:  
              match: "LTE"  
              policy: Auto Select  
        default_policy: Manual Selection  
## Configuration Example​
    policy_groups:  
      # Manual selection: filter Hong Kong nodes from subscription  
      - select:  
          name: "HK Node"  
          policies:  
            - Subscription  
          flatten: true  
          filter: "(?i)香港|HK|Hong Kong"  
          icon: globe  
      # Auto test  
      - auto_test:  
          name: "Auto Select"  
          policies:  
            - HK Node  
            - JP Node  
          interval: 600  
          tolerance: 100  
      # Mix static nodes with a subscription: subscription nodes come after  
      # the static sub-policies and are deduplicated by name  
      - auto_test:  
          name: "Subscription Picks"  
          policies:  
            - Self-hosted Node  
          urls:  
            - "https://example.com/subscribe"  
          filter: "(?i)香港|HK"  
          update_interval: 86400  
      # Smart selection  
      - smart:  
          name: "Smart Selection"  
          policies:  
            - HK Node  
            - JP Node  
            - SG Node  
      # Fallback  
      - fallback:  
          name: "Fallback"  
          policies:  
            - Primary Node  
            - Backup Node  
          interval: 600  
      # Load balance  
      - load_balance:  
          name: "Load Balance"  
          policies:  
            - Node 1  
            - Node 2  
      # External resource: merge multiple subscriptions  
      - external:  
          name: "Subscription"  
          type: auto_test  
          urls:  
            - "https://provider1.com/subscribe"  
            - "https://provider2.com/subscribe"  
          filter: "(?i)香港|日本|HK|JP"  
          update_interval: 86400  
      # Conditional policy group: switch based on network environment  
      - conditional:  
          name: "Network Environment"  
          rules:  
            - ssid:  
                match: "Home-*"  
                policy: DIRECT  
            - cellular:  
                match: "NR*"  
                policy: Auto Select  
          default_policy: HK Node