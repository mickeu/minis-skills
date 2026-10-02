# REJECT Policy

To meet different needs, Surge has multiple built-in REJECT policies. In most cases, using `REJECT` directly is sufficient. If there are special requirements, consider the derivative policies.

#### REJECT

Reject the request. If the request is HTTP, an error page is returned. This behavior can be controlled by the `show-error-page-for-reject` option in the [\[General\] section](../profile/general.md).

#### REJECT-TINYGIF

Reject the request. If the request is HTTP, a 1px transparent GIF is returned, which is useful for ad blocking.

#### REJECT-DROP

Reject the request. Unlike REJECT, this policy silently discards the connection. Some applications have very aggressive retry logic and immediately retry after a connection failure, leading to a request storm. Using this policy can mitigate the issue.

#### REJECT-NO-DROP

If a large number of requests to a hostname trigger the `REJECT`/`REJECT-TINYGIF` policy within a short period of time (the threshold is 50 times within 30 seconds in the current version), Surge automatically upgrades the policy to `REJECT-DROP` to avoid wasting resources.

Use the `REJECT-NO-DROP` policy to avoid this behavior: it rejects the request and is never upgraded to `REJECT-DROP`.

## Pre-matching Reject {{ book.VER | replace("%TEXT%", "iOS 5.14.0+") }} {{ book.VER | replace("%TEXT%", "Mac 5.9.0+") }}

Due to the extensive range of properties that Surge's rule system can evaluate, rule determination can normally only occur after receiving the first TCP packet. This results in excessive unnecessary overhead when dealing with storm requests or ad-blocking needs.

The pre-matching feature quickly rejects requests with low overhead. For rules using a REJECT policy, enable it with the `pre-matching` tag:

```
[Rule]
DOMAIN,ad.com,REJECT,pre-matching
```

Rules marked with `pre-matching` take effect before the normal rule matching process, thus having the highest priority.

All rules marked with `pre-matching` are extracted for prioritized matching and executed during the DNS resolution and TCP SYN phases. If a DNS domain is matched, Surge returns No Record directly. If a TCP SYN is matched, Surge generates a TCP RST response immediately. In case of numerous requests, Surge escalates to packet loss. UDP is handled similarly.

Additionally, each rule only appears once in the recent request list every 5 minutes to avoid flooding.

The rule types that can be marked with `pre-matching`:

- Domain types: [DOMAIN, DOMAIN-SUFFIX, DOMAIN-KEYWORD, DOMAIN-SET, DOMAIN-WILDCARD](../rules/domain.md)
- IP types: [IP-CIDR, IP-CIDR6, GEOIP, IP-ASN](../rules/ip.md)
- Logical rules: [AND, OR, NOT](../rules/logical.md)
- Others: [SUBNET, CELLULAR-RADIO, CELLULAR-CARRIER](../rules/protocol-and-network.md), [DEST-PORT, SRC-PORT, SRC-IP](../rules/source-and-port.md)

[RULE-SET](../rules/ruleset.md) can also be used, but its content is subject to the above restrictions as well.

## Pre-matching Technical Details

For optimal user experience, rejections are made during the pre-matching phase. The derivative policies behave slightly differently.

#### For DNS queries

- If a REJECT policy is matched, Surge returns a No Record DNS response. If the frequency limit built into the REJECT policy is triggered, the DNS query is discarded without a response.

- If a REJECT-DROP policy is matched, the DNS query is discarded without a response.

- If a REJECT-NO-DROP policy is matched, it returns a special IP address 198.18.0.244; Surge generates TCP RST responses for all TCP connections accessing this address.

#### For TCP requests using IP

- If a REJECT policy is matched, Surge directly generates TCP RST responses; if the frequency limit built into the REJECT policy is triggered, it discards the corresponding TCP SYN handshake packet.

- If a REJECT-DROP policy is matched, Surge directly discards the TCP SYN handshake packet.

- If a REJECT-NO-DROP policy is matched, Surge directly generates TCP RST responses.

{% hint style='info' %}

Some software has aggressive retry logic that immediately retries after a request fails, causing abnormal CPU usage. Even for the REJECT-NO-DROP policy, when Surge generates a large number of TCP RST packets in a short period of time (the threshold is 100 times within 3 seconds in the current version), a protection mechanism pauses returning TCP RST and drops packets instead.

{% endhint %}

#### For UDP packets

Since UDP packets have no handshake overhead, there is no pre-matching phase; they are directly matched using the main rule set:

- If a REJECT policy is matched, an ICMP Administratively Prohibited response is generated. If the frequency limit built into the REJECT policy is triggered, packets are discarded.

- If a REJECT-DROP policy is matched, packets are directly discarded.

- If a REJECT-NO-DROP policy is matched, an ICMP Administratively Prohibited response is generated.
