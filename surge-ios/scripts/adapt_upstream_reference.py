#!/usr/bin/env python3
"""Apply Minis transport notes to an upstream Surge command reference."""
from pathlib import Path
import sys

import hashlib

# Reviewed official baseline. Unknown upstream revisions require reviewing the
# raw diff and updating this set; never silently discard new CLI options.
REVIEWED_SHA256 = {
    '66f0b248fa7f696ea5f9b8511729f6c82a25c3bee23a6f5305ce4bdf6b64df4b',
}
path = Path(sys.argv[1])
text = path.read_text()
if hashlib.sha256(path.read_bytes()).hexdigest() not in REVIEWED_SHA256:
    # Idempotent execution is permitted only for the exact installed adaptation.
    if hashlib.sha256(path.read_bytes()).hexdigest() != '5331f03b90a1d6b21e406057b48364499b7b7a43697f566746e1ec6a0170c51f':
        raise SystemExit('Unreviewed upstream reference: inspect raw diff and update reviewed baseline before adaptation')
start = text.index("## 1. CLI Usage")
end = text.index("### 1.2 Response envelope", start)
replacement = '''## 1. CLI Usage

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
- `--check <path>` / `-c <path>`: upload the explicitly named UTF-8 profile to Surge's official beta validation service (`https://services.nssurge.com/v1/config/validate`). This is remote validation, not the bundled macOS local parser. The CLI never uploads the active profile automatically; warn about profile secrets and redact a copy first when appropriate.
- `--help` / `-h`: print help.
- If no command is provided, the Minis implementation prints help rather than entering an interactive terminal.
- Command keywords are handled by the connected Controller.

'''
text = text[:start] + replacement + text[end:]

# The upstream baseline includes a full profile dump, which may expose proxy
# addresses or subscription URLs. Keep it opt-in in the Minis reference.
text = text.replace(
    "Before mutating settings, collect context with `environment`, `dump policy`, and `dump profile`.",
    "Before mutating settings, collect context with `status`, `environment`, and `dump policy`. Run `dump profile` only when necessary and treat its output as sensitive.",
)
text = text.replace(
    'surge-cli set AutoPolicyGroupOverride.Streaming=<nil>',
    "surge-cli set 'AutoPolicyGroupOverride.Streaming=<nil>'",
)
path.write_text(text)
