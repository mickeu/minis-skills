-- pinyin_reverse.lua: 笔画方案内的拼音反查
-- 用法：切换到 26 字母键盘输入拼音（如 zhong），候选显示对应汉字（带拼音注释）。
-- 挂载：schema translators 添加 - lua_translator@*pinyin_reverse
-- 注意：librime-lua 的 lua_translator 调用模块表的 func 字段。
local pinyin_index = require("pinyin_index")

local T = {}

-- 精确匹配优先 + 前缀匹配补充（按字频降序，去重，最多 30 个）
function T.func(input, seg, env)
  if not input or input == "" then return end
  -- 只处理纯小写字母（拼音）
  if not input:match("^[a-z]+$") then return end
  local py = input:lower()

  local seen = {}
  local emitted = 0
  local function emit(ch, comment_py)
    if seen[ch] then return end
    seen[ch] = true
    yield(Candidate("reverse", seg.start, seg._end, ch, comment_py))
    emitted = emitted + 1
  end

  -- 1. 精确匹配（全拼）
  local exact = pinyin_index[py]
  if exact then
    for _, item in ipairs(exact) do
      emit(item[1], py)
      if emitted >= 30 then return end
    end
  end

  -- 2. 前缀匹配补充（候选不足时）
  if emitted < 20 then
    local prefix_hits = {}
    for k, v in pairs(pinyin_index) do
      if k:sub(1, #py) == py then
        for _, item in ipairs(v) do
          prefix_hits[#prefix_hits + 1] = {item[1], item[2], k}
        end
      end
    end
    table.sort(prefix_hits, function(a, b)
      if a[2] ~= b[2] then return a[2] > b[2] end
      return a[1] < b[1]
    end)
    for _, item in ipairs(prefix_hits) do
      emit(item[1], item[3])
      if emitted >= 30 then return end
    end
  end
end

return T