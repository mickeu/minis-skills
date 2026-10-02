# 规则
Egern 支持多种类型的规则，可以用于控制网络流量的代理行为，同时可以用于阻止某些流量。规则按照配置顺序依次匹配，匹配成功后不再继续匹配后续规则。
## 支持的规则​
### 域名规则​
类型| 名称| 说明  
---|---|---  
domain| 域名完全匹配| 完全匹配域名  
domain_suffix| 域名后缀匹配| 匹配域名后缀，自动处理子域名边界（如 `google.com` 匹配 `www.google.com` 但不匹配 `fakegoogle.com`）  
domain_keyword| 域名关键词匹配| 匹配含有指定关键词的域名  
domain_regex| 域名正则匹配| 通过正则表达式匹配域名  
domain_wildcard| 域名通配符匹配| 使用 glob 模式匹配域名，大小写不敏感（如 `*.google.*`）  
### IP 规则​
类型| 名称| 说明  
---|---|---  
geoip| GeoIP 匹配| 根据 ISO 3166-1 alpha-2 国家/地区代码匹配 IP 地址（如 `CN`、`US`）  
ip_cidr| IPv4 范围匹配| 匹配指定 IPv4 CIDR 范围  
ip_cidr6| IPv6 范围匹配| 匹配指定 IPv6 CIDR 范围  
asn| ASN 匹配| 匹配 ASN 编号或组织名称（如 `13335`、`AS13335`、`Telegram Messenger Inc`）  
### 其他规则​
类型| 名称| 说明  
---|---|---  
url_regex| URL 正则匹配| 通过正则表达式匹配完整 URL（仅 HTTP/HTTPS 流量）  
user_agent| User-Agent 匹配| 使用 glob 模式匹配 User-Agent 头，大小写不敏感（仅 HTTP/HTTPS 流量）  
dest_port| 目标端口匹配| 匹配目标端口，支持单端口、范围和混合格式（如 `80,443,8000-9000`）  
protocol| 协议匹配| 匹配协议类型：`tcp`、`udp`、`http`、`https`、`quic`、`stun`  
rule_set| 规则集合| 引用本地或远程规则集文件，将多条规则打包复用  
### 网络环境规则​
类型| 名称| 说明  
---|---|---  
ssid| Wi-Fi SSID 匹配| 使用 glob 模式匹配当前 Wi-Fi 名称，大小写不敏感  
bssid| Wi-Fi BSSID 匹配| 使用 glob 模式匹配当前 Wi-Fi 接入点的 MAC 地址  
cellular| 蜂窝网络匹配| 使用 glob 模式匹配蜂窝网络类型（如 `NR`、`LTE`、`WCDMA`）  
### 逻辑规则​
类型| 名称| 说明  
---|---|---  
and| 逻辑与| 所有子条件都满足时匹配  
or| 逻辑或| 任一子条件满足时匹配  
not| 逻辑非| 子条件不满足时匹配  
### 默认规则​
类型| 名称| 说明  
---|---|---  
default| 默认规则| 兜底规则，匹配所有未被其他规则匹配的流量  
## 规则字段​
  * **match** (string), 必填
匹配值。
  * **policy** (string), 必填
策略名称。决定了匹配的流量应该如何处理。`DIRECT` 表示直连，`REJECT` 表示拒绝连接，也可以使用代理服务器或策略组的名称。
  * **name** (string), 可选
规则名称，用于日志和调试。
  * **no_resolve** (bool), 可选
仅适用于 IP 类规则（geoip、ip_cidr、ip_cidr6、asn）。设为 `true` 时仅匹配已解析的 IP 地址，不会触发 DNS 解析。
  * **disabled** (bool), 可选
是否禁用此规则。
## 配置示例​
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
## 规则集合​
规则集合可以是本地文件或远程文件。规则集合允许你在多个配置文件中复用或共享规则。规则集中的所有条件使用逻辑或关系，即任一条件匹配则整个规则集匹配。
### 规则集字段​
类型| 名称  
---|---  
domain_set| 域名完全匹配集合  
domain_keyword_set| 域名关键词匹配集合  
domain_suffix_set| 域名后缀匹配集合  
domain_regex_set| 域名正则匹配集合  
domain_wildcard_set| 域名通配符匹配集合  
geoip_set| GeoIP 国家/地区代码集合  
ip_cidr_set| IPv4 CIDR 集合  
ip_cidr6_set| IPv6 CIDR 集合  
url_regex_set| URL 正则匹配集合  
asn_set| ASN 编号或组织名称集合  
user_agent_set| User-Agent glob 模式集合  
ssid_set| Wi-Fi SSID glob 模式集合  
bssid_set| Wi-Fi BSSID glob 模式集合  
cellular_set| 蜂窝网络类型 glob 模式集合  
protocol_set| 协议匹配集合  
dest_port_set| 目标端口匹配集合  
and_set| 逻辑与规则集合  
or_set| 逻辑或规则集合  
not_set| 逻辑非规则集合  
  * **no_resolve:** (可选) 是否跳过 DNS 解析，影响所有 IP 相关规则。
### 规则集合示例​
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