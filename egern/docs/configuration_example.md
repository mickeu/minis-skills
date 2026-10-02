# Configuration Example
You can configure Egern's parameters in the `Profile.yaml` file.
Here is an example of a `Profile.yaml` file:
    ---  
    # Content of automatic update configuration. Default value is empty  
    auto_update:  
      url: http://example.com/  
      interval: 86400  
    # Whether to enable IPv6. Default value is false  
    ipv6: false  
    # HTTP proxy port number. Default value is 3080  
    http_port: 3080  
    # SOCKS proxy port number. Default value is 3090  
    socks_port: 3090  
    # Allow external connections to access the proxy on the device through Wi-Fi. Default value is false  
    allow_external_connections: false  
    # Virtual interface only mode. Default value is false  
    vif_only: false  
    # Globally block the QUIC protocol, forcing TCP connections. Default value is false  
    # Priority: proxy > policy group > global. The proxy's own block_quic takes  
    # the highest priority, followed by the policy group's, then this global setting.  
    # If none are set, the protocol default is used (TCP-based protocols block by default,  
    # UDP-based protocols allow by default).  
    block_quic: false  
    # Close connections that are still using the old node when a policy group's  
    # selected node changes (manual switch, automatic latency-test switch, failover,  
    # or selection fallback after a subscription update), so traffic immediately  
    # reconnects through the new node. Default value is false  
    close_connections_on_policy_change: false  
    # List of domains that bypass the tunnel proxy. Default value is an empty array  
    bypass_tunnel_proxy:  
      - "*.local"  
      - "192.168.0.0/16"  
    # List of domains that use real IP (not Fake IP). Default value is an empty array  
    real_ip_domains:  
      - "*.lan"  
      - "*.push.apple.com"  
    # Hide VPN icon. Default value is false  
    hide_vpn_icon: false  
    # List of addresses for DNS hijacking. Default value is an empty array  
    hijack_dns:  
      - '*'  
    # Specify a custom GeoIP database URL. Default value is empty  
    geoip_db_url: null  
    # Specify a custom ASN database URL. Default value is empty  
    asn_db_url: null  
    # Custom proxy latency test URL. Default value is empty  
    proxy_latency_test_url: null  
    # Custom direct latency test URL. Default value is empty  
    direct_latency_test_url: null  
    # Compatible routing mode. Default value is false  
    compat_route: false  
    # Include all network traffic. Default value is false  
    include_all_networks: false  
    # Include APNs traffic (requires include_all_networks to be enabled). Default value is false  
    include_apns: false  
    # Include cellular network service traffic (requires include_all_networks to be enabled). Default value is false  
    include_cellular_services: false  
    # Include local network traffic (requires include_all_networks to be enabled). Default value is false  
    include_local_networks: false  
    # Routes included in the virtual interface. Default value is an empty array  
    vif_included_routes:  
      - 192.168.0.1/32  
    # Routes excluded from the virtual interface. Default value is an empty array  
    vif_excluded_routes:  
      - 192.168.0.1/32  
    dns:  
      bootstrap:  
        - system  # Use the system's default DNS configuration as bootstrap  
      upstreams:  
        google:  
          - https://8.8.8.8/dns-query  
          - https://8.8.4.4/dns-query  
      forward:  
        - domain_suffix:  
            match: "cn"  
            value: bootstrap  
        - wildcard:  
            match: '*.cn'  
            value: bootstrap  
        - proxy_rule_set:  
            match: https://github.com/ACL4SSR/ACL4SSR/raw/master/Clash/ChinaDomain.list  
            value: bootstrap  
        - regex:  
            match: ^ad\..*|^ads\..*  
            value: reject  
        - wildcard:  
            match: '*'  
            value: google  
      hosts:  
        example.com: www.example.com  
        localhost: 127.0.0.1  
        "*.local": 192.168.1.1  
      block_ips:  
        - 1.2.3.4  
        - 4.3.2.1/32  
      public_ip_lookup_url: https://ifconfig.me/ip  
    # Proxy list  
    proxies:  
      # Shadowsocks protocol  
      - shadowsocks:  
          name: MyShadowsocks  
          method: chacha20-ietf-poly1305  
          password: Password  
          server: 127.0.0.1  
          port: 443  
          tfo: false  
          udp_relay: false  
          # IP version strategy when the server is a domain that needs DNS resolution.  
          # One of: dual_stack (default) / v4_only / v6_only / v4_prefer / v6_prefer  
          ip_version: dual_stack  
          obfs: http  
          obfs_host: www.bing.com  
          obfs_uri: "http://www.bing.com/"  
      # Trojan protocol  
      - trojan:  
          name: MyTrojan  
          server: 127.0.0.1  
          port: 443  
          sni: www.bing.com  
          password: Password  
          tfo: false  
          udp_relay: true  
      # Vless protocol  
      - vless:  
          name: MyVless  
          server: 127.0.0.1  
          port: 443  
          user_id: 27848739-7e62-4138-9fd3-098a63964b6b  
          tfo: false  
          udp_relay: true  
          transport:  
            wss:  
              path: "/ws"  
              sni: www.bing.com  
      # Vmess protocol  
      - vmess:  
          name: MyVmess  
          server: 127.0.0.1  
          port: 443  
          user_id: 27848739-7e62-4138-9fd3-098a63964b6b  
          security: auto  
          legacy: false  
          tfo: false  
          udp_relay: true  
          transport:  
            wss:  
              path: "/ws"  
              sni: www.bing.com  
      # Hysteria2 protocol  
      - hysteria2:  
          name: MyHysteria2  
          server: 127.0.0.1  
          port: 443  
          auth: your_password  
          sni: www.bing.com  
          obfs: salamander  
          obfs_password: cry_me_a_r1ver  
          skip_tls_verify: false  
      # TUIC protocol  
      - tuic:  
          name: MyTuic  
          server: 127.0.0.1  
          port: 443  
          uuid: 27848739-7e62-4138-9fd3-098a63964b6b  
          password: Password  
          udp_relay_mode: native  
          alpn:  
            - h3  
          sni: www.bing.com  
      # SOCKS5 protocol  
      - socks5:  
          name: MySocks  
          server: 127.0.0.1  
          port: 443  
          username: Username  
          password: Password  
          tfo: false  
          udp_relay: true  
      # HTTP protocol  
      - http:  
          name: MyHttp  
          server: 127.0.0.1  
          port: 443  
          username: Username  
          password: Password  
          tfo: false  
      # WireGuard protocol  
      - wireguard:  
          name: MyWireGuard  
          server: engage.cloudflareclient.com  
          port: 2408  
          private_key: "base64_encoded_private_key"  
          peer_public_key: "base64_encoded_public_key"  
          local_ipv4: 172.16.0.2/32  
          reserved: [1, 2, 3]  
    # Policy group configuration list  
    policy_groups:  
      # Manually selected policy group  
      - select:  
          name: Select  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          icon: globe  
      # Auto test policy group  
      - auto_test:  
          name: AutoTest  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          interval: 600  
          tolerance: 100  
          timeout: 5  
      # Fallback policy group  
      - fallback:  
          name: Fallback  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          interval: 600  
          timeout: 5  
      # Load balance policy group  
      - load_balance:  
          name: LoadBalance  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
      # External resource policy group  
      - external:  
          name: MyExternal  
          type: select  
          urls:  
            - "https://example.com/proxies.yaml"  
          filter: ".*"  
          interval: 600  
          tolerance: 100  
          timeout: 5  
          update_interval: 86400  
      # Conditional policy group  
      - conditional:  
          name: NetworkSwitch  
          rules:  
            - ssid:  
                match: "Home-*"  
                policy: DIRECT  
            - cellular:  
                match: "LTE"  
                policy: AutoTest  
          default_policy: Select  
    # Proxy rule list  
    rules:  
      - domain:  
          match: example.com  
          policy: REJECT  
      - domain_keyword:  
          match: example  
          policy: DIRECT  
      - domain_suffix:  
          match: google.com  
          policy: Select  
      - domain_regex:  
          match: "^ads?\\."  
          policy: REJECT  
      - domain_wildcard:  
          match: "*.google.*"  
          policy: Select  
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
      - url_regex:  
          match: "^https://.*\\.example\\.com/"  
          policy: DIRECT  
      - asn:  
          match: "AS13335"  
          policy: Select  
      - dest_port:  
          match: "80,443"  
          policy: Select  
      - protocol:  
          match: udp  
          policy: DIRECT  
      - rule_set:  
          match: "https://example.com/rules.yaml"  
          policy: Select  
          update_interval: 86400  
      - default:  
          policy: Select  
    # URL rewrite list  
    url_rewrites:  
      - match: "(.*google)\\.cn"  
        location: $1.com  
        status_code: 307  
    # HTTP header rewrite list  
    header_rewrites:  
      - add:  
          match: "^https://example\\.com"  
          name: X-Custom-Header  
          value: custom-value  
          type: request  
      - replace:  
          match: "^https://example\\.com"  
          name: Cache-Control  
          value: no-cache  
          type: response  
      - delete:  
          match: "^https://example\\.com"  
          name: X-Tracking-Id  
          type: request  
    # HTTP body rewrite list  
    body_rewrites:  
      # Response body regex replacement  
      - response_regex:  
          match: "^https://example\\.com"  
          find: old_content  
          replace: new_content  
      # Request body jq filter  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.version = "2.0"'  
    # Scripting configuration list  
    scriptings:  
      - http_request:  
          name: HTTP Script 1  
          match: "^https://example\\.com"  
          script_url: "https://example.com/scripts/request.js"  
          update_interval: 86400  
          max_size: 131072  
          timeout: 30  
          body_required: false  
      - http_response:  
          name: HTTP Script 2  
          match: "^https://example\\.com"  
          script_url: "https://example.com/scripts/response.js"  
          update_interval: 86400  
          max_size: 131072  
          timeout: 30  
          body_required: false  
      - schedule:  
          name: Scheduled Script 1  
          cron: "0 8 * * *"  
          script_url: "https://example.com/scripts/task.js"  
          update_interval: 86400  
          timeout: 30  
      - generic:  
          name: Widget Script 1  
          script_url: "https://example.com/scripts/widget.js"  
          env:  
            API_KEY: "your_api_key"  
      - network:  
          name: Network Script 1  
          script_url: "https://example.com/scripts/network.js"  
    # Map Local configuration. Maps matching URL requests to local custom responses  
    map_locals:  
      - match: "^https://api\\.example\\.com/mock$"  
        status_code: 200  
        headers:  
          Content-Type: application/json  
        body: '{"code": 0, "message": "ok"}'  
    # MITM configuration. Man-in-the-middle decryption for modifying HTTPS traffic (URL rewrites, header/body rewrites, scripts, etc.)  
    mitm:  
      ca_p12: ""  
      ca_passphrase: "123456"  
      hostnames:  
        includes:  
          - "*.example.com"  
        excludes:  
          - "*.internal.example.com"  
    # HTTP capture configuration list  
    http_captures:  
      - "*.example.com"  
    # Widget configuration. Display custom content on Home Screen and Lock Screen, rendered by generic scripts  
    widgets:  
      - name: "Widget Script 1"  
        env:  
          REGION: "cn"  
    # Default external policy group for adding subscriptions. Default is empty  
    default_subscription_group: Subscription  
    # Policy group to automatically add proxies to. Default is empty  
    default_proxy_group: PROXY  
    # Module configuration list  
    modules:  
      - name: "Ad Filtering"  
        url: "https://example.com/module.yaml"  
        update_interval: 86400  
        enabled: true  
      - url: "https://example.com/custom.yaml"  
        compat_arguments:  
          API_KEY: "your_api_key"