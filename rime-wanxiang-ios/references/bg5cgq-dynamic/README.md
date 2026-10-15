# BG5CGQ 动态学习版源码快照（主开发核心）

本目录是 BG5CGQ 笔画输入法「动态学习版」主开发核心的可运行源码备份。

## 来源
- 主开发会话：`BE297AE8-293E-49FD-9B7D-D01A2F540524`「对比Rime配置排查导入空白」（2048 条消息，覆盖 v6.x~v7.9 全部开发过程）
- 备份时间：2026-10-16
- 触发原因：主开发核心会话删除前，确认核心经验已入技能库（SKILL.md 第九章 + `bg5-staged-compose.md`），但可运行源码此前仅散落在 /tmp 临时目录，需持久归档。

## 版本沿革（重要）
- **v7.6**：主开发过程版本，9 个 Lua（无计算器）。
- **v8.0**：计算器独立方案（`bg5cgq_calc`）——**已废弃回退**（会跨方案外泄），交付后即被「关死」清理，勿使用。
- **v7.9（最终版，本目录 v7.9/）**：计算器**内嵌主方案**，前缀 `V` 触发，不切方案。含完整计算器 Lua（`wanxiang_super_calculator.lua` / `calculator.lua` / `bg5_math.lua` / `bg5_calc_*.lua`）。这是用户当前使用的版本。

## 目录结构
```
bg5cgq-dynamic/
├── README.md
├── tests/                 # 回归测试脚本（test_digit_final / test_bg5_full_fixed）
├── v7.6/                  # 历史版本（9 Lua，无计算器）
│   ├── default.custom.yaml
│   ├── hamster.yaml
│   ├── predict.db         # 7.5M，本地保留，不上传 GitHub
│   ├── stroke_bg5cgq.dict.yaml
│   ├── stroke_bg5cgq_learning.schema.yaml
│   └── lua/
└── v7.9/                  # 最终版（15 Lua，含内嵌计算器）
    ├── default.custom.yaml
    ├── hamster.yaml
    ├── predict.db         # 7.5M，本地保留，不上传 GitHub
    ├── stroke_bg5cgq.dict.yaml
    ├── stroke_bg5cgq_learning.schema.yaml
    └── lua/
```

## GitHub 上传说明
按 GLOBAL.md 规则，>2MB 的大数据文件**不上传 GitHub**，仅存本地技能库：
- `lua/words.lua`（7.6M，词库数据）
- `lua/phrase_stroke_index.lua`（3.4M，词组索引数据）
- `predict.db`（7.5M，预测模型）

需要完整数据时，从本地技能库 `/var/minis/skills/rime-wanxiang-ios/references/bg5cgq-dynamic/` 取。

## 相关经验文档
- `rime-wanxiang-ios/SKILL.md` 第九章「BG5CGQ 动态分段造词：真机成功基线」
- `rime-wanxiang-ios/references/bg5-staged-compose.md`（三个核心修复 + 验收命令 + 性能纪律）
- 每日记忆 2026-10-12 ~ 2026-10-15（各版本关键改动、索引架构、SHA256、验收结论）