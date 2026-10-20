# BG5CGQ 笔画方案 v8.1 —— 空格连续上屏补丁（设备增强版）

## 功能
输入编码后，候选区不再「上屏即消失」，**连续按空格可依次上屏候选区第一个字/词**：

- 第 1 次空格：上屏候选 1
- 第 2 次空格：候选区自动前移，上屏新的候选 1（原候选 2）
- 依此类推，直到候选全部上屏完，自动清空编码进入联想阶段
- 联想候选出现后，原有 `predict_space` 接管空格连打（讯飞式连打不中断）

示例：候选依次为「我 / 我们 / 你 / 你们」，连按 4 次空格即可整串上屏。

## 与设备现有 predict_space 的分工
设备增强版已内置 `lua/predict_space.lua`（处理**编码为空**时空格连打联想候选）。
本补丁新增 `space_commit`（处理**编码非空**时候选区连续上屏）。两者条件互斥、互补：
- 有编码 → `space_commit` 连续上屏当前候选
- 编码空 → `predict_space` 连打联想候选

## 新增/修改文件（共 4 个）
| 文件 | 说明 |
|---|---|
| `lua/space_commit.lua` | 核心：共享「已上屏」状态 + processor/filter 逻辑 + 学习补偿 |
| `lua/space_commit_processor.lua` | processor 入口（schema 新增引用） |
| `lua/space_commit_filter.lua` | filter 入口（schema 新增引用） |
| `stroke_bg5cgq_learning.schema.yaml` | 覆盖原文件（version 8.1，注册新 processor/filter） |

## 安装
1. 元书 → 文件管理，进入 BG5CGQ 方案目录（`.../BG5CGQ-WanXiang-Rime/`）
2. 把 `lua/space_commit*.lua` 3 个文件放入方案目录的 `lua/` 文件夹
3. 用本包 `stroke_bg5cgq_learning.schema.yaml` 覆盖原文件
4. 元书 → 重新部署

## 原理
- 新增 `lua_processor`（在 `predict_space` 之后）拦截空格：用 `engine:commit_text(候选)` 上屏——该方法**不清空编码**；随后 `context:set_input(原编码)` 强制重建候选；
- 新增 `lua_filter`（在 `uniquifier` 之前）把已上屏候选从候选流剔除，剩余候选自动前移，空格下一次仍上屏「第一个」；
- 候选全部上屏完后自动 `set_input('')` 清空编码，交回 `predict_space` 连打联想；
- 编码变化（增删笔画、翻页、切换候选）自动重置连续状态。

## 学习补偿（重要）
`engine:commit_text` 不触发 Rime 的 `commit_notifier`，因此连续上屏的词**默认不会**进入自学习/造词。
本补丁在 processor 内手动调用 `learning.add` / `learning.learn_word` / `learning.set_last_commit`，
使连续上屏的词同样进入调频、组合造词和「上次上屏词」上下文联想，与正常上屏行为对齐。

## 测试
- 语法：`luac5.4 -p` 全部通过
- 逻辑 mock（含学习补偿）：候选池 `[我, 我们, 你, 你们]`
  - 连续 4 次空格依次上屏 我 → 我们 → 你 → 你们 ✅
  - `learning.add` 记录 4 次、组合造词 3 次 ✅
  - 候选耗尽后自动清空编码、空格交回默认/联想处理 ✅

## 备注
- 空格键在「有候选且未耗尽」期间专用于连续上屏；候选耗尽清空编码后，空格恢复正常/联想连打。
- 真机部署前请先备份原 `stroke_bg5cgq_learning.schema.yaml` 和 `lua/` 目录。