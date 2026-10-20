# 免输配对码：官方资料与实现细节

更新：2026-10-20

## 1. 结论与证据范围

本文说明的是**设备主动发起、主机作为 responder 的 RemotePairing 免输码流程**：用户仍需在系统设置中选择主机并确认，但不必输入六位配对码。

核心组合：

1. 主机发布 `_remotepairing-pairable-host._tcp` Bonjour 服务并监听 TCP。
2. 手机从系统设置发起连接。
3. 主机握手响应声明 `allowsPinlessPairing: true`。
4. 主机以协议约定值 `000000` 执行 SRP 服务端计算，不向用户展示该值。
5. 完成 M1–M6 后保存配对身份；后续独立 pair-verify 验证通过才启用新记录。

**这不是跳过系统授权，也不是把任意 PIN 猜成六个零。** 声明免输码能力、协议角色、系统发起流程和 SRP 参数必须一致。

证据分层：

| 来源 | 能证明的内容 | 不能据此声称 |
|---|---|---|
| Apple 官方文档 | 开发者模式、设备配对、系统信任的用户操作流程 | 已公开本文全部 RemotePairing 私有字段与免输码算法 |
| 用户提供的 Swift/Rust 源码 | 成功原生 App 的具体免输码实现 | 对所有系统版本普遍兼容 |
| 用户实测反馈 | 该原生 App 已实现免输码配对 | 修正后的 Scripting 脚本也已真机验收 |
| 本地 TCP 与密码学测试 | 当前 responder 的消息交换、密码学与清理可运行 | 真实 Bonjour、系统设置 UI 和设备授权已通过 |

## 2. Apple 官方资料

### 2.1 Device Hub 中管理与配对设备

[Managing your simulated and physical devices in Device Hub](https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub)

已读取的官方页面包含：

- 使用 Device Hub 的 Pair Nearby Device 入口进行无线配对。
- 按设备类型完成发现、开发者模式等准备。
- 页面描述了输入设备上显示的 PIN，以及在设备上确认 Trust This Computer 的步骤。
- 有线配对及后续无线连接的说明。

**该页面没有给出 `allowsPinlessPairing`、固定 `000000`、SRP M1–M6 或 pairable-host responder 的完整线协议，也没有明确声明“所有免输码配对仅支持 iOS 27”。**

### 2.2 开启开发者模式

[Enabling Developer Mode on a device](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)

这是开发者模式的官方用户操作资料，不是 RemotePairing 免输码协议规范。设备信任、开发者模式和后续具体服务的授权是不同环节，不应混为同一个开关。

### 2.3 在实体设备运行 App

[Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices)

官方说明通过 Device Hub 配对实体设备，并另行处理构建、签名与运行。**建立配对本身不赋予任意 IPA 的签名、安装或 FairPlay 授权。**

### 2.4 官方资料的边界

本次官网查阅未取得足以复现本文免输码流程的完整 Apple RemotePairing 规范。以下实现细节来自用户提供的成功源码与当前脚本，不标作“Apple 官方公开协议”。

## 3. 系统版本：目前确认到哪里

用户提供的 `Swift/InstallerModel.swift:110` 有以下入口检查：

```swift
 guard #available(iOS 27.0, *) else {
   pairingMessage = "设置内配对需要 iOS 27；当前系统可导入 RemotePairing 记录。"
 }
```

这是源码摘录，省略了分支内其他语句。

- 该工程把**设置内反向配对整体入口**限制为 iOS 27+，不仅限制免输码开关。
- `responder.rs` 注释也把设备主动配对描述为从 iOS 27 开始的流程。
- 用户报告当前原生工程已成功免输码。
- **不能只凭工程版本检查得出 Apple 全部免输码方式的最低版本。** 更早系统是否存在其他无需输入配对码的配对路径，本文未验证。
- 修正后的 Scripting responder 尚无本轮真机成功反馈，不能据离线测试扩大版本支持范围。

## 4. 成功原生源码位置

源码根目录：

```text
/var/mobile/Library/Mobile Documents/com~apple~CloudDocs/Downloads/免码配对源码/
```

