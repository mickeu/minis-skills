---
name: Dynamic Lyrics 灵动歌词知识库
description: 灵动歌词 2.0.5 逆向工程知识库。涵盖灵动岛/Live Activity 歌词实现架构、AppGroup 数据共享、LRC 解析、动画系统、内购逻辑。当用户提到「灵动歌词」「Dynamic Lyrics」「灵动岛歌词架构」「Live Activity 歌词」「LiveActivityRefresher」「MarqueeText」「ClockAnimation」时触发。
---

# Dynamic Lyrics 2.0.5 逆向工程知识库

## 基本信息
- **Bundle ID**: `com.bing.lyrics`
- **App Store ID**: 6477542032
- **Team ID**: `NAC5X5LCW4`
- **架构**: ComposableArchitecture (TCA) + Swift Sharing
- **二进制状态**: cryptid=0（未加密），可完整提取符号/字符串/反射元数据

## 文件路径
```
Payload/Dynamic Lyrics.app/Dynamic Lyrics                          # 主App
Payload/Dynamic Lyrics.app/PlugIns/lyricsWidgetExtension.appex/lyricsWidgetExtension  # Widget Extension
```

## 核心架构：Widget 自包含
灵动歌词的核心设计原则：**Widget Extension 自包含，不依赖 App 推送歌词**。

### 数据流
```
App（播放音乐）
  → 每秒写 AppGroup UserDefaults（lyric/position/isPlaying/duration/songName/artist/fontSize）
  → Widget Extension 自读 AppGroup → 自解析 LRC → 自算换行 → 自做动画
```

### AppGroup Keys
```
lyric                          # LRC 歌词文本（全量）
artist                         # 歌手
artwork                        # 专辑封面 URL
currentTime                    # 当前播放位置（秒）
position                       # 备用播放位置
duration                       # 歌曲总时长
fontSize                       # 字号
isPlaying                      # 是否播放中
liveActivityCurrentArtworkColorKey  # 封面主色调
liveActivityCurrentArtworkImageKey  # 封面图片
widgetCurrentArtworkImageKey        # Widget 封面
refreshLiveActivityRealTimeKey      # 实时刷新开关
dynamicIslandSmoothScrollKey        # 平滑滚动开关
dynamicIslandLyricsUseArtworkColorKey  # 用封面色做背景
kLiveActivityPushToStartTokenKEY    # Push to Start token
liveActivityAutoHideTimeKey         # 暂停后自动隐藏时间
hideDynamicIslandOnPauseKey         # 暂停时隐藏灵动岛
```

### ContentState 字段（精简）
```swift
struct ContentState: Hashable, Codable {
    var songName: String
    var artist: String
    var fontSize: Int
    var isPlaying: Bool
    // 歌词文本 NOT in ContentState — Widget 从 AppGroup 直接读
}
```

### Widget 不靠 Activity.update 驱动歌词
Activity.update 只在**切歌/暂停/恢复**时调几次（更新 songName/isPlaying），歌词换行完全靠 Widget 自读 AppGroup + TimelineView 动画。

## LRC 解析（LyricsXCore）
基于 macOS 开源框架 LyricsX 的 iOS 移植版。

### 支持的 LRC 格式
```
[00:00.330]Chandelier - Sia           # 主歌词行
[00:00.330][tr:zh-Hans]               # 翻译行（忽略）
[00:00.330][tt]<0,0><150,11><310,13>  # 逐字时间标签（InlineTimeTag）
```

### LrcParser 核心逻辑
```swift
// 时间标签正则
let timePattern = #"\[(\d{1,2}):(\d{2})(?:[.:](\d{1,3}))?\]"#

// 解析流程
1. 逐行扫描
2. 跳过元数据行 [al:] [ar:] [ti:] [by:] [offset:] [length:] [tr:] [tt]
3. 用正则提取所有时间标签 [mm:ss.xx]
4. 提取最后一个时间标签之后的歌词文本
5. 一行多时间标签时，为每个时间创建一条 LrcLine
6. 按时间排序
```

### LrcLine 结构
```swift
struct LrcLine: Hashable {
    let time: TimeInterval  // 秒
    let text: String
}
```

