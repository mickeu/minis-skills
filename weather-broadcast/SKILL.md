---
name: 天气语音播报
description: 天气语音播报。当用户说"天气播报"、"播报天气"、"今天天气"、"天气怎么样"、"早上好"等与天气播报相关的指令时触发。使用 Minis 原生工具（apple-weather、apple-player、apple-speak）获取天气并语音播报，无需任何外部 API Key。
license: MIT
last_sync: 2026-07-26
---
# 天气播报 Skill

## 触发方式
在 Minis 聊天里说 **"天气播报"**、**"播报天气"**、**"今天天气"** 等，AI 直接运行脚本。

自动化：iOS 快捷指令 → 发送提示词"天气播报"给 Minis。

## ⚠️ 核心规则

**直接运行脚本，不要手动拆解步骤替代。** 脚本包含完整流程（农历日期、edge-tts 晓晓合成、BGM 混音），手动 apple-weather + apple-speak 拼凑会丢失体验。脚本超时重试即可，不要改方案。

## 步骤

### 1. 确保依赖
```bash
pip install edge-tts lunardate
```

### 2. 运行播报（唯一方式）
```bash
python3 /var/minis/skills/weather-broadcast/scripts/morning-briefing.py
```

### 脚本流程
1. 定位 → 获取天气数据
2. 生成 6 段口语化文案（问候 → 天气 → 温湿度 → 紫外线 → 降雨 → 收尾）
3. edge-tts 晓晓语音合成（+10% 语速），失败回退 apple-speak
4. BGM 拼接到语音后面（先播天气，再放鸟鸣，BGM 30% 音量）
5. apple-player 播放，播完自动清理临时文件

### 资源
- 脚本：`scripts/morning-briefing.py`
- 背景音乐：`assets/birds.mp3`
- 临时文件：`/var/minis/shared/weather-broadcast/`（播完即删）
