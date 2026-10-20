-- space_commit.lua
-- 空格连续上屏：输入编码后，候选区保留，已上屏候选被剔除并自动前移，
-- 连续按空格即可依次上屏候选区第一个字/词。
-- 与 predict_space.lua 分工：
--   predict_space：编码为空、联想候选出现时，空格连打联想候选；
--   本模块：编码非空、有笔画候选时，空格连续上屏当前候选。
-- 实现：
--   processor 拦截空格 -> 用 engine:commit_text(候选) 上屏（不清空编码），
--     记入 done 表，再用 context:set_input(原编码) 强制重建候选；
--   filter 把 done 中已上屏的候选从候选流剔除，剩余候选前移；
--   候选耗尽时 set_input('') 清空编码，交回 predict_space 连打联想。

local M = {}
local done = {}           -- input 编码 -> { [已上屏文本] = true }
local current_input = ''  -- 当前输入编码，编码变化时清空 done
local prev_commit = nil    -- 连续上屏组合造词的上一词
local learning = nil      -- 懒加载 learning 模块（nil=未加载，false=加载失败）

-- 取候选文本：兼容 .text 字段与 :get_text() 方法
local function cand_text(cand)
  if cand and cand.text and cand.text ~= '' then return cand.text end
  if cand and type(cand.get_text) == 'function' then
    local ok, t = pcall(function() return cand:get_text() end)
    if ok and t and t ~= '' then return t end
  end
  return nil
end

-- 取当前菜单第一个候选：兼容 get_menu()/menu 字段与 get_candidate_at()/candidate_at()
local function first_candidate(context)
  local menu = nil
  if context.get_menu then
    local ok, m = pcall(function() return context:get_menu() end)
    if ok then menu = m end
  end
  if not menu and context.menu then menu = context.menu end
  if not menu then return nil end
  for _, fn in ipairs({ 'get_candidate_at', 'candidate_at' }) do
    local f = menu[fn]
    if type(f) == 'function' then
      local ok, cand = pcall(function() return f(menu, 0) end)
      if ok and cand then return cand end
    end
  end
  return nil
end

-- 取当前输入：兼容 get_input() 方法与 input 字段
local function get_input(context)
  if context.get_input then
    local ok, v = pcall(function() return context:get_input() end)
    if ok and v then return v end
  end
  if context.input then return context.input end
  return ''
end

-- 编码变化时清空已上屏记录
local function sync_input(input)
  if input ~= current_input then
    done = {}
    current_input = input
  end
end

-- 学习补偿：engine:commit_text 不触发 commit_notifier，这里手动补记，
-- 使连续上屏的词也进入调频、组合造词与「上次上屏词」联想。
local function feed_learning(text, env)
  if learning == nil then
    local ok, mod = pcall(require, 'learning')
    learning = ok and mod or false
  end
  if not learning or not learning.add then return end
  pcall(function()
    learning.add(text, env)
    if prev_commit and prev_commit ~= text then
      local combined = prev_commit .. text
      if learning.learn_word then learning.learn_word(combined, env) end
    end
    prev_commit = text
    if learning.set_last_commit then learning.set_last_commit(text) end
  end)
end

function M.processor(key_event, env)
  local context = env.engine and env.engine.context
  if not context then return 2 end

  local input = get_input(context)
  sync_input(input)

  if key_event:repr() ~= 'space' then
    return 2 -- 非空格键，放行给后续处理器
  end

  -- 空输入：编码为空，联想阶段交回 predict_space/默认处理
  if input == '' then
    return 2
  end

  -- 有编码但无候选（候选已全部上屏完）：清空编码回到联想阶段
  if not context:has_menu() then
    done = {}
    if context.set_input then
      pcall(function() context:set_input('') end)
    end
    return 2
  end

  local cand = first_candidate(context)
  local text = cand_text(cand)
  if not text then
    -- 防御：菜单异常为空，同样清空回联想
    done = {}
    if context.set_input then
      pcall(function() context:set_input('') end)
    end
    return 2
  end

  -- 上屏当前第一个候选（engine:commit_text 不清空编码）
  if env.engine.commit_text then
    pcall(function() env.engine:commit_text(text) end)
  end

  -- 记录已上屏，供 filter 剔除
  local set = done[input] or {}
  set[text] = true
  done[input] = set

  -- 学习补偿（失败静默，不影响上屏）
  feed_learning(text, env)

  -- 强制重建候选，让 filter 剔除已上屏项、剩余候选前移
  if context.set_input then
    pcall(function() context:set_input(input) end)
  end

  return 1 -- 吃掉空格
end

function M.filter(input, env)
  local ctx = env.engine and env.engine.context
  local inpt = ctx and get_input(ctx) or ''
  local set = done[inpt]
  if not set then
    -- 无已上屏记录，原样放行
    for cand in input:iter() do yield(cand) end
    return
  end
  for cand in input:iter() do
    local text = cand_text(cand)
    if text and set[text] then
      -- 已上屏候选，剔除
    else
      yield(cand)
    end
  end
end

return M