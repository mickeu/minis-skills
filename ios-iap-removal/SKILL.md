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
- 二进制补丁偏移（Hamster 1.11.0 参考，其他版本需重新定位）：主程序 h3kb Store getter 0x4e3678 / Redux getter 0x4eb6d0 / setter 0x4e986c / 直接写入 0x4e7e7c；插件 h3kb_plugin Store getter 0x39e30c / Redux getter 0x3a63a4 / setter 0x3a4540 / 直接写入 0x3a2b10。
- 工具：radare2/rabin2、capstone、zsign。