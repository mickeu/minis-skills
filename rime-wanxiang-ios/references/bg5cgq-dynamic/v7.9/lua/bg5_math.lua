-- 独立数学表达式解析器；不执行输入中的 Lua 代码。
-- 参考：Lua 5.4 数学库与运算优先级手册；2026-10-15。
local M = {}
local unpack_ = table.unpack or unpack
local function fail(message, incomplete)
  error({message=message, incomplete=not not incomplete}, 0)
end
local function real(x)
  if type(x) ~= 'number' or x ~= x or math.abs(x) == math.huge then
    fail('结果不在有限实数范围')
  end
  return x
end
local function num(x) if type(x)~='number' then fail('此运算需要数字') end; return x end
local function integer(x)
  num(x); if x~=math.floor(x) or math.abs(x)>9007199254740991 then fail('需要可精确表示的整数') end
  return x
end
local function fact(x)
  integer(x); if x<0 or x>170 then fail('阶乘参数范围为0到170') end
  local r=1; for i=2,x do r=r*i end; return r
end
local function gcd(a,b)
  a,b=math.abs(integer(a)),math.abs(integer(b))
  while b~=0 do a,b=b,a%b end; return a
end
local function root(x,n)
  n=n or 2; num(x); num(n); if n==0 then fail('根指数不能为零') end
  if x<0 then
    if n~=math.floor(n) or n%2==0 then fail('负数不能开偶次实数根') end
    return real(-((-x)^(1/n)))
  end
  return real(x^(1/n))
end
local function sum(...)
  local a={...}; if #a==0 then fail('至少需要一个参数') end
  local r=0; for _,v in ipairs(a) do r=r+num(v) end; return real(r)
end
local function variance(...)
  local a={...};local mean=sum(...)/#a;local r=0
  for _,v in ipairs(a) do r=r+(v-mean)^2 end;return r/#a
end
local function comb(n,r,perm)
  integer(n);integer(r);if n<0 or r<0 or r>n or n>100000 then fail('排列组合参数范围错误') end
  if not perm then r=math.min(r,n-r) end
  if r>1000 then fail('排列组合参数过大') end
  local v=1;for i=1,r do v=real(v*(n-i+1)/(perm and 1 or i)) end;return v
end
local functions={}
local function reg(name,minargs,maxargs,fn)
  functions[name]=function(args)
    if #args<minargs or #args>maxargs then fail(name..'参数数量错误') end
    for _,v in ipairs(args) do num(v) end
    return real(fn(unpack_(args)))
  end
