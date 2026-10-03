---
name: StikDebug iOS JIT 加速
description: StikDebug（旧名 StikJIT）免电脑启用 iOS JIT 加速工具的完整知识库。涵盖侧载安装、iLoader 配对文件生成、LocalDevVPN、启用 JIT、GPS 虚拟定位、iOS 26 兼容性与排错。当用户提到「StikDebug」「StikJIT」「免电脑启用 JIT」「iOS JIT 加速」「配对文件 pairingFile」「LocalDevVPN」「iLoader」「模拟器 JIT」时触发。
version: 1.0.0
last_sync: 2026-10-03
---

# StikDebug 免电脑启用 iOS JIT 加速

## 概述

StikDebug（旧名 **StikJIT**）是 **on-device JIT enabler**：免电脑、无需越狱，在设备上直接为侧载 App 启用 JIT（Just-In-Time 动态编译）。由 **Jackson Coxson** 开发，开源（AGPL-3.0），仓库 `StikDebug/StikDebug`。

- 适用：**UTM、PojavLauncher、PPSSPP、RetroArch、Flycast** 等模拟器/侧载 IPA，JIT 加速后可大幅提升执行效能
- 额外功能：**GPS 虚拟定位**（Location Simulator）
- 原理：基于 **idevice**（libimobiledevice），通过设备 RSD 隧道为另一进程启用 JIT；iOS 26 的 JIT 主要靠**自动化脚本**（TXM scripts）实现
- 状态：曾上架 App Store 后被 Apple 下架，**必须手动侧载 IPA**
- 官网：<https://stikdebug.xyz/>（组织页）

## 兼容性矩阵（官方 README）

| iOS 版本 | 状态 | 备注 |
|---|---|---|
| 1.0 – 17.3.x | ❌ 不支持 | 使用不同连接协议 |
| 17.4 – 18.x | ✅ 完全支持（稳定） | 主力使用区间 |
| 26.0+ | ⚠️ 支持 | App 可用性有限，需开发者更新 App 适配 |

**关键限制**：
- **iOS 26 上 App Store 版 App 无法启用 JIT**，必须侧载 IPA（如 RetroArch 需从 GitHub 侧载，不能用 App Store 版）
- 启用 JIT 的前提：侧载 App 带 `get-task-allow` entitlement
- App 关闭后需重新到 StikDebug 启用 JIT
- Pairing file 在 iOS 系统更新后可能失效，需重新生成

## 安装链路（四步）

### 1. 侧载 StikDebug IPA
- 下载官方 Release IPA：`https://github.com/StikDebug/StikDebug/releases`（如 `StikDebug-3.1.13.ipa`，12.9 MB，附 sha256）
- 用 **SideStore / AltStore / 自签工具**（或其他侧载工具）安装
- 已侧载 IPA 由 AltSource / direct .ipa / 自编译提供

### 2. 生成 Pairing File（一次性，必须用电脑）
⚠️ **不要用 Jitterbugpair，已停止维护！**

推荐工具：**iLoader**（`StikDebug/iLoader`）
1. 电脑（Windows/Linux/macOS）安装 iLoader
2. 登录 Apple ID，与 iPhone 配对
3. 按「管理配对档案」→ 点「**放置**」配对档案到 StikDebug（自动写入 App）
   - 或点「**匯出**」手动导出 `pairingFile.plist`
4. 手动导出时，用 **LocalSend** 等方式传到 iOS「文件」App
   - ⚠️ **不要用 iCloud**，副档名会丢失（`.plist` 扩展名不保留）
   - 文件也可用 `.mobiledevicepairing` 格式

### 3. 连接 LocalDevVPN
- 安装 **LocalDevVPN**（回环 VPN）并开启
- 之后 StikDebug 通过 LocalDevVPN 与设备本地通信

### 4. 启用 JIT
1. 首次打开 StikDebug，未放置配对文件时会提示导入 → 选取 `pairingFile.plist`
2. 点「**Enable JIT**」按钮
3. 从列表选择要启用 JIT 的侧载 App
4. 成功后可断开 VPN（iOS 设置 → 一般 → VPN 与装置管理）

## GPS 虚拟定位（可选）

- 路径：StikDebug → **Tools → Location Simulation**
- 在地图上放置图钉 → 选位置 → 按下 **Simulate Location**
- 用 Apple Map 验证即可
- 注意：按 IP 判断位置的网站/服务仍会破功（只欺骗 GPS 类 App）

## 排错（Troubleshooting）

| 现象 | 处理 |
|---|---|
| "Connection dropped" / loopback 错误 | 检查 iOS 版本兼容性表 / beta 警告 |
| Heartbeat 错误 | 确认 VPN 已开、已连 Wi-Fi；可能是 pairing file 问题 |
| Pairing file 问题 | 设备解锁并信任电脑后重新生成/替换 |
| 仍不行 | 带日志/截图加入 Discord（StikDebug 官方 Discord） |

## 相关项目

| 仓库 | 说明 |
|---|---|
| `StikDebug/StikDebug` | 主 App（Swift，2.6k stars） |
| `StikDebug/StikDebug-Guide` | 图文安装指南 |
| `StikDebug/StikJIT` | iOS XCFramework，供其他 App 集成 JIT（基于 StikDebug） |
| `StikDebug/iLoader` | 配对文件生成工具（跨平台） |
| `StikDebug/.github` | 组织 README |
| `chachillie/Flycast-iOS` | Flycast for iOS 26，内置 StikDebug 支持 |
| `truongkma/t-location` | 纯虚拟定位 fork（仅 Location Simulation） |
| `CelloSerenity/iOS-26-Sideloading-and-JIT-Complete-Walkthrough` | SideStore + LiveContainer + StikDebug 完整教程（WIP） |

## 参考资料

- 技术原理（作者解释）：*StikJIT - A Technical Explanation by Jackson Coxson*（SideStore Docs 亦收录）
- SideStore 文档 *Enabling JIT* 章节
- 中文介绍：Ivon 部落格《StikDebug，免電腦啟用iOS的JIT加速！》（2026-07-31）
- 相关玩法：AltStore 启用 JIT、SideStore 免电脑重签 IPA、UDID Registrations 付费签名

## 版本记录

| 版本 | 日期 | 要点 |
|---|---|---|
| 3.1.13 | 2026-10 初 | 修复 MeloCafé 自动分配；最新 |
| 3.1.12 | - | 修复 iOS 26.4 以下 DDI 问题；TXM 脚本/虚拟定位/keep-alive 大量修复 |
| 3.1.11 | - | 改用 cryptex 挂载 DDI，修复 iPhone 18 Pro 系列问题；iOS 26.4+ 上 DDI 仅更新/重置后卸载，不再需要重启 |
| 3.1.9 | - | 尝试修复 pairing file 问题；`rp_pairing_file.plist` 改回 `pairingFile.plist` |