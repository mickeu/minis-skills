# Profile Format

The profile is the source of truth for Surge behavior. Most profile content can be adjusted in the user interface, but advanced or experimental features may still require manual editing.

Surge profiles use an INI-like format. Content is divided into sections such as `[General]`, `[Proxy]`, `[Proxy Group]`, and `[Rule]`.

```
[General]
loglevel = notify

[Proxy]
ProxyA = http, 1.2.3.4, 80

[Rule]
DOMAIN-SUFFIX,example.com,ProxyA
FINAL,DIRECT
```

Each section has its own syntax. Sections like `[General]` and `[MITM]` use `key = value` lines, and line order usually does not matter. In ordered sections such as `[Rule]`, line order is part of the behavior.

## Sections

Surge recognizes the following section names. Content in unrecognized sections is preserved as-is when the profile is saved, without errors.

| Section | Purpose |
|---|---|
| `[General]` | [Global settings](general.md) |
| `[Proxy]` | [Proxy policies](../policies/overview.md) |
| `[Proxy Group]` | [Policy groups](../policy-groups/overview.md) |
| `[Rule]` | [Rules](../rules/overview.md) |
| `[Host]` | [Local DNS mapping](../dns/local-dns-mapping.md) |
| `[URL Rewrite]` | [URL Rewrite](../http/url-rewrite.md) |
| `[Header Rewrite]` | [Header Rewrite](../http/header-rewrite.md) |
| `[Body Rewrite]` | [Body Rewrite](../http/body-rewrite.md) |
| `[Map Local]` | [Map Local](../http/map-local.md) |
| `[MITM]` | [HTTPS decryption](../http/mitm.md) |
| `[Keystore]` | [Certificates and private keys](keystore.md) |
| `[SSID Setting]` | [Subnet settings](../features/subnet-settings.md) |
| `[Script]` | [Scripting](../scripting/overview.md) |
| `[Panel]` | [Information panels](../tools/panel.md) |
| `[Ponte]` | [Surge Ponte](../features/ponte.md) |
| `[Port Forwarding]` | [Port forwarding](../features/port-forwarding.md) |
| `[Testing]` | [Throughput testing](../tools/testing.md) |
| `[DHCP]` | [DHCP server](../features/dhcp.md) (Mac gateway mode) |
| `[Snell Server]` | [Built-in Snell server](../features/snell-server.md) |
| `[MTProto]` | [Built-in MTProto server](../features/mtproto.md) |
| `[WireGuard <name>]` | [WireGuard policy configuration](../policies/wireguard.md) |
| `[Tailscale <name>]` | [Tailscale policy configuration](../policies/tailscale.md) |
| `[Ruleset <name>]` | [Inline rule sets](../rules/ruleset.md) |

## Comments

Comment lines start with `#`, `;`, or `//`. Inline comments are also supported.

```
# This is a comment line.
; This is a comment line.
// This is a comment line.
```

```
dns-server = 8.8.8.8 // This is an inline comment.
dns-server = 8.8.8.8 # This is an inline comment.
dns-server = 8.8.8.8 ; This is an inline comment.
```

When using inline comments, there must be at least one space before the delimiter.

## Quoted Values {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Inside a double-quoted profile value, use `\"` for a literal double quote and `\\` for a literal backslash. This allows values containing quotes or backslashes to be saved and reloaded without changing their contents.

```
example = "a quoted value: \"text\"; path: C:\\Proxy"
```

## Profile Types

Profiles are divided into three categories:

1. Normal profile: created manually or used by default.
2. [Managed profile](managed-profile.md): usually provided by an enterprise administrator or service provider. A managed profile cannot be modified locally because it can be updated remotely. To make changes, first create a copy to turn it into a normal profile.
3. Enterprise profile: Enterprise version only. It cannot be modified, viewed, or copied.

## Detached Profile Section

To support complex setups, Surge can split one or more sections into another file with the `#!include` statement.

Main.conf

```
[Proxy]
#!include Proxy.dconf
```

The referenced file must contain the corresponding section declaration. The file can contain one section, multiple sections, or a complete profile.

Proxy.dconf

```
[Proxy]
ProxyA = http, 1.2.3.4, 80
```

This is useful when you want to:

1. Reference the `[Proxy]`, `[Proxy Group]`, and `[Rule]` sections of a managed profile while writing other sections yourself. This keeps proxy-related content updated without affecting local UI-managed settings.
2. Share sections across multiple profiles. For example, when using Surge on both iOS and macOS, `[Proxy]`, `[Proxy Group]`, and `[Rule]` are often the same, while `[General]` may be different. You can create `iOS.conf` and `macOS.conf`, then place the shared sections in another file.

