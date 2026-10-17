# IP Rewrite / reflect 与本机开发服务回环

## 能力与版本边界

来源：[Surge TestFlight 公告 415](https://t.me/SurgeTestFlightFeed/415)。以下模块与双向反射曾于 2026-10-05 在 Surge iOS `5.102.0 / build 3859 / Core 6010000` 实测；这是已知实测版本，不是最低支持版本，也不代表当前实例状态。使用前核实当前版本及对应官方说明，不推断旧版本同样支持。

`[IP Rewrite]` 在进入 Surge VIF 的 IP 包层面执行，先于普通 Rule 和 Policy。`reflect` 交换源/目标 IP，将包送回设备，不是创建代理出站连接或 TCP Listener。因此这条路径不应再按 `LAN → DIRECT`、`interface=lo0` 或旧端口转发方案排障。不要把旧实验中未验证的 DIRECT/接口猜测固化成结论。

## 最小独立模块

仅当用户需要本机开发服务通道且接受 VIF 配置影响时使用：

```ini
#!name=Local Device Loopback
#!desc=Reflect 10.7.0.1 back to this device for on-device developer tools.

[General]
ipv6-vif = disabled
tun-included-routes = %INSERT% 10.7.0.1/32

[IP Rewrite]
10.7.0.1 = reflect
```

- `/32` 将目标地址流量纳入 VIF；`%INSERT%` 保留已有 included routes，不整表覆盖。
- `ipv6-vif = disabled` 是部分开发工具仅识别无 IPv6 地址 utun 的兼容措施，不是全设备关闭 IPv6，也不是所有 reflect 任务必需的通用设置。启用前说明影响，按目标工具需要选用并验证相关网络行为。
- 用独立模块隔离变更；落盘、API 启用和复核见 [HTTP API 模块流程](http-api.md#本地模块安装与启用)。不恢复旧端口转发实验，不改用户原 LAN 规则。
- 配置变化可能触发重载/VIF 更新；如需日志，在变更稳定后再设 verbose，诊断期间不要 reload。

这是开发工具访问本机设备服务的网络通道，不替代 Pairing File、签名材料、受信任会话或安装工具。`minis-sign` 的 MITM + Map Local + itms-services 是不同路径；不要用 reflect 替换其正常 Ad Hoc OTA 流程。

## 分层验证

1. API `enabled` 只证明模块状态，不证明网络成功。
2. 向目标服务发最小只读请求；例如 `10.7.0.1:62078` 的 Lockdown QueryType。协议使用四字节大端长度加 Plist；需要收到有效协议响应，不能仅凭 `connect()` 成功宣布可用。
3. 遇到 EOF/reset 先按主技能重新核实引擎状态；不要直接归因于 Suspend、配对文件或 reflect 故障，也不擅自重启引擎。
4. 日志捕获正常却无目标连接记录时转 Packet Capture：IP 层反射可能不产生常规连接日志。也可在授权范围内以普通本机 TCP 服务作对照，将通道问题与设备服务问题分开。
5. 只有协议通道有效后，再按用户授权验证配对/受信任会话及安装；不要为了诊断网络直接执行配对或安装。

## 反射 PCAP 判读

抓包与导出限制见 [诊断参考](diagnostics.md#packet-capture-与导出边界)。探测前记录时间、源地址和端口；以下是历史样本，不应写死到脚本：

```text
反射前：198.18.0.1:58038 → 10.7.0.1:62078
反射后：10.7.0.1:58038 → 198.18.0.1:62078
```

同一份抓包可能同时包含反射前后的包。样本中端口、TCP seq/ack 和 Flags 保持对应，源/目标 IP 交换；回包也反向交换。用这些字段与时间关联，不要将成对记录误判为重传或独立连接。`198.18.0.1` 在此是探测 socket 观察到的源地址，不能仅因其地址段就断言 DNS 假 IP 异常。

依次判断：

1. SYN 与反射后的 SYN 是否对应；
2. SYN-ACK 是否返回，三次握手是否完成；
3. 哪个端口侧先 FIN/RST；
4. 关闭发生在应用请求载荷发送之前还是之后。

该样本显示双向反射、握手成功，服务端口一侧先 FIN，早于客户端请求载荷。这支持将问题范围移到服务侧连接接受/关闭行为，而不是继续改 Plist 字段或反射路由；但不能仅凭包序列认定具体进程、配对状态或 iOS 安全策略是原因。反射成功与 Lockdown/安装成功应分开报告。
