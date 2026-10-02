# Surge 知识库 (kb.nssurge.com)

> 来源：https://kb.nssurge.com/surge-knowledge-base/
> 同步时间：2026-08-08

---

## FAQ / 常见问题

## Surge iOS 特定常见问题

### Surge iOS 电量消耗的说明

Surge iOS 可能产生的电量消耗由两项组成：网络通讯（基带）电量消耗与 CPU 电量消耗。

#### 关于网络通讯（基带）电量消耗

当开启 Surge iOS 后，由于所有的应用的网络请求都由 Surge 所接管并转发，使得 iOS 统计时，将所有网络通讯所产生的电量消耗计算在 Surge 上，所以 Surge 的电量占用比例会很高。但实际上并未产生额外的电量消耗。

#### 关于 CPU 电量消耗

* 如果配置了加密的代理进行流量转发，由于进行转发时需要进行加解密运算，将产生额外的 CPU 电量消耗。一般来说该额外开销很低，基本可忽略不计，但是如果在长时间、高带宽的场景下，可能产生较大消耗，如 iCloud 同步、App Store 应用包下载等，但默认情况下这些操作系统通常是在连接电源时才会执行。
* 如果配置了 cron 类型脚本，且触发时间很频繁，可能因为不断唤醒 CPU 导致额外的电量消耗。

综上所说，持续开启 Surge iOS 对电量消耗的影响很小，据我们的测试，正常使用下 24 小时额外消耗不到 2%，不必担心。

部分用户会因为系统电耗统计中 Surge 所占用百分比很高而认为 Surge 非常耗电。请注意该统计中的百分比，指的是这段时间内的总电量消耗中 Surge 的占比，而非表示 Surge 消耗的剩余电量。由于 Surge NE 常驻后台，如果这段时间内没有几乎没有使用过设备，那即使 Surge 只消耗了极少的电量，也会被统计为 100%。

## Surge Mac 特定常见问题

### 为什么 TCP 请求仅能看到 IP 无法看到域名

