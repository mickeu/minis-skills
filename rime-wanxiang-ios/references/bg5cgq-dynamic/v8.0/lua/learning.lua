-- BG5 learning v10: 高性能、健壮可靠的词组自学习与单字调频系统
-- 1. 静态词与新造词统一调频：使用频次优先；
-- 2. 学习词自动构建 O(1) 前缀索引：杜绝 DFS 性能卡顿；
-- 3. 安全的文件 I/O：原子重命名与 pcall 异常防护；
-- 4. 上屏写入合并（每 4 次上屏落盘一次），杜绝连续上屏卡顿；
-- 5. 纯净度保障：不输出任何 comment 或数字编码。

local M = {}
local loaded = false
local data = {}             -- 文字/词组 -> 累计上屏频次（唯一持久化数据源）
local learned = {}          -- 所有学习到的多字词组 -> 频次
local learned_chars = {}    -- 学习到的单字 -> 频次
local learned_prefix = {}   -- 学习词组的前缀哈希集合 -> true
local path = nil
local revision = 0
local save_counter = 0
local SAVE_INTERVAL = 4     -- 每 4 次上屏合并落盘一次，减少写盘卡顿

-- 偏旁部首不参与学习：必须完整码输入才出现在候选区，不能通过学习调频。
local NON_LEARNING_RADICALS = {}
for ch in ("氵亻艹扌辶讠纟饣忄阝宀疒礻衤钅彳犭夂攵冖冂勹匚廴彡卩厶巛灬爫户戈攴疋癶缶聿艮豸"):gmatch("[\1-\127\194-\244][\128-\191]*") do
  NON_LEARNING_RADICALS[ch] = true
end

function M.revision() return revision end

local function user_dir()
  if rime_api and rime_api.get_user_data_dir then
    local d = rime_api:get_user_data_dir()
    if d and d ~= '' then return d end
  end
  return '.'
end

local function utf8_chars(s)
  local t = {}
  for ch in s:gmatch("[\1-\127\194-\244][\128-\191]*") do
    t[#t + 1] = ch
  end
  return t
end

-- 提取汉字，排除所有控制字符、英文字母及单字节符号
local function chinese_only(s)
  if not s or s == '' then return false end
  local chars = utf8_chars(s)
  if #chars == 0 then return false end
  for _, ch in ipairs(chars) do
    if #ch < 3 or ch:byte() < 0x80 then return false end
  end
  return true
end

local function add_learned_prefixes(w)
  local chars = utf8_chars(w)
  if #chars <= 1 then return end
  local prefix = ""
  for i = 1, #chars - 1 do
    prefix = prefix .. chars[i]
    learned_prefix[prefix] = true
  end
end

-- 从 data 重建派生索引（加载时执行一次）
local function rebuild_indexes()
  learned = {}
  learned_chars = {}
  learned_prefix = {}
  for w, cnt in pairs(data) do
    local chars = utf8_chars(w)
    if #chars == 1 then
      -- 偏旁部首不参与学习重建。
      if not NON_LEARNING_RADICALS[w] then
        learned_chars[w] = cnt
      end
    else
      learned[w] = cnt
      add_learned_prefixes(w)
    end
  end
end

local function load(env)
  if loaded then return end
  loaded = true
  local d = user_dir()
  path = d .. '/bg5-learning.user.tsv'

  local f = io.open(path, 'r')
  if f then
    for line in f:lines() do
      local w, n = line:match('^([^\t]+)\t(%d+)$')
      if w then
        data[w] = tonumber(n)
      end
    end
    f:close()
  end
  rebuild_indexes()
end

local function safe_save_file(p, table_data)
  if not p then return end
  local tmp = p .. '.tmp.' .. tostring(math.random(100000, 999999))
  local f = nil
  local ok, err = pcall(function()
    f = assert(io.open(tmp, 'w'))
    for w, n in pairs(table_data) do
      f:write(w, '\t', tostring(n), '\n')
    end
    f:close()
    f = nil
    -- POSIX 原子替换，绝不提前 os.remove
    os.rename(tmp, p)
  end)
  if f then
    pcall(function() f:close() end)
  end
  if not ok then
    pcall(os.remove, tmp)
  end
end

-- 合并落盘：每次上屏只累加计数器，达到间隔才写文件（数据源只有 data 一个表）
local function save()
  if path then safe_save_file(path, data) end
end

function M.freq(w, env)
  load(env)
  return data[w] or 0
end

function M.all(env)
  load(env)
  return learned
end

function M.all_chars(env)
  load(env)
  return learned_chars
end

function M.is_learned(w, env)
  load(env)
  return learned[w] ~= nil
end

-- O(1) 哈希查询前缀，彻底避免在大规模学习数据下全表扫描卡顿
function M.has_prefix(prefix, env)
  load(env)
  return learned_prefix[prefix] == true
end

function M.add(w, env)
  load(env)
  if not chinese_only(w) then return end
  local chars = utf8_chars(w)
  -- 偏旁部首不参与学习，不累计、不调频。
  if #chars == 1 and NON_LEARNING_RADICALS[w] then return end
  local cnt = (data[w] or 0) + 1
  data[w] = cnt

  if #chars == 1 then
    learned_chars[w] = cnt
  else
    learned[w] = cnt
    add_learned_prefixes(w)
  end

  revision = revision + 1
  -- 合并写盘：每 SAVE_INTERVAL 次上屏才落盘一次，消除连续上屏卡顿
  save_counter = save_counter + 1
  if save_counter >= SAVE_INTERVAL then
    save_counter = 0
    save()
  end
end

local last_commit = nil
local prev_commit = nil

function M.get_last_commit()
  return last_commit
end

function M.set_last_commit(text)
  last_commit = text
end

-- 连续上屏组合造词：上一次上屏的字/词 + 本次上屏的字/词 = 新造词（讯飞式造词）
function M.learn_word(w, env)
  load(env)
  if not chinese_only(w) then return end
  local chars = utf8_chars(w)
  -- 偏旁部首不参与学习。
  if #chars == 1 and NON_LEARNING_RADICALS[w] then return end
  local cnt = (data[w] or 0) + 1
  data[w] = cnt
  if #chars == 1 then
    learned_chars[w] = cnt
  else
    learned[w] = cnt
    add_learned_prefixes(w)
  end
  revision = revision + 1
  save_counter = save_counter + 1
  if save_counter >= SAVE_INTERVAL then
    save_counter = 0
    save()
  end
end

function M.attach(env)
  local c = env.engine and env.engine.context
  if not c or not c.commit_notifier then return false end
  -- 避免重复挂接
  if env._bg5_learning_connected then return true end
  local function on_commit(ctx)
    local text = ctx:get_commit_text() or ''
    if text ~= '' and chinese_only(text) then
      -- 连续上屏组合造词：上一次上屏 + 本次上屏 = 新造词（若组合仍为纯中文）
      if prev_commit and prev_commit ~= text then
        local combined = prev_commit .. text
        if chinese_only(combined) then
          M.learn_word(combined, env)
        end
      end
      M.add(text, env)
      prev_commit = text
      last_commit = text
    end
  end
  c.commit_notifier:connect(on_commit)
  env._bg5_learning_connected = true
  return true
end

return M