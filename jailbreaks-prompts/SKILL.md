# Jailbreak 提示词合集

针对前沿 / 开源权重 / 免费潜行模型的系统提示词、persona 锁定、workspace 策略、AGENTS.md 与 Ollama Modelfile 合集。所有文件完整可粘贴，无摘要。

## 用途

- 研究 LLM 指令层级、persona 框架、提示冲突与策略覆盖如何影响模型行为
- 学习如何防御 prompt 注入与指令操纵
- 在自用客户端 / API / 编码代理（如 OpenCode）中应用特定模型的 persona 与操作规范

## 内容索引

### OpenCode Zen 免费潜行模型
| 模型 | 文件 | 类型 |
|---|---|---|
| Big Pickle | `BigPickle-opencode.md` | VANTA persona 锁定 + 显式操作下限 |
| Space Bunny | `spacebunny-agents.md` | 助手操作规范 |
| LongCat 2.5 | `longcat-agents.md` | 助手操作规范 |
| MiMo V2.6 | `mimo-2.6-agents.md` | 助手操作规范 |
| Step 5 Preview | `Step-5-preview.md` | workspace 操作档案 |
| Muse Spark 1.3 | `Muse spark 1.3.md` / `Muse-spark-1-3-v2.md` | Agent 部署操作策略 / 运行时范围注记变体 |
| Muse.ai | `muse-ai-AGENTS.md` | 助手操作规范 |
| 其他未列入 README 表格 | `Beam.md`、`Muse-wonder.md`、`Unified.md` | 通用/潜行 persona |

### Anthropic — Claude
| 模型 | 文件 |
|---|---|
| Opus | `opus v1.md` / `opus v2.md` |
| Sonnet | `sonnet v1.md` / `Sonnet v2.md` |

### Zhipu — GLM / ZCode
| 模型 | 文件 |
|---|---|
| GLM-5.2 | `glm-5.2.md` |
| GLM ZCode 5.2 | `glm-zcode-5.2.md` |
| GLM ZCode 5.3 | `glm-zcode-5.3.md` + `glm-zcode-5.3-AGENTS.md` |
| GLM-5.3 Flash | `glm-5-3-flash.md` |
| GLM-5.3 (OpenCode) | `glm5-3opencode.md` |

### DeepSeek
| 模型 | 文件 |
|---|---|
| V3 | `deepseek v3.md` |
| V4 | `deepseek v4.md` |
| 4.1 | `deepseek-4-1.md` |

### Moonshot — Kimi
| 模型 | 文件 |
|---|---|
| K2 | `kimi-k2.md` |
| K3 | `kimi-k3-agents.md` |
| K3.1 | `kimik3.1.md` |

### xAI — Grok
| 模型 | 文件 |
|---|---|
| Grok Build | `Grok build.md` |
| Grok 4.7 | `grok-4.7.md` |
| Grok Config | `grok-config.txt`（`<CFG>` 优先级与路由配置） |

### NVIDIA / Google / Mistral / Alibaba
| 模型 | 文件 |
|---|---|
| Nemotron 3 Ultra 550B A55B | `nemotron-3-ultra.md` |
| Gemini 4 Argon | `Gemini-4-Argon.md` |
| Mistral Large 4 | `Mistral-Large-4.md` |
| Qwen 3.7 / 3.8 | `qwen-3.7.md` / `qwen-3.8.md` |
| Qwen preferences | `qwen-preferences.md` |

### Ollama Modelfiles
| 模型 | 文件 |
|---|---|
| Gemma 4 | `gemma4.md`（`FROM` + `SYSTEM`） |
| GPT-OSS 20B | `gpt-oss-20b.md`（`FROM` + `SYSTEM`） |

## 使用方式

- **系统提示词**：将对应文件内容粘贴到客户端的 system-prompt / 自定义指令 / API `system` message。
- **AGENTS.md**：以 `AGENTS.md` 保存到仓库/工作区根目录，供编码代理读取。
- **workspace 策略**：放入支持持久全局指令的环境，如 `~/.config/opencode/AGENTS.md`。
- **Ollama Modelfile**：`ollama create <name> -f gemma4.md`。
- **Grok 配置**：放入目标 harness 的配置字段，而非逐轮对话。

> [!NOTE]
> 提示行为高度依赖版本。模型更新、指令层级变化后，旧 prompt 可能失效。失效时以仓库上游最新版为准。

## 维护

- 上游仓库：https://github.com/togg53192-cmd/jailbreaks
- 更新：`git -C <repo> pull` 后覆盖 `prompts/` 下文件并重新校验。
- 敏感内容：本技能仅存本地技能库与 config-backup 私库，**不推送公开 minis-skills**。

## 参考资料（来源）

- 原始仓库：https://github.com/togg53192-cmd/jailbreaks （togg53192-cmd，MIT 未声明，README 标注 research/educational）
- 收录日期：2026-10-30，克隆自 main 分支（commit 以 git log 为准）
- 收录时文件数：38 个 md/txt，总计约 547KB