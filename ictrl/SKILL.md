---
name: iCTRL iOS 真机控制
description: iCTRL 基于 DDI 挂载 + StikDebug 启动的 iOS 真机控制工具知识库。涵盖自签名闪退根因与修复、JSON-RPC 控制接口（device_info / shot / tap / swipe / type / launch_app）、PlugIns 保留规则、开发者模式要求、待机消耗与服务重启。当用户提到「iCTRL」「ictrl.sh」「iOS 真机控制」「自签名闪退」「iOS 控件操作」「device_info」「截取真机屏幕」「xctest 模块」时触发。
version: 1.0.0
last_sync: 2026-10-05
---

# iCTRL iOS 真机控制

## 概述

**iCTRL** 是一个 iOS 真机控制工具：通过挂载 **DDI（Developer Disk Image）** 并借助 **StikDebug** 启动服务进程，对外暴露 **JSON-RPC 接口**，可直接驱动 iOS 真机的各类真实 App（tap / swipe / type / launch 等）。

- 依赖链路：`StikDebug 启动 → DDI 镜像挂载 → iCTRL 服务进程常驻 → 监听 JSON-RPC 请求`
- 典型入口脚本：`/usr/local/bin/ictrl.sh`（真机侧）
- 本机侧调用方式：`sh call <method>`（封装了对真机 RPC 的调用）

## 自签名闪退：根因与修复（关键）

**现象**：自签名安装的 iCTRL 一打开就闪退。

**根因（高置信，来自避坑实践）**：签名工具在重签过程中开启了「移除扩展插件 / 精简体积」类开关，把核心 **xctest 模块** 删掉了 → App 启动时因缺失 xctest 直接崩溃。

**修复（一次性，重签时）**：
- 任何签名工具中的「移除扩展插件」「精简体积」等开关 **必须全部关闭**，保留 **PlugIns** 目录，否则必删核心 xctest 模块。
- 签名时必须 **绑定设备专属 UDID 的个人开发者证书**。
- 安装后 **无需** 在「设置 → 通用 → 设备管理」里额外点信任 —— 但前提是系统 **「开发者模式」已打开**（iOS 16+ 在「设置 → 隐私与安全性 → 开发者模式」）。开发者模式没开时证书即使装了也不会生效。

> 一句话：闪退几乎都是「签名时把 PlugIns/xctest 精简掉了」或「开发者模式没开」。先查这两点。

## AI 自动签名（zsign 方案，2026-10-06）

**背景**：现成签名工具（爱思/AltSign 等）大多只处理普通 App，不处理 Xcode 的 xctest bundle（`PlugIns/*.xctest`），导致 iCTRL 闪退。命令行工具 **zsign** 可正确处理 xctest——「自己签 / 喊 AI 签」用它最可靠。

**环境**：iSH（Alpine）里已编译安装 `zsign 1.1.2`（`/usr/local/bin/zsign`）。编译依赖 `g++ openssl-dev zlib-dev`；源码 `zhlynn/zsign` 在 Linux 下需修复 `json.h` 缺少 `#include <ctime>`（macOS 碰巧间接引入 `time_t`，Linux 会编译报错）。

**一键签名脚本**：`/var/minis/skills/ictrl/scripts/sign_ictrl.sh`
```bash
sign_ictrl.sh <输入.ipa> <证书.p12> <证书密码> [描述文件.mobileprovision] [输出.ipa]
```
- 不传描述文件时自动使用 IPA 内嵌的 `embedded.mobileprovision`
- 脚本自动验证输出 IPA 里 `PlugIns/*.xctest` 是否存在

**实测（ad-hoc）**：`zsign -a` 正确签名 `PlugIns/iCTRLUITests.xctest/iCTRLUITests` 并重新生成 `_CodeSignature`（CodeResources 2834→3194 字节），输出 IPA 结构完整。

**真实签名需要的材料**：
- Apple Development 证书（.p12）+ 密码
- 描述文件：通配符 `*` 即可（示例：XC Wildcard，Team K8Q74NT2BG，49 台设备，2027-08 到期，entitlements 含 `get-task-allow=true`）

**注意**：iSH（PRoot）环境下 zsign 输出 `/tmp/zsign_folder_*` 时可能报 `Operation not permitted` 警告，不影响最终 IPA 生成。

## 核心功能与接口

### 1. 获取设备信息
```bash
sh call device_info
```
成功返回：屏幕 **物理/逻辑分辨率**（如 390×844 pt）、**电量**、以及 **20 项控制接口能力集**（设备支持的控制能力清单）。

### 2. 截取真机屏幕
```bash
sh /usr/local/bin/ictrl.sh shot /tmp/screen.jpg
```
秒级返回真机实时渲染图像，存到指定路径（示例 `/tmp/screen.jpg`）。

### 3. 控件操作（标准 JSON-RPC 方法）
通过 JSON-RPC 直接驱动真实 App，支持的方法包括：

| 方法 | 用途 |
|---|---|
| `tap` | 点击指定坐标 |
| `swipe` | 滑动（指定起点/终点/方向） |
| `type` | 输入文本 |
| `launch_app` | 启动指定 App |

> 调用形式经 `sh call` 封装，具体参数 schema 以真机返回的 20 项能力集为准。需要精确参数时先跑 `device_info` 看能力集定义。

## 实践经验与避坑要点

1. **自签证书属性**：绑定设备专属 UDID 的个人开发者证书安装后，无需在「设置-设备管理」中额外点信任，但前提是必须打开系统「开发者模式」。
2. **保留 PlugIns 目录**：任何签名工具中若有「移除扩展插件」「精简体积」等开关，**必须全部关闭**，否则必删核心 xctest 模块（这是闪退的首要原因）。
3. **日常待机消耗**：iCTRL 在空闲等待 RPC 请求时，CPU 占用约 **5%**，内存占用约 **49MB**，无需频繁关闭。如需退出：通知中心长按通知点「停止服务」，或后台多任务直接划掉。
4. **服务重启**：只要手机未重启，**DDI 镜像始终维持挂载**；后续若重新使用，仅需在桌面点一下 iCTRL 图标即可立刻恢复服务，**无需重新运行 StikDebug**。

## 与 StikDebug / DDI 的关系

- iCTRL 本身依赖 DDI 挂载 + StikDebug 拉起，属于「侧载 + 开发者磁盘镜像」玩法，与 StikDebug JIT 启用链路共用同一套 on-device 基础设施。
- 相关技能：`stikdebug`（免电脑启用 iOS JIT 加速）—— 若 DDI 挂载或 tunnel 建立失败，先按该技能排错。
- **iOS 27 注意**：主线 StikDebug 3.1.13 在 iOS 27.0/27.2 上 tunnel 建立失败（issue #471，open），若 iCTRL 起不来先确认 StikDebug 本身是否可用。

## 版本记录

| 版本 | 日期 | 要点 |
|---|---|---|
| 1.0.0 | 2026-10-05 | 首版：自签名闪退根因（PlugIns/xctest 保留 + 开发者模式）、device_info/shot/控件 JSON-RPC 接口、待机消耗与服务重启经验 |

## 来源

- 用户实测经验（2026-10-05）：自签名闪退已解决，附避坑要点与接口示例。
- 关联：`stikdebug` 技能（DDI / StikDebug 链路排错）。
