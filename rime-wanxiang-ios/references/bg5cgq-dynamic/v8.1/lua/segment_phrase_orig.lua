-- BG5 learning v10: 真正符合用户直觉的动态笔画分词与自学习系统
-- 核心体验保障：
-- 1. 点分词键（按 1 次 '）：严格锁定两字词组，按首字+次字笔顺顺序精准匹配；
-- 2. 点 2 次分词键：严格锁定三字词组；点 3 次：严格锁定四字词组；
-- 3. 刚按分词键（如 1324454'）：绝不卡顿、绝不空白，立刻推荐该字开头的两字高频词（如“还是”）；
-- 4. 笔画顺序完全匹配（exact）：无条件稳居第一位；
-- 5. 纯净度保障：绝无任何阿拉伯数字或编码注释。

local index = require('index')
local words = require('words')
local stroke = require('stroke')
local learning = require('learning')
local head_words = require('head_words')
local phrase_stroke_index = require('phrase_stroke_index')
local next_words = require('next_words')

local MAX_PREFIX = 96
local MAX_STATES = 8000
local MAX_OUTPUT = 150

local attached = setmetatable({}, { __mode = 'k' })
local cache = setmetatable({}, { __mode = 'k' })
local cache_rev = setmetatable({}, { __mode = 'k' })

-- 候选层级：单笔画符号顶格；普通字与词语先出；部件/部首仅完整笔顺后出现。
local STROKE_SYMBOLS = { ["一"] = true, ["丨"] = true, ["丿"] = true, ["丶"] = true, ["乙"] = true }
local PRIORITY_COMPONENTS = {}
for ch in ("一丨丿丶乙氵亻艹扌辶讠纟饣忄阝宀疒礻衤钅彳犭夂攵冖冂勹匚廴彡卩厶巛灬爫户戈攴疋癶缶聿艮豸"):gmatch("[\1-\127\194-\244][\128-\191]*") do
  PRIORITY_COMPONENTS[ch] = true
