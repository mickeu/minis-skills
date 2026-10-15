-- 计算结果只在V模式出现；错误算式不产生可上屏的伪结果。
local M={}
function M.init(env)
  env.math=require('bg5_math')
end
function M.func(input,seg,env)
  if not input or input:sub(1,1)~='V' then return end
  local expr=input:sub(2)
  local display=env.math.display(expr)
  local r=env.math.evaluate(expr)
  if not r.ok then return end
  local c=Candidate('calculator',seg.start,seg._end,r.text,' = '..display)
  c.quality=1000000;c.preedit=display;yield(c)
  if expr~='' then
    local c2=Candidate('calculator_expression',seg.start,seg._end,display..'='..r.text,'算式与结果')
    c2.quality=999999;c2.preedit=display;yield(c2)
  end
end
return M
