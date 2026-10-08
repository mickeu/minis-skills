# LUNO｜Minis 客户端配置

**加载边界**：本文是 `luno-minis` 的专项资源，公共前提与路由见入口；其中操作只在 Minis 端可用。

## 配置接口
- `minis-config` 覆盖设置与部分配置读写（`get`/`set`/`set-batch`），写入触发 App 内确认并记入可回滚审计（Logs → Config Changes）；数组字段用 `--filter`/分页查询，必要时才整体列举。
- 技能与子代理的 App 页面与 CLI 等效，按用户便利选择；改完以回读为准。
- `set-batch` 的 `value_json` 必须是 JSON **文本**（多一层编码）；批量中任一项失败会整批 `partial_write_failed`，**同批已成功项也可能未落盘**——失败后先逐项回读确认差异，只重写缺失项。
- 环境变量经 App 设置页维护；引用按变量名，缺失即说明并给创建入口，不换来源。凭据类只读存在性与长度，取值不经对话。

## 子代理与模型
- 子代理条目在 App UI 配置；新增必须走 App UI，`minis-config` 不能新增。内置通用子代理位于 `subagents.general.instructions`（roster 显示为 `builtin.general`）。
- **平台技术能力**（2026-09 实测，App 版本未记录；历史观测，**非永久限制**）：子代理模板不注入常驻，可读写文件，无记忆工具、不能再派发/向用户确认。**现行集中路由政策**（有意选择，不随观测是否成立改变）：关键写入的授权核对/决策责任、用户确认归主助理，执行可派执行角色；专职仅回传、不互派，审查子代理只读。派发后核实际角色/模型组：2026-09 实测中断后自动 resume 可能换主体（如 LENS→通用兜底）/模型组；`minis-sessions-cli status --id <child_session_id>` 回读实际执行者/模型，缺元数据标「通道身份未验证」。
- 分组 `contextLimitTokens` 决定生效窗口，**分组优先于模型条目**的 `contextWindowOverride`/`contextWindowTokens`；关掉「Limit Context Window」回落到条目值，再打开后**须回读当前分组的生效值**，不以历史观测代替（2026-09 曾观测到 1000000，仅作历史记录、非固定默认）。
- `minis-config get models.<provider>/<model_id>.<field>` 中，含点号的 model_id 无需转义、可直接读取。
- 模型不可用时按分组解析结果与报错判断，区分「配置已保存」「分组已绑定」「调用实际成功」。

## SOUL 与提示词
- 写入：`minis-config set soul.body --file <json>`，文件内容必须是 **JSON 字符串**（`json.dumps(body, ensure_ascii=False)`），不是裸文本。
- 改写 `SOUL.md` 须保留 frontmatter，正文按 `body_contract.body_bytes` 提取；重组不额外追加 LF。文件正文、`soul.body` 与仓库正文按 UTF-8 bytes 判等，禁 strip/换行归一。

## 目录与持久化（记忆与真源）
- **记忆**：`memory_write` 写入 `/var/minis/memory/YYYY-MM-DD.md`；需每轮注入的偏好/约定可放入 `GLOBAL.md`——默认只读、由用户维护，AI 仅按用户明示修改，只承载本端约定、不作跨端真源。本端记忆仅在本端维护，不与 LobeHub 同步；**跨端共享的规则与技能以 Minis 侧为真源**——技能正文 `/var/minis/skills/<name>/SKILL.md`、常驻提示词 `soul.body`（文件视图 `SOUL.md`）。记忆有误即更正或删除（判据、授权与诚实边界见 `luno-memory`）；自动注入窗口与容量诊断按需读取入口〈资源与触发〉中列出的记忆注入资源，本文不复述。
- **条目格式体检**：`memory-tools/verify-memory-format.py`（只读；按**条目**判定条目数、关键词行、时间戳、词数与字节预算；退出码 1＝有硬失败）。写入或整理记忆后跑一次，用于发现漏项；`--strict-terms` 是**回补专用**严格档（要求词在正文原样出现，比规则严，勿用于判断既有条目）。它是事后查漏工具，**不是写入强制入口**，不得据此宣称格式已强制。
- **条目压缩门禁**：`memory-tools/entry-guard.py`（只读）——压缩某条记忆前后，用 `--old <压缩前副本> --new <当前文件>` 逐条比对**可检索标识是否丢失**（哈希/提交号/job id/`skl_*`/路径/文件名/容量/常量名），并检查条目数与关键词行。硬失败非 0 即不得宣称压缩无损。**子代理自述不代替父级运行该脚本复核。**

