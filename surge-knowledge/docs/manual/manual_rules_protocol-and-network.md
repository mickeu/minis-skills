# Protocol and Network Rules

These rule types match on properties of the connection itself or the network environment, rather than the destination: the connection protocol, the form of the hostname, the current cellular network, and the current Wi-Fi or wired network. Use them to route traffic differently depending on how the request was made or where the device currently is.

```
PROTOCOL,STUN,REJECT
SUBNET,SSID:MyHome,DIRECT
FINAL,Proxy
```

## PROTOCOL

Rule matches if the protocol of the request matches. The accepted values are `HTTP`, `HTTPS`, `TCP`, `UDP`, `QUIC`, `STUN`, `MTProto`, `DOH`, `DOH3`, `DOQ`, `DOT`, and `DNS`.

```
PROTOCOL,HTTP,DIRECT
```

The comparison is case-sensitive; write the keywords exactly as listed above.

Two keywords act as umbrella matchers:

- `PROTOCOL,TCP` also matches HTTP, HTTPS, and MTProto connections, so a single rule can cover all TCP-based traffic.
- `PROTOCOL,UDP` also matches QUIC and STUN connections.

Use `MTProto` to match connections accepted by the built-in MTProto proxy server. {{ book.VER | replace("%TEXT%", "iOS 5.21.0+") }} {{ book.VER | replace("%TEXT%", "Mac 6.8.0+") }}

```
PROTOCOL,MTProto,Proxy
```

{% hint style='info' %}
1. Due to the existence of multiple draft versions of QUIC, not all QUIC traffic can be recognized by Surge.
2. STUN detection is available for filtering P2P traffic; `PROTOCOL,STUN` matches STUN packets specifically so they can be blocked or forwarded.
3. The keywords `DOH`, `DOH3`, `DOQ`, `DOT`, and `DNS` only match DNS requests sent by Surge itself (`DOT` matches DNS over TLS connections and `DNS` matches plain DNS over TCP connections configured with the `tcp://` prefix). By default these requests bypass the rule system and always use the DIRECT policy; set `encrypted-dns-follow-outbound-mode=true` in the [General] section to route them through rules. See [Encrypted DNS](../dns/encrypted-dns.md).
{% endhint %}

The PROTOCOL rule does not support the `pre-matching` flag.

## HOSTNAME-TYPE {{ book.VER | replace("%TEXT%", "Mac 5.7.3+") }}

Rule matches the form of the hostname in a request. The supported keywords are:

- `IPv4`: hostname is an IPv4 literal.
- `IPv6`: hostname is an IPv6 literal.
- `DOMAIN`: hostname contains dots and is a regular domain name.
- `SIMPLE`: hostname without a dot, such as `localhost`.

```
HOSTNAME-TYPE,IPv6,REJECT
HOSTNAME-TYPE,SIMPLE,DIRECT
```

The keywords are case-sensitive: `IPv4` and `IPv6` must be written with this exact capitalization. An unrecognized keyword invalidates the rule.

## CELLULAR-RADIO {{ book.VER | replace("%TEXT%", "iOS Only") }}

Rule matches if the cellular radio technology of the current network matches. The rule only matches when the device is not on Wi-Fi. The possible values are `GPRS`, `Edge`, `WCDMA`, `HSDPA`, `HSUPA`, `CDMA1x`, `CDMAEVDORev0`, `CDMAEVDORevA`, `CDMAEVDORevB`, `eHRPD`, `HRPD`, `LTE`, `NRNSA`, and `NR`. The comparison is case-sensitive.

```
CELLULAR-RADIO,LTE,DIRECT
```

## CELLULAR-CARRIER {{ book.VER | replace("%TEXT%", "iOS Only") }}

Rule matches if the mobile carrier of the current cellular network matches. The value is the carrier's MCC (mobile country code) followed by the MNC (mobile network code) as a single string of digits. The rule only matches when the device is not on Wi-Fi.

```
CELLULAR-CARRIER,310260,Proxy
```

To match the same condition inside a subnet expression (for example in a [Subnet Policy Group](../policy-groups/subnet.md) or an [SSID Setting](../features/subnet-settings.md)), use the `MCCMNC:` prefix described below.

## SUBNET

Rule matches if the current network matches the subnet expression.

```
SUBNET,TYPE:WIRED,DIRECT
SUBNET,SSID:MyHome,Proxy
```

Only the network of the outgoing interface is considered: the rule describes the network Surge is currently on, not the destination of the request.

### Subnet Expressions

Subnet expressions are also used outside the [Rule] section: the [Subnet Policy Group](../policy-groups/subnet.md) and the [SSID Setting section](../features/subnet-settings.md) accept the same syntax. This section is the canonical reference.

A subnet expression takes one of these forms:

#### `SSID:<value>`

Matches the Wi-Fi network name (SSID). Wildcard characters `*` and `?` are allowed. The comparison is case-sensitive.

```
SUBNET,SSID:Office-*,DIRECT
```

#### `BSSID:<value>`

Matches the Wi-Fi access point MAC address (BSSID). Wildcard characters are allowed. The comparison is case-insensitive.

```
SUBNET,BSSID:aa:bb:cc:*,DIRECT
```

#### `ROUTER:<ip>`

Matches the default gateway IP address of the current network exactly.

```
SUBNET,ROUTER:192.168.1.1,DIRECT
```

#### `TYPE:WIFI` / `TYPE:WIRED` / `TYPE:CELLULAR`

Matches all Wi-Fi networks, all wired networks, or all cellular networks respectively. The type keyword is case-insensitive.

```
SUBNET,TYPE:CELLULAR,DIRECT
```

#### `MCCMNC:<digits>`

Matches the mobile carrier of the current cellular network by MCC+MNC. The expression only matches when the device is not on Wi-Fi.

```
SUBNET,MCCMNC:310260,Proxy
```

#### Bare value (legacy)

If no prefix is given, the value is compared for compatibility with old profiles: a value containing `*` or `?` is wildcard-matched against the SSID; otherwise it matches the SSID exactly, the BSSID case-insensitively, or the router IP exactly.

Prefer the prefixed forms in new profiles.
