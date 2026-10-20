-- 空格连续上屏（联想连打）
-- 上屏一个字/词后，predictor 注入联想候选；此时按空格直接上屏第一个联想候选，
-- 用正常确认流程（confirm_current_selection + commit）触发 commit_notifier / select_notifier，
-- predictor 基于最新 commit_history 继续注入下一个联想候选，实现讯飞式「我 → 的 → 人」连打。
-- 有笔画编码（正常输入）时：任何按键都先清除 composition 中残留的 prediction 段，
-- 确保正常确认绝不上屏联想词（避免「你+的」「我+的」一起上屏），再放行原生处理。
-- 只在「编码为空（纯联想阶段）+ 空格 + 有候选」时执行联想连打。

local M = {}

-- 判断并删除 composition 中残留的 prediction 段（不影响笔画输入段）
local function clear_prediction(ctx)
  local comp = ctx.composition
  if not comp or not comp.back then return end
  local ok, seg = pcall(function() return comp:back() end)
  if not ok or not seg then return end

  local is_pred = false
  -- 1) 通过 has_tag('prediction')
  if not is_pred and seg.has_tag then
    local ok2, v = pcall(function() return seg:has_tag('prediction') end)
    if ok2 and v then is_pred = true end
  end
  -- 2) 通过 tags 表（prediction/predict/placeholder）
  if not is_pred and seg.tags and type(seg.tags) == 'table' then
    for _, t in ipairs(seg.tags) do
      if t == 'prediction' or t == 'predict' or t == 'placeholder' then
        is_pred = true break
      end
    end
  end
  -- 3) 空段特征（start == end）：正常笔画输入段必有编码（start < end），
  --    空段只可能是预测占位段
  if not is_pred then
    local s, e = seg.start, seg._end
    if s and e and s == e then is_pred = true end
  end

  if is_pred and comp.pop_back then
    pcall(function() comp:pop_back() end)
  end
end

function M.func(key_event, env)
  if key_event.keycode ~= 0x20 then return 2 end  -- kNoop：不是空格
  local ctx = env.engine and env.engine.context
  if not ctx then return 2 end

  local ok_input, input = pcall(function() return ctx:get_input() end)
  if not ok_input then input = '' end

  -- 有笔画编码（正在输入）：任何按键都先清除残留预测段，再放行原生处理
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