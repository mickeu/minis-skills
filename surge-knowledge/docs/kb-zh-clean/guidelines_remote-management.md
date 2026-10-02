> For the complete documentation index, see [llms.txt](https://kb.nssurge.com/surge-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/remote-management.md).

# Surge 远程管理

使用 Surge iOS、Surge Dashboard 或 surge-cli 管理另一台 Mac、iPhone、iPad 或 Apple TV 上运行的 Surge。

你可以从另一台设备管理 Surge。例如，在 Mac 上查看 iPhone 的请求，从 iPhone 切换无显示器的 Mac mini 上的策略组，随时随地查看 Apple TV 的运行情况，或通过终端脚本控制远程 Surge 实例。

Surge 提供三种方式：

* **外部控制器**：原生远程管理通道，Surge iOS、Surge Dashboard 和 surge-cli 均通过它进行控制。这是功能最完整的方式，也是本指南的重点。
* **HTTP API**：REST 风格的接口，供你自己的脚本和自动化工具使用。
* **Web Dashboard**：通过 HTTP API 提供的浏览器控制面板。

如果你只是想管理另一台设备上的 Surge，使用外部控制器即可。

## 控制端与被控实例

远程管理涉及两个角色：

* **被控实例**：你想要管理的 Surge，可以是 Surge Mac、Surge iOS（iPhone 和 iPad）或 Surge tvOS。
* **控制端**：用于管理它的应用，可以是：
  * **Surge iOS**：入口位于工具页面的远程控制器区域。
  * **Surge Dashboard**：Surge Mac 随附的应用。
  * **surge-cli**：Surge Mac 随附的命令行工具。

这三种控制端使用相同的协议，因此任意一种都可以管理任意被控实例。控制端也可以管理本机的 Surge 实例。例如，Surge Dashboard 和 surge-cli 无需配置即可连接本机的 Surge Mac。

| 被控实例       | Surge iOS | Surge Dashboard | surge-cli |
| ---------- | --------- | --------------- | --------- |
| Surge Mac  | ✅         | ✅               | ✅         |
| Surge iOS  | ✅         | ✅（Wi-Fi 或 USB）  | ✅         |
| Surge tvOS | ✅         | ✅               | ✅         |

## 选择连接方式

### A. Surge Ponte（Mac 和 Apple TV 推荐使用）

如果被控设备上的 Surge Mac 或 Surge tvOS 已作为 [Surge Ponte](/surge-knowledge-base/zh/guidelines/ponte.md) 服务端运行，这是最简单的方式：

* 无需地址、端口或密码。设备会自动出现在所有登录了相同 iCloud 账号的 Surge iOS 设备上。
* 可在任何网络下使用，包括蜂窝网络和外出时使用的网络。
* 连接始终采用端到端加密。

### B. 通过局域网连接外部控制器

在被控设备上开启外部控制器，并设置端口和密码。同一网络中的控制端即可通过设备的 IP 地址、端口和密码连接。此方式适用于 Surge Mac、Surge iOS 和 Surge tvOS。

### C. USB（仅限 Surge iOS）

将 iPhone 或 iPad 通过数据线连接到 Mac 后，Surge Dashboard 即可通过 USB 连接。这不需要 Wi-Fi，也是查看使用蜂窝数据的 iPhone 流量的唯一方式。

{% hint style="info" %}
你可以组合使用这些方式。例如，如果两端都运行 Surge 并开启 Ponte，就可以让 Surge Dashboard 或 surge-cli 连接 `ponte-name.sgponte`，随时随地访问家中 Mac 的外部控制器。详见下方的[使用技巧](#tips)。
{% endhint %}

## 配置被控设备

### Surge Mac

**通过 Surge Ponte**

1. 按照 [Surge Ponte 指引](/surge-knowledge-base/zh/guidelines/ponte.md) 开启 Surge Ponte。
2. 在配置向导中，保持勾选**允许其他设备通过 Surge Ponte 进行远程控制**。

随后，这台 Mac 就会出现在你其他设备上 Surge iOS 的远程控制器列表中，无需密码。

**通过外部控制器**

1. 打开**设置 › 通用**，找到**外部控制器**区域。
2. 设置 TCP 端口（默认为 6170）和访问密码。
3. 打开**允许**以接受其他设备的连接。如果未开启，则只有同一台 Mac 上的控制端（例如本机的 surge-cli 或 Dashboard）以及通过 Surge Ponte 建立的连接可以访问。

### Surge iOS

Surge iOS 无法作为 Surge Ponte 服务端，因此只能通过外部控制器进行管理：

1. 在首页打开**更多设置**，然后在**远程控制**区域找到外部控制器选项。
2. 开启该选项，并设置端口和密码。
3. 默认仅允许 USB 连接。如需允许同一 Wi-Fi 网络中的控制端访问，请开启**允许从 Wi-Fi 访问**。

{% hint style="warning" %}
出于安全考虑，Surge iOS 始终拒绝来自蜂窝网络的外部控制器连接。如需管理正在使用蜂窝数据的 iPhone，请通过 USB 数据线将其连接到 Mac。
{% endhint %}

外部控制器仅在 Surge 运行时可用。

### Surge tvOS

Surge tvOS 没有自己的控制界面，其设计就是通过远程方式进行管理。使用 Surge iOS 完成部署后，Apple TV 会通过 Surge Ponte 自动出现在 Surge iOS 的远程控制器列表中。如果你无需在外出时访问 Apple TV，可以将 Surge Ponte 设置为 LAN-Only。详见 [Surge tvOS](/surge-knowledge-base/zh/guidelines/tvos.md)。

### 配置文件语法

外部控制器的设置保存在配置文件的 `[General]` 段中，因此你也可以直接配置：

```
[General]
external-controller-access = MyPassword@0.0.0.0:6170
```

该值的格式为 `password@address:port`，三个部分均不可省略。

* `127.0.0.1`：仅接受本机连接。在 Surge iOS 上，这表示仅允许 USB 连接。
* `0.0.0.0`：同时接受来自局域网的连接。在 Surge iOS 上，这表示允许 Wi-Fi 连接。

## 从控制端连接

### 使用 Surge iOS

打开**工具**页面，找到**远程控制器**区域：

* 可通过 Surge Ponte 访问的 Surge Mac 和 Apple TV 设备会自动列出，并标注「通过 Surge Ponte」。
* 如需连接局域网中的设备，点击**远程控制器**，输入其 IP 地址、端口和密码，然后点击**连接**。

连接后，你可以将设备加入**收藏**，以便日后一键访问。你也可以为已收藏的设备添加**主屏幕快捷方式**，直接打开其控制界面。

### 使用 Surge Dashboard

Surge Dashboard 默认打开本机的 Surge Mac。如需管理其他设备，选择**新建连接**，然后：

* **远程**：输入主机地址、端口和密码。你可以保存常用设备，之后从已保存的列表或 Dock 菜单中再次打开。
* **USB**：选择已连接的 iPhone 或 iPad，并输入在该设备上配置的端口和密码。

{% hint style="success" %}
当 Surge iOS 正在运行且外部控制器允许通过 Wi-Fi 访问时，iPhone 会向附近的 Mac 提供一个\*\*接力（Handoff）\*\*项目。在 Mac 的 Dock 中点击该项目，即可打开 Surge Dashboard 并自动连接到 iPhone。
{% endhint %}

### 使用 surge-cli

surge-cli 位于 `/Applications/Surge.app/Contents/Applications/surge-cli`。不添加额外参数时，它控制本机的 Surge Mac。添加 `--remote` 即可控制其他实例：

```
surge-cli --remote 192.168.1.20:6170 status
```

为避免密码出现在 shell 历史记录中，请在安全的密码提示中输入密码，设置 `SURGE_CLI_PASSWORD` 环境变量，或通过 `--password-stdin` 传入密码。不要将密码写在命令行中。

运行 surge-cli 时不指定命令，即可进入支持自动补全的交互模式。所有命令详见 [Surge CLI 文档](https://manual.nssurge.com/others/cli.html)。

{% hint style="info" %}
Surge iOS 也内置了**终端**，支持与 surge-cli 相同的命令。你可以在工具页面打开本机实例的终端，也可以在各个远程设备的远程控制器菜单中打开对应的终端。
{% endhint %}

## 可以远程执行哪些操作

连接后，你可以像在设备本机上一样管理 Surge：

* **监控**：查看最近和活跃的请求、实时流量统计、事件、DNS 缓存和 Logbook 记录。
* **路由**：切换出站模式、更改策略组选择、测试策略，以及查看和编辑规则。
* **临时规则**：添加立即生效、在 Surge 停止时自动丢弃的规则，便于调试。
* **功能开关**：开启或关闭 MitM、重写、脚本、HTTP 抓包等功能。
* **配置与资源**：切换配置、启用或停用模块、更新外部资源，以及更新托管配置。
* **诊断**：执行网络诊断、DNS 查询、规则匹配分析等操作（主要在终端中进行）。
* **维护**：重新加载配置或重启引擎。

当被控设备运行 **Surge Mac** 时，你还可以：

* 管理[网关模式](/surge-knowledge-base/zh/guidelines/gateway.md)下的设备，包括分配静态 IP、重命名设备、更改图标和重新连接设备。
* 编辑 Mac 配置中的规则。
* 管理插件。
* 对 Surge Mac 执行无人值守升级，无需有人在 Mac 前操作即可完成更新和重启。

{% hint style="warning" %}
两台设备都运行最新版本时，远程管理的效果最佳。如果控制端提示版本不匹配，部分功能可能不可用或不稳定。如果一台设备使用测试版本，请在另一台设备上也使用测试版本。
{% endhint %}

## 安全

外部控制器拥有 Surge 的完整控制权限，因此请妥善保护：

* **仅在可信网络中使用。** 通过局域网建立的外部控制器连接不加密。不要通过路由器端口转发或 DMZ 等方式将外部控制器端口暴露到互联网。如需从局域网外管理设备，请使用始终采用端到端加密的 Surge Ponte。
* **使用强密码。**
* **防止密码猜测**：如果在 30 秒内出现 10 次密码验证失败，Surge 会临时封禁来源 IP 地址或本机进程，并显示「未经授权的访问」警告。你可以使用 `surge-cli security ban` 查看或清除封禁。
* 在 Surge iOS 上，来自蜂窝网络的连接始终会被拒绝；除非你明确允许，否则 Wi-Fi 连接也会被拒绝。

## 与 HTTP API 和 Web Dashboard 的比较

Surge 也提供 [HTTP API](https://manual.nssurge.com/others/http-api.html) 和 Web Dashboard。它们支持切换策略、切换功能开关和查看请求等常见操作，但功能不如外部控制器完整。

|                    | 外部控制器                               | HTTP API   | Web Dashboard            |
| ------------------ | ----------------------------------- | ---------- | ------------------------ |
| 使用方                | Surge iOS、Surge Dashboard、surge-cli | 你自己的脚本和工具  | 浏览器                      |
| 功能范围               | 最完整：几乎涵盖设备本机上的所有功能                  | 常用操作       | 常用操作                     |
| 可通过 Surge Ponte 使用 | ✅                                   | ❌          | ❌                        |
| USB 连接             | ✅（Surge iOS）                        | ❌          | ❌                        |
| 配置项                | `external-controller-access`        | `http-api` | `http-api-web-dashboard` |

与其他工具集成时可使用 HTTP API；从未安装 Surge 的设备快速访问时可使用 Web Dashboard。日常管理自己的设备时，建议使用外部控制器。

## 使用技巧 <a href="#tips" id="tips"></a>

1. **通过 Surge Ponte 使用 surge-cli 或 Dashboard。** 如果控制端 Mac 和被控 Mac 都运行 Surge 并开启 Surge Ponte，你可以使用 `ponte-name.sgponte` 作为主机地址，例如 `surge-cli --remote mymacmini.sgponte:6170 status`。连接会通过加密的 Ponte 隧道传输。由于 `.sgponte` 在远端设备上会被解析为 127.0.0.1，被控 Mac 的外部控制器可以继续仅监听 `127.0.0.1`，无需向局域网开放。
2. **无显示器的 Mac mini。** 在用作家庭网关的 Mac 上开启 Surge Ponte，并允许远程控制。之后，你就可以随时随地从 iPhone 管理它，包括管理[网关模式](/surge-knowledge-base/zh/guidelines/gateway.md)下的设备和执行无人值守升级。
3. **从 Mac 调试 iPhone。** 使用 USB 数据线连接 iPhone，然后在 Surge Dashboard 中打开它。即使 iPhone 正在使用蜂窝数据，你也可以在更大的屏幕上查看每个请求。

## 故障排除

* **设备未出现在列表中。** 请确认两台设备登录了相同的 iCloud 账号，Mac 或 Apple TV 已开启 Surge Ponte，并在 Ponte 配置过程中允许了远程控制。
* **无法连接 Surge iOS。** 请确认 iPhone 上的 Surge 正在运行，外部控制器已开启；如果通过 Wi-Fi 连接，还需开启**允许从 Wi-Fi 访问**。同时确认两台设备处于同一个 Wi-Fi 网络中。
* **密码错误。** 请检查密码。如果连续多次输入错误，请稍等片刻，或在被控设备上清除封禁后再重试。
* **部分功能缺失。** 被控设备可能运行较旧版本，或者该功能仅适用于 Surge Mac，例如网关模式设备管理。请更新两台设备上的 Surge。
