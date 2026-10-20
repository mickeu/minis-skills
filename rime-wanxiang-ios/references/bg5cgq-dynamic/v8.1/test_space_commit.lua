-- 空格连续上屏 逻辑测试 v2（含 learning 补偿 + 候选耗尽清空）
package.path = '/var/minis/workspace/bg5cgq-space-commit/lua/?.lua;' .. package.path

-- mock learning 模块（避免真实读写文件）
local learned_adds = {}
local learned_words = {}
local last_commit_val = nil
local mock_learning = {
  add = function(w) learned_adds[#learned_adds+1] = w end,
  learn_word = function(w) learned_words[#learned_words+1] = w end,
  set_last_commit = function(w) last_commit_val = w end,
}
package.loaded['learning'] = mock_learning

local sc = require('space_commit')

-- 原始候选池
local original = { {text='我'}, {text='我们'}, {text='你'}, {text='你们'} }
local current = {}
for _, c in ipairs(original) do current[#current+1] = {text=c.text} end

local input_str = '3121'
local committed = {}
local cleared = false

local context = {}
function context:get_input() return input_str end
function context:has_menu() return #current > 0 end
function context:get_selected_candidate() return current[1] end
function context:get_menu()
  return { get_candidate_at = function(_, i) return current[i+1] end }
end
function context:set_input(s)
  input_str = s
  if s == '' then cleared = true end
  -- 模拟重建候选
  local out = {}
  local saved_yield = yield
  yield = function(cand) out[#out+1] = {text=cand.text} end
  local input = {
    iter = function()
      local i = 0
      return function() i = i + 1 return original[i] end
    end
  }
  sc.filter(input, { engine = { context = context } })
  yield = saved_yield
  current = out
end

local engine = {}
engine.context = context
function engine:commit_text(t) committed[#committed+1] = t end

local key_event = { keycode = 0x20, repr = function() return 'space' end }
local env = { engine = engine }

print('初始候选:', table.concat((function()
  local t = {} for _, c in ipairs(current) do t[#t+1] = c.text end return t
end)(), ' / '))

for i = 1, 6 do
  local ret = sc.processor(key_event, env)
  local top = current[1] and current[1].text or '(空)'
  print(string.format('第%d次空格 -> 上屏[%s] 剩余候选[%s] 返回值[%d] 输入[%q]',
    i, committed[i] or '(无)', top, ret, input_str))
end

print('=== 上屏序列:', table.concat(committed, ' -> '))
print('=== learning.add 调用:', table.concat(learned_adds, ', '))
print('=== learning.learn_word 调用:', table.concat(learned_words, ', '))
print('=== 候选耗尽后清空编码:', cleared and '是' or '否')

-- 断言
local expect = { '我', '我们', '你', '你们' }
local pass = #committed == 4
for i = 1, 4 do if committed[i] ~= expect[i] then pass = false end end
if #learned_adds ~= 4 then pass = false end
if #learned_words ~= 3 then pass = false end
if not cleared then pass = false end
print(pass and '✅ 测试通过' or '❌ 测试失败')