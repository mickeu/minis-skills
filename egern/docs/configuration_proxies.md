# Proxies
Configuration for proxies, supporting the following protocols: `Shadowsocks`, `Snell`, `Trojan`, `AnyTLS`, `Hysteria2`, `TUIC`, `SOCKS5`, `SOCKS5 over TLS`, `SSH`, `HTTP`, `HTTPS`, `Vmess`, `Vless`, `WireGuard`. All optional fields of type `bool` default to `false`.
## Shadowsocks​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **method** (string), Required
Encryption method.
AEAD-2022: `2022-blake3-aes-128-gcm`, `2022-blake3-aes-256-gcm`, `2022-blake3-chacha20-poly1305`
AEAD: `chacha20-poly1305`, `aes-256-gcm`, `aes-128-gcm`
Stream: `none`, `table`, `rc4`, `rc4-md5`, `aes-128-cfb`, `aes-192-cfb`, `aes-256-cfb`, `aes-128-ctr`, `aes-192-ctr`, `aes-256-ctr`, `bf-cfb`, `camellia-128-cfb`, `camellia-192-cfb`, `camellia-256-cfb`, `cast5-cfb`, `des-cfb`, `idea-cfb`, `rc2-cfb`, `seed-cfb`, `salsa20`, `chacha20`, `chacha20-ietf`
  * **password** (string), Required
The password. Shadowsocks 2022 uses a Base64-encoded key.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **udp_port** (integer), Optional
Dedicated UDP port. Used when the server listens on different ports for TCP and UDP.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **obfs** (string), Optional
Obfuscation method. Possible values: `http`, `tls`.
  * **obfs_host** (string), Optional
The hostname used for obfuscation.
  * **obfs_uri** (string), Optional
