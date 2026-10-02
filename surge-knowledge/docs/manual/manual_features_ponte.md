# Surge Ponte

Surge Ponte links your Surge devices into a device-to-device network, so one device can reach another remotely — for example, accessing your home network from outside. Devices signed in to the same iCloud account register themselves automatically; a device can also be shared with another iCloud account explicitly using a confirmation code.

Every Surge device can act as a Ponte client, but only Surge Mac can serve as the Ponte server (the access point for a home network). See [Platform Differences](../getting-started/platform-differences.md).

## How It Works

Ponte devices register through iCloud and can then reach each other:

- By hostname: each device is reachable as `<name>.sgponte`, where the name is the device name from the device's system settings. These names are handled by Surge itself; they are not public DNS domains.
- As a policy: a rule can send matching traffic through another device by using `DEVICE:<name>` as the policy.

Depending on network conditions, a Ponte connection can be established over several channel types: Direct Access, NAT Traversal, Proxy NAT Traversal, LAN Only, and IPv6. Surge selects the channel automatically.

Setup is performed with the guided wizard in the Surge app. Most Ponte state — device records, keys, and ports — is stored in iCloud and app data rather than in the profile, so there is usually nothing to configure by hand.

## The [Ponte] Section

The profile carries only the Ponte parameters that reference proxy policies, as `key = value` lines:

```
[Ponte]
client-proxy-name = Relay-Proxy
server-proxy-name = Proxy-A, Proxy-B
```

#### `client-proxy-name`: Optional, policy name

The relay proxy for the client: the proxy policy this device uses to reach other Ponte devices when a relay is needed.

#### `server-proxy-name`: Optional, comma-separated policy names

The proxies the Ponte server may use for proxy-assisted NAT traversal. The referenced proxy must support Full Cone UDP relay; the setup wizard verifies this. Surge keeps these references in sync automatically when the referenced policy is renamed or deleted.

## Related Features

- The [DEVICE-NAME rule](../rules/source-and-port.md) matches incoming requests by the client's device name. For Surge Ponte access, the device name is the device name in the client device's system settings.
- The Surge Dashboard and iOS Remote Controller can connect to a remote device through its `<name>.sgponte` hostname when remote controller access is enabled. See [Dashboard](../tools/dashboard.md).
