# Minis Surge CLI

A Python reimplementation of the transport and command-line surface used by Surge's `surge-cli --remote` mode, designed for iSH/Minis on iOS.

## Protocol

The External Controller transport is a CRLF-delimited JSON Lines stream:

1. Client sends password plus CRLF.
2. Server returns a welcome JSON object.
3. Client sends `{"argv":[...]}` plus CRLF.
4. Server returns one result JSON object, or a stream of JSON event objects.

No HTTP API translation is used. The Surge Controller parses most command arguments, so ordinary commands track the connected Surge build. The client also reproduces the official CLI's known local conversions for `summary`, `profile diff`, `rule temp`, `watch speed`, and `script evaluate <file>` (including mock-type name to numeric ID conversion). `--raw` returns the resulting Controller JSON unchanged apart from compact serialization.

## Installation

`/usr/local/bin/surge-cli` is a symlink to `scripts/surge_cli.py`.

Default controller: `127.0.0.1:6170` (override with `SURGE_CLI_REMOTE` or `--remote`).

Credential precedence:

1. `--password-stdin`
2. `SURGE_CLI_PASSWORD` — recommended for Minis; store it in Settings → Environment Variables
3. secure interactive prompt

The CLI does not create or read password files. When `SURGE_CLI_PASSWORD` is missing, offer the Minis environment-variable settings link rather than asking the user to disclose the password in chat.

## Compatibility

Most commands are transparently passed to Surge. Human-readable formatting is implemented for common commands such as status, version, mode, features, policy groups, rule match/explain, DNS lookup/trace, modules, GeoIP, performance, and macOS VMNET diagnostics. Other commands print pretty JSON; use `--raw` for scripting and exact Controller data.

Protocol 23 adds `vmnet status|arp|ndp|ra`. The local client passes these through and can render their response, but Surge iOS currently returns `Unsupported command`; the VMNET backend is macOS-only.

The local macOS-only `--check <path>` mode cannot work in iSH because it relies on the bundled Surge parser and is intentionally reported as unavailable.
