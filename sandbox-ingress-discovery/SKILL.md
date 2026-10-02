---
name: sandbox-ingress-discovery
description: 在托管云沙箱/云容器中定位平台分配的「直连入站域名」(public URL)，从而无需自建 Cloudflare/ngrok 隧道即可从公网访问容器端口。适用于 E2B、Modal、Daytona、RunPod、Fly Machines、Codespaces 等平台。当用户提到「不用 CF 内网穿透」「怎么从外面连进容器」「找入站域名」「沙箱公网地址」「容器公网 URL」「直连容器」「免隧道访问」时触发。
version: 1.0.0
---

# 云沙箱直连入站域名发现

## 目的

托管沙箱平台会给每个实例分配一个**公网入站域名**（用于把容器内某端口暴露到公网）。
本技能给出**从容器内部把这个域名挖出来**的通用流程 —— 挖到后即可自建隧道（SSH / 任意 TCP / 代理），**完全不依赖 Cloudflare、ngrok 等第三方穿透**。

## 标注说明（先读这个）

本技能**混合了通用方法论与单一平台的实测结论**，阅读时务必区分：

| 标记 | 含义 | 能否照搬 |
|---|---|---|
| 🟢 **通用** | 平台无关的原理 / 协议约束 | ✅ 可直接套用 |
| 🟡 **需实测** | 原理通用，但具体形态、端口、行为随平台而异 | ⚠️ 必须自行验证 |
| 🔵 **Manus 专属** | 仅在 Manus 容器（E2B + Manus 控制面）实测确认 | ❌ **别套到别的平台** |

> **一句话**：🟢 是"物理定律"，🟡 是"常见套路"，🔵 是"这台机器的体检报告"。
> **把 🔵 当成 🟢 用，必然踩坑。**

## 核心原理

1. **平台必然存在入站域名**：没有它，用户就无法访问容器内的 Web 服务（Jupyter / VSCode / 预览端口）。平台只是不把它明文写在容器里。
2. **容器内部能"听到"它** 🟡：平台控制面会用该域名作 `Host` 头，**主动连进容器内的管理端口**（supervisor / agent / metrics）。但**是否明文取决于厂商** —— Manus 是裸 HTTP（🔵 好挖），换成 TLS 控制面的平台就挖不到，只能退回 `strings` 或平台 API。
3. **域名通常编码了路由信息**：常见形态 `<port>-<sandboxId>-<hash>.<region>.<平台域名>` —— 端口、实例 ID、区域都是可替换的。

## 侦察流程

### 阶段 0：确认是托管沙箱（而非普通 VPS）🟢

```bash
systemd-detect-virt                  # kvm / gvisor / docker → 托管沙箱特征
ip -4 addr show | grep inet          # 169.254.x.x 或纯私网 → 无公网 IP
cat /proc/cmdline                    # Firecracker 特征: virtio_mmio / nomodules / pci=off (🟡)
ls / | grep -iE 'e2b|modal|daytona|runpod|codespace|fly'   # 平台指纹 (🟡 关键词需扩充)
```

### 阶段 1：识别平台与其 metadata 服务 🟡

| 线索 | 命令 |
|---|---|
| 平台 agent 进程 | `ps -eo pid,args \| grep -iE 'envd\|agent\|supervisor\|init'` |
| 平台启动脚本 | `ls /e2b-startup.sh /etc/<platform>` |
| 平台配置 | `cat /.e2b 2>/dev/null`（E2B 写 ENV_ID / BUILD_ID） |
| 云 metadata | `curl -s -m3 http://169.254.169.254/`（Firecracker MMDS，需先取 token） |
| 控制面连接 | `ss -tnp \| grep -vE '127.0.0.1\|::1'` |

**MMDS 取 token（Firecracker 专用）**：

```bash
T=$(curl -s -X PUT http://169.254.169.254/latest/api/token -H 'X-metadata-token-ttl-seconds: 300')
curl -s -H "X-metadata-token: $T" http://169.254.169.254/     # 列出全部键
```

常见键：`instanceID` / `sandboxID` / `envID` / `teamID`（🔵 Manus/E2B 实测；**其他平台键名不同**）。**instanceID 是后续路由的钥匙。**

### 阶段 2（关键）：抓内部明文流量，提取 Host 头 🟡

#### ⚠️ 前提：这些流量**不是容器自己产生的**，是外部平台层驱动出来的

**这是整个流程最容易失败的地方。**

