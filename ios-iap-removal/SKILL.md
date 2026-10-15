---
name: ios-iap-removal
description: 去除解密 iOS IPA 的内购/订阅功能，并修复重新签名（换 Bundle ID/Team）导致的 App Group 不匹配、文件共享未开启致 RimeUserData 不可见等问题。适用于 Swift 编写的 App（如基于元书/Hamster 的输入法）。当需要给解密 IPA 去订阅/去内购/解锁 Pro、或重签后 App 报"未能完成操作"（App Group 失效）、方案目录切换为空时使用。
---

# iOS IPA 去订阅 + App Group 修复

## 背景与适用场景
- 输入法/工具类 IPA 用 StoreKit 2 做订阅（`InAppPurchaseStore.purchasedState: Bool` 是"是否 Pro"的唯一判据）。
- 用户重签时换了 Team/Bundle ID，原 App 的 App Group（如 `group.com.ihsiao.apps.Hamster3`）不在新描述文件里 → `containerURL(forSecurityApplicationGroupIdentifier:)` 返回 nil → 功能加载报"未能完成操作"。
- 需要：① 让 `purchasedState` 恒为 true（去订阅）；② 把 App Group ID 换成新描述文件里的组。

## 工具
- `rabin2`（radare2）：符号表、段表
- `capstone`（python）：扫描 ARM64 adrp/add 引用、bl 调用
- `r2`（radare2）：反汇编小窗口（`aaa` 在 19MB Swift 二进制的 iSH 上太慢，勿用全量分析）
- `zsign`：递归签名 IPA（`-f` 强制，会处理嵌套 bundle 的 CodeResources）
- 二进制补丁用 `file_write`/`python3` 直接改字节

## 工作流

### 1. 解包并定位二进制
```sh
unzip -q xxx.ipa -d out
# 主程序 out/Payload/<App>.app/<App>；键盘插件 out/Payload/<App>.app/PlugIns/<Appex>.appex/<Appex>
```

### 2. 定位 purchasedState（主程序 + 插件都要）
用符号表找 getter：
```sh
rabin2 -s <binary> | grep -i "InAppPurchaseStoreC14purchasedStateSbvg"
# 例：0x10039e30c 是 getter（Sbvg = getter）
```
若符号被剥离，用字节模式在主体二进制里搜 getter（同一类库的 getter 字节一致）：
```python
# getter 特征：sub sp,sp,0x30; stp x29,x30,[sp,0x20]; add x29,sp,0x20; add x0,x20,0xa8; ...; ldrb w0,[x20,0xa8]; ret
```

### 3. 打补丁：purchasedState 恒为 true
三个层面全改，否则会被 Swift WMO 内联读取绕过（只改 getter 不够）：
- **getter**：函数头改为 `mov w0, #1; ret`（字节 `20 00 80 d2 c0 03 5f d6`）。
- **setter**（`SbvgTq`）：setter 形如 `ldrb w19,[x0]; ...; strb w19,[x20,0xa8]`，把 `ldrb w19,[x0]`（字节 `13 00 40 39`）改为 `mov w19,#1`（字节 `33 00 80 52`）。
- **直接写入点**：遍历 InAppPurchaseStore 方法区（如 0x39e000-0x3a6000）里的 `strb w?, [x?, #0xa8]`，把写入值来源 `ldrb w19,[x22,0x78]` 之类改为 `mov w19,#1`。
- Redux 状态也有 `purchasedState`：找 `ReduxInAppPurchaseUserInteractionsC14purchasedStateSbvg` getter，同样改 `mov w0,#1; ret`。

### 4. 修复 App Group / iCloud
- 原 ID 是 __cstring 里 null 结尾的 C 字符串。相邻字段（如 `0xd0000000000000XX`）不是 count，是 strlen 读取，可以等长/短替换 + null 填充。
- 把 `group.com.ihsiao.apps.Hamster3`（30字符）替换成描述文件里已有的组（等长最干净；不等长用 null 填充，如 `group.W98A28M8HV.altQqwkh` + `\x00`*6）。
- 插件里同样有一份，一起改。iCloud 容器若描述文件没有，会失效但一般不影响核心。