end
reg('sqrt',1,1,function(x) if x<0 then fail('平方根参数不能为负数') end;return math.sqrt(x) end)
reg('cbrt',1,1,function(x) return root(x,3) end)
reg('root',2,2,root);reg('pow',2,2,function(x,n)return x^n end)
reg('abs',1,1,math.abs);reg('floor',1,1,math.floor);reg('ceil',1,1,math.ceil)
reg('exp',1,1,math.exp)
reg('ln',1,1,function(x)if x<=0 then fail('对数参数必须大于零') end;return math.log(x) end)
reg('log',1,2,function(x,b)if x<=0 or b and (b<=0 or b==1) then fail('对数参数错误') end;return math.log(x)/(b and math.log(b) or 1) end)
reg('log10',1,1,function(x)if x<=0 then fail('对数参数必须大于零') end;return math.log(x)/math.log(10) end)
for _,name in ipairs({'sin','cos','tan','asin','acos'}) do reg(name,1,1,math[name]) end
reg('atan',1,2,function(y,x)if x then return math.atan(y,x) end;return math.atan(y) end)
reg('atan2',2,2,function(y,x)return math.atan(y,x) end)
reg('sinh',1,1,function(x)return (math.exp(x)-math.exp(-x))/2 end)
reg('cosh',1,1,function(x)return (math.exp(x)+math.exp(-x))/2 end)
reg('tanh',1,1,function(x)if x>350 then return 1 elseif x< -350 then return -1 end;local v=math.exp(2*x);return (v-1)/(v+1) end)
reg('deg',1,1,math.deg);reg('rad',1,1,math.rad)
reg('round',1,2,function(x,n)n=n or 0;integer(n);if math.abs(n)>15 then fail('舍入位数范围为-15到15')end;local q=10^n;return (x<0 and math.ceil(x*q-.5) or math.floor(x*q+.5))/q end)
reg('min',1,64,math.min);reg('max',1,64,math.max)
reg('sum',1,64,sum);reg('avg',1,64,function(...)local a={...};return sum(...)/#a end)
reg('var',1,64,variance);reg('std',1,64,function(...)return math.sqrt(variance(...))end)
reg('fact',1,1,fact);reg('factorial',1,1,fact)
reg('ncr',2,2,function(n,r)return comb(n,r,false) end)
reg('npr',2,2,function(n,r)return comb(n,r,true) end)
reg('gcd',2,2,gcd)
reg('lcm',2,2,function(a,b)if a==0 or b==0 then return 0 end;return math.abs(integer(a)/gcd(a,b)*integer(b)) end)
reg('mod',2,2,function(a,b)if b==0 then fail('模除数不能为零')end;return a%b end)
reg('recip',1,1,function(x)if x==0 then fail('零没有倒数')end;return 1/x end)
reg('hypot',2,2,function(x,y)return math.sqrt(x*x+y*y)end)
local constants={pi=math.pi,e=math.exp(1),tau=2*math.pi}
local replacements={['×']='*',['÷']='/',['−']='-',['＋']='+',['％']='%',
 ['（']='(',['）']=')',['．']='.',['，']=',',['π']='pi',['√']='@',
 ['²']='~2',['³']='~3',['‰']='~p',['≤']='<=',['≥']='>=',['≠']='!=',
 ['＝']='==',['∛']='~r',['°']='~d',['［']='(',['］']=')'}
function M.normalize(s)
  s=s:gsub('×','*'):gsub('÷','/'):gsub('−','-'):gsub('＋','+')
    :gsub('％','%%'):gsub('²','~2'):gsub('³','~3')
    :gsub('π','pi'):gsub('≤','<='):gsub('≥','>='):gsub('≠','!=')
    :gsub('＝','='):gsub('．','.'):gsub('，',','):gsub('（','('):gsub('）',')')
    :gsub('√','@'):gsub('∛','~r'):gsub('‰','~p'):gsub('°','~d')
  return s
end
function M.display(s)
  return s:gsub('~2','²'):gsub('~3','³'):gsub('~p','‰'):gsub('~r','∛'):gsub('~d','°'):gsub('@','√')
end
local function lex(s)
  local t,i={},1
  local function add(k,v) t[#t+1]={k=k,v=v};if #t>256 then fail('表达式过长') end end
  while i<=#s do
    local c=s:sub(i,i);local rest=s:sub(i)
    if c:match('%s') then i=i+1
    elseif c:match('%d') or c=='.' then
      local raw=rest:match('^%d+%.?%d*') or rest:match('^%.%d+')
      if not raw then fail('小数尚未输入完整',c=='.' and #rest==1)end
      local n=i+#raw
      if s:sub(n,n):lower()=='e' then
        local exp=s:sub(n):match('^[eE][+-]?%d+')
        if exp then raw=raw..exp end
      end
      add('n',real(tonumber(raw)));i=i+#raw
    elseif c:match('[A-Za-z_]') then
      local word=rest:match('^[A-Za-z_][A-Za-z_0-9]*');add('id',word:lower());i=i+#word
    else
      local two=s:sub(i,i+1)
      if two=='<=' or two=='>=' or two=='==' or two=='!=' or two=='~=' or two=='~2' or two=='~3' or two=='~p' or two=='~d' or two=='~r' or two=='//' then
        add('op',two);i=i+2
      elseif c:match('[+%-*/^%%!<>=(),@]') then add('op',c);i=i+1
      else fail('不支持的字符：'..c,c=='~' and i==#s)end
    end
  end
  add('eof','');return t
end
local function parse(tokens)
  local p,depth=1,0
  local function peek()return tokens[p].v end
  local function take()local x=tokens[p];p=p+1;return x end
  local expression
  local function expect(v)
    if peek()~=v then fail('需要 '..v,tokens[p].k=='eof')end;take()
  end
  local function call(name)
    local fn=functions[name]
    if not fn then fail('未知函数：'..name)end
    expect('(');local args={}
    if peek()~=')' then
      while true do
        args[#args+1]=expression(0)
        if #args>64 then fail('函数参数过多')end
        if peek()~=',' then break end;take()
      end
    end
    expect(')');return fn(args)
  end
  local function primary()
    local x=take()
    if x.k=='n' then return x.v end
    if x.k=='id' then
      if functions[x.v] then return call(x.v)end
      if constants[x.v] then return constants[x.v]end
      fail('未知常量或函数：'..x.v)
    end
    if x.v=='(' then local v=expression(0);expect(')');return v end
    if x.v=='+' then return num(expression(25))end
    if x.v=='-' then return -num(expression(25))end
    if x.v=='@' then return root(num(expression(25)),2)end
    if x.v=='~r' then return root(num(expression(25)),3)end
    fail('缺少操作数',x.k=='eof')
  end
  local precedence={['+']=10,['-']=10,['*']=20,['/']=20,['//']=20,['^']=30,
    ['<']=5,['>']=5,['<=']=5,['>=']=5,['!=']=5,['~=']=5,['==']=5,['=']=5}
  local postfix={['!']=true,['%']=true,['~p']=true,['~2']=true,['~3']=true,['~d']=true}
  expression=function(minbp)
    depth=depth+1;if depth>64 then fail('括号或运算嵌套过深')end
    local left=primary()
    while true do
      local op=peek()
      if postfix[op] and 40>=minbp then
        take();num(left)
        if op=='!' then left=fact(left)
        elseif op=='%' then left=left/100
        elseif op=='~p' then left=left/1000
        elseif op=='~d' then left=left*math.pi/180
        else left=real(left^(op=='~2' and 2 or 3))end
      else
        local implicit=false;local bp=precedence[op]
        local nextkind=tokens[p].k
        local prev=tokens[p-1] and tokens[p-1].v
        if not bp and (nextkind=='id' or op=='(' or op=='@' or op=='~r'
           or nextkind=='n' and prev==')') then
          implicit=true;op='*';bp=20
        end
        if not bp or bp<minbp then break end
        if not implicit then take()end
        local right=expression(op=='^' and bp or bp+1)
        if op=='=' or op=='==' then left=left==right
        elseif op=='!=' or op=='~=' then left=left~=right
        else
          num(left);num(right)
          if op=='<' then left=left<right
          elseif op=='>' then left=left>right
          elseif op=='<=' then left=left<=right
          elseif op=='>=' then left=left>=right
          elseif op=='+' then left=real(left+right)
          elseif op=='-' then left=real(left-right)
          elseif op=='*' then left=real(left*right)
          elseif op=='/' then if right==0 then fail('除数不能为零')end;left=real(left/right)
          elseif op=='//' then if right==0 then fail('除数不能为零')end;left=math.floor(left/right)
          elseif op=='^' then left=real(left^right)end
        end
      end
    end
    depth=depth-1;return left
  end
  local value=expression(0)
  if tokens[p].k~='eof' then fail('表达式含多余内容')end
  return value
end
function M.format(value)
  if type(value)=='boolean' then return value and 'true' or 'false' end
  real(value);if value==0 then return '0' end
  return string.format('%.14g',value)
end
function M.evaluate(source)
  if type(source)~='string' then return {ok=false,error='表达式类型错误'}end
  if #source>1024 then return {ok=false,error='表达式过长'}end
  if source:match('^%s*$') then return {ok=false,error='请输入算式',incomplete=true}end
  local ok,value=pcall(function()return parse(lex(M.normalize(source)))end)
  if not ok then
    if type(value)=='table' then return {ok=false,error=value.message,incomplete=value.incomplete}end
    return {ok=false,error='表达式错误',incomplete=false}
  end
  return {ok=true,value=value,text=M.format(value)}
end
return M