如果在 Dashboard 发现，所有 TCP 请求均以 IP 地址展示，不显示域名，则说明 Surge 未能成功劫持 DNS。详细原理请见：[《Surge 官方中文指引：理解 Surge 原理 》](https://manual.nssurge.com/book/understanding-surge/cn)

可能的原因和解决方法有：

* 首先请检查设备的 DNS 设置是否为 Surge 的专用 DNS 地址：198.18.0.2，Surge 开启增强模式时会自动修改当前设备的 DNS，DHCP 模式下会自动为客户端设备配置该 DNS。
* 部分操作系统或浏览器带有 DoH/DoT 或其他加密 DNS 协议支持，Surge 无法劫持此类 DNS 请求，请手动关闭该功能。
* 设备上装有其他会劫持系统 DNS 的软件。

### 请求查看器中不显示请求

如果 Surge 请求查看器中不显示请求，可按照以下顺序进行排查：

1. 确认 Surge 已接管本地或另一设备的网络：

* 开启设置为系统代理选项可接管当前设备的大部分 HTTP/HTTPS 请求。
* 开启增强模式可接管当前设备的几乎所有请求。

可通过 Surge 主界面的客户端与进程列表确认接管是否成功，如果有项目说明接管成功。

2. 确认请求查看器的过滤器设置

在 Surge 主程序的截取页面中，可配置请求查看器截取过滤器参数，若该参数配置不当，可导致请求查看器不显示结果。

### 助手程序（Helper）异常处理方式

如果 Surge Mac 助手程序（Helper）异常，会导致无法设置系统代理和无法开启增强模式。（使用 CleanMyMac 或其他清理软件强行清理可能导致该问题）

请参照以下步骤修复：

1. 打开 Surge Mac 的设置界面，选择系统权限总览，在助手程序中选择移除。
2. 输入你的系统登录密码。
3. 点击打开终端。
4. 在终端窗口处再次输入系统登录密码并回车。
5. 重启电脑。
6. 打开 Surge，尝试勾选设置为系统代理，输入系统密码重新安装助手程序。

由于 macOS 是开发性系统，导致该问题产生的原因可能非常复杂，如果仍然不能正常工作，可能需要尝试重置整个系统。

### Surge Mac 与 VPN 一同使用

如果在 Surge 开启时同时连接了其他 VPN，可能会出现问题，请尝试关闭增强模式，如果开启增强模式需要配合自定义 direct 策略强制绑定 interface，详见手册。

如果出现了访问内网域名无法解析的问题，请：

1. 如果 VPN 正确配置了 Split DNS，那么只要由系统去进行 DNS 解析即可拿到正确结果。使用 本地 DNS 映射功能直接将内网的域名配置为 syslib 解析。

```
[Host]
*.internal.example.com = server:syslib
```

2. 请注意，server:syslib 参数在开启增强模式时无法生效，可使用本地 DNS 映射功能直接将内网的域名交给内网的 DNS 进行解析。

```
[Host]
*.internal.example.com = server:10.0.0.1
```

如果该域名本身也可以由外网访问，这样的配置可能引起问题。（可通过 DNS 脚本判断环境解决）

### 增强模式兼容性问题

Surge Mac 增强模式的原理是通过一个虚拟网卡接管所有流量。该工作模式下可能引发兼容性问题，表现可能有网速缓慢、Surge 被直接关闭、Surge 反应缓慢等，以下列出部分已知的可能产生冲突的程序。

* AdGuard
* Viscosity
* Little Snitch

### 为什么 Surge Mac 菜单栏图标无法显示在菜单栏中？

请注意，自 macOS 26 起，系统设置中新增了隐藏特定 App 菜单栏图标的选项。如果 Surge 图标在此处被隐藏，那么无论你如何修改 Surge 内部的外观设置，该图标都不会显示。请在系统设置的菜单栏选项中打开 Surge 的开关。

按住 Command 键并拖动菜单栏图标，可以将某个 App 的菜单栏图标从菜单栏中移除，这等同于在系统设置中关闭对应开关。许多用户都是由于此误操作而隐藏了 Surge 图标。

## Surge iOS 与 Mac 通用常见问题

### 关于 skip-proxy 参数的说明

配置中的 skip-proxy 参数由于命名问题可能被部分用户错误理解，Surge iOS/Mac 只是在配置自身为系统代理时，将配置于 `skip-proxy` 参数中的内容同时配置到系统的「跳过代理」设置中。与手动在系统的网络代理中进行配置相同。

* 如果 Surge Mac 仅勾选了设置为系统代理，未开启增强模式，那么处于该参数中的主机名的请求将不会被 Surge 所接管，所有 Surge 的相关功能不会生效。
* 如果 Surge Mac 勾选了设置为系统代理，且开启了增强模式，或者是在 Surge iOS 上。那么该参数将使对应请求的接管模式由代理接管变为 Surge VIF 接管。Surge 的各项功能仍然生效但是会有细节上的区别。

所以，并非是配置在 `skip-proxy` 参数中的主机名就不会使用代理转发，该参数只影响请求被 Surge 接管的方式。


* 关于接管方式的不同的具体区别，请参见 [《Surge 官方中文指引：理解 Surge 原理 》](https://manual.nssurge.com/book/understanding-surge/cn/)。
* 部分 App 即使遵循系统代理设置，也可能忽略跳过代理中的内容，具体取决于应用的代理实现。

### 为什么尝试修改设置时提示不可以进行修改？

如果你的配置来源于其他人，这种情况下配置可能会随着远程修改而自动更新（即托管配置）。

由于远程随时可能更新并覆盖本地的配置，所以这种情况下并不允许在本地对设置进行调整，以避免冲突。

如果希望在原有托管配置的基础上调整配置，可以

1. 创建该托管配置的副本，这将使得新配置脱离原配置的自动更新，从而可以随意进行编辑。
2. 以该配置为基础，创建关联配置（Linked Profile），仅从原配置中引用部分段（通常为 \[Proxy] 和 \[Proxy Group]），这样可以自己编辑其他段的相关配置。详见：[配置分离](/surge-knowledge-base/zh/guidelines/detached-profile.md)

### 为什么 Surge 频繁提示网络质量差？

简单来说，是当网络确实出现问题时才会给出该提示，此时网络处于几乎不可用的状态。

技术细节上，当 Surge 检查到 TCP 的握手时间超过 2000 ms，便会向当前配置的所有传统 DNS 发送一个 DNS 请求，若在 2000ms 内未收到应答，则判定当前网络质量差通过给于提示。

* 如果在网络确实没有问题的状态下频繁出现该提示，请检查 DNS 服务器配置是否合理（比如在中国大陆使用 8.8.8.8/8.8.4.4 和 1.1.1.1/1.0.0.1 极易无法联通）。
* 如果不希望收到该提示，可以前往 Surge 内的通知设置中单独关闭该通知。

### 为什么 Surge 进行代理转发时屏蔽了 QUIC 流量？

默认情况下，Surge 会自动屏蔽发往代理服务器的 QUIC 流量，因为代理并不适合用于转发 QUIC 流量，会产生严重的性能问题。

几乎所有应用都具备在 QUIC 不可用时自动回退到 HTTPS 的机制，所以不用担心因为 QUIC-BLOCK 而导致某网站不可访问或 App 无法使用。

相比 HTTP/2，QUIC(HTTP/3)协议只有微弱的性能改善，同时由于两者都使用了 TLS/1.3 作为安全层，所以安全性几乎完全一致。而由代理转发导致的性能问题大幅超过了 HTTP/3 的改善，所以完全没有必要为了追求使用 HTTP/3 而放行 QUIC 流量。

如果因为开发与调试需要使用 QUIC，请在对应代理策略的设置中调整 QUIC Block 选项。

**为什么代理不适合转发 QUIC 流量？**

问题 1：TCP over TCP 问题

TCP 协议和 QUIC 协议都是可靠的传输协议，这表示他们在传输数据时，如果发现某数据包丢包，会自动将该数据包重传。

我们看一下在一个假设情形中，TCP-based 的代理中转 QUIC 会出现什么问题：

1. 发送数据段 A，该数据段被封装进了 QUIC 的 UDP 数据包 B，通过 TCP-based 的代理中转又被封装进了 TCP 数据包 C。
2. 网络出现抖动，C 包被丢包了。
3. TCP 协议检查到丢包，重发 C‘2 包。
4. QUIC 协议也检查到丢包，重发 B’2 包，B’2 包在 TCP 层看来是新的数据流，产生新的 TCP 数据包 D 包。

可以看到，本来单次丢包所导致的重发，在双重可靠传输协议的嵌套下，产生了双倍的重发包。这里举例的是一个最简单的情况，如果丢包情况严重，那么 QUIC 层将产生大量的重发包，而 TCP 层又要保证所有的 QUIC 层重发包都被送达（实际上他们包含的数据是一样的），TCP 层再产生大量的重发包，导致拥塞情况承指数级上升。

以上只提及了众多问题中的一个，还会有双倍的 ACK 包，拥塞算法失效的问题。

所以，应当尽量避免在 TCP-based 的代理上使用 QUIC。但是如果 TCP 代理本身线路情况良好，极少丢包，同时 QUIC 流量不大，那么用起来可能确实感受不到明显问题。但是实际上也产生了不必要的额外开销，性能远不如直接使用 TCP 层代理，所以除非是需要测试 QUIC 等开发者用途，请勿调整 block-quic 参数放行 QUIC 流量。

问题 2：QUIC 流控信息不透明

即使通过基于 UDP 的协议对 QUIC 流量进行转发，由于 QUIC 的流量控制机制对中间节点不可见，代理服务器无法像转发 TCP 流量那样引入额外的中间缓冲区。在链路质量不佳的情况下，其整体稳定性往往明显弱于基于 TCP 的协议。 因此，放行 QUIC 流量可能导致显著的使用体验下降，仅建议具有明确需求的用户手动启用。

### 为什么进行 MITM 时，提示 MITM Failed？

MITM 是用于解密 HTTPS 流量的工具，使用前应先了解 MITM 的基本原理。可参考 [Wikipedia](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)。

1. 首先应确保完成 CA 证书安装操作（iOS/tvOS/visionOS 中除了安装外还需要在系统设置中手动开启开关）
2. 在 Surge 中为特定主机名开启 MITM，如 example.com。
3. 打开 Surge 的 MITM 开关。
4. 使用浏览器访问 <https://example.com/> 网站，观察是否可以解密出完整的 URL 和 HTTP 方法。

如果顺利，则表示 MITM 已正确配置并生效。

如果浏览器中的请求已经可以被正确解密，但是一些 App 的请求却显示 MITM Failed，则说明该 App 使用了 SSL Pinning 机制阻止 MITM，请自行搜索相关关键词了解详情（一般来说 SSL Pinning 无法突破，强行绕过需要非常复杂的 hack 技术，如在越狱设备中注入 dylib 覆盖相关验证代码。）

很多常见的应用，如系统进程发往 apple.com 与 icloud.com 的请求，Facebook，Instagram，X等等，都采用了 SSL Pinning 机制阻止 MITM。

---
## FAQ / iOS TestFlight

加入 Surge iOS TestFlight 后可以使用 Surge iOS 和 Surge tvOS 的 Beta 版本，Beta 版本包含实验性的功能且可能不稳定，仅推荐喜欢尝鲜且有经验的用户参与，所有已购买用户都可以自行加入。

1. 如果是从网站购买的授权或者已经绑定了邮箱

直接访问 <https://nssurge.com/account> 登录后操作。

2. 如果通过 App Store IAP 购买

请先在 App 的授权管理页面绑定邮箱，然后再访问 <https://nssurge.com/account> 登录后操作。

详情请参考 [Surge iOS 授权相关问题](/surge-knowledge-base/zh/license/ios-faq.md)

技术支持不会回答关于 TestFlight 自身的询问邮件，请查阅 Apple 的相关说明。

## 常见问题

### 为什么提示：「无法接受此邀请，因为你的 Apple 账户 <joe@icloud.com> 已与此 App关联。」

受限于 TestFlight 系统限制，如果已经加入过 Surge 的 TestFlight，希望通过 Opt-out 操作修改绑定账号，重绑定操作必须要等待 90 天后方可进行。

### TestFlight 版本可否绑定在 Surge iOS 未上架的 App Store 区域账号？

不可以，Apple 于 2021 年 2 月修改了 TestFlight 的行为，必须使用一个 Surge 上架区域的 Apple ID 方可安装 TestFlight 版本。（即不可以使用中国区 ID）

如果在非上架区域尝试安装，会收到「所请求的 App 不可用或者不存在」错误。

### TestFlight 的 Apple ID 和授权邮箱有关系吗？

最终关联的 Apple ID 由点击邀请邮件的 iOS 设备的当前登录的 App Store 账号决定，和授权邮箱（即收取 TestFlight 邀请的邮箱）并没有关系。

但是我们强烈推荐使用与授权邮箱一致的 Apple ID 进行绑定，使用不一致的 Apple ID 接受邀请，可能导致后续解除绑定时出现异常（此为 Apple 服务端的一个问题）。可以在加入 TestFlight 前先自助修改授权邮箱。

请注意一旦出现异常，需要在执行 Opt-out 后等待 90 天方可绑定至其他账号。

### TestFlight 版本是否稳定？

TestFlight 版本的目标是测试新功能，更新频率高但是可能不太稳定，如遇到问题请及时反馈，一般严重问题会在一到两天内修复。另外 TestFlight 中允许随时会退到先前的版本，如果遇到严重问题也可以自行进行版本回退。

### 收不到 TestFlight 邀请邮件怎么办？

邀请邮件由 Apple 服务器发出，部分邮箱可能接收困难，请先检查垃圾邮件箱，也可 Opt-out 后重新加入以重发，或者修改授权邮箱到另一个邮箱地址接收。

### 怎样修改绑定的 Apple ID？（或者操作错误导致邀请码失效）

可在上述管理页面执行 Opt-out 操作，然后重新进行加入。请注意退出后需要等待 90 天方可重新加入。

### 怎样取消 TestFlight 的邮件通知和推送

所有 TestFlight 相关的推送和邮件均由 Apple 发送，如需取消邮件或推送需在 TestFlight 的 App 内进行操作。

---
## FAQ / Mac 重置

如果你在使用中遇到了问题，希望重置 Surge 的所有状态（或者希望完全的卸载 Surge）。请注意在 macOS 中删除应用并重新安装并不影响应用数据，请在关闭 Surge 后删除以下文件和目录，无需删除 App 重新安装。

```
~/Library/Preferences/com.nssurge.surge-mac.plist
~/Library/Preferences/com.nssurge.surge-dashboard.plist
~/Library/Application Support/com.nssurge.surge-mac
~/Library/Application Support/com.nssurge.surge-dashboard
~/Library/Application Support/Surge
~/Library/Caches/com.nssurge.surge-mac
```

也可以直接使用以下脚本

```bash
#!/bin/bash

defaults delete com.nssurge.surge-mac
defaults delete com.nssurge.surge-dashboard

rm -Rf ~/Library/Application\ Support/com.nssurge.surge-mac
rm -Rf ~/Library/Application\ Support/com.nssurge.surge-dashboard
rm -Rf ~/Library/Application\ Support/Surge
rm -Rf ~/Library/Caches/com.nssurge.surge-mac

```

---
## Guidelines / 配置分离

为了满足各种使用场景的复杂性，Surge 支持将配置的一个段分离至另一个或多个文件中。该功能在 UI 层面又被叫做关联配置。

样例：

```
[General]
loglevel = notify

[Proxy]
#!include Proxy1.dconf, Proxy2.dconf

[Proxy Group]
#!include Group.dconf

[Rule]
#!include Rule.dconf
```

其中所引用的另一个文件，必须包含对应段的 \[] 声明。因此，该文件既可以是一个只包含部分段的文件（一个或多个），也可以是一个完整的配置。

使用该功能，你可以：

1. 只引用服务商托管配置的 \[Proxy] 和 \[Proxy Group] 段，自行编写其他段。
2. 在多个配置间共享某几个段的内容。

请注意：

* 在通过 UI 修改配置后，会按照 include 的声明将配置写入对应的分离配置段文件。但是如果一个段中引用了多个分离配置段文件，那么该段的相关内容无法在 UI 中进行编辑。
* 如果引用的是一个托管配置，则和该段相关的配置不可被编辑，但是不影响其他段的调整。
* 文件名的后缀并没有要求，如果是一个完整配置可继续使用 conf 后缀，如果并非一个完整配置建议使用 dconf，dconf 文件在 Surge iOS 里可在列表中显示，并可以使用文本编辑。
* 引用的文件不可以再次去引用另一个文件。

<details>

<summary><mark style="color:purple;">用例 #1：</mark>代理服务商提供了托管配置，仅需要其代理策略，并不想使用托管配置中的其他内容</summary>

1. 新建空白配置。
2. 在配置中增加以下内容：

```
[Proxy]
#!include ManagedProfile.conf

[Proxy Group]
#!include ManagedProfile.conf
```

其中 ManagedProfile.conf 为托管配置文件名。

3. 重载该配置，此时可以使用来自 ManagedProfile.conf 的策略和策略组，但是其他内容均可自由编辑。

</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>多个客户端间配置不同的 WireGuard Peer IP 和 Private Key</summary>

1. 假设原配置名为 Common.conf，新建 iPhone.conf 供 iPhone 使用，新建 Mac.conf 供 MacBook 使用。
2. iPhone.conf 和 Mac.conf 文件里，共同使用的内容放在 Common.conf 中并引用，WireGuard 段的内容和其他需要分开对待的内容单独撰写：

```
[General]
loglevel = notify

[Proxy]
#!include Common.conf

[Proxy Group]
#!include Common.conf

[Rule]
#!include Common.conf

[WireGuard HomeServer]
private-key = …
```

由于 Surge iOS 和 Mac 的 \[General] 段内容区别较大，一般建议分开单独撰写。

</details>

---
## Guidelines / 网关性能问题排查

### 常见问题

请先排除以下常见问题

* 无线网络

请务必使用有线方式连接，网关设备使用无线接入将严重影响性能。

* MTU 设置

请勿配置 Jumbo MTU，虽然 Surge 完整支持 Jumbo MTU，但是依然有很多设备在 Jumbo MTU 下可能出现问题。请至少在排查阶段关闭 Jumbo MTU。

### 性能排查步骤

1. 外网性能测试

首先应测试外网速度是否符合预期，在用做网关的设备上关闭 Surge，运行各类网速测试工具，如 [SpeedTest](https://www.speedtest.net/)、[WiFiman](https://wifiman.com/) 等。如果外网速度不及预期，请排查路由器、交换和网线，可联系 ISP 工作人员协助排查。

2. 内网设备间链路测试

应测试内网设备与用做网关设备间的链路速度，可使用 iperf3 进行测试。为避免无线网络的各种复杂干扰，推荐使用有线设备进行测试。千兆网络下双向速度应达到 900Mbps+。

3. 网关设备性能测试

在用做网关的设备上开启 Surge，新建一份空白配置以避免干扰，再次运行各类网速测试工具，测试结果应于步骤 1 的结果一致，如果偏低，建议在测试时同步观察系统的 CPU 使用情况。Surge 有着非常优异的性能优化，在最近 5 年内生产的 Mac 设备上均不太可能遇到设备硬件性能瓶颈（千兆网络下），如确认是该问题请尝试重装操作系统后再试。

4. 代理性能测试

若使用了加密的代理，应在 Surge 中配置代理后，使用全局代理模式配合网速测试工具再次进行网速测试。该步骤的结果受两个因素限制：代理服务器线路带宽和网关设备性能。同样的，Surge 有着非常优异的性能优化，在最近 5 年内生产的 Mac 设备上均不太可能因设备硬件性能而限制了网速（千兆网络下），如确认是该问题请尝试重装操作系统后再试。

---
## Guidelines / 网关模式配置

Surge 可作为网络网关，用于接管局域网内其他设备的全部网络流量。此功能通常被称为“旁路由”或“透明网关”。

### 工作模式

Surge Mac 提供两种网关模式：

1. **增强模式 (Surge VIF)**: 利用 Surge 的虚拟网络接口作为网关。
2. **Surge VM 网关**: 提供更优的性能和更丰富的功能，但无法与其他虚拟机软件的桥接模式（如 Parallels Desktop, VMware Fusion）同时运行。此模式仅在 Surge Mac 6.0 及以上版本中可用。

增强模式可同时用作接管当前设备的网络请求，但 VM 网关仅可用于接管其他设备的网络请求。

## 配置方法

1. 在 Surge Mac 中启用“增强模式”或“VM 网关”。
2. 在需要被接管的设备上，进入其网络设置。
3. 将其**网关地址**修改为 Surge Mac 所在设备的 IP 地址（若使用 VM 网关，则修改为 VM 网关的 IP 地址）。
4. 将其 **DNS 服务器**地址修改为 **`198.18.0.2`**。

**注意**：DNS 地址是 **`198.18.0.2`**，而非 `192.168.x.x`。

完成以上步骤后，Surge 即开始接管该设备的网络流量。

### 自动化配置 (Surge DHCP)

您可以使用 Surge 的 DHCP 功能来自动为客户端配置网络设置，从而实现自动接管。

**使用前请注意：**

1. **基本知识**: 您需要了解 DHCP 的基本工作原理。
2. **DNS 配置**: 必须在 Surge 的配置文件中至少配置一个有效的上游 DNS 服务器。
3. **禁用现有 DHCP**: 您必须禁用当前网络中的其他 DHCP 服务器（通常由主路由器提供）。
4. **有线连接**: 运行 Surge 的 Mac 设备应使用有线网络连接，强烈不建议使用 Wi-Fi。
5. **静态 IP**: Surge Mac 自身必须使用静态 IP。当启用 Surge DHCP 功能时，Surge 会自动将设备的网络设置为静态 IP。
6. **稳定性**: 开启此功能后，请勿随意移动或关闭运行 Surge 的 Mac 设备，否则可能导致整个网络中断。
7. **紧急恢复**: 如果网络出现问题，请关闭 Surge DHCP 功能，并重新开启主路由器的 DHCP 服务以恢复网络。

默认情况下，新设备加入网络后不会被自动接管。您可以在 Surge 的设备列表中，右键点击目标设备并选择“使用 Surge 作为网关”。如需自动接管所有新设备，可在网关模式配置中勾选“默认使用 Surge 作为网关”选项。

**兼容性提示**: Surge 网关模式的实现机制可能与部分设备存在兼容性问题。建议仅为需要接管的设备开启此功能。

### IPv6 RA 覆盖

对于存在 IPv6 的网络环境，仅通过 DHCP 修改 IPv4 设置可能导致流量接管不完整。Surge Mac 6.0 新增了 IPv6 RA (Router Advertisement) 覆盖功能，以确保 IPv6 流量也能被正确接管。

* 此功能不影响客户端的 IPv6 地址分配。
* 如果主路由器的 RA 消息优先级被设为“高”，Surge 可能无法成功覆盖。请将路由器的 RA 优先级调整为“普通”或“低”。

如果您不使用 IPv6，也可以直接在路由器设置中禁用整个网络的 IPv6 功能。

### 常见问题排查

#### Q: 请求查看器中为何只显示 IP 地址，不显示域名？

**A:** 这是因为客户端的 DNS 未被正确指向 `198.18.0.2` 或 `fd00:6152::2`，导致 Surge 无法通过其 Fake IP 机制将 IP 地址映射回域名。

**解决方案：**

1. **检查配置**: 检查客户端 DNS 设置是否正确。
2. **强制劫持 DNS**: 对于无法手动修改 DNS 的设备，可以在 Surge 网关模式配置中，勾选“劫持所有发送到 53 端口的 UDP DNS 查询”。此选项能解决大部分问题。
3. **处理 IPv6 RA DNS**: 在某些情况下，即使勾选了劫持选项也无效。这可能是因为网络的 IPv6 RA 广播了一个本地链接地址 (link-local) 或路由器自身的 IPv6 地址作为 DNS，导致 DNS 查询绕过了 Surge。请在路由器的 IPv6 设置中，将 RA 的 DNS 地址设置为空，或改为一个公共 DNS 地址（如 Google Public DNS `2001:4860:4860::8888`）。（在配置 Surge IPv6 RA 覆盖时，若检测到此问题会发出警告）

部分路由器（如华硕 ASUS 原厂固件）无法自定义 IPv6 RA 的 DNS 设置。可以考虑刷入 Merlin 或 OpenWRT 等第三方固件来解决。

4. **处理加密 DNS (DoH/DoT)**: 如果设备或应用内置了加密 DNS 功能，Surge 的 Fake IP 机制将失效。此时，虽然无法显示域名，但仍可通过规则进行流量分流。请为相关规则启用 `extended-matching` 标记，利用 HTTP Host 或 TLS SNI 嗅探结果进行匹配。

如果仅仅是少数 Apple 相关域名，如 gateway.icloud.com 和 tether.edge.apple，以 IP 形式进行了请求，这是预期行为，iOS/macOS 对部分域名有特殊的加密 DNS 解析逻辑阻止了 Fake IP 机制。

### 已知兼容性问题

#### P2P 客户端

在被接管的设备上运行 P2P 下载软件（如 BT、迅雷）、游戏下载器或直播应用时，可能会因瞬时并发连接数过高而导致 Surge 出现性能问题甚至中断。建议避免在此类设备上使用网关模式。我们将在未来的更新中优化此问题。

**技术说明**: 传统路由器在数据包层面工作，处理大量并发连接（如 1000 个）仅涉及 NAT 表的少量开销，压力很低。 而 Surge 工作在应用层，需要对每个连接进行协议嗅探、规则匹配和日志记录。单个大流量连接不成问题，但瞬间产生数千个新连接会带来巨大的处理开销。

#### PlayStation Portal™ Remote Player

当 PS Portal 被 Surge 网关模式接管时，异地串流无法正常开启。

这是因为 PS Portal 异地串流的逻辑与 Surge 的工作模式存在冲突，由于 Surge 需要进行 Protocol Sniffing，会对所有 TCP 请求先接受握手再进行处理，而 PS Portal 检查是否是同局域网的方式是直接访问 PS5 的内网 IP，检查是否能完成 TCP 握手，所以导致误判为同局域网。

可以通过增加一条规则的方式解决该问题，如：

`IP-CIDR,192.168.0.100/32,REJECT-DROP,pre-matching,no-resolve`

其中的 IP 地址为 PS5 的内网 IP 地址，规则一定需要带上 `pre-matching` 标记，这样 PS Portal 便不会误判，可以正常启用异地串流流程。

另外，也可以利用该机制，欺骗 PS Portal PS5 处于同一局域网中，这样便可使用自己的私有网络畅玩 PS Portal。如果使用的是 Surge Ponte，只需增加规则将 PS Portal 对 PS5 的访问转至 PS5 所在网络即可。

---
## Guidelines / Ponte 模式

Surge Ponte 是一种在运行 Surge Mac 和 iOS 设备之间的私有网络。

* 无需繁琐配置。
* Surge 会自动选择最合适的通道建立连接。
* 始终端到端加密。
* 设备信息和加密密钥通过您的 iCloud 同步，除了您选择的代理服务器外，您的数据不会经过任何第三方服务器。

该文章将协助您开始使用 Surge Ponte。

### 了解 Ponte 类型

Surge Mac 可以用作 Surge Ponte 服务端和客户端，而 Surge iOS 只能用作 Surge Ponte 客户端。

当配置 Surge Mac 作为 Surge Ponte 服务端时，有 3 种不同的配置方式。

1. 直接 NAT 穿透

仅当当前网络处于 Full Cone NAT 时可用，当前网络的 NAT 类型和路由器的具体型号、ISP 有关，一般很难改变。

2. 通过代理 NAT 穿透

可在任何网络情况下使用，需借助一支持 UDP 转发的代理实现。（请注意，如果你使用的是付费代理服务，使用 Surge Ponte 时同样会消耗你的流量。）

3. 静态端口转发（高级用户）

如果您有公网 IP 地址并且知道如何配置路由器，则可以选择配置静态端口转发。

### 在 Surge Mac 上配置 Surge Ponte

1. 在侧边栏中选择“概览”，然后打开 Surge Ponte 开关。
2. 点击下一步。
3. 等待 Surge 测试当前网络的 NAT 类型。
4. 如果测试结果是：
   * Full Cone NAT（A）：您可以选择任意方法来设置 Surge Ponte。
   * 其他（B/C/D）：您可以选择通过代理的 NAT 穿透，或者如果您有公网 IP 地址并且知道如何配置路由器，则可以选择静态端口转发。
5. 如果您选择了通过代理的 NAT 穿透，请选择一个支持 UDP 中继的代理（Snell/shadowsocks/Trojan/SOCKS5/WireGuard）。
6. Surge 将测试代理是否合格。代理服务器不能位于 NAT 或防火墙后面，除非它们已经适当配置以允许 Full Cone NAT。
7. 为当前设备选择一个名称，例如 MyMacMini。名称不区分大小写，只能包含字母、数字、下划线和连字符。
8. 在其他设备上打开 Surge Ponte。Surge iOS 配置起来会非常简单，因为它只能用作客户端。

### 使用 Surge Ponte

你现在可以从任何一个运行 Surge 且登录了相同 iCloud 的设备上访问这个设备了。有两种使用方式：

1. 你可以使用域名 `ponte-name.sgponte`（如 mymacmini.sgponte）访问这个设备上的服务，如你在该设备上的 8080 端口上运行了一个 HTTP 服务器，那在其他设备上可以直接访问 <http://mymacmini.sgponte:8080/>
2. 你也可以使用策略 `DEVICE:PONTE-NAME` 使用该设备作为跳板使用其访问其他网络，如内网中的 NAS。规则示例：

```
IP-CIDR,192.168.30.0/24,DEVICE:MyMacMini
```

<details>

<summary><mark style="color:purple;">用例 #1：</mark>配合 Surge Ponte 和系统文件共享服务，你可以随时从 iOS 设备上访问 Mac 中的文件。</summary>

1. 在 Surge Mac 上开启 Surge Ponte，这里取名为 macbook。
2. 在 macOS 的系统设置中，找到通用›共享›文件共享，打开开关。
3. 在 iOS 设备上开启 Surge iOS，确认 Surge Ponte 界面中可以看见 Mac 设备。
4. 打开系统自带的「文件」app，切换到「浏览」页，点击右上角的更多按钮，选择连接服务器。
5. 输入 macbook.sgponte，点击下一步。
6. 选择注册用户，输入 Mac 的用户名和登录密码。

</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>可以配合 Surge 的 DNS 映射功能访问家庭网络中的设备，而无需配置全网段规则。</summary>

1. 在 Surge Mac 上开启 Surge Ponte，这里取名为 `macbook`。
2. 在 Surge Mac 上配置 DNS 映射：nas.myhome = 192.168.1.20，具体 IP 与名字为需要访问的设备。
3. 在客户端设备上配置规则，`DOMAIN-SUFFIX,myhome,DEVICE:macbook`，请注意由于该域名无法在客户端设备上被解析，所以该规则必须放置于会触发解析的 IP 类规则之前。
4. 通过浏览器访问 nas.myhome 即可。

</details>

### 客户端侧代理

在客户端同样可以配置代理以访问 Ponte 服务端，这不是必须的。即使服务端配置了代理 NAT 穿透，客户端也不需要配置代理，但配置代理可以帮助突破某些网络环境下的 UDP 流量封锁。

比如由于中国大陆的出境网络通常于网络高峰期会出现 UDP 流量严重丢包的现象，若使用了一个境外的代理作为 NAT 穿透，客户端最好也配置使用相同的代理访问 Ponte 设备。

<figure><img src="/files/GSKasMqtGd97HqM0RAok" alt=""><figcaption></figcaption></figure>

Vector 为 Surge Ponte 服务所使用的底层代理协议。

### 提示

1. 你可以将内网网段设置为一个不常见的子网地址，如 192.168.150.0/24，已确保不会在其他网络下访问内网时产生地址冲突。
2. 当 Ponte 客户端与服务端处于同一个 LAN 时，将自动通过 LAN 建立连接，不会使用 NAT 穿透或代理服务器。
3. 当访问的 Ponte 设备名就是当前设备时，该策略将被转换为 DIRECT 策略。
4. 当使用 `ponte-name.sgponte` 进行访问时，实际上是动态创建了 `DEVICE:ponte-name` 策略并使用，且在远端会将 `ponte-name.sgponte` 解析为 127.0.0.1。所以即使是监听于 127.0.0.1 上的服务也可以被访问。
5. `DEVICE:NAME` 策略可以不需要在 `[Proxy]` 处声明就直接使用，且也可以用在 `[Proxy Group]` 中作为子策略，如与 Subnet Group 联用。
6. 目前 Surge Ponte 仅支持通过 IPv4 建立连接，但是可以转发 IPv6 请求。

---
## Guidelines / 使用代理服务商线路

## 配置模式

### A. 托管配置

大多数服务商会提供一份完整的 Surge 托管配置，以实现“开箱即用”。这是最便捷的接入方式：在该模式下，所有系统设置和分流规则均由服务商预设并负责维护更新。但也正因如此，用户无法在本地直接修改其中的设置与规则。

### B. 关联配置

关联配置以一份托管配置为基础，创建一个可供编辑的本地副本。通过使本地配置中的部分配置段（Section）持续跟踪托管配置的变化，从而在“配置自动更新”与“本地个性化修改”之间取得平衡。

对于大多数用户，推荐配置 `[Proxy]` 和 `[Proxy Group]` 段追踪托管配置，而其他段（如通用设置、规则等）则由本地自行控制。

### C. 外置策略组

这是 Surge 进阶用户最推荐的模式。它允许用户完全自主控制配置文件，利用外部资源实现高度灵活的定制，但要求用户对 Surge 的特性有较深入的了解。

配置示例：

`Proxy-Provider = select, policy-path=https://airport.com/surge.conf`

`policy-path` 对应的 URL 可以是一个纯代理策略列表（每行为一个代理策略声明的文本文件），也可以是一个完整的 Surge 配置文件，Surge 会自动提取其中的 `[Proxy]` 段内容。

## 实践场景

Surge 提供了极高的灵活性以满足各类复杂需求。具体参数说明请参阅官方手册，以下整理了一些推荐的配置方案与常见需求示例。

<details>

<summary><mark style="color:purple;">用例 #1：</mark>按地区划分线路</summary>

如果您的代理服务商提供了多个地区的线路，且您希望能够手动或自动选择特定地区的线路。

首先，建立一个外置策略组以导入服务商的所有线路：

```
Airport-All = select, policy-path=https://airport.com/surge.conf, hidden=true
```

设置 `hidden=true` 是因为该策略组仅作为“资源池”，我们不会在 UI 中直接使用它。

随后建立多个子策略组，利用正则过滤功能筛选出特定地区的线路：

```
Airport-US = smart, include-other-group=Airport-All, policy-regex-filter=美国
Airport-UK = smart, include-other-group=Airport-All, policy-regex-filter=英国
```

由于我们通常不关注具体使用该地区的哪条线路，建议将策略组类型设为 `smart`。这样 Surge 将自动测速并优选最佳线路，且当某条线路故障时，只要组内仍有可用线路，即可实现无感切换。

之后，您便可以在规则 `[Rule]` 中直接使用 `Airport-US` 或 `Airport-UK` 指定地区。

若需要可以随时切换线路地区，还可以再建立一个手动选择组：

```
Booster = select, Airport-US, Airport-UK
```


</details>

<details>

<summary><mark style="color:purple;">用例 #2：</mark>多供应商资源融合</summary>

假设您同时订阅了 Awesome 和 Fantastic 两家供应商的服务，并希望像“用例 1”那样统一按地区调度，可以进行如下融合配置：

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-name-prefix=Awesome-
Airport-Fantastic = select, policy-path=https://fantastic.com/surge.conf, hidden=true, external-policy-name-prefix=Fantastic-

Airport-US = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=美国
Airport-UK = smart, include-other-group="Airport-Awesome, Airport-Fantastic", policy-regex-filter=英国
```

`external-policy-name-prefix` 参数的作用是为该组内的子策略名添加前缀。由于各供应商对线路的命名通常仅包含地区（如“美国-01”），添加前缀后（如“Awesome-美国-01”）可以方便在请求列表和日志中辨别当前线路所属的供应商。

在配置 `include-other-group` 参数时，若需包含多个策略组，必须使用引号 `""` 将参数内容包裹。

</details>

<details>

<summary><mark style="color:purple;">用例 #3：</mark>跳板代理（链式代理）</summary>

若您需要通过一个跳板代理（Relay）来访问供应商的线路，有以下两种配置方式。

**方式 A：使用 `external-policy-modifier` 参数（适用于所有版本）**

使用 `external-policy-modifier` 参数为导入的策略动态追加 `underlying-proxy` 参数：

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, external-policy-modifier="underlying-proxy=Airport-Fantastic"
```

这将构建出：客户端 -> Airport-Fantastic (跳板) -> Airport-Awesome (出口) -> 目标服务器 的代理链。

**方式 B：使用策略组级别的 `underlying-proxy` 参数（Surge Mac 6.9.0+ / iOS 5.22.0+）**

较新版本的 Surge 支持直接在策略组上声明跳板代理：

```
Airport-Awesome = select, policy-path=https://awesome.com/surge.conf, hidden=true, underlying-proxy=Airport-Fantastic
```

两种方式构建出的代理链相同，但覆盖范围和呈现方式有所区别。以一个同时包含手动声明策略与导入策略的策略组为例：

```
[Proxy]
NodeA = snell, a.example.com, 443, psk=pwd, version=5

[Proxy Group]
Mixed = select, NodeA, policy-path=https://awesome.com/surge.conf, external-policy-modifier="underlying-proxy=Airport-Fantastic"
```

* 使用**方式 A** 时，只有通过 `policy-path` 导入的策略会接入代理链。`NodeA` 仍然直连，因为 `external-policy-modifier` 不会作用于手动列出的成员（也不会作用于来自 `include-all-proxies` / `include-other-group` 的成员）。修改后的策略会保留原名称，因此接入代理链的 `US-01` 在 UI 和流量统计中看起来与未接入时完全相同。
* 使用**方式 B** 时（即以 `underlying-proxy=Airport-Fantastic` 取代 `external-policy-modifier` 参数），组内所有成员都会接入代理链，包括 `NodeA`。接入代理链的成员会显示为类似 `US-01 (via Airport-Fantastic)` 的派生策略，并拥有独立的延迟测试结果。因此，自动类型策略组可以根据经过跳板代理后的实际性能选择最佳节点。该参数也可以在策略组编辑器 UI 中配置。

如果您的 Surge 版本支持，建议使用方式 B；如果配置文件必须兼容旧版本，则继续使用方式 A。

无论使用哪种方式，您都可以预先定义一个包含 `DIRECT` 策略的 `select` 组并将其设为 `underlying-proxy`，这样就能在控制面板中随时开启或关闭跳板代理模式。

对于导入策略的其他微调（如打开 TCP Fast Open），`external-policy-modifier` 仍是合适的工具。

</details>

### 策略组分组显示（`category` 参数，Surge iOS 5.102.0+）

当策略组数量较多时，可用 `category` 参数为策略组指定分组，UI 按分类折叠显示，方便管理。

```
[Proxy Group]
PROXY = select, "🇺🇸 美国节点", icon-url=..., category=🛰️ 流量分流
AIGC = select, "🇯🇵 日本节点", icon-url=..., category=🎯 场景分流
🇭🇰 香港节点 = smart, include-other-group=🌍我的节点, policy-regex-filter=(🇭🇰)|(香港), category=🌍 地区节点
```

要点：

* `category` 值可为**任意字符串**（常用 emoji + 中文，如 `🎯 场景分流`、`🌍 地区节点`），Surge 按该值分组折叠显示。
* 属于同一分类的策略组会归到同一折叠块下。
* 该参数**仅影响 UI 显示**，不影响策略逻辑、规则匹配或选组结果。
* `hidden` 参数控制是否在 UI 中显示该策略组；若想"拉出隐藏的策略组显示"，把对应组的 `hidden=1` 改为 `hidden=0` 并补上 `category` 即可。
* 经验上，订阅源（资源池，如 `🌍我的节点`）可归入 `🌍 地区节点` 分类，与地区子组放一起语义更连贯。

</details>

---
## Guidelines / Smart 智能策略组

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（`url/load-balance/fallback`），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

*该功能为 Surge iOS 订阅功能，需要订阅解锁。Surge Mac 5 可以免费获得该更新。*

### Smart 策略组特性

* Real-Time Dynamic Optimization 实时动态优化

  与目前的自动测试组的定期进行重测以决定策略不同，Smart 策略组会动态的收集每个子策略的状态，包含握手延迟、丢包率、连通性、RTT 等多个维度的信息，并根据这些信息动态的改变决策。
* Adaptive Retry 自适应重试

  在 Surge 原来的架构中，策略组的决策路径解析完成于规则匹配阶段，这使得即使通过该代理无法建立连接，也需要重新触发策略组重测才能完成策略切换。 我们为 Smart 策略组重新设计了架构，现在当出现连接建立故障或缓慢时，Smart 策略组可以立刻使用备选策略完成连接，上层的连接甚至不会察觉到发生了切换。

  同时 Smart 策略组将会以该线路的历史数据作为依据来判定线路是否出现异常，因此可在极短的时间内发现策略异常并启用备选策略接力，在先前版本通常需要等待数秒超时后才会触发异常处理流程。
* Per-site Tuning 站点调优

  目前的自动测试组的决策，是依据针对 `test-url` 的测试结果得出的。但是同一个代理可能在访问不同网站时有较大的差异，甚至完全无法访问（如部分代理不允许 SMTP 流量通过）。Smart 策略组会记录往各个网站的连通性和延迟表现，并在下次连接时针对性进行策略调整。
* Test Optimization 测试优化

  Smart 策略组同样会进行定期重测以确认一些之前出现了异常的策略是否恢复，但与传统自动测试组不同的是，Smart 策略组会自动根据使用情况进行分析，选取部分策略进行重测，而非将所有策略全部重测。这意味着即使在 Smart 策略组中配置了大量的策略，也不会因重测而产生大量开销。
* Customizable weights 可自定义的权重

  你可以使用表达式为子策略设置权重值，以微调 Smart 策略组的决策。

我们选取了几个案例，用于展示 Smart 策略组对比原自动测试组的改进：

<details>

<summary><mark style="color:purple;">故障案例 #1：</mark>当组选定的策略出现超时故障时</summary>

* url-test 组：当握手时间超过策略的 test-timeout 值后，判定为策略故障，对应的请求失败，触发策略组的重测试，若策略非常多/超时设置很长的话测试可能需要等待数十秒，待重测试完成后，新的连接开始使用新策略。

  整个过程可能导致几秒到几十秒的网络中断。
* smart 组：当握手时间超过先前的平均握手时间的 1.5 倍时，smart 组怀疑策略故障，立刻启用备用策略完成该连接，同时为该策略施加惩罚，后续连接使用该策略的概率下降，若再次使用该策略并出现了失败，那再次施加惩罚，惩罚的效果乘指数上升，策略几乎不会再被使用。

  同时惩罚会因逝去的时间衰减，使用该策略的概率将随着时间恢复，如果该线路恢复了正常，那新的成功记录将大幅抹除惩罚的效果。

  所以只要策略组中还存在可联通的策略，用户就基本不会感受到网络中断。

</details>

<details>

<summary><mark style="color:purple;">故障案例 #2：</mark>某个代理访问特定网站十分缓慢，但是访问其他网站正常</summary>

* url-test 组：由于选定策略只与 test-url 有关，这种缓慢不会引发策略组切换。
* smart 组：Smart 组可以注意到，访问该网站时的时间远高于该代理访问其他网站时的时间。于是在下次连接时，自动尝试与最优策略 A 相差不大的 B 策略：
  * 如果 B 策略的表现远好于 A 策略，则以后都使用 B 策略
  * 如果 B 策略的表现也很差，将继续尝试 C 策略，当尝试多个策略后，Smart 组认定该问题应该属于目标网站问题，不再尝试切换策略，稳定在已尝试过的策略中表现最优的策略。

</details>

以上仅为 Smart 组处理连接问题时的部分逻辑，Smart 组包含了大量精心设计的逻辑和决策系统，并且我们会持续优化，以适应更多的情况。

### 使用方法

Smart 组为全新的策略组类型，为了方便用户迁移，可以使用配置升级向导，自动将所有 url-test/fallback 组升级为 Smart 组。

* Surge iOS：升级完毕后打开 app 会直接提示升级
* Surge Mac：升级完毕后，可在更多，配置里找到配置升级向导。（下个版本会自动弹出）

请注意，由于兼容问题，升级后需要所有使用该配置的 Surge iOS 版本为 5.11.0 以上，且需要功能订阅解锁该功能。Surge Mac 需要 5.7.0 版本。升级前会自动备份原配置。

### 使用提示

* 对于同一个网站，Smart 组会尽量使用相同的策略进行连接，以避免 IP 地址变化产生问题。但是对于访问 IP 地址特别敏感的网站（如在线银行），建议单独配置规则避免使用 Smart 组。 (如果某网站访问速度本身存在问题，Smart 策略组会在尝试多个策略后逐渐收敛稳定到单个策略)
* Smart 策略组不可以使用其他组作为子策略，也不可以用作 `url-test/load-balance` 组的子策略。但是可以使用 `include-other-group` 参数从其他组复制子策略。

### 自定义的权重

可通过 `policy-priority` 参数为子策略设置权重。实现权重条件的方式为对策略的延迟乘以一个系数，以此干涉算法的决策。（如果没有特别的需求无需配置该参数）

举例来说，策略 A 原本延迟为 100ms，当配置为 0.9 时，该策略在算法中将被当作一个延迟为 90ms 的策略进行考量。配置为 1.3 时即为 130 ms。

即 <1 为提高优先级，>1 为降低优先级，默认为 1。

`policy-priority="Premium:0.9"`

第一个参数为对子策略名的正则表达式，第二个参数为系数。可以连续重复配置（但单个策略只会被匹配一次）

`policy-priority="Premium:0.9;SG:1.3"`

如果配置为 0，则表示总是首先使用该策略，失败后再尝试其他策略。（不推荐）

### FAQ

**Q: Smart 策略组的算法引擎具体用了一种算法？**

A: Smart 策略组的算法引擎相当复杂，这里的算法一词并非单指一种具体的算术逻辑，而是类似于 BBR 算法那样，包含了一整套规则、计算方法、数据结构和控制逻辑，同时还包括大量我们工程师多年的经验数据调校。

**Q: Smart 策略组的使用场景是什么？**

A: Smart 策略组的目标是取代原有的所有自动测试组，用户只需要将可用的策略放入该组，剩下的事情完全由 Surge 自动完成。

**Q: 那是否是往 Smart 策略组组中放入越多的策略越好？**

A: 我们的目标是希望能够完全自动的解决这个问题。但是由于设备本身的网络存在不稳定性，如果往组中放入了大量低质量线路，当出现意外的网络波动时，Smart 策略组可能会启用一些次等线路，但其实这只是因为设备本身网络导致的临时问题。（Smart 策略组算法引擎中存在对当前网络质量的考量，但是由于测试当前网络质量存在时间差，所以不一定能获取到准确的信息）这导致需要一定的时间后才能回归到优选线路。

因此推荐在 Smart 策略组组中放入的线路品质应比较相近，可再加上少量次等备用线路。不建议往组中放入过多的几乎不可能被使用的策略。

**Q: Smart 策略组可否用于有地区锁限制的站点的线路自动切换？**

A: 不可以，Surge 无法判断访问的内容是否遭遇了地区锁限制，因此无法进行自动调整。Smart 策略组可以对连接错误、超时、连接卡死等异常做出反应。

**Q: Smart 策略组的策略总是会变化怎么办？**

A: 这是预期行为，Smart 策略组总是会从目前表现最良好的几个策略中随机选取一个进行连接，以此不断监测线路质量。 Smart 策略组会对同一个网站尽量使用相同的策略，因此没有必要太在意策略变化。 即使真的产生了变化，除了个别网站外（通常为金融服务，如 Paypal），大部分网站对 IP 变化并不敏感，没有必要过于担心这个问题而因此放弃 Smart 策略组或设置极大权重。

**Q: 为什么对于同一个域名，Smart 策略组依然会尝试不同的策略连接**

A: 当通过一个代理访问某个域名时，如果该域名的响应速度远低于该代理访问其他网站的速度，则推测该代理对此目标网站不友好，所以在后续连接中会尝试其他线路，在一段时间的数据收集后，最终会收敛稳定到一个策略上。

**Q: 为什么某个代理明明已经故障了，但是界面上还是标记为最常使用**

A: Smart 策略组界面上显示的“最常使用”，指的是最近一段时间内最常被使用的策略，当某个策略突然故障时，虽然它已经不再是首选策略，他可能依然是最近一段时间最常被使用的策略。

### 已知问题

* 在 Smart 策略组中使用 Snell 协议时，reuse 机制将不会生效
* Smart 策略组目前重点考量的是延迟，并不会考量线路的带宽，请保证放入该组的策略的最大带宽都是基本符合需求的，避免选择了低带宽策略影响大数据量传输时的体验。

---
## Guidelines / 故障排除指南

如果你在使用 Surge 时遇到了问题，请参照该文进行故障排除。

在开始前，可以先阅读 [《Surge 官方中文指引：理解 Surge 原理》](https://manual.nssurge.com/book/understanding-surge/cn/) 了解 Surge 的具体工作原理。

在进行仔细排错前，请先尝试重启 Mac 或者 iPhone 试一下是否可以解决问题。如果问题在重启后消失且不再出现，一般属于系统级偶发 Bug，可以忽略。

如果该指南未能成功协助解决问题，请联系 <support@nssurge.com>，请记得附带本指南中所提供的测试命令的输出结果。

{% stepper %}
{% step %}

#### 托管配置问题

请注意，Surge 是一款网络工具，其工作行为取决于配置的设置，如果你的配置来源于服务商或者其他人，如果在安装或更新配置时出现错误，请与配置提供者联系，我们无法提供协助。
{% endstep %}

{% step %}

#### 分析问题来源

Surge 作为一款本地网络转发工具，常见的问题分为两大类：未能成功接管网络请求，和未能成功发出网络。这两类问题的处理方式上有本质的区别。

首先，请打开 Surge Mac 的请求查看器（Dashboard），如果是 Surge iOS 请打开最近请求页面。然后打开浏览器访问任意常见网站，如 <https://bing.com。然后观察请求列表中是否出现了该请求。>

如果你曾经修改过 Surge 的捕获过滤器设置，可能导致请求被隐藏，请务必确认捕获过滤器中没有隐藏测试的请求。

如果请求列表中没有该请求，则说明是接管问题。如果出现了请求，则说明是转发问题。
{% endstep %}

{% step %}

#### 如果未能看见请求 - 接管类问题

{% tabs %}
{% tab title="Surge Mac" %}
Surge Mac 存在系统代理与增强模式（NE VIF）两大接管模式，请先前往总览页面确认这两项是否开启，状态是否正常。其中任意一个开启即可接管浏览器请求。

**确认系统代理**

如果这里显示正常，则可以通过命令行进一步确认，在终端执行 `scutil --proxy` 可以打印当前系统中生效的系统代理设置，如果 Surge 正确设定了系统代理，那么结果应该为：

```
<dictionary> {
  ExcludeSimpleHostnames : 1
  HTTPEnable : 1
  HTTPPort : 6152
  HTTPProxy : 127.0.0.1
  HTTPSEnable : 1
  HTTPSPort : 6152
  HTTPSProxy : 127.0.0.1
}
```

其中 ExcludeSimpleHostnames 字段的值无所谓，如果其他字段的值不一样，则说明 Surge 未能成功设置系统代理，请检查是否有其他同类软件抢占了系统代理设置。

**确认增强模式**

可在系统设置›网络›VPN 设置中，查看 Surge 是否处于开启状态。如果没有，则说明增强模式启动失败，通常你应该在 Surge 的界面上看到明确的错误提示。同时如果有其他 VPN 项目处于开启状态，说明是该程序抢占了系统 VPN 使用权。

也可以通过命令行进行测试，执行 `ping apple.com`，如果成功，且目标 IP 为 `198.18.x.x`，则说明 Surge 增强模式工作正常，可进一步通过 `curl -vvv https://apple.com` 确认。

如果增强模式不正常，在尝试重启无效后，可尝试在 Surge Mac 的更多›设置›系统权限总览中，将网络扩展和 VPN 配置移除。然后重启电脑后重新尝试打开增强模式。
{% endtab %}

{% tab title="Surge iOS" %}
通常来讲，Surge iOS 正常开启的情况下，几乎不会出现接管问题。请尝试重启系统，如果无效的话，请尝试在系统设置中，重置网络设置。如果依然无法出现请求，请联系 <support@nssurge.com>。
{% endtab %}
{% endtabs %}

如果你仅在访问某些域名时，出现接管问题，这通常是配置导致的：

* Surge 配置中的 `skip-proxy` 参数，会使得该参数中的请求，不使用系统代理进行接管，所以如果访问域名出现于该参数中，请删除。
* 在 Surge iOS 或 Surge Mac 增强模式下，如果是访问某个内网 IP 无法被接管，这是正常情况，因为当前网络可能存在范围更小、优先级更高的路由表，系统将直接访问而不会经由 Surge VIF 处理。请务必为该 IP 配置一个域名（本地 DNS 映射）进行访问，以保证请求一定会被 Surge 接管。
  {% endstep %}

{% step %}

#### 如果能看见请求 - 转发类问题

请点击到具体的请求，切换到日志（Notes）标签页，这里记录了该请求失败的具体原因。通常来将一般都是代理服务器故障导致的，一些常见错误如下：

* Connection refused: 代理配置错误或代理服务器故障
* Connection timeout: 代理配置错误或代理服务器故障
* No upstream DNS server: Surge 配置中不存在有效的 DNS 服务器，请调整配置
* No route to host: 代理配置错误或者当前设备没有网络
  {% endstep %}
  {% endstepper %}

---
## Guidelines / tvOS 指南

Apple 于 tvOS 17 中加入了 Network Extension 支持，Surge 终于可以直接运行于 tvOS 中。所有已购买 Surge iOS 的用户均可直接使用，无需额外购买与功能订阅。

在将 tvOS 升级至 17.0 后，可直接从 App Store 安装 Surge tvOS，也可以在加入 TestFlight 后使用测试版本，详见：[Surge iOS TestFlight](/surge-knowledge-base/zh/faq/ios-testflight.md)

### 功能

Surge tvOS 版本与 Surge iOS 版本使用完全一致的核心，即所有 Surge iOS 的功能均可以在 Surge tvOS 版本中使用，包括脚本、WireGuard 等复杂功能。但是部分依赖于 UI 的功能无法使用，如流量统计等。

同时，Surge tvOS 允许作为 Surge Ponte 服务端或客户端使用，正确配置后可以 Apple TV 作为跳板访问内部网络，也可以用于远程控制 Surge tvOS。关于 Surge Ponte 的详情请参考 [Surge Ponte 指引](/surge-knowledge-base/zh/guidelines/ponte.md)。

### 开始使用

请将 Surge iOS 升级到 5.7.0 或以上版本，在更多页面中找到 Surge tvOS 项目，然后按照向导操作。

请注意，Apple TV 所登录的**主账号**必须与 Surge iOS 设备的 **iCloud 账号**一致。

### 配置

由于 Surge tvOS 无法访问 iCloud Drive（tvOS 系统未提供该机制），所有的配置相关操作需由 Surge iOS 进行部署操作进行修改。

请注意由于 Surge iOS 版本无法评估 Apple TV 所在的网络情况，所有在配置 Surge Ponte 服务端时无法像 Surge Mac 那样，对选项的可用性进行检测，请先自行确认所处网络或者所选择的代理是否为 Full Cone NAT。

#### 关于外部资源

与 Surge iOS 不相同的是，Surge tvOS 将在第一次启动时进行外部资源更新，这时部分外置策略组、外置规则可能能为空，并回退至 DIRECT，请查看日志以确认是否有外置资源持续加载失败，如有必要请调整规则与策略保证外置资源可以完成初始化。

也可以通过远程控制器查看当前的远程资源更新情况，并手动进行更新。

### 控制

Surge tvOS 不提供直接的 UI 控制功能，所有控制操作均应通过 Surge iOS 完成，在完成配置部署并开启 Surge tvOS 后，在工具列表的远程控制器设备列表中会自动出现 Apple TV 的项目，可通过 Surge iOS 进行各项控制操作与查看请求和统计结果。

远程控制器通过 Surge Ponte 进行访问，可在任何网络下进行控制，若无需使用 Surge Ponte 穿透功能，可将 Surge Ponte 配置为 LAN-Only，仅供同局域网下远程控制使用。

### 调试

若在使用中出现了问题，可在主界面下按 3 次播放按钮，调出调试菜单，可在菜单中查看日志以分析错误。

---
## License / iOS 授权 FAQ

Surge iOS Pro Personal License 授权供个人永久使用，你可以在你所控制或拥有的最多三台 iOS 设备上同时使用，不可分享给他人。如果你的常用设备数量超过了 3 台，需要购买多份授权。

你可以随意的进行设备激活与反激活，或者重置授权反激活所有设备。

## 授权绑定

Surge iOS Pro 授权有两种绑定形式：绑定在应用内购买支付的 Apple ID 上，和绑定在邮箱地址上。

* 使用应用内购买的授权，绑定在购买的 Apple ID 上。
* 在官网购买的授权，绑定在邮箱地址上。
* 绑定在邮箱上的授权，可脱离 Apple ID 使用，即可以使用任何 Apple ID 去下载或更新 Surge iOS，然后使用邮箱方式激活。
* 使用应用内购买的授权的用户，可以在 App 的授权管理界面进行邮箱绑定。绑定后即可以使用邮箱进行授权恢复，也可以继续使用 Apple ID 进行授权恢复。
* 邮箱绑定完成后会收到授权信息邮件，然后在 Pro 升级界面，点击恢复购买按钮后选择使用邮箱恢复，并输入信息。
* 绑定邮箱后可以在[授权管理页面](https://nssurge.com/account)修改绑定邮箱，修改需通过原邮箱验证。

## 反激活

你随时可以在当前设备上反激活该设备。

如果无法在原设备上操作，且该设备已超过 72 小时未连接互联网，可在[授权管理页面](https://nssurge.com/account)单独反激活该不活跃设备，无需进行完整的授权重置。每个授权每 7 天可执行一次该不活跃设备反激活操作。该频率限制不会影响在原设备上进行的常规反激活操作。

## 重置授权

如果无法进行反激活，可以通过重置授权的方式反激活所有设备：

* 在尝试激活第 4 个设备的时候，会提示是否要反激活所有设备。
* 在[授权管理页面](https://nssurge.com/account)进行重置，以该方式进行重置，会生成新的激活密钥并作废旧密钥。（仅限邮箱绑定的用户）

## 常见问题

### 为什么使用应用内购买恢复购买时，提示找不到已购买项目？

首先请确认使用了正确的 Apple ID，最好的方式是查询收据邮件确认。

另外应用内购买恢复购买时的账号有可能是该 Surge 安装时使用的账号，而非当前 App Store 的登录账户，如果安装账号不正确需删除后重新安装。

### 我的 Apple ID 丢失了，或者状态异常无法登录，可以操作转移授权绑定吗？

由于 Apple 隐私保护限制，开发者无权对 Apple ID / In-App Purchase 进行任何操作，包括且不限于查询、转移、退款等，请联系 Apple 客服处理。

### 我忘了我的邮箱激活码或者一直提示激活信息错误

请注意重置授权后激活码会重置，需要使用最新的激活码。如果忘记了最新的激活码，可前往[授权管理页面](https://nssurge.com/account)重发。

### 在 App 内绑定邮箱时，提示「未知错误」该怎么办？

该错误为 App Store 的一个 Bug，请删除 Surge iOS 后重新安装再进行操作。

### 授权不应该是终生有效吗？为什么授权管理页面中有有效期？

Surge iOS 的授权终身有效，且终身享受维护性更新。同时在购买时自动享有一年期的「功能更新订阅」，可免费解锁购买后一年内的新功能。详见 [Surge iOS 功能订阅更新说明](/surge-knowledge-base/zh/license/ios-fus.md)

## 免费升级至 6 设备授权

Surge iOS 授权限制最多可在 3 设备上使用，其目的是为了防止大面积的账号分享的盗版行为，Surge iOS 授权一直是「个人授权」。但是 3 设备数量的限制对于部分用户确实造成了不便。

为了尽可能的满足用户的合理需求，可将 Surge iOS 授权绑定至 iCloud 账户上，在绑定后可使用的设备数量将免费扩展至 6 设备。

1. 在进行绑定前，必须先绑定邮箱。
2. 可在 Surge iOS 的授权页面进行 iCloud 绑定，绑定过程中需要使用授权邮箱收取验证码。
3. 绑定完成后，除当前设备外的所有设备将被反激活。
4. 在其他设备上，需要使用邮箱激活功能重新激活。(邮箱和激活密钥会自动输入)
5. 激活过程会确认是否为同一 iCloud 账户，如果不同则拒绝激活。
6. 在使用过程中，如果切换/注销了 iCloud 账户，则激活状态会失效。
7. 激活与反激活的各种操作与逻辑和未绑定前一致。
8. 可将已绑定的授权重新恢复至未绑定状态，授权数量降回 3 设备。该操作需要至少在绑定后 24 小时后方可进行。可使用该功能换绑另一 iCloud 账户。
9. iCloud 账号和 App Store 账户相互独立并不相同，该功能和购买账号、当前 App Store 登录账户没有任何关系，请从系统设置的顶部确认当前的 iCloud 账号。
10. 有可能出现 iCloud 数据异常导致即使使用正确的 iCloud 账号也无法激活，可前往[授权管理页面](https://nssurge.com/account)登录重置授权以强行解除 iCloud 绑定后重新绑定。

绑定过程中将通过向用户的 iCloud 存储写入验证密钥的方式验证为同一账户， Surge 不会也不能获取到用户的 iCloud Apple ID。

---
## License / iOS 功能订阅更新

从 Surge iOS 4 开始，Surge iOS 开始使用功能更新订阅制。

## 什么是功能更新订阅？

简单的说，一次购买可以终身使用，但是一年后需要续订才能够解锁新推出的功能，细节如下：

* 首次购买价格不变，依然为 $49.99，购买后享有自购买日起一年时间的功能更新订阅和终身使用权。
* 功能更新订阅续订价格为每年 $14.99 。
* 处于订阅期内，可自动解锁所有新功能。
* 订阅到期之后，依然可以终身使用所有已被解锁的功能。
* 如果不需要最近更新的新功能，可以暂时不续订，等有需要了再续订，一旦续订将解锁所有错过的新功能。

## 如果已经购买过 Surge iOS Pro

作为 Surge iOS Pro 已购用户，你现在可以享受到更多福利：

* 可以永久使用已经解锁的功能。
* 永久免费获得针对已解锁功能的增强更新。
* 永久免费获得针对新设备和新系统的基础适配更新。
* 免费获得一年更新订阅，自购买日期计算。
* 当你对新的功能感兴趣时，再续订你的功能更新订阅，完全可选。

这样的方案对于不准备更新的用户也非常有利，在大版本更新制下，开发者通常会在新版发布后，放弃旧版本的维护。而在功能更新订阅制下，即使不续订，你依然可以：

* 终身使用已解锁的功能，并享受针对这些功能的 Bug 修正和增强性小更新。
* 获得针对新的操作系统和设备的基础兼容性更新，如分辨率适配和处理器架构适配。

## 常见问题

### 怎样的新功能需要更新订阅才可以使用呢？

通常来说只有新的独立功能才需要，一些增强性功能将免费提供给所有用户，举例来说，Surge iOS 3 最近的更新中以下功能算作新的独立功能：

* Remote Dashboard
* Always On
* Snell Proxy
* Ruleset & External Policy Group
* Logical Rule: AND, OR, NOT
* Rule Types: SRC-IP, DEST-PORT

而其余的功能为免费更新

### 怎样查询我的订阅到期时间，以及怎样续费？

可以在 App 内的授权管理页面查看，如果绑定了授权邮箱，也可以前往[授权管理页面](https://nssurge.com/account)查询和续费。

### 怎样取消订阅？

如果是在官网进行的订阅，可以前往[授权管理页面](https://nssurge.com/account)关闭自动续订。如果是从 iOS App Store 进行的订阅，请在 App Store 的订阅管理页面进行管理。

---
## License / Mac 授权 FAQ

### 购买之后可以升级授权数量吗？

可以，在[购买页面](https://nssurge.com/buy_now?upgrade=1)有升级入口可以进行升级，升级后订阅有效期为一年后，需为原有设备补满至同一到期日。

比如当前拥有 1 设备授权，订阅到期日为 200 天后，升级 3 设备授权的费用为：$69.99 - $49.99 + $29.99 / 3 \* (1 − 200 / 365) = $24.5，即差价 $20 + 已拥 1 设备新增 165 天订阅费 $4.5，升级完成后整个授权更新有效期为 365 天后。

由于是以更高档位折扣的订阅价格对原设备进行续订，所以直接购买升级包的价格，会比先续订再升级数量的价格更优惠。

### Surge Mac 授权的有效期是多久？可以持续享受后续更新吗？

Surge Mac 授权终身有效，购买后可在一年内免费获得更新。超过一年后需要续订更新订阅方可获得后续更新，详见：[Surge Mac 维护更新订阅模式说明](/surge-knowledge-base/zh/license/mac-fus.md)

即使不续订，你也可以继续使用维护期内的最后一个版本，永久有效。

### Surge Mac 授权和 iOS 授权有什么关系吗？

Surge Mac 的授权和 iOS 版本完全独立，没有关系。

### 多设备的 Surge Mac 授权的密钥会有多个吗？

多设备授权的密钥只有一个，该密钥可激活多个设备。

### 可以将 Surge Mac 的授权名额转让给其他人吗？

Surge Mac 的授权，允许将自己的配额给自己的朋友或家人使用，但是禁止进行分销转售，一旦发现进行转售将会封禁授权。

### 怎样管理授权激活了哪些设备？

每个授权可以自由的激活数量限制内的设备。

1. 已激活的设备可以终生无限制的使用。
2. 如果已到达数量限制，激活新设备前需要先反激活旧设备，反激活操作只可以在原先的设备上进行。（设置 › 授权 › 反激活）
3. 如果无法在原设备上操作（如设备丢失或维修），且该设备已超过 72 小时未连接互联网，可在[授权管理页面](https://nssurge.com/account)单独反激活该不活跃设备，无需进行完整的授权重置。每个授权每 7 天可执行一次该不活跃设备反激活操作。
4. 不活跃设备反激活的频率限制不会影响在原设备上进行的常规反激活操作。
5. 如需反激活授权下所有设备，可以在官网账号管理中进行 Reset，并重新生成新的激活码，该操作每 3 天可执行一次。

### 为什么提示我的授权码不正确？

1. 首先请先确认你的授权码是否为对应产品的授权码，Surge iOS 的授权码无法供 Surge Mac 使用。
2. 然后请注意授权版本与软件版本是否一致，在激活时若版本不一致会给与提示。
3. 最后请注意，在执行 Reset 操作后，原来的激活码会作废并发送新的激活码至邮箱。如果忘记了最新的授权 Key，可前往[授权管理页面](https://nssurge.com/account)重发。
4. 如果失去了原授权邮箱的访问权，请填写该表格：[Surge License Retrieve](https://goo.gl/forms/lYmbWMBXrqh0NSPs1)
5. 如果曾修改过授权邮箱，请记得使用修改过后的邮箱进行激活。

如果出现了其他问题，请联系 <support@nssurge.com> 并附带错误提示截图。

---
## License / Mac 维护更新订阅

***

## 为何采用维护更新订阅

* **及时交付新功能**\
  大版本付费模式往往促使开发者将功能“囤积”至下一次付费升级再行发布，造成更新周期延长。维护更新订阅允许功能一经完成即刻发布，确保用户第一时间就能使用到新特性。
* **成本可预期**\
  用户每年仅需一次固定支出即可持续获得最新版本，而无需纠结下次大版本的时点与价格。
* **保留永久使用权**\
  与纯订阅软件不同，Surge Mac 仍提供永久授权：订阅到期后，用户可无限期使用到期日前获得的最后一个版本。
* **高灵活性** 你可以根据对新特性的需求决定是否立刻进行续订，如果对新的功能没有需求，那么可以暂缓订阅，等到对新功能有需求时再进行续订。

## 首次购买与订阅权益

| 授权设备数 | 首次购买价格（含 12 个月维护更新订阅） |
| ----- | --------------------- |
| 1 台   | US $49.99             |
| 3 台   | US $69.99             |
| 5 台   | US $99.99             |

* 首次购买即获得完整功能及 12 个月维护更新订阅。
* 订阅期内发布的任何更新均可免费升级。
* 订阅结束后，仍可继续使用到期日前发布的最终版本。

## 续订与授权升级

### 续订价格

| 授权设备数 | 维护更新订阅续费（12 个月） |
| ----- | --------------- |
| 1 台   | US $19.99       |
| 3 台   | US $29.99       |
| 5 台   | US $45.99       |

* 续订不改变当前授权设备数量。
* 若需增加设备，可购买升级包；系统根据剩余订阅天数自动补差价并统一到期日。

比如当前拥有 1 设备授权，订阅到期日为 200 天后，升级 3 设备授权的费用为`$69.99 - $49.99 + $29.99 / 3 * (1 − 200 / 365) = $24.5`，即差价 `$20 + 已拥 1 设备新增 165 天订阅费 $4.5`，升级完成后整个授权更新有效期为 365 天后。

由于是以更高档位折扣的订阅价格对原设备进行续订，所以直接购买升级包的价格，会比先续订再升级数量的价格更优惠。

## 试用政策

每年您都可以进行一次 7 天免费试用，以便在无续订情况下体验新版本特性。

## 常见问题

#### 我必须要在订阅期内升级到最新版本才能够一直使用最后版本吗？

不需要，即使订阅已过期，也可以随时更新到过期前发布的最后一个版本。

#### 维护更新订阅是 Surge 自创的吗？

维护更新订阅并非 Surge 自创，早已被很多软件所使用，已经是一种成熟的软件授权模式，以 macOS 为例，TablePlus、ForkLift、Sketch、Tower、Kaleidoscope 等软件均使用维护更新订阅模式。Windows 平台下同样也有很多软件使用该模式。

#### 我怎样知道有什么新功能：

我们新上线了更新日志的网页版本，与更新系统同步更新：<https://nssurge.com/support/mac/release-notes>，可在这里查看所有版本的更新内容与发布时间。

当有新的版本时，如果订阅已经过期，将在主界面的事件列表中进行弱提示，可点击查看。如果不想收到此消息，可以点击后选择暂停检测的时间，或者永久关闭提示。

#### 如果在订阅期结束前的最后一个版本，遇到了严重 Bug 该怎么办，只能续订吗？

如果出现了非常严重的 Bug，我们在收到报告后会立刻发布新版本，且新版本的解锁时间将与有问题的版本一致，确保不影响正常使用。

但是请注意，对最新 macOS 的适配性更新不属于这项承诺，通常随着系统更新，我们需要耗费大量的时间与精力去进行适配（比如为了解决与 macOS Sequoia 的兼容性问题，我们使用 Network Extension 重写了整个增强模式的实现。），这本身也是更新维护更新订阅的意义。

---
## License / 购买前常见问题

### Surge 是怎样一款软件？

Surge 是面向专业技术人员的一款网络工具集软件，功能主要包含对网络请求的接管、修改和转发，可先阅读在线手册以理解 Surge 的用途。

[在线手册](https://manual.nssurge.com)

[官方中文指引：理解 Surge 原理](https://manual.nssurge.com/book/understanding-surge/cn/)

### Surge 是 VPN 吗？

请注意，虽然 Surge 有转发请求的能力，但是 Surge 并不提供任何 VPN 或代理服务，Surge 是一款面向技术人员的纯工具类型软件。

### Surge iOS 和 Mac 是什么关系？

Surge iOS 和 Surge Mac 分别用于 iOS 设备和 Mac 设备。Surge iOS 可以使用远程控制器功能远程管理 Surge Mac 和查看 Surge Mac 的请求。Surge Mac 的 Dashboard 可以通过网络或者 USB 连接查看 Surge iOS 的请求。

Surge tvOS 为 Surge iOS 的附属品，免费提供给 Surge iOS 用户使用。与 Surge Mac 版本授权没有关联。

### Surge iOS 和 Mac 需要分别购买吗？

是的，两者的授权独立销售，需要分别购买。

### Surge Mac 授权形式是怎样的，有效期是多久？

Surge Mac 的授权终身有效，可享受在购买的大版本内的免费更新。我们通常每两年进行一次大版本更新，大版本更新后，已购买用户可以以优惠价格进行升级，也可以继续使用旧版本。

不用担心临近大版本更新日期时，购买可能不划算的问题，升级费用采用和购买时间相关的阶梯制，一般近半年内购买的用户都可以享受免费升级。

### Surge iOS 授权形式是怎样的，有效期是多久？

Surge iOS 的授权终身有效，且终身享受维护性更新。同时在购买时自动享有一年期的「功能更新订阅」，可免费解锁购买后一年内的新功能。详见 [Surge iOS 功能订阅更新说明](/surge-knowledge-base/zh/license/ios-fus.md)

### 可以试用吗？

Surge Mac 提供 14 天的全功能免费试用。Surge iOS 提供 7 天全功能免费试用，部分功能无限期免费试用。

### 授权可以用于多少台设备上？

Surge iOS 授权可以用于自己拥有的最多不超过 3 台的设备上，Surge Mac 的授权数量在购买时确定。

Surge tvOS 授权可以用于自己拥有的 Apple TV 设备上，不设具体数量限制，但是若出现明显滥用行为将导致授权封禁。

### 更换了设备怎么办？

可以在更换设备前反激活该设备以释放授权配额。如果无法在原设备上操作，且该设备已超过 72 小时未连接互联网，也可以在[授权管理页面](https://nssurge.com/account)单独反激活该不活跃设备，无需重置授权；每个授权每 7 天可执行一次该操作。也可以重置授权以反激活所有设备，详见：

* [Surge iOS 授权相关问题](/surge-knowledge-base/zh/license/ios-faq.md)
* [Surge Mac 授权相关问题](/surge-knowledge-base/zh/license/mac-faq.md)

### 为什么在 App Store 里找不到 Surge？

* Surge Mac：由于 Surge Mac 使用的技术不适用与 Mac App Store，故不可从 Mac App Store 安装，请从官网下载安装。
* Surge iOS/tvOS：由于中国区禁止所有与 VPN 有关的 App 上架，故 Surge iOS 无法在中国区上架，其他区域不受影响。

---
## Release Notes / Snell 协议更新

Snell is a lean encrypted proxy protocol developed by our team. Here are some highlights:

* Extreme performance.
* Support UDP over TCP relay.
* Single binary with zero dependencies. (except glibc)
* A wizard to help you start.
* Proxy server will report remote errors to the client if an error encounters. Clients may choose countermeasures for different scenarios.

> The Snell protocol is intended for Surge users only. Please do not reverse-analyze the protocol and make a compatible client of it. We want to keep the user base as small as possible; thanks for your understanding.

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v5.0.1-linux-armv7l.zip
```

{% endcode %}

## Release Notes

### v6.0.0 Beta

#### RC 更新

* 修复开始转发时，最初几个 UDP 数据包可能被截断的问题。

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v6.0.0rc-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v6.0.0rc-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v6.0.0rc-linux-aarch64.zip
```

{% endcode %}

#### RC2 更新

* 当 `ipv6=false` 且客户端明确访问 IPv6 地址时，返回更清晰的错误信息。

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v6.0.0rc2-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v6.0.0rc2-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v6.0.0rc2-linux-aarch64.zip
```

{% endcode %}

### v5.0.1

* 修正了一处因断言低概率出现的崩溃问题

### v5.0.0

#### Dynamic Record Sizing

该特性将提高在存在丢包的网络环境下延迟表现。技术细节可参考 ：[Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

Snell v5 加入了专为 QUIC 流量设计的 QUIC Proxy 模式，该模式工作属于 UDP over UDP，以避免 TCP over UDP 问题。（服务端需开放 UDP 端口）

* 该工作模式为 QUIC 进行了特殊优化，仅当 Surge 识别到 QUIC 流量时会启用，其他 UDP 流量依然使用 UDP over TCP 模式。
* QUIC Proxy 只会对 QUIC Handshake 数据包进行强加密，以保护 SNI 和目标主机名，同时进行鉴权。后续的所有 QUIC 数据包，由于本身已经被 QUIC 强加密，将直接以裸包进行转发，大幅降低了不必要的加解密开销。同时由于未引入额外字节，不会影响 QUIC 的 PMTU 探测。

#### 出口控制

* 支持配置 `egress-interface` 参数控制出口 interface（需要 root 权限或者给予`CAP_NET_RAW/CAP_NET_ADMIN` 授权，同时该 interface 上需要有目标地址和 DNS 的路由表）
* 支持 systemd 的 Socket Activation 机制，可用于配置 network namespace，也可用于出口 interface 配置。我们会在之后提供配置样例。

Snell v5 的服务端可以向下兼容 v4 客户端，如果不想使用 QUIC Proxy Mode 功能，客户端设置为 v4 版本即可，Dynamic Record Sizing 的优化只和服务端有关。

### v4.1.1

* Fix a potential crash that may occur during UDP forwarding.

{% code overflow="wrap" %}

```markdown
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-amd64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-i386.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-aarch64.zip
https://dl.nssurge.com/snell/snell-server-v4.1.1-linux-armv7l.zip
```

{% endcode %}

### v4.1.0

* Add a dns parameter for customizing DNS server addresses, supporting multiple address configurations.
* Update the DNS library c-ares to the latest version to resolve compatibility issues with specific DNS records.
* Add output of the currently used DNS server at startup.
* Adjust log output to lower broken pipe error messages to verbose level.
* Update libuv to v1.48.0 to fix potential crashes when accessing IPv6 addresses on certain systems.
* Improve log information for DNS errors.
* Fix an issue where certain invalid DNS records could cause a crash.

### v4.0.1

Fixed a bug that UDP packets can't be forwarded to IPv6 addresses.

## Surge Mac as Snell Proxy Server

You may also use Surge Mac as a Snell proxy server (Starting from version 3.1.0). Add the following lines to your profile.

```
[Snell Server]
interface = 0.0.0.0
port = 6160
psk = RANDOM_KEY_HERE
```

The embedded Snell server in Surge uses the Snell V1 protocol.

---
## Release Notes / Surge iOS 更新日志

### 版本 5.14.6

* 新增 \[General] 参数 `block-quic`，该参数用于全局覆盖是否阻止 QUIC 流量的行为
* 优化请求查看器中的文本与 JSON 浏览器，支持大文件与代码高亮
* 重写 HTTP 脚本相关实现，现在在处理大型 Body 时性能更好且内存占用更低
* 支持 gQUIC 的 SNI 提取
* 重构流量统计功能，现在即使长期未进主程序，也不会在进入流量统计页面时需要长时间等待了
* 流量统计新增导出功能
* 其他细节优化与问题修正

### 版本 5.14.5

* 支持 DNS over TLS。
* 修复错误和性能改进。

### 版本 5.14.4

* 启用 HTTP 捕获开关时，所有活动连接现在将被强制中断，以确保不会由于现有长连接而漏请求。
* 优化了与某些 QUIC 客户端（如 Lark）的兼容性。
* 修复了在使用脚本或其他机制修改请求 HTTP 后，统计中的下载数据字节数不正确的问题。
* 调整了转发 QUIC 时的处理逻辑优先级。现在，对于不支持 UDP 转发的代理策略，将优先考虑 QUIC Block，然后才会回退到 DIRECT 或 REJECT。
* 修复错误和其他改进。

### 版本 5.14.3

#### 新功能：端口转发

* 该功能常用于开发和调试场景，例如使用 SSH 连接到 MariaDB 等服务器。

#### #!需求 升级

* 现在提供了三个简单的表示法：#!IOS-ONLY、#!MACOS-ONLY 和 #!TVOS-ONLY。
* 由该行尾注释禁用的内容现在可以在 UI 中显示和编辑。当条件不满足时，将显示为禁用状态，并且如果启用了，将自动移除限制。

#### \[Host] 优化

* \[Host] 部分支持使用 DOMAIN-SET 和 RULE-SET 进行配置，以提高匹配效率。使用实例：

#### 其他改进

* 添加了 icmp-forwarding 选项，默认启用。
* 优化使用智能策略组作为基础代理。现在在这种使用场景中，可以充分利用智能策略组的特性。
* 修复错误和其他改进。

### 版本 5.14.2

* 修复错误和其他改进。

### 版本 5.14.1

* 修复错误和其他改进。

### 版本 5.14.0

#### 新功能

* 添加了低开销请求拒绝的预匹配规则。详情请参阅文档。<https://manual.nssurge.com/policy/reject.html>
* Body Rewrite 支持使用 JQ 表达式操作 JSON。
* shadowsocks 协议新增支持 `2022-blake3-aes-256-gcm` 和 `2022-blake3-aes-128-gcm` 加密模式。
* 针对 iOS 18 的图标模式进行了适配。
* 新增用于 HTTP 捕获的控制中心控件。
* DNS 现在支持系统搜索域设置。
* 增加参数 proxy-restricted-to-lan，以限制代理仅接受来自同一子网的设备。
* 在更新外部资源时，将记录并发送 ETag；如果资源未更改，则不会触发重新下载。

#### 改进

* 全面优化和改进 UDP 转发性能。
* 策略组列表视图支持配置自定义图标。
* 解决了 iOS 18 上实时显示的问题。
* 优化策略组图标的显示效果。
* 提高 HTTP 引擎对非标准请求的兼容性。
* 当 Surge 无网络连接激活时，提供更明确的错误提示信息。
* 优化加密 DNS 的错误处理逻辑，在遇到错误时立即重试。
* 对于过多 \[Host] 条目添加警告消息。
* URL 正则表达式规则现在支持 `extended-matching` 标签。
* 允许使用 Ponte 策略作为底层代理。

#### Bug 修复

* 修复了即使 Surge 已关闭，控制中心/主屏幕小组件仍会显示为活动状态的问题。
* 修复了在某些错误情况下，加密 DNS 出现内存泄漏的问题。
* 更正新图标订阅周期约束错误。
* 其他 bug 修复。

### 版本 5.13.0

* 控制中心小组件：在 iOS 18 上，您现在可以在控制中心快速开关 Surge
* 新图标：Sapphire（蓝宝石）
* 添加 Ponte 诊断功能，用于快速定位与 Ponte 相关的问题，可从 Ponte 设备页面访问。
* 端口跳跃：Hysteria2 和 TUIC 协议现在支持端口跳跃，以改善 ISP 的 UDP QoS 问题。详情请参阅服务器文档
* 添加 `[General]` 参数 `show-error-page`，用于控制是否在发生错误时显示 Surge 的 HTTP 错误页面。此参数默认启用，其行为与以前的版本一致
* 其他问题修正

### 版本 5.12.0

* 新的订阅功能：自定义策略组图标
* 使用 CloudKit 重构 Surge tvOS 配置部署流程，稳定性得到大幅提升。请注意需要将 iOS 和 tvOS 都升级至最新版本后才可以使用配置部署功能，且 tvOS 版本需要先启动一次完成注册
* 在请求列表里使用增加规则功能时，可以选择加入已存在的规则集。（支持本地规则文件和 inline 规则集）
* 模块支持配置 client-source-address 参数
* 修正导出 HAR 时的一些问题
* UI 恢复兼容模式（接管模式）设置并增加详细描述
* 优化 No Default Route 模式下开启 IPv6 VIF 时的行为
* 修正 UI 编辑规则时的一些细节问题，如开启状态和注释
* 优化在外部资源页面查看巨型资源时的表现
* 其他细节优化与问题修正

### 版本 5.11.3

* 支持在始终开启开关打开的情况下，通过小组件/控制中心/捷径关闭 Surge
* 支持在 Surge VPN Profile 未被选中的情况下（其他 VPN 运行时），通过小组件/控制中心/捷径开启 Surge
* 修正规则集中包含重复的 DOMAIN 与 DOMAIN-SUFFIX 规则时，可能导致 DOMAIN-SUFFIX 失效的问题
* No Default Route 模式相关优化，大幅提高可用性
* 其他问题修正

### 版本 5.11.2

* 新的订阅功能：规则分析，目前包含两个子功能：
  1. 规则使用计数，会记录规则的匹配次数。（只统计主规则集中的条目，各类规则集和逻辑规则的子规则不会被统计，统计时会忽略规则参数）
  2. 当前规则集性能测试
* 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
* Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
* 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
* 新增规则类型 HOSTNAME-TYPE，用于判断请求的主机名的类型，可选值有：IPv4, IPv6, DOMAIN, SIMPLE。（SIMPLE 指的是不包含 . 的主机名，如 localhost）
* 优化了 DNS 的请求日志，现在会显示更多的信息，且在规则系统未触发 DNS 时，如果是 DIRECT 策略直连也可以显示 DNS 的相关日志了
* 在删除策略时，如果该策略被策略组所使用，现在允许直接删除并将自动从所有策略组移除
* 建立 Subnet 策略组时，现在可以使用 Subnet 表达式的编辑向导
* 修正规则集索引建立过程可能是会阻塞 UI 的问题
* 优化了请求详情页的 IP 地址展示
* 编辑策略组时不再可以将自身作为子策略加入

### 版本 5.11.1

* 优化小型规则集的匹配性能，在旧型号 CPU 上效果尤为明显
* 外置资源更新页面可以显示规则集处理产生的错误信息
* 自动忽略规则集中的无效空行
* 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题
* 修正当外部策略组产生变化时，可能导致的崩溃
* 修正配置升级功能未能对托管配置和企业配置正确生效的问题
* 在 Smart 组初始化阶段，不再显示最常使用标签，以避免产生误解
* 修正本地脚本文件被编辑后无法被自动重载的问题
* 优化大型规则集的索引流程
* 限制 iCloud 后台自动同步的最大文件数量为 200，避免产生内存占用问题
* 修正通过远程控制器调整策略时，UI 可能显示不正确的问题

### 版本 5.11.0

#### Smart Group

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（url/load-balance/fallback），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

详情请见：<https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group>

#### 规则系统

* 规则系统整体性能优化。
* 大幅优化大型域名规则集中的索引算法，对于十万条以上的规则集，检索效率提高了十倍以上。
* 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题
* 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 \* 匹配域名
* DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题

#### IPv6

* ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
* 为 ipv6-vif=always 参数增加了警告
* 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）

#### 其他优化

* $notification.post 增强，新增媒体资源支持、声音提示和自动消除。
* 优化 WireGuard 失败处理
* 降低 TUIC 协议在休眠时对电量的消耗
* 请求日志系统时间统计精度提高，现在可精确到 µs 级
* 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
* 优化外部资源的缓存系统
* 新增配置文件行命令 #!REQUIREMENT
* 在发现当前网络由 Surge Mac Gateway 所接管时，现在将自动暂停 Surge iOS。（可通过 auto-suspend 选项调整行为，默认开启）
* 优化 TUN 接管和特定 app 的性能兼容性问题
* 优化了内存占用，不常用和巨大的脚本现在将不会被缓存至内存
* 网络诊断页新增 SSID/BSSID，增加复制功能
* 现在在日志界面执行日志上传时，将自动为当前运行的引擎生成最近的 verbose 日志（新版本在内存缓存了 256KB 的日志），这样在汇报问题时，直接执行上传即可，无需再使用 verbose 模式复现。
* 对于策略组与脚本类型的外部资源，现在限制最大大小为 2MB，避免当错误配置时，导致的内存超限。

#### 细节调整

* 提高内存警告的阈值到 45MB，原为 40MB。
* 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
* 默认 UDP 测试目标改为 1.0.0.1
* 在脚本中使用 API 时如果传入了错误类型的字段，将产生脚本异常
* 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

#### 问题修正

* 修正在 Surge iOS 主程序和引擎都开启时，iCloud 内容发生变化可能无法被主程序所检测的问题
* 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
* 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
* 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

### 版本 5.10.0

#### 新功能

* 新的订阅功能：Body Rewrite。Surge 现在可以重写 HTTP 请求或响应的 Body，用正则表达式替换原始内容。如果你需要进行更灵活的修改，请使用脚本。

#### 改进

* Mock (Map Local) 功能全面强化，- 新增 text, tiny-gif, base64 等数据类型，以便于 inline 直接返回数据。同时增加了 status code 自定义。
* 请求列表过滤器优化，现在将把过滤器显示于顶部，并快速切换过滤器是否启用，长按过滤器项目可以显示菜单，可删除或反转该项目为负过滤器。
* 新增对 STUN 数据包的识别，可用 PROTOCOL,STUN 进行匹配。
* 优化外置资源管理页面
* 优化脚本编辑器页面
* 优化模块管理页面
* 新增 Utilites 标签页的长按快捷菜单
* iOS 版本新增 URL scheme: surge:///install-module?url=…

#### 优化

* 配置 Shortcuts 执行 Surge 脚本时可直接读取当前配置的脚本列表
* 增强了 HTTP Body 解压时的兼容性
* 优化脚本引擎，限制 JSC 引擎并发处理数为 2 以避免内存问题
* GeoIP 数据库由主应用更新后不再需要重启即可生效
* 优化了请求记录，现在将显示匹配到的 URL Rewrite 和 Header Rewrite 的具体规则
* 调整了 DNS 引擎处理空结果的逻辑，现在在配置了多个 DNS 服务器的时候，也不再等待所有服务器响应空结果，以避免在 AAAA 记录不存在时产生额外等待。
* 模块页面允许撤销修改以避免误操作导致生效顺序修改

#### 修正

* 修正了在使用覆盖策略组后，显示策略组的延迟依然是覆盖前的选项的结果
* 修正在 iPad 上长按过滤器会导致崩溃的问题
* 修正因模块配置而产生的警告信息不会显示的问题
* 修正在脚本中传入一些错误类型的参数会导致 Surge 崩溃的问题
* 修正与新版 Safari 的非 https WebSocket 在代理模式下的兼容性问题
* 修正在规则搜索页删除条目时，会将重复条目全部删除的问题
* 修正编辑器高亮的一些缺失

### 版本 5.9.0

#### 模块系统

* 新增数个官方模块，现在官方模块可以动态更新了。
* 模块新增分类字段，用于在 UI 上便捷访问与归类。
* 模块新增参数表传入，支持传入多个参数，参数将用以文本替换的形式对模块内容进行修改。

#### 脚本系统

* 全新的脚本执行引擎。优化了执行性能和内存占用。
* $httpClient 新增了多个实用参数。 以上更新详见文档。

#### 增强

* 新增远程控制器的桌面快捷跳转，详见设备页面底部的配置向导。
* 新参数：always-raw-tcp-keywords，使用方式详见文档。
* 新增规则 SRC-PORT 用于匹配客户端端口号。
* IN-PORT/SRC-PORT/DEST-PORT 三个规则统归为端口号规则类，支持更多用法。
* 现在 UI 编辑后可以保持原配置中的纯空行了。

#### 修正

* 修正 QUIC 流控的一个细节问题，优化了 Ponte/TUIC/Hysteria2 协议的延迟表现。
* 编辑单条规则后，notification 相关参数将会保留。
* 修正新版 iOS 下无法通过小组件切换出站模式的问题。
* 修正在处理巨型的外部资源时，有可能会出现突发的内存超限导致停止。

### 版本 5.8.1

#### 规则引擎优化

RULE-SET 与 DOMAIN-SET 的实现完全重写，现在 Surge 会在资源更新时自动对规则集进行预处理，建立索引数据结构，大幅提高匹配速度。

1. RULE-SET 和 DOMAIN-SET 两种类型规则集不再有性能和内存占用区别，可以随意使用。
2. DOMAIN-SET 规则集不再存在不可以使用 eTLD 的限制。
3. RULE-SET 中的 DOMAIN, DOMAIN-SUFFIX, IP-CIDR, IP-CIDR6 规则匹配速度得到大幅提升。
   * 十万条左右的 DOMAIN/DOMAIN-SUFFIX 规则集，在旧版中单次匹配需要 100ms，现在只需要个位数 ms。
   * 一万条左右的 IP-CIDR 规则集，在旧版中单次匹配需要约 0.1ms。新版只需要0.0002ms，提升了约 500 倍。IP-CIDR6 规则的性能提升幅度更高。
4. 在新版本中，自行通过 IP-CIDR 规则集构建出地区的 IP 地址集合，与直接使用内部的 GEOIP 规则的性能已经完全一致。
5. 先前版本加入的 Inline Ruleset 无法享受该优化，但是在百条数量级下几乎无差异。
6. 先前版本中，Ruleset 中的规则也是按照从上至下的方式逐条匹配，如果规则集中同时包含了需要 DNS 解析的规则，也只有当开始匹配该子规则时才会触发 DNS。新版本中，只要规则集中包含任意一条需要 DNS 解析的规则，在测试该规则集前就会先进行 DNS 解析。（绝大多数情况下没有任何区别）

* 主规则匹配效率小幅优化。
* IP-CIDR6 规则在非索引情况下的效率也得到大幅提升。
* RULE-SET 规则可直接配置参数 no-resolve 和 extended-matching，均等价于为所有子规则配置了该参数。
* DOMAIN-SET 规则集也支持配置 extended-matching。

#### Minor Optimizations

* MITM 时发送签名所使用的证书（证书链），以支持使用 intermediate 证书作为签发证书。
* 行首与行末注释，现在可以随意使用 `#` `//` `;` 等三种常见写法
* 配置文件错误消息提示优化，现在它可以更准确地给出发生错误的确切行号。
* 修复了 BSSID 相关匹配规则可能会失败的问题。
* 优化 Surge Ponte 错误处理流程，修正某些错误下不会自动更新设备信息的问题
* Bug 修正。

### 版本 5.8.0

#### 新功能

* 新的 Inky 图标
* 协议嗅探

  发往 80 与 443 端口的请求，会等待客户端发送第一个数据包后，提取 SNI 等信息用于规则系统判断。

  * `DOMAIN`、`DOMAIN-SUFFIX`、`DOMAIN-KEYWORD` 规则新增可选参数 `extended-matching`。开启该参数后，该规则将同时尝试匹配 SNI 和 HTTP Host Header （或 :authority）中的字段。
  * 新增参数 `always-raw-tcp-hosts`，用于强行关闭对特定主机名的主动协议探测。
* 新代理协议支持：Hysteria 2

  Hysteria 2 是一个为不稳定和容易丢包的网络环境所优化的代理协议，基于 UDP/QUIC。
* 自动 QUIC 阻止

  由于大部分代理协议并不适合用于转发 QUIC 流量，现在 Surge 会自动阻止 QUIC 流量使其回退 HTTPS/TCP 协议，以保证性能，对于命中了 MITM 主机名的 QUIC 流量，同样将自动拒绝。
* QUIC 类协议的 ECN (Explicit Congestion Notification) 支持

  显著改善了 Vector(Surge Ponte)/TUIC/Hysteria 2 协议的性能表现。

#### 优化

* HTTP 捕获功能重做
  * 相关设置不再存放于配置中，`[Replica]` 段已废弃。
  * 新增开启捕获开关后的自动关闭设置，可根据时间、大小、请求数自动停止抓取。
  * 新增 MITM 自动开启，开启捕获开关后可对特定主机名额外开启 MITM。（即使 MITM 主开关未开启）。
  * 新增在开启捕获开关后，只保存 HTTP/HTTPS 请求的选项。
* VIF 性能优化，经测试可在 iPhone 15 Pro 下以 VIF 接管单线程达到 2.5Gbps 有线网卡满速。（代理模式性能更佳）
* Wi-Fi Assist 和 Hybrid 功能将只在设备解锁后生效，避免造成不必要的电量与流量消耗。
* 该版本中开始限制外部资源大小为不超过 10MB，避免异常的外部资源导致内存超限。（domain-set 除外）
* `udp-policy-not-supported-behaviour`、`include-apns`、`include-cellular-services` 参数加入了 UI 设置。
* 优化了对一些非标准协议的兼容性。
* 对 Ponte 策略进行测试时，测试 URL 由 proxy-test-url 改为 internet-test-url。
* 根据 WireGuard 协议标准推荐，现在 WireGuard 的握手数据包将打上 0x88 (AF41) 的 DSCP 标记以增加成功率。
* 通过 WireGuard 转发 UDP 数据包时，支持 tunnel 内数据包保留 TOS(DSCP/ECN) 标记了。
* 根据 WireGuard 协议标准推荐，Surge 将复制 tunnel 内数据包的 ECN 标记到 tunnel 外数据包上。收到含有 ECN 标记的数据包时，将严格按照 RFC6040 进行合并处理。（需要为策略配置 `ecn=true`）
* UDP NAT 支持根据 ICMP 消息提前关闭 UDP 会话。
* 完善了 QUIC 的 PMTU 支持。

#### 问题修正

* 修正规则集的外部资源更新后需要重新才能生效的问题。
* 在网络切换后将强制打断原有的 DoH/DoQ/DoH3 长连接，避免获取到不适合当前网络环境的结果。
* 修正无效的证书可能导致密钥库界面崩溃的问题。
* 修正策略组页面的 Ponte 设备选项可能不显示文字的问题。
* 在对使用 IP 地址直连的 HTTPS 请求进行 MITM 时，不应将 IP 地址作为 SNI 发送，这可能导致出现兼容性问题。
* 其他问题修正。

### 版本 5.7.0

#### 新功能

* Surge tvOS 现已可以使用，所有 Surge iOS 已购用户均可直接使用，无需额外付费
* 支持 iOS 17 的可交互小组件
* 新增请求的 Header 与 Body 全文搜索支持
* Web Dashboard 更新至 2.0 版本
* 新增功能 Inline Ruleset，可将 Ruleset 直接写于主配置中

#### 细节优化

* 优化脚本日志系统，确保并发执行时请求日志中的脚本日志不会显示其他会话的内容
* 拆分开启与关闭的 iOS 17 的捷径动作，iOS 17 版本用户请使用使用 (iOS 17) 后缀的动作
* 取消了 Wi-Fi Assist 的提示通知
* 使用 UI 编辑策略组时可以选择 Ponte 设备了
* 为远程设备创建临时规则时，可以选择 Ponte 设备了
* 远程控制器支持查看与更新远程设备的外部资源，支持 Surge Mac 与 Surge tvOS
* Ponte 设备的图标可以显示设备类型了
* 优化了无障碍访问相关的细节
* 优化了一些 UI 细节

#### 问题修正

* 修正 MITM Hostname 列表编辑时可能出现的一些问题
* 修正为远程设备创建规则时，策略选项有可能是本地的策略而非远端策略的问题
* 修正了当使用 iCloud 同步时，当缓存被清除时可能导致本地模块的勾选被取消的问题
* 修正了无法切换到 Dropbox 同步的问题
* 修正了部分卡片背景在展开时背景不完整的问题
* 修正了使用 Basic Auth URL 添加的模块，无法自动更新的问题
* 修正快速切换模式下，从 IPv6 网络切换至非 IPv6 网络后，v6-vif 为 auto 时未能正确自动关闭 v6 vif 的问题

### 版本 5.6.0

#### 细节增强

* 请求列表页面全面优化
* 可以在 iOS 端直接发起和管理 Ponte 设备共享了
* 查看外部请求时将显示来源设备名
* 分离配置支持使用 作为关键字引用企业配置中的内容
* 配置列表新增 Create Linked Profile 选项，用于快速创建分离配置
* 性能优化
* 修改了访问数据保护区的逻辑，现在 Surge 在锁屏状态下也可以正常被开启。（重启手机后除外）
* 当检查到 CA 证书过期时给予提示
* 单个请求导出的 .zip 文件支持导入回 Surge iOS，将显示在收藏请求中

#### 问题修正

* 修正在同一轮策略测试中，如果混用不同的测试 URL，在二次测试时构造的 HTTP Header 可能不正确导致测试结果异常的问题
* 修正从后台打开主程序后，Panel 刷新可能无法正确被执行的问题。
* 修正列表策略组视图下，策略组标题选项有可能更新不及时的问题。
* 修正使用 DIRECT 策略作为 underlying\* proxy 时，有可能导致 UDP 失败的问题
* 修正使用 SSH 协议时，如果服务端配置了 banner 无法正确握手的问题。
* 修正 iPad 下 Lucid 主题可能出现的一些问题。
* 修正部分情况下 SSID 相关功能无法正确工作的问题。
* 修正当使用 TUIC v5 作为 underlying-proxy 时可能出现的一些问题。
* 修正当直接使用 IPv6 地址作为 vmess 主机名时，如果开启 WebSocket 会无法正确构造 WebSocket 请求的问题。
* 修正当 DOMAIN-SET 规则使用了特定的无效数据会导致崩溃的问题
* 修正配置错误可能导致的崩溃
* 修正了重放的请求返回数据如果存在压缩则无法查看的问题
* 修正云通知界面提示错误的问题
* 修正只有共享的 Ponte 设备时无法载入设备列表的问题
* 修正 DNS over HTTP3 可能出现的一些崩溃
* 修正 Surge Ponte 在子网 CIDR 不为 8 的整数倍时，会错误判断导致不使用局域网直连的问题
* 修正使用 Surge Ponte 时可能出现的一些问题
* 优化 TUIC/Ponte 在网络切换后重建主连接的逻辑

### 版本 5.5.1

#### 远程控制器全面优化

* 支持远程增加与修改临时规则
* 设备管理器默认分组为活跃和非活跃设备（是否有请求）
* 支持为设备直接增加临时或永久规则
* 其他细节优化

#### 其他

* 新增 TUIC v5 协议支持。
* 策略组菜单新增显示隐藏的策略组选项。
* 流量统计中，apple.com 的子域名将拆分处理，便于观察系统服务的流量消耗。
* 外部资源更新后，现在仅策略组更新会导致策略组页面重载，其他类型不再会导致策略组页面重载。
* 优化了 Surge Ponte/TUIC 的性能表现。
* 优化了策略组异常时的请求 Note 记录。
* 修正 MITM H2 模式下未能正确进行连接复用的问题
* 修正了有时 $httpClient/DoH 的请求可能被意外取消的问题。
* 其他问题修正。

### 版本 5.5.0

#### 界面

* 新 UI 主题 Lucid，源自 Surge Mac 5 的设计语言的主题风格。（需要订阅功能）
* 远程控制的设备管理支持远程修改设备图标。（Surge Mac 需更新至 5.1.0 版本）

#### Surge Ponte

* Surge Ponte 支持跨 iCloud 账号分享。（Surge Mac 需更新至 5.1.0 版本）
* 修正通过 Surge Ponte 或 TUIC 协议，访问 HTTP/1.0 的服务端时可能出现的问题。（如 ASUS 路由器管理页面）

#### 代理协议相关

* 支持 ShadowTLS v3。（需要订阅功能）
* 新功能：Adaptive TLS Fingerprint，详见手册。
* 修正了 Snell V4 下 reuse 功能不能正常生效的问题。
* SSH 协议新增服务器公钥指纹指定，使用方式详见手册。
* 为 VMess 协议增加了 UDP 转发支持。

#### 脚本

* 脚本的 $httpClient 支持 binary 模式。
  * 请求时的 body 支持传入 TypedArray。
  * 请求时的参数传入 `binary-mode: true` 可使返回结果以 TypedArray 返回。
* 修正 `http-request` 类型脚本无法使用 binary 数据直接作为 response 的问题。

#### 其他

* 策略组新增参数 `external-policy-modifier`，可用于对外部策略进行调整。
* 优化了请求的日志系统
  * 增加了日志的分类标识。
  * 规则判断系统增加 DNS 和规则集的更多输出。
* 临时规则上侧滑可将规则写入永久规则。
* 其他问题修正和优化。

### 版本 5.4.0

#### Surge Ponte

Surge Ponte 是一种在运行 Surge Mac 和 iOS 设备之间的私有网络。

* 无需繁琐配置。
* Surge 会自动选择最合适的通道建立连接。
* 始终端到端加密。
* 设备信息和加密密钥通过您的 iCloud 同步，除了您选择的代理服务器外，您的数据不会经过任何第三方服务器。

需要配合 Surge Mac 5 使用 Surge Ponte。

#### WireGuard 相关优化

* 大幅优化了握手相关逻辑。
* WireGuard 的 Client ID 支持由 UI 配置，且新增 0xabcdef 和 6 字符 base64 格式支持

#### 其他更新

* 重做了网络诊断页面，优化了信息展示。。
* 优化 QUIC 的峰值带宽性能和 CPU 占用。
* 被 REJECT 规则匹配的请求将被标记为 Rejected 并使用灰色区分，不再归为 Failed。
* 优化了各功能的开关控制逻辑，避免在一些情况下意外关闭/开启某项功能。
* MITM 时优先使用客户端上报的 SNI 生成证书，未上报 SNI 时使用访问域名。
* 加快了在未开启 Surge 下通过捷径执行 Surge 脚本的唤醒速度。
* SOCKS5 代理请求类型显示时修改为 TCP，可在 Notes 中确认是由 SOCKS5 代理接管。
* 支持在 \[Host] 中为特定域名配置 DNS over QUIC/H3。
* 引入了 FAILED 内置策略用于在特殊情况下标记请求失败（如策略组无法加载），而不是使用 REJECT。
* 修正当规则匹配时，如果客户端意外发送大写字母的域名会无法匹配的问题。
* 修正当多个外置策略组使用了相同名字当实际内容不同的策略时，会导致策略组决策失败的问题。
* DNS Local Mapping 允许为域名配置多个 IP 作为并发使用结果。
* 优化了有线网络适配器的判断，避免误判。
* 其他问题修正。

请注意，从 iOS 16.4 版本开始，系统不再允许读取数据网络的 MCC/MNC，相关功能可能会失效。

### Version 5.3.1 (Feb 16, 2023)

* The installed modules are now synced between iOS devices via iCloud.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Improved WireGuard handshake logic.
* Fixed some UDP forwarding problems.
* Fixed some text editor issues.

### Version 5.3.0 (Feb 3, 2023)

#### New Subscription Feature: Temporary Rules

We have added the temporary rules feature in Surge Mac to the iOS version. Temporary rules will automatically disappear after Surge is stopped and will not be written to the profile for some temporary usage scenarios.

#### New subscription feature: Whois lookup

Quickly perform a Whois lookup to identify the domain or IP owner in the request details menu.

#### New feature: Proxy Detail View

#### Traffic statistics have been enhanced

* In addition to traffic statistics, the number of requests will now be recorded as well.
* In addition to this month's data, last month's data will also be kept.

#### Bug fixes and minor improvements

* JSON and text viewers support search on iOS 16
* Network switching no longer interrupts in-progress $httpClient requests.
* Fixed an issue where scripted requests would sometimes accidentally carry the x-surge header handled internally by Surge
* Fixed an issue that some requests constructed in a special way could not be matched by MITM hostnames.
* Fixed an issue that the LAN proxy and Dashboard may not be accessible if the fast-switch is configured.
* Fixed an issue that could occur when using the expanded card layout on iPad
* Fixed an issue that the Panel button is not showing on iOS 14.

### Version 5.2.2 (Dec 3, 2022)

#### New Feature

* Gaming Optimization. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.

#### Minor Improvements

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* Added a workaround for suspend and subnet settings that may occur when the SSID is temporarily not available under iOS 16.
* The log view supports freezing now.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

### Version 5.2.0 (Nov 11, 2022)

#### Support New Proxy Protocol

* Snell V4
* TUIC
* Shadow TLS

See the online manual for more information.

#### Other Improvements

* A new expanded card style for the Policy Group view.
* Refined the Route Table view.
* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.

#### Bug fixes

* Fixed an issue that when using Subnet Suspend, the switch in the interface did not display the status correctly.
* Fixed an issue that the module could not configure the MITM h2 parameter.
* Fixed some keyboard-related layout problems.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue where UI jumping may occur when starting Surge if iCloud Drive is used.
* Fixed a memory leak that could occur when HTTP capturing is enabled.

### Version 5.1.3 (Sep 29, 2022)

* Added a delayed update mode to the view of the recent request, which will automatically start when too many requests are received, to avoid the Surge main application from getting jammed.
* Optimized the check logic of ICMP traffic limit to avoid the alarm triggered by high concurrency in a very short period.
* Added a lock screen widget that can be used to quickly open Surge.
* Added a view to examine the modified profile after modules are applied.
* Added a new Siri action: enable or disable modules, which can be used with Shortcut.

### Version 5.1.0 (Sep 11, 2022)

#### IPv6 Improvements

* Support UDP forwarding with IPv6 VIF, including local and proxy forwarding.
* Support ICMPv6 local forwarding with IPv6 VIF.
* Fixed an issue that IPv6 address could not be used when using Surge Private DDNS.
* IPv6 handling details refined.

#### WireGuard IPv6 Tunneling

* WireGuard policy now supports IPv6 Tunneling (the previous version already supports connecting to an endpoint with IPv6, this version adds IPv6 support inside the tunnel)
* Read the manual for more information.

#### Text Editor

* A toolbar was added to the text editor.
* Fixed a crash in text editing.
* You can search text in the text editor now.

#### Other updates

* Optimize the proxy failure handling policy. Now when the TCP handshake time to the proxy server is greater than the test-timeout parameter, it is directly determined as failure in order to trigger the policy group to retest faster.
* TabBar shortcut menu added module shortcut opening and closing.
* External resources view allows side-swipe to edit local resources file.
* All types of scripts that use $httpClient to initiate requests are now viewable in the view of the recent request.
* Adjusted script concurrency limit policy to avoid deadlock when multiple scripts refer to each other.
* Other minor bug fixes and improvements.

### Version 5.0.2 (Aug 19, 2022)

* Fixed a bug that the text editor may be unable to save content.

### Version 5.0.1 (Aug 17, 2022)

* You may now flush the DNS cache in the DNS result view.
* Improved the script editor and log viewer.
* Other bug fixes and minor improvements.

### Version 5.0.0 (Aug 10, 2022)

Surge 5.0 comes with a brand new UI design, including a brand new policy group selection view, a new Start tab, and a new icon.

And now, you can try all the features for free for seven days before you purchase.

#### New Features:

* DNS over QUIC and DNS over HTTP3 support
* Real-Time View: Show live speed or request list floating window when using other applications.
* Subnet Setting: Override global settings under specified networks.

#### Minor updates:

* Comprehensive UI improvements.
* New contextual menu in the tab bar items.
* Fixed a bug that encrypted-dns-skip-cert-verification may not work
* MITM hostname and force-http-engine-hosts now support keywords: `<ip-address>`, `<ipv4-address>`, and `<ipv6-address>`.
* Script added function `$utils.ipasn(ipAddress:<String>)` to lookup ASN.
* Script added function `$utils.ipaso(ipAddress:<String>)` to lookup ASO
* Script added function `$utils.ungzip(ipAddres:<Uint8Array>)` for gzip decompression.
* Bug fixes.

### Version 4.15.0 (Jun 30, 2022)

#### MITM over HTTP/2

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

#### Others

* You may use `doh-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.
* Bug fixes.

### Version 4.14.0 (Jun 1, 2022)

#### SSH Proxy Support

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released in 2016.)

#### Keystore

* You may now save sensitive keystore items to the system keychain.
* You may now configure TLS client certificate authentication with the UI.
* You may use a keystore item as the CA certificate for MITM.

#### Others

* New rule type: `IP-ASN`. You may use the rule to match the autonomous system number of the remote address.
* The request details now include the ASN and ASO information of remote IP addresses.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* The preview of SVG images is removed. You can use the new Web View to see the SVG image.
* Bug fixes.

### Version 4.13.0 (Apr 24, 2022)

#### HTTP Capture

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools
* The image viewer now supports SVG format.

#### Proxy

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

#### MITM

* You can export the CA certificate to a P12 or PEM file.
* Fixed an issue that the CA certificate can’t be installed if the default browser isn’t Safari.

#### Header Rewrite

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers. Scripting
* The default timeout of $httpClient is now 5 seconds and you may override it with the timeout parameter.
* You can manage the data of $persistentStore with the UI now.
* You may edit the argument with UI now.

#### Remote Controller

* You may sort and search in the remote device list.

### Version 4.12.0 (Mar 18, 2022)

#### New Feature: Personal Hotspot Proxy Access

* When using an iPhone/iPad as a hotspot, an HTTP or SOCKS5 proxy can be used on the client device to take over the traffic using Surge iOS.
* The proxy IP to be configured on the client is shown in the More Settings and the port number is the same as the WiFi proxy service.

#### New Feature: Hybrid Network

* Instead of setting up connections with cellular data when the Wi-Fi network is poor, always set up connections with Wi-Fi and cellular data simultaneously.
* This feature can improve the network experience significantly on poor Wi-Fi or when the Wi-Fi network is switching.

#### WireGuard

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard now supports underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

#### Detached Profile

* You can now include multiple detached profiles in one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

#### Policy Group

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

#### Subnet expression

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.
* The \[SSID Setting] can control the Wi-Fi assist and Hybrid Network behavior now. Read the manual for more information.

#### Proxy Protocol

* The Trojan protocol now supports using WebSocket as the transport layer.
* Shadowsocks protocol now supports underlying-proxy for UDP relay.
* You may configure the UDP testing endpoint for proxies. e.g., proxy-test-udp = google.com\@1.1.1.1
* You may benchmark a single proxy by long press on the proxy cell.

#### Module

* New Official Module: Block HTTP3/QUIC
* Surge will check updates for installed modules automatically.

#### Others

* Performance improvements.
* OpenSSL is now the default TLS engine.
* The managed profile can be opened with the text editor now.
* The default timeout of $httpClient is 5 seconds now.
* Reduced the app package size.
* You need to perform a one-time Dropbox re-authorization if you are using Dropbox syncing.
* Modules allow modifying the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

### Version 4.11.1 (Jan 27, 2022)

* You may edit the profile in the text mode without changing the current profile now.
* The REJECT policy now can evolve to REJECT-DROP policy for UDP traffics.
* Bug fixes.

### Version 4.11.0 (Jan 21, 2022)

#### Proxy Protocol Upgrades:

* WireGuard: Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy.
* Snell V3: Snell protocol now supports UDP relay.
* Trojan protocol now supports UDP relay. (No additional parameter required)
* VMess protocol supports VMessAEAD. (Policy parameter: vmess-aead = true)

#### Improvements:

* The underlying proxy (aka proxy chains) now supports using a policy group.
* New parameter: udp-policy-not-supported-behaviour. To control the fallback behavior when UDP traffic matches a policy that doesn't support UDP relay.
* You may acquire the request's headers within an http-response script via $request.headers.
* Performance optimization.
* Bug fixes.

### Version 4.10.0 (Dec 3, 2021)

* You may extend your Surge iOS Pro license to 6 devices for free. You may find the guidance in the License Management view.

#### New Features

* Sorting option in the request list.
* Supports remote rule editing for the remote controller.
* Added the effective order adjustment view for the module. You can now adjust the effective order of the module.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.

#### Other Improvements

* UI details refined.
* Performance improvements.
* The network changed notification message will display the data network operator. If network automatic switching is enabled, you can use the notification to confirm the current carrier.
* The URL query part of the HTTP request is no longer displayed in the request list. It is now displayed in the details view.
* Fixed the problem that the JavaScript script timeout mechanism might not work properly.
* Fixed an issue that could occur when a load-balance group contains another group.
* Removed the "All" option from traffic statistics, as it took too long to count all historical traffic when the feature had not been used for a long time.
* You may remove devices in DDNS and Cloud Notification views.

### Version 4.9.4 (Oct 28, 2021)

Bug fixes

### Version 4.9.3 (Sep 30, 2021)

* New feature: Information Panel. Read the manual for more info: <https://manual.nssurge.com/others/panel.html>
* The profile now supports the profile version remark. Read the manual for more info: <https://manual.nssurge.com/release-note/profile-version.html>
* The HTTP scripts now support binary mode to modify the request/response body.
* Other minor improvements and bug fixes.

### Version 4.9.2 (Sep 3, 2021)

Bug fixes

### Version 4.9.1 (Aug 24, 2021)

Bug fixes

### Version 4.9.0 (Aug 20, 2021)

#### New Features: Surge Private DDNS

Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

#### New Features: Egress Control (No UI Settings Currently)

* You can use the new internal policy HYBRID to make requests to try Wi-Fi and cellular simultaneously. You can also use the "hybrid=true" parameter to gain a proxy policy for the behavior.
* You can now tell Surge to use IPv4 or IPv6 under a dual-stack environment. Read the manual for more information.

#### New Features: Profile Syntax

You can look up the configuration parameters for the text editing mode within the app. It always displays the syntax for the current version.

#### New Features: Surge VIF IPv6 Stack (No UI Settings Currently)

Surge VIF now supports the IPv6 stack for the raw TCP connections. Use parameter "ipv6-vif=true" to enable.

#### Improvements

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.
* $request.id is added to the http-request and http-response scripts for continuity among scripts.
* Bug fixes.

### Version 4.8.0 (Jun 14, 2021)

New Features:

* Request Display Filter You may use multiple conditions to filter which requests to show.
* Web Dashboard You may control Surge via a web browser on local or remote devices.

Other bug fixes and improvements.

### Version 4.7.0 (Apr 21, 2021)

#### Rules

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* New rule type: CELLULAR-CARRIER, which can match the MCC-MNC code.
* New rule type: CELLULAR-RADIO, which can match the radio access technology of the cellular network.

#### Profile

* You may put partial sections into a detached file. See manual for more information.

#### HTTP API

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including: GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

Other bug fixes and improvements.

### Version 4.6.0 (Feb 26, 2021)

#### Remote Controller

* You may use this remote controller to view real-time statistics, and events and perform network diagnostics remotely.
* You may use the remote controller to control the DHCP server feature of Surge Mac, including adjusting each device's settings.

#### Cloud Notification

* You can receive Surge Mac's notifications on your iOS device.

#### Scripting

* You may execute a script with Siri or Shortcuts.

#### Policy Group

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.

* The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
* The latency of the load-balance group is the average of the latencies of all available policies.

4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

### Version 4.5.1 (Jan 20, 2021)

Bug fixes

### Version 4.5.0 (Jan 19, 2021)

* New Feature: Network Layer Packet Capture: You may now capture the raw TCP/UDP/ICMP packets and inspect them right on the device. Or you can export a standard .pcap file for other tools.
* You can customize the GeoIP database updating URL now.
* The GeoIP database can be updated automatically now.
* Bug fixes and improvements.

### Version 4.4.3 (Oct 28, 2020)

* Optimized for the iPhone 12 series.
* Modified requests are now marked with orange color.
* Bug fixes.

### Version 4.4.2 (Sep 25, 2020)

Bug fixes

### Version 4.4.1 (Sep 23, 2020)

Bug fixes

### Version 4.4.0 (Sep 20, 2020)

New Features:

* HTTP API: Control Surge with HTTP API with another app or from another device.
* Proxy Chain: Connection to a remote host will be performed sequentially from one proxy server to another.

Major Improvements:

* You may mix the external proxies with the proxies of the profile in one policy group now.
* The DNS result view has more information.
* You may use 'policy-regex-filter' to include a part of an external proxy list's content.
* New CELLULAR and CELLULAR-ONLY policy.

Minor Improvements:

* iCloud Drive sync improved.
* You may use $notification.post in a script to post a notification with an action URL.
* The HTTP proxy service now supports basic authentication.
* Surge now enables TCP keepalive for all outgoing connections.
* Surge now supports to use of a URL with a username and password to perform basic authentication for an external resource. (<https://username:password@example.com>)

We recently published official guidance for you to understand Surge. You may find it in the More tab. Version 4.3.2 (Jun 25, 2020) Improvements for the latest iOS system. Version 4.3.1 (Jun 22, 2020) New Feature: Wi-Fi Timeline You may check the connected Wi-Fi network timeline, including entering and leaving time.

Minor Changes

* Optimized the timing system. The DNS time cost is now calculated precisely.
* Bug fixes.

### Version 4.3.0 (Jun 4, 2020)

New Feature: Mock

* You may mock the API server and return a static response. This feature may also be called as Map Local or API Mocking. New Feature: Event Center
* You may now review all historical events.

Minor Changes:

* Optimized the classical start view for Dark Mode.
* The Load-Balance group now supports connectivity testing.
* Add a parameter "use-local-host-item-for-proxy", to use local DNS mapping result even through a proxy protocol.
* The module may adjust contents in \[SSID Setting] now.
* Optimized Wi-Fi Assist feature.
* You may specify the timeout while using the script editor. Version 4.2.2 (May 19, 2020)
* New Feature: Traffic Statistics You may examine the history of traffic usage grouped by the host, by policy, or by the network interface.
* New Feature: DOMAIN-SET We have added a new type of rule: DOMAIN-SET, which may contain millions of sub-rules. No UI configuration in this version. Please configure with the Text Mode

\[Rule] DOMAIN-SET,hostname.txt,REJECT

Each line in the file is a hostname or an IP address. If the hostname starts with a dot, all sub-domains will be matched.

* Other bug fixes and improvements. Version 4.2.1 (Apr 28, 2020) New Feature: Enhanced Wi-Fi Assist
* Surge will try to set up a connection with cellular data when the Wi-Fi network is poor.

Changes in DNS-over-HTTPS

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.

Bug fixes and stability improvements

### Version 4.2.0 (Apr 17, 2020)

New Feature: Module Module is a set of settings to override the current profile. You may use modules to:

* Tweak settings in a non-editable profile, such as managed profile and enterprise profile.
* Change part of settings with one tap. For example, you may use a module to enable MitM for all hostnames and adjust the filter temporarily.
* Use a module written by others to accomplish a particular task. For example, your co-work may share with you a module that rewrites the API requests to a test server.
* When you share one profile among devices, some settings might need modifying for different scenarios. The enabling state of modules won't be synced to other devices, so you can use a module to fulfill.

Minor Improvements:

* Added a new rule type: PROTOCOL.
* Improved the MITM CA certificate install assistant.
* You may now use UI to configure a load-balance policy group.
* You may now use UI to configure SSID suspend.
* Bug fixes.

### Version 4.0.2 (Feb 11, 2020)

* Bug fixes
* Supports choosing profiles in a subdirectory
* A new feature has been added: iperf3 client mode. You may use it to benchmark the bandwidth. Different from the standalone iperf app, you may force the test to use a specified proxy.

A quick guide:

1. Install iperf3 on the proxy server.
2. Run "iperf3 -s" within a screen or tmux session.
3. Start iperf test with Surge. Leave the hostname field empty. 127.0.0.1 will be used and indicates the proxy server itself. Version 4.0.1 (Dec 31, 2019)

* Support VMess proxy protocol
* Bug fixes

### Version 4.0.0 (Sep 18, 2019)

Welcome to Surge 4. We are now introducing the Feature Subscription. As a Pro license owner, you: · Always have access to all your features for a lifetime. · Get free enhancement updates for features you already have for a lifetime. · Get compatibility updates for new systems and new devices for a lifetime. · Get a one-year free Feature Subscription since your purchasing date. · Renew the subscription when a new feature impresses you, totally optional.

New features: · Scripting: Use JavaScript to extend the ability of Surge as your wish. · Dark Mode: Fully adapted for iOS 13 Dark Mode. · DNS over HTTPS: Use DNS over HTTPS (DoH, RFC 8484) to perform DNS queries. · TLS v1.3: TLS v1.3 support for HTTPS/SOCKS5-TLS proxy. · Dropbox: Use Dropbox to sync your profiles across devices.

### Version 3.8.1 (Jun 4, 2019)

Bug fixes

### Version 3.8.0 (May 21, 2019)

Proxy

* Rules can be enabled/disabled now. Try sliding left on it.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluation. Enable the option to delay the requests until the evaluation is completed.

MitM

* HTTP and MitM engine has been refactored.
* You can now use the URL-REGEX rule for MitM connections.
* You may use the prefix '-' to exclude domains for MitM.
* MitM hostname list now supports port numbers. By default, only the connections to port 443 will be decrypted.

Minor Improvements

* Move the 'External Resources' item to the profile list view. Managed profile users may utilize the view to update resources now.
* It won't bother you anymore that the Cloud profiles disappear sometimes.
* Touch ID / Face ID now allows passcode as a fallback.
* Refined English localization.
* Refined UI details.
* The notification banner is draggable now.
* All advanced options can be edited with UI now. Please do not touch it before reading the manual.

Bug Fixes

* Fixed a bug that the request detail page doesn't update in real-time
* Fixed a bug that the GEOIP rule doesn't work for IPv6 addresses. Version 3.7.1 (Apr 27, 2019)
* Remote Dashboard: You may connect to another device with Surge iOS/Mac running and inspect the requests.
* An active connection can be killed now.
* Bug fixes Version 3.7.0 (Apr 16, 2019)
* Refined UI, including a fullscreen text editor for complex text fields, new colorful icons, and more detail improvements.
* New feature: Always On. Surge may start automatically even after a device reboot.
* The request detail page now updates in real-time.
* The ruleset can be added or edited with UI now.
* Policy group with an external list can be added or edited with UI now.
* Bug and compatibility fixes.

### Version 3.6.1 (Mar 20, 2019)

* Bug fixes

### Version 3.6.0 (Mar 15, 2019)

* Added support for a new proxy protocol Snell.
* You may export all dumped requests to a .surgearchive file and open with Surge Mac Dashboard.
* Optimizations for the request search view.
* Experimental feature: You can enable Network.framework to utilize user-space network stack, which can improve throughput, reduce latency and enable cutting edge features such as Multipath TCP.
* Minor bug fixes.

### Version 3.5.0 (Jan 3, 2019)

* Performance improvements
* Prompts profile changes via iCloud Drive
* Allows to customize Wi-Fi access ports for HTTP & SOCKS5 proxy services
* Supports to update GeoIP database manually
* Copy cURL is now available for all HTTP methods
* Captured body data may be exported to other apps
* Bug fixes

### Version 3.4.2 (Nov 21, 2018)

Bug fixes

---
## Release Notes / Surge Mac 6

自 Surge Mac 5 发布已过去了两年多，在这两年里我们诸多重量级的免费更新，如：

* 新的 Network Extension 接管模式
* Smart Group
* 新的代理协议支持（SS2022/Hysteria2/TUIC）
* 预匹配规则
* 使用 JQ 表达式操作 JSON Body
* 端口转发
* 代理端口跳跃
* 脚本面板
* 巨型规则集支持
* 协议嗅探
* Surge Ponte共享
* 设备图标库

我们统计了下，这两年内我们总共发布了 11 个大版本，43 个小版本，超过 1000 个 beta build。

我们之前曾经撰文解释过，在大版本收费更新的模式下，开发者应该尽量将功能“囤积”到下一个大版本中发布，才是最优的策略。但是我们确实不想这么做，不想有意的拖延新功能的实现，所以即使在免费更新周期内，Surge 也一直保持着高强度、无保留的更新节奏。

但这确实也给我们带来了困扰，当我们应该进行大版本更新时，用户可能会觉得新的功能并不足够支撑这次付费更新，除非我们刻意拖延新功能的发布。

这也几乎是所有活跃的开发商所遇到的共同问题，因此现在大量的软件均采用纯订阅，或者维护更新订阅模式（如 TablePlus、ForkLift、Sketch、Tower、Kaleidoscope 等）。因此 Surge 也决定转向维护订阅模式。

具体细节如下：

1. Surge Mac 6 的售价保持不变，购买后带有一年期的维护订阅，可在一年内免费获取所有更新。
2. 订阅过期后，可终身继续使用最后的版本，如果想要进行更新，需要续订维护订阅。
3. 维护订阅价格为

| 授权设备数 | 维护更新订阅续费（12 个月） |
| ----- | --------------- |
| 1 台   | US $19.99       |
| 3 台   | US $29.99       |
| 5 台   | US $45.99       |

4. 目前已经购买 Surge Mac 5 的用户，也将获得自购买日起一年期的维护订阅。也就是说于 2024 年 7 月 1 日后购买 Surge Mac 5 的用户，可以免费更新至 Surge Mac 6.0。在这之前购买了 Surge Mac 5 的老用户，只需要续订订阅即可升级到 v6。
5. 之后不再会有付费大版本更新。
6. Surge Mac 3/4 用户，依然需要先一次性付费升级到 v6。同样附带自升级日起的一年期订阅。

与 iOS 版本一样，你只需要在觉得有需求的情况下，再订阅进行更新即可。**订阅是完全可选的，即使不订阅也可以一直使用已有的 Surge Mac 版本**。

### Surge Mac 6.0 新功能

在 Surge Mac 6.0 中，我们再次带来了多项创造性的独有新功能，同时升级了全新的设计。由于功能众多，请跳转到 [Surge Mac 6.0 Release](/surge-knowledge-base/zh/release-notes/surge-mac-6-release-note.md) 查看。

<a href="https://dl.nssurge.com/mac/v6/Surge-latest.zip" class="button primary">下载 v6 版本</a>

### 试用

如果你希望在续订前进行试用，请在 Surge Mac 的更多 › 授权面板中，反激活当前授权，然后重启 Surge 选择开始试用，即可免费试用 Surge Mac 6 七天。

即使曾经使用过七天免费试用，也可以再次试用 6.0。另外现在开始，每次试用期结束一年后，都可以再次开启七天免费试用，也就是说每年都可以免费试用一次。用于免费体验新的订阅更新版本。

在试用到期后，如果希望回滚到旧的版本，直接进行授权激活即可，Surge 会自动下载旧版本完成替换。（如果已经进行了不兼容的配置修改，请记得调整回旧版本的设置）

### 其他细节

* 如果在 Surge Mac 5 时期，曾经进行过授权数量升级，那将会根据付款金额加权计算得到购买日期，并以此为基准计算维护订阅期。

比如在 2021/7/27 日购买了 1 设备授权，然后在 2022/8/23 日升级到了 3 设备授权，那么等价购买时间为 2021/12/20。

* 现在开始，进行授权数量包升级时，升级费用不再和直接购买授权包存在差价。升级后订阅有效期为一年后，需为原有设备补满至同一到期日。

比如当前拥有 1 设备授权，订阅到期日为 200 天后，升级 3 设备授权的费用为：$69.99 - $49.99 + $29.99 / 3 \* (1 − 200 / 365) = $24.5，即差价 $20 + 已拥 1 设备新增 165 天订阅费 $4.5，升级完成后整个授权更新有效期为 365 天后。

由于是以更高档位折扣的订阅价格对原设备进行续订，所以直接购买升级包的价格，会比先续订再升级数量的价格更优惠。

* 为了保证老用户升级权益，首个 Surge Mac 6.0 版本的解锁时间，锁定为 2025 年 7 月 1 日。即使最终 6.0 版本的发布时间已经超过订阅有效期，只要订阅期在 2025 年 7 月 1 日后便可以使用。后续的版本将以版本的发布时间为准。

### FAQ

* 我必须要在订阅期内升级到最新版本才能够一直使用最后版本吗？

不需要，即使订阅已过期，也可以随时更新到过期前发布的最后一个版本。

* 我怎样知道有什么新功能：

我们新上线了更新日志的网页版本，与更新系统同步更新：<https://nssurge.com/support/mac/release-notes>，可在这里查看所有版本的更新内容与发布时间。

当有新的版本时，如果订阅已经过期，将在主界面的事件列表中进行弱提示，可点击查看。如果不想收到此消息，可以点击后选择暂停检测的时间，或者永久关闭提示。

---
## Release Notes / Surge Mac 6.0 Release Note

<a href="https://dl.nssurge.com/mac/v6/Surge-latest.zip" class="button primary">下载 v6 版本</a>

在 Surge Mac 6.0 中，我们再次带来了多项创造性的独有新功能，同时升级了全新的设计。

### Surge Gateway Mode

在 Surge Mac 6.0 中，原本的 Surge DHCP Server 功能升级为了全新的 Surge Gateway Mode，包含众多新特性：

1. Surge Gateway VM

旧版本中，Surge 依赖系统的 utun 设备和 IP forwarding 机制处理来自其他设备的网络流量，这带来了不必要的开销，也限制了 Surge 的功能。现在，Surge 将使用 macOS 的 VMNET framework，以虚拟机的方式接入网络，直接工作在 Layer 2。（类似于使用虚拟机运行 RouterOS） 这不仅提高了性能，也给 Surge 实现更多的网关功能提供了可能性。

2. IPv6 RA Override

旧版本中使用 Surge DHCP 模式时，遇到的一大问题是与 IPv6 相冲突，因为 IPv6 RA 下发的 DNS 会导致 Surge 的 Fake DNS 机制失效。

现在 Surge 可以发送更高优先级的 RA 消息，覆盖并接管选定设备的 IPv6 网关，不仅解决了原先可能出现的 DNS 问题，也完成了对设备的 IPv6 网络的完全接管。 而且这种接管是定向、非排他性的，不需要对原本网络的 IPv6 进行任何调整即可使用（除非原路由 RA 消息优先级设置为了高，需要手动降低为中），也不会影响其他非选定设备。

如果需要上述两个新特性，需要关闭 Gateway Mode 重新开启以打开相应的开关。

使用 IPv6 RA Override 功能，需要保证路由器的 IPv6 RA 广播的 DNS 地址，不为 fe80::/10 的 link-local 地址，也不可以为路由器自身的 IPv6 地址。 绝大多数路由可以自定义 IPv6 RA DNS 地址，将其置空或者修改为任意公网 DNS 即可。少数路由不支持修改，已知不兼容的路由为

* ASUS 全系（可通过更换 Merlin/OpenWRT 固件解决）

更多利用 Surge Gateway VM 的新功能尚在开发中，如 UDP FastPath，将在后续版本中加入。

### Surge VIF Engine

Surge Mac 5.0 时我们推出了 VIF v2 工作模式，利用系统的 Packet Filter 取得了极其强悍的性能表现，在 M3 下测试可达 \~ 37 Gbps，后续又更新了 v3 版本改善了兼容性。

然而由于 macOS Sequoia 系统的新兼容性问题，我们被迫放弃了原本的 utun VIF 方案，转而使用 Apple 目前推荐的 Network Extension 框架实现 Surge VIF，以确保出现问题的可能性最低。NE 下 v2 与 v3 并不能工作，更雪上加霜的是，NE 没有给开发者开放足够的接口去进行调优，使得我们在 v1 中的许多性能优化也失效了。

为此，在 Surge Mac 6.0 中，我们完全重写了 Surge VIF，使用了最新的理论和极致的优化，大幅提高了增强模式下的表现。在 M4 Mac Mini 上进行回环 iperf 测试，上行最大吞吐量可达 \~30Gbps，下行 \~23Gbps，远超其他同类软件。最大吞吐量不仅意味着可以处理更高的流量，也表示在低带宽时开销也更低，对 CPU 占用少且能耗低。

从 Surge Mac 6 开始，我们提供**最优性能保证**，如果在购买 Surge 后，发现 Surge 性能指标（包含吞吐量和延迟）在同等条件下劣于其他软件，在购买 30 天内都可以以此申请全额退款。

同时本次重写还优化了对于 UDP 流量的处理，特别是大吞吐量下的表现，在 M4 Mac Mini 上进行回环 iperf 测试，可达 10Gbps（此为 iperf3 UDP 测试下的最高限制）。

同时由于 WireGuard 协议栈也依赖于 Surge VIF 的实现，其性能也得到了一定提高。

其他技术细节上，Surge VIF 现在新增了 Active Queue Management （AQM）和 TCP pacing 机制，用于处理大吞吐量时的拥塞和其他兼容性问题。

你也可以自行进行 iperf3 测试 TCP 回环吞吐量，首先开启一个终端，执行 `iperf3-darwin -s` 启动测试服务端。 再开启另一个终端，执行 `iperf3-darwin -Rc lvh.me` 即可测试下行吞吐量，执行 `iperf3-darwin -c lvh.me` 测试上行吞吐量。

### Surge Ponte 2.0 - Multiple Channels

在 Surge Mac 5.0 中，我们推出了 Surge Ponte 功能用于组建点到点的私人加密网络，得益于创新的工作模式，这可能是使用起来最简单的内网穿透方式。

6.0 中 Surge Ponte 得到了重要强化，Surge Ponte 的服务端不再被限制于只能选择一种工作模式了，你可以同时开启多种穿透模式，甚至选择多条代理线路进行穿透。当 Ponte 客户端进行连接时，将自动选择最快速的通道进行连接。

同时，现在 Surge Ponte 新增了 IPv6 直连通道，仅需在防火墙中开放端口，Surge Ponte 就可以通过 IPv6 直连完成组网。

另外，Surge Ponte 不再依赖公共的 STUN 服务器，开始使用自建的 STUN 服务，由于该服务专门为 Surge Ponte 设计，响应速度得到了明显提升。

请注意，Surge iOS 也需要升级到最新测试版本才能使用该特性，使用旧版只会使用第一个通道。

### Surge Smart Group

6.0 中 Smart Group 也得到了增强，我们完成了 Smart Group 对 UDP 连接的优化，现在 UDP 流量使用 Smart Group 也会享受到 Smart Group 的智能调优。

同时 Smart Group 本身也得到了强化与改进，以适应更多的情形。Smart Group 与 Snell 协议 reuse 机制的冲突也已经解决。

### Snell v5

Surge 自有的代理协议 Snell 升级到了 v5，带来了两个新特性

Snell 协议同样享有**最优性能保证**，如果在购买 Surge 后，发现 Snell 代理协议性能指标（包含吞吐量和延迟）在同等技术条件下劣于其他软件，在购买 30 天内都可以以此申请全额退款。

#### Dynamic Record Sizing

该特性将提高在存在丢包的网络环境下延迟表现。技术细节可参考 ：[Cloudflare Blog](https://blog.cloudflare.com/optimizing-tls-over-tcp-to-reduce-latency/)

#### QUIC Proxy Mode

我们之前专门解释过为什么对 QUIC 进行代理转发不是一个好主意，并且加入了 block-quic 参数用于自动屏蔽 QUIC 请求。但是无奈的是，最近发现有些应用开始强依赖 QUIC，若屏蔽 QUIC 流量可能会导致其工作异常。

因此 Snell v5 加入了专为 QUIC 流量设计的 QUIC Proxy 模式，该模式工作属于 UDP over UDP，以避免 TCP over UDP 问题。（服务端需开放 UDP 端口）

* 该工作模式为 QUIC 进行了特殊优化，仅当 Surge 识别到 QUIC 流量时会启用，其他 UDP 流量依然使用 UDP over TCP 模式。
* QUIC Proxy 只会对 QUIC Handshake 数据包进行强加密，以保护 SNI 和目标主机名，同时进行鉴权。后续的所有 QUIC 数据包，由于本身已经被 QUIC 强加密，将直接以裸包进行转发，大幅降低了不必要的加解密开销。同时由于未引入额外字节，不会影响 QUIC 的 PMTU 探测。

服务端下载链接请见：[Snell](/surge-knowledge-base/zh/release-notes/snell.md)

Snell v5 的服务端可以向下兼容 v4 客户端，如果不想使用 QUIC Proxy Mode 功能，客户端设置为 v4 版本即可，Dynamic Record Sizing 的优化只和服务端有关。

#### 出口控制

* 支持配置 `egress-interface` 参数控制出口 interface（需要 root 权限或者给予`CAP_NET_RAW/CAP_NET_ADMIN` 授权，同时该 interface 上需要有目标地址和 DNS 的路由表）
* 支持 systemd 的 Socket Activation 机制，可用于配置 network namespace，也可用于出口 interface 配置。我们会在之后提供配置样例。

### 流量统计系统

流量统计系统得到了大幅升级，现在能以目标主机名为维度进行统计了，同时统计数据的时间维度扩大到了月度，除了本月外也会保留上月的数据。

同时，越来越多的应用开始使用子进程进行网络请求，这造成了统计和查看上的混乱，新版本中可以将应用包内的所有进程都合并进行统计。

### Fake DNS v6

Surge DNS server 现在同时监听于虚拟 IPv6 地址 fd00:6152::2，可以对 AAAA 查询返回 Fake IPv6 地址，也就是说如果有需要，Surge 现在可以工作在纯 IPv6 环境中。

### Linked Profile

为了解决托管配置的本地修改难题，我们再次优化了 Linked Profile 的设计，现在 #include 语句可以直接使用一个托管配置的 URL 了。

同时，v6 版本在安装托管配置时，将会主动提示用户创建 Linked Profile，如果已经在使用托管配置，现在在尝试修改配置时，也会主动引导创建 Linked Profile。

### 界面更新

新版本带来了全新的设计，Surge Mac 6.0 中着重优化了数据展现，现在你可以在首页看到更多维的数据。

请注意，本次设计更新还没有全面为 macOS 26 进行调整，等待 macOS 26 风格稳定后，我们会再次进行界面更新适配。

同时，几乎每个页面都经过了重新优化，以确保符合最新 macOS 设计标准。

### 其他细节更新

* `IP-CIDR` 规则允许直接使用单 IP，即隐含 `/32`。
* `PROTOCOL,TCP` 规则现在也会对 HTTP 和 HTTPS 连接生效了，保证与 `PROTOCOL,TCP` 规则的语义一致性。
* 优化对特别巨大的配置的处理性能（数百条代理和策略组），现在即使加载巨型配置也不会产生卡顿。
* HTTP request/response 规则新增 `full-header-mode` 参数，开启后 `headers` 字段将以数组格式提供，以保证在处理多个同名字段（如 `Set-Cookie`）时的兼容性。
* 不支持 UDP 的代理的默认回退行为改为 REJECT
* 新增 HTTP 的 zstd 压缩算法支持
* 全局优化 wildcard 匹配性能
* 重做高级设置页面，现在所有高级参数都可以通过 UI 直接编辑了。

---
## Release Notes / Surge Mac 历史版本

## Surge Mac 旧版本

自 v6 版本开始，请从这里查看更新日志：<https://nssurge.com/support/mac/release-notes>

* 自 Surge Mac v5.8.0 版本起，Surge 对 macOS 的最低版本需求提高至 macOS 12.0。如果你的操作系统为 10.13/10.14/10.15/11。请下载 5.7.5 版本：<https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>
* Surge Mac v5 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v5/Surge-latest.zip>
* Surge Mac v4 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v4/Surge-latest.zip>
* Surge Mac v3 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v3/Surge-latest.zip>
* Surge Mac v2 的最后一个版本下载链接：<https://dl.nssurge.com/mac/v2/Surge-latest.zip>

## Surge Mac v5 更新日志

#### 版本 5.10.3

* 新增 `[General]` 参数 `block-quic`，用于全局覆盖是否阻止 QUIC 流量的行为。可设置为：
  * `per-policy`：由 policy 的 `block-quic` 参数决定，默认为当前版本行为。
  * `all-proxy`：覆盖代理 policy 的 `block-quic` 参数，全部阻止
  * `all`：覆盖所有 policy 的 `block-quic` 参数，包括 DIRECT policy 在内全部阻止
  * `always-allow`：覆盖代理 policy 的 `block-quic` 参数，全部允许
* 新增规则添加视图现在可以记住上一次的选项。
* 错误页面新增深色模式支持。
* 增加对 Dia 浏览器的集成支持。
* 修复了 bug 并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.3-3272-5cf851de0c9af2bf96ab410244010f9a.zip>

#### 版本 5.10.2

* 访问 Ponte 设备的远程 Dashboard 不再需要启用增强模式。
* 新增对 DNS over TLS 的支持，例如 `tls://8.8.8.8`
* 优化了通过 Dashboard 添加规则的流程。
* Surge Dashboard 现在可以远程操作目标 Surge 实例的临时规则。
* 修复了一些错误并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.2-3235-9255a55c4af59cbf0ed01b245ef86dcc.zip>

#### 版本 5.10.1

* 当启用 HTTP 捕获开关时，现在会强制中断所有活动连接，以确保不会因现有长连接而漏捕任何请求。
* 优化了对部分 QUIC 客户端（如 Lark）的兼容性。
* 修复了通过脚本或其他机制修改请求 HTTP 后，统计中的下载数据字节数不正确的问题。
* 调整了转发 QUIC 时的处理逻辑优先级。现在，对于不支持 UDP 转发的代理 policy，会优先考虑 QUIC Block，然后再回退到 DIRECT 或 REJECT。
* 修复了绑定出站接口时无法使用 utun 设备的问题。
* 修复了 Ponte Server 重试失败期间可能持续出现重复通知的问题。
* 解决了 Surge Ponte 转发的特定请求在某些网络下可能卡住的问题。
* Bug 修复及其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.1-3207-1e925800c695a40e8a34ceca6d856b0d.zip>

#### 版本 5.10.0

**新功能：端口转发**

示例

```
[Port Forwarding]
0.0.0.0:6841 localhost:3306 policy=SQL-Server-Proxy
```

policy 参数为可选项；如果未指定，将使用标准代理匹配来确定 policy。 该功能常用于开发和调试场景，例如通过 SSH 连接 MariaDB 等服务器。

**#!REQUIREMENT 升级**

* 现在提供三种简单标记：#!IOS-ONLY、#!MACOS-ONLY 和 #!TVOS-ONLY。
* 被此行尾注释禁用的内容现在可以在 UI 中显示和编辑。当条件不满足时会显示为已禁用，若启用则会自动移除限制。

示例

```
DOMAIN,reject.com,REJECT #!MACOS-ONLY
```

**\[Host] 优化**

\[Host] 部分支持使用 DOMAIN-SET 和 RULE-SET 配置，以提升匹配效率。使用案例：

```
[Host]
DOMAIN-SET:https://example.com/domains.txt = server:https://doh.com/dns-query
RULE-SET:https://example.com/rules.txt = server:https://doh.com/dns-query
```

**其他改进**

* 优化以 Smart policy 分组作为底层代理的情况。。现在，在这种使用场景下，可以充分发挥 Smart policy 分组的特性。
* Surge Ponte 在出现异常 NAT 类型后，现在可以自动重试恢复。
* 修复了一些 bug 并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.10.0-3195-d468f4e99b54bcde0432f2b5a0e38296.zip>

#### 版本 5.9.3

* 修复了漏洞并进行了其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.9.3-3122-0244efc5738b3cebde7c87c556cfddb8.zip>

#### 版本 5.9.2

* 菜单栏图标现在可以显示出站模式。
* 修复了与 Ponte 相关的一些问题。
* 修复了在 DHCP 配置页面上错误信息有时无法显示，导致无法继续操作的问题。
* 修复了为 .local 域名配置的 \[Host] 条目可能无效的问题。
* 优化了代理和规则编辑页面；UI 中不可编辑的参数现在也会被保留。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.9.2-3098-643c195efc1153b6d4993af6bba73a59.zip>

#### 版本 5.9.0

#### 新功能

* 添加了低开销请求拒绝的预匹配规则。详情请参阅文档：<https://manual.nssurge.com/policy/reject.html>
* Body Rewrite 支持使用 JQ 表达式操作 JSON。
* shadowsocks 协议新增支持 `2022-blake3-aes-256-gcm` 和 `2022-blake3-aes-128-gcm` 加密模式。

#### 改进

* URL-REGEX 规则现在支持 `extended-matching` 标签。
* 允许使用 Ponte 策略作为底层代理。
* 修改 HTTP 脚本的终止逻辑。如果需要中断请求，请使用 $done({abort: true})。其他失败不会修改或终止请求。
* 全面优化和改进 UDP 转发。

#### 错误修复

* 修复在增强模式下 DNS 请求无法根据路由表选择正确接口的问题。
* 修复 macOS 12 上无法获取系统路由的问题。
* 修正某些情况下判断 IPv6 是否存在可能不正确的问题。
* 修复有时错误提示代理设置已被其他程序修改的问题。
* 其他错误修复。

<https://dl.nssurge.com/mac/v5/Surge-5.9.0-3025-f8d045da66079150d4a281ed3770b3f6.zip>

#### 版本 5.8.2

* 修复启用 `gateway-restricted-to-lan` 参数时 IPv6 VIF 无法接管请求的问题。
* 对 `use-application-dns.net` 的 DNS 查询将返回 NXDOMAIN，导致 Firefox 自动禁用应用程序 DNS（即 DoH）。直接在浏览器中使用加密 DNS 会阻止 Surge 正确获取请求的域名。
* 错误修复和小幅改进。

<https://dl.nssurge.com/mac/v5/Surge-5.8.2-2946-b739968f1d90da3b755d3bf82941e8c2.zip>

#### 版本 5.8.1

* 新参数：proxy-restricted-to-lan/gateway-restricted-to-lan 一些用户由于缺乏网络安全知识，意外地将代理和网关服务暴露在互联网上（例如，配置了 DMZ）。因此，添加了这两个参数以限制代理和网关服务仅接受来自当前子网的设备。这两个参数默认启用。
* 修复增强模式与 PPPoE 直接拨号之间的兼容性。
* 支持使用 ETag 避免在请求外部资源时下载重复数据。
* Surge 现在支持处理系统的 DNS 搜索域设置。
* 其他错误修复和兼容性改进。

<https://dl.nssurge.com/mac/v5/Surge-5.8.1-2929-5220af95366dfacec7ca84cb8ddd122c.zip>

#### 版本 5.8.0

**网络扩展**

* 鉴于传统 utun 接管方案在新系统版本中出现了诸多问题，从 Surge Mac 5.8.0 开始，Surge Mac 将使用 Network Extension 作为增强模式来接管系统网络。
* Surge Mac 的最低系统版本要求提升至 macOS 12。
* 因为所需权限不同，更新后需要手动授权操作。
* `vif-mode` 参数将不再有效。
* 增强模式现在可以与网络共享功能结合使用，这意味着你可以直接创建由 Surge 管理的 Wi-Fi（需要有线网络）。

**端口跳跃**

Hysteria2 和 TUIC 协议现在支持端口跳跃，以改善 ISP 对 UDP 的 QoS 问题。详情请参阅服务器文档。

`Proxy = hysteria2, 1.2.3.4, 443, password=pwd, port-hopping="1234;5000-6000;7044;8000-9000", port-hopping-interval=30`

配置 `port-hopping` 参数后，前面配置的主端口号将不再有效。

参数：

* `port-h-hopping`: 用于配置端口范围。用逗号分隔，并支持用连字符配置的范围。
* `port-hopping-interval`: 更换端口号的间隔时间。默认为30秒

**其他改进**

* 鉴于新 macOS 系统中大量需要权限的功能，新增了一个专门用于管理系统权限的页面。
* 本地 DNS 映射中的 `syslib` 关键字现在可以在增强模式下使用。然而，在非增强模式下，解析完全由系统处理。在增强模式下，Surge 使用系统的 DNS 地址进行解析。
* 新增 `[General]` 参数 `show-error-page`, 用于控制当发生错误时是否显示 Surge 的 HTTP 错误页面。此参数默认启用，其行为与之前版本一致。

<https://dl.nssurge.com/mac/v5/Surge-5.8.0-2900-6379c9d5240ae1555772aed2eb977e69.zip>

#### 版本 5.7.5

* 面板现在可以在 Surge Mac 中使用。
* DNS 转发子系统优化
* 当 DNS 查询的域名是不应转发到公共网络的域名（例如 .home.arpa, 1.0.168.192.in-addr.arpa）时，将自动确定上游 DNS 地址并仅转发到局域网 DNS 服务器。
* Surge 现在可以正确响应假 IP 的 PTR 请求，这意味着使用 `dig -x 198.18.23.87` 命令可以确定与假 IP 对应的原始域名。
* DNS 转发器现在将根据 `[Host]` 部分配置将 DNS 请求转发到特定的上游服务器。
* 对于不支持的假 IP 的 DNS-SD PTR 请求，直接以 NOTIMP 响应，而不进行转发。
* 为当前网页添加规则时，可以选择添加到现有规则集中。
* 修复了一些错误。

<https://dl.nssurge.com/mac/v5/Surge-5.7.5-2826-4f19761fb2275ebbe2acf43907bd9371.zip>

#### 版本 5.7.4

* 由于 Surge Ponte 所依赖的公共 STUN 服务器突然关闭，导致 Surge Ponte 无法使用，我们进行了紧急替换。此外，我们将在未来建立自己的 STUN 服务器，以避免此类问题。
* 增强与 VPN 和多网卡的兼容性

在之前的版本中，如果启用了增强模式，由于 Surge 覆盖了系统的路由表，所有出站数据包将被强制使用主接口。这绕过了路由表以避免创建循环。

然而，这也导致在有多个网卡或其他 VPN 的情况下，数据包无法从正确的接口发送的问题。

本版本改进了这一设计。现在，在增强模式下，如果存在更高优先级的子路由，Surge 将自动检查路由，并仍然对 TCP/UDP 数据包使用标准路由，从而提高兼容性。

* 修复包含重复 DOMAIN 和 DOMAIN-SUFFIX 规则时可能导致 DOMAIN-SUFFIX 规则失效的问题。
* 其他错误修复。

<https://dl.nssurge.com/mac/v5/Surge-5.7.4-2806-afe67661ef616b7bbab189dec1473b68.zip>

#### 版本 5.7.3

* 现在可以在规则列表中看到某条规则被使用的次数
* 优化了阻拦 QUIC 流量的实现方法，以提高让客户端正确回退的可能性
* Smart 组当不存在子策略时，也会使用 SUBSTITUTE 策略(DIRECT)而非直接失败。
* 修正 TLS 类协议，在 sni=off 的设置下，server-cert-fingerprint-sha256 参数未能生效的问题
* 新增规则类型 HOSTNAME-TYPE，用于判断请求的主机名的类型，可选值有：IPv4, IPv6, DOMAIN, SIMPLE。（SIMPLE 指的是不包含 . 的主机名，如 localhost）
* 优化了 DNS 的请求日志，现在会显示更多的信息，且在规则系统未触发 DNS 时，如果是 DIRECT 策略直连也可以显示 DNS 的相关日志了
* 在删除策略时，如果该策略被策略组所使用，现在允许直接删除并将自动从所有策略组移除

<https://dl.nssurge.com/mac/v5/Surge-5.7.3-2785-048c0bdc5ee2b05dab39852d51a19ff4.zip>

#### 版本 5.7.2

* 优化规则集中 ASN 规则的匹配性能
* 修复无法通过 UI 编辑 FINAL 规则的问题
* 修复无效的 cron 表达式会导致脚本被重复执行的问题
* 优化了脚本引擎的管理机制
* 其他小问题修复

<https://dl.nssurge.com/mac/v5/Surge-5.7.2-2762-9a963758f386b5da00e7744b2a7f254d.zip>

#### 版本 5.7.1

* 优化小型规则集的匹配性能，在旧型号 CPU 上效果尤为明显
* 外置资源更新页面可以显示规则集处理产生的错误信息
* 自动忽略规则集中的无效空行
* 修正应用临时规则后，如果产生了策略变化，不会打断原有连接的问题
* 修正在 Smart 组内使用 Ponte 策略时，如果目标设备是自身，未能自动转换为 DIRECT 策略的问题
* 修正 Ponte 设备请求在请求日志中显示的时间错误的问题
* 修正当外部策略组产生变化时，可能导致的崩溃
* 修正配置升级功能未能对托管配置和企业配置正确生效的问题
* 在 Smart 组初始化阶段，不再显示最常使用标签，以避免产生误解
* 修正在建立策略组时，如果勾选了外部策略但是没有填写 URL，会导致崩溃的问题
* 修正密钥库管理页面，进行移动操作后的项目未能正确显示存储位置的问题

<https://dl.nssurge.com/mac/v5/Surge-5.7.1-2757-e7b680d5dc23e1258188adc4d81116d7.zip>

#### 版本 5.7.0

**Smart Group**

这是一种全新的策略组类型，由我们精心设计的算法引擎所驱动，可以自动从该策略组的子策略中选择合适的策略。Smart 策略组的目标是取代原有的自动测试组（url/load-balance/fallback），大幅优化体验的同时，尽可能减少用户需要手动干预策略组的情况，用户只需将可用策略放入该组即可。

详情请见：<https://kb.nssurge.com/surge-knowledge-base/v/zh/guidelines/smart-group>

**规则系统**

* 规则系统整体性能优化。
* 大幅优化大型域名规则集中的索引算法，对于十万条以上的规则集，检索效率提高了十倍以上。
* 修正规则集内的逻辑规则的子规则无法被规则集的 no-resolve 和 extended-matching 参数覆盖的问题
* 新增规则类型 DOMAIN-WILDCARD，支持 ? 与 \* 匹配域名
* DOMAIN-SET 与 RULE-SET 改为强校验，当文件中包含无效行时将导致整个规则集无效，以避免误用产生问题

**IPv6**

* ipv6-vif 参数行为修改，当设置为 always 时，即使未设置 ipv6=true，也会开启 IPv6 功能。
* 为 ipv6-vif=always 参数增加了警告
* 调整了自动重试机制，在非 IPv6 网络下访问 IPv6 地址不再会进入重试流程，请求会立刻失败（以此解决在非 IPv6 环境下开启 IPv6 VIF 造成部分应用卡顿的问题，如微信和淘宝，但是应用仍然会持续发出 IPv6 请求）

**其他优化**

* $notification.post 增强，新增媒体资源支持、声音提示和自动消除。
* 优化 WireGuard 失败处理
* 降低 TUIC 协议在休眠时对电量的消耗
* 请求日志系统时间统计精度提高，现在可精确到 µs 级
* 优化各种异常的重试机制，避免在出现一些特定问题时持续重试导致高资源占用。对于需要持续重试的操作（如 WireGuard 重连、Ponte 服务端上报 iCloud），现在 Surge 会在出错后的 0.1s, 0.5s, 1s, 5s, 10s, 30s 后重试。
* 优化外部资源的缓存系统
* 新增配置文件行命令 #!REQUIREMENT

**细节调整**

* 限制了脚本在 debug 模式下，可以往请求 notes 中写入的日志的长度
* 默认 UDP 测试目标改为 1.0.0.1
* 在脚本中使用 API 时如果传入了错误类型的字段，将产生脚本异常
* 当脚本已完成或超时后，未完成的 $httpClient 不再会调用回调函数

**问题修正**

* 修正 Dashboard 查看远端设备时，无法读取截取的 HTTP Body 的问题
* 修正 Header Rewrite 规则无法根据 Host 字段进行 URL 匹配的问题
* 修正了在测试代理时，ip-version 和 tos 参数无法生效的问题
* 修正通过 HTTP-API 执行脚本时，若果错误的传入 null 会导致崩溃的问题

<https://dl.nssurge.com/mac/v5/Surge-5.7.0-2724-acaafccea020f6afdc758c83057ffcbb.zip>

#### 版本 5.6.0

**新功能**

* Mock (本地映射) 功能全面增强。
  * 新增数据类型如 `text`, `tiny-gif`, `base64` 以便直接内联返回数据。
  * 新增 `status-code` 参数
  * UI 相关配置尚未更新。使用方法见文档：<https://manual.nssurge.com/http-processing/mock.html>
* 当配置了参数 `encrypted-dns-follow-outbound-mode=true`，如果 DoH/DoQ/DoH3 连接匹配到使用域名的代理服务器，并且该代理服务器的域名存在 DNS 本地映射记录含有 IP 地址或传统 DNS 服务器，则允许通过该代理服务器查询。（通过代理服务器查询 DNS 会破坏 CDN 优化，导致加载图片和视频时严重缓慢。除非有非常特殊的需求并且不必这样配置，应使用域规则确保请求直接由代理服务器查询。）
* 新增 Body Rewrite 功能，详情见文档：<https://manual.nssurge.com/http-processing/body-rewrite.html>
* 新增对 STUN 数据包的识别，可使用 PROTOCOL,STUN 进行匹配。类似 QUIC，为确保兼容性，PROTOCOL,UDP 也可继续匹配 STUN 流量。

**增强**

* 优化请求日志记录。现在将显示匹配到的 URL Rewrite 和 Header Rewrite 的具体规则。
* 调整了 DNS 引擎处理空结果的逻辑。现在当配置了多个 DNS 服务器时，不再等待所有服务器响应空结果，以避免在 AAAA 记录不存在时产生额外等待。（然而，由于 DNS 服务器在不同环境下的表现可能有所不同，观察此更改是否引起副作用；如果出现问题导致异常结果，请提供反馈。）
* 取消了 ICMP 超限时的警告通知

#### 修正

* 增强了 HTTP Body 解压时的兼容性。
* 修正了 Surge 由于传入某些错误类型的参数而导致的崩溃。
* 适应新系统限制，修正了在某些情况下选择显示主窗口无效的问题
* 修正了代理模式下非 https WebSocket 与新版 Safari 的兼容性问题

<https://dl.nssurge.com/mac/v5/Surge-5.6.0-2611-efc3b7ebb3872061e9a6a4917742e203.zip>

#### 版本 5.5.0

**模块**

* 新增了多个新的官方模块；现在可以动态更新官方模块了。
* 模块新增了一个用于在 UI 中便捷访问和分类的分类字段。
* 模块现在接受参数表，支持多个参数。参数将用于通过文本替换修改模块内容。

**脚本**

* 新的脚本执行引擎。优化了执行性能和内存使用。
* $httpClient 增加了几个实用参数。 有关上述更新的更多详情，请参阅文档。

**增强功能**

* 新参数：always-raw-tcp-keywords。使用方法，请参见文档。
* 增加了 SRC-PORT 规则用于匹配客户端端口号。
* IN-PORT/SRC-PORT/DEST-PORT 三条规则被归类为端口号规则类型，支持三种表达式：
  * 直接写端口号，如 IN-PORT,6153
  * 端口号闭区间：如 DEST-PORT,10000-20000
  * 使用 >, <, <=, >= 操作符，如 SRC-PORT,>=50000
* UI 现在可以在编辑后保持原始配置中的纯空行。

**修复**

* 修正了 QUIC 流量控制的一个细节问题并针对 Ponte/TUIC/Hysteria2 协议优化了延迟性能。
* 编辑单个规则后，通知相关参数将被保留。

<https://dl.nssurge.com/mac/v5/Surge-5.5.0-2586-ed7ce88d6b2a286537ff5402324cb7fe.zip>

#### 版本 5.4.3

* 重写了虚拟 IP 数据库，现在数据库可以基于最后一次使用时间自动清理数据。
* 修复了在使用 Snell v4 与 WireGuard 并启用复用时可能出现的一些问题。
* 对于带有非法域名的 DNS 请求，将生成一个空结果响应，而不是被直接忽略。
* `tun-included-routes` 和 `tun-excluded-routes` 参数现在支持在启用 IPv6 VIF 时使用 IPv6 CIDR 块。
* 支持为内置规则集/内联规则集配置 no-resolve。
* Surge Ponte 连接不再验证对等地址，以确保在某些特殊场景下的正常运行。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.3-2540-511d4692c27626166bbcbb61fdd56bc8.zip>

#### 版本 5.4.2

* 修复了内置规则集 LAN 无法正确触发 DNS 解析的问题。
* 修复了处理某些格式错误的 UDP 包时可能导致崩溃的问题。
* 修复了一个系统可能错误判断已经重启，导致 Fake IP 表被清除的问题。
* 修复了与特定 HTTP 服务器的兼容性问题。
* 兼容了一些非标准 SOCKS5 UDP 服务器实现，将错误调整为警告。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.2-2502-001dc6b9672b7e79f92ca5cd3be6baf2.zip>

#### 版本 5.4.1

**规则引擎优化**

RULE-SET 与 DOMAIN-SET 的实现完全重写，现在 Surge 会在资源更新时自动对规则集进行预处理，建立索引数据结构，大幅提高匹配速度。

1. RULE-SET 和 DOMAIN-SET 两种类型规则集不再有性能和内存占用区别，可以随意使用。
2. DOMAIN-SET 规则集不再存在不可以使用 eTLD 的限制。
3. RULE-SET 中的 DOMAIN, DOMAIN-SUFFIX, IP-CIDR, IP-CIDR6 规则匹配速度得到大幅提升。
   * 十万条左右的 DOMAIN/DOMAIN-SUFFIX 规则集，在旧版中单次匹配需要 100ms，现在只需要个位数 ms。
   * 一万条左右的 IP-CIDR 规则集，在旧版中单次匹配需要约 0.1ms。新版只需要0.0002ms，提升了约 500 倍。IP-CIDR6 规则的性能提升幅度更高。
4. 在新版本中，自行通过 IP-CIDR 规则集构建出地区的 IP 地址集合，与直接使用内部的 GEOIP 规则的性能已经完全一致。
5. 先前版本加入的 Inline Ruleset 无法享受该优化，但是在百条数量级下几乎无差异。
6. 先前版本中，Ruleset 中的规则也是按照从上至下的方式逐条匹配，如果规则集中同时包含了需要 DNS 解析的规则，也只有当开始匹配该子规则时才会触发 DNS。新版本中，只要规则集中包含任意一条需要 DNS 解析的规则，在测试该规则集前就会先进行 DNS 解析。（绝大多数情况下没有任何区别）

* 主规则匹配效率小幅优化。
* IP-CIDR6 规则在非索引情况下的效率也得到大幅提升。
* RULE-SET 规则可直接配置参数 no-resolve 和 extended-matching，均等价于为所有子规则配置了该参数。
* DOMAIN-SET 规则集也支持配置 extended-matching。

**Minor Optimizations**

* MITM 时发送签名所使用的证书（证书链），以支持使用 intermediate 证书作为签发证书。
* 行首与行末注释，现在可以随意使用 `#` `//` `;` 等三种常见写法
* 配置文件错误消息提示优化，现在它可以更准确地给出发生错误的确切行号。
* 优化 Surge Ponte 错误处理流程，修正某些错误下不会自动更新设备信息的问题
* Bug 修正。

<https://dl.nssurge.com/mac/v5/Surge-5.4.1-2495-041f47425e9ecf56580562ce01560448.zip>

#### 版本 5.4.0

**新功能**

* 协议嗅探

  发往 80 与 443 端口的请求，会等待客户端发送第一个数据包后，提取 SNI 等信息用于规则系统判断。

  * `DOMAIN`、`DOMAIN-SUFFIX`、`DOMAIN-KEYWORD` 规则新增可选参数 `extended-matching`。开启该参数后，该规则将同时尝试匹配 SNI 和 HTTP Host Header （或 :authority）中的字段。
  * 新增参数 `always-raw-tcp-hosts`，用于强行关闭对特定主机名的主动协议探测。
* 新代理协议支持：Hysteria 2

  Hysteria 2 是一个为不稳定和容易丢包的网络环境所优化的代理协议，基于 UDP/QUIC。
* 自动 QUIC 阻止

  由于大部分代理协议并不适合用于转发 QUIC 流量，现在 Surge 会自动阻止 QUIC 流量使其回退 HTTPS/TCP 协议，以保证性能，对于命中了 MITM 主机名的 QUIC 流量，同样将自动拒绝。
* QUIC 类协议的 ECN (Explicit Congestion Notification) 支持

  显著改善了 Vector(Surge Ponte)/TUIC/Hysteria 2 协议的性能表现。

**优化**

* 重新设计了 HTTP 捕获功能
  * 相关设置不再存储在配置中，`[Replica]` 部分已被弃用。
  * 在打开捕获开关后增加了一个自动关闭设置，可以根据时间、大小或请求次数自动停止捕获。
  * 在打开捕获开关后增加了自动激活 MITM，可以额外为特定主机名打开。 (即使主 MITM 开关关闭)。
  * 增加了在打开捕获开关后仅保存 HTTP/HTTPS 请求的选项。
* 提高了与某些非标准协议的兼容性。
* 在测试 Ponte 策略时，测试 URL 已从 `proxy-test-url` 更改为 `internet-test-url`。
* 按照 WireGuard 协议标准推荐，现在 WireGuard 握手数据包将被标记为 0x88 (AF41) DSCP 以提高成功率。
* 当通过 WireGuard 转发 UDP 数据包时，它支持保留隧道内数据包的 TOS(DSCP/ECN) 标签。
* 根据 WireGuard 协议标准推荐，Surge 将从隧道内的数据包复制 ECN 标签到外部数据包。收到带有 ECN 标签的数据包时，它们将根据 RFC6040 严格合并。 (`ecn=true` 必须为策略设置)。
* UDP NAT 可以根据 ICMP 消息提前关闭 UDP 会话。
* 改进了 QUIC 的 PMTU 支持。

**Bug 修复**

* 修复了规则集的外部资源需要重新加载才能在更新后生效的问题。
* 在网络切换后，它将强制断开原始的 DoH/DoQ/DoH3 长连接，以避免获得不适合当前网络环境的结果。
* 修复了无效证书可能导致密钥存储界面崩溃的问题。
* 在对直接使用 IP 地址进行连接的 HTTPS 请求执行 MITM 时，不应将 IP 地址发送为 SNI，因为这可能导致兼容性问题。
* 其他 bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.4.0-2470-d6f513ab6e647abc29490f1f3506667f.zip>

#### 版本 5.3.2

* Surge Mac 现已准备好支持 macOS Sonoma。
* 外部资源现在可以由 Surge iOS 远程管理和更新。
* 修复了位置权限请求不能正确触发的问题。
* Surge Web 仪表板升级到版本 2.0.4。
* 其他改进。

<https://dl.nssurge.com/mac/v5/Surge-5.3.2-2393-f4b3e5e9a7bc5b73106ace7b0776eefe.zip>

#### 版本 5.3.1

* Surge 仪表板现在可以直接为本地和远程 Surge 实例创建临时规则。
* Surge Web 仪表板现已升级到版本 2.0。
* 添加了 Inline Ruleset，允许直接在主配置文件中编写 Ruleset。
* 模块增强。模块现在可以操作 \[WireGuard \*] 和 \[Ruleset \*] 部分。
* 添加了用于获取 CA 证书（DER 格式）的 HTTP API：GET /v1/mitm/ca。
* 修复了 MITM 失败记录无法正确生成的问题。

<https://dl.nssurge.com/mac/v5/Surge-5.3.1-2383-066f883d96a472655c9ea7be50475b8b.zip>

#### 版本 5.3.0

* 现在您可以直接通过 Surge Ponte 访问已注册设备的远程仪表板。
* Surge 仪表板现在可以操作远程设备的策略组和出站选项。
* macOS Sonoma 现在需要位置权限以获取 SSID。如果使用相关规则和子网设置，Surge 将提示位置权限。
* 修复了策略组的覆盖不能被远程取消的 bug。
* 更正了 VIF 和特定设备之间的兼容性问题。
* Surge Ponte 改进。

<https://dl.nssurge.com/mac/v5/Surge-5.3.0-2375-bc1b4791973df9aba493c3190a7b0050.zip>

#### 版本 5.2.3

* 您现在可以基于现有的配置文件创建一个新的可修改的配置文件。在这个新的配置文件中，选中的部分将引用原始配置文件中的相应内容，并自动与原始配置文件同步。同时，新配置文件中未选中的部分可以自由修改，不受原始配置文件的影响。（用于分离配置文件功能的 UI。）
* 分离的配置文件现在可以包括企业配置文件。
* 修复了当 SSH 服务器配置了横幅时无法连接的问题。
* 您现在可以使用 UI 来编辑 ShadowTLS 参数。
* 优化 ARM64 架构下的 VIF v1 模式的性能。当 VIF 模式设置为自动时，新版本将在 M1/M2 处理器下自动使用 v1 引擎，最大性能为 \~8Gbps，从而避免兼容性和稳定性问题。
* 纠正了 Dashboard 主窗口的打开位置可能不正确的问题。

<https://dl.nssurge.com/mac/v5/Surge-5.2.3-2354-ce8606235be8df196c0e9619a9c8cbbd.zip>

#### 版本 5.2.2

* 修复了在没有有效网络时可能会有关于系统代理设置被其他应用程序修改的错误提示的问题。
* 修复了使用 TUIC v5 作为底层代理时可能出现的一些问题。
* 修复了当启用 WebSocket 时，如果直接使用 IPv6 地址作为 vmess 主机名，无法正确构建 WebSocket 请求的问题。
* 当 SOCKS5 服务器不支持 UDP 转发时，提供更清晰的错误提示。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.2.2-2340-74b1e55a52888040394976468a61d973.zip>

#### 版本 5.2.1

* Surge Ponte 现在可以在 NAT 类型不满足要求时以 LAN-only 模式工作。同一 LAN 上的设备仍然可以访问。
* 在上一个版本中添加的连接限制器机制已被暂时移除。
* 优化设置为系统代理功能的逻辑。
* 修复了一个内存泄漏问题。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.2.1-2333-ef97cd79e935d838387dc99712fb38b3.zip>

#### 版本 5.2.0

* 由于 macOS 网络栈内存的大小固定，当网络栈缓冲区耗尽时，内核将自动关闭占用最高的程序以释放资源。使用 Surge 接管 P2P 下载器时可能出现这个问题。此版本将自动检查此问题并自动进入安全模式。
* Surge VIF 引擎已升级至 v3，不再依赖 Packet Filter (pf)，解决了与虚拟机和网络共享功能的兼容性问题。同时，增加了连接数限制，以避免由过多并发请求导致的系统资源耗尽。
* 为单个进程和单个设备添加了连接限制器，以避免个别设备消耗大量资源。
* 支持 QUIC 的 PMTU 发现，提高了 Surge Ponte 和 TUIC 协议的性能。
* 优化了基于 QUIC 的协议的错误处理逻辑。
* 使用 TUIC v5 转发 UDP 数据包时，遵循 IP 数据包的 DF 标志。避免了使用 TUIC v5 访问 QUIC 网站时可能出现的问题。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.2.0-2302-721d7db5429609c5a54af922f045a509.zip>

#### 版本 5.1.1

* 增加了对 TUIC v5 协议的支持。
* 优化了 Surge Ponte/TUIC 的性能。
* 当策略组异常时，优化了请求 Note 的记录。
* 修复了在 MITM H2 模式下未正确进行连接复用的问题。
* 修复了 $httpClient/DoH 的请求可能有时会被误取消的问题。
* 调整了 Snell v4 协议的流量特性。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.1.1-2264-6f04d8ac1bbf1c91178a09124e45e37e.zip>

#### 版本 5.1.0

**Surge Ponte**

* Surge Ponte 支持跨 iCloud 账户共享。
* 修复了通过 Surge Ponte 或 TUIC 协议访问 HTTP/1.0 服务器时可能出现的问题（例如 ASUS 路由器管理页面）。

**界面**

* 图标库：您现在可以从约 7000 个图标的库中为您的设备选择图标。

**代理协议相关**

* 修复了 Snell V4 下复用功能无法正常工作的问题。
* SSH 协议现在支持服务器公钥指纹 pinning，查看手册以获取使用方法。

**脚本**

* $httpClient 支持二进制模式。
  * 请求的 body 支持 TypedArray。
  * 在请求参数中传入 binary-mode: true 允许返回结果作为 TypedArray 返回。
* 修复了 `http-request` 类型脚本无法直接使用二进制数据作为响应的问题。

**其他**

* 策略组添加了参数 `external-policy-modifier`，可用于调整外部策略。
* 优化了请求日志系统
  * 在日志中添加了类别标记。
  * 规则系统为 DNS 和规则集添加了更多输出。
* 其他 bug 修复和优化。

<https://dl.nssurge.com/mac/v5/Surge-5.1.0-2216-82115a08df678cfa87137a506f7df061.zip>

#### 版本 5.0.3

* 为 VMess 协议添加了 UDP 中继支持
  * 由于 VMess 服务器端默认支持 UDP 转发，因此无需添加额外参数即可使用。
  * 由于 VMess 协议的设计缺陷，当使用 VMess 转发 UDP 流量时，P2P 场景可能无法工作，如语音通话、在线游戏等。因此，不建议使用 VMess 协议。
* SSH 协议现在支持指定服务器的公钥指纹。查看手册获取更多信息。
* 现在通过 STUN 协议获取外部 IP 地址，不再依赖 api.my-ip.io。
* DDNS 现在在选择 IPv6 时使用安全的 IPv6 地址而非临时地址。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.3-2199-c241935acf37b3ec7f7fa4f5120e8690.zip>

#### 版本 5.0.2

* 由于 macOS 的新隐私限制，如果使用了与 Wi-Fi BSSID 相关的功能，Surge 将请求位置服务权限以读取 Wi-Fi BSSID。
* 现在支持 Shadow TLS v3。附加 `shadow-tls-version=3` 以启用它。
* Surge Mac 现在支持 Adaptive TLS Fingerprint。有关更多信息，请查看社区线程。
* 支持了一个新参数 `external-policy-modifier`，用于修改外部策略的参数。
* 新的代理客户端通知只有在接收到真正的请求时才会提示，被端口扫描时将不再显示。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.2-2186-2ab1aba0dc49688683b2e4d43200e468.zip>

#### 版本 5.0.1

* 当 Ponte 开关关闭时，现在可以查看已注册的 Ponte 设备视图。
* 修复了通过 USB 使用 Surge Dashboard 时的崩溃。
* $httpClient 现在支持二进制模式。
* Bug 修复。

<https://dl.nssurge.com/mac/v5/Surge-5.0.1-2162-22743a4d2f1e0aeb0b872e8f544c2e69.zip>

### Surge Mac v4

#### Version 4.11.2 (May 6, 2023)

* Replace the API service provider for obtaining external IP.

<https://dl.nssurge.com/mac/v4/Surge-4.11.2-2016-b4c9dad3472594b01ef3d8ac9b05c78e.zip>

#### Version 4.11.1 (Apr 15, 2023)

* Fixed a bug that Surge VIF v6 may not be enabled automatically when set to auto.
* Fixed a bug that requests sent by $httpClient may not obey the ip-version parameter of the selected policy.
* Fixed a bug that DDNS can’t be enabled if the user deleted the iCloud data of Surge.
* Fixed a bug that domain rules can’t match if the requests’ domain is in uppercase.
* Fixed a bug that the UI can’t add listeners in the advanced proxy service settings.
* Fixed a bug that the UI can’t add new items in the metered network SSID view.
* Fixed a WireGuard related crash.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.11.1-2013-eac717436d753b5ea2b82a206d5851e7.zip>

#### Version 4.10.3 (Feb 16, 2023)

* The installed modules are now synced between Mac devices via iCloud.
* Performance optimization.
* Fixed an issue that the DHCP service might not be able to start after auto-upgrading.
* Fixed an issue that the remove helper script can't be executed on macOS Ventura.
* Fixed menu bar icon issues when using multiple displays.
* WireGuard related optimizations.
* Support for customizing the reserved bits of WireGuard, also known as the client ID or routing ID.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.3-2004-d730cb305e3cbb949f82d01771624b4e.zip>

#### Version 4.10.2 (Feb 3, 2023)

* UDP performance optimization.
* Change the way connections are rejected from ICMP to TCP RST. This ensures that the Windows operating system can correctly detect the rejection.
* Fixed the proxy editing view layout issue.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.2-1981-d99d487bbd9f9109a00dd5a5b7915be4.zip>

#### Version 4.10.1 (Dec 3, 2022)

**New Feature**

* Gaming Optimization Mode: `udp-priority = true`. Enabling it will prioritize UDP packets when the system load is very high, and packet processing is delayed.
* SOCKS5 proxy now supports UDP forwarding, as the server side does not consistently support UDP forwarding, the parameter udp-relay=true needs to be explicitly configured.
* The `ipv6-vif` parameter now supports `always` and `auto` like Surge iOS. If set to `auto`, IPv6 VIF will only be enabled if a valid Internet IPv6 address (2000::/3) exists.

**Minor Improvements**

* URL regular expressions for Script, Rewrite, Mock, etc. will try to match URLs constructed in many different ways (e.g. Host field in Header) to solve the problem that some apps use custom DNS logic to request directly to IP addresses.
* Removed the silencing mechanism after UDP forwarding errors to avoid extra waiting time after switching networks.
* The IPv6 switch no longer prevents direct access to IPv6 addresses when turned off. The switch is now limited to controlling whether the DNS Client requests AAAA records.
* Automatic disabling of AAAA queries due to DNS issues will be prompted in the Event Center instead of just in the logs.
* Fixed handling issue of generating IPv6 fragmentation when forwarding IPv6 UDP packets via WireGuard.
* The external policy group will skip the line and continue processing when it encounters invalid content instead of returning an error directly.
* Adjusted the buffering mechanism of raw TCP forwarding to avoid conflicts with some apps.
* Fixed REJECT requests not being marked as failed under MITM H2.
* Adjusted the output text under diagnostics.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.10.1-1964-34ee4f3efbd20065ad808cf0cab6d380.zip>

#### Version 4.10.0 (Nov 10, 2022)

**Support New Proxy Protocol**

* New proxy protocol supported: TUIC. (<https://github.com/EAimTY/tuic>).
* New proxy protocol supported: Snell V4. (<https://manual.nssurge.com/others/snell.html>)
* New proxy transport layer protocol supported: Shadow TLS. (<https://github.com/ihciah/shadow-tls>). You may append `shadow-tls-password=pwd` to any proxy to utilize it.

**Other Improvements**

* shadowsocks now supports the none cipher.
* Modified the handshake packet construction logic when forwarding HTTPS requests to proxies, which can slightly optimize latency.
* Surge HTTP requests for proxy testing no longer contain a User-Agent header.
* A new option to allow to disable system processes combining in the process view.
* Fixes an issue on M1 processors where the system would move Surge to the efficiency core when using an application in full screen causing a significant drop in performance.

**Bug fixes**

* Fixed a memory leak that could occur when HTTP capturing is enabled.
* Fixed an issue that may not work properly when nesting proxy chains with a specific protocol combination.
* Fixed an issue that the module could not configure the MITM h2 parameter.

<https://dl.nssurge.com/mac/v4/Surge-4.10.0-1927-f009d35c5da9df00cccf818edd74b20d.zip>

#### Version 4.9.1 (Sep 29, 2022)

* Overall performance optimization.
* Added an alert when using router mode in an IPv6 network.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.1-1866-e90f4c1609827e5669c21803ac8e90a3.zip>

#### Version 4.9.0 (Sep 11, 2022)

**Router Mode**

* Overall performance optimization.
* Fixed a performance issue with PS5.

**Surge VIF IPv6**

* You may use the parameter `ipv6-vif = always` to let Surge configure IPv6 address and the default route for Surge VIF.
* Surge VIF now supports handling raw TCP and UDP traffic with IPv6.
* ICMPv6 relay is now supported.

**MITM**

* New parameter `client-source-address`. Use this parameter to enable the MITM function on some devices only.
  * It's a list parameter, using commas as the separator.
  * You may specify a single IP address or use a CIDR block, both IPv4 and IPv6 are supported.
  * You may use the `-` prefix to exclude some clients, e.g., `client-source-address = -192.168.1.2, 0.0.0.0/0`
  * If the parameter is not set, MITM is enabled for all clients. A equivalent to `client-source-address = 0.0.0.0/0, ::/0`
  * `127.0.0.1` should be included if you want to enable MITM for the current device.

**WireGuard**

* WireGuard now supports IPv6 tunneling.
  * Use parameter `self-ip-v6` to assign an IPv6 address for Surge.
  * You may configure `self-ip` and `self-ip-v6` to utilize the IPv4 & IPv6 dual stack, or just one of them to use the single stack.
  * Make sure to use the correct `dns-server` address for the enabled IP protocol version.
  * The `allowed-ips` parameter supports IPv6 CIDR now, e.g., `allowed-ips = 0.0.0.0/0, ::0/0`

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.9.0-1850-c52ab2531bb82ff6f8d72df65f65c76a.zip>

#### Version 4.8.0 (Aug 9, 2022)

**Experimental function: DNS over QUIC and DNS over HTTP/3**

* Surge now supports DNS over QUIC. (e.g.: `encrypted-dns-server = quic://example.com`)
* Surge now supports DNS over HTTP/3. (e.g.: `encrypted-dns-server = h3://example.com/dns-query`)
* Parameter `doh-server` renames to `encrypted-dns-server`.
* Parameter `doh-follow-outbound-mode` renames to `encrypted-dns-follow-outbound-mode`.
* Parameter `doh-skip-cert-verification` renames to `encrypted-dns-skip-cert-verification`.
* The DNS relay (`always-real-ip` and non-A/AAAA record lookup) in the Enhanced Mode now uses the encrypted DNS servers.
* You may use `encrypted-dns-skip-cert-verification=true` to disable server certificate verification for DNS-over-HTTPS.

**Scripting**

* New helper functions: `$utils.ipasn(ipAddress<String>)`, `$utils.ipaso(ipAddress<String>)` and `$utils.ungzip(binary<Uint8Array>)`.
* New subtype of the event script: `notification`. You may use a script to forward Surge notifications to a third-party message service.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.8.0-1788-3b96ac4d92f39b6a4a8e195708aae8d8.zip>

#### Version 4.7.0 (Jun 30, 2022)

**MITM over HTTP/2**

* Surge now supports performing MITM with HTTP/2 protocol to improve concurrent performance.
* Surge now supports performing MITM on WebSocket connections.

**Others**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.7.0-1757-0b3d1ec3c3f7067386361dd582ad964a.zip>

#### Version 4.6.1 (Jun 10, 2022)

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.1-1718-a39555f74c3f6d43fdcaa8501d55d26a.zip>

#### Version 4.6.0 (Jun 8, 2022)

**SSH Proxy Support**

* You can use SSH protocol as a proxy protocol. The feature is equivalent to the `ssh -D` command.
* Both password and public key authentications are supported.
* All the four types of private keys, RSA/ECDSA/ED25519/DSA, are supported.
* Surge only supports `curve25519-sha256` as the kex algorithm and `aes128-gcm` as the encryption algorithm. The SSH server must use OpenSSH v7.3 or above. (It should not be a problem since OpenSSH 7.3 was released on 2016-08-01.)

**Keystore**

* You may now save sensitive keystore items to the system keychain. (More, Profile, Manage Keystore)

**Others**

* New rule type: IP-ASN. You may use the rule to match the autonomous system number of the remote address.
* Dashboard now shows more details about the remote address, including the ASN.
* Surge will try to fix the system proxy settings after applying fails.
* You can now enable/disable the rewrite rules and DNS local mapping items.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.6.0-1708-9ef4eecae3a0cc5dfebd74e5e850cb2f.zip>

#### Version 4.5.2

**Dashboard**

* You can now export HTTP/HTTPS requests to a HAR file, which is a standard format and can be opened by many web analysis tools

**Proxy**

* New parameter `server-cert-fingerprint-sha256` for TLS proxy policies. Use a pinned server certificate instead of the standard X.509 validation.
* `tls-engine` option is now deprecated. OpenSSL is now the only TLS engine.
* You may use `%PROFILE_DIR%` in the external proxy arguments, which will be replaced to the path of the profile directory.
* You can now use a full profile as the external policy group (policy-path). All proxies in the \[Proxy] section will be used.

**DHCP Server**

* Surge DNS is now integrated with the DHCP device management. You can use a device name to get the IP address directly. Reverse IP lookup is also supported.
* The helper upgrade is now optional to prevent the interrupt after an auto-upgrade.
* Surge now can relaunch itself after a crash.

**CLI**

* surge-cli just got a refresh. Use `surge-cli --help` to know what you can do with it.

**Others**

* Header rewrite now supports using the regex to replace the value.
* Header rewrite now supports modifying the response headers.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.2-1663-d480512b326806e7e850f98efe875bec.zip>

#### Version 4.5.1

* There is a kernel bug in macOS 12.3, which significantly degrades performance of the Enhanced Mode and Router Mode. A workaround is deployed in this version.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.1-1621-c2a973ddb992df5c34757daacc632598.zip>

#### Version 4.5.0

**WireGuard**

* WireGuard supports multiple peers.
* The allowed-ips now support multiple IP ranges.
* WireGuard supports preshared-key and keepalive.
* WireGuard supports peers with IPv6 endpoints. (But still no IPv6 tunnel support)
* WireGuard and shadowsocks policy now support underlying-proxy.
* The raw TCP connections are now relayed on the L3 layer if no high-level features are used.

**Detached Profile**

* You can now include multiple detached profiles into one section. But the section will be marked read-only and can't be edited with UI.

`#!include A.dconf, B.dconf`

**Policy Group**

* You can now temporarily override an auto test group or an SSID group's optimal option, until Surge restart or reload.
* The new parameter include-all-proxies=true is added to the policy group, which will include all proxy policies defined in the \[Proxy] section, and can be used with the policy-regex-filter parameter for filtering.
* The new parameter include-other-group="group1,group2" is added to include policies from another policy group, and can include multiple policy groups separated by commas, also can be used with the policy-regex-filter parameter for filtering.
* include-all-proxies, include-other-group, and policy-path parameters are allowed to be used in a single policy group at the same time. The policy-regex-filter parameter applies to all three.
* There is an order of precedence among the policy groups for the include-other-group parameter, but there is no order of precedence among the include-all-proxies, include-other-group, and policy-path parameters. For scenarios where the order of sub-policies makes sense (e.g., fallback groups), use policy groups nesting with include-other-group.

**Subnet expression**

* SSID Group is now upgraded to Subnet Group, which supports subnet expression.
* SSID Setting now supports subnet expression.
* The SUBNET rule now supports subnet expression.
* A subnet expression can be one of these:
  * Use SSID:value to match the Wi-Fi SSID, wildcard character is allowed.
  * Use BSSID:value to match the Wi-Fi BSSID, wildcard character is allowed.
  * Use ROUTER:value to match the router IP address.
  * Use TYPE:WIFI to match all Wi-Fi networks.
  * Use TYPE:WIRED to match all wired networks.
  * Use TYPE:CELLULAR to match all cellular networks. (iOS Only)
  * Use MCCMNC:100-200 to match a cellular network. (iOS Only)
* The \[SSID Setting] can control the TCP Fast Open behavior now. Read the manual for more information.

**Others**

* Performance improvements.
* The default timeout of $httpClient is 5 seconds now.
* New Official Module: Block HTTP3/QUIC
* You can now adjust the effective order among modules.
* Modules allow to modify the skip-server-cert-verify and tcp-connection parameters of \[MITM].
* The client will get an ICMP connection refused message instead of TCP RST if a REJECT policy matches.
* Supports IPv6 addresses with scope ID.
* The Network diagnostics can test proxy UDP relay now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.5.0-1618-5d2042223762269c5322520810dd7e0c.zip>

#### Version 4.4.1

* You may click a proxy of a select group in the main menu with holding the Option key, to test the proxy alone.
* Fixed a bug that UDP NAT can't be released if a REJECT policy is matched.
* Other bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.1-1532-abe4b5471dcb3eaeec51fcda768cc635.zip>

#### Version 4.4.0

* Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy. More information: <https://manual.nssurge.com/policy/wireguard.html>
* Supports VmessAEAD. (Policy parameter: vmess-aead = true)
* Trojan protocol now supports UDP relay. (No additional parameter required)
* The underlying proxy now supports using a policy group.
* Performance optimization.
* Added a release note window to show update history.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.4.0-1521-a0024e9fbe33f5ccaa41316d63cdefee.zip>

#### Version 4.3.1

* Snell Protocol v3, which brings UDP over TCP relay support
  * Optimized for high throughput.
  * Port Restricted Cone NAT support. (aka NAT type 2)
* The http-response scripts can read request headers via $request.headers now.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.1-1461-829471a307259fe1729cf06a7cd13d06.zip>

#### Version 4.3.0

* Surge Dashboard now supports managing DHCP devices. All of the properties (name, icon, static IP address, gateway mode) can be edited locally and remotely.
* The traffic statistics data is now persistent between sessions. And you may use Dashboard to view all the detailed statistical data.
* The statistics data range is extended to 24 hours.
* Performance improvements.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.3.0-1430-bde27671bfdadfab143338a7cd5b2fa3.zip>

#### Version 4.2.5

* Performance improvements.
* Supports remote rule editing for Surge iOS remote controller.
* Kill other processes that take over port 53 when starting DHCP service.
* Surge now only executes reloading if the profile is valid.
* Supports custom the policy IP TOS field. Example: test-policy = direct, tos=0xb8.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.5-1414-764146258a319c307056593a1309cf89.zip>

#### Version 4.2.4

* New option: Menubar icon display mode. You can now hide the icon and display the real-time speed only, to save the precious menubar space.
* New HTTP API: GET /policies/benchmark\_results
* Supports IP Fragmentation for UDP and ICMP packets. (IP Fragmentation for TCP packets is already supported in the previous versions.)
* You can now right click on a remote client to add a new rule in the Dashboard.
* Performance improvements.
* Added a few device icons.
* The UI editor of policy group now supports filter and mixed policies.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.4-1399-4f3c53abfe45fce5646d84af11e589c4.zip>

#### Version 4.2.3

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.3-1357-0803594c82248360a95722089650f7f7.zip>

#### Version 4.2.2

* Supports binary mode for http-request and http-response scripts.
* DHCP can detect if a device is private address enabled now.
* Surge won't reload the profile automatically if the new profile is invalid.
* New local and remote notification selections: auto-updating and profile reloading.

<https://dl.nssurge.com/mac/v4/Surge-4.2.2-1351-5dc813192d6e37fdb0895034ebc90b57.zip>

#### Version 4.2.1

**External IP**

* You may now check the external IP address in the interfaces view.

**DDNS**

* Surge Mac can associate its external IP address to .sgddns hostname. You may use the hostname with Surge iOS or Surge Mac on another device. The data is synced via iCloud, and the hostname can't be used publicly.

**Others**

* Surge Mac now can fix the helper installtion issues automatically。

<https://dl.nssurge.com/mac/v4/Surge-4.2.1-1333-14f7cb7cd943be7e4b3cecfb3fcd8ba3.zip>

#### Version 4.2.0

**Web Dashboard**

* The community project YASD is now part of Surge. You can now control Surge via a web browser on local or remote devices. (Licensed by author @geekdada)
* You may now manage the DHCP devices with the Web Dashboard.

**Profile Syntax**

* We have added a profile syntax view to show all the available syntax for the current view if you prefer to edit profile with a text editor. You can find it in Help ▸ Profile Syntax.
* The Diagnostics now can report invalid config lines in the profile.

**Benchmark**

* We have changed the proxy benchmark standard. The result is now similar to a ping test result, which ignores the proxy setup cost.

**Minor Improvements**

* SOCKS proxy service now supports SOCKS4 and SOCKS4a protocol. (Server-side only)
* Cloud Notifications now supports rule notifications.
* The real-time speed is now available on the proxy view.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.2.0-1321-d4d84696bb58cf8be0189b59ccbe926b.zip>

#### Version 4.1.0

**Scripting**

* You may configure and edit scripts with UI now.

**Profile**

* You may put partial sections into a detached file. See <https://manual.nssurge.com/overview/configuration.html>

**HTTP API**

* Added new profile related HTTP APIs, including GET /profiles, POST /profiles/check
* Added new device management HTTP APIs, including GET /devices, POST /devices, GET /devices/icon
* The HTTP API, proxy services, and external controller now support listening on IPv6 addresses. (No UI supports. Manual profile editing is required.)
* You may now use 'http-api-tls=true' enable TLS for HTTP API access. (aka HTTPS-API)

**Unsupervised Optimizations**

* The external resources downloading now occurs after surge engine started.
* The external resources downloading now automatically starts after if a resource is not ready.

**Other Improvments**

* New rule type: SUBNET, which can match SSID/BSSID/router IP address with a wildcard pattern.
* Significantly optimizes Dashboard performance when handling large numbers of requests.

<https://dl.nssurge.com/mac/v4/Surge-4.1.0-1298-f07b1b8713b2397518f4b252b5786452.zip>

#### Version 4.0.5

**Policy Group**

In this release, we completely refactored the policy group functionality, bringing the following changes:

1. The url-test/fallback/load-balance policy group can no longer be configured with a specific testing URL but with a global testing URL or a policy-configured testing URL. The policy's test results can be used directly in all policy group decisions, eliminating the need to retest each policy group individually.
2. All types of policy groups support mixed nesting. The only requirement is that no circular references can be used.
3. When a group policy is used as a sub-policy of the url-test/fallback/load-balance group.
   * The latency of the select/url-test/fallback/ssid group is the latency of the selected policy.
   * The latency of the load-balance group is the average of the latencies of all available policies.
4. The timeout parameter of a policy group marks policies with latency exceeding this parameter as unavailable when making decisions for the group. But the maximum time taken to test the policy group is controlled by the global test-timeout parameter. (Default is 5s)
5. When testing a group due to decision making, all sub-policies that the group may use are tested, including sub-policies of the sub-policy group.
6. You may use no-alert=true parameter to suppress notifications for particular groups.

**Cloud Notification**

You can receive the notifications on iOS devices. Enable this option first and then configure it on Surge iOS. The two device must use a same iCloud account.

**Minor Changes**

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.5-1262-db70f680cd0f15236c8415ec7b804c3a.zip>

#### Version 4.0.4

* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.4-1227-9acb8b9e3f39e9048fc82e427184a4af.zip>

#### Version 4.0.3

* You may override the testing URL of a policy for network diagnostics and activity cards.
* The GeoIP database can be updated automatically in the background.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.3-1224-4ef8ae10c8a74c395bb4b6c3f6af6af6.zip>

#### Version 4.0.2

* You may now customize the GeoIP database updating URL.
* tun-excluded-routes and tun-included-routes are now available for Surge Mac.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.2-1219-dbd08724b90aa8b444cd6d0679a245b5.zip>

#### Version 4.0.1

* You may configure the proxy chain with the UI now.
* Fixed some visual inconsistency under reducing transparency mode.
* Bug fixes.

<https://dl.nssurge.com/mac/v4/Surge-4.0.1-1207-ee7bea1b244950c82a6f90e060fa2d89.zip>

#### Version 4.0.0

* The first version of 4.0.0.

<https://dl.nssurge.com/mac/v4/Surge-4.0.0-1191-d8140b0084223fd3fc4335e4414c0884.zip>

### Surge Mac V3

#### Version 3.5.8

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.8-1130.zip>

#### Version 3.5.7

* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.5.7-1129.zip>

#### Version 3.5.5

**Minor Changes**

* All URL resources now support URLs with a username and password (e.g. <https://user:pass@example.com>), including managed profile, external resources, and importing profile form URL.
* You may switch among the main views with shortcut keys.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.5-1123.zip>

#### Version 3.5.4

**Changes in Policy Group**

* New parameter: policy-regex-filter. If the parameter is configured, only matched policy line will be used.

**Minor Changes**

* Provides more details for the TLS handshake error.
* Increases the file description limitation alert threshold.

<https://dl.nssurge.com/mac/v3/Surge-3.5.4-1119.zip>

#### Version 3.5.3

**New Parameter: use-local-host-item-for-proxy**

`[General]`

`use-local-host-item-for-proxy = true`

If use-local-host-item-for-proxy is true, Surge sends the proxy request with the IP address defined in the \[Host] section, instead of the original domain.

**Changes in Load Balance Group**

* load-balance group now supports connectivity testing before being used. Add 'url' parameter to enable it.
* Parameters 'timeout', 'interval' and 'evaluate-before-use' are also available.

**Minor Changes**

* Surge will send an ICMP port unreachable message if UDP forwarding fails.
* Eliminate unnecessary local DNS lookup while forwarding UDP traffic to a proxy server.
* Fixed a bug that connecting to Surge iOS via USB is not working in Surge Dashboard.

<https://dl.nssurge.com/mac/v3/Surge-3.5.3-1094.zip>

#### Version 3.5.2

**SSID Suspend**

* Surge Mac supports SSID suspend now. The system proxy and enhanced mode will be temporarily suspended under specified SSIDs.
* The name of WiFi can be an SSID, a BSSID, or a gateway IP address.
* No UI configuration in the current version.

**REJECT-DROP**

* REJECT-DROP policy is now effective to proxy connections. The connections matched with a REJECT-DROP policy will be closed in 60-120s later without any data returned.

**Global Proxy**

* You may now select and view sub-policy for policy groups while using the global proxy mode.

<https://dl.nssurge.com/mac/v3/Surge-3.5.2-1082.zip>

#### Version 3.5.1

**New rule type: DOMAIN-SET**

* DOMAIN-SET is just like RULE-SET. But it is designed a large number of rules and highly efficient.
* Unlike RULE-SET, you can only write hostnames (domain or IP address) in it. One hostname per line.
* You may use "." prefix to include all sub-domains.

**Changes in SRC-IP**

* SRC-IP rule now supports IP-CIDR for both IPv4 and IPv6.

**Changes in DNS over HTTPS**

* From this version, if DNS-over-HTTPS is configured, the traditional DNS will only be used to test the connectivity and resolve the domain in the DOH URL.
* The DNS over HTTPS now has a separate parameter: doh-server. The DOH servers in 'dns-server' will be moved to the new parameter after saving.
* The legacy DNS is always required now.
* DOH can be matched with rule 'PROTOCOL,DOH' now.
* Added a new parameter 'doh-follow-outbound-mode'. In the previous version, the DOH client follows the system proxy settings. From this version, all DOH requests will use DIRECT policy by default. If 'doh-follow-outbound-mode' is set, the DOH requests will follow the outbound mode settings regardless of the system proxy settings.
* We are refactoring the HTTP client for DOH and scripting. Please feedback if you encounter any issue.

**Changes in Scripting**

* Added a simple view to test the script. You may find it in the Window menu.

**Minor Changes**

* Fixed a crash in Dashboard while using search.
* Bug fixes.

**Known Issues**

* You may not configure DOH with UI in this version temporarily.

<https://dl.nssurge.com/mac/v3/Surge-3.5.1-1069.zip>

#### Version 3.5.0

* New feature: Module, which can override the current profile with a set of settings. Highly flexible for diverse purposes. See the post in the community for more information: <https://community.nssurge.com/d/225-module>.
* You may enable modules in the menu now.
* You may view the detail of a module by double clicking.
* Supports pattern filter for Dashboard requests.
* Added a new rule type: PROTOCOL. The possible values are HTTP, HTTPS, SOCKS, SNELL, TCP, UDP.
* You may now use UI to add and edit load-balance group.
  * DNS over HTTP (DoH) now uses DNS wireformat by default. You may configure doh-format=json in \[General] to continue using JSON format.
  * TCP connection setup optimizations.
  * Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.5.0-1039.zip>

#### Version 3.4.0

* Snell protocol now upgrade to version 2, supporting to reuse TCP connections to improve performance. <https://github.com/surge-networks/snell/releases>
* Supports a new proxy protocol: Trojan.
* Remote Dashboard now upgraded to Remote Controller. You may use Surge iOS to select policy group, toggle HTTP capture/MitM, and switch outbound mode remotely.
* The comment lines in the text config won't lost after editing with UI.
* You may open the new connection window of Dashboard by holding the Option key while clicking the Dashboard item in the main menu.
* Supports to use OpenSSL as TLS provider. See the post in the community for more information: <https://community.nssurge.com/d/196-surge-ios-mac-tls-provider>.
* Fixed a bug that Surge may not be able to process DNS answer packets which is longer than 512 bytes.

<https://dl.nssurge.com/mac/v3/Surge-3.4.0-989.zip>

#### Version 3.3.3

* Fixed a bug which causes TFO failed.
* You may use a profile which stores in a subdirectory of the profile directory.
* Added Traditional Chinese localizations.
* Fixed a bug that the menu might be unresponsive.
* Fixed crashs on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.3.3-939.zip>

#### Version 3.3.2

* Supports MITM on non-standard port for TCP mode.
* Proxy editing view now supports VMess protocol and all misc options.
* A new option 'persistent' has been added to the load-balance group. (aka PCC, per connection classifier) When 'persistent=true' is set, a same hostname will always get the same policy.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.3.2-925.zip>

#### Version 3.3.1

* Supports VMess proxy protocol.
  * vmess-proxy= vmess, example.com, 443, username = 12345678-abcd-1234-1234-47ffca0ce229, ws=true, tls=true, ws-path=/v2, ws-headers=X-Header-1:value|X-Header-2:value
  * All proxy options for TLS proxy are available.
  * Web-socket and TLS options would degrade performance. Only enable when necessary.
  * Surge only supports chacha20-poly1305 encryption algorithm. Please make sure the server supports it. We have no plan to implement other ciphers.

<https://dl.nssurge.com/mac/v3/Surge-3.3.1-906.zip>

#### Version 3.3.0

* The scripting has been rewritten totally. The old scripts are not compatible with this version. See <https://community.nssurge.com/d/33-scripting/3>
* Added support for TLS 1.3. Append 'tls13=true' to the proxy line to enable it. (Requires macOS 10.14 or above)
* Supports to use 'X-Surge-Policy' to force policy for HTTP/HTTPS requests.
* SSID group now supports to use the IP address of default router as an identifier.
* New policy group type: load-balance, which will use a random sub-policy for every request.
* Supports DNS over HTTPS. More information in community: <https://community.nssurge.com/d/48-dns-over-http>
* IN-PORT and DEST-PORT rule now supports port range expression: `DEST-PORT,8000-8999,DIRECT`
* Provides compatibility for Surge iOS 4.
* Surge Mac software package is now notarized by Apple.
* A new standalone view to manage all external resources.

<https://dl.nssurge.com/mac/v3/Surge-3.3.0-893.zip>

#### Version 3.2.1

* Fixed a bug that Handoff doesn't work between Surge iOS and Dashboard.
* Fixed a bug that 'Update All Remote Resources' may not work.

<https://dl.nssurge.com/mac/v3/Surge-3.2.1-863.zip>

#### Version 3.2.0

**Scripting**

* New major feature: scripting. You may use JavaScript to modify the response as you wish. See the manual for more information: <https://manual.nssurge.com/http-processing/scripting.html>
* You can now use a script to modify the response headers and status code.

**Dashboard**

* USB module has been refactored to improve stability. Also, you may choose the device from multiple USB devices now.

**MitM**

* HTTP and MitM engine has been refactored. Please report if you encounter any issues.
* You can now use URL-REGEX rule for MitM connections.
* You may use prefix '-' to exclude domains for MitM. Example:

```
[MITM]
hostname = -*.apple.com, -*.icloud.com, *
```

* MitM hostname list now supports port number. By default only the connections to port 443 will be decrypted. Use suffix :port to enable MitM for other ports. Use suffix :0 to enable MitM for all ports on the hostname.
* URL rewrite type 'header' is now available for MitM connections. You may also use it to rewrite a plain HTTP request to an HTTPS request.

**Misc**

* You can now enable/disable a rule.
* Added a small indicator in the menu icon for Metered Network Mode.
* Added main switches for rewrite and scripting.
* Supports TCP SACKs for Surge VIF.
* New general option: force-http-engine-hosts. You can force Surge to treat a raw TCP connection as an HTTP connection, to enable high-level functions such as URL-REGEX rules, rewrite and scripting. This option uses the same format as \[MITM] hostname option.
* New option for url-test/fallback group: evaluate-before-use. By default, the requests before a connection evaluation will use the first policy in the list and trigger the evaluate. Enable the option to delay the requests until the evaluation completed.

<https://dl.nssurge.com/mac/v3/Surge-3.2.0-860.zip>

#### Version 3.1.1

* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.1-811.zip>

#### Version 3.1.0

* Added more feature to the main menu.
* Dashboard now supports to export all requests to an archive file for opening later or sharing.
* Supports a new proxy protocol: Snell. (<https://github.com/surge-networks/snell>)
* Surge Mac can work as a Snell proxy server now. See <https://manual.nssurge.com/others/snell-server.html> for more information.
* A new option to automatically reload if the profile was modified externally/remotely.
* Fixed a compatibility issue with some FTP clients.
* Added a new option to disable automatically notification dismissing.
* The update notification is now shown as a banner instead of an alert window.
* Bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.1.0-807.zip>

#### Version 3.0.6

* Optimizations for no network error handling.
* Reduces CPU usage on idle.
* Fixed a bug while enabling MitM with a new certificate.
* Fixed crashes on macOS 10.11.

<https://dl.nssurge.com/mac/v3/Surge-3.0.6-781.zip>

#### Version 3.0.5

* CPU usage optimizations (50% reduced for high throughout).
* Enabled Hardened Runtime to get enhanced security protections in macOS Mojave.
* Add more notes for rule evaluating stage.
* WeChat.app may flood ping when network is unstable, which causes a high CPU usage of Surge. We added a mechanism to limit ICMP throughput in this version.

<https://dl.nssurge.com/mac/v3/Surge-3.0.5-773.zip>

#### Version 3.0.4

* Added a new option 'hijack-dns' to hijack DNS queries to other DNS servers with fake IP addresses. See manual for more information: <https://manual.nssurge.com/others/misc-options.html>.
* Bug fixes

<https://dl.nssurge.com/mac/v3/Surge-3.0.4-759.zip>

#### Version 3.0.3

* Supports new iCloud container for Surge iOS migration.
* The MitM feature is now compatible with Android system. Please regenerate an new CA certificate before using with Android.
* Fixed some UI issues in Dashboard.
* Fixed a bug that MitM may refuse to enable after modifying settings.
* Fixed a bug that br decompress may fail.
* Fixed a bug that the menu item may use a wrong color if the accent color of system isn't blue.
* Fixed the JSON viewer color issue in the Dark Mode.
* Minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.3-754.zip>

#### Version 3.0.2

* Allows import the profile from a URL.
* Fixed an issue that the HTTP capture button may show wrong state in Dashboard.
* Fixed an issue that Dashboard doesn't show User-Agent as the process name while connecting to iOS device.
* Fixed an issue that the bandwidth of processes may be inaccurate.
* Fixed an issue that the DEST-PORT rule may not be parsed.
* Fixed an issue that ruleset can't be used with logical type rule.

<https://dl.nssurge.com/mac/v3/Surge-3.0.2-736.zip>

#### Version 3.0.1

* Fixed an issue that TFO option will not be saved.
* Fixed an issue that UDP relay option shows wrong state.
* Fixed some i18n issues.
* Fixed crashs on macOS 10.11.
* Save proxy declarations with legacy style (custom) if the proxy is written in legacy style in the text file.
* Other minor bug fixes.

<https://dl.nssurge.com/mac/v3/Surge-3.0.1-711.zip>

#### Version 3.0.0

<https://dl.nssurge.com/mac/v3/Surge-3.0.0-702.zip>

### Surge Mac V2

#### Version 2.6.7

* Fixed a compatibility issue with 304 response.
* Fixed a Dashboard crash.

<https://dl.nssurge.com/mac/Surge-2.6.7-656.zip>

#### Version 2.6.6

* Fixed a compatibility issue with 304 response.
* Fixed an issue that Dashboard may not use the correct encoding to decode text body.

<https://dl.nssurge.com/mac/Surge-2.6.6-654.zip>

#### Version 2.6.5

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.5-652.zip>

#### Version 2.6.4

* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.4-647.zip>

#### Version 2.6.3

* New Features: External Proxy Provider. See <https://medium.com/@Blankwonder/surge-mac-new-features-external-proxy-provider-375e0e9ea660> for more information.
* Surge will automatically track system proxy settings now. When Surge is no longer the default proxy, the status icon will turn grey and a notification will raise.
* Fixed a compatibility issue with Docker.

<https://nssurge.com/mac/Surge-2.6.3-637.zip>

#### Version 2.6.2

* Fixed an issue that the UDP mode with AEAD ciphers doesn't work.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.6.2-618.zip>

#### Version 2.6.1

* Surge now allows expired DNS answers for performance reasons. See 'Optimistic DNS' section in <https://developer.apple.com/videos/play/wwdc2018/714/> for more information.
* Performance improvements.
* Fixed an issue that UDP traffics are not included in the real-time speed.
* Supports hardware acceleration for AES-GCM encryption.
* Supports NAT64 in a pure IPv6 network. (Previous versions already supported DNS64)

<https://nssurge.com/mac/Surge-2.6.1-612.zip>

#### Version 2.6.0

* Supports using Surge Mac as a gateway.
* A new setup guide view.
* A new config panel for traffic capture options.
* Fixed an issue which Dashboard may disconnect unexpectedly under huge pressure.
* The status bar icon will be red while traffic capture is enabled.
* Improved TUN interface performance.
* Enabling TCP Fast Open in macOS 10.14.

<https://nssurge.com/mac/Surge-2.6.0-596.zip>

#### Version 2.5.3

* Supports UDP relay for shadowsocks protocol. A brief introduction in Chinese: <https://trello.com/c/ugOMxD3u>.
* You may use Dashboard to view UDP conversations.
* Dashboard now can save multiple remote machine profiles.
* Improved the JSON viewer in Dashboard.
* Added an UI switch for the dns-failed option in FINAL rule.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.3-563.zip>

#### Version 2.5.2

* You may toggle the hidden state of columns in Dashboard now.
* Supports to export selected rows to csv file.
* Added a connection duration column in Dashboard.
* Supports obfs-uri parameter.
* Improved the benchmark view.
* Fixed a serious bug in the SOCKS5 proxy implementation.
* Bug fixes.

<https://nssurge.com/mac/Surge-2.5.2-544.zip>

#### Version 2.5.1

* The MitM enabling switch has been moved to the main menu and isolated from profile.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.1-528.zip>

#### Version 2.5.0

* Added Outbound Mode options: Direct Outbound, Global Proxy and By Rule.
* Added options for all policy to specify outgoing interface: 'interface' and 'allow-other-interface'.
* Added all\_proxy environment variable for 'Copy Shell Export Command'
* Supports client-side SSL/TLS certificate validation for HTTPS and SOCKS5-TLS proxy. A config example is here: <https://gist.github.com/Blankwonder/cd9fa1987e41cf1a1f1df50583ba1d9c> (DO NOT support editing with UI in this version.)
* Refined MitM.
* Concurrently setup connection to host with Round-robin DNS to boost performance.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.5.0-520.zip>

#### Version 2.4.6

* Supports xchacha20-ietf-poly1305.
* Bug fixes.
* HTTP request header and response header can be extracted from TCP connection now. (SOCKS5 and TUN)
* Enhanced mode can handle all connections now, even for connections initialized with IP address directly.
* Surge TUN now supports forwarding ICMP packets.

**From this version, the minimum system version requirement was raised to macOS 10.11. If you are still using macOS 10.10, please use version 2.4.5.**

<http://dl.nssurge.com/mac/Surge-2.4.6-490.zip>

#### Version 2.4.5

* Bug fixes.
* Improved performance for high concurrency.
* TCP fast open has been disabled temporarily since there is a serious problem in macOS/iOS kernel.
* Dashboard will display decoded URL query now.

<http://dl.nssurge.com/mac/Surge-2.4.5-468.zip>

#### Version 2.4.4

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.4-459.zip>

#### Version 2.4.3

* Supports obfs=tls for shadowsocks protocol.
* Refined the proxy edit panel.
* Added Simplified Chinese language.

<http://dl.nssurge.com/mac/Surge-2.4.3-457.zip>

#### Version 2.4.2

* Fixed an issue that enhanced mode may not be closed properly when switching to a profile without dns-server.
* Fixed an issue that managed profile updating and license info are unavailable while enhanced mode enabled.
* When the necessary port is used by another process, the error alert will show which process is using the port.
* Fixed an issue that map local items can't be edited with UI.
* Fixed an issue that system proxy settings may not be reset properly.
* Auto URL test group will execute a retest immediately after the selected policy has failed.

<http://dl.nssurge.com/mac/Surge-2.4.2-445.zip>

#### Version 2.4.1

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.4.1-439.zip>

#### Version 2.4.0

* Supports enterprise license and profile management.
* Fixed a bug that some fields are unavailable in the configuration panel in some cases.
* Fixed a bug that the FINAL rule can't be edited.
* Fixed a bug that you may not be able to use custom storage path for profiles.
* The interface related options are no longer controlled by profile. Sorry for the repetitive changes.
* You may use $1, $2 to use the matched string in the value while using header rewrite.
* Added an option for HTTP/HTTPS proxy: always-use-connect. When it is true, Surge will use CONNECT method for plain HTTP requests.

<http://dl.nssurge.com/mac/Surge-2.4.0-429.zip>

#### Version 2.3.2

* Added a option to control whether show proxy error notification.
* Fixed a problem that Dashboard show data doesn't exist error.

<http://dl.nssurge.com/mac/Surge-2.3.2-421.zip>

#### Version 2.3.1

* Added a wizard to install CA’s root certificate for iOS simulator.
* Connectivity quality is now an option. (Not show by default)
* Line comments in \[Rule] section in profile file is now presented in UI.
* You may add proxy rule with Dashboard by right-clicking the request or process.
* Dashboard will always open a new window for local machine, instead of asking. You may use "File" menu to connect to a remote machine.
* Added a patch mechanism for adjusting settings for managed config. See manual for more information: <https://manual.nssurge.com/others/managed-configuration.html>

<http://dl.nssurge.com/mac/Surge-2.3.1-420.zip>

#### Version 2.3.0

* Completely redesign the configure interface. You may configure every function with UI now.
* Proxy benchmark is now moved to main application from Dashboard.
* New feature: Header rewrite. See manual for more information: <https://manual.nssurge.com/header-rewrite.html>.
* You may switch profile with command line now: surge-cli switch-profile profilename.

<http://dl.nssurge.com/mac/Surge-2.3.0-416.zip>

#### Version 2.2.4

* Notifications presented by Surge will be removed from Notification Center automatically.
* The interval of attempts to refresh managed config changes to one hour from one minute. (After config expired)
* Supports new encryption methods for shadowsocks-libev 3.0.
* Optimized Dashboard performance.
* Supports TCP Fast Open for shadowsocks proxy. You need add "tfo=true" flag in \[Proxy] section to enable the feature. You may use benchmark to confirm TFO is working.
* You can sort benchmark results now.
* You may choose to reload config after managed config updated.

<http://dl.nssurge.com/mac/Surge-2.2.4-394.zip>

#### Version 2.2.2

* Fixed a bug when using SOCKS5 without authorization.

<http://dl.nssurge.com/mac/Surge-2.2.2-375.zip>

#### Version 2.2.1

* You may use Dashboard to benchmark proxies now.
* Fixed "Too many open files" error by raising limit to 2048.
* Fixed a bug in SOCKS5 with authorization.
* Fixed a bug that managed config may refresh continuously.

<http://dl.nssurge.com/mac/Surge-2.2.1-374.zip>

#### Version 2.2.0

* Map local function is now available.
* Adds notifications when proxy encounters errors.
* Network changed notification will show service name instead of BSD name now.
* Fixed a bug that Dashboard may show the incorrect state of body dump.
* Changes for HTTPS and SOCK5-TLS proxy:
  * Option 'skip-common-name-verify' is deprecated.
  * Add a new option 'skip-cert-verify' to skip certificate verify completely.
  * Add a new option 'sni' to customize SNI field while handshaking. You may use 'sni=off' to disable SNI.
* New rule type: PROCESS-NAME, USER-AGENT and URL-REGEX.
* You can use simple wildcard matching (? and \*) for PROCESS-NAME rule, local DNS mapping and MitM hosts.
* Dashboard supports display POST form data in a table view.
* You may let Surge reload config by sending SIGHUP. You can use command 'killall -HUP Surge' or 'surge-cli reload'.
* Managed configuration is supported now.
* Add a new option 'skip-server-cert-verify' for MitM.

<http://dl.nssurge.com/mac/Surge-2.2.0-368.zip>

#### Version 2.1.4

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.4-362.zip>

#### Version 2.1.3

* Fixed a bug that helper may crash on macOS 10.10.
* Add a option to remove Surge helper for troubleshooting.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.3-337.zip>

#### Version 2.1.2

* New option: Collapse policy group items in menu
* Fixed a bug that enhanced mode DNS settings may not be reverted.
* Hold option key to click 'Copy Shell Export Command' to get a command with primary interface IP instead of 127.0.0.1.
* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.1.2-327.zip>

#### Version 2.1.0

* New feature: Enhanced Mode

  Some applications may not obey the system proxy settings. Using enhanced mode can make all applications handled by Surge.
* New rule type: IP-CIDR6

  Example: IP-CIDR6,2005::/16,DIRECT,no-resolve
* The /etc/hosts file will be reloaded automatically if it has changes.

<http://dl.nssurge.com/mac/Surge-2.1.0-318.zip>

#### Version 2.0.13

* Dashboard supports to use ⌘ + 1,2,3,4 to switch panel.
* Dashboard Supports handoff with Surge iOS.
* Fixed a bug that Dashboard may show incorrect process name.

<http://dl.nssurge.com/mac/Surge-2.0.13-304.zip>

#### Version 2.0.12

* Bug fixes.
* Supported SNI while performing MitM.
* The original certificate will be resigned and used while performing MitM, instead of generating a new certificate.

<http://dl.nssurge.com/mac/Surge-2.0.12-295.zip>

#### Version 2.0.11

* Rule test cache will be flushed after network switching now.
* Added a option 'Grey icon if set as system proxy is disabled'.
* Bug fixes and performance improvements.

<http://dl.nssurge.com/mac/Surge-2.0.11-289.zip>

#### Version 2.0.10

* Surge talks to HTTP proxies with a plain HTTP method for non-HTTPS requests now, instead of CONNECT.
* Improved compatibility with some HTTP server.
* Improved compatibility with some DNS server.

<http://dl.nssurge.com/mac/Surge-2.0.10-280.zip>

#### Version 2.0.9

* Dashborad: The height of the detail panel will not change now while switching pages.
* A notification will show when proxy client access from other machine.
* Used SF Mono as monospaced font for header and body data display.
* Supported TCP half-open mechanism.

<http://dl.nssurge.com/mac/Surge-2.0.9-273.zip>

#### Version 2.0.8

* Add a new option 'exclude-simple-hostnames' in the gereral section.
* Dashborad: Selected row will not be lost while the filter or sort column changed.
* Dashborad: Fixes some issues in the active panel.

<http://dl.nssurge.com/mac/Surge-2.0.8-260.zip>

#### Version 2.0.5

* Bug fixes.

<http://dl.nssurge.com/mac/Surge-2.0.5-255.zip>

#### Version 2.0.3

* New feature: Show connectivity quality in menu.

  Surge will send a DNS question to all DNS servers concurrently to test physical network connectivity while opening the menu.
* Fixes a problem that Surge may freeze while opening the menu.
* Fixes a problem that if a policy group contains duplicate policies, Surge may crash.

<http://dl.nssurge.com/mac/Surge-2.0.3-250.zip>

#### Version 2.0.2

* Dashboard will no longer display process icon in remote mode.
* Fixes a bug: "Set as System Proxy" option does not work properly if only SOCKS service is enabled.
* Fixes a bug: Dashboard can't add a rule with no-resolve option on and comment not empty.
* Minor bug fixes.

#### Version 2.0.1

* Bug fixes

---
## Technotes / DNS 本地与代理解析

我们经常接到用户请求支持配置分地区 DNS 解析功能 (Split DNS)，这种功能往往是无必要的。

Surge 只有在这 3 个环节会触发本地的 DNS 解析：

1. 在规则判定时

在进行规则判定时，Surge 自上往下依次尝试匹配每条规则，如果遇到了一条 IP 类型的规则（包含 IP-CIDR, IP-CIDR6, GEOIP, ASN 等规则），且该规则没有 no-resolve 参数修饰，那么 Surge 将进行 DNS 解析后再进行匹配。

2. 如果使用了一个代理策略，而该代理服务器主机名为域名时。
3. 使用 DIRECT 策略时

若某请求使用了 DIRECT 策略，则会触发 DNS 解析。

也就是说，若在遇到需要触发 DNS 的规则前就已经完成匹配，且策略并非 DIRECT，则不需要在本地进行 DNS 解析。

而当使用代理策略时，除非配置了 `use-local-host-item-for-proxy` 参数，Surge 总是会使用域名向代理服务器发起请求，也就是说 DNS 解析永远在代理服务器进行。

这是最合理且高效的工作流，一方面省去了在本地进行 DNS 的不必要开销，另一方面在本地进行 DNS 的结果并不一定适合代理服务器使用。

为了使该工作流达到最优，应该遵循以下原则撰写规则：

1. 将需要进行 DNS 解析的规则放在最后，避免提前触发不必要的 DNS 解析。
2. 若某些域名在本地完全不能解析，应增加 `DOMAIN` 类型规则直接指定代理策略，避免在本地触发 DNS。
3. 若 FINAL 规则使用了代理策略，可为 `FINAL` 规则配置 `dns-failed` 参数修饰，这样当本地 DNS 解析失败时，也可将请求转至代理服务器。

---
## Technotes / HTTP 协议版本

### 可能的 HTTP 版本

1. HTTP/1.0：目前已几乎绝迹，仅有极个别网站在使用。但本质上与 HTTP/1.1 区别不大。
2. HTTP/1.1：使用最为广泛的 HTTP 协议版本。当访问非 https\:// 网站时，一定使用的是 HTTP/1.x 协议。
3. HTTP/2：已逐渐成为主流的 HTTP 协议版本。必须配合 https 即 TLS 使用。相对于 HTTP/1.x 最大的改进为支持请求的 Multiplexing。
4. HTTP/3：最新的 HTTP 规范，于 2022 年 6 月 9 日正式定稿，但互联网上已存在很多基于先前草稿版本规范实现的网站。与先前版本最大的不同是，HTTP/3 基于 UDP 而非 TCP 实现。

### 一般情况下浏览器与服务端协商 HTTP 版本的方法（即非 Surge 介入时）

1. 当访问非 https\:// 网站时，一定使用 HTTP/1.1。
2. 当访问 https\:// 网站时，在 TLS 握手阶段，浏览器会通过 TLS 的 ALPN（Application-Layer Protocol Negotiation） 扩展，向服务端告知希望使用 `h2` 协议。若服务端支持 HTTP/2，则在 TLS 的握手回应中会告知客户端。此后浏览器与服务端间在 TLS 层上开始使用 HTTP/2。若服务端未表明支持 `h2`，则回退至 HTTP/1.1。
3. 服务端返回的 HTTP Response Header 中，可能带上 `Alt-Svc` 字段，表明该网站支持其他的协议，如 `Alt-Svc: h3=":443"`，表示该服务在端口号 443 上还支持使用 HTTP/3 协议，浏览器在下次请求时将使用 HTTP/3 协议访问。（具体策略由浏览器逻辑自行决定，不同的浏览器策略可能不同）
4. 因此，即使网站支持 HTTP/3，在首次访问时也必须先使用 HTTP/2 或 1.1 连接，当读取到 Alt-Svc 字段后再升级为 HTTP/3。
5. 为了解决这个问题，又新加入了 SVCB/HTTPS RRs DNS 记录，浏览器在访问时优先查询该记录而非 A/AAAA 记录，该记录中会标明服务端具体支持的协议版本和各版本对应的接入点。所以可直接使用 HTTP/3 进行连接。

### 不同浏览器的策略区别

不同的浏览器实现在 HTTP 版本协商上有不一致的地方，比如 Chrome 在 HTTP/3 可用时，总是优先使用 HTTP/3 协议，当失败后再回退至 HTTP/2。而 Safari 则是并发尝试使用 HTTP/2 和 HTTP/3，并优先选择最先完成连接建立过程的连接。这可能使得在测试时发现 Safari 经常甚至永不使用 HTTP/3。

### Surge 开启时对 HTTP 协议版本协商的影响

1. 当 MITM 生效时

若 MITM 对某连接生效，此时由 Surge 完全接管 HTTP 协议栈，Surge 支持以 HTTP/1.1 或 HTTP/2 与客户端进行对话。

在配置中开启 MITM via HTTP/2 开关后（`h2=true`），Surge 会接受客户端的 h2 ALPN，否则将回退至 HTTP/1.1。

* 若使用 HTTP/1.1 接管，那么与真实服务器间的握手也不会发送 h2 ALPN，强行使用 HTTP/1.1。
* 若使用 HTTP/2 接管，那么与真实服务器间的握手会发送 h2 ALPN，根据握手结果使用 HTTP/1.1 或 HTTP/2。

2. 当使用代理模式接管时

若勾选了设置为系统代理选项，或是以其他方式配置了浏览器代理设置。由于 HTTP 代理不支持 UDP 流量转发，HTTP/3 将永不会被使用。（这是浏览器自身策略决定的）

HTTP/2 的协商不受影响，当访问 https 网站时，浏览器将使用 HTTP CONNECT 代理方法，此时 Surge 仅作为 TCP 层代理，对高层 TLS/HTTP 协议协商没有干扰。

3. 代理模式关闭，仅使用增强模式接管时
   * 对于 HTTP/2 的协商没有影响。
   * 对于 HTTP/3：
     * 默认情况下，由于 Surge 依靠 fake IP 机制接管请求（详见《Surge 官方中文指引：理解 Surge 原理》），会自动屏蔽掉所有 SVCB DNS 请求。如果某网站依赖该机制进行 HTTP/3 协商，那么将会失败。可通过配置 `allow-dns-svcb=true` 关闭该行为。但请注意关闭后可能导致 Surge 接管的请求中出现无法正确映射的 IP 和 CNAME。
     * 对于使用 `Alt-Svc` 进行协商的网站没有影响。
     * 若使用代理策略，请注意对应策略是否支持 UDP 转发，若不支持则会回退至 DIRECT 策略。

---
## Technotes / IPv6 RA Override

在 Surge Mac v6 中，新增了 IPv6 RA Override 功能，用于接管其他设备的 IPv6 网络。该功能为 Surge 首创，因此互联网上几乎不存在该方案的技术资料，因此创建了该文档以解释功能细节，方便使用者排错。

### 核心原理

在 IPv6 网络中，RA 广播是网络的基石之一，一般情况下，路由器通过发送 RA 广播完成三件事：

1. 提供 IPv6 地址前缀，让其他设备可以生成自己的公网 IPv6 地址（GUA 地址）。
2. 宣告自己的 link-local 地址为默认路由。
3. 配置客户端的 IPv6 DNS。

RA 消息的设计中，存在优先级的机制，因此可以通过高优先级的 RA 消息，覆盖中和低优先级的消息。这是 Surge IPv6 RA Override 的核心工作原理，一个不太一样的地方是，RA 消息通常是进行广播，而 Surge 的 RA 是单播，只影响需要被接管的设备。

同时，Surge 的 RA 不包含地址前缀信息，所以地址分配依然依赖原路由的 RA 广播，Surge 的高优先级广播只进行路由和 DNS 覆盖。因此原路由的 RA 广播一定不可关闭，否则无法完成 IPv6 地址分配，只需要保证优先级设置不为高即可。

### IPv6 RA DNS

如果原路由的 RA 配置了 IPv6 DNS，且该地址为 link-local 地址，或路由器自身的 IPv6 地址。则会因为路由优先级问题导致 DNS 包无法被 Surge 劫持，fake IP 机制无法生效。

Surge 的 RA 包会广播自己的 v6 DNS 地址 `fd00:6152::2`，但是不同操作系统对高优先级 RA DNS 的处理方式不同，有些系统是覆盖原有设置，有些只是单纯追加。因此 Surge 会提示建议修改原广播的 DNS 地址为空或任意公网地址，以避免无法覆盖时的情况。

不过，即使 DNS 覆盖失败，也只是 fake IP 机制失效，仍然可以接管请求，域名类规则也可以靠 SNI 嗅探完成。

### 稳定性

在 v4 DHCP 模式下，由于 Surge 是完全取代了原有的 DHCP 服务，所以可以确保接管一定成功，否则客户端根本无法连接网络。

但是在 v6 RA 覆盖模式下，由于覆盖行为与原有 RA 相互独立，所以如果存在网络波动，导致 Surge的 RA 覆盖消息丢包，则可能出现客户端设备未能被覆盖的情况，此时客户端设备的 IPv6 将会是直接连接。

但是这种情况即使发生，一般也只出现于刚接入网络的时候，一旦接入后，Surge 会定期不断发送 RA 覆盖消息，且周期远高于 RA 消息的有效期，所以很少会出现失效的情况。

### 兼容性问题

在我们的测试中，绝大多数设备对 Surge 的 RA 覆盖表现良好，在少数情况下可能会有兼容性问题：

#### Sony PS5

PS5 的 IPv6 协议栈不完善，无法正确处理高优先级 IPv6 RA 消息，因此无法接管。

#### Windows

部分 Windows 设备，可能在一段时间后，出现接管失效的问题，事件查看器中出现警告：`TCPIP - Event 4205 - Autoconfigured route limit has been reached. No further autoconfigured routes will be added until the interface is reconnected.`。

发现只有部分设备在低概率下出现该问题，我们还在分析与测试出现该问题的真正原因，由于 Windows 闭源且未提供相关文档，因此比较困难，也可能就是 Windows 的 Bug。

以上问题，都可以通过手动修改设备的 IPv6 配置解决，即不再依赖 RA，直接配置 IPv6 地址、网关和 DNS。

* IPv6 地址：保证与原自动分配的地址一致即可。但是如果你的 IPv6 前缀可能会变化，则变化后需要重新配置。
* 网关地址：可在 Surge 总览页面查看 Surge VM 的 IPv6 地址，填入该地址。
* DNS：`fd00:6152::2`

手动配置后即可保证稳定的完全接管。

---
## Technotes / NAT 类型详解

在进行 UDP 转发时，不同的转发映射策略会导致 UDP 穿透功能的差异，这种差异通常被称为 **NAT 类型**。

NAT 类型的命名在不同软件和文档中可能有所不同，但一般可分为以下几类：

* **A 类**：Full Cone NAT（也称 1 类或开放型）
* **B 类**：Address Restricted Cone NAT（也称 2 类或中等型）
* **C 类**：Port Restricted Cone NAT
* **D 类**：Symmetric NAT

NAT 类型主要由你的**路由器**决定，但也可能受到互联网服务提供商（ISP）的限制。

***

### Surge 对 NAT 类型的影响

当启用 Surge 并通过其 VIF 接管网络后，由于增加了一层转换，会对 NAT 类型产生影响。具体表现为：

* 如果原始网络为 **A 类 Full Cone NAT**，Surge 会将其降级为 **B 类 Address Restricted Cone NAT**。
* 如果原始网络为 **B 类及以下**，则 NAT 类型保持不变。

这种变化不仅影响本机所有进程，还会作用于通过网关模式接管的其他设备。

若想避免 NAT 级别降低（例如，确保在线游戏联机），可以通过配置 **`always-real-ip`** 参数解决问题。配置时，需确保该参数覆盖相关的 **STUN 域名**（可通过 Surge 的请求列表确认具体域名）。

Surge Mac 内置的 **Game Console STUN** 模块即为常见游戏主机的 STUN 域名预设了配置：

```
always-real-ip = *.srv.nintendo.net, *.stun.playstation.net, xbox.*.microsoft.com, *.xboxlive.com
```

暴力一点，可以使用该配置覆盖绝大多数 SUN 服务器，通常不会有明显的副作用：

```
always-real-ip = *stun*
```

### 使用代理时的 NAT 类型

当请求通过**代理策略**处理时，其对应的 NAT 级别由**代理服务器的 NAT 类型**决定，与本地网络的 NAT 类型无关。你可以通过 Surge Mac 的**代理诊断功能**（位于窗口菜单 › 代理诊断）测试代理服务器的 NAT 级别。

### Surge Ponte 对 NAT 类型的要求

若希望在不借助代理服务器的情况下使用 Surge Ponte，则本地网络需要为 A 类 Full Cone NAT，这需要你的路由器与 ISP 共同支持。

若通过代理服务器进行穿透，则与本地 NAT 类型无关，仅需要关注代理服务器的 NAT 类型。如果该服务器由您自己所维护，通常情况下设置防火墙放行所有端口的 UDP 流量即可。

### Surge 的 NAT 类型测试准确吗？

所有的 NAT 类型测试工具，都是靠发出不同的 STUN 请求，观察是否能收到响应以进行判断的，如果网络丢包情况严重，或者 STUN 服务器异常，则可能导致测试结果偏低。Surge 在测试时或多次发包以保证测试结果尽量准确。

---
## Technotes / REJECT 策略区别

Surge 内置了多个不同的 REJECT 策略，不同策略间有一些细微的差别：

* `REJECT`：拒绝该请求，当连接类型为 HTTP 时，会返回一个错误页面。（该行为可被 `show-error-page-for-reject` 参数控制）
* `REJECT-TINYGIF`：拒绝该请求，当连接类型为 HTTP 时，返回一个 1px 的 GIF 图片响应。若为其他类型连接则直接断开。该策略主要用于 Web 广告屏蔽。
* `REJECT-DROP`：拒绝该请求，与 `REJECT` 不同的是，该策略将静默抛弃请求。因为部分程序有着十分暴力的重试逻辑，在连接失败后会立刻进行重试，导致请求风暴，这将严重浪费系统资源。

如果发往某主机名的请求短时间内大量触发 REJECT/REJECT-TINYGIF 策略（当前版本的阈值为 30 秒内 10 次），Surge 将自动升级 REJECT 策略为 REJECT-DROP 策略。

* `REJECT-NO-DROP`：一般情况下与 `REJECT` 策略相同，区别在于使用该规则时将不会触发上述自动升级的行为。

---
## Technotes / 自动策略组测试策略

自动类策略组包含：url-test、fallback 和 load-balance。

### 初次使用时

当第一次使用某个策略组时，Surge 默认行为是使用策略组中的第一个子策略，并与此同时触发策略组的测试，在测试完成之前，若该策略组被再次使用，依然会使用第一个子策略。

若策略组配置了 `evaluate-before-use=true` 参数，那么当策略组测试未完成时，将会堵塞住对应请求，等待测试完毕后使用测试结果再继续。

### 定期重测试

自动类型策略组支持配置 `interval` 参数，当上一次的测试的时间与当前时间超过此间隔后，则上一次的测试结果被标记为过期。

当该策略组再次被使用时，将先使用过期结果的子策略，同时触发一次新的测试。也就是说，如果该策略组未被使用，即使结果已过期也不会立刻触发重测试。

### `tolerance` 参数

`url-test` 策略组有一个特别的参数：`tolerance`，默认为 100 ms。只有当某子策略的测试成绩比原先的选定子策略的成绩，差值高于 `tolerance` 的设定值时，才变更选定策略。

举例说明，策略组包含 A 与 B 两子策略，目前选定为 A，`tolerance` 为 100 ms。

当新的测试结果为 A: 50ms B: 10 ms 时，依然继续使用 A。 当新的测试结果为 A: 150ms B: 10 ms 时，切换至 B。

该特性用于避免选定策略在若干个结果相差不大的策略间反复跳动。导致出口 IP 不断变化引发异常。

### 异常情况下的重测试

当某策略组的选定代理策略出现故障时，理应立刻进行重测试并切换至其他策略，但是由于实际情况通常并不简单，Surge 为此做了较为复杂的逻辑。

通过代理访问一个目标网站时出现了问题，遇到的错误可被分为三大类

1. 设备本身的网络问题，如信号差、网络中断等。
2. 代理服务器出现故障或网络问题。
3. 目标网站服务器出现故障或网络问题。

很明显，我们只希望在遇到错误 2 时才触发策略组的重测试。问题在于，Surge 无法准确地确认问题的来源。为此 Surge 将错误重新进行分类：

* A 类：一定是错误 1。（如：No route to host 错误）
* B 类：可能是错误 1 或 2。（如：TCP hankshake timeout 错误）
* C 类：一定是错误 2。（如：Connection refused 错误）
* D 类：可能是错误 2 或 3。（如：Socket closed by remote 错误）
* E 类：一定是错误 3。

目前版本 Surge 的策略为：当选定子策略遇到错误 C 时，将立刻触发重测试，当在 60 秒内遇到 3 次 B 或 D 类错误，也会触发重测试。A 与 E 类不触发重测试。

对于不同的代理协议，错误的划分方法会有不同，比如 shadowsocks、Trojan、VMess 协议都不会在目标网站出错时返回状态码，所以填错了代理服务器密钥和目标服务器不通这两种截然不同的错误，从 Surge 看来并没有任何区别，都只是代理服务器主动断开了 TCP 连接。（Snell 协议有完整的错误码和错误信息回报）

---
## Technotes / TCP Fast Open

## 什么是 TCP Fast Open（TFO）

TCP 连接需要进行三次握手方可开始传输数据。这使得每个 TCP 连接都需要浪费掉一个 RTT 去建立连接。这是因为 TCP 协议被发明时，网络还处于 LAN 局域网时代，RTT 只有毫秒级，所以这个设计并没有问题。

而到了互联网与无线网络时代，RTT 通常可高达几十上百毫秒。这时被浪费掉的这一个 RTT 便成为不可忽略的开销。TCP Fast Open 也因此而生。TFO 的具体实现方式简单来说，就是在三次握手时的第一个 SYN 包里，附带上所需要传输的第一个数据包，如 TLS 协议的 Client Hello。当握手完成时，服务端就已收到了第一个数据包，开始进行后续的传输。这样就挽回了握手导致的延迟损失。（具体实现中还有很多细节，如 cookie，这里不再展开）

### 兼容性问题

但是这项改进遇到了一个问题，由于这是一项对 TCP 协议的扩展，中间网络设备有可能不支持该特性。比方说有些防火墙（NAT）会直接将带有数据段的 SYN 包认为是非法数据包直接抛弃。导致使用了 TFO 的连接完全无法建立。（如中国的移动数据网络）

为此，操作系统不得不引入一个 blackhole 机制，当对某 IP 以 TFO 进行握手时，如果在一定时间内都没有收到回应，那么就重新尝试以非 TFO 方式进行握手，如果成功，则将该 IP 加入黑名单，之后不再以 TFO 进行握手。

但该机制有两个问题：

1. 可能因为网络正常波动丢包而误判，导致 IP 进入黑名单，后续连接全部丧失 TFO 特性。
2. 有的时候是在特定网络下 TFO 无效（如数据网络），但操作系统的黑名单只记录了目标 IP，所以在切换网络后，依然无法使用 TFO。

在我们的测试中，一段时间后代理服务器 IP 几乎一定会被加入黑名单。

两个关于 macOS 的 Tips：

1. 可使用 sudo sysctl -w net.inet.tcp.clear\_tfocache=1 命令，强行清空系统的黑名单。
2. 可使用 sudo sysctl -w net.inet.tcp.disable\_tcp\_heuristics=1，强行关闭黑名单功能。（但同时还会影响 ECN 与 MPTCP）

### Surge 中的相关设置

在 Surge 中使用 TFO 时，首先需要为对应的代理策略配置 `tfo=true` 参数。

为了解决操作系统的 blackhole 机制可能带来的问题，Surge 允许通过子网设置手动配置 TFO 可用性，绕过系统的限制。

```
[SSID Setting]
"SSID:My Home" tfo-behaviour=force-enabled
```

`tfo-behaviour` 参数有 3 个选项：

1. `auto`：使用系统的默认黑名单行为。
2. `force-enabled`：在该网络下无视系统黑名单，始终使用 TFO 进行握手。
3. `force-disabled`：在该网络下完全不使用 TFO。

在配置之前，请务必先在该网络下测试 TFO 是否可用，以避免配置为 force-enabled 导致代理完全无法联通。

### 请求日志

在请求的日志中，会显示关于 TFO 的细节信息，一些常见的结果如下：

* `TCP Fast Open was successful (tfo_syn_data_sent, tfo_syn_data_acked)`

  表示 TFO 已成功。
* `Attempted to use TCP Fast Open but failed (tfo_heuristics_disable)`

  表示由于被加入黑名单，TFO 已自动禁用。
* `Attempted to use TCP Fast Open but failed (tfo_cookie_req, tfo_no_cookie_rcv)`

  表示尝试进行了 TFO 握手，但是服务端未开启 TFO 支持。

---
## Technotes / VM UDP Fast Path

在使用 Surge 网关模式接管下游设备时，如果某些设备运行了大量使用 UDP 的 P2P 应用（如 BT 下载、游戏平台启动器、直播客户端等），可能会在 Dashboard 中瞬间产生海量连接。这不仅会拖慢 Surge 的整体处理速度，在极端情况下甚至可能导致 macOS 资源耗尽，使 Surge 被系统强制重启。

## 问题成因

Surge 作为工作在四层的代理，对每一个「四元组」不同的 UDP 流（源地址 / 源端口 / 目标地址 / 目标端口）都会按一个独立连接进行管理。\
对于普通应用而言，即便使用 UDP，通常也只会维持少量逻辑连接，这一开销是完全可接受的；但对 P2P 应用来说，在数秒内就可能产生上千个逻辑连接，显著放大了连接管理成本。

## UDP Fast Path 机制

为应对上述情况，我们引入了 UDP Fast Path 防御机制。当检测到某个客户端在短时间内新建了大量 UDP 连接时（**1 秒内 ≥ 10 个** 或 **10 秒内 ≥ 30 个**），Surge 会对该客户端启用 UDP Fast Path，将其 UDP 流量退化为仅进行 L3 转发处理。

在 UDP Fast Path 模式下：

* 每个数据包只做最小化的三层转发处理，不再为每个四元组建立独立连接；
* 处理性能极高，理论上可轻松超过物理网卡的带宽极限；
* 大幅降低连接管理与系统资源消耗，不再需要担心 P2P 连接风暴拖垮系统。

## 注意事项

1. **绕过代理**：\
   启用 UDP Fast Path 的数据包会被直接转发，**不会经过代理规则和策略处理**。
2. **关键端口与 FakeIP 保护**：\
   为避免影响正常应用，对以下 UDP 流量**始终使用常规模式处理**，不会进入 Fast Path：
   * 目标端口号 **小于 1024** 的 UDP 数据包；
   * 目标地址为 **FakeIP** 的 UDP 数据包。
3. **仅适用于 Surge Gateway VM**：\
   UDP Fast Path 仅在配合 **Surge Gateway VM** 使用时生效，对增强模式接管无效。
4. **按设备单独开关**：\
   自 Surge Mac 6.4.2 起，Dashboard 中新增了按设备单独关闭 UDP Fast Path的开关。\
   你可以根据需要，为特定设备单独启用或禁用 UDP Fast Path，以在性能与可控性之间取得平衡。

---
## Technotes / User Agent 规则

Surge 的规则系统中有提供依据 User-Agent 进行判别的规则。使用该规则时请注意：

1. 该规则仅对 HTTP/HTTPS 请求有效。如果是一个 raw TCP 请求中提取的 HTTP header，规则无法生效，需配置 `force-http-engine` 参数，详见[《Surge 官方中文指引：理解 Surge 原理 》](https://manual.nssurge.com/book/understanding-surge/cn/#%25E5%25A4%2584%25E7%2590%2586)。
2. 对于 HTTPS 请求，存在发给 HTTP 代理的 CONNECT 请求 User-Agent 和真实的 HTTP 请求 User-Agent ，两者的内容可能相同也可能不同。前者的内容通常是由系统生成，不可被 app 调整。在未开启 MITM 的情况下，匹配时仅对前者生效。开启 MITM 后仅对后者生效。
3. 在 iOS 15 系统后，系统出于隐私保护考虑，不再于 CONNECT 请求中提供 User-Agent，这意味着对于所有 HTTPS 请求，在未开启 MITM 时，User-Agent 均不可见且规则无法生效。

---
