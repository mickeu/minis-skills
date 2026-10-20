-- 空格连续上屏（联想连打）
-- 上屏一个字/词后，predictor 注入联想候选；此时按空格直接上屏第一个联想候选，
-- 用正常确认流程（confirm_current_selection + commit）触发 commit_notifier / select_notifier，
-- predictor 基于最新 commit_history 继续注入下一个联想候选，实现讯飞式「我 → 的 → 人」连打。
-- 只在「非输入状态 + 有候选」时生效；正常笔画输入时空格仍走原生 confirm。

local M = {}

function M.func(key_event, env)
  if key_event.keycode ~= 0x20 then return 2 end  -- kNoop：不是空格
  local ctx = env.engine and env.engine.context
  if not ctx then return 2 end

  local composing = ctx:is_composing()
  local ok_input, input = pcall(function() return ctx:get_input() end)
  if not ok_input then input = '' end
  if (not composing or input == '') and ctx:has_menu() then
    local cand = ctx:get_selected_candidate()
    if cand and cand.text and cand.text ~= '' then
      -- 正常确认流程：先选中当前高亮候选，再 commit
      -- （触发 commit_notifier 写入 commit_history + 上屏 + 清空，
      --   清空触发 update_notifier，predictor 基于最新 commit_history 注入下一个联想候选）
      if ctx.confirm_current_selection then
        pcall(function() ctx:confirm_current_selection() end)
      end
      if ctx.commit then
        pcall(function() ctx:commit() end)
      end
    end
    return 1  -- kAccepted：空格被消费，用于联想上屏
  end

  return 2
end

return M