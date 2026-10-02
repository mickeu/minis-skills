# Upstream Source and Synchronization

## Current snapshot

Synchronized from the Surge Skill bundled on the user's Mac mini on 2026-08-14:

- SSH source alias: `macmini` (synchronization only; never a runtime dependency)
- Source directory: `/Applications/Surge.app/Contents/Resources/Skills/surge/`
- Surge for macOS: `6.9.0` (`12100`)
- Core: `6009000`
- Controller Protocol: `23`
- Upstream `SKILL.md`: `3d18154d374db4439c843b16c7c394c99e18293b40a03652654202478180eeee`
- Upstream `references/command-reference.md`: `9ddfe6dd8a9871e612c0e3babdb262598a084d04d5f89bf4739b62f09c9e8b7f`
- `agents/openai.yaml`: `ef5cdcb1edd583d4b673774aa1e3b1c153b83df23cf1105191e8aac4d09912b1`
- `assets/logo.png`: `6e8ba4a6ee0ac71c7c03e4a5c7ee457d2f782abe71542e9819dc35443fb1d6f9`

The exact official `SKILL.md` snapshot is retained as `upstream-SKILL.md`. The local `SKILL.md` merges its operational guidance with Minis/iOS transport, credential, privacy, and safety rules. The command reference is copied from upstream and automatically receives a small Minis-specific invocation preface.

## Local additions that must survive synchronization

- `scripts/surge_cli.py`: Linux/iSH implementation of External Controller protocol.
- `scripts/surge_ios.py`: localhost HTTP API fallback.
- `scripts/sync_upstream.sh`: repeatable import command.
- `scripts/adapt_upstream_reference.py`: replaces only command-reference section 1.1 with Minis invocation rules.
- `scripts/install.sh`: installs the symlink; Minis environment variable `SURGE_CLI_PASSWORD` is the default credential path.
- `scripts/acceptance.sh`: non-destructive read-only acceptance test.
- `scripts/package_release.py`: scans and builds a sanitized ZIP for sharing.
- `references/controller-cli.md`: protocol and installation notes.
- `references/http-api.md`: HTTP API fallback reference.
- `SKILL.md`: curated Minis overlay; never blindly overwrite with the macOS file.

Do not sync credential files, profiles, request bodies, API keys, Controller passwords, or any other secrets into the Skill directory.

## Update command

```sh
/var/minis/skills/surge/scripts/sync_upstream.sh
```

Optional SSH alias argument:

```sh
/var/minis/skills/surge/scripts/sync_upstream.sh macmini
```

The script updates the exact upstream snapshot, command reference, agent metadata, and icon. It deliberately preserves the local `SKILL.md` and scripts. After synchronization, compare `references/upstream-SKILL.md` with the previous upstream hash and manually merge any new workflows or capability notes into local `SKILL.md`.

## Runtime architecture

The Minis CLI does not execute the macOS Mach-O binary and does not need SSH at runtime. It connects to Surge iOS External Controller (default `127.0.0.1:6170`) using:

1. password plus CRLF;
2. welcome JSON plus CRLF;
3. `{"argv":[...]}` plus CRLF;
4. one or more JSON Lines result/event frames.

Because the Controller parses most `argv`, newly supported ordinary commands can generally be passed through without adding an HTTP endpoint mapping. The local client must still reproduce official CLI-side conversions (currently `summary`, `profile diff`, `rule temp`, and script-file Base64 encoding). Human-readable formatters in `surge_cli.py` are optional; `--raw` is the authoritative Controller response.
