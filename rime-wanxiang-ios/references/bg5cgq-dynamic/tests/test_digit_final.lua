package.path = "/var/minis/workspace/bg5-learning/package/lua/?.lua;" .. package.path
local tr = require("segment_phrase")
local filter = require("filter_seg_count")

local env = { engine = { schema = { config = { get_string = function() return "" end } }, context = { input = "" } } }
yield = coroutine.yield
Candidate = function(t, s, e, text, comment)
  return {type=t, text=text, comment=comment or "", preedit=(text or ""):gsub("1","一"):gsub("2","丨"):gsub("3","丿"):gsub("4","丶"):gsub("5","乛"):gsub("'"," "):gsub("[^一丨丿丶乛 ]","？")}
end

local function translate(input)
  env.engine.context.input = input
  local cands = {}
  local co = coroutine.create(function()
    tr(input, { start = 0, _end = #input }, env)
  end)
  while coroutine.status(co) ~= "dead" do
    local ok, c = coroutine.resume(co)
    if not ok then return cands, c end
    if c then cands[#cands+1] = c end
  end
  return cands
end

local function run_filter(cands)
  local idx = 0
  local iter = coroutine.create(function()
    for _, c in ipairs(cands) do
      coroutine.yield(c)
    end
  end)
  local yielded = {}
  local co = coroutine.create(function()
    local fake_input = {
      iter = function()
        return function()
          local ok, c = coroutine.resume(iter)
          if ok and c then return c end
        end
      end
    }
    filter(fake_input, env)
  end)
  while coroutine.status(co) ~= "dead" do
    local ok, c = coroutine.resume(co)
    if ok and c then yielded[#yielded+1] = c end
  end
  return yielded
end

local function check(name, input, must_have)
  local cands, err = translate(input)
  if err then print("ERR", name, err); return false end
  local filtered = run_filter(cands)
  local texts = {}
  for _, c in ipairs(filtered) do texts[#texts+1] = c.text end
  local has_digit = false
  for _, t in ipairs(texts) do if t:find("%d") then has_digit = true end end
  local hit = false
  if must_have then
    for _, t in ipairs(texts) do if t == must_have then hit = true end end
  end
  local ok = #filtered > 0 and not has_digit and (not must_have or hit)
  print(string.format("%-32s filter后n=%d 数字=%s 命中[%s]=%s => %s",
    name, #filtered, has_digit and "有!" or "无", must_have or "-", ok and "PASS" or "FAIL", table.concat(texts, " | ")))
  return ok
end

local all = true
all = check("审查全码", "44525112'123425111", "审查") and all
all = check("审查全码多输55", "44525112'12342511155", "审查") and all
all = check("审查前2+查全码", "44'123425111", "审查") and all
all = check("审查前2+查前2", "44'12", "审查") and all
all = check("分词第二段无效", "44525112'99999", nil) and all
all = check("无效+分词键", "99999'", nil) and all
all = check("你好全码", "3235234'531521", "你好") and all
all = check("词语全码", "4551251'451251251", "词语") and all
all = check("暴露前4+露前4", "2511'1452", "暴露") and all
all = check("你差一笔按分词", "323523'", "你") and all
all = check("单字多输", "3121534123", "我") and all
all = check("空输入联想", "", nil) and all
print(all and "ALL_PASS" or "HAS_FAIL")