The URI path used for obfuscation.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Shadowsocks defaults to `false` (allow QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    shadowsocks:  
      name: "my-ss"  
      method: "aes-256-gcm"  
      password: "mypassword"  
      server: "1.2.3.4"  
      port: 8388  
      tfo: true  
      udp_relay: false  
      obfs: "http"  
      obfs_host: "example.com"  
      obfs_uri: "/path"  
## Snell​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **psk** (string), Required
The pre-shared key.
  * **version** (integer), Optional
Protocol version, one of `1`/`2`/`3`/`4`/`5`. Defaults to `1`; v5 is implemented as v4.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay. Only available on v3/v4.
  * **reuse** (bool), Optional
Whether to enable connection reuse. Only effective on v4; v2 always reuses.
  * **obfs** (string), Optional
Obfuscation method. Possible values: `http`, `tls`.
  * **obfs_host** (string), Optional
The hostname used for obfuscation. Defaults to `bing.com`.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Snell defaults to `false` (allow QUIC).
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    snell:  
      name: "my-snell"  
      server: "1.2.3.4"  
      port: 8388  
      psk: "mypassword"  
      version: 4  
      udp_relay: true  
      obfs: "http"  
      obfs_host: "example.com"  
## Trojan​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **sni** (string), Optional
The Server Name Indication (SNI) used for TLS. Defaults to the value of the `server` field.
  * **password** (string), Required
The password for the Trojan protocol.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **reality** (object), Optional
REALITY configuration (mutually exclusive with plain TLS). When set, REALITY replaces plain TLS as the security layer: it borrows a real site's certificate to complete the handshake and carries its own authentication, so `skip_tls_verify` and `fingerprint_sha256` are ignored.
    * **public_key** (string), Required
The server Reality public key (Base64 URL-safe encoded).
    * **short_id** (string), Optional
The short ID (hexadecimal string).
  * **websocket** (object), Optional
WebSocket configuration for Trojan:
    * **path** (string), Required
The WebSocket path.
    * **host** (string), Optional
The Host header for the WebSocket.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Trojan defaults to `true` (block QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    trojan:  
      name: "my-trojan"  
      server: "trojan.example.com"  
      port: 443  
      sni: "trojan.example.com"  
      password: "trojanpass"  
      tfo: true  
      udp_relay: true  
      skip_tls_verify: true  
      websocket:  
        path: "/ws"  
        host: "trojan.example.com"  
## AnyTLS​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **password** (string), Required
The authentication password.
  * **sni** (string), Optional
The Server Name Indication (SNI) used for TLS. Defaults to the value of the `server` field.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay (UDP over TCP).
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification. **Unlike other TLS protocols, AnyTLS defaults to skipping verification when this field is unset** , preserving its historical behavior (AnyTLS commonly uses a self-signed certificate, with authentication handled by the password and TLS serving only as camouflage). Set to `false` to enable standard CA-chain verification. Ignored when `fingerprint_sha256` is set.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **reality** (object), Optional
REALITY configuration (mutually exclusive with plain TLS). When set, REALITY replaces plain TLS as the security layer: it borrows a real site's certificate to complete the handshake and carries its own authentication, so `skip_tls_verify` and `fingerprint_sha256` are ignored.
    * **public_key** (string), Required
The server Reality public key (Base64 URL-safe encoded).
    * **short_id** (string), Optional
The short ID (hexadecimal string).
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, AnyTLS defaults to `true` (block QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    anytls:  
      name: "my-anytls"  
      server: "anytls.example.com"  
      port: 443  
      password: "mypassword"  
      sni: "anytls.example.com"  
      udp_relay: true  
## Hysteria2​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **auth** (string), Required
The authentication password or token for Hysteria2.
  * **sni** (string), Optional
The Server Name Indication (SNI) used for TLS.
  * **obfs** (string), Optional
Obfuscation method. Possible values: `salamander`.
  * **obfs_password** (string), Optional
The obfuscation password.
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **port_hopping** (string), Optional
Port hopping configuration string. Supports a single port `8080`, a port range `20000-30000`, or a mixed format `1234,5000-6000,8080`. The client will randomly select a port from the specified set for connection.
  * **port_hopping_interval** (integer), Optional
Port hopping interval (in seconds). After a connection is established, the client switches to a new random port every specified number of seconds.
  * **bandwidth** (integer), Optional
Upload bandwidth (Mbps). When configured, the Brutal congestion control algorithm will be enabled to send data at the target bandwidth. It is recommended to set this to 80%-90% of the actual available bandwidth.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Hysteria2 defaults to `false` (allow QUIC).
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    hysteria2:  
      name: "my-hysteria2"  
      server: "hysteria.example.com"  
      port: 443  
      auth: "my_auth_token"  
      sni: "hysteria.example.com"  
      obfs: "salamander"  
      obfs_password: "myobfspass"  
      skip_tls_verify: true  
      port_hopping: "20000-30000"  
      port_hopping_interval: 30  
      bandwidth: 100  
## TUIC​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **uuid** (string), Required
The UUID.
  * **password** (string), Required
The password.
  * **udp_relay_mode** (string), Optional
UDP relay mode. `native` (native UDP relay, default), `quic` (transmit UDP datagrams over QUIC streams).
  * **alpn** (array of string), Optional
The ALPN list for TLS. Common values: `h3`.
  * **sni** (string), Optional
The Server Name Indication (SNI) used for TLS.
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **port_hopping** (string), Optional
Port hopping configuration string. Supports a single port `8080`, a port range `20000-30000`, or a mixed format `1234,5000-6000,8080`.
  * **port_hopping_interval** (integer), Optional
Port hopping interval (in seconds).
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, TUIC defaults to `false` (allow QUIC).
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    tuic:  
      name: "my-tuic"  
      server: "tuic.example.com"  
      port: 443  
      uuid: "22222222-2222-2222-2222-222222222222"  
      password: "tuicpass"  
      udp_relay_mode: "native"  
      alpn:  
      - "h3"  
      sni: "tuic.example.com"  
      skip_tls_verify: true  
      port_hopping: "443,445,447"  
      port_hopping_interval: 30  
## SOCKS5​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **username** (string), Optional
The username.
  * **password** (string), Optional
The password.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, SOCKS5 defaults to `false` (allow QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    socks5:  
      name: "my-socks5"  
      server: "1.2.3.4"  
      port: 1080  
      username: "user"  
      password: "pass"  
      tfo: false  
      udp_relay: true  
## SOCKS5 over TLS​
SOCKS5 wrapped in a TLS layer: the client first completes a TLS handshake with the server, then performs the SOCKS5 handshake and relays traffic inside the encrypted channel. This is the TLS variant of `socks5`, just as `https` is to `http`.
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **username** (string), Optional
The username.
  * **password** (string), Optional
The password.
  * **sni** (string), Optional
TLS SNI (Server Name Indication). Defaults to the value of the `server` field.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **reality** (object), Optional
REALITY configuration (mutually exclusive with plain TLS). When set, REALITY replaces plain TLS as the security layer: it borrows a real site's certificate to complete the handshake and carries its own authentication, so `skip_tls_verify` and `fingerprint_sha256` are ignored.
    * **public_key** (string), Required
The server Reality public key (Base64 URL-safe encoded).
    * **short_id** (string), Optional
The short ID (hexadecimal string).
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, SOCKS5 over TLS defaults to `false` (allow QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    socks5_tls:  
      name: "my-socks5-tls"  
      server: "1.2.3.4"  
      port: 443  
      username: "user"  
      password: "pass"  
      sni: "example.com"  
      udp_relay: true  
## SSH​
Tunnels TCP connections through an SSH server's `direct-tcpip` channel (similar to `ssh -L`), multiplexing all connections over a single SSH session. SSH has no datagram channel, so UDP is not relayed.
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port (SSH default is 22).
  * **username** (string), Required
The SSH login username.
  * **password** (string), Optional
The login password. Provide a password and/or a private key; when both are present, the private key is tried first.
  * **private_key** (string), Optional
Inline private key contents in PEM/OpenSSH format (the key itself, not a file path).
  * **host_keys** (array of string), Optional
Accepted server host keys. Each entry is a full `known_hosts` public key line, i.e. `<type> <base64-key>` (e.g. `ssh-ed25519 AAAAC3Nza...`), optionally with a trailing comment. When set, the server's host key is pinned and verified, and the connection is refused on mismatch. When left empty, host key verification is skipped.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, SSH defaults to `true` (block QUIC), since SSH cannot relay UDP.
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    ssh:  
      name: "my-ssh"  
      server: "ssh.example.com"  
      port: 22  
      username: "root"  
      # Authenticate with an inline private key (PEM/OpenSSH format)...  
      private_key: |  
        -----BEGIN OPENSSH PRIVATE KEY-----  
        ...  
        -----END OPENSSH PRIVATE KEY-----  
      # ...and/or with a password  
      password: "mypassword"  
      # Optional: pin the server's host key (a full known_hosts public key line)  
      host_keys:  
        - "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl"  
## HTTP​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **username** (string), Optional
The username for the HTTP proxy.
  * **password** (string), Optional
The password for the HTTP proxy.
  * **headers** (object), Optional
Custom HTTP request headers.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    http:  
      name: "my-http"  
      server: "5.6.7.8"  
      port: 8080  
      username: "user"  
      password: "pass"  
      tfo: false  
## HTTPS​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **username** (string), Optional
The username for the HTTPS proxy.
  * **password** (string), Optional
The password for the HTTPS proxy.
  * **headers** (object), Optional
Custom HTTP request headers.
  * **sni** (string), Optional
TLS SNI (Server Name Indication). Defaults to the value of the `server` field.
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **skip_tls_verify** (bool), Optional
Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional
SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and CA-chain verification is bypassed. Mutually exclusive with `skip_tls_verify`, which is ignored when this field is set.
  * **reality** (object), Optional
REALITY configuration (mutually exclusive with plain TLS). When set, REALITY replaces plain TLS as the security layer: it borrows a real site's certificate to complete the handshake and carries its own authentication, so `skip_tls_verify` and `fingerprint_sha256` are ignored.
    * **public_key** (string), Required
The server Reality public key (Base64 URL-safe encoded).
    * **short_id** (string), Optional
The short ID (hexadecimal string).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    https:  
      name: "my-https"  
      server: "proxy.example.com"  
      port: 443  
      username: "user"  
      password: "pass"  
      sni: "proxy.example.com"  
## Vmess​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **user_id** (string), Required
The Vmess user ID (UUID).
  * **security** (string), Required
Encryption method. `auto` (automatic selection, default), `aes-128-gcm`, `chacha20-poly1305`, `none`, `zero`
  * **legacy** (bool), Optional
Whether to use the legacy Vmess protocol format (not recommended).
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **transport** (object), Optional
Transport configuration. See Vmess Transport for details.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Vmess defaults to `true` (block QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    vmess:  
      name: "my-vmess"  
      server: "vmess.example.com"  
      port: 443  
      user_id: "00000000-0000-0000-0000-000000000000"  
      security: "auto"  
      legacy: false  
      tfo: true  
      udp_relay: true  
      transport:  
        ws:  
          path: "/myws"  
          headers:  
            Host: "vmess.example.com"  
## Vless​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **user_id** (string), Required
The Vless user ID (UUID).
  * **tfo** (bool), Optional
Whether to enable TCP Fast Open.
  * **udp_relay** (bool), Optional
Whether to enable UDP relay.
  * **flow** (string), Optional
Flow control mode. Supports `xtls-rprx-vision`.
  * **transport** (object), Optional
Transport configuration. See Vmess Transport for details.
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, Vless defaults to `true` (block QUIC).
  * **shadow_tls** (object), Optional
ShadowTLS transport configuration. See ShadowTLS for details.
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    vless:  
      name: "my-vless"  
      server: "vless.example.com"  
      port: 443  
      user_id: "11111111-1111-1111-1111-111111111111"  
      flow: xtls-rprx-vision  
      tfo: true  
      udp_relay: false  
      transport:  
        tls:  
          sni: www.microsoft.com  
          reality:  
            public_key: "base64_encoded_public_key"  
            short_id: "abc123"  
## WireGuard​
  * **name** (string), Required
The proxy name, which must be globally unique.
  * **server** (string), Required
The server address, which can be an IP or domain name.
  * **port** (integer), Required
The server port.
  * **private_key** (string), Required
The local private key (Base64-encoded, 32-byte X25519 key).
  * **peer_public_key** (string), Required
The peer public key (Base64-encoded, 32-byte X25519 public key).
  * **preshared_key** (string), Optional
The preshared key (Base64-encoded).
  * **reserved** (array of integer), Optional
The reserved field (3-byte array). Used for client identification in services such as Cloudflare WARP. Format: `[byte1, byte2, byte3]`.
  * **local_ipv4** (string), Optional
The local IPv4 address. Supports CIDR notation (e.g., `172.16.0.2/32`) or a plain IP. At least one of `local_ipv4` or `local_ipv6` must be set.
  * **local_ipv6** (string), Optional
The local IPv6 address. Supports CIDR notation (e.g., `fd01:5ca1:ab1e::2/128`) or a plain IP.
  * **dns_servers** (array of string), Optional
The list of DNS servers used internally by WireGuard.
  * **mtu** (integer), Optional
MTU (Maximum Transmission Unit).
  * **keepalive** (integer), Optional
Keepalive interval (in seconds).
  * **block_quic** (bool), Optional
Whether to block the QUIC protocol. When set to `true`, connections using this proxy will not use QUIC/HTTP3. This setting takes the highest priority, overriding both policy group and global `block_quic`. When not set, the policy group and global settings are used in order; if none are set, WireGuard defaults to `false` (allow QUIC).
  * **prev_hop** (string), Optional
The name of the preceding proxy, used to build a proxy chain. Traffic path: local machine -> preceding proxy -> current proxy -> destination.
  * **ip_version** (string), Optional
IP version strategy applied when `server` is a domain that requires DNS resolution; it has no effect on an IP-literal `server`. One of `dual_stack` (default), `v4_only`, `v6_only`, `v4_prefer`, `v6_prefer`.
### Configuration Example​
    wireguard:  
      name: "WARP"  
      server: engage.cloudflareclient.com  
      port: 2408  
      private_key: "base64_encoded_private_key"  
      peer_public_key: "base64_encoded_public_key"  
      local_ipv4: 172.16.0.2/32  
      local_ipv6: "fd01:5ca1:ab1e::2/128"  
      reserved: [1, 2, 3]  
      mtu: 1280  
      keepalive: 25  
## Vmess Transport​
Used in the `transport` field of Vmess and Vless proxy types. The available options and example configurations are as follows:
### HTTP 1​
Disguises proxy traffic as HTTP/1.1 requests.
    transport:  
      http1:  
        method: "GET"  
        path: "/"  
        headers:  
          User-Agent: "curl/7.77.0"  
          Accept: "*/*"  
### HTTP 2​
Transmits proxy traffic over HTTP/2 multiplexing.
    transport:  
      http2:  
        method: "GET"  
        path: "/"  
        headers:  
          User-Agent: "curl/7.77.0"  
          Accept: "*/*"  
        sni: "example.com"  
        skip_tls_verify: true  
        fingerprint_sha256: "aa:bb:cc:..."  
The `fingerprint_sha256` field accepts a SHA-256 fingerprint of the server's leaf certificate (hex, case-insensitive; `:` or `-` separators allowed). When set, the leaf certificate's DER SHA-256 is pinned and `skip_tls_verify` is ignored.
### TLS​
Transmits traffic directly over TLS encryption. Supports Reality configuration.
    transport:  
      tls:  
        sni: "my-sni.example.com"  
        skip_tls_verify: true  
        fingerprint_sha256: "aa:bb:cc:..."  
The `fingerprint_sha256` field behaves the same as in HTTP 2.
#### Reality Configuration​
    transport:  
      tls:  
        sni: www.microsoft.com  
        reality:  
          public_key: "base64_encoded_public_key"  
          short_id: "abc123"  
  * **public_key** (string), Required - The server Reality public key (Base64 URL-safe encoded).
  * **short_id** (string), Optional - The short ID (hexadecimal string).
### WSS​
Encapsulates proxy traffic in WebSocket and transmits it over TLS encryption.
    transport:  
      wss:  
        path: "/websocket"  
        headers:  
          Host: "myhost.example.com"  
        sni: "my-sni.example.com"  
        skip_tls_verify: false  
        fingerprint_sha256: "aa:bb:cc:..."  
The `fingerprint_sha256` field behaves the same as in HTTP 2.
### WS​
Encapsulates proxy traffic in WebSocket (without TLS encryption).
    transport:  
      ws:  
        path: "/ws"  
        headers:  
          Host: "myhost.example.com"  
### gRPC​
Encapsulates proxy traffic in a gRPC bidirectional stream, carried over TLS with ALPN `h2`. The TLS layer is always applied, so gRPC traffic is always encrypted.
    transport:  
      grpc:  
        service_name: "GunService"  
        sni: "example.com"  
        skip_tls_verify: false  
        fingerprint_sha256: "aa:bb:cc:..."  
  * **service_name** (string), Optional - The gRPC service name (e.g. `GunService`); it must match the server. A value starting with `/` switches to custom-path mode (e.g. `/your/path/Tun`).
  * **user_agent** (string), Optional - Custom User-Agent. Defaults to a Chrome User-Agent for traffic camouflage.
  * **sni** (string), Optional - TLS SNI. Defaults to the server address.
  * **skip_tls_verify** (bool), Optional - Whether to skip TLS certificate verification.
  * **fingerprint_sha256** (string), Optional - Behaves the same as in HTTP 2.
gRPC can also run over REALITY instead of plain TLS by adding a `reality` block (same fields as the TLS transport):
    transport:  
      grpc:  
        service_name: "grpc"  
        sni: www.microsoft.com  
        reality:  
          public_key: "base64_encoded_public_key"  
          short_id: "abc123"  
## ShadowTLS​
ShadowTLS transport configuration, available for use in Shadowsocks, Trojan, AnyTLS, SOCKS5, SOCKS5 over TLS, SSH, HTTP, HTTPS, Vmess, and Vless proxy types.
  * **password** (string), Required
The ShadowTLS authentication password.
  * **sni** (string), Optional
TLS SNI (used for disguise, e.g., `www.microsoft.com`).
### Configuration Example​
    shadowsocks:  
      name: "SS with ShadowTLS"  
      server: example.com  
      port: 443  
      method: aes-256-gcm  
      password: ss_password  
      shadow_tls:  
        password: shadow_tls_password  
        sni: www.microsoft.com