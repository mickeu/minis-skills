# DHCP {{ book.VER | replace("%TEXT%", "Mac Only") }}

Surge can provide DHCP service for devices in the local network when [Gateway Mode](gateway.md) and the related network features are enabled.

Statically assigned IP addresses are automatically excluded from the dynamic address pool, preventing the same address from being allocated to another client. {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

## DHCP Section {{ book.VER | replace("%TEXT%", "Mac 6.5.0+") }}

The `[DHCP]` section can customize DHCP lease behavior. These parameters are only intended for users with special requirements; the default settings are sufficient in most cases.

```
[DHCP]
max-lease-time = 86400
default-lease-time = 43200
min-lease-time = 600
one-lease-per-client = true
ping-check = true
```

### Parameters

#### max-lease-time

Optional, seconds

The maximum lease time.

#### default-lease-time

Optional, seconds

The default lease time.

#### min-lease-time

Optional, seconds

The minimum lease time.

#### one-lease-per-client

Optional, Boolean

When enabled, Surge keeps only one active lease for each client.

#### ping-check

Optional, Boolean

When enabled, Surge checks whether an address is already in use before assigning it.