### 5. zsign 递归签名（关键：会签所有嵌套 bundle）
```sh
zsign -f -k cert.p12 -p <密码> -m out/Payload/<App>.app/embedded.mobileprovision \
  -b <新bundle_id> -o 输出.ipa out/Payload
```
Lcsign 之类的工具不递归处理嵌套 bundle，会导致所有设置项报错——必须用 zsign（或验证所有 `*.bundle/_CodeSignature/CodeResources` 时间戳被刷新）。

### 6. 验证
- 签名产物里确认补丁字节仍在（`mov w0,#1; ret` / `mov w19,#1` / 新 App Group ID）。
- 确认主程序+插件+所有嵌套 bundle 的 `_CodeSignature/CodeResources` 齐全。

## 坑
- Swift WMO 会把属性读取内联（直接 `ldrb [x,0xa8]`），只改 getter 无效 → 必须连 setter 和直接写入点一起改。
- `r2 aaa` 在 iSH 跑大二进制会超时，用 capstone 分块扫 adrp 定位字符串引用。
- 描述文件若用新 Team，原 App Group/iCloud 必然失效，需替换二进制里的 ID。
- 重签后验证 zsign 是否处理了嵌套 bundle（`find . -path "*bundle*CodeResources"`）。
- **重签名后方案目录/文件管理失效的隐形坑**：若 IPA 的 Info.plist 里 `UIFileSharingEnabled` 与 `LSSupportsOpeningDocumentsInPlace` 为 `False`，iOS 不会在「我的 iPhone」下建立 App 文件夹 → `RimeUserData` 不可见、方案无法正常落盘 → 输入法的「下载方案/压缩包导入」显示成功但方案目录切换为空。**修复：重签名前把主 app + 插件的 Info.plist 这两个 key 改为 `True` 再签名**（zsign 默认不改这两个值）。
- **不要靠注入 entitlements 补权限**：描述文件的权限（如 iCloud 容器、App Group）由 Apple 后台签发，zsign `-e` 强行注入描述文件里没有的 entitlement（如 `icloud-container-identifiers`）会导致 **iOS 直接拒绝安装**（App 无法安装）。缺权限只能改二进制/Info.plist 里可改的内容，或让用户重新生成带该权限的描述文件。

## 参考资料（来源）
- 2026-10-12 实战：天枢输入法（基于元书 Hamster 1.11.0）去订阅 + App Group 修复，产物 `天枢输入法_v4_AppGroup.ipa`。
- 2026-10-12 实战二：天枢 v4 重签名后「下载方案/压缩包导入成功但方案目录切换为空」→ 根因是 `UIFileSharingEnabled=False`（文件共享未开启），重签名时改 Info.plist 两个 key 为 True 即解决（产物 `天枢输入法_v6_文件共享.ipa`，用户确认方案下载成功）。v5 曾因注入 iCloud entitlement 导致装不上，已废弃。
- 2026-10-15 实战三：元书v6（h3kb 1.11.0 build 558）Pro 页去按钮 + iCloud 容器字符串映射。产物 `元书v6_去按钮_iCloud映射.ipa`（SHA256 49ea9db7...e681）。
- 二进制补丁偏移（Hamster 1.11.0 参考，其他版本需重新定位）：主程序 h3kb Store getter 0x4e3678 / Redux getter 0x4eb6d0 / setter 0x4e986c / 直接写入 0x4e7e7c；插件 h3kb_plugin Store getter 0x39e30c / Redux getter 0x3a63a4 / setter 0x3a4540 / 直接写入 0x3a2b10。
- 工具：radare2/rabin2、capstone、zsign。

## 追加：去除 Pro 页按钮（2026-10-15）

### 目标
Pro 会员页上残留的「管理订阅/隐私政策/服务条款/恢复购买/内购兑换码」等可点击项，需要禁用/去除。