| 文件 | 作用与关键位置 |
|---|---|
| `先看这里.md` | 原作者归档说明及实现导航 |
| `Swift/LocalPairingHost.swift:69–153` | `run(pinless:...)`；准备 Rust responder、监听 TCP、回调状态、保存配对记录与 host IRK |
| `Swift/LocalPairingHost.swift:55–62` | 免输码模式只报告阶段；有 PIN 模式才展示验证码 |
| `Swift/InstallerModel.swift:110` | iOS 27 入口检查 |
| `Rust-idevice/idevice/src/remote_pairing/responder.rs:67–69` | `allows_pinless_pairing` 配置 |
| `responder.rs:94–107` | Bonjour TXT 记录 |
| `responder.rs:180–245` | handshake、角色检查及能力响应 |
| `responder.rs:268–273` | 免输码使用固定 `000000`；普通模式生成随机六位数 |
| `responder.rs:248–414` | SRP、M1–M6、设备身份解析及记录输出 |
| `Rust-idevice/ffi/src/pairing_host.rs` | `pairable_host_prepare` / `pairable_host_accept_fd` 的 C FFI |

保留归档内许可证和来源说明；该目录是源码归档，不是完整可独立编译的 Xcode 项目。

## 5. 网络角色：最容易做错的部分

```text
主机/脚本                               iPhone 系统设置
    │                                        │
    ├─ TCP 通配监听、发布 Bonjour ────────────►│ 发现主机
    │◄──────────── 用户选择后主动 TCP 连接 ───┤
    │◄──────────── handshake / M1 ────────────┤
    ├───────────── handshake response / M2 ──►│
    │◄──────────── M3 ────────────────────────┤
    ├───────────── M4 ───────────────────────►│
    │◄──────────── M5 ────────────────────────┤
    ├───────────── M6 ───────────────────────►│
```

| 项目 | 手机 | 主机/脚本 |
|---|---|---|
| TCP 角色 | client / initiator | server / listener |
| RemotePairing `originatedBy` | `host` | `device` |
| SRP 角色 | client / controller | server / accessory |

**物理设备是手机，不代表信封里一定写 `device`。** 这里是相对于协议发起方的角色。

该流程不需要脚本先主动连接 `10.7.0.1:49152` 来判断手机是否允许免输码。那个入口用于另一类主动客户端流程或后续验证，不能拿它的握手能力代替本 responder 应声明的能力。

## 6. Bonjour 服务与 TCP 帧

### 6.1 广播

```text
类型：_remotepairing-pairable-host._tcp
实例名：本次主机身份 identifier
端口：TCP listener 分配的端口
```

对应 TXT：

| key | 值 |
|---|---|
| `name` | 显示名称；脚本使用 `IPA Installer` |
| `identifier` | 与实例名及配对身份一致的主机标识 |
| `authTag` | host altIRK 与 identifier 派生的 Base64 标签 |
| `model` | 原实现使用 `Mac17,7` |
| `flags` | `1` |
| `ver` | `26` |
| `minVer` | `17` |

当前脚本的 authTag 实现使用 SipHash-2-4：16 字节 host IRK 为 key、identifier UTF-8 为消息，输出按既有实现取反向排列的 6 字节，再 Base64。不要与设备的 altIRK 混用。

原 Swift 实现绑定 IPv4 通配地址并检查入站来源为本机；当前 TS responder 使用 node:net 通配监听，未完整移植其本机来源检查，属于实现差异与待加固项。

### 6.2 RemotePairing 帧

```text
9 字节 ASCII "RPPairing"
+ 2 字节 big-endian JSON UTF-8 长度
+ JSON UTF-8 body
```

明文信封结构：

```json
{
  "message": { "plain": { "_0": "业务消息对象" } },
  "originatedBy": "device",
  "sequenceNumber": 0
}
```

此例 `_0` 为说明占位，实际应为 handshake 或 event 对象。发送方向各自维护序号；TCP 是字节流，必须处理拆包、合包，不能把一次 read 当成一帧。

## 7. 免输码握手

设备发来 `request._0.handshake._0`。responder 拒绝 `hostOptions.attemptPairVerify=true`，因为此入口只处理首次 pair-setup。

主机响应的关键部分：

```json
{
  "wireProtocolVersion": 26,
  "minimumSupportedWireProtocolVersion": 8,
  "deviceOptions": {
    "allowsPairSetup": true,
    "allowsPinlessPairing": true,
    "allowsIncomingTunnelConnections": false,
    "allowsUpgradeOfLockdownPairings": false,
    "allowsSharingSensitiveInfo": false
  },
  "peerDeviceInfo": {
    "udid": "",
    "deviceKVSIncludesSensitiveInfo": false,
    "identifier": "",
    "name": "IPA Installer",
    "model": "Mac17,7"
  }
}
```

