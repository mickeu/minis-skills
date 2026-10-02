> For the complete documentation index, see [llms.txt](https://kb.nssurge.com/surge-knowledge-base/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://kb.nssurge.com/surge-knowledge-base/zh/guidelines/proxy-provider.md).

# 使用来自代理服务商的线路

若您购买了第三方服务商提供的代理服务，并希望将其线路接入 Surge 使用，请阅读本指引了解详情。

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

{% hint style="success" %}
若需要可以随时切换线路地区，还可以再建立一个手动选择组：

```
Booster = select, Airport-US, Airport-UK
```

{% endhint %}

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

{% hint style="warning" %}
在配置 `include-other-group` 参数时，若需包含多个策略组，必须使用引号 `""` 将参数内容包裹。
{% endhint %}

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

{% hint style="info" %}
无论使用哪种方式，您都可以预先定义一个包含 `DIRECT` 策略的 `select` 组并将其设为 `underlying-proxy`，这样就能在控制面板中随时开启或关闭跳板代理模式。
{% endhint %}

{% hint style="info" %}
对于导入策略的其他微调（如打开 TCP Fast Open），`external-policy-modifier` 仍是合适的工具。
{% endhint %}

</details>
