---
name: Scripting App 知识库
description: Scripting App 完全知识库。AI Agent 驱动的 iOS 自动化与脚本工作台（开发者 Thom Fang）。涵盖 TypeScript/TSX 脚本、AI Agent、小组件/灵动岛/控制中心/自定义键盘、iOS 原生 API 全集（HealthKit/MapKit/AVCapture/BLE/NLP/Charts 等 33 大类 578 篇官方文档）、VSCode 协同开发（scripting-cli）、npm 包管理、60+ 社区脚本。当用户提到「Scripting」「Scripting App」「iOS 脚本」「TSX 小组件」「灵动岛脚本」「iOS 自动化」「Thom Fang」时触发。
source_url: https://www.scripting.fun
source_repo: https://scriptingapp.github.io
license: MIT
last_sync: 2026-07-26
---
# Scripting App 完全知识库

> 作者: Thom Fang（有智 方）| 开发者: 深圳引世科技有限公司
> 版本: 3.2.0（2026-07-01 更新）| iOS 17.0+ | 大小: 494.3 MB | 评分: 4.8（106评）
> App Store: https://apps.apple.com/cn/app/scripting/id6479691128
> 官网: https://www.scripting.fun
> 官方文档: https://scriptingapp.github.io（GitHub Pages）
> Telegram 群: https://t.me/scriptingappchat
> Telegram 频道: https://t.me/scripting_app（~1.5K subscribers）
> Telegram 频道: https://t.me/scriptableJS（Scriptable教学，也发布Scripting内容）
> GitHub: https://github.com/ScriptingApp（5 个仓库）
> 开发者 GitHub: https://github.com/ThomFang（⭐55，14 个仓库，6 个开源：drunk MVVM 框架/canvas2djs 游戏引擎/scripting-cli/xcode-localizable-translation/scripting-music/flutter_qjs）
> 隐私政策: https://scripting.fun/privacy_policy/zh.html
> 使用条款: https://scripting.fun/terms/zh.html
> 附带文档：llms.txt（90KB 文档索引）+ llms-full.txt（2.9MB 全量文档，103587行，1162个文档片段）---

## 目录

