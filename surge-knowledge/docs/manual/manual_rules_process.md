# Process Rules

You may assign a policy to requests from a specific process. Process rules are available on Surge Mac only; Surge iOS ignores these rules.

```
[Rule]
PROCESS-NAME,Telegram,Proxy
```

#### PROCESS-NAME {{ book.VER | replace("%TEXT%", "Mac Only") }}

Matches the executable of the process that originated the request. The rule expression supports three matching modes, selected by the shape of the value:

1. **Filename Mode**

    If the expression does not start with `/`, it matches only the executable file name, regardless of its path.

    Wildcards `*` and `?` are supported. For example: `PROCESS-NAME,Google*`

2. **Full Path Mode**

    If the expression starts with `/` (and does not end with `/`), it matches the executable's full absolute path.

    Wildcards `*` and `?` are supported in this mode as well. For example: `PROCESS-NAME,/usr/bin/ssh` or `PROCESS-NAME,/Applications/*.app/Contents/MacOS/*`

3. **App Bundle Mode** {{ book.VER | replace("%TEXT%", "Mac 6.0.0+") }}

    If the expression starts with `/` and also ends with `/`, the executable path is matched by prefix.

    This mode is particularly useful for application bundles that contain multiple executables. For example: `PROCESS-NAME,/Applications/ChatGPT.app/`

Matching is case-sensitive in all modes.

{% hint style='info' %}
Process rules do not support the `pre-matching` parameter, since the originating process is not known at the DNS-query stage.
{% endhint %}
