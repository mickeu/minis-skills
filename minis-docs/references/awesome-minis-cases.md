# AwesomeMinis 社区案例详情

来源：https://github.com/openminis/AwesomeMinis

## 🏥 健康与生活

### Apple Watch Heart Health Monitor
分析 Apple Watch 的心率、HRV、血氧（SpO2）、ECG 数据，检测早期预警信号并生成风险报告。使用 cardiac-health-monitor 技能。

### Photo a Coffee → Auto-Log Caffeine
拍一张咖啡照片 → Minis 识别咖啡种类 → 自动将咖啡因摄入量记录到 Apple Health。

### Photo Every Meal → Auto-Log Nutrition
每餐拍照 → Minis 识别菜品 → 估算卡路里/蛋白质/碳水 → 全部记录到 Apple Health。

---

## ⚡ 生产力与自动化

### Smart Daily Briefing
每天早晨自动：拉取日历事件、天气、新闻头条、提醒事项 → 合并为单一语音简报。

### X Timeline Voice Alarm
替代闹钟：快捷指令自动抓取 X 时间线 → AI 摘要 → doubao-tts 生成音频 → 播放唤醒。
所需技能：twitter-x-hub, doubao-tts

### Auto-Create Calendar from Shared Content
通过 iOS Share Sheet 分享含时间和地点的内容 → Minis 自动创建日历事件。

### Daily Briefing Auto-Push to WeChat
iPad 上定时运行：获取天气+新闻 → 通过 openilink-hub 自动推送微信。

### Group Messages → Auto-Extract to Reminders
拉取 Telegram 群消息 → 自动提取 Bug 和任务 → 去重 → 写入 Apple Reminders。
所需技能：tg-hub

### Web Page → Apple Notes
发送任意 URL 给 Minis → 抓取网页内容 → AI 摘要 → 结构化保存到 Apple Notes。

### Mount Obsidian Vault
将 Obsidian 仓库挂载到 Minis → AI 对笔记进行总结、清理、研究、回写。使用 Shared Folders 功能。

### Batch Set Complex Alarms
一句话描述整个闹钟计划（如"工作日 7 点，周末 9 点"）→ Minis 一次创建所有闹钟。

### Convert Notes & Ideas into Dida Tasks
脑暴文本/零散笔记 → Minis 提取提炼 → 格式化写入滴答清单（TickTick）。
需要自定义 Dida API 技能。

### Schedule Minis Tasks via iOS Shortcuts
用 iOS 快捷指令自动化触发 Minis 任务。Minis 提供快捷指令动作。

### Edit Clash Config Without Touching YAML
把 Clash 配置文件丢给 Minis → 自然语言描述想改什么 → Minis 读取、编辑、输出新版 + 变更摘要。

### Remote Control Home Phone
从任何地方通过 SSH 或网络远程触发家中 iPhone/iPad 上的 Minis 任务。

### Course Creation Assistant
产品经理用 Minis 完成课程设计、代码、逐字稿。使用 project-case-builder、video-script-writer 技能。

### Taobao Store Management
通过 SSH 构建完整淘宝工具包：订单追踪、比价、购物车管理、买家沟通。零代码基础。

### WeRead AI Reading Companion
连接微信读书账号 → 浏览书架、导出划线、分析阅读习惯、推荐书籍。

---

## 🔬 数据与研究

### Automated Paywall Bypass Article Reader
自动将付费文章 URL 重写为公共存档链接（archive.is/12ft.io 等），在对话中读取全文。

### Fetch HK News & Generate Chinese HTML Digest
获取香港新闻文章 → 翻译并摘要为中文 → 输出格式化 HTML 摘要文档。

### City Commercial Market Research Report
一句话 → Minis 搜索 JLL/赢商/DTZ 数据 → 编写分析脚本 → 生成完整市场报告含图表。

### Tweet Fact-Check: Verify Health Claims
粘贴推文链接 → 获取内容 → 对照医学文献交叉验证 → 输出结构化裁决表（含可信度评分、证据来源）。
所需技能：twitter-x-hub

### MacBook Neo Purchase Decision
一句话 → 基准跑分阶梯对比（单核/多核 vs 所有 MacBook 型号）→ 痛点分析 → 国补价格分解 → AI 生成可分享信息图。
所需技能：nano-banana-2（图像生成）

---

## 🎨 创意与内容

### Search Torrents & Manage qBittorrent
一句话 → 搜索 7 个种子站 → 选最佳版本 → 提取磁力链接 → 远程添加到 qBittorrent → 报告下载状态。
所需技能：exa-search

### Download X/Twitter Videos
粘贴 X/Twitter 视频链接 → 自动安装 yt-dlp → 下载视频+音频流 → ffmpeg 合并 → 自动排错。

### Local Video Compression with ffmpeg
拖入 4K 视频 → 检测编码/码率 → 选择最优 H.265 参数 → 本地压缩。实测 32MB → 13.5MB，缩小 58% 无画质损失。

### One-Click PPT Generator
将脚本或大纲 → Jobs 风格极简 HTML 演示文稿（支持幻灯片切换、代码高亮、动画）。
所需技能：ppt-generator

### End-to-End Automated Video Production
调研 → 脚本 → TTS 配音 → 图片搜索 → ffmpeg 剪辑 → 上传 Bilibili。单次会话 200+ 工具调用。
所需技能：bilibili-hub, doubao-tts, ffmpeg

### TikTok Song → YouTube Music Playlist
截图抖音评论中带歌曲名的部分 → OCR 识别 → 批量添加到 YouTube Music 歌单。
所需技能：ytmusic-hub

### Spotify Voice Control
一句话搜索歌曲、切歌、控制 Spotify 播放。
所需技能：spotify-hub

### Read Article Then Auto-Generate Audio
总结文章后自动生成对应配音版本 → 自动播放。
所需技能：doubao-tts

### Local Lightweight TTS on Old iPhone
通过 Minis shell 安装 edge-tts → 免费离线 TTS。64GB iPhone 8 Plus 也能流畅运行。

### AI Personal Color Analysis
上传自拍 → Minis 判断 12 季型色彩 → 生成专业诊断报告（穿搭、美妆、发型、配饰建议）。
所需技能：personal-color-analysis

---

## 💰 金融与追踪

### Photo a Receipt → Auto-Log Expense
拍收据照片 → Apple Vision OCR 提取商家/金额/商品 → 自动分类记账。

### Stock Technical Analysis with Charts
输入股票代码 → 抓取富途/Yahoo Finance/TradingView 数据 → 生成 K 线 + MACD + RSI 图表 + 技术分析报告。

---

## 🛠 开发者工具

### Rescue a Crashed OpenClaw via SSH
OpenClaw 更新后崩溃？从 iPhone SSH 进入 → 自动诊断并重启服务。无需笔记本电脑。

### Remote Dev & Architecture Diagram Generation
SSH 远程服务器 → 扫描 Swift 源码 → 提取三层架构 → 通过 Nano Banana 生成架构图。2 分钟零干预。
所需技能：nano-banana（图像生成）

### Managing Oracle Free-Tier Servers
自然语言管理多台 Oracle 免费服务器：检查磁盘、内存、服务状态、运行命令。