## 刷新计算引擎：RefreshKeeper
Widget 内部类，**自计算**歌词换行时机。

### 核心函数签名
```swift
// 构造函数
init(lineDuration: Double, elapsed: Double, isPlaying: Bool, refreshLeadTime: Double)

// 刷新计算
static func clockAnimation(
    start: TimeInterval,      // 当前行开始时间
    duration: TimeInterval,   // 当前行时长
    contentWidth: CGFloat,    // 歌词文本宽度
    height: CGFloat,          // 容器高度
    viewL: /* view */,        // 视图引用
    refreshTime: TimeInterval // 下次刷新时间
)

// 行索引查找
func lineIndex2at(time: TimeInterval) -> Int?  // 二分查找

// 重算当前行
func recalculateCurrentLineIndex()
func recalculateCurrentLyrics(startLiveActivity: Bool, forceFlash: Bool, flashDuration: Double)
```

### 关键变量
```
lineDuration          # 当前行时长
elapsed               # 已播放时间
refreshLeadTime       # 提前刷新量（预留动画时间）
nextRefreshInterval   # 下次刷新间隔
nextRefreshDate       # 下次刷新时间戳
currentLineIndex      # 当前行号
refreshTimestamps     # 歌词行时间戳表
lastSongEndTimestamp  # 最后一行结束时间
```

## 动画系统

### 三种动画 Modifier
```swift
ClockAnimationModifier    // 时钟驱动（主力，知道 start/duration/contentWidth/refreshTime）
ScrollAnimationModifier   // 滚动
SwingAnimationModifier    // 摆动
```

### ClockAnimationModifier 参数
```
start          # 当前行开始时间（秒）
duration       # 整行持续时间（秒）
contentWidth   # 歌词文本宽度（pt）
height         # 容器高度（pt）
viewL          # 视图引用
refreshTime    # 下次刷新时间
```

### 动画实现
- **CADisplayLink** + `displayLinkWithTarget:selector:` — 帧级动画（60fps）
- **AnimationTimelineSchedule** — SwiftUI 给 Widget/Live Activity 专用的动画 schedule
  - `AnimationTimelineScheduleV(minimumInterval:paused:)` — 系统允许高频率更新
  - `.periodic` 在 Live Activity 中会卡 3-5 秒，必须用 `.animation`
- **TimelineView(.animation)** — 替代 `.periodic`

### MarqueeText
跑马灯组件，用 CADisplayLink 驱动文字水平滚动。

### SwingAnimationModifier
```swift
swingAnimation(
    text: String,
    duration: Double,
    direction: Direction,  // left/right
    distance: CGFloat,
    delay: Double,
    isPreview: Bool
)
```

## Timeline Provider 三档刷新策略
```swift
getTimelineFlash(in:completion:)    // 快速闪烁模式
getTimelineNormal(in:completion:)   // 普通模式
getTimelineRealTime(in:completion:) // 实时模式（iOS 17+ setExpectsMediaDataInRealTime）
```

### Timeline Entry 存储
```swift
var entries: [Date: Entry]  // 按时间戳存储，Dictionary
```

### Timeline 构造
```swift
Timeline(entries: [...], policy: .after(date))  // 精确指定下次刷新时间
Timeline(entries: [...], policy: .never)         // 不自动刷新
```

### relevance 计算
```swift
TimelineEntry.relevance  // 影响刷新优先级
```

## iOS 27 实时刷新
```swift
// iOS 27 新 API
setExpectsMediaDataInRealTime  // 借用 AVQueuedSampleBufferDisplayLayer 实时媒体数据通道
isReadyForMoreMediaData        // 判断是否准备好接收新数据
iOS27ExperimentalModeKey       // 实验性模式开关
```

## Activity 生命周期管理
```swift
// 创建/更新
Activity.request(attributes:content:policy:)
Activity.update(content:alertConfiguration:)
Activity.end(dismissalPolicy:)

// Content 构造
ActivityContent(state:staleDate:relevanceScore:)
  - staleDate: 过期时间（nil=不过期）
  - relevanceScore: 0.0~1.0（系统资源调度优先级）

// 监听状态变化
ActivityStateUpdates.makeAsyncIterator

// Push to Start
Activity.PushTokenUpdates  // 获取推送令牌
pushToStartTokenUpdates    // 监听推送令牌变化
```