以上对象置于 `response._1.handshake._0`，`response.forRequestIdentifier` 对应请求。原 Rust 归档写死 0；当前 TS 在请求提供 identifier 时回传匹配值，缺省使用 0。

这里 `allowsIncomingTunnelConnections=false` 是 responder 自报不提供后续入站隧道，不代表手机设备服务无法另建隧道。

**只有把 `allowsPinlessPairing` 与 SRP password 同步切换，才是该源码的免输码实现。仅隐藏随机 PIN 的 UI 不是免输码。**

## 8. SRP 与 M1–M6

采用 SRP-6a，SHA-512，3072-bit group，generator=5，username=`Pair-Setup`。

### 8.1 模式差异

| 模式 | handshake 能力 | SRP password | UI |
|---|---|---|---|
| 免输码 | `allowsPinlessPairing=true` | `000000` | 不显示六位码；提示去设置确认 |
| PIN | `allowsPinlessPairing=false` | 随机六位数字 | 显示本次验证码，用户在设备输入 |

### 8.2 消息表

| 步骤 | 方向 | TLV8 内容与处理 |
|---|---|---|
| M1 | 手机 → responder | State=1；检查 Method 若提供则为0 |
| M2 | responder → 手机 | State=2、随机16字节Salt、SRP公钥B（当前实现384字节） |
| M3 | 手机 → responder | State=3、公钥A、64字节client proof |
| M4 | responder → 手机 | 校验client proof；成功发送State=4与server proof；失败发认证错误2 |
| M5 | 手机 → responder | State=5、EncryptedData；解密设备身份与OPACK Info |
| M6 | responder → 手机 | State=6、加密后的主机identifier、公钥、签名、Info |

SRP 使用32字节随机服务端私有材料；当前实现遇B长度不是384字节时重新生成。TLV8单条长度最多255字节，超长字段需分片并拼接；当前TS也兼容连续254字节分片。

### 8.3 M5/M6 加密

```text
setupKey = HKDF-SHA512(
  SRP session key,
  salt = "Pair-Setup-Encrypt-Salt",
  info = "Pair-Setup-Encrypt-Info",
  length = 32
)
```

使用 ChaCha20-Poly1305，空 AAD：

```text
M5 nonce = 4个零字节 || ASCII "PS-Msg05"
M6 nonce = 4个零字节 || ASCII "PS-Msg06"
```

nonce为12字节，密文附16字节认证标签。必须校验State、长度、错误TLV与AEAD结果。

### 8.4 身份签名

M6 主机签名：

```text
AccessoryX = HKDF-SHA512(
  sessionKey,
  "Pair-Setup-Accessory-Sign-Salt",
  "Pair-Setup-Accessory-Sign-Info",
  32
)

signature = Ed25519Sign(
  hostPrivateKey,
  AccessoryX || UTF8(hostIdentifier) || hostPublicKey
)
```

M6 OPACK Info 包含 host altIRK、accountID、name、model等；host altIRK须与Bonjour authTag使用的同一份身份材料一致。

当前 TS 对M5有额外检查：若设备提供完整Identifier/PublicKey/Signature，使用Controller-Sign派生值和设备公钥验证签名；部分身份字段拒绝。为兼容原有WLOC，Info-only M5仍可接受，但明确不宣称完成设备长期身份签名验证。不能用主机公钥验证手机签名。

## 9. 保存记录与后续连接

保存的关键材料：

- 主机identifier。
- 主机Ed25519 private seed/public key，各32字节。
- 手机altIRK，16字节，用于匹配手机Bonjour身份。
- host altIRK，16字节，用于主机自己的Bonjour身份。
- 设备名与UDID（设备提供时）。

原Swift将host IRK以 `IPAInstallerHostAltIRK` 写入配对文件；TS当前内部字段为 `hostAltIrk`。跨格式迁移时须显式处理别名，不能假设所有导出格式已保留该字段。

当前TS流程：

```text
M1–M6成功
→ 关闭首次配对listener、连接和公告
→ 使用新记录建立独立pair-verify连接
→ 验证通过
→ 写入本项目Keychain
```

取消、失败或独立验证不通过，不替换原记录。配对完成不等于已建立安装隧道；pair-verify、createTcpListener、RSD服务发现是后续阶段。

