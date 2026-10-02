# Upstream Source and Synchronization

## Historical validated baseline

The entries below record the 2026-09-02 validation, not the current runtime. After a staged update, `upstream-manifest.json` is authoritative for imported source/version/hash provenance; it does not claim runtime validation.

Synchronized from the Surge Skill bundled on the user's Mac mini on 2026-09-02:

- SSH source alias: `macmini` (synchronization only; never a runtime dependency)
- Source directory: `/Applications/Surge.app/Contents/Resources/Skills/surge/`
- Surge for macOS: `6.9.0` (`12250`, formal release; bundled Skill files unchanged from build 12130)
- Core: `6009000`
- Controller Protocol: `25`
- Upstream `SKILL.md`: `904a33f378a45d89e945f470c446f5511d156c977d248f40a7652342ed121f05`
- Upstream `references/command-reference.md` before Minis invocation adaptation: `66f0b248fa7f696ea5f9b8511729f6c82a25c3bee23a6f5305ce4bdf6b64df4b`
- Upstream `references/plugin-authoring.md`: `d41b905588c8a941e5c208854f76b05b8a395f981a6027ba758a8b9ee4ac7193`
- `agents/openai.yaml`: `ef5cdcb1edd583d4b673774aa1e3b1c153b83df23cf1105191e8aac4d09912b1`
- `assets/logo.png`: `6e8ba4a6ee0ac71c7c03e4a5c7ee457d2f782abe71542e9819dc35443fb1d6f9`

The exact official `SKILL.md` snapshot is retained as `upstream-SKILL.md`. The local `SKILL.md` merges its operational guidance with Minis/iOS transport, credential, privacy, and safety rules. The command reference is copied from upstream and automatically receives a small Minis-specific invocation preface.

## Local additions that must survive synchronization

- `scripts/surge_cli.py`: Linux/iSH implementation of External Controller protocol plus the explicit-file official HTTPS `--check` fallback.
- `scripts/surge_ios.py`: localhost HTTP API fallback.
- `scripts/test_policy_descriptor.py`: local helper for testing an unconfigured node through `/v1/scripting/evaluate` plus `$httpClient` `policy-descriptor`, without changing the Profile.
- `scripts/sync_upstream.sh`: repeatable import command.
- `scripts/adapt_upstream_reference.py`: adapts command-reference section 1.1, keeps sensitive profile dumps opt-in, and shell-quotes the `<nil>` assignment example. The remaining upstream command semantics are preserved.
- `scripts/install.sh`: installs the symlink; Minis environment variable `SURGE_CLI_PASSWORD` is the default credential path.
- `references/diagnostics.md`: task-specific routing, DNS, temporary-rule, performance and tunnel guidance; preserve on sync.
- `references/platform-compatibility.md`: platform limitations and historical protocol verification snapshot; preserve on sync.
- `scripts/update_upstream.py`: staged import, provenance, drift checks and recoverable application; `sync_upstream.sh` is its entry point.
- `scripts/acceptance.sh`: defaults to offline checks; `--controller` queries the local instance, `--network` additionally uploads a synthetic secret-free Profile and performs DNS requests.
- `references/controller-cli.md`: protocol and installation notes.
- `references/http-api.md`: HTTP API fallback reference.
- `references/plugin-authoring.md`: exact official macOS plugin authoring guide, synchronized from upstream.
- `SKILL.md`: curated Minis overlay; never blindly overwrite with the macOS file.

Do not sync credential files, profiles, request bodies, API keys, Controller passwords, or any other secrets into the Skill directory.

## Update workflow

Check official release notes and relevant Mac/iOS differences first. No relevant change means no client rewrite. Reading the Mac source is an SSH task: follow the SSH skill and verify the host; never disable host-key checks.

```sh
# Prepare only; downloads five explicit official files, never changes active skill.
/var/minis/skills/surge-ios/scripts/sync_upstream.sh prepare --host macmini
# After reviewing the returned directory's review.diff, raw/ and staged/:
/var/minis/skills/surge-ios/scripts/sync_upstream.sh apply /var/minis/workspace/surge-updates/TRANSACTION
```

No arguments also means prepare. The old positional alias syntax is removed. Local/offline fixtures use `prepare --source DIRECTORY --version LABEL`.

- Raw source and diff persist even if adaptation rejects a new official reference hash. Review changed CLI options/semantics, update the adapter and its reviewed hash, test it, then prepare again. Do not approve a hash without reviewing the text.
- Apply only within user-authorized update scope. It checks source and staged hashes for drift, preserves local overlays, creates a persistent backup and writes `upstream-manifest.json` with source hashes/version and **runtime not tested** status. Official command-reference raw text is retained separately.
- Handled apply failures restore touched files. This is not a filesystem-wide atomic transaction or kill-proof rollback: if interrupted with `state=applying`, inspect the transaction and restore from `backup/` using its before-hashes before attempting another update. Do not run concurrent updates.
- Manually merge relevant new workflows into local references/entry; imported source versions must not replace historical **tested** baselines without corresponding evidence.
- Run `scripts/acceptance.sh` for offline syntax/links. Use `--controller` only for relevant integration checks after confirming the instance/engine; `--network` additionally sends DNS requests and uploads a synthetic no-secret Profile. No mode changes settings. `watch speed` is only a first-frame subscription smoke test, not full streaming validation.
- Transport/argument conversion changes need targeted fixtures and, when relevant, device tests. Restart, temporary-rule mutation and bandwidth tests remain separately authorized operations, never automatic acceptance steps.

No packaging step is part of updates. If the user later requests a shareable archive, handle it separately with explicit content and credential review.

## Runtime architecture

The Minis CLI does not execute the macOS Mach-O binary and does not need SSH at runtime. It connects to Surge iOS External Controller (default `127.0.0.1:6170`) using:

1. password plus CRLF;
2. welcome JSON plus CRLF;
3. one textual command line plus CRLF (bare verb, each following argv item double-quoted);
4. one or more JSON Lines result/event frames.

Surge iOS Protocol 25 still accepts the legacy `{"argv":[...]}` request, but the formal Surge Mac 6.9.0 build 12250 CLI emits the textual format, which the Minis client now follows. Its bundled official Skill/reference files are byte-identical to those first synchronized from build 12130.

Because the Controller parses most command arguments, newly supported ordinary commands can generally be passed through without adding an HTTP endpoint mapping. The local client must still reproduce official CLI-side conversions (currently `summary`, `profile diff`, `rule temp`, `watch speed`, and script-file Base64/mock-type encoding). Online `plugin` operations are ordinary Controller commands on macOS; `plugin validate` and `plugin pack` are local macOS CLI tools and are not implemented in iSH. Human-readable formatters in `surge_cli.py` are optional; `--raw` is the authoritative Controller response.
