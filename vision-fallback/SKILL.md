# vision-fallback — 视觉兜底链

## 触发条件

用户发送图片、要求看图、OCR、截图分析、图片理解等任何视觉任务时，**直接调用本技能，无需用户指定引擎**。

## 核心脚本

`/var/minis/skills/vision-fallback/scripts/vision-read.sh`

```
用法：vision-read.sh <图片路径> [问题]
FORCE_ENGINE=sensenova1|sensenova2|gemini 可强制指定引擎（测试用）
```

## 降级顺序（自动）

1. **日日新1·sensenova-6.8-flash-lite**（看图主力 key1）
2. **日日新2·sensenova-6.8-flash-lite**（key2，轮询/限流切换）
3. **Gemini 3.1 Flash Lite**（免费备用，实测可用）
4. **apple-vision OCR**（本地兜底，无需网络/key，只出文本不出语义）

失败判定：调用超时 60s、`ok:false`、输出空、报 429/配额错误 → 自动切换下一个引擎，`[vision-read]` 日志标注实际命中的引擎。

## 实测记录（2026-08-17）

- 默认链路：6.8 key1 命中，形状/颜色/文字识别正确
- Gemini 路径：FORCE_ENGINE=gemini 命中，识别正确（椭圆细节偶有误差）
- OCR 兜底：FORCE_ENGINE=bad 触发，输出 JSON 文本块（位图字体小字识别率一般，截图类清晰文字没问题）

## 注意

- 图片路径：/var/minis/attachments/ 下的附件、/tmp 生成的测试图均可
- 输出格式：引擎行 `[vision-read] 引擎=xxx` 后跟识别文本；OCR 兜底输出 JSON
- 依赖 minis-model-use（三日日新/Gemini 配置）+ apple-vision（本地框架）