# Minis 技能开发指南

来源：https://github.com/openminis/MinisSkills

## 什么是技能？

技能是包含 SKILL.md 文件的目录，是复用指令集，扩展 AI 智能体的专业工作流、领域知识和捆绑资源。

## 三级加载系统

1. **元数据（Frontmatter）**：name + description → 始终在上下文中，用于触发
2. **SKILL.md 正文**：触发时加载到上下文（建议 < 500 行）
3. **捆绑资源**：按需加载（scripts/、references/、assets/），无大小限制

## 目录结构规范

```
MinisSkills/
├── README.md
└── <skill-name>/          # 每个技能一个目录
    ├── SKILL.md           # 必需
    ├── evals/
    │   └── evals.json     # 可选：测试用例
    ├── scripts/           # 可选：可执行脚本
    ├── references/        # 可选：参考文档
    └── assets/            # 可选：模板、图标、字体
```

## 命名规则

- 使用 lowercase-kebab-case：`my-skill-name`
- 2-4 个单词最佳
- 可用领域/动作为前缀便于分组
- ✅ 正确：`health-sleep-analysis`, `nano-banana`, `twitter-x-hub`
- ❌ 错误：`MySkill`, `skill_for_doing_things`, `s1`

## SKILL.md 格式

### 必需 Frontmatter
```yaml
---
name: skill-name
description: >
  一句话描述技能功能及触发条件。包含具体用户短语、上下文和关键词。
  可以"激进"一点：列出边缘情况和近似场景，确保技能能被正确触发。
---
```

### 可选 Frontmatter
```yaml
---
name: skill-name
description: ...
compatibility: Python 3.10+, requires ffmpeg
---
```

### 正文编写指南
- 使用祈使句："获取文件"、"解析 JSON"、"返回表格"
- 解释"为什么"——Claude 理解推理后可更灵活应用
- ALWAYS/NEVER 少用，用推理替代硬性规则
- 目标 < 500 行；超出时拆分到 references/
- 输出格式固定时使用模板块

### 多领域技能
当技能覆盖多个框架/平台时，SKILL.md 保持精简，委托给 reference 文件：
```
cloud-deploy/
├── SKILL.md
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

### 渐进式披露模式
- SKILL.md：概览、决策逻辑、指向子参考
- references/<topic>.md：深度细节，按需加载
- scripts/<task>.py：直接执行，不加载到上下文

## 评估（Evals）
```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "真实的用户输入",
      "expected_output": "正确结果的描述",
      "files": [],
      "assertions": [
        {"text": "输出包含有效 JSON", "type": "contains"}
      ]
    }
  ]
}
```

## 提交检查清单
- [ ] 目录名是 lowercase-kebab-case
- [ ] SKILL.md 存在且含有效 YAML frontmatter（name + description）
- [ ] description 清楚说明功能和触发条件
- [ ] 正文 < 500 行（或使用 references/ 分流）
- [ ] 使用祈使句，解释关键步骤的"为什么"
- [ ] 无硬编码密钥或凭证
- [ ] 脚本在 scripts/，参考在 references/，静态资源在 assets/
- [ ] 如有 evals，遵循上述 schema