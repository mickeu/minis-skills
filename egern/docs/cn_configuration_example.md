# 配置示例
您可以在 Profile.yaml 文件中配置 Egern 的参数。
下面是一个 Profile.yaml 文件的示例：
    ---  
    # 自动更新配置的内容。默认值是空  
    auto_update:  
      url: http://example.com/  
      interval: 86400  
    # 是否启用 IPv6。默认值是 false  
    ipv6: false  
    # HTTP 代理端口号。默认值是 3080  
    http_port: 3080  
    # SOCKS 代理端口号。默认值是 3090  
    socks_port: 3090  
    # 允许外部连接通过 Wi-Fi 访问设备上的代理。默认值是 false  
    allow_external_connections: false  
    # 仅虚拟网接口模式。默认值是 false  
    vif_only: false  
    # 全局阻止 QUIC 协议，强制使用 TCP 连接。默认值是 false  
    # 优先级：代理 > 策略组 > 全局。代理自身的 block_quic 优先级最高，  
    # 其次是策略组的 block_quic，最后是此全局设置。  
    # 若三者均未设置，则使用协议默认值（TCP 类协议默认阻止，UDP 类协议默认放行）。  
    block_quic: false  
    # 策略组选中节点变化时（手动切换、自动测速切换、故障转移、订阅更新后选中项回退），  
    # 关闭仍在使用旧节点的连接，使流量立即通过新节点重连。默认值是 false  
    close_connections_on_policy_change: false  
    # 绕过隧道代理的域名列表。默认值是空数组  
    bypass_tunnel_proxy:  
      - "*.local"  
      - "192.168.0.0/16"  
    # 使用真实 IP 的域名列表（不使用 Fake IP）。默认值是空数组  
    real_ip_domains:  
      - "*.lan"  
      - "*.push.apple.com"  
    # 隐藏 VPN 图标。默认值是 false  
    hide_vpn_icon: false  
    # 劫持 DNS 的地址列表。默认值是空数组  
    hijack_dns:  
      - '*'  
    # 指定自定义的 GeoIP 数据库 URL。默认值是空  
    geoip_db_url: null  
    # 指定自定义的 ASN 数据库 URL。默认值是空  
    asn_db_url: null  
    # 自定义的代理延迟测试 URL。默认值是空  
    proxy_latency_test_url: null  
    # 自定义的直连延迟测试 URL。默认值是空  
    direct_latency_test_url: null  
    # 兼容路由模式。默认值是 false  
    compat_route: false  
    # 包含所有网络流量。默认值是 false  
    include_all_networks: false  
    # 包含 APNs 流量（需 include_all_networks 启用）。默认值是 false  
    include_apns: false  
    # 包含蜂窝网络服务流量（需 include_all_networks 启用）。默认值是 false  
    include_cellular_services: false  
    # 包含本地网络流量（需 include_all_networks 启用）。默认值是 false  
    include_local_networks: false  
    # 虚拟接口包含的路由。默认值是空数组  
    vif_included_routes:  
      - 192.168.0.1/32  
    # 虚拟接口排除的路由。默认值是空数组  
    vif_excluded_routes:  
      - 192.168.0.1/32  
    dns:  
      bootstrap:  
        - system  # 使用系统默认的 DNS 配置作为引导  
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
    # 代理列表  
    proxies:  
      # Shadowsocks 协议  
      - shadowsocks:  
          name: MyShadowsocks  
          method: chacha20-ietf-poly1305  
          password: Password  
          server: 127.0.0.1  
          port: 443  
          tfo: false  
          udp_relay: false  
          # 当 server 为需要 DNS 解析的域名时，选用的 IP 版本策略。  
          # 可选值：dual_stack（默认）/ v4_only / v6_only / v4_prefer / v6_prefer  
          ip_version: dual_stack  
          obfs: http  
          obfs_host: www.bing.com  
          obfs_uri: "http://www.bing.com/"  
      # Trojan 协议  
      - trojan:  
          name: MyTrojan  
          server: 127.0.0.1  
          port: 443  
          sni: www.bing.com  
          password: Password  
          tfo: false  
          udp_relay: true  
      # Vless 协议  
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
      # Vmess 协议  
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
      # Hysteria2 协议  
      - hysteria2:  
          name: MyHysteria2  
          server: 127.0.0.1  
          port: 443  
          auth: your_password  
          sni: www.bing.com  
          obfs: salamander  
          obfs_password: cry_me_a_r1ver  
          skip_tls_verify: false  
      # TUIC 协议  
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
      # SOCKS5 协议  
      - socks5:  
          name: MySocks  
          server: 127.0.0.1  
          port: 443  
          username: Username  
          password: Password  
          tfo: false  
          udp_relay: true  
      # HTTP 协议  
      - http:  
          name: MyHttp  
          server: 127.0.0.1  
          port: 443  
          username: Username  
          password: Password  
          tfo: false  
      # WireGuard 协议  
      - wireguard:  
          name: MyWireGuard  
          server: engage.cloudflareclient.com  
          port: 2408  
          private_key: "base64_encoded_private_key"  
          peer_public_key: "base64_encoded_public_key"  
          local_ipv4: 172.16.0.2/32  
          reserved: [1, 2, 3]  
    # 策略组配置列表  
    policy_groups:  
      # 手动选择的策略组  
      - select:  
          name: Select  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          icon: globe  
      # 自动测试的策略组  
      - auto_test:  
          name: AutoTest  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          interval: 600  
          tolerance: 100  
          timeout: 5  
      # 故障转移策略组  
      - fallback:  
          name: Fallback  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
          interval: 600  
          timeout: 5  
      # 负载均衡策略组  
      - load_balance:  
          name: LoadBalance  
          policies:  
            - MyShadowsocks  
            - MyTrojan  
      # 外部资源策略组  
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
      # 条件策略组  
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
    # 代理规则列表  
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
    # URL 重写列表  
    url_rewrites:  
      - match: "(.*google)\\.cn"  
        location: $1.com  
        status_code: 307  
    # HTTP 头部重写列表  
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
    # HTTP 消息体重写列表  
    body_rewrites:  
      # 响应体正则替换  
      - response_regex:  
          match: "^https://example\\.com"  
          find: old_content  
          replace: new_content  
      # 请求体 jq 过滤器  
      - request_jq:  
          match: "^https://api\\.example\\.com/submit"  
          filter: '.data.version = "2.0"'  
    # 脚本配置列表  
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
    # Map Local 配置。将匹配的 URL 请求映射到本地自定义响应  
    map_locals:  
      - match: "^https://api\\.example\\.com/mock$"  
        status_code: 200  
        headers:  
          Content-Type: application/json  
        body: '{"code": 0, "message": "ok"}'  
    # MITM 配置。中间人解密，用于修改 HTTPS 流量（URL 重写、头部/消息体重写、脚本等）  
    mitm:  
      ca_p12: ""  
      ca_passphrase: "123456"  
      hostnames:  
        includes:  
          - "*.example.com"  
        excludes:  
          - "*.internal.example.com"  
    # HTTP 抓包配置列表  
    http_captures:  
      - "*.example.com"  
    # 小组件配置。在主屏幕和锁定屏幕上显示自定义内容，由通用脚本渲染  
    widgets:  
      - name: "Widget Script 1"  
        env:  
          REGION: "cn"  
    # 添加订阅时默认使用的外部策略组名称。默认值是空  
    default_subscription_group: Subscription  
    # 添加代理时自动加入的策略组名称。默认值是空  
    default_proxy_group: PROXY  
    # 模块配置列表  
    modules:  
      - name: "广告过滤"  
        url: "https://example.com/module.yaml"  
        update_interval: 86400  
        enabled: true  
      - url: "https://example.com/custom.yaml"  
        compat_arguments:  
          API_KEY: "your_api_key"