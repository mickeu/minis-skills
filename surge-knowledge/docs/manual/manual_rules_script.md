# Script Rule

The SCRIPT rule delegates the matching decision to a JavaScript script, for conditions beyond what the built-in rule types can express.

```
SCRIPT,ScriptName,DIRECT
```

The value is the name of a script defined in the [Script] section with `type=rule`:

```
[Script]
ssid-rule = type=rule,script-path=ssid-rule.js

[Rule]
SCRIPT,ssid-rule,DIRECT
```

The script receives the request details (hostname, ports, protocol, process path, User-Agent, URL, source address, listen port, DNS result) in `$request` and must call `$done({matched: true})` or `$done({matched: false})`. See [Script Type: rule](../scripting/rule.md) for the full parameter list and examples.

#### requires-resolve

By default, a SCRIPT rule does not trigger a DNS lookup, so `$request.dnsResult` may be empty for domain hostnames. Add the `requires-resolve` flag to perform the DNS lookup before the script runs:

```
SCRIPT,ssid-rule,DIRECT,requires-resolve
```

The script's result is cached for the rest of the evaluation of the same request, so referencing the same script from multiple rules does not run it repeatedly.

The SCRIPT rule does not support the `pre-matching` flag.