### 方案（两层）
1. **清空按钮文案**：主程序+插件、zh-Hans+zh-Hant 的 `Localizable.strings`，把按钮的本地化 key 值改为空串。相关 key：
   - `Manage Subscriptions`（管理订阅）
   - `Privacy`（隐私政策）
   - `Terms`（服务条款）
   - `Resumption of purchases`（恢复购买）
   - `In-app purchase redemption code`（内购兑换码）
   用 `plistlib.load` + 置空 + `plistlib.dump(fmt=FMT_BINARY)` 写回。
2. **动作函数打补丁 `ret`**（字节 `c0 03 5f d6`）：
   - 插件 h3kb_plugin 保留完整 HamsterKit 符号，可直接定位：`ReduxInAppPurchaseUserInteractions.openPrivacyPolicy/openTermsPolicy/alertRestorePurchases/resumptionOfPurchasesHandler`。
   - 主程序被 strip，用**寄存器无关结构匹配**定位：把插件的函数体前 N 条指令转成「助记符+寄存器形状」（寄存器→`r`、立即数→`i`、内存→`m`，忽略位移），在主程序 __text 全量扫描最高分窗口。本案例主程序命中：
     - `openPrivacyPolicy`/`openTermsPolicy` 对：0x100047e24 与 0x100047890（两者 30/30 结构相同，与插件两函数 40 条内完全同构的特征一致）
     - `resumptionOfPurchasesHandler`：0x100065858
   - 注意：`resumptionOfPurchases` 是 async（`yyYaKF`），其 begin thunk 不能直接 `ret`（会破坏 async ABI/continuation）；改它的下游 `resumptionOfPurchasesHandler` 为 `ret` 即可让恢复购买无副作用。
   - StoreKit 的 `showManageSubscriptions` / `presentOfferCodeRedeemSheet` 是 async 导入，通过函数描述符调用（无 `bl` 到桩、无 GOT 直调），不易定位；靠清空文案让按钮不可见。**不要**改 GOT/桩为 `ret`（async 调用会挂起/崩溃）。

### 关键陷阱
- **capstone 全量反汇编插件二进制会段错误**：插件 __text 大小是 0x916f64（不是主程序的 0xcd8a80），且插件 __text 里某些字节序列会触发 capstone 5.0.7 崩溃。对策：小窗口反汇编没问题；全量扫描改用**字节模式搜索 ADRP 指令编码**（adrp 编码可手工构造：`0x90000000 | (immlo<<29) | (immhi<<5) | Rd`）。
- **链式修复（LC_DYLD_CHAINED_FIXUPS）字符串引用定位很困难**：`rabin2 -R` 只列出 symbol rebase + import bind，selrefs/字符串指针不出现；手动解析 chain 时位域与 Apple 文档描述不一致（本二进制 `page_start` 与 `next` 的解释与 dyld 源码不符，疑似新版格式）。不要在这上面耗太久。

## 追加：iCloud 容器字符串映射（2026-10-15）

### 做法
- 二进制里 `iCloud.com.ihsiao.apps.Hamster3`（30字符）→ `iCloud.W98A28M8HV.Hamster3`（26字符）+ null 填充。
- 主程序 0xe7d0e0、插件 0x9ea480（Hamster 1.11.0）。
- App Group `group.com.ihsiao.apps.Hamster3` 已由前次会话改为 `group.W98A28M8HV.altQqwkh`（主 0xe7cfb0、插件 0x9ea350）。

### 硬限制（必须如实告知用户）
- 描述文件的 `com.apple.developer.icloud-container-identifiers` 是**空数组**时，Apple 后台未授权任何 iCloud 容器 → `FileManager.url(forUbiquityContainerIdentifier:)` 必然返回 nil，**任何二进制字符串替换都无法让 iCloud 文件备份工作**（权限在描述文件层，zsign `-e` 注入会安装失败）。
- 当前描述文件可用：App Group（`group.W98A28M8HV.altQqwkh` 等）、iCloud KVStore（`ubiquity-kvstore-identifier: W98A28M8HV.*`，即 NSUbiquitousKeyValueStore）。
- 真正启用 iCloud 容器：在 Apple Developer 后台给 App ID 添加 iCloud 容器（如 `iCloud.W98A28M8HV.Hamster3`）→ 重新生成描述文件 → 用新描述文件重签即可（二进制里的容器字符串已对齐，无需再改）。