### 结束原因
```swift
EndLiveActivityReason  // 多种结束原因枚举
```

## App 侧 LiveActivityHelper
```swift
class LiveActivityHelper {
    func updateOrStartLiveActivity(start: Bool, activityContent: /* content */)
}
```

## Widget 刷新辅助类
```swift
class RefreshKeeper { /* 核心刷新引擎 */ }
class RefreshPlayer { /* 刷新播放器 */ }
class RefreshState  { /* 刷新状态 */ }
class MusicPlayerTimerHelper { /* 播放计时器 */ }
```

## 内购逻辑（StoreKit 1）

### 产品 ID
```
com.bing.lyrics.premium          # 终身版
com.bing.lyrics.premium.month    # 月度订阅
com.bing.lyrics.premium.year     # 年度订阅
```

### 关键组件
```swift
PremiumView              // 内购 UI 页面
PremiumInfo              // 内购信息模型
ShowPremiumIntent        // AppIntent 快捷唤起内购页
_isPremium               // 是否已购买
_notPremium              // 非 Premium
_showNotPremiumToast     // 未购买提示
getSavedPremiumInfo()    // 读取已保存的购买信息
requestProductsWithProductIdentifiers:queue:completionHandler:  // 请求产品信息
paymentQueue:updatedTransactions:  // 交易状态回调
paymentQueue:updatedFilteredTransactions:  // 过滤后的交易回调
```

### 内购 UI
```swift
SubscriptionView  // 订阅视图
_isPremiumViewPresented  // 是否弹出内购页
_openPremiumViewTag      // 打开内购页标记
```

### 免费获取 Premium
```
https://dynamic-lyrics.super.site/english/common-problem/get-a-free-premium
```

## 播放进度获取
- **MusicKit**: `MusicPlayer.playbackTime`（Apple Music 原生播放器）
- **NowPlaying**: `MPNowPlayingInfoPropertyElapsedPlaybackTime`（第三方播放器兜底）

## 源文件路径（可提取完整模块结构）
```
lyrics/Helper/LiveActivityHelper.swift
lyrics/Helper/LiveActivityRefresher.swift
lyrics/Composable/Store/PremiumView.swift
lyrics/Shared/Data/AppIntent/
lyricsWidget/Widget/Common/LyricsWidget+Provider.swift
LyricsXCore/Sources/LyricsXCore/Composable/
LyricsXCore/Sources/LyricsXCore/Misc/Lyrics+Persist.swift
```

## 关键技术总结

### 为什么 .periodic 在 Live Activity 中不工作
`.periodic(by:0.05)` 在灵动岛 compact/minimal 模式下被 iOS 限制不刷新。**必须用 `.animation`**（AnimationTimelineSchedule），这是 SwiftUI 给 Widget/Live Activity 专用的连续动画 schedule。

### 为什么不能靠 Activity.update 推送歌词
iOS 对 Activity.update 有限流（约 60s 内最多 6 次）。Widget 侧自读 AppGroup + 自算换行是正确方案。

### ContentState 不包含歌词文本
歌词文本通过 AppGroup UserDefaults 传递，不在 ContentState 中。ContentState 只包含 songName/artist/fontSize/isPlaying 等轻量字段。Widget 视图通过 `LyricsSharedData.load()` 从 AppGroup 直接读取歌词数据。

### LRC 逐字标签（InlineTimeTag）
格式：`[tt]<0,0><150,11><310,13>...`
逐字标签是字符级时间信息，用于卡拉OK逐字高亮。灵动岛空间小，不需要逐字高亮，只需逐行滚动。

### 播放进度估算
Widget 读取的 `currentTime` 是 App 最后写入的值。由于 Widget 和 App 之间有时间差，需要估算：
```swift
func estimatedCurrentTime(snapshot: Snapshot) -> TimeInterval {
    let elapsed = Date().timeIntervalSince(snapshot.lastUpdate)
    return snapshot.isPlaying ? snapshot.currentTime + elapsed : snapshot.currentTime
}
```
