# Built-in Policies

Surge provides several built-in policies, the most important being `DIRECT` and `REJECT`. `DIRECT` sends the request directly to the host; `REJECT` rejects it. They can be used in rules and policy groups without any declaration.

#### DIRECT

Send the request to the host directly.

#### CELLULAR {{ book.VER | replace("%TEXT%", "iOS Only") }}

Prefer the cellular network over the Wi-Fi network. If the cellular network is unavailable, other interfaces are used instead.

#### CELLULAR-ONLY {{ book.VER | replace("%TEXT%", "iOS Only") }}

Use the cellular network only. The connection fails if the cellular network is not available.

#### HYBRID {{ book.VER | replace("%TEXT%", "iOS Only") }}

Try to set up connections with the Wi-Fi and cellular network simultaneously, then use the faster link. Only meaningful while the All Hybrid option is not on.

#### NO-HYBRID {{ book.VER | replace("%TEXT%", "iOS Only") }}

Never try to set up connections with the cellular network if Wi-Fi is available. Only meaningful while either the All Hybrid or Wi-Fi Assist option is enabled.

For `REJECT`, `REJECT-DROP`, `REJECT-NO-DROP`, and `REJECT-TINYGIF`, see the [REJECT Policy](reject.md) page.

## Alias

You can define an alias of a built-in policy in the `[Proxy]` section, using one of the type keywords `direct`, `reject`, `reject-drop`, `reject-no-drop`, or `reject-tinygif`:

```
[Proxy]
On = direct
Off = reject
```

`On` and `Off` can then be used as policy names in rules and policy groups.

An alias accepts the [common policy parameters](parameters.md), which makes it useful for egress control. For example, a direct alias bound to a specific network interface:

```
[Proxy]
Corp-VPN = direct, interface = utun0
WiFi = direct, interface = en2, allow-other-interface=true
```

{% hint style='info' %}

A `[Proxy]` line that redefines the name `DIRECT` is silently ignored. Redefining any other built-in policy name, such as `REJECT` or `CELLULAR`, is a configuration error.

{% endhint %}
