# Surge Dashboard

Surge Dashboard is a graphical interface for reviewing requests, inspecting the DNS cache, and managing devices. It is included with Surge Mac and can connect either to the local Surge instance or to a remote Surge instance.

## Local and Remote Connections

On macOS, the Dashboard connects to the local Surge instance directly, with no configuration required.

The Dashboard can also manage a remote Surge instance — another Surge Mac, or a Surge iOS device — when `external-controller-access` is configured on the remote instance:

```
[General]
external-controller-access = apassword@127.0.0.1:8888
```

For Surge iOS, the Dashboard can connect over Wi-Fi or over USB. Since inbound connections from cellular networks are always rejected, connect the device over USB to inspect traffic while it is using a cellular connection.

Surge Dashboard can also read [Logbook](logbook.md) content from remote Surge Mac and Surge iOS instances.

## Parameters

#### `external-controller-access`

This `[General]` option enables management from an external controller, such as Surge Dashboard or [Surge CLI](cli.md) with `--remote`.

The value is made up of three parts: password, listen address, and port number, in the form `password@address:port`. No part can be omitted.

On Surge iOS, the listen address controls which connections are accepted:

* `127.0.0.1`: only USB connections are allowed.
* `0.0.0.0`: connections from the local Wi-Fi network are also allowed.

Connections from cellular networks are always restricted for security reasons.

## Web Dashboard

Besides the native Dashboard, Surge also provides a web-based dashboard served by the HTTP API. Enable it with the `http-api-web-dashboard` option; see [HTTP API](http-api.md) and the [\[General\] section reference](../profile/general.md).
