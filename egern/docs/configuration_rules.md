# Rules
Egern supports multiple types of rules that can be used to control the proxy behavior of network traffic and to block certain traffic. Rules are matched in the order they appear in the configuration; once a rule matches, subsequent rules are no longer evaluated.
## Supported Rules​
### Domain Rules​
Type| Name| Description  
---|---|---  
domain| Exact Domain Match| Matches the domain exactly  
domain_suffix| Domain Suffix Match| Matches domains by suffix, automatically handling subdomain boundaries (e.g., `google.com` matches `www.google.com` but not `fakegoogle.com`)  
domain_keyword| Domain Keyword Match| Matches domains containing the specified keyword  
domain_regex| Domain Regex Match| Matches domains using regular expressions  
domain_wildcard| Domain Wildcard Match| Matches domains using glob patterns, case-insensitive (e.g., `*.google.*`)  
### IP Rules​
Type| Name| Description  
---|---|---  
geoip| GeoIP Match| Matches IP addresses based on ISO 3166-1 alpha-2 country/region codes (e.g., `CN`, `US`)  
ip_cidr| IPv4 Range Match| Matches the specified IPv4 CIDR range  
ip_cidr6| IPv6 Range Match| Matches the specified IPv6 CIDR range  
asn| ASN Match| Matches ASN numbers or organization names (e.g., `13335`, `AS13335`, `Telegram Messenger Inc`)  
### Other Rules​
Type| Name| Description  
---|---|---  
url_regex| URL Regex Match| Matches the full URL using regular expressions (HTTP/HTTPS traffic only)  
user_agent| User-Agent Match| Matches the User-Agent header using glob patterns, case-insensitive (HTTP/HTTPS traffic only)  
dest_port| Destination Port Match| Matches the destination port; supports single ports, ranges, and mixed formats (e.g., `80,443,8000-9000`)  
protocol| Protocol Match| Matches the protocol type: `tcp`, `udp`, `http`, `https`, `quic`, `stun`  
rule_set| Rule Set| References a local or remote rule set file, allowing multiple rules to be bundled for reuse  
### Network Environment Rules​
Type| Name| Description  
---|---|---  
ssid| Wi-Fi SSID Match| Matches the current Wi-Fi name using glob patterns, case-insensitive  
bssid| Wi-Fi BSSID Match| Matches the MAC address of the current Wi-Fi access point using glob patterns  
cellular| Cellular Network Match| Matches the cellular network type using glob patterns (e.g., `NR`, `LTE`, `WCDMA`)  
### Logical Rules​
Type| Name| Description  
---|---|---  
and| Logical AND| Matches when all sub-conditions are satisfied  
or| Logical OR| Matches when any sub-condition is satisfied  
not| Logical NOT| Matches when the sub-condition is not satisfied  
### Default Rule​
Type| Name| Description  
---|---|---  
default| Default Rule| A fallback rule that matches all traffic not matched by any other rule  
## Rule Fields​
  * **match** (string), required
The value to match.
  * **policy** (string), required
The policy name. Determines how matched traffic should be handled. `DIRECT` means direct connection, `REJECT` means the connection is refused. You can also use the name of a proxy server or policy group.
  * **name** (string), optional
The rule name, used for logging and debugging.
  * **no_resolve** (bool), optional
Applicable only to IP-based rules (geoip, ip_cidr, ip_cidr6, asn). When set to `true`, the rule only matches already-resolved IP addresses and will not trigger DNS resolution.
  * **disabled** (bool), optional
Whether to disable this rule.
## Configuration Example​
    rules:  
      - domain:  
          match: www.google.com  
          policy: Proxy  
      - domain_keyword:  
          match: google  
          policy: Proxy  
      - domain_suffix:  
          match: google.com  
          policy: Proxy  
      - domain_regex:  
          match: "^ads?\\."  
          policy: REJECT  
      - domain_wildcard:  
          match: "*.google.*"  
          policy: Proxy  
      - geoip:  
          match: CN  
          policy: DIRECT  
          no_resolve: true  
      - ip_cidr:  
          match: 192.168.0.0/16  
          policy: DIRECT  
      - ip_cidr6:  
          match: "2001:db8::/32"  
          policy: REJECT  
      - asn:  
          match: "AS13335"  
          policy: Proxy  
      - url_regex:  
          match: "^https://.*\\.google\\.com/"  
          policy: Proxy  
      - user_agent:  
          match: "*Chrome*"  
          policy: Proxy  
      - dest_port:  
          match: "80,443,8000-9000"  
          policy: Proxy  
      - protocol:  
          match: udp  
          policy: DIRECT  
      - ssid:  
          match: "Home*"  
          policy: DIRECT  
      - rule_set:  
          match: "https://example.com/rules.yaml"  
          policy: Proxy  
          update_interval: 86400  
      - and:  
          match:  
            - domain_suffix:  
                match: "example.com"  
            - dest_port:  
                match: "443"  
          policy: Proxy  
      - or:  
          match:  
            - domain_keyword:  
                match: "google"  
            - domain_keyword:  
                match: "youtube"  
          policy: Proxy  
      - not:  
          match:  
            geoip:  
              match: CN  
          policy: Proxy  
      - default:  
          policy: DIRECT  
## Rule Sets​
Rule sets can be local or remote files. They allow you to reuse or share rules across multiple configuration files. All conditions within a rule set use a logical OR relationship, meaning the entire rule set matches if any single condition matches.
### Rule Set Fields​
Type| Name  
---|---  
domain_set| Exact Domain Match Set  
domain_keyword_set| Domain Keyword Match Set  
domain_suffix_set| Domain Suffix Match Set  
domain_regex_set| Domain Regex Match Set  
domain_wildcard_set| Domain Wildcard Match Set  
geoip_set| GeoIP Country/Region Code Set  
ip_cidr_set| IPv4 CIDR Set  
ip_cidr6_set| IPv6 CIDR Set  
url_regex_set| URL Regex Match Set  
asn_set| ASN Number or Organization Name Set  
user_agent_set| User-Agent Glob Pattern Set  
ssid_set| Wi-Fi SSID Glob Pattern Set  
bssid_set| Wi-Fi BSSID Glob Pattern Set  
cellular_set| Cellular Network Type Glob Pattern Set  
protocol_set| Protocol Match Set  
dest_port_set| Destination Port Match Set  
and_set| Logical AND Rule Set  
or_set| Logical OR Rule Set  
not_set| Logical NOT Rule Set  
  * **no_resolve:** (optional) Whether to skip DNS resolution; affects all IP-related rules.
### Rule Set Example​
    no_resolve: true  
    domain_set:  
      - www.google.com  
      - www.youtube.com  
    domain_keyword_set:  
      - google  
      - youtube  
    domain_suffix_set:  
      - google.com  
      - youtube.com  
    domain_regex_set:  
      - "google|gstatic|ytimg|youtube|ggpht"  
    domain_wildcard_set:  
      - "*.google.*"  
    geoip_set:  
      - US  
      - JP  
    ip_cidr_set:  
      - 192.168.0.0/16  
    ip_cidr6_set:  
      - "2001:db8::/32"  
    url_regex_set:  
      - "^https://www\\.google\\.com/"  
    asn_set:  
      - "AS15169"  
    user_agent_set:  
      - "*Chrome*"  
    dest_port_set:  
      - "80,443"  
    protocol_set:  
      - udp