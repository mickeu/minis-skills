-- 空格连续上屏（联想连打）
-- 上屏一个字/词后，predictor 注入联想候选；此时按空格直接上屏第一个联想候选，
-- 用正常确认流程（confirm_current_selection + commit）触发 commit_notifier / select_notifier，
-- predictor 基于最新 commit_history 继续注入下一个联想候选，实现讯飞式「我 → 的 → 人」连打。
-- 有笔画编码（正常输入）时：先清除 composition 中残留的 prediction 段，
-- 避免正常确认把联想词一起上屏（如「你+的」），再放行原生 confirm。
-- 只在「编码为空（纯联想阶段）+ 有候选」时执行联想连打。

local M = {}

-- 删除 composition 中最后一个 prediction 段（不影响笔画输入段）
local function clear_prediction(ctx)
  local comp = ctx.composition
  if not comp or not comp.back then return end
  local ok, seg = pcall(function() return comp:back() end)
  if not ok or not seg then return end
  if seg.has_tag then
    local ok2, is_pred = pcall(function() return seg:has_tag('prediction') end)
    if ok2 and is_pred and comp.pop_back then
      pcall(function() comp:pop_back() end)
    end
  end
end

function M.func(key_event, env)
  if key_event.keycode ~= 0x20 then return 2 end  -- kNoop：不是空格
  local ctx = env.engine and env.engine.context
  if not ctx then return 2 end

  local ok_input, input = pcall(function() return ctx:get_input() end)
  if not ok_input then input = '' end

  -- 有笔画编码（正常输入）：清除残留预测段，放行原生 confirm（只上屏当前字）
  if input ~= '' then
    clear_prediction(ctx)
    return 2
  end

  -- 编码为空（联想阶段）+ 有候选：联想连打
  if not ctx:has_menu() then return 2 end
  local cand = ctx:get_selected_candidate()
  if cand and cand.text and cand.text ~= '' then
    -- 正常确认流程：先选中当前高亮联想候选，再 commit
    if ctx.confirm_current_selection then
      pcall(function() ctx:confirm_current_selection() end)
    end
    if ctx.commit then
      pcall(function() ctx:commit() end)
    end
  end
  return 1  -- kAccepted：空格被消费，用于联想上屏
end

return M