package.path = '/var/minis/mounts/BG5CGQ-learning-v7 6/lua/?.lua'
_G.rime_api = { get_user_data_dir = function() return '/tmp/bg5-test-user' end }
os.execute('mkdir -p /tmp/bg5-test-user')
for _, f in ipairs({'bg5-learning.user.tsv','bg5-learning.words.tsv'}) do
  os.remove('/tmp/bg5-test-user/' .. f)
end
local learning = require('learning')
local segment_phrase = require('segment_phrase')
local env = { engine = { context = {} } }

function yield(...) return coroutine.yield(...) end
function Candidate(_type, s, e, text, comment)
  return {type=_type, start=s, _end=e, text=text, comment=comment or ''}
end

local function run_input(input)
  local seg = { start = 0, _end = #input }
  local out = {}
  local co = coroutine.create(function() segment_phrase(input, seg, env) end)
  while true do
    local ok, cand = coroutine.resume(co)
    if not ok then error(cand) end
    if coroutine.status(co) == 'dead' then break end
    out[#out + 1] = cand
  end
  return out
end

local results = {}
local function pr(label, input, n)
  local ok, out = pcall(run_input, input)
  io.write('\n== ' .. label .. ' ==\n')
  if not ok then io.write('ERROR: ', tostring(out), '\n') return end
  local all_comment_empty = true
  for i, c in ipairs(out) do
    if i > (n or 20) then break end
    if c.comment ~= '' then all_comment_empty = false end
    io.write(string.format('%d.%s(comment=%q,type=%s)\n', i, c.text, c.comment, c.type))
  end
  io.write(string.format('[纯净度] 输出%d条, comment全空=%s\n', math.min(#out,n or 20), tostring(all_comment_empty)))
end

pr('A.完整笔顺直接输入312153432425(我们)', "312153432425", 12)
pr('B.分词输入31215\'32425(我们)', "31215'32425", 12)
pr('C.分词输入31215\'324(们前缀)', "31215'324", 12)
pr('D.我完整笔顺3121534', '3121534', 8)

-- 学习：模拟上屏“犍”一次（完整笔顺312154）
learning.add('犍', env)
pr('E.调频后完整312154', '312154', 10)
pr('F.调频后前缀3121', '3121', 10)
pr('G.调频后首笔3', '3', 12)

-- 学习陌生词
learning.add('张三丰', env)
learning.add('狗娘养的', env)
pr('H.输入3召回(张三丰/狗娘养的)', '3', 20)
pr('I.输入张三丰分词5153154\'111\'1112', "5153154'111'1112", 12)
pr('J.输入狗娘养的完整分词35335251\'5314511534\'431113432\'32511354', "35335251'5314511534'431113432'32511354", 12)
pr('K.输入我\'们完整(带6=分词的常规输入)', "31215'32425", 12)
io.write('\n=========== 深度验证 ===========\n')
-- 检查持久化内容
for _, f in ipairs({'bg5-learning.user.tsv','bg5-learning.words.tsv'}) do
  io.write('-- '..f..' --\n')
  local h=io.open('/tmp/bg5-test-user/'..f,'r')
  if h then io.write(h:read('*a') or '', '\n'); h:close() end
end
-- 验证"3"完整输出中学习词位置（不过滤）
pr('L.输入3完整候选(含学习词)', '3', 60)
-- 验证完整笔顺我们学习：模拟提交我们(分词)后
learning.add('我们', env)
pr('M.学习我们后输入31215(我们首字前缀)', '31215', 10)
pr('N.学习我们后输入31215\'32425', "31215'32425", 10)
-- 输入错误笔顺/无候选：优雅降级
pr('O.错误笔顺99999', '99999', 10)
pr('P.空输入', '', 10)
