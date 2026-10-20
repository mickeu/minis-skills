-- 空格连续上屏（联想连打）
-- 上屏一个字/词后，predictor 注入联想候选；编码为空（联想阶段）时按空格，
-- 直接上屏第一个联想候选（与设备原版 predict_space 行为一致，用 commit_text 上屏文本）。
-- 有笔画编码（正常输入）时：先清除 composition 中残留的 prediction 段，
-- 避免正常确认把系统预测联想词一起上屏（如「你+的」「我+的」），再放行原生 confirm。
-- 不做任何 _auto_commit / 候选区干预，保证次选三选等正常显示。

local M = {}

-- 删除 composition 中最后一个 prediction 段（不影响笔画输入段）
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

  -- 有笔画编码（正在输入）：清除残留预测段，放行原生 confirm
  if input ~= '' then
    clear_prediction(ctx)
    return 2
  end

  -- 编码为空（联想阶段）+ 有候选：上屏第一个联想候选（原版行为）
  if not ctx:has_menu() then return 2 end
  local cand = ctx:get_selected_candidate()
  if cand and cand.text and cand.text ~= '' then
    -- 用 commit_text 直接上屏候选文本（不触发 commit_notifier，不污染候选区）
    if ctx.commit_text then
      pcall(function() ctx:commit_text(cand.text) end)
    elseif env.engine.commit_text then
      pcall(function() env.engine:commit_text(cand.text) end)
    end
  end
  return 1  -- kAccepted：空格被消费，用于联想上屏
end

return M