# Surge CLI

Surge Mac provides a CLI program for controlling Surge from the command line. You may find it at `/Applications/Surge.app/Contents/Applications/surge-cli`.

Use `--help` to get the latest usage information, or `help <command>` for the detailed usage of one command or command family, for example `help rule match` or `help dump`.

```
Surge CLI
Usage: surge-cli <command> [arguments]

Command groups:
  Status       status, summary, version
  Routing      mode, global-policy, policy-group, rule match, rule explain, rule temp
  Profile      profile, module, feature, managed-profile, external-resource
  Network      dns, geoip, http probe, test, diagnostics, flush dns
  Inspection   dump, watch, log, logbook, proxy-runtime-status
  Automation   script, script-log, benchmark
  Gateway      device, vmnet, security ban
  Control      reload, switch-profile, kill, stop, unattended-upgrade
  Environment  environment, set, set-log-level

Available parameters:
  --raw - Output raw JSON instead of the human-readable command format
  --remote/-r <host:port> - Connect to a remote Surge instance. IPv6 uses [address]:port
  --password-stdin - Read the remote password from the first line of stdin
  Remote password fallback: SURGE_CLI_PASSWORD, then a secure terminal prompt
Utilities:
  --check/-c <path> - Check whether a profile is valid.
```

Running `surge-cli` without a command enters the interactive mode, which supports command auto-completion and history.

The `--remote` parameter requires `external-controller-access` to be configured on the remote instance; see [Surge Dashboard](dashboard.md).

## Expanded Management and Diagnostics {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Surge CLI includes the following additional command groups. Use `surge-cli <command> --help` for the complete options supported by a command.

| Command | Purpose |
| --- | --- |
| `status` | Show the active profile, outbound mode, feature states, uptime, and version information. |
| `version` | Show Surge, Core, Controller protocol, operating-system, and device versions. |
| `dump summary` | Show a passive summary of interfaces, addresses, routers, DNS servers, Wi-Fi or cellular state, and configuration warnings. |
| `mode` | View or switch the Rule, Direct, and Global Proxy outbound modes. |
| `global-policy` | View or change the policy used in Global Proxy mode. |
| `policy-group` | List groups, inspect or change selections, and clear an automatic-group override. |
| `profile` | Inspect, validate, list, or switch profiles. Listing and validation are available on macOS. |
| `module` | List modules and enable or disable multiple modules. |
| `feature` | Inspect or control MitM, Rewrite, Scripting, HTTP Capture, Packet Capture, and Cellular Mode. System Proxy and Enhanced Mode are also available on macOS. |
| `device` | List or inspect Gateway Mode devices on macOS. |
| `reconnect-device` | Reconnect an access-point client on macOS. |
| `script list` / `script run` | List configured scripts or run a cron script by name. |
| `log` / `log watch` | Read recent logs or stream new log entries. |
| `logbook` / `script-log` | Read structured [Logbook](logbook.md) records or the log from a script execution. |
| `benchmark encryption` | Measure encryption and decryption performance on the Surge device. |
| `managed-profile update` | Force an update check for the active managed profile, validate the result, replace the profile, and reload it. |
| `test-policy-bandwidth` | Run a bandwidth test for a policy. |
| `proxy-runtime-status` | Show protocol-specific runtime details, including Tailscale and WireGuard state. |

These commands can operate compatible Surge iOS 5.21.0 and Surge tvOS 5.21.0 instances through `--remote`. Query and diagnostic commands use readable formatted output by default; use `--raw` for automation. Remote Controller passwords can be entered through the secure prompt, `SURGE_CLI_PASSWORD`, or `--password-stdin` instead of placing the password in the command line.

See [Surge CLI Updates](https://nssurge.com/blog/surge-cli-updates/) for an overview of the new commands.

## Routing and Network Diagnostics {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

Surge CLI includes the following commands for diagnosing routing decisions and network state without generating real traffic.

| Command | Purpose |
| --- | --- |
| `rule match` | Evaluate the active rule set for a hostname or URL without creating a connection, and show the matched rule and final policy. All matching attributes — process path, User-Agent, source address, client device, protocol, and more — can be supplied as `key=value` options. |
| `rule explain` | Show why a request selects a particular policy: the matched rule, each policy-group decision with its reason, the Smart Group selection, and the underlying proxy chain. |
| `rule temp` | List, add, remove, modify, or clear temporary rules. Temporary rules take effect immediately, precede all profile rules, and are discarded when Surge stops, making them convenient for debugging sessions. |
| `dns lookup` / `dns trace` | Resolve a domain through Surge's DNS pipeline and show the answers, responding server, interface, route, timing, and cache lifetime. `dns trace` also includes the complete resolver trace log, and the lookup can be forced through a specific network interface. |
| `geoip` | Look up an IP address in the local GeoIP and ASN databases — the same data `GEOIP` and `IP-ASN` rules match against — and show the database dates. |
| `http probe` | Send an HTTP HEAD request through a specified policy or the active rule system, reporting the status, latency, selected policy, matched rule, and response headers. |
| `summary` | The passive network summary is now a top-level command; the previous `dump summary` spelling remains available. |
| `profile diff` | Compare the original profile with the effective profile after modules have been applied. |
| `vmnet` | Inspect the virtual network interface used by Gateway Mode on macOS: interface status and addresses, the ARP table, the IPv6 NDP table, and the IPv6 RA takeover state. |
| `security ban` | Inspect or clear the bans triggered by repeated unauthorized access to the Controller ports. |
| `dump performance` | Show engine memory usage, uptime, active requests, and the sizes of the DNS cache, virtual IP, and temporary rule tables. |
| `dump rule-usage` | Show per-rule match counters, helping identify rules that never match. |
| `dump virtual-ip` | Query the virtual IP database for a specific IP address or domain. |
| `benchmark rule-matching` | Measure the average matching time of the active rule set. |
| `watch speed` | Continuously display real-time upload and download speeds. |

These commands can also operate compatible Surge iOS and Surge tvOS instances through `--remote`.

## Agent Skill {{ book.VER | replace("%TEXT%", "Mac 6.5.0+") }}

Surge includes an agent skill that exposes `surge-cli` capabilities to AI agents that support skills. The skill can be installed from `/Applications/Surge.app/Contents/Resources/Skills/`. Use a symbolic link when installing it so the skill can be updated together with the application bundle.

The bundled skill in Surge Mac 6.8.0 includes instructions for the expanded management and diagnostics commands described above. {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

The bundled skill in Surge Mac 6.9.0 additionally covers the routing and network diagnostics commands, including `rule match`/`rule explain`, temporary rule management, DNS and GeoIP lookups, and the `vmnet` gateway diagnostics. {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}
