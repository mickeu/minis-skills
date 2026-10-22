# Surge 按需诊断

仅在实际排查对应功能时读取；先按入口确认目标实例及引擎状态。这里是 Surge 特有行为，不以其他代理软件语法替代。

### 路由与 DNS

```sh
surge-cli --raw rule match example.com
surge-cli --raw rule explain https://example.com
surge-cli --raw dns trace example.com
surge-cli --raw geoip 1.1.1.1
```

- `rule match`：快速查看命中规则和最终策略。
- `rule explain`：查看完整策略组决策路径；回答“为什么这样走”时优先使用。
- `http probe <url> [policy]` 会发送真实 HEAD 请求，只在需要端到端验证时使用。

需要改变路由才能验证、且用户授权时，优先考虑临时规则而非改 Profile；临时规则立即生效并优先于 Profile 规则。先列出已有规则，记录本次新增项。

```sh
surge-cli rule temp list
# 确认 Proxy 存在且获准测试后再添加：
surge-cli rule temp add "DOMAIN-SUFFIX,example.com,Proxy"
surge-cli rule temp list
```

`rule temp flush` 会清空全部临时规则，禁止当作本次测试的常规清理。只移除本次新增规则；具体标识与 remove 参数先核对 [命令参考](command-reference.md) 及返回结果，不能猜索引或清除用户既有规则。

### 实时日志与临时 verbose

先完成已授权的模块/配置变更，再记录原日志等级并设 `verbose`。`set-log-level` 只改运行时；reload 会恢复配置等级，模块切换也可能触发重载。诊断期间不要做这些操作；结束、超时或失败时均恢复原等级，不把 `notify` 当固定默认值。

```sh
surge-cli --raw set-log-level verbose
surge-cli --raw log watch > /tmp/surge-watch.jsonl 2> /tmp/surge-watch.err &
echo $! > /tmp/surge-watch.pid
```

监听是持续进程，必须重定向 stdout/stderr，并记录本次 PID 以便清理。确认订阅建立后再发探测（跨工具调用可用 `delay`），记录时间与 `socket.getsockname()` 的源 IP/端口。只结束本次监听进程。

`log watch` 不回放历史；近期留存细节用 `log memory`，较长历史用 `log file`。原始 JSON Lines 包含订阅确认和事件 envelope：

```json
{"result":"Log watch subscribed"}
{"event":"log","data":{"level":"verbose","module":"…","log":"…"}}
```

解析时跳过无 `log` 的确认帧，从 `data` 取字段，兼容解包结果可用 `d = obj.get('data', obj)`。不要从顶层直接取 `log/level/module` 而将空字段误认为没有日志。

目标搜索零命中时，先检查总事件数、等级分布、起止时间是否覆盖探测及 stderr。涉及 VIF/IP Rewrite 的流量，即使日志捕获完整也可能没有普通连接记录；无日志不等于未处理，应转数据包抓取，参见 [reflect 专题](ip-rewrite-loopback.md)。

### Packet Capture 与导出边界

`capture`/`Replica` 是 HTTP 捕获；`packet-capture`/`PacketCaptureEnabled` 是 IP 数据包捕获，不要混用。参数见 [命令参考 §4.6](command-reference.md#46-packetcaptureparameters-fields)。

开始前记录已有抓包状态和参数。若用户已在抓包，不接管、重置或关闭已有会话；先确认处理方式。环境响应可能包装为 `{"result":…, "environment":{…}}`，字段缺失不等于已确认默认值；原参数无法读取时不得宣称之后已完整恢复。

已获准新建短时抓包且原抓包关闭时，可用：

```sh
surge-cli --raw set \
  PacketCaptureParameters.packetType=6 \
  PacketCaptureParameters.timeLimit=10 \
  PacketCaptureParameters.packetCountLimit=500 \
  PacketCaptureParameters.sizeLimit=1048576
surge-cli --raw feature set packet-capture on
# 发只读探测，记录时间和源端口
surge-cli --raw feature set packet-capture off
```

- `packetType=6` 为 TCP。现有字段支持协议、时长、包数、大小限制，未提供目的 IP/端口过滤；不要先承诺精确过滤，再执行全 TCP 抓包。说明可能包含短时间内的其他流量。
- 执行时用 `try/finally` 或 shell trap 保障异常清理；关闭本次抓包后恢复已记录的原参数并复核状态，不只关闭开关。原值不可读时使用最小变更并如实报告恢复限制。
- 截至 2026-10-05 所查 Controller/HTTP 文档未找到 PCAP 导出接口；`retrieve-data` 是 HTTP 请求/响应 body，不是 PCAP 导出。不要猜 API 端点。
- 可先在已挂载 Surge 目录用 `rg --files -g '*.pcap' -g '*.pcapng'` 查找；挂载中没有文件时，请用户从 Surge 的 Packet Capture 页面分享导出 `.pcap/.pcapng`。这不等于断言所有版本都无自动导出能力。
- 收到附件后用 `tcpdump -nn -tttt -S -vvv -r <file>` 离线分析。不要把完整流量上传公开网站；围绕本次端口和时间筛选。`[IP Rewrite]` 的 `reflect` 在 IP 层、先于规则交换源/目标 IP，同一抓包会有反射前后两份包（IP 互换、端口与 seq/ack 不变），不要误判为重传；详见 [reflect 专题](ip-rewrite-loopback.md)。

### 性能与隧道

```sh
surge-cli --raw dump performance
surge-cli --raw dump rule-usage
surge-cli --raw benchmark rule-matching
surge-cli --raw benchmark encryption 25
```

`benchmark encryption` 测量 Surge 所在设备的本地加密性能，不是网络带宽。

排查 Tailscale/WireGuard 时，用策略名（来自 `dump policy`，line-hash 也可）读取运行时状态：

```sh
surge-cli --raw proxy-runtime-status "<policy-name>"
```

优先检查握手、底层策略、Tailscale 会话、Exit Node、DERP 和 peer path，不要先做宽泛日志搜索。
