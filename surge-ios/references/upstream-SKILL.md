---
name: surge
description: Operate and troubleshoot Surge via surge-cli, including command discovery, runtime diagnostics, state inspection (dump/watch/test), and environment mutation with set key-paths. Use when a task asks to control Surge behavior, inspect live status, adjust policy/runtime switches, or automate Surge operations from CLI.
---

# Surge CLI Ops

Use this skill to run Surge operations safely and consistently through `surge-cli`.

## Startup

1. Resolve executable path in this order:
   - `surge-cli` in `PATH`
   - `/Applications/Surge.app/Contents/Applications/surge-cli`
2. Prefer JSON output with `--raw` for machine parsing.
3. If operating on remote instances, add `--remote password@host:port`.

## Baseline Context Workflow

Before mutating runtime settings, collect baseline state:

1. `surge-cli --raw environment`
2. `surge-cli --raw dump policy`
3. `surge-cli --raw dump profile`

After changes, re-run the relevant read commands to verify effects.

## Mutation Rules

When using `set`:

1. Use minimal key-path deltas only.
2. Batch related updates in one command when possible.
3. Treat `<nil>` and `(null)` as null assignments.
4. Re-check `environment` immediately after mutation.

Examples:

```bash
surge-cli --raw set ProxyMode=2
surge-cli --raw set ProxyGroupSelection.Proxy=HK
surge-cli --raw set AutoPolicyGroupOverride.Streaming=<nil>
```

## Streaming Command Handling

For streaming commands (for example diagnostics/bandwidth tests):

1. Process incremental chunks.
2. Respect completion markers (`hasMore=false` or command-specific completion payload).
3. Do not assume a single response frame.

## Routing Decision Diagnostics

To answer "how would Surge route this request" without generating traffic:

1. `surge-cli --raw rule match <host|url>` shows the matched rule and final policy.
2. `surge-cli --raw rule explain <host|url>` additionally walks every policy-group
   hop with its decision reason — prefer it when the question is "why".
3. `surge-cli --raw geoip <ip>` and `surge-cli --raw dns trace <domain>` verify the
   database and resolution inputs a rule decision depends on.
4. `surge-cli --raw http probe <url> [policy]` sends a real HEAD request when an
   end-to-end confirmation is needed.

## Temporary Rules

Use `rule temp` for immediate, profile-independent routing changes (highest
priority, discarded when Surge stops):

```bash
surge-cli rule temp add "DOMAIN-SUFFIX,example.com,Proxy"
surge-cli rule temp list
surge-cli rule temp flush
```

Prefer temporary rules over profile edits for debugging sessions; quote any rule
containing spaces.

## Performance Inspection

1. `surge-cli --raw dump performance` reports engine memory and table sizes —
   the primary tool when investigating the iOS Network Extension memory limit.
2. `surge-cli --raw dump rule-usage` shows per-rule match counters (non-destructive;
   counters accumulate since the app last collected them).
3. `surge-cli --raw benchmark rule-matching` measures average rule matching time.

## Tailscale and WireGuard Diagnostics

Treat `proxy-runtime-status` as the primary per-tunnel diagnostic command for
Tailscale and WireGuard issues:

1. Run `surge-cli dump policy` and locate the affected proxy's `lineHash`.
2. Run `surge-cli --raw proxy-runtime-status <line-hash>`.
3. Inspect the tunnel-specific `tailscale` or `wireguard` payload before using
   broad log searches.

This command exposes state that general status and connectivity tests do not,
including WireGuard peer handshakes and underlying policy information, plus
Tailscale session, Exit Node, DERP, connectivity, and peer-path details.

## Encryption Benchmark

Use `surge-cli --raw benchmark encryption [data-size-mib]` to measure encryption
throughput and correctness on the device running Surge. The size defaults to
100 MiB and accepts 1–1024 MiB. Treat it as a streaming command and distinguish
it from `test-policy-bandwidth`: the encryption benchmark measures local crypto
implementations, not network or proxy performance. A remote Controller command
benchmarks the remote Surge device.

## Platform and Capability Notes

1. Some commands are platform-limited (for example certain device-management and profile-edit commands).
2. Validate capability and platform before execution in automation workflows.
3. Newer commands require a matching Controller protocol version on the Surge
   side (`rule`/`dns`/`http probe`/`security ban` need ≥20; `geoip`,
   `dump performance|rule-usage|virtual-ip`, and `benchmark rule-matching` need
   ≥22; `vmnet` needs ≥23). Older cores answer `Unknown command`; check
   `surge-cli version` when targeting remote or outdated instances.
4. For gateway-mode client connectivity issues on macOS, inspect the VMNET
   interface directly: `vmnet arp` / `vmnet ndp` for neighbor resolution and
   `vmnet ra` for IPv6 RA takeover state.

## Reference

Read detailed command semantics, full command list, and environment key definitions from:

- [Command Reference](references/command-reference.md)
