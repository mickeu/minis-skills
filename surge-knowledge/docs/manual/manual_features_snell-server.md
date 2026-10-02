# Built-in Snell Server

Surge can accept incoming Snell proxy connections with the `[Snell Server]` section, letting other Surge devices use this device as a Snell server. Besides Surge Mac, the server is available on Surge iOS and Surge tvOS, which makes an always-on Apple TV a convenient home access point. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }}

On Surge iOS and tvOS, a listener on `0.0.0.0` is bound to the current Wi-Fi/Ethernet address and the loopback address, and follows network changes automatically.

```
[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
```

When `version` is omitted, the server uses Snell v1. Existing configurations continue to work unchanged.

### Parameters

#### interface

The local address the server listens on, e.g. `0.0.0.0`.

#### port

The TCP listening port.

#### psk

The pre-shared key. Clients must be configured with the same PSK.

#### version

Optional, 1 or 6, default: 1.

The Snell protocol version served. Only `1` and `6` are accepted.

#### mode

Optional, `default` | `unshaped` | `unsafe-raw`, default: `default`. Snell v6 only.

The transport mode. Use `default` for normal deployments. Clients must set the matching [`mode` parameter](../policies/snell.md) on their Snell policies.

### Snell v6 {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

Set `version=6` to enable the Snell v6 server:

```
[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
version = 6
mode = default
```

The built-in Snell v6 server supports reusable encrypted TCP transports and UDP tunneling. Its protocol profile is derived automatically from the PSK, so no traffic-shaping profile needs to be configured manually.

{% hint style='info' %}
Adding `version=6` is required to opt in. Existing `[Snell Server]` sections without a version continue to use Snell v1.
{% endhint %}

### Client Configuration

Configure an outbound Snell policy on the client with a matching PSK and version:

```
[Proxy]
My Snell Server = snell, server.example.com, 6160, psk=RANDOM_KEY_HERE, version=6
```

See the [Snell policy](../policies/snell.md) reference for all client-side parameters.

### Using a Module {{ book.VER | replace("%TEXT%", "iOS 5.23.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.10.0+") }}

The `[Snell Server]` section may also be provided by a [module](../profile/module.md). This is useful when one profile is shared by several devices and only some of them should run the server, for example a module enabled only for the Apple TV when deploying from Surge iOS. The module's section replaces the one in the profile as a whole.
