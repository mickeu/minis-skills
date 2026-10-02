# Module

A module is a set of settings that overrides the current profile. You may use modules to:

- Tweak settings in a non-editable profile, such as a managed profile or enterprise profile.
- Change part of the settings with one tap. For example, you may use a module to enable MITM for all hostnames and adjust the filter temporarily.
- Use a module written by others to accomplish a particular task. For example, a coworker may share a module that rewrites API requests to a test server.
- Customize a shared profile for different devices or scenarios. The enabled state of modules is not synced to other devices.

## Basic Concepts

A module is like a patch to the current profile. The settings of modules have a higher priority than the settings of the profile.

There are three types of modules:

- Internal Modules: Provided by Surge itself.
- Local Modules: `.sgmodule` files placed in the profile directory.
- Installed Modules: Modules installed with a URL.

Compared with [detached profile sections](format.md#detached-profile-section), which split one profile into multiple files, modules patch selected parts of a profile to enable a specific behavior. However:

- Modules cannot adjust the content of `[Proxy]` and `[Proxy Group]` sections. Rule lines may only be inserted at the top of the rule list and are restricted to internal policies.
- A module cannot adjust the CA certificate of MITM.
- The settings of a module override the main profile, so they cannot be adjusted via the UI.

## Write a Module

The syntax of a module is the same as the profile. You are allowed to override these sections:

* General, MITM
  * Override: `key = value`
  * Append to the original value: `key = %APPEND% value`
  * Insert in the front of the original value: `key = %INSERT% value`

	You can manipulate the `hostname` and `skip-server-cert-verify` fields only in a [MITM](../http/mitm.md) section.

	> The legacy `[Replica]` section used by the HTTP capture feature was removed in Surge Mac 5.4.0, so modules no longer need to patch it.

* `[WireGuard *]` sections

	[WireGuard](../policies/wireguard.md) policies live in sections whose names start with `WireGuard `. Modules can override or append keys inside those sections just like the main profile.

* `[MTProto]` {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }} and `[Snell Server]` {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }} sections

	A module can enable the built-in [MTProto proxy server](../features/mtproto.md) or [Snell server](../features/snell-server.md). The section must be complete: it replaces the corresponding section of the profile as a whole instead of patching individual keys.

* `[Ruleset *]` sections

	A module may add lines to an [inline rule set](../rules/ruleset.md). If the profile, or another enabled module, already defines a rule set with the same name, the lines are merged into it; otherwise a new rule set is created. Since the order inside a rule set has no effect, a module cannot remove or reorder existing lines. {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }}

* Rule, Script, URL Rewrite, Header Rewrite, Host

	New lines are inserted at the top of the original content.

	The rules in a module can only use internal policies: DIRECT, REJECT, and REJECT-TINYGIF.

* Metadata

	You may add metadata in a module file:

	```
	#!name=Name Here
	#!desc=Description Here
	```

	You may limit a module to a specified platform. (Optional)

	```
	#!system=mac
	```

## Examples

```
#!name=MitM All Hostnames
#!desc=Perform MitM on all hostnames with port 443, except those to Apple and other common sites which can't be inspected. You still need to configure a CA certificate and enable the main switch of MitM.

[MITM]
hostname = -*.apple.com, -*.icloud.com, -*.mzstatic.com, -*.crashlytics.com, -*.facebook.com, -*.instagram.com, *
```

```
#!name=Game Console SNAT
#!desc=Let Surge handle SNAT conversation properly for PlayStation, Xbox, and Nintendo Switch. Only useful if Surge Mac acts the router for these devices.
#!system=mac
[General]
always-real-ip = %APPEND% *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

## Parameter Tables {{ book.VER | replace("%TEXT%", "Mac 5.5.0+") }}

Use the `#!arguments` metadata to declare parameters that the user can customize when enabling the module. Separate multiple parameters with commas. Use a colon after a parameter name to provide its default value; the default value is optional.

```
#!arguments=hostname:example.com,enable_mitm:true
#!arguments-desc=Configure the hostname and whether MITM is enabled.
```

`#!arguments-desc` is optional. Its value is displayed as a general description for the parameter table; it does not define a separate description for each parameter.

Reference a parameter by wrapping its name in three braces. Surge replaces every declared placeholder with the configured value, or its default value when the user has not provided one, before applying the module. Parameter names and placeholders are case-sensitive.

{% raw %}
```
[MITM]
hostname = {{{hostname}}}

[Script]
example = type=generic, script-path=script/example.js, argument="{{{enable_mitm}}}"
```
{% endraw %}

Values entered by the user are saved with the module instance and shown again when its parameters are edited.

{% hint style='info' %}
The query-string form (`hostname=example.com&enable_mitm=true`) and `%PARAMETER%` placeholders are not supported for module parameter tables. `%APPEND%` and `%INSERT%` are separate module operators and are unrelated to parameter substitution.
{% endhint %}

Use only letters, numbers, and underscores in parameter names, and remove unused placeholders when deleting an argument.

## Requirements {{ book.VER | replace("%TEXT%", "iOS 5.10.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.6.0+") }}

A module may add a `#!requirement=` description, allowing for more complex usage condition restrictions. For example, if the module uses the newly added Body Rewrite feature, it needs to restrict the version of the Surge core.

```
#!requirement=CORE_VERSION>=20
```

It also supports logical expressions, such as `CORE_VERSION>=20 && (SYSTEM = 'iOS' || SYSTEM = 'tvOS')`.

The variables that can be used for judgment are as follows:

- CORE_VERSION: Number, such as `20`
- SYSTEM: String, such as `macOS`, `iOS`, `tvOS`
- SYSTEM_VERSION: String, such as `Version 17.4.1 (Build 21E236)`
- DEVICE_MODEL: String, such as `Mac15,8`
- LANGUAGE: String, such as `zh-Hans`

These are the same variables used by [line requirements](requirement.md); see that page for Core Version values.
