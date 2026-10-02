# Line Requirement {{ book.VER | replace("%TEXT%", "iOS 5.11.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.7.0+") }}

You can set constraints to make a certain line of configuration effective only when specific conditions are met. This is mainly useful for sharing one profile across devices, platforms, and Surge versions.

```
Group = url-test, policyA, policyB #!REQUIREMENT CORE_VERSION<22
```

For items that support an enabled/disabled state, lines that do not meet the conditions are treated as disabled. Other unmatched lines are treated as comments.

## Start-of-Line and End-of-Line Forms

A `#!REQUIREMENT` expression can be placed at the beginning of a line or appended to the end of a line:

```
#!REQUIREMENT CORE_VERSION>=22 Group = smart, policyA, policyB
Group = url-test, policyA, policyB //!REQUIREMENT CORE_VERSION<22
```

{% hint style='tip' %}

Since versions earlier than Surge iOS 5.11.0 and Surge Mac 5.7.0 do not support this expression, both forms are provided so you can support older clients. In the example above, an older version treats the first line as a normal comment and the end-of-line requirement on the second line as a regular comment, so only the second line takes effect. A newer version evaluates both expressions and uses the Smart group instead.

{% endhint %}

## REQUIREMENT Expression

Variables available for judgment: `CORE_VERSION`, `SYSTEM`, `SYSTEM_VERSION`, `DEVICE_MODEL`, `LANGUAGE`, `DEVICE_NAME` {{ book.VER | replace("%TEXT%", "iOS 5.22.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.9.0+") }}.

`DEVICE_NAME` is the user-assigned device name, as shown in Settings → General → About → Name on iOS, or the computer name in System Settings on macOS.

Available operators: `=`, `==`, `>=`, `=>`, `<=`, `=<`, `>`, `<`, `!=`, `<>`, `AND`, `&&`, `OR`, `||`, `NOT`, `!`, `BEGINSWITH`, `CONTAINS`, `ENDSWITH`, `LIKE`, `MATCHES`.

A typical example of variable values:

```
CORE_VERSION: 22
SYSTEM: iOS
SYSTEM_VERSION: System Version 17.4.1 (Build 21E236)
DEVICE_MODEL: iPhone16,1
LANGUAGE: en-US
DEVICE_NAME: Tim's iPhone
```

Strings in expressions should be wrapped in `'`, such as `#!REQUIREMENT SYSTEM=='macOS'`.

{% hint style='tip' %}

When an expression contains spaces, wrap the whole expression in `"`.

`#!REQUIREMENT "CORE_VERSION>=22 AND SYSTEM=='iOS'" Group = smart, policyA, policyB`

{% endhint %}

### Core Version

Core Version can be used to determine whether a feature is available.

Starting with Surge Mac 6.8.0 and Surge iOS 5.21.0, Core Version is derived from the corresponding Surge Mac version instead of being maintained separately. The value is encoded as `major * 1000000 + minor * 1000 + patch`. For example, Surge Mac 6.8.0 and Surge iOS 5.21.0 use Core Version `6008000`. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Earlier releases used independently assigned Core Version values:

- 22: Surge Mac 5.7.0, Surge iOS 5.11.0, Smart Group
- 20: Surge Mac 5.6.0, Surge iOS 5.10.0, Body Rewrite, Inline Map Local

## Simplified Notation {{ book.VER | replace("%TEXT%", "iOS 5.14.3+") }} {{ book.VER | replace("%TEXT%", "Mac 5.10.0+") }}

Three simplified notations are provided for convenience: `#!IOS-ONLY`, `#!MACOS-ONLY`, `#!TVOS-ONLY`.

```
DOMAIN,reject.com,REJECT #!MACOS-ONLY
```

## Usage in Managed Profiles

{% hint style='tip' %}

Requirement expressions are lost when a profile is modified in the UI, so this feature is mainly used in [managed profiles](managed-profile.md) and enterprise profiles.

{% endhint %}