容器自己**不会**产生入站控制面流量 —— 那些调用来自**平台后端**（在 Manus 里，就是对话框那头跟你对话的 **AI 控制面**）。容器空闲时，控制面只发保活心跳，**不带公网 Host 头**。

**所以顺序必须是"两头同时开工"：**

| 步骤 | 在哪做 | 做什么 |
|---|---|---|
| ① | **容器内** | 先把抓包挂起来（后台跑） |
| ② | **外部平台层** | **回到 AI 对话框，让它去调用容器** |
| ③ | 容器内 | 停止抓包 → 分析 |

**第 ② 步具体怎么"驱动"**（动作越多，抓到的 Host 越全）：

- 让 AI **执行一条 shell 命令**（`ls` / `whoami` 就够）
- 让 AI **读 / 写一个文件**
- 让 AI **启动或重启桌面 / 工作负载**
- 让 AI **截屏**、或跑任意一次工具调用

这些动作会逼平台后端**用公网 Host 头回调容器**，Host 头就出现在包里了。

> **反面教材**：挂上抓包然后干等 90 秒 —— 大概率只抓到心跳，或者**什么都抓不到**。
> 抓包是"在容器里装监听"，而"制造通话"的按钮在**外面那个 AI 对话框**上。**少哪一头都不行。**

> **推广到其他平台** 🟡：同理，你要先找到该平台的"外部驱动入口" —— 可能是它的 Web 控制台、CLI、SDK 调用，或者（如果是 AI 沙箱）对话框本身。

#### 挂抓包（容器内，被动零影响）

```bash
apt-get install -y -qq tcpdump tshark
tcpdump -i eth0 -s 0 -w /tmp/cap.pcap &     # 被动旁路，不碰业务流量
# ── 现在切到外部对话框，让 AI 操作容器（见上表第 ② 步）──
sleep 90; kill %1
```

#### 快速提取 Host 头

```bash
tshark -r /tmp/cap.pcap -Y 'http.request' \
  -T fields -e ip.dst -e http.host -e http.request.uri -e http.user_agent \
  | sort -u
```

**找什么**：形如 `<port>-<id>-<hash>.<region>.<domain>` 的 Host 头，或任何非标准域名。
同时看 **body** —— 平台常在请求体里下发**预签名 URL**（S3 等），可反推账号 / 桶 / 区域。

#### 如何分析抓到的流量（四步收敛）

**别一上来就翻包** —— 几十万条会淹死你。按顺序收敛：

**① 先看有哪些会话**（只统计，不展开内容）

```bash
tshark -r /tmp/cap.pcap -q -z conv,tcp     | head -30   # 会话：谁和谁、传了多少
tshark -r /tmp/cap.pcap -q -z endpoints,ip | head -20   # 端点：按流量排序找大头
```

**② 区分明文 / 密文**（决定能挖到什么）

```bash
# 明文 HTTP → 能看 Host / URI / body（金矿）
tshark -r /tmp/cap.pcap -Y 'http.request' -T fields -e ip.dst -e http.host | sort -u
# TLS → 只能看 SNI，看不到内容
tshark -r /tmp/cap.pcap -Y 'tls.handshake.extensions_server_name' \
  -T fields -e ip.dst -e tls.handshake.extensions_server_name | sort -u
```

**③ 定向提取明文请求 + 请求体**

```bash
# 请求行全字段
tshark -r /tmp/cap.pcap -Y 'http.request' \
  -T fields -e frame.time -e ip.src -e ip.dst -e http.host \
              -e http.request.method -e http.request.uri -e http.user_agent | sort -u

# 请求体（hex → 还原文本，常藏预签名 URL / 内部 ID）
tshark -r /tmp/cap.pcap -Y 'http.request' -T fields -e http.file_data \
  | head -20 | while read -r h; do echo "$h" | xxd -r -p 2>/dev/null; echo; done
```

**④ 校准方向 + 归属进程 + 滤噪声**

抓包只看到 IP，**必须先确定哪边是上行**：用你自己发起的已知流量做基准（比如 `curl` 下载一个大文件），流量大的那侧就是下行。

```bash
tshark -r /tmp/cap.pcap -q -z conv,tcp | grep '<你的基准IP>'   # 对方向
```

把流量**归到进程** —— 抓包期间另开一路采样 `ss`：

```bash
while :; do date +%s; ss -tnp state established; sleep 2; done > /tmp/procs.log
```

