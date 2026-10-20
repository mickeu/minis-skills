# BG5CGQ 笔画方案 v8.1 —— 空格连续联想上屏（讯飞式连打）

## 功能
上屏一个字/词后，predictor 注入联想候选；连续按空格依次上屏联想候选，
实现「我 → 的 → 人」这样基于上文的连打成句，不再需要逐字输入编码。

## 实现
增强 `lua/predict_space.lua`：
- 空格键在「非输入状态 + 有联想候选」时，用 **正常确认流程**
  `confirm_current_selection()` + `commit()` 上屏当前联想候选；
- 这触发 commit_notifier（写 commit_history + 上屏 + 清空）与 update_notifier，
  让 librime-predict 基于最新上屏词注入下一个联想候选，形成连打。
- 正常笔画输入（有编码）时空格仍走原生 confirm，不干扰。

## 关键技术依据（librime-predict 源码）
- predictor 监听 context 的 `update_notifier`：composition 为空 + commit_history 有记录 +
  prediction 开关开 时，基于最近一次 commit 文本生成联想候选。
- `engine:commit_text` 会把 commit_history 记为 `"raw"` 类型，predictor 看到 raw 会**清空预测**
  （predict_engine_->Clear()），导致联想不更新、候选卡在第一个 → 不能用它上屏。
- 必须走 `Context::Commit()`（触发 commit_notifier，写入正常类型 + Clear 触发 update_notifier），
  联想才会更新。librime-lua 中对应 `ctx:commit()`，配合 `ctx:confirm_current_selection()` 选中候选。

## 文件
- `lua/predict_space.lua`（覆盖原文件）
- `stroke_bg5cgq_learning.schema.yaml`（v8.1，无需新增引用，predict_space 原已注册）

## 安装
1. 用 `lua/predict_space.lua` 覆盖方案目录 lua/ 下的同名文件
2. 用 `stroke_bg5cgq_learning.schema.yaml` 覆盖原文件
3. 元书 → 重新部署

## 备注
- 联想依赖 predict.db 有对应的词对联想数据，以及 `prediction` 开关开启。
- 候选耗尽后空格恢复默认行为。
