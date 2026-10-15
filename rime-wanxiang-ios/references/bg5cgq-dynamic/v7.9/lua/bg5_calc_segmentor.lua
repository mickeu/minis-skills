-- 整条算式保留为一个calculator segment，不参与笔画分段。
return function(segmentation,env)
  local text=segmentation.input
  if not text or text:sub(1,1)~='V' then return true end
  if segmentation:get_current_start_position()~=0 then return false end
  local seg=Segment(0,#text)
  seg.tags=Set({'calculator'})
  segmentation:add_segment(seg)
  return false
end