## 10. 当前 Scripting 项目如何调用

目录：`scripts/IPA Install Test/`。

- `core/pair_setup.ts`：TCP listener、Bonjour、免输码能力、SRP responder、M1–M6及取消清理。
- `pair.ts`：旧记录验证、新配对协调、验证后保存。
- `index.tsx`：配对入口、状态、PIN手动入口、删除记录。

免输码模式的关键调用：

```ts
const record: PairingRecord = await pairThisDevice(host, "000000", {
  pinless: true,
  onStatus: report,
  shouldStop,
})
```

代码片段中的类型、变量及函数由项目相应模块提供，不是独立可运行脚本。

当前自动入口走上述反向responder，不再调用旧 `core/pair_setup_client.ts`。旧文件对应另一条主动客户端路线，不能作为当前功能的实际调用依据。

**当前策略：免输码失败不自动降级展示PIN。** 未核实可靠的系统不支持信号前，避免把网络错误、用户拒绝、超时误报为不支持；用户需要时可显式选择“直接使用 PIN 配对”。这与最初“自动回退PIN”的计划不同。

## 11. 先前错误与修正

先前实现错误：

1. 把免输码放进主机主动连接手机的客户端流程。
2. 实际用于系统设置配对的responder仍声明 `allowsPinlessPairing=false`。
3. 某些入口错误/能力判断最终转为随机PIN，因此出现“优先无码仍显示码”。

对照用户成功源码后修正为：

- 设备主动连接主机listener。
- responder声明 `allowsPinlessPairing=true`。
- SRP password固定000000。
- UI不展示验证码，提示系统设置确认。
- 明确手动PIN入口，不盲目自动回退。

旧主动客户端的31场景mock只能验证那套代码的内部行为，不构成当前反向免输码流程的真机兼容证据。

## 12. 生命周期与安全

- 广播/listen启动有期限；当前TS listen/publish各10秒。
- 发布后总等待180秒；单次握手90秒，最多3次。
- 约50ms检查取消；停止后关闭公告、listener和socket。
- 晚到的公告/连接须单独清理，不允许取消后复活任务或保存记录。
- 每次异步握手拥有主机密钥副本；pending native crypto未settle前不清零其正在使用的输入。
- 不记录PIN、私钥、session key、完整TLV或身份payload。
- 固定000000不提供随机PIN的秘密性，不能把SRP成功单独当作邻近连接可信。用户系统确认、受控广播和入站来源检查很重要。
- 原生来源检查尚未完整移植到TS，免输码listener应只在用户明确操作时短时开放。
- BigInt和opaque CryptoKey无法由JS保证物理内存确定性擦除。

## 13. 验证状态与验收

已完成：

- 用户原生App免输码成功反馈。
- 当前修正后的responder：本地真实TCP与原生密码学M1–M6测试通过。
- 断言覆盖 `allowsPinlessPairing=true`、共享参数互通、Controller-Sign、254字节分片、取消与晚到公告清理。
- 本轮测试3 PASS / 23 assertions，Bonjour替换为受控公告，不会真实发布或触发手机配对。
- 修改时正式项目TypeScript diagnostics为0。

尚未取得：

- 修正后的TS脚本在真实系统设置内免输码成功日志。
- 旧系统的版本兼容矩阵。
- 能可靠区分“不支持免输码”和其他失败的自动降级信号。

实机步骤：

1. 重开 `IPA Install Test`，必要时点击“重新配对（自动）”，避免只复用旧记录。
2. 等待“免输码配对已就绪”。
3. 在系统设置的开发者配对入口选择 `IPA Installer` 并确认。
4. 应不显示或要求输入六位配对码。
5. 等待独立pair-verify通过、新记录保存。
6. 再建立RSD连接；安装另行以系统Complete为准。

## 14. 参考索引

### Apple 官方

- https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub
- https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device
- https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices

### 本地成功实现

- `Downloads/免码配对源码/先看这里.md`
- `Downloads/免码配对源码/Swift/LocalPairingHost.swift`
- `Downloads/免码配对源码/Swift/InstallerModel.swift`
- `Downloads/免码配对源码/Rust-idevice/idevice/src/remote_pairing/responder.rs`
- `Downloads/免码配对源码/Rust-idevice/ffi/src/pairing_host.rs`

这些本地源码不是Apple官方发布的免输码SDK或完整协议规范。
