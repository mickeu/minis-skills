# Port Forwarding {{ book.VER | replace("%TEXT%", "iOS 5.14.3+") }} {{ book.VER | replace("%TEXT%", "Mac 5.10.0+") }}

Surge can listen on a specific local port and forward TCP requests from that port to a specific host. This feature works independently, even when Surge request handling (system proxy or enhanced mode) is not enabled.

```
[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
```

Each line takes the form:

```
<listen-address:port> <target-host:port> policy=<policy-name>
```

#### policy

Optional, policy name

The policy used for the forwarded connections. If it is not specified, standard rule matching determines the policy.

## Use Cases

This feature is commonly used in development and debugging scenarios, such as connecting to a server like MariaDB through an SSH proxy: Surge listens on a local port and forwards the connection to the database host via the configured policy.
