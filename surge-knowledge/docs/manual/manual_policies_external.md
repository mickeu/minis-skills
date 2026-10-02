# External Proxy Program {{ book.VER | replace("%TEXT%", "Mac Only") }}

Surge Mac supports the External Proxy Program policy, which allows Surge to work with other proxy software: Surge launches an external program and forwards requests to the local SOCKS5 port it listens on.

The following is an SSH example. The policy type keyword is `external`.

```
[Proxy]
external = external, exec = "/usr/bin/ssh", args = "11.22.33.44", args = "-D", args = "127.0.0.1:1080", local-port = 1080, addresses = 11.22.33.44
```

Surge iOS does not support external proxy programs. The `external` policy is treated as `REJECT` on iOS.

## Parameters

#### exec

Required. The path of the external program's executable.

#### local-port

Required. The SOCKS5 port that the external program listens on at 127.0.0.1. Surge forwards requests to this port.

#### args

Optional. A command-line argument passed to the external program. The parameter can be used repeatedly to append multiple arguments in order.

#### addresses

Optional. A proxy server IP address to be excluded from the VIF routes when Enhanced Mode is on. The parameter can be used repeatedly to append multiple addresses. Hostnames and domains are not supported.

#### udp-relay

Optional. Boolean. Default: false.

Relay UDP traffic through the external program's local SOCKS5 port. The external program must support SOCKS5 UDP relay.

## Lifecycle

Surge will do the following:

1. When the policy is used, Surge starts the external process with the `exec` and `args` parameters, then forwards the request to SOCKS5 `127.0.0.1:[local-port]`.
2. If the external process is terminated, Surge restarts it automatically when the policy is used.
3. Surge automatically excludes the addresses in the `addresses` parameter from the VIF routes when [Enhanced Mode](../features/enhanced-mode.md) is on. Use the proxy server IP address in this field. Hostnames and domains are not supported.
4. Surge always uses the `DIRECT` policy for requests from external processes. Children of external processes are handled the same way for plugin programs such as `obfs-local`.
5. Surge automatically shuts down all external processes when it exits, and automatically cleans up route table items when Enhanced Mode shuts down.

Some notes:

1. The behavior of items 3 and 4 overlaps. Prefer the `addresses` declaration to exclude VIF processing, which reduces processing overhead. Item 4 is an additional protection.
2. stdout and stderr of external processes are redirected to `/tmp/Surge-External-xxxxxx.log` for troubleshooting.
3. External processes may take a short time to start. If a connection refused error is encountered when forwarding to `127.0.0.1:[local-port]`, Surge automatically retries after 500 ms, up to 6 times per request.

## See Also

* [Common Policy Parameters](parameters.md) — shared parameters such as `interface`, `tfo`, and `test-url`.
* [UDP Relay](udp.md)
