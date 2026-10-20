-- 空格连续上屏（联想空格）
-- 上屏一个字/词后，候选区会出现联想候选；此时按空格直接上屏第一个联想候选，
-- 实现讯飞式的「连打不中断」。
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
      ctx:commit_text(cand.text)
    end
    return 1  -- kAccepted：空格被消费，用于联想上屏
  end

  return 2
end

return M