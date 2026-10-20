-- predict_space.lua 逻辑测试（mock librime-lua 环境）
package.path = '/var/minis/workspace/BG5CGQ-WanXiang-Rime-v8.1/lua/?.lua;' .. package.path
local ps = require('predict_space')

local function make_seg(opts)
  local tags = {}
  if opts.tags then
    for _, t in ipairs(opts.tags) do tags[t] = true end
  end
  return {
    has_tag = function(_, tag) return tags[tag] == true end,
    tags = opts.tag_list,
    start = opts.start,
    _end = opts.end_,
  }
end

local function make_ctx(opts)
  local segs = opts.segs or {}
  local ctx = {
    _input = opts.input,
    _menu = opts.has_menu,
    _cand = opts.cand,
    _confirm = 0,
    _commit = 0,
    composition = {
      back = function() return segs[#segs] end,
      pop_back = function() table.remove(segs, #segs) end,
      segs = segs,
    },
  }
  function ctx:get_input() return self._input end
  function ctx:has_menu() return self._menu end
  function ctx:get_selected_candidate() return self._cand end
  function ctx:confirm_current_selection() self._confirm = self._confirm + 1 return true end
  function ctx:commit() self._commit = self._commit + 1 return true end
  return ctx
end

local key_space = { keycode = 0x20 }
local function run(ctx)
  return ps.func(key_space, { engine = { context = ctx } })
end

local pass = 0
local fail = 0
local function check(name, cond)
  if cond then pass = pass + 1 print('✅ ' .. name)
  else fail = fail + 1 print('❌ ' .. name) end
end

-- 用例1：input 非空 + 预测段 has_tag('prediction') → 应清除预测段并返回2
local ctx1 = make_ctx({
  input = '3121', has_menu = true,
  segs = {
    make_seg({ start = 0, end_ = 4, tags = {} }),
    make_seg({ start = 0, end_ = 0, tags = {'prediction'}, tag_list = {'prediction','placeholder'} }),
  },
})
local r1 = run(ctx1)
check('用例1 返回2（放行原生）', r1 == 2)
check('用例1 预测段已清除', #ctx1.composition.segs == 1)

-- 用例2：input 非空 + 空段（start==end，无 prediction tag）→ 也应清除
local ctx2 = make_ctx({
  input = '3121', has_menu = true,
  segs = {
    make_seg({ start = 0, end_ = 4, tags = {} }),
    make_seg({ start = 0, end_ = 0, tags = {}, tag_list = {} }),
  },
})
local r2 = run(ctx2)
check('用例2 返回2', r2 == 2)
check('用例2 空段已清除', #ctx2.composition.segs == 1)

-- 用例3：input 非空 + 无预测段 → 不动段，返回2
local ctx3 = make_ctx({
  input = '3121', has_menu = true,
  segs = { make_seg({ start = 0, end_ = 4, tags = {} }) },
})
local r3 = run(ctx3)
check('用例3 返回2', r3 == 2)
check('用例3 正常段保留', #ctx3.composition.segs == 1)

-- 用例4：input 空 + 有候选（联想阶段）→ 调用 confirm+commit，返回1
local ctx4 = make_ctx({
  input = '', has_menu = true, cand = { text = '的' },
  segs = { make_seg({ start = 0, end_ = 0, tags = {'prediction'}, tag_list = {'prediction'} }) },
})
local r4 = run(ctx4)
check('用例4 返回1（联想上屏）', r1 ~= nil and r4 == 1)
check('用例4 confirm 被调用', ctx4._confirm == 1)
check('用例4 commit 被调用', ctx4._commit == 1)

-- 用例5：input 空 + 无候选 → 返回2
local ctx5 = make_ctx({ input = '', has_menu = false, segs = {} })
local r5 = run(ctx5)
check('用例5 返回2', r5 == 2)

-- 用例6：非空格键 → 返回2
local r6 = ps.func({ keycode = 0x61 }, { engine = { context = ctx1 } })
check('用例6 非空格返回2', r6 == 2)

print(string.format('\n结果: %d 通过, %d 失败', pass, fail))
if fail == 0 then print('✅ 全部通过') else print('❌ 有失败') end