**滤噪声**（很重要）：沙箱里常有**大流量但无关**的通道（桌面画面推流、屏幕流），会淹没真正的控制面流量。**控制面请求的特征是小包、高频、明文**：

```bash
tshark -r /tmp/cap.pcap -Y 'http.request && http.content_length < 4096' \
  -T fields -e ip.dst -e http.host -e http.request.uri | sort | uniq -c | sort -rn | head
```

**判断优先级**：`Host` 头里出现**非标准域名**（形如 `<port>-<id>-<hash>.<region>.<domain>`）→ 那就是目标，立刻进阶段 3 验证。

#### 无明文 HTTP 时的补充手段（🟡 厂商把控制面换成 TLS 时用）

```bash
# 平台 agent / 日志里的域名
grep -rhoE '[a-z0-9-]+\.(amazonaws|cloudfront|workers|app|dev|computer|internal)[a-z.]*' \
  /var/log /opt 2>/dev/null | sort -u
# agent 二进制字符串
strings <agent-binary> | grep -aoE '[a-z0-9-]+\.[a-z0-9-]+\.[a-z]{2,}' | sort -u | head
```

> ⚠️ 抓包**不要做 MITM**。平台流量多为 TLS，解密既破坏业务又触碰合规红线；**被动旁路足够**。

### 阶段 3：验证域名路由

```bash
H='<port>-<sandbox-id>-<hash>.<region>.<domain>'
dig +short "$H"                            # → 通常 CNAME 到平台 LB
curl -s -o /dev/null -w '%{http_code}\n' "https://$H/"
```

**做三个变量实验，搞清路由规则**：

| 改动 | 观察 | 结论 |
|---|---|---|
| 换端口前缀（如 `22-` / `49983-`） | 各端口返回不同服务 | 端口是路由的一部分 → **可暴露任意端口** |
| 换 sandbox-id | `502` | **id 才是路由钥匙** |
| 换 hash | 仍 `200` | hash 常**不校验**（装饰性） |

**验证外部可达**：在容器内起个临时 HTTP 服务，从公网 `curl` 对应端口前缀，确认 `200`。

### 阶段 4：判断 LB 层级（决定能用什么协议）🟢

这是**最关键的一步** —— 它决定后续所有方案是否可行。

```bash
echo | openssl s_client -connect "$H:443" -servername "$H" 2>/dev/null \
  | openssl x509 -noout -subject -issuer
```

| 看到的证书 | 含义 | 影响 |
|---|---|---|
| **平台的证书**（ACM / Let's Encrypt，通配 `*.<region>.<domain>`） | **L7 LB，TLS 在 LB 终止** | 只能走 HTTP / WS / gRPC |
| **你自己的证书**（你在容器内起的） | L4 透传 | 任意 TCP / 裸 TLS 均可 |

辅助判断：`curl -sI "https://$H/"` 看 `Server:` 头（`awselb` / `envoy` / `nginx` / `cloudflare`）。🔵 Manus 实测返回 `Server: awselb/2.0` → 直接坐实 L7。

**决定性实验**：在容器内起一个带**自定义证书**的 TLS 服务，从外部握手看拿到谁的证书：

```bash
# 容器内
openssl req -x509 -newkey rsa:2048 -nodes -days 1 \
  -keyout /tmp/k.pem -out /tmp/c.pem -subj '/CN=PASSTHRU-PROBE' 2>/dev/null
openssl s_server -accept <PORT> -cert /tmp/c.pem -key /tmp/k.pem -quiet &

# 外部
echo | openssl s_client -connect "$H:443" -servername "$H" 2>/dev/null | openssl x509 -noout -subject
# 显示 CN=PASSTHRU-PROBE → L4 透传
# 显示平台通配证书     → L7 终止（确认无疑）
```

**L7 是硬约束**（务必记住）：

| 协议 | L7 LB | L4 LB |
|---|---|---|
| HTTP / WebSocket / gRPC / XHTTP | ✅ | ✅ |
| 裸 TLS（Reality、Trojan 原始、XTLS Vision） | ❌ | ✅ |
| 任意 TCP（SSH、Shadowsocks、数据库） | ❌ | ✅ |

> **Reality 在 L7 下物理不可能**：它的核心是"客户端 ↔ 节点端到端裸 TLS 握手"，而 L7 LB 会先解开 TLS 再转发，握手根本到不了后端。
> 同理 **Trojan 原始（裸 TLS）**、**XTLS Vision** 也都不可用。

### 阶段 5：搭隧道（L7 场景）

L7 下要用 **WebSocket 类隧道**把任意 TCP 包进 HTTP。首选 `chisel`（单文件静态二进制，零依赖）：

```bash
# ── 容器内（服务端）──
curl -sL -o chisel.gz https://github.com/jpillora/chisel/releases/latest/download/chisel_<ver>_linux_amd64.gz
gunzip chisel.gz && chmod +x chisel
./chisel server -p <PORT> --auth <user>:<pass>          # 明文 HTTP，TLS 由 LB 提供

# ── 外部（客户端）──
chisel client --auth <user>:<pass> \
  https://<PORT>-<sandbox-id>-<hash>.<region>.<domain> \
  2222:localhost:22                 # 本地 2222 → 容器 22
ssh -p 2222 root@127.0.0.1

# SOCKS5 出口
chisel client --auth <user>:<pass> https://<...> 1080:socks
```

**固化为常驻服务**（避免重启后失联）：

```ini
# /etc/systemd/system/<name>.service
[Unit]
Description=WS tunnel server
After=network.target
[Service]
Type=simple
ExecStart=/usr/local/bin/chisel server -p <PORT> --auth <user>:<pass>
Restart=always
RestartSec=5
[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload && systemctl enable --now <name>.service
```

**同类替代**：

| 工具 | 说明 |
|---|---|
| `wstunnel` | Rust 实现，同样把任意 TCP 包进 WS |
| `Xray` `vless+ws` / `trojan+ws` / `xhttp` | 完整代理，`xhttp` 是官方推荐的新一代 |
| `cloudflared` / `ngrok` / `frp` | 需要外部账号，**本技能就是为了绕开它们** |

> **Xray 官方已把 WebSocket 与 Trojan 标记 deprecated**，新部署优先 **XHTTP** —— 它本身就是 HTTP 协议族，与 L7 LB 天然契合，抗封也更好。

## 平台对照 🟡（**仅 E2B 行经实测**，其余均为公开资料推测，未验证）

| 平台 | 平台 agent / 线索 | 公网 URL 形态 | 备注 |
|---|---|---|---|
| **E2B** 🔵 | `envd`（:49983）、`/e2b-startup.sh`、`/.e2b` | `<port>-<sandboxId>-<hash>.<region>.<platform-domain>` | 走 AWS ALB，**L7 终止**（本技能实测来源） |
| **Modal** | `modal` CLI / worker | 由 `@web_endpoint` / `web_server` 生成 | 自研代理层 |
| **Daytona** | `daytona` | `<port>-<id>.<domain>` | 端口前缀式 |
| **RunPod** | `runpod` / `start.sh` | `https://<podId>-<port>.proxy.runpod.net` | 代理层 |
| **Codespaces** | `code` / `gh` | `https://<name>-<port>.app.github.dev` | GitHub 代理 |
| **Fly Machines** | `init`（fly） | `https://<app>.fly.dev` | 可另配独立 IP |
| **Gitpod / Coder** | `supervisor` | `<port>-<workspace>.<domain>` | 同类前缀式 |

> **通用形态**：绝大多数平台用 `<端口>-<实例ID>.<平台域名>` 或 `<实例ID>-<端口>.<平台域名>`。
> 拿到一个后，**先做阶段 3 的三变量实验**，几分钟就能确认规则。

## 常见陷阱

1. **hash 段常不校验** → 真正的防线是 `sandbox-id`。**只要 id 泄露，任何人都能访问你容器的所有端口。**
2. **L7 终止 TLS** → 别浪费时间试 Reality / 裸 TLS / XTLS Vision 类协议，物理不通。
3. **端口前缀可任意** → 你自己起的服务也会被暴露。**切勿在沙箱跑无鉴权服务**（Redis / Docker API / Jupyter 无密码）。
4. **出口 IP 可能是共享代理池**（移动 / 住宅 / 数据中心混用）→ 出站 IP 会漂移，且易被 IP 信誉库标为 `proxy: true` / `hosting: true`。用 `curl ip-api.com/line/<ip>?fields=proxy,hosting` 自查。
5. **空闲即挂起** → 托管沙箱普遍有 freeze / pause 机制，隧道会随实例冻结而断。客户端要开**自动重连**，服务端要 `Restart=always`。
6. **内部流量常是明文** → 能抓到预签名 URL / 内部域名 / 协议版本。这些属敏感信息，**不外传、不留存**。
7. **抓包别做 MITM** → 平台流量多为 TLS，解密既破坏业务又触碰合规红线。**被动旁路足够。**