```
[Proxy]
#!include Forwarding.dconf

[Proxy Group]
#!include Forwarding.dconf

[Rule]
#!include Forwarding.dconf
```

This way, adjusting `[General]` on iOS does not affect macOS, and you do not need to maintain two copies of the same routing configuration.

### Include Patterns

How a section can be edited in the UI depends on how `#!include` is used.

#### Dedicated Include

When a section contains only one `#!include` statement referencing a local file, the section remains fully editable in the UI. Changes made in the UI are written back to the included file. If that file contains other unused sections, only the section referenced by the main profile is modified.

```
[Proxy]
#!include Proxy.dconf
```

#### Multiple Includes {{ book.VER | replace("%TEXT%", "iOS 4.12.0+") }} {{ book.VER | replace("%TEXT%", "Mac 4.5.0+") }}

A section can combine content from multiple included files. Because Surge cannot determine how UI changes should be written back to the individual files, the section is read-only in the UI.

```
[Proxy]
#!include A.dconf, B.dconf
```

#### Mixed Content and Includes {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

`#!include` statements can be freely mixed with regular content in the same section. The included content expands exactly at the statement's position, so in ordered sections like `[Rule]`, where the statement sits decides the priority of the included rules.

```
[Rule]
#!include common-rule-a.dconf
DEST-PORT,123,DIRECT
#!include common-rule-b.dconf
```

For line-based sections — `[Rule]`, `[Host]`, `[URL Rewrite]`, `[Header Rewrite]`, `[Body Rewrite]`, `[Map Local]`, `[Panel]`, `[Port Forwarding]`, `[Script]`, `[SSID Setting]`, and `[Ruleset <name>]` — a mixed section remains editable in the UI: Surge remembers which file every line came from and writes each change back to that file. New entries added in the UI are stored in the main profile, and reordering an entry away from its original file's block moves it into the main profile as well.

The section becomes read-only in the UI when any referenced file is itself read-only (for example a managed profile URL), or when the section is of another type (such as `[Proxy]`).

{% hint style='danger' %}
In the `[Rule]` section, a `FINAL` rule immediately terminates rule matching. Rules included or defined after it are never evaluated, so check the position of `FINAL` in both the main profile and the included files.
{% endhint %}

#### Wildcard Named Sections {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}

For named `[Ruleset <name>]`, `[WireGuard <name>]`, and `[Tailscale <name>]` sections, a wildcard detached section can load all matching sections from another profile with a single `#!include`. The included profile can be a local file or a remote URL.

```
[Ruleset *]
#!include shared-rulesets.conf

[WireGuard *]
#!include shared-tunnels.conf

[Tailscale *]
#!include https://example.com/shared-tailscale.conf
```

For example, `[Ruleset *]` imports every `[Ruleset <name>]` section from the referenced profile while ignoring its unrelated sections. The same behavior applies to the `[WireGuard *]` and `[Tailscale *]` forms.

Additional notes:

- Sections loaded from a local file remain editable in the UI. Changes are written back to the file that defines the section, and deleting the item in the UI removes its section from that file. New items created in the UI are stored in the main profile.
- If a managed profile is referenced, the referenced sections cannot be edited locally, but other sections remain editable.
- Loading fails if two included files provide a section with the same name, or if an included section duplicates one already declared in the profile.
- One file may back wildcard and regular `#!include` statements at the same time; a single save updates all of them together.
- A filename suffix is not required. If the file is a complete profile, you can continue using `.conf`. If it is not a complete profile, use another suffix to avoid showing it in the profile list.

### Linked Profiles {{ book.VER | replace("%TEXT%", "Mac 6.0.0+") }}

`#!include` can also reference a remote managed profile (a URL) directly. This lets you build a local "overlay" profile that keeps following updates from the upstream config.

```
[Rule]
#!include https://example.com/managed.conf
```

When the referenced content is read-only, Surge will prompt to create a linked layer if you try to edit those sections. The local layer stores only your overrides, while the remote managed profile keeps receiving updates automatically.

## Modules

Detached profile sections split one profile into multiple files. [Modules](module.md) are different: they patch selected parts of a profile to enable a specific behavior, and can be turned on and off independently.

## Line Requirement

A line can be constrained to take effect only in specific environments, using the `#!REQUIREMENT` statement or the simplified notations `#!IOS-ONLY`, `#!MACOS-ONLY`, and `#!TVOS-ONLY`. See [Line Requirement](requirement.md).
