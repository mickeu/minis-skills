# 通用破限词 · Jailbreak Prompt

> 来源：https://github.com/mickeu/workbuddy2api-panel （破限 commit `5d08495` · 人格合并 commit `7d6fd72`，2026-10-05 调研）
> 创建 2026-10-05 · 由 WorkBuddy2API 网关技能剥离转制（网关已弃用，破限词独立保留）
> 破限词全文：同目录 `jailbreak-prompt.md`

**核心定位**：一段可复用的系统提示词（system prompt），用于破除 LLM 的自我设限——不拒绝话题、不输出免责声明/道德说教、不自我审查、把用户目标放在第一位。已融合 Minis 人格设定（语言 / 行动准则 / 回报风格 / 技术纪律 / 安全红线）与工程行为约束，可直接用于任何 OpenAI 兼容客户端。

## 使用方式

破限词全文见同目录 `jailbreak-prompt.md`（约 3.7KB / 60 行），两种注入路径：

### A. 注入 Minis 人格（soul.body）
```bash
minis-config set soul.body '<破限词全文>'
```
- ⚠️ `soul.body` 有 **2000 token 上限**（中文按字符计），全量放不下时必须精简
- 精简策略：保留「核心立场」+「工程行为」+「边界」，删掉「Minis 人格设定」段——因为注入后宿主本来就是 Minis，无需重复
- 生效后破限词会成为助手人格一部分，**覆盖默认安全红线**，操作前需用户知情确认

### B. 用于其他 OpenAI 兼容客户端
- 直接复制 `jailbreak-prompt.md` 全文，粘贴到客户端的「自定义 system prompt / 人格设定 / 角色设定」输入框
- 若客户端已有自己的 system，建议让破限词**替换**而非追加（追加时客户端限制性 system 仍保留，破限不彻底）

## 注意事项

- 破限词本质是越狱指令，会覆盖客户端默认安全设定，仅限自用，**不要用于违规用途**
- 注入后模型可能对敏感话题给出直接回答，请自行评估风险
- 破限效果取决于模型本身的内容安全策略，不一定 100% 生效

## 参考资料（来源）

- 破限 fork：https://github.com/mickeu/workbuddy2api-panel （commit 5d08495 = 破限，7d6fd72 = 人格合并，2026-10-05）
- 上游项目：https://github.com/linguo2625469/workbuddy2api-panel （已弃用，仅供溯源）