1. [概述](#1-概述)
2. [核心能力](#2-核心能力)
3. [开发环境与工具链](#3-开发环境与工具链)
4. [脚本系统](#4-脚本系统)
5. [UI 组件系统（TSX + SwiftUI）](#5-ui-组件系统tsx--swiftui)
6. [小组件 / Widget](#6-小组件--widget)
7. [AppIntent / 快捷指令集成](#7-appintent--快捷指令集成)
8. [AI / Assistant](#8-ai--assistant)
9. [iOS 原生 API 全集](#9-ios-原生-api-全集)
10. [社区生态](#10-社区生态)
11. [版本历史](#11-版本历史)
12. [FAQ / 常见问题](#12-faq--常见问题)

---

## 1. 概述

**Scripting App** 是一款 AI Agent 驱动的 iOS 自动化与脚本工作台。它让用户在 iPhone/iPad 上使用 **TypeScript/TSX** 编写脚本，调用 **iOS 原生 API**，创建 **小组件/灵动岛/自定义键盘**，并与 **AI Agent** 深度集成。

**一句话**：Scripting = JSBox 的现代替代 + AI Agent + 原生 iOS API + 小组件引擎

### 与同类工具对比

| 能力 | Scripting | JSBox | Pythonista | Shortcuts |
|------|-----------|-------|-----------|-----------|
| TypeScript/TSX | ✅ 原生支持 | ❌ | ❌ | ❌ |
| AI Agent | ✅ 内置 | ❌ | ❌ | ❌ |
| 小组件 | ✅ TSX 实时预览 | ✅ | ❌ | ❌ |
| 灵动岛 | ✅ | ❌ | ❌ | ✅ 有限 |
| 自定义键盘 | ✅ | ❌ | ❌ | ❌ |
| 控制中心控件 | ✅ (iOS 18+) | ❌ | ❌ | ✅ |
| 原生 API | ✅ 丰富 | ✅ 中等 | ✅ 有限 | ✅ 中等 |
| npm 包管理 | ✅ Package Manager | ❌ | ✅ pip | ❌ |
| VSCode 协同开发 | ✅ scripting-cli | ❌ | ❌ | ❌ |
| Python 运行 | ✅ 内嵌 | ❌ | ✅ | ❌ |

---

## 2. 核心能力

### 2.1 AI Agent 驱动的自动化

Scripting 不只是脚本工具，它内置了 **AI Agent** 系统：
- Agent 可以调用工具、运行脚本、读写文件、访问 iOS 原生能力
- 支持 **Skills**（可扩展能力包）：Git、SSH、网页抓取、地图、天气、照片、日历、快捷指令、通知、视频合成等
- 支持 **MCP 风格工具集成**
- 用户可使用自己的 API Key 接入各种 AI 服务

### 2.2 脚本能力

- 自定义 **小组件**（主屏幕/锁定屏幕）
- **控制中心小组件**（iOS 18+ Control Widget）
- **灵动岛**（Live Activities）
- **自定义键盘**
- **快捷指令**（App Intents）
- **分享菜单**（Share Sheet 扩展）
- **Safari 浏览器脚本**
- **通知**（Rich Notifications）

### 2.3 开发体验

- **移动端编辑器**：支持语法高亮、自动补全、代码提示、语法检查
- **VSCode 脚手架**（scripting-cli）：桌面编辑 + 手机实时预览 + 双向同步
- **实时预览**：修改代码后立即在手机上看到效果
- **TypeScript 强化**：类型检查、自动完成

---

## 3. 开发环境与工具链

### 3.1 scripting-cli（桌面 CLI 工具）

GitHub: https://github.com/thomfang/scripting-cli

```bash
# 安装（无需全局安装）
npx scripting-cli start

# 指定端口
npx scripting-cli start --port=4000

# 启用 Bonjour 自动发现
npx scripting-cli start --bonjour

# 指定编辑器
npx scripting-cli start --editor=cursor
```

**支持的编辑器**：VSCode、VSCode Insiders、VSCodium、Cursor、Windsurf、Trae、Zed、WebStorm、IntelliJ IDEA、Fleet、Sublime Text、Nova、Vim、Neovim、Emacs + 自定义

**配置文件** `scripting.config.json`：
```json
{
  "editor": "cursor",
  "port": 3000,
  "autoOpen": true,
  "generateTsConfig": true,
  "logLevel": "info",
  "ignore": ["*.log", "dist"]
}
```

**特性**：
- 双向文件同步（桌面 ↔ 手机）
- 实时代码同步，保存即运行
- 支持图片/二进制文件同步
- 支持 Bonjour 自动发现

### 3.2 Package Manager（npm 包管理）

GitHub: https://github.com/ScriptingApp/Package-Manager

App 内建的包管理器，支持：
- 搜索 npm 包
- 从 unpkg.com 下载 bundled JS 文件
- 自动 symlink 到脚本的 modules 目录
- 通过 `import xxx from './modules/xxx'` 使用

**限制**：
- 只支持提供 bundled 单文件的纯 JS 包
- 不支持 Node.js API 依赖
- 不支持自动安装依赖
- 不支持 `.d.ts` 类型声明下载

### 3.3 脚本文件结构

```
my-script/
├── index.tsx          # 入口文件（运行时的主界面）
├── widget.tsx         # 小组件文件（主屏幕小组件）
├── app_intents.tsx    # AppIntent 定义文件
├── script.json        # 脚本元数据配置
├── modules/           # 外部模块目录
│   └── dayjs.js       # 通过 Package Manager 安装
└── assets/            # 资源文件
```

**重要**：AppIntent **必须**定义在 `app_intents.tsx` 中。

---

## 4. 脚本系统

### 4.1 脚本类型与执行环境

| 环境 | 触发方式 | 可用 API |
|------|---------|----------|
| `Script.env === "app"` | 用户手动运行 index.tsx | 全部 |
| `Script.env === "widget"` | 小组件刷新渲染 widget.tsx | Widget API + 有限原生 API |
| `Script.env === "app_intents"` | 用户触发 AppIntent | 后台安全 API |
| `Script.env === "live_activity"` | 灵动岛渲染 | Live Activity API |
| `Script.env === "control_widget"` | 控制中心控件渲染 | Control Widget API |

### 4.2 脚本生命周期

- **Script Minimization and Resume**（v2.4.9+）：脚本可在 iPhone 上隐藏 UI 而不终止实例，并监听 resume/重触发事件
- 脚本运行时可保持后台存活

### 4.3 脚本元数据（script.json）

```json
{
  "name": "My Script",
  "description": "Description",
  "author": "me",
  "version": "1.0",
  "icon": "star.fill",
  "background": true,
  "runAtStartup": false
}
```

---

## 5. UI 组件系统（TSX + SwiftUI）

Scripting 使用 **React 风格的 TSX 语法**，底层映射到 **SwiftUI**。所有 UI 组件以标签形式使用。

### 5.1 布局组件

| 组件 | 说明 |
|------|------|
| `VStack` | 垂直排列 |
| `HStack` | 水平排列 |
| `ZStack` | 层叠排列 |
| `ScrollView` | 可滚动容器（v3.1.0+ 支持滚动位置追踪） |
| `List` | 列表 |
| `Grid` | 网格布局 |
| `Spacer` | 弹性间距 |
| `Divider` | 分割线 |
| `Section` | 分组 |

### 5.2 基础 UI 组件

| 组件 | 说明 |
|------|------|
| `Text` | 文本显示，支持富文本、Markdown |
| `TextField` | 文本输入（v3.1.0+ 支持 textContentType） |
| `SecureField` | 密码输入 |
| `TextEditor` | 多行文本编辑 |
| `Image` | 图片显示（SF Symbols / 网络 / 本地） |
| `Button` | 按钮 |
| `Toggle` | 开关 |
| `Slider` | 滑块（v2.4.8+ 支持 thumb 显示控制） |
| `Stepper` | 步进器 |
| `Picker` | 选择器 |
| `DatePicker` | 日期选择 |
| `ColorPicker` | 颜色选择 |
| `ProgressView` | 进度条 |
| `Link` | 链接 |

### 5.3 高级 UI 组件

| 组件 | 版本 | 说明 |
|------|------|------|
| `Map` | v3.1.0 | Apple MapKit 地图，支持标注/路线/3D |
| `MapLookAround` | v3.1.0 | Look Around 街景 |
| `MapSnapshotter` | v3.1.0 | 静态地图截图 |
| `Canvas` | v3.1.0 | Web Canvas 风格 2D 绘图 |
| `PathShape` | v3.1.0 | SwiftUI Path 矢量路径 |
| `Chart` | v3.1.0 | Swift Charts（LinePlot/AreaPlot/柱状图等） |
| `VideoPlayer` | | 视频播放 |
| `WebView` | | 网页视图 |
| `SFSymbol` | | SF Symbols 图标 |
| `MeshGradient` | | 网格渐变 |
| `StyledText` | | 富文本样式 |

### 5.4 图表组件（Charts，v3.1.0）

完整的 Swift Charts 集成：
- `Chart` + `BarMark`/`LineMark`/`PointMark`/`AreaMark`
- `LinePlot`/`AreaPlot`（函数曲线）
- 图表手势（ChartGesture + ChartProxy）
- 图例控制（chartLegend）
- 滚动目标行为（chartScrollTargetBehavior）
- 坐标轴格式化

### 5.5 导航与容器

- `NavigationStack` / `NavigationSplitView`
- `TabView`（底部 Tab 切换）
- `Sheet` / `Popover` / `Alert` / `ConfirmationDialog`
- `Menu` / `ContextMenu`

---

## 6. 小组件 / Widget

### 6.1 支持的组件类型

| 类型 | 说明 |
|------|------|
| **主屏幕小组件** | systemSmall / systemMedium / systemLarge / systemExtraLarge |
| **锁定屏幕小组件** | accessoryCircular / accessoryRectangular / accessoryInline |
| **控制中心小组件** | Control Widget（iOS 18+） |
| **灵动岛** | Live Activities（紧凑/扩展/锁屏模式） |

### 6.2 小组件快速开始

`widget.tsx` 是小组件的入口文件：

```tsx
import { Widget, VStack, Text } from 'scripting-api'

export default function MyWidget() {
  return (
    <Widget>
      <VStack spacing={8} padding={16}>
        <Text font="title">Hello Scripting</Text>
        <Text font="caption" color="secondary">
          {new Date().toLocaleString()}
        </Text>
      </VStack>
    </Widget>
  )
}
```

### 6.3 Widget 关键特性

- **交互性**：支持 Button/Toggle 绑定 AppIntent 实现交互
- **动画**：v3.1.0+ 支持小组件动画（drawOn/drawOff + symbolEffect）
- **着色模式适配**：Tinted Mode 背景适配指南
- **小组件刷新**：支持设置 refreshAfter 时间
- **多尺寸适配**：通过 Script.env 判断尺寸

### 6.4 控制中心控件（Control Widget，iOS 18+）

```tsx
// control_widget_toggle.tsx
ControlWidget.present(
  <ControlWidgetToggle
    intent={MyIntent({ param: value })}
    label={{ title: "My Control", systemImage: "star.fill" }}
    activeValueLabel={{ title: "Active" }}
    inactiveValueLabel={{ title: "Inactive" }}
  />
)
```

### 6.5 灵动岛（Live Activities）

支持三种显示模式：
- **紧凑**（Compact）：Leading + Trailing
- **扩展**（Expanded）：自定义 UI
- **锁屏**：底部区域

```tsx
// 启动灵动岛
LiveActivity.request(attributes, content)

// 更新
LiveActivity.update(using: newContent)

// 结束
LiveActivity.end()
```

---

## 7. AppIntent / 快捷指令集成

### 7.1 AppIntentManager

所有 AppIntent **必须**定义在 `app_intents.tsx` 中：

```tsx
// app_intents.tsx
export const MyIntent = AppIntentManager.register({
  name: "MyIntent",
  protocol: AppIntentProtocol.AppIntent,
  perform: async (params: { id: string }) => {
    // 执行逻辑
    ControlWidget.reloadToggles()
  }
})
```

### 7.2 协议类型

| 协议 | 值 | 说明 |
|------|-----|------|
| `AppIntent` | 0 | 通用操作 |
| `AudioPlaybackIntent` | 1 | 音频播放控制 |
| `AudioRecordingIntent` | 2 | 音频录制（iOS 18+，需保持 Live Activity） |
| `LiveActivityIntent` | 3 | 灵动岛控制 |

### 7.3 Intent.view（v2.4.8+）

Shortcuts 中可以返回自定义 UI：
```tsx
Intent.view({
  type: "view",
  children: [/* TSX UI */]
})
```

---

## 8. AI / Assistant

### 8.1 Assistant API

系统托管的 AI 聊天界面，Scripting 处理 UI、流式输出、Provider 选择和消息生命周期：

- **Conversation APIs**：启动/控制/展示完整的聊天界面
- **requestStreaming**：请求流式响应
- **requestStructuredData**：请求结构化 JSON 数据

### 8.2 本地 AI（LanguageModelSession，v2.4.8+）

设备端 AI 任务：
```tsx
const session = new LanguageModelSession()
const result = await session.generate("Translate to Chinese: Hello")
```

支持：文本生成、结构化 JSON 输出、流式响应

### 8.3 Assistant Tool（v2.4.9+）

构建交互式 Assistant 工具：
```tsx
// 使用 registerUIView 注册交互式 UI
// 返回结构化输出
```

---

## 9. iOS 原生 API 全集

Scripting 封装了大量 iOS 原生 API，按功能分类如下：

### 9.1 系统信息与设备

| API | 说明 |
|-----|------|
| `Device` | 设备信息（型号、系统版本、屏幕尺寸等） |
| `BackgroundKeeper` | 后台保活 |
| `AppStore` | App Store 评级/评论 |
| `DocumentInteraction` | 文档分享/预览 |
| `DocumentPicker` | 文档选择器 |
| `FontPicker` | 字体选择器 |
| `HapticFeedback` | 触觉反馈 |
| `Spotlight` | 系统搜索索引 |

### 9.2 健康与健身（HealthKit）

33 篇文档覆盖完整的 HealthKit API：
- **数据类型**：QuantityType、CategoryType、CharacteristicType
- **样本读写**：QuantitySample、CategorySample、Correlation、HeartbeatSeries
- **统计**：Statistics、StatisticsCollection
- **Workouts**：Workout、WorkoutActivityType、WorkoutEvent
- **ActivitySummary**：活动圆环
- **权限**：HealthKit Permission Behavior

### 9.3 日历与提醒

| API | 说明 |
|-----|------|
| `Calendar` | 日历读写 |
| `CalendarEvent` | 事件创建/查询/修改 |
| `Reminder` | 提醒事项（v2.4.8+ 支持指定日历，v2.4.9+ 支持 get by ID） |
| `EventAlarm` | 事件提醒设置 |

### 9.4 通讯录（Contact）

- 读取/写入联系人
- 联系人分组

### 9.5 定位与地图

| API | 说明 |
|-----|------|
| `Location` | 连续定位/航向流/后台定位 |
| `Map` | MapKit 地图（标注/路线/选择） |
| `MapDirections` | 路线导航 |
| `MapSearch` | 地图搜索 |
| `MapLookAround` | Look Around 街景 |
| `MapSnapshotter` | 静态地图截图 |
| `MapUtils` | 地图工具 |

### 9.6 摄像头与录像

| API | 说明 |
|-----|------|
| `AVCaptureSession` | 摄像头会话（QR 扫码、拍照、视频） |
| `Camera Control` | iPhone 16 硬件按钮控制（iOS 18+） |
| `CaptureVideoPreviewView` | 实时预览视图 |
| `Device formats` | 分辨率/fps/HDR/多摄格式切换 |
| `Live Photo` | Live Photo 拍摄 |
| `VideoRecorder` | 视频录制高级封装 |
| `AudioCapture` | 实时麦克风采集（PCM/RMS/音高） |
| `AudioRecorder` | 音频录制（v3.1.0+ 支持电平计量） |

### 9.7 媒体与音频

| API | 说明 |
|-----|------|
| `AVAsset` | 媒体资源元数据/缩略图 |
| `AVPlayer` | 视频播放（v3.1.0+ 支持自定义请求头） |
| `MediaPlayer` | 直播流（锁屏隐藏进度条） |
| `SharedAudioSession` | 共享音频会话 |
| `SystemMusicPlayer` | 系统音乐播放器控制 |
| `MediaLibrary` | 本地媒体库读取 |
| `MediaComposer` | 媒体合成 |

### 9.8 蓝牙

| API | 说明 |
|-----|------|
| `BluetoothCentralManager` | BLE 中心模式 |
| `BluetoothPeripheral` | BLE 外设 |
| `BluetoothPeripheralManager` | BLE 外设管理器 |
| `BluetoothService` | BLE 服务 |
| `BluetoothCharacteristic` | BLE 特征值 |

### 9.9 自然语言处理（NLP）

| API | 说明 |
|-----|------|
| `Tokenizer` | 分词（词/句/段/文档） |
| `Tagger` | 词性标注/命名实体/情感分析 |
| `Language Recognition` | 语言识别 |
| `Embedding` | 词向量/句向量 |
| `Contextual Embedding` | Transformer 序列嵌入 |
| `Gazetteer` | 自定义词典覆盖 |

### 9.10 图形与图像

| API | 说明 |
|-----|------|
| `Canvas` | Web Canvas 风格 2D 绘图 |
| `Path2D` | SwiftUI Path 矢量路径 |
| `ImageIO` | 图片元数据读写（EXIF/GPS/IPTC）+ 编码（HEIC/TIFF/GIF） |
| `Haptics` | Core Haptics 自定义震动模式（AHAP） |

### 9.11 网络与通信

| API | 说明 |
|-----|------|
| `Remote Push` | 远程推送通知 |
| `Github API` | GitHub API 调用 |
| `WebScraper` | 网页数据抓取（v2.4.9+） |
| `JWT` | JWT 签名/验证/解码（HS/RS/PS/ES/EdDSA） |
| `SSH` | SSH 客户端（command + SFTP） |

### 9.12 输入法 / 自定义键盘

| API | 说明 |
|-----|------|
| `Custom Keyboard` | 自定义键盘脚本（v3.1.0+ 支持脚本切换） |
| `Rime` | Rime 输入法引擎集成（v3.1.0+） |

### 9.13 浏览器与 Safari

| API | 说明 |
|-----|------|
| `Safari Browser Scripts` | Safari 浏览器扩展脚本（v3.1.0+） |
| `Redirect Rules` | URL 重写规则（v3.1.0+） |

### 9.14 存储与文件

| API | 说明 |
|-----|------|
| `FileManager` | 文件管理（v3.0.0+ 支持 WebDAV） |
| `CloudSharedData` | iCloud 共享数据（v3.2.0+） |
| `ctx.storage` | KV 持久化存储 |
| `Shell` | Shell 命令执行（v3.1.0+） |
| `Python` | Python 代码执行（v3.1.0+） |

### 9.15 其他

| API | 说明 |
|-----|------|
| `AlarmManager` | AlarmKit 闹钟/定时器（v3.0.0+） |
| `Alarm Live Activity` | 闹钟灵动岛（v3.0.0+） |
| `TranslationUIProvider` | 系统翻译面板控制（v3.0.0+） |
| `SpeechRecognition` | 语音识别 |
| `Speech (SSML)` | SSML 语音合成 |
| `HeadphoneMotionManager` | 空间音频耳机运动追踪（v2.4.9+） |
| `Notification` | 本地通知（富媒体/附件/操作） |

---

## 10. 社区生态

### 10.1 GitHub 官方组织

**ScriptingApp**（https://github.com/ScriptingApp）：

| 仓库 | 星标 | 说明 |
|------|------|------|
| `Community-Scripts` | ⭐24 | 社区脚本分享（60+ 脚本） |
| `ScriptingApp.github.io` | ⭐8 | 官方文档站（578 篇文档） |
| `Package-Manager` | ⭐8 | npm 包管理器 |
| `skills` | ⭐2 | Skills 示例 |
| `scripts` | - | 官方脚本示例 |

### 10.2 开发者个人仓库

**ThomFang**（https://github.com/ThomFang，⭐55，14 个仓库，26 followers）：

| 仓库 | ⭐ | 语言 | 说明 |
|------|----|------|------|
| `drunk` | ⭐32 | TypeScript | web 前端 MVVM 框架（已归档），高性能/轻量/自定义组件/指令/动画 |
| `scripting-cli` | ⭐13 | TypeScript | Scripting App 桌面 CLI 工具，VSCode/Cursor/WebStorm 等多编辑器支持 |
| `canvas2djs` | ⭐6 | TypeScript | HTML5 Canvas 游戏引擎，支持 Sprite/Texture/Action/TSX |
| `xcode-localizable-translation` | ⭐5 | TypeScript | 用 ChatGPT/Gemini 翻译 Xcode `.xcstrings` 的 Scripting 脚本 |
| `scripting-music` | ⭐3 | TypeScript | 运行在 Scripting App 内的完整 iOS 音乐播放器，74 commits |
| `flutter_qjs` | ⭐1 | C/Dart | Flutter quickjs 引擎（fork），领先上游 11 commits |

### 10.3 社区脚本示例（Community-Scripts 60+）

涵盖类别：
- **工具类**：Gist、RSS、Iconset Helper、URL Scheme 启动台、Script Launchpad
- **数据类**：App Store 多区价格、Goldapi 金价、Twelvedata 金价、上金所金价、东方财富金价、万年历
- **网络类**：Cloudflare Panel、Codex Panel、Vercel Panel、Netlify Panel、Docker 面板
- **媒体类**：Music、网易云歌词、网易云音乐热评、抖音分享下载、影视推荐
- **生活类**：公交、电信小组件、南方电网、文件传输助手
- **娱乐类**：彩票、今日飞机、心算练习、颜色选择器、随机配色
- **文化类**：子午流注、紫微斗数、罗盘、Imperial Dating System、写作助手
- **开发类**：Testfight、SF Symbol 7、openapi-to-llm-text、SnippetIntent Test

### 10.4 Telegram 社区

| 名称 | 链接 | 说明 |
|------|------|------|
| **Scripting App 官方群** | https://t.me/scriptingappchat | 官方交流群组 |
| **Scripting App 频道** | https://t.me/scripting_app | 官方频道，发布小组件/脚本更新（~1.5K subscribers） |
| **Scriptable教学** | https://t.me/scriptableJS | 频道，也发布 Scripting 内容 |

### 10.5 学习资源

- **官方文档**：https://scriptingapp.github.io（578 篇，含 llms.txt 供 AI 使用）
- **App Store 页面**：https://apps.apple.com/cn/app/scripting/id6479691128
- **官网**：https://www.scripting.fun

---

## 11. 版本历史

| 版本 | 发布日期 | 主要更新 |
|------|---------|---------|
| 3.2.0 | 2026-07-01 | Node.js/npm 支持、CloudSharedData API、Bug 修复 |
| 3.1.0 | - | 大量新增：AVCapture、Charts、MapKit、NLP、Haptics、Canvas、Path2D、ImageIO、Location、Python、Shell、Safari 脚本、Redirect Rules、Custom Keyboard 切换、Rime、Spotlight、Photos、MediaPlayer 直播、ScrollView 追踪、symbolEffect 动画、Remote Push、Github API、AudioCapture、AudioRecorder 电平计量、Camera Control、Live Photo、Search Shortcuts |
| 3.0.0 | - | AlarmKit 闹钟/Live Activity、FileManager WebDAV、TranslationUIProvider |
| 2.4.9 | - | Assistant Tool 交互式 UI、CalendarEvent.get、HeadphoneMotionManager、JWT、MediaLibrary、Reminder.get、Script Minimization/Resume、SystemMusicPlayer、WebScraper |
| 2.4.8 | - | Intent.view、LanguageModelSession、Rich Text、Slider 增强 |

---

## 12. FAQ / 常见问题

### Q: Scripting 和 JSBox 有什么区别？
Scripting 是 JSBox 的现代替代，使用 TypeScript/TSX 替代 JavaScript，增加了 AI Agent、更多原生 API、小组件实时预览、VSCode 协同开发等能力。

### Q: 需要 iOS 多少版本？
iOS 17.0 或更高版本。

### Q: 支持 iPad 吗？
支持，专为 iPad 设计，有 systemExtraLarge 小组件尺寸。

### Q: 如何导入社区脚本？
在 Community-Scripts 仓库下载 `.scripting` 文件，在 Scripting App 中导入即可。

### Q: 能用 Python 吗？
v3.1.0+ 内置 Python 解释器，可执行 Python 代码片段（与 Shell.run 共享串行队列）。

### Q: 能运行 Node.js 吗？
v3.2.0+ 新增 Node.js/npm 支持。

### Q: 怎么在桌面端开发？
使用 `npx scripting-cli start` 启动本地服务，Scripting App 连接后即可双向同步。

### Q: 收费模式？
免费下载，内购 Scripting Pro 解锁全部功能。

### Q: 隐私安全？
开发者声明不收集任何数据。脚本数据存储在 App 沙盒和 iCloud Drive。

### Q: 能访问哪些系统 API？
几乎涵盖所有 iOS 原生能力：HealthKit、MapKit、AVCapture、Core Bluetooth、Natural Language、Core Haptics、Calendar、Reminder、Contacts、Location、Photos、Spotlight、FileManager 等。