## 安全与合规边界

- ✅ 仅对**自己拥有 / 已授权**的实例操作。
- ❌ 不要枚举 / 爆破他人的 `sandbox-id` —— 那等同入侵，且平台有审计日志。
- ⚠️ 把托管沙箱当**代理节点长期使用**，通常**违反平台 ToS**，且平台可随时封禁、销毁实例。
- 🔒 抓到的预签名 URL、密钥 ID、内部域名、实例 ID **一律脱敏**后再分享。

## 🔵 Manus 专属速查（**别套到其他平台**）

以下是 **Manus 容器**（E2B Firecracker + Manus 控制面）实测确认的**具体值**，仅供对照参考：

| 项目 | Manus 实测值 |
|---|---|
| 底层平台 | E2B（Firecracker microVM，`systemd-detect-virt` → `kvm`） |
| 平台 agent | `envd`（:49983） |
| 控制面入口 | `supervisor-http.py`（:8331，**裸 HTTP** —— 这次能挖到的关键） |
| 公网域名形态 | `<端口>-<instanceId>-<任意8位hash>.<区域>.<平台域名>` |
| 区域 | `us1` / `us2` / `us3` / `eu1` / `ap1` |
| 路由钥匙 | `instanceId`（换掉 → `502`） |
| hash 段 | **不校验**（任意值均 `200`） |
| 边缘设备 | AWS ALB，**L7 终止 TLS**（`Server: awselb/2.0`） |
| MMDS 键 | `envID` / `instanceID` / `teamID` / `traceID` / `address`（仅 5 个扁平键） |
| 挂起机制 | 三层冻结（桌面 pause / cgroup freeze / VM suspend），空闲必断 |
| 出站 | 走共享代理池，IP 漂移且已被标 `proxy: true` |

**由此推导的 Manus 硬约束**：

| 想做的事 | Manus 能否 |
|---|---|
| SSH / 任意 TCP 直连 | ❌（L7）→ 必须 WS 隧道 |
| Reality / 裸 Trojan / XTLS Vision | ❌ 物理不通 |
| Trojan+WS / VLESS+WS / XHTTP | ✅ |
| 出口 IP 干净、不被识别为代理 | ❌ |
| 固定落地 | ❌ IP 轮换 |

> ⚠️ 上表**只对 Manus 成立**。换到 Modal / RunPod / Daytona 等平台，这些值**一个都不能假设**，必须从阶段 0 重新走一遍。

## 最小复现清单

```bash
# ① 确认托管沙箱 + 拿 sandbox-id
systemd-detect-virt                                   # kvm/gvisor → 托管沙箱
T=$(curl -s -X PUT http://169.254.169.254/latest/api/token \
      -H 'X-metadata-token-ttl-seconds: 300')
curl -s -H "X-metadata-token: $T" http://169.254.169.254/   # → instanceID

# ② 抓内部明文 Host 头（核心）
tcpdump -i eth0 -s0 -w /tmp/c.pcap &
#   ⚠️ 关键：立刻切到【外部 AI 对话框】，让它执行命令 / 读写文件 / 截屏
#      —— 不驱动容器 = 抓不到 Host 头
sleep 90; kill %1
tshark -r /tmp/c.pcap -Y 'http.request' -T fields -e http.host | sort -u
#   → 形如 <port>-<id>-<hash>.<region>.<domain>

# ③ 验证路由规则
H='<port>-<sandbox-id>-<hash>.<region>.<domain>'
dig +short "$H"
curl -s -o /dev/null -w '%{http_code}\n' "https://$H/"      # 200 = 通

# ④ 判定 LB 层级
echo | openssl s_client -connect "$H:443" -servername "$H" 2>/dev/null \
  | openssl x509 -noout -subject -issuer                    # 平台证书 → L7

# ⑤ 起 WS 隧道（L7 场景）
chisel server -p <PORT> --auth <u>:<p> &                    # 容器内
chisel client --auth <u>:<p> "https://$H" 2222:localhost:22 # 外部
ssh -p 2222 root@127.0.0.1
```

## 一句话总结

> **平台一定会给它自己的容器留一个入站域名 —— 抓一次内部明文 HTTP 的 `Host` 头就能拿到，然后用 `instanceID` 换端口即可暴露任意服务。唯一要先确认的是 LB 层级：L7 就只能走 HTTP/WS。**