end
-- 笔画前缀匹配：支持通配符 ?（匹配任意一笔 1-5）
local function prefix_match(code, part)
  if not code then return false end
  if not part:find("?", 1, true) then
    return code:sub(1, #part) == part
  end
  local pat = "^" .. part:gsub("%?", "[12345]")
  return code:match(pat) ~= nil
end

local function complete_component(ch, code, input)
  return PRIORITY_COMPONENTS[ch] and code and not input:find("?", 1, true)
    and code == input
end

-- 精确码倒排（常驻，极小）：完整笔顺直接命中单字
local exact_stroke = {}
-- 单字词频：由 index 高频表累计，用于前缀候选按常用度排序，保证「暴」「露」这类常用字在短码下也能进入候选池
local char_freq = {}
for _, list in pairs(index) do
  for _, item in ipairs(list) do
    local ch = item[1]
    char_freq[ch] = (char_freq[ch] or 0) + (item[2] or 0)
  end
end
for ch, code in pairs(stroke) do
  local list = exact_stroke[code]
  if not list then
    list = {}
    exact_stroke[code] = list
  end
  list[#list + 1] = ch
end

-- Trie 增量桶（iOS 式按需构建 + LRU 即弃）：
-- 只预构建 1-5 首笔桶，后续每笔从父桶过滤（O(父桶大小)，<1ms），
-- 缓存上限 1024 个桶，远大于单次输入链，几乎不会触发全量重建；内存占用始终 <1MB。
-- 预排序字符表：全量重建时直接按词频序遍历，免去每次排序，彻底消除首字重建卡顿。
local sorted_chars = {}
for ch in pairs(stroke) do
  sorted_chars[#sorted_chars + 1] = ch
end
table.sort(sorted_chars, function(a, b)
  return (char_freq[a] or 0) > (char_freq[b] or 0)
end)
local bucket_cache = {}
local BUCKET_CACHE_MAX = 1024
local function build_bucket_full(seg)
  -- 全量返回（预排序），父桶过滤才能逐级保留低频常用字（如「审」在 4 前缀 300 名外也必须进入 44 桶）
  local arr = {}
  for _, ch in ipairs(sorted_chars) do
    local code = stroke[ch]
    if code and code:sub(1, #seg) == seg then
      arr[#arr + 1] = ch
    end
  end
  return arr
end
local function get_bucket(seg)
  if not seg or seg == '' then return {} end
  local cached = bucket_cache[seg]
  if cached then return cached end
  local parent = seg:sub(1, -2)
  local parent_bucket = bucket_cache[parent]
  local bucket
  if parent_bucket then
    -- 从父桶过滤，保持词频顺序（Trie 增量，极快）
    bucket = {}
    for _, ch in ipairs(parent_bucket) do
      local code = stroke[ch]
      if code and code:sub(1, #seg) == seg then
        bucket[#bucket + 1] = ch
      end
    end
  else
    bucket = build_bucket_full(seg)
  end
  local n = 0
  for _ in pairs(bucket_cache) do n = n + 1 end
  if n >= BUCKET_CACHE_MAX then
    bucket_cache = {}
  end
  bucket_cache[seg] = bucket
  return bucket
end
-- 预构建 1-5 首笔桶，保证第一笔输入零卡顿
for i = 1, 5 do
  get_bucket(tostring(i))
end

-- 词组切片索引：首字 → 以该字开头的全部词组（2字/3字/4字/5字+）。
-- 只索引 #w 为 3 的倍数的词（全部为三字节汉字，扩展字极罕见跳过，不影响常用词）。
-- 不排序：命中词在检索时按词频即时排序，命中通常很少，排序开销可忽略。
local char_words = {}
-- 仅为双字词建立第二字 1/2 笔前缀索引：覆盖最常用短码，避免运行时扫描全部词桶。
-- 索引保存已有词字符串引用，不复制文本；三字以上仍走通用桶，控制内存。
local pair_prefix_index = {}
-- 短码首字检索本身只遍历高频首字前 120 个；其余首字保留通用桶，避免无效常驻索引。
local indexed_first = {}
for i = 1, math.min(#sorted_chars, 120) do
  indexed_first[sorted_chars[i]] = true
end
for w, sf in pairs(words) do
  local n = #w
  if n >= 6 and n % 3 == 0 then
    local first = w:sub(1, 3)
    local bucket = char_words[first]
    if not bucket then
      bucket = {}
      char_words[first] = bucket
    end
    bucket[#bucket + 1] = w
    if n == 6 and indexed_first[first] then
      local second = w:sub(4, 6)
      local code = stroke[second]
      if code then
        local by_prefix = pair_prefix_index[first]
        if not by_prefix then
          by_prefix = {}
          pair_prefix_index[first] = by_prefix
        end
        for plen = 1, math.min(2, #code) do
          local p = code:sub(1, plen)
          local list = by_prefix[p]
          if not list then
            list = {}
            by_prefix[p] = list
          end
          list[#list + 1] = w
        end
      end
    end
  end
end

-- 惰性排序缓存：只在词组桶首次访问某首字时对该桶按词频排序一次并缓存。
-- 避免冷启动全量排序（+3.6s），同时保证每桶取词时高频词（审查/第一等）排前面。
local char_words_sorted = {}
local function get_sorted_bucket(first_ch)
  local sorted = char_words_sorted[first_ch]
  if sorted then return sorted end
  local raw = char_words[first_ch]
  if not raw or #raw == 0 then return nil end
  table.sort(raw, function(a, b)
    return (words[a] or 0) > (words[b] or 0)
  end)
  char_words_sorted[first_ch] = raw
  return raw
end

-- 词组桶 LRU 缓存：按「每字笔画前缀」直接命中词库词组（支持任意字数）。
-- 按下分词键时优先调用本桶；同一编码重复输入 O(1) 命中；缓存上限 64，超过即弃，内存始终极小。
local phrase_cache = {}
local PHRASE_CACHE_MAX = 64
-- 检查词 w（nchars 字）是否每一段的笔画前缀都与 parts 匹配
local function phrase_match(w, parts, nchars, start_part, wild_patterns)
  local ok = true
  for i = start_part or 1, nchars do
    local c = stroke[w:sub((i - 1) * 3 + 1, i * 3)]
    local part = parts[i]
    local matched
    if wild_patterns and wild_patterns[i] then
      matched = c and c:match(wild_patterns[i]) ~= nil
    else
      matched = prefix_match(c, part)
    end
    if not matched then
      ok = false
      break
    end
  end
  return ok
end
local function slice_phrase_bucket(parts)
  local key = table.concat(parts, "'")
  local cached = phrase_cache[key]
  if cached then return cached end
  local hits = {}
  local nchars = #parts
  local want_len = nchars * 3
  local wild_patterns = {}
  for i, part in ipairs(parts) do
    if part:find("?", 1, true) then
      wild_patterns[i] = "^" .. part:gsub("%?", "[12345]")
    end
  end
  local seen_first = {}
  local function collect(first_ch, is_exact)
    if seen_first[first_ch] then return end
    seen_first[first_ch] = true
    -- 先匹配再排序命中结果，避免对无关词组做整桶排序。
    -- 双字词且第二段为 1/2 笔短码时，直接命中惰性前缀索引；其余仍走完整桶。
    local bucket = char_words[first_ch]
    local indexed_pair = false
    -- 首笔确定、第二笔任意（如 1?）可复用第一笔索引；
    -- ?1、1?? 等无法安全复用的模式仍回退完整桶，确保不漏词。
    if nchars == 2 and #parts[2] <= 2 then
      local prefix_key = parts[2]
      local first_stroke = prefix_key:match("^([1-5])%?$")
      if first_stroke then prefix_key = first_stroke end
      if not prefix_key:find("?", 1, true) then
        local by_prefix = pair_prefix_index[first_ch]
        if by_prefix and by_prefix[prefix_key] then
          bucket = by_prefix[prefix_key]
          indexed_pair = true
        end
      end
    end
    if bucket then
      local limit = #bucket
      if indexed_pair then
        -- 索引桶只含双字词，且首字已由桶键验证。
        for idx = 1, limit do
          local w = bucket[idx]
          if phrase_match(w, parts, nchars, 2, wild_patterns) then hits[#hits + 1] = w end
        end
      else
        for idx = 1, limit do
          local w = bucket[idx]
          if #w == want_len and phrase_match(w, parts, nchars, 2) then
            hits[#hits + 1] = w
          end
        end
      end
    end
  end
  -- 1. 精确首字优先（全码输入时目标首字必在 exact_stroke 中，保证全量词库 100% 无遗漏命中）
  local exact_first = exact_stroke[parts[1]]
  if exact_first then
    for _, ch in ipairs(exact_first) do
      collect(ch, true)
    end
  end
  -- 2. 再遍历前缀桶高频首字（短码/前缀输入；限制前 120 字，每桶取前 30 高频词，兼顾召回与性能）
  local first_chars = get_bucket(parts[1])
  if first_chars then
    local limit = math.min(#first_chars, 120)
    for i = 1, limit do
      collect(first_chars[i], false)
    end
  end
  local n = 0
  for _ in pairs(phrase_cache) do n = n + 1 end
  if n >= PHRASE_CACHE_MAX then
    phrase_cache = {}
  end
  -- 只保留真实词频最高的 120 个，避免先对超大命中集全量排序。
  local K = 120
  local top_hits = {}
  local function score(w) return words[w] or 0 end
  local function sift_up(i)
    while i > 1 do
      local p = math.floor(i / 2)
      if score(top_hits[p]) <= score(top_hits[i]) then break end
      top_hits[p], top_hits[i] = top_hits[i], top_hits[p]
      i = p
    end
  end
  local function sift_down(i)
    while true do
      local l, r = i * 2, i * 2 + 1
      local m = i
      if l <= #top_hits and score(top_hits[l]) < score(top_hits[m]) then m = l end
      if r <= #top_hits and score(top_hits[r]) < score(top_hits[m]) then m = r end
      if m == i then break end
      top_hits[m], top_hits[i] = top_hits[i], top_hits[m]
      i = m
    end
  end
  for _, w in ipairs(hits) do
    if #top_hits < K then
      top_hits[#top_hits + 1] = w
      sift_up(#top_hits)
    elseif score(w) > score(top_hits[1]) then
      top_hits[1] = w
      sift_down(1)
    end
  end
  table.sort(top_hits, function(a, b) return score(a) > score(b) end)
  phrase_cache[key] = top_hits
  return top_hits
end

local function init(env)
  if not attached[env] then
    learning.attach(env)
    attached[env] = true
    cache[env] = {}
    cache_rev[env] = learning.revision()
  end
end

local function utf8_chars(s)
  local t = {}
  if not s then return t end
  for ch in s:gmatch("[\1-\127\194-\244][\128-\191]*") do
    t[#t + 1] = ch
  end
  return t
end

-- 快速 UTF-8 前两字提取（按字节数直接定位，比 gmatch 快数倍，用于构建 20 万双字词索引）
local function utf8_first_two(w)
  local b1 = w:byte(1)
  if not b1 then return nil, nil end
  local l1 = (b1 < 0x80) and 1 or (b1 < 0xE0) and 2 or (b1 < 0xF0) and 3 or 4
  local c1 = w:sub(1, l1)
  local rest = w:sub(l1 + 1)
  if rest == "" then return c1, nil end
  local b2 = rest:byte(1)
  local l2 = (b2 < 0x80) and 1 or (b2 < 0xE0) and 2 or (b2 < 0xF0) and 3 or 4
  return c1, rest:sub(1, l2)
end

local function utf8_first_char(s)
  if not s or s == '' then return nil end
  return s:match("^[\1-\127\194-\244][\128-\191]*")
end

local function to_stroke_symbol(s)
  if not s then return "" end
  -- 分词符 ' 必须保留（讯飞式：词组未上屏前，分词符一直显示在笔画串中）
  return s:gsub("1", "一"):gsub("2", "丨"):gsub("3", "丿"):gsub("4", "丶"):gsub("5", "乛"):gsub("[^一丨丿丶乛']", "？")
end

local function make_candidate(type, start, _end, text, raw_input)
  local c = Candidate(type, start, _end, text, '')
  local preedit = raw_input or ''
  local s, e = tonumber(start), tonumber(_end)
  if s and e and s >= 0 and e >= s and e <= #preedit then
    preedit = preedit:sub(s + 1, e)
  end
  c.preedit = to_stroke_symbol(preedit)
  return c
end

-- 笔画前缀匹配：支持通配符 ?（匹配任意一笔 1-5）
local function add_unique(out, seen, ch, exact, rank, component)
  if not seen[ch] then
    seen[ch] = exact and 2 or 1
    out[#out + 1] = {ch = ch, exact = exact, stroke_symbol = STROKE_SYMBOLS[ch] or false, component = component or false, rank = rank or 999999}
  else
    for _, item in ipairs(out) do
      if item.ch == ch then
        if exact then
          seen[ch] = 2
          item.exact = true
        end
        if component then item.component = true end
        break
      end
    end
  end
end

local function chars_for(seg, env)
  if not seg or seg == '' then return {} end
  local rev = learning.revision()
  if cache_rev[env] ~= rev then
    cache[env] = {}
    cache_rev[env] = rev
  end

  local saved = cache[env][seg]
  if saved then return saved end

  local out, seen = {}, {}
  local function add_char(ch, exact, rank)
    local is_component = PRIORITY_COMPONENTS[ch] and not STROKE_SYMBOLS[ch]
    if is_component and stroke[ch] ~= seg then return end
    add_unique(out, seen, ch, exact, rank, is_component or false)
  end

  -- 0. 通配检索：段内含 ? 时，? 匹配任意一笔（1-5），全量扫描命中所有可能字
  if seg:find("?", 1, true) then
    local pat = "^" .. seg:gsub("%?", "[12345]")
    for ch, code in pairs(stroke) do
      if code and code:match(pat) then
        if not PRIORITY_COMPONENTS[ch] then
          add_unique(out, seen, ch, false, 3000)
        end
      end
    end
    table.sort(out, function(a, b)
      if a.component ~= b.component then return a.component end
      local af, bf = learning.freq(a.ch, env), learning.freq(b.ch, env)
      if af ~= bf then return af > bf end
      local af2, bf2 = char_freq[a.ch] or 0, char_freq[b.ch] or 0
      if af2 ~= bf2 then return af2 > bf2 end
      if a.rank ~= b.rank then return a.rank < b.rank end
      return a.ch < b.ch
    end)
    cache[env][seg] = out
    return out
  end

  -- 1. O(1) 直取完整笔顺完全匹配的单字，彻底消灭 10117 次循环全表遍历！
  local exact_list = exact_stroke[seg]
  if exact_list then
    for _, ch in ipairs(exact_list) do
      add_char(ch, true, 0)
    end
  end

  -- 2. 注入用户在当前前缀下学习过的字（上屏频次优先）
  for ch, cnt in pairs(learning.all_chars(env)) do
    local code = stroke[ch]
    if code and (code == seg or code:sub(1, #seg) == seg) then
      add_char(ch, code == seg, 0)
    end
  end

  -- 只有完整笔顺输入时才注入偏旁/部首；前缀阶段不抢普通高频字位置。
  for ch in pairs(PRIORITY_COMPONENTS) do
    local code = stroke[ch]
    if complete_component(ch, code, seg) then
      add_unique(out, seen, ch, true, 900000, true)
    end
  end

  -- 3. Trie 增量桶（主索引）：按词频排序的完整切片，任何中间笔顺和低频常用字都能命中！
  local bucket = get_bucket(seg)
  if bucket then
    for i, ch in ipairs(bucket) do
      if i > MAX_PREFIX then break end
      local code = stroke[ch]
      local exact = code == seg
      add_char(ch, exact, 2000 + i)
    end
  end

  -- 4. 兜底：若全量切片缺失，回退 index 高频表
  local indexed = index[seg]
  if indexed and #out == 0 then
    for i = 1, math.min(#indexed, MAX_PREFIX) do
      local item = indexed[i]
      local ch = item[1]
      add_char(ch, false, i)
    end
  end

  table.sort(out, function(a, b)
    if a.stroke_symbol ~= b.stroke_symbol then return a.stroke_symbol end
    if a.component ~= b.component then return not a.component end
    if a.exact ~= b.exact then return a.exact end
    local af, bf = learning.freq(a.ch, env), learning.freq(b.ch, env)
    if af ~= bf then return af > bf end
    -- 完整部件只在完整编码后出现；普通字与学习频次先参与排序。
    if a.rank ~= b.rank then return a.rank < b.rank end
    return a.ch < b.ch
  end)

  cache[env][seg] = out
  return out
end

-- 单字及无分词高频词组联想输出（输入笔画时，单字优先，高频词组紧随其后）
local function emit_single(input, seg, env)
  local chars = chars_for(input, env)

  -- 笔画打多时的最长前缀容错兜底：绝不返回 0 候选，绝不把原始数字暴露在屏幕上！
  -- 回退时过滤偏旁部首：超过完整码后不得让部首重新出现。
  if #chars == 0 and #input > 1 then
    for l = #input - 1, 1, -1 do
      local sub_chars = chars_for(input:sub(1, l), env)
      local filtered = {}
      for _, item in ipairs(sub_chars) do
        if not item.component then filtered[#filtered + 1] = item end
      end
      if #filtered > 0 then
        chars = filtered
        break
      end
    end
  end

  local phrases = {}
  local seen_phrases = {}

  -- 1. 从用户学习库中收集当前编码开头的短语
  for word, count in pairs(learning.all(env)) do
    local chs = utf8_chars(word)
    local first = chs[1]
    local code = first and stroke[first]
    if code and code:sub(1, #input) == input and not seen_phrases[word] then
      seen_phrases[word] = true
      phrases[#phrases + 1] = {text = word, freq = count * 100000, exact = (code == input)}
    end
  end

  -- 2. 从系统 head_words 极速索引中提取前 3 个核心字的高频词组，复杂度 O(1)，绝不全表遍历！
  for i = 1, math.min(#chars, 3) do
    local ch = chars[i].ch
    local is_exact = chars[i].exact
    local bucket = head_words[ch] or {}
    for _, item in ipairs(bucket) do
      local w, sf = item[1], item[2]
      if not seen_phrases[w] then
        seen_phrases[w] = true
        local uf = learning.freq(w, env)
        phrases[#phrases + 1] = {text = w, freq = (uf * 100000) + sf, exact = is_exact}
      end
    end
  end

  table.sort(phrases, function(a, b)
    if a.exact ~= b.exact then return a.exact end
    if a.freq ~= b.freq then return a.freq > b.freq end
    return a.text < b.text
  end)

  -- 候选层级：单笔画顶格 → 完全码偏旁部首 → 完全码普通字 → 其他高频字 → 高频词语。
  local emitted = 0
  local symbols, comp_exacts, exacts, others = {}, {}, {}, {}
  for _, item in ipairs(chars) do
    if item.stroke_symbol then
      symbols[#symbols + 1] = item.ch
    elseif item.exact and item.component then
      comp_exacts[#comp_exacts + 1] = item.ch
    elseif item.exact then
      exacts[#exacts + 1] = item.ch
    else
      others[#others + 1] = item.ch
    end
  end

  -- 1. 单笔画符号顶格输出。
  for _, ch in ipairs(symbols) do
    yield(make_candidate('single', seg.start, seg._end, ch, input))
    emitted = emitted + 1
  end

  -- 2. 完全码命中的偏旁部首优先显示。
  for _, ch in ipairs(comp_exacts) do
    yield(make_candidate('single', seg.start, seg._end, ch, input))
    emitted = emitted + 1
  end

  -- 3. 完全码命中的普通字。
  for _, ch in ipairs(exacts) do
    yield(make_candidate('single', seg.start, seg._end, ch, input))
    emitted = emitted + 1
  end

  -- 4. 其他高频字（最多补足 9 个普通字展示位）。
  for _, ch in ipairs(others) do
    if emitted >= 9 + #exacts + #comp_exacts + #symbols then break end
    yield(make_candidate('single', seg.start, seg._end, ch, input))
    emitted = emitted + 1
  end

  -- 5. 高频词组联想（剩余配额）。
  for i = 1, math.min(#phrases, MAX_OUTPUT - emitted) do
    yield(make_candidate('phrase', seg.start, seg._end, phrases[i].text, input))
  end
end

-- 统一判断一个词是否与 parts 每一段完全匹配完整笔顺
local function is_phrase_exact(w, parts)
  local chs = utf8_chars(w)
  if #chs ~= #parts then return false end
  for i, ch in ipairs(chs) do
    local code = stroke[ch]
    if not code or code ~= parts[i] then
      return false
    end
  end
  return true
end

-- 动态分词组词输出：target_len 严格按分词次数锁定
-- full_len: Rime 分段模式下传入完整输入长度（用于跨段词组候选的 end）；不分段时传 nil
local function emit_phrase_with_parts(parts, target_len, raw_input, seg, env, full_len)
  local found = {}

  local function add_cand(w, sf)
    local chs = utf8_chars(w)
    if #chs ~= target_len then return end
    local exact = is_phrase_exact(w, parts)
    local uf = learning.freq(w, env)
    local old = found[w]
    if not old or (exact and not old.exact) or (uf > old.uf) then
      found[w] = {text = w, sf = sf or 0, uf = uf, exact = exact}
    end
  end

  -- 1. 词组精确桶：完整编码 O(1) 命中（分词后最高优先级，只检索词库词条）
  local has_phrase = false
  local fast_key = table.concat(parts, "'")
  local fast_list = phrase_stroke_index[fast_key]
  if fast_list then
    has_phrase = true
    for _, item in ipairs(fast_list) do
      add_cand(item[1], item[2])
    end
  end
  -- 2. 词组切片桶：按「每字笔画前缀」直接命中词库词组（任意字数，分词后第一优先级，LRU 缓存）
  local slice_hits = slice_phrase_bucket(parts)
  if #slice_hits > 0 then
    has_phrase = true
    for _, w in ipairs(slice_hits) do
      add_cand(w, words[w] or 0)
    end
  end

  -- 3. 用户自造/已学词库注入（上屏学习后始终参与召回，权重按 learning 频次排序）
  for w in pairs(learning.all(env)) do
    local chs = utf8_chars(w)
    if #chs == target_len then
      local matched = true
      for i, ch in ipairs(chs) do
        local code = stroke[ch]
        local part = parts[i]
        if not code or code:sub(1, #part) ~= part then
          matched = false
          break
        end
      end
      if matched then
        add_cand(w, words[w] or 0)
      end
    end
  end

  -- 4. 词组桶全部未命中时，才走单字组合（新造词/生僻词路径，优先级最低但绝不卡死）。
  --    5 字以上词已由词组切片桶覆盖，未完成时不再跑组合（避免长词逐键卡顿）。
  local count_found = 0
  for _ in pairs(found) do count_found = count_found + 1 end
  if count_found == 0 and target_len <= 4 then
    local candidates = {}
    for i, part in ipairs(parts) do
      local c_list = chars_for(part, env)
      if #c_list == 0 and #part > 1 then
        local merged, seen2 = {}, {}
        for l = #part - 1, 1, -1 do
          local sub_c = chars_for(part:sub(1, l), env)
          for _, item in ipairs(sub_c) do
            -- 回退时过滤偏旁部首：超过完整码后不得让部首重新出现。
            if not item.component and not seen2[item.ch] then
              seen2[item.ch] = true
              merged[#merged + 1] = item
            end
          end
          if #merged >= 96 then break end
        end
        c_list = merged
      end
      candidates[i] = c_list
    end
    local per_len = 12
    if target_len == 2 then per_len = 64
    elseif target_len == 3 then per_len = 25
    elseif target_len == 4 then per_len = 16 end
    -- 状态上限：单字组合是「新造词兜底路径」，绝不能因笛卡尔积爆炸卡顿（长词未完成时也绝不卡）
    local combine_states = 0
    local DYNAMIC_COMBINE_LIMIT = 8000
    local function combine_parts(depth, cur_text)
      combine_states = combine_states + 1
      if combine_states > DYNAMIC_COMBINE_LIMIT then return end
      if depth > target_len then
        local sf = words[cur_text]
        local uf = learning.freq(cur_text, env)
        if (sf and sf > 0) or (uf and uf > 0) then
          add_cand(cur_text, sf or 0)
        end
        return
      end
      local list = candidates[depth] or {}
      local limit = math.min(#list, per_len)
      for idx = 1, limit do
        combine_parts(depth + 1, cur_text .. list[idx].ch)
      end
    end
    combine_parts(1, "")
  end

  -- 5. 多输容错：仅当某段不是任何字的前缀（用户多输错笔画）时才回退截短。
  --    全码有效时绝不截短（否则「华」全码会被截成 1 笔「3」而错误命中「我国」等词）。
  count_found = 0
  for _ in pairs(found) do count_found = count_found + 1 end
  if count_found == 0 and #parts == 2 then
    local need_fallback = false
    for _, part in ipairs(parts) do
      local exact_list = exact_stroke[part]
      local bucket = get_bucket(part)
      if (not exact_list or #exact_list == 0) and (not bucket or #bucket == 0) then
        need_fallback = true
        break
      end
    end
    if need_fallback and (#parts[2] > 2 or #parts[1] > 2) then
      local p1, p2 = parts[1], parts[2]
      for l2 = #p2, 1, -1 do
        for l1 = #p1, 1, -1 do
          local try_key = p1:sub(1, l1) .. "'" .. p2:sub(1, l2)
          local try_list = phrase_stroke_index[try_key]
          if try_list and #try_list > 0 then
            for _, item in ipairs(try_list) do
              add_cand(item[1], item[2])
            end
            break
          end
        end
        local c2 = 0
        for _ in pairs(found) do c2 = c2 + 1 end
        if c2 > 0 then break end
      end
    end
  end
  local order = {}
  for w in pairs(found) do order[#order + 1] = found[w] end

  -- 计算 raw_input 中每一段（按 ' 分隔）在整体输入中的字节偏移（0-based，供候选独立提交用）
local function compute_part_offsets(raw_input)
  local offsets = {}
  local pos = 1
  for p in raw_input:gmatch("[^']+") do
    local idx = raw_input:find(p, pos, true)
    if idx then
      -- Rime Candidate.end 是右开位置；非末段词连同其后的分隔符一起消费，
      -- 这样点选前段词后，剩余 composition 从下一段笔画开始。
      local e = idx + #p - 1
      if raw_input:sub(e + 1, e + 1) == "'" then e = e + 1 end
      offsets[#offsets + 1] = { start = idx - 1, _end = e }
      pos = idx + #p + 1
    end
  end
  return offsets
end

  -- 造词等待区词组排序：重复上屏词优先，静态词频次之，原索引顺序兜底。
  local function sort_waiting_phrases(items, env)
    table.sort(items, function(a, b)
      local au, bu = learning.freq(a.text, env), learning.freq(b.text, env)
      if au ~= bu then return au > bu end
      local as, bs = a.sf or 0, b.sf or 0
      if as ~= bs then return as > bs end
      return (a.rank or 0) < (b.rank or 0)
    end)
  end

  -- 统一候选输出：分词输入优先词库已有词组（整词/前后段词），检索不到词组时才按段序输出全码字，再其余字与完整部件。
  local function emit_all(emit_candidate, whole_phrases, waiting_items, parts, env, offsets, seg_start, seg_end)
    -- 1. 词库已有整词最优先。
    if whole_phrases then
      for _, item in ipairs(whole_phrases) do
        emit_candidate('phrase', item.text, seg_start, seg_end)
      end
    end
    -- 2. 前/后段成型词组（词库已有词组按编码匹配优先）。
    if waiting_items then
      for _, item in ipairs(waiting_items) do
        emit_candidate('phrase', item.text, item.s, item.e)
      end
    end
    -- 3. 检索不到词组时，才按段序输出每段全码精确字（范围锁在本段）。
    for i, part in ipairs(parts) do
      local s = offsets[i] and offsets[i].start or seg_start
      local e = offsets[i] and offsets[i]._end or seg_end
      local clist = chars_for(part, env)
      for _, item in ipairs(clist) do
        if item.exact then
          emit_candidate('single', item.ch, s, e)
        end
      end
    end
    -- 4. 每段其余候选字。
    for i, part in ipairs(parts) do
      local s = offsets[i] and offsets[i].start or seg_start
      local e = offsets[i] and offsets[i]._end or seg_end
      local clist = chars_for(part, env)
      for _, item in ipairs(clist) do
        if not item.exact and not item.component then
          emit_candidate('single', item.ch, s, e)
        end
      end
    end
    -- 5. 完整部件。
    for i, part in ipairs(parts) do
      local s = offsets[i] and offsets[i].start or seg_start
      local e = offsets[i] and offsets[i]._end or seg_end
      clist = chars_for(part, env)
      for _, item in ipairs(clist) do
        if item.component and not item.exact then
          emit_candidate('single', item.ch, s, e)
        end
      end
    end
  end

  -- 容错兜底：整词不存在时，启动【造词引擎】，前段成词与后段字词全部按编码优先进入候选区！
  if #order == 0 then
    local offsets = compute_part_offsets(raw_input)
    local added = {}
    local function add_output(type, cand_text, s, e)
      s, e = s or seg.start, e or seg._end
      local key = type .. "\0" .. tostring(s) .. ":" .. tostring(e) .. "\0" .. cand_text
      if not added[key] then
        added[key] = true
        yield(make_candidate(type, s, e, cand_text, raw_input))
      end
    end

    -- 全码精确字最优先，随后是前/后段成型词组，再是其余候选字与完整部件。
    local waiting = {}
    if #parts >= 2 then
      for sub_len = 2, #parts - 1 do
        local sub_parts = {}
        for i = 1, sub_len do sub_parts[i] = parts[i] end
        local sub_key = table.concat(sub_parts, "'")
        local s = offsets[1] and offsets[1].start or seg.start
        local e = offsets[sub_len] and offsets[sub_len]._end or seg._end
        local fast_sub = phrase_stroke_index[sub_key]
        if fast_sub then
          for rank, item in ipairs(fast_sub) do waiting[#waiting + 1] = {text=item[1], sf=item[2], rank=rank, s=s, e=e} end
        end
        local sub_hits = slice_phrase_bucket(sub_parts)
        for rank, hp in ipairs(sub_hits) do waiting[#waiting + 1] = {text=hp, sf=words[hp] or 0, rank=1000+rank, s=s, e=e} end
      end
      if #parts >= 4 then
        local tail_parts = { parts[#parts - 1], parts[#parts] }
        local tail_key = table.concat(tail_parts, "'")
        local s = offsets[#parts - 1] and offsets[#parts - 1].start or seg.start
        local e = offsets[#parts] and offsets[#parts]._end or seg._end
        local fast_tail = phrase_stroke_index[tail_key]
        if fast_tail then
          for rank, item in ipairs(fast_tail) do waiting[#waiting + 1] = {text=item[1], sf=item[2], rank=rank, s=s, e=e} end
        end
        local tail_hits = slice_phrase_bucket(tail_parts)
        for rank, tp in ipairs(tail_hits) do waiting[#waiting + 1] = {text=tp, sf=words[tp] or 0, rank=1000+rank, s=s, e=e} end
      end
      sort_waiting_phrases(waiting, env)
    end
    emit_all(add_output, nil, waiting, parts, env, offsets, seg.start, seg._end)

    -- 3. 终极死守：如果连一个字都没拼出来，输出笔画符号，绝不露数字
    local has_any = false
    for _ in pairs(added) do has_any = true break end
    if not has_any then
      local sym = to_stroke_symbol(raw_input)
      yield(make_candidate('single', seg.start, seg._end, sym, raw_input))
    end
    return
  end

  table.sort(order, function(a, b)
    if a.exact ~= b.exact then return a.exact end
    if a.uf ~= b.uf then return a.uf > b.uf end
    if a.sf ~= b.sf then return a.sf > b.sf end
    return a.text < b.text
  end)

  -- 统一候选输出：全码精确字 → 整词 → 前/后段成型词组 → 其余候选字 → 完整部件。
  local emitted_count = 0
  local added = {}
  local offsets = compute_part_offsets(raw_input)
  local function add_output(type, cand_text, s, e)
    if emitted_count >= MAX_OUTPUT then return false end
    s, e = s or seg.start, e or seg._end
    local key = type .. "\0" .. tostring(s) .. ":" .. tostring(e) .. "\0" .. cand_text
    if not added[key] then
      added[key] = true
      yield(make_candidate(type, s, e, cand_text, raw_input))
      emitted_count = emitted_count + 1
      return true
    end
    return false
  end
  local whole_phrases = {}
  for _, item in ipairs(order) do
    whole_phrases[#whole_phrases + 1] = {text=item.text}
  end
  local waiting = {}
  if #parts >= 2 then
    for sub_len = 2, #parts - 1 do
      local sub_parts = {}
      for i = 1, sub_len do sub_parts[i] = parts[i] end
      local sub_key = table.concat(sub_parts, "'")
      local s = offsets[1] and offsets[1].start or seg.start
      local e = offsets[sub_len] and offsets[sub_len]._end or seg._end
      local fast_sub = phrase_stroke_index[sub_key]
      if fast_sub then
        for rank, item in ipairs(fast_sub) do waiting[#waiting + 1] = {text=item[1], sf=item[2], rank=rank, s=s, e=e} end
      end
      local sub_hits = slice_phrase_bucket(sub_parts)
      for rank, hp in ipairs(sub_hits) do waiting[#waiting + 1] = {text=hp, sf=words[hp] or 0, rank=1000+rank, s=s, e=e} end
    end
    if #parts >= 4 then
      local tail_parts = { parts[#parts - 1], parts[#parts] }
      local tail_key = table.concat(tail_parts, "'")
      local s = offsets[#parts - 1] and offsets[#parts - 1].start or seg.start
      local e = offsets[#parts] and offsets[#parts]._end or seg._end
      local fast_tail = phrase_stroke_index[tail_key]
      if fast_tail then
        for rank, item in ipairs(fast_tail) do waiting[#waiting + 1] = {text=item[1], sf=item[2], rank=rank, s=s, e=e} end
      end
      local tail_hits = slice_phrase_bucket(tail_parts)
      for rank, tp in ipairs(tail_hits) do waiting[#waiting + 1] = {text=tp, sf=words[tp] or 0, rank=1000+rank, s=s, e=e} end
    end
    sort_waiting_phrases(waiting, env)
  end
  emit_all(add_output, whole_phrases, waiting, parts, env, offsets, seg.start, seg._end)

  -- 终极保底：如果没有任何候选，输出笔画符号
  if emitted_count == 0 then
    local sym = to_stroke_symbol(raw_input)
    yield(make_candidate('single', seg.start, seg._end, sym, raw_input))
  end
end


-- 处理末尾按下分词键（以 ' 结尾）的通用高频连缀联想（不限字数，字词皆可连）
-- 场景1: 打出单字笔画后按分词（如 3121' 或 1324454'）-> 联想以“我”或“还”开头的所有高频短语（我们、我的、我想、还是、还有...）
-- 场景2: 打出两字词后按分词（如 31'32'）-> 联想以“我们”开头的所有高频连缀短语（我们的、我们可以、我们要...）
local function emit_open_continuation(prefix_expr, raw_input, seg, env)
  local head_candidates = {}
  if prefix_expr:find("'", 1, true) then
    -- 优先 O(1) 查 phrase_stroke_index 快速获取前序词（如 "我们"）
    local fast_heads = phrase_stroke_index[prefix_expr]
    if fast_heads then
      for i = 1, math.min(#fast_heads, 8) do
        head_candidates[#head_candidates + 1] = fast_heads[i][1]
      end
    end

    local parts = {}
    for p in prefix_expr:gmatch("[^']+") do
      if p:match("^[12345?]+$") then parts[#parts + 1] = p end
    end
    if #parts >= 2 and #head_candidates == 0 then
      local cand_groups = {}
      for i, pt in ipairs(parts) do
        cand_groups[i] = chars_for(pt, env)
        if #cand_groups[i] == 0 then
          -- 错码后按分隔符仍须提供覆盖当前输入的笔画候选，避免原始编码回显。
          yield(make_candidate('stroke_fallback', seg.start, seg._end,
            to_stroke_symbol(raw_input), raw_input))
          return
        end
      end
      local sub_states = 0
      local function sub_dfs(depth, txt)
        if sub_states >= MAX_STATES then return end
        if depth > #parts then
          if words[txt] or learning.is_learned(txt, env) then
            head_candidates[#head_candidates + 1] = txt
          end
          return
        end
        for _, it in ipairs(cand_groups[depth]) do
          sub_states = sub_states + 1
          if sub_states > MAX_STATES then return end
          local nxt = txt .. it.ch
          if depth == #parts then
            if words[nxt] or learning.is_learned(nxt, env) then sub_dfs(depth + 1, nxt) end
          else
            sub_dfs(depth + 1, nxt)
          end
        end
      end
      sub_dfs(1, "")
    end
  else
    local clist = chars_for(prefix_expr, env)
    for i = 1, math.min(#clist, 5) do
      head_candidates[#head_candidates + 1] = clist[i].ch
    end
  end

  if #head_candidates == 0 then
    -- 前缀对不上任何字：只显示笔画图形，绝不把原始数字留在输入栏
    yield(make_candidate('single', seg.start, seg._end, to_stroke_symbol(raw_input), raw_input))
    return
  end

  local found = {}
  local seen_head = {}
  for _, head in ipairs(head_candidates) do
    if not seen_head[head] then
      seen_head[head] = true
      local h_len = #head
      local first_ch = utf8_first_char(head)
      local bucket = head_words[first_ch] or {}
      for _, item in ipairs(bucket) do
        local w, sf = item[1], item[2]
        if #w > h_len and w:sub(1, h_len) == head then
          local uf = learning.freq(w, env)
          found[w] = {sf = sf, uf = uf}
        end
      end
      for w, uf in pairs(learning.all(env)) do
        if #w > h_len and w:sub(1, h_len) == head then
          local sf = words[w] or 0
          found[w] = {sf = sf, uf = uf}
        end
      end
    end
  end

  -- 单段刚按分词：先出这个笔画能对上的字，再出以它开头的词。不能只出更长词，更不能空。
  local single_heads = {}
  if not prefix_expr:find("'", 1, true) then
    local clist = chars_for(prefix_expr, env)
    for i = 1, math.min(#clist, 8) do
      single_heads[#single_heads + 1] = clist[i].ch
    end
  end

  local order = {}
  for w in pairs(found) do order[#order + 1] = w end

  if #order == 0 and #single_heads == 0 then
    for i = 1, math.min(#head_candidates, MAX_OUTPUT) do
      yield(make_candidate('phrase', seg.start, seg._end, head_candidates[i], raw_input))
    end
    if #head_candidates == 0 then
      local sym = to_stroke_symbol(raw_input)
      yield(make_candidate('single', seg.start, seg._end, sym, raw_input))
    end
    return
  end

  table.sort(order, function(a, b)
    local item_a, item_b = found[a], found[b]
    if item_a.uf ~= item_b.uf then return item_a.uf > item_b.uf end
    if item_a.sf ~= item_b.sf then return item_a.sf > item_b.sf end
    return a < b
  end)

  local emitted = {}
  for i = 1, math.min(#single_heads, 4) do
    local ch = single_heads[i]
    emitted[ch] = true
    yield(make_candidate('single', seg.start, seg._end, ch, raw_input))
  end
  for i = 1, math.min(#order, MAX_OUTPUT) do
    if not emitted[order[i]] then
      yield(make_candidate('phrase', seg.start, seg._end, order[i], raw_input))
    end
  end
end

-- 上屏后的无按键智能连贯联想（字词上屏后，候选区自动跟出可连上的高频字词）
local function emit_predict_continuation(seg, env)
  local last = learning.get_last_commit()
  if not last or last == '' then
    -- 还没有任何上屏记录时，给出可点的常用起句词，避免候选栏空白
    for _, w in ipairs({"你好", "我们", "可以", "这个", "什么", "现在", "今天", "没有"}) do
      yield(Candidate('predict', seg.start, seg._end, w, ''))
    end
    return
  end
  local l_len = #last

  local found = {}
  -- 任意词上屏后都有可接的通用后接词。next_words 只覆盖几十个词，不能让其它词联想空白。
  local generic = {"的", "了", "吗", "啊", "呢", "吧", "和", "是", "不", "也", "就", "都", "很", "在", "有"}
  for i, w in ipairs(generic) do
    found[w] = {sf = 200000 - i * 100, uf = learning.freq(w, env)}
  end

  -- 1. 优先提取二元文法 next_words[last]，输出最地道、最顺畅的后接词组，支持无限连击打字！
  local nxt_list = next_words[last]
  if nxt_list then
    for rank, w in ipairs(nxt_list) do
      local uf = learning.freq(w, env)
      found[w] = {sf = 300000 - (rank * 1000), uf = uf}
    end
  end

  -- 2. 从 head_words 中截取后缀作为词内补全候选
  local first_ch = utf8_first_char(last)
  local bucket = head_words[first_ch] or {}
  for _, item in ipairs(bucket) do
    local w, sf = item[1], item[2]
    if #w > l_len and w:sub(1, l_len) == last then
      local suffix = w:sub(l_len + 1)
      local uf = learning.freq(suffix, env)
      local old = found[suffix]
      if not old or sf > old.sf or uf > (old.uf or 0) then
        found[suffix] = {sf = sf, uf = uf}
      end
    end
  end

  -- 3. 在用户学习库中寻找
  for w, uf in pairs(learning.all(env)) do
    if #w > l_len and w:sub(1, l_len) == last then
      local suffix = w:sub(l_len + 1)
      local sf = words[suffix] or 0
      local old = found[suffix]
      if not old or uf > (old.uf or 0) then
        found[suffix] = {sf = sf, uf = uf}
      end
    end
  end

  -- 4. 末尾字组词（降权）：上一个字的末尾字能组成的双字词，其第二字作为候选，支持连续组词联想
  local last_chs = utf8_chars(last)
  local tail_ch = last_chs[#last_chs]
  if tail_ch then
    local sorted_bucket = get_sorted_bucket(tail_ch)
    if sorted_bucket then
      for _, w in ipairs(sorted_bucket) do
        if #w == 6 then
          local second = w:sub(4, 6)
          local wf = words[w] or 0
          local old = found[second]
          if not old or (150000 + wf) > (old.sf or 0) then
            found[second] = {sf = 150000 + wf, uf = learning.freq(second, env)}
          end
        end
      end
    end
  end

  local order = {}
  for s in pairs(found) do order[#order + 1] = s end
  table.sort(order, function(a, b)
    local item_a, item_b = found[a], found[b]
    if item_a.uf ~= item_b.uf then return item_a.uf > item_b.uf end
    if item_a.sf ~= item_b.sf then return item_a.sf > item_b.sf end
    return a < b
  end)

  for i = 1, math.min(#order, 20) do
    yield(Candidate('predict', seg.start, seg._end, order[i], ''))
  end
end

local function translator(input, seg, env)
  if not seg or seg.start == nil or seg._end == nil then return end
  if input and input:sub(1, 1) == 'V' then return end
  init(env)

  -- 顶部 preedit 显示笔画符号（如 323'53 -> 丿丨丿'乛丿），不显示阿拉伯数字
  if input and input ~= '' then
    local ctx = env.engine and env.engine.context
    if ctx and ctx.composition and not ctx.composition:empty() then
      local segobj = ctx.composition:back()
      if segobj then
        segobj.preedit = to_stroke_symbol(input)
      end
    end
  end

  -- 情况 0: 空输入状态（字/词刚刚上屏，等待用户打下一个字或点击联想）
  if not input or input == '' then
    emit_predict_continuation(seg, env)
    return
  end

  -- 情况 A: 刚按下分词符，末尾是 ' (例如 3121' 或 1324454' 或 31'32')
  -- 立即触发高频连缀联想（不限字数，字词皆通）
  if input:sub(-1, -1) == "'" then
    local prefix_expr = input:sub(1, -2)
    if prefix_expr ~= "" and not prefix_expr:find("''", 1, true) then
      emit_open_continuation(prefix_expr, input, seg, env)
      return
    end
  end

  -- 统计分词符数量
  local seg_count = 0
  for _ in input:gmatch("'") do seg_count = seg_count + 1 end

  if seg_count > 0 then
    -- 点 1 次分词：锁定 2 字词；点 2 次分词：锁定 3 字词；以此类推
    local target_len = seg_count + 1
    local parts = {}
    for p in input:gmatch("[^']+") do
      if p:match("^[12345?]+$") then
        parts[#parts + 1] = p
      end
    end

    if #parts == target_len then
      emit_phrase_with_parts(parts, target_len, input, seg, env)
      return
    end
    -- 若分段数量暂未完全对齐（例如刚按了分词键），优先输出第一段的匹配结果兜底
    if #parts >= 1 then
      emit_phrase_with_parts(parts, #parts, input, seg, env)
      return
    end
  else
    -- 无分词输入：纯单字模式
    if input:match("^[12345?]+$") then
      emit_single(input, seg, env)
      return
    end
  end

  -- 全局终极保底：任何未预期的输入，候选显示笔画符号，绝不留白，绝不显示数字！
  local safe_sym = to_stroke_symbol(input)
  yield(make_candidate('single', seg.start, seg._end, safe_sym, input))
end

return translator
