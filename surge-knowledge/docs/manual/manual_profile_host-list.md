# Host List Parameter Type

In Surge, many parameters use the Host List type to accommodate various complex needs, such as `force-http-engine-hosts` and `always-raw-tcp-hosts` in the [\[General\] section](general.md), the `hostname` parameter of [\[MITM\]](../http/mitm.md), and more.

A Host List parameter is a list separated by `,` and follows these rules:

* Use prefix `-` to exclude a hostname.
* Wildcard characters `*` and `?` are supported.
* Items in the list are matched in order. Once a match succeeds, matching stops. Therefore, items at the front have higher priority. When using the `-` prefix, write excluded hostnames at the front.
* If a port number is not provided, Surge automatically appends the standard port number for that parameter. For example, for the `force-http-engine-hosts` parameter, a bare hostname is only effective for port 80. For the MITM feature, it is only effective for port 443.
* Use suffix `:port` to match other ports.
* Use suffix `:0` to match all ports.
* Use `<ip-address>` to match all hostnames using an IPv4/IPv6 address directly instead of a domain.
* Use `<ipv4-address>` to match all hostnames using an IPv4 address directly instead of a domain.
* Use `<ipv6-address>` to match all hostnames using an IPv6 address directly instead of a domain.
* Use `<simple-hostname>` to match all hostnames without a dot.

Taking the `force-http-engine-hosts` parameter as an example:

* `-*.apple.com`: Excludes all requests sent to *.apple.com on port 80.
* `www.google.com`: Uses forced HTTP processing for www.google.com on port 80.
* `www.google.com:8080`: Uses forced HTTP processing for www.google.com on port 8080.
* `www.google.com:0`: Uses forced HTTP processing for www.google.com on all ports.
* `*:0`: Uses forced HTTP processing for all hostnames on all ports.
* `-<ip-address>`: Excludes all requests using an IPv4/IPv6 address directly.

## Example

When configuring the hostname list for [MITM](../http/mitm.md), if you want to decrypt all HTTPS connections but exclude well-known hostnames that cannot be decrypted due to certificate pinning, you can write it like this:

```
[MITM]
hostname = -*icloud*, -*.mzstatic.com, -*.facebook.com, -*.instagram.com, -*.twitter.com, -*dropbox*, -*apple*, -*.amazonaws.com, -<ip-address>, *
```
