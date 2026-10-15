-- 更新时间：2026.10.15 10:55
-- 先于default与笔画的6/-/=绑定处理V计算输入，普通笔画全部放行。
local M={}
local accepted,noop=1,2
local function commit(env)
  local ctx=env.engine.context
  local expr=(ctx.input or ''):sub(#env.prefix+1)
  local result=env.math.evaluate(expr)
  if not result.ok then
    ctx:set_property('bg5_calc_error',result.error or '表达式未完成')
    return accepted
  end
  ctx:set_property('bg5_calc_committing','1')
  env.engine:commit_text(result.text)
  ctx:clear()
  ctx:set_property('bg5_calc_committing','')
  return accepted
end
function M.init(env)
  env.prefix=env.engine.schema.config:get_string('calculator/trigger') or 'V'
  env.math=require('bg5_math')
  local wx=require('wanxiang.super_calculator')
  env.math.set_provider(wx.methods,wx.descriptions)
end
function M.func(key,env)
  if key:release() or key:ctrl() or key:alt() or key:super() then return noop end
  local ctx=env.engine.context
  local input=ctx.input or ''
  local code=key.keycode
  local active=input:sub(1,#env.prefix)==env.prefix
  if code==string.byte(env.prefix) then
    if not active then
      if input~='' then
        if ctx:has_menu() then ctx:commit() else return accepted end
      end
      ctx:push_input(env.prefix)
    end
    return accepted
  end
  if not active then return noop end
  if code==0xff0d or code==0xff8d or code==32 then return commit(env) end
  if code==0xff1b then ctx:clear();return accepted end
  if code==0xff08 then
    if #input<=#env.prefix then ctx:clear()
    elseif ctx.caret_pos==#input and input:match('~[23pdr]$') then ctx:pop_input(2)
    else ctx:pop_input(1) end
    return accepted
  end
  if code==0xffff then ctx:delete_input(1);return accepted end
  if code==0xff51 then ctx.caret_pos=math.max(#env.prefix,ctx.caret_pos-1);return accepted end
  if code==0xff53 then ctx.caret_pos=math.min(#input,ctx.caret_pos+1);return accepted end
  if code==0xff50 then ctx.caret_pos=#env.prefix;return accepted end
  if code==0xff57 then ctx.caret_pos=#input;return accepted end
  if code>=33 and code<=126 then
    if #input<1024 then
      ctx:set_property('bg5_calc_error','')
      ctx:push_input(string.char(code))
    end
    return accepted
  end
  return noop
end
return M
