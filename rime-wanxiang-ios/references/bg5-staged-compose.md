# BG5CGQ 分段造词：元书真机成功经验

记录日期：2026-10-14。用户确认：BG5CGQ learning **v7.0「造词完美通过」**。这是用户真机验收结论，不是助手直接操作 iOS 的结果；未明确确认的其他功能不能据此推定全部完美。

## 1. 成功基线（勿覆盖）

- 交付包：`/var/minis/workspace/bg5-learning/BG5CGQ-learning-v7.0.zip`
- SHA-256：`a65e80d12c46e36b1e9aaf09ef60fdd6b7497c3d9f2322a5605d39bbc0d4b606`
- 开发目录：`/var/minis/workspace/bg5-learning/package/`
- 主文件：`lua/segment_phrase.lua`、`lua/filter_seg_count.lua`、`lua/learning.lua`。
- 方案：`stroke_bg5cgq_learning.schema.yaml`；schema/dict 版本均为 `7.0`。
- 包结构直接对齐方案目录根层，不多套一层目录；不含测试 `bg5-learning.user.tsv`。
- 后续修改先备份/对比这个 zip 的成功基线；开发目录会变化，不可假定它永远等于成功包。

## 2. 用户定义的交互契约

1. 一次 composition 输入多段笔画，用 `'` 分隔。
2. 前段只要能成词，就必须保留；**短码成词也有效，不要求全码**。
3. 即使整串碰巧命中长词，不能提前 return，吞掉前段成型词和后段候选。
4. 前段词只消费自身编码及其后的分隔符，不消费后段笔画。
5. 后段能成词时保留后段词；不能成词时按该段编码检索单字，复用单打字的权重逻辑，并优先显示。
6. 已造好的词最终点选应干净提交到输入框；不能在文字后面拖着未消费的笔画。
7. 单笔画、既有偏旁、部首在匹配编码下优先，普通字词频不能把它们挤掉。优化不得擅自改变此规则。
8. 相同文字出现在不同分段位置时，必须保留不同范围的候选。
9. 空候选、错尾、连续分隔符等要有安全回退，不能让数字泄漏到候选或预编辑显示。

例子不是限定词表：`我要+国`、`苹果+车`、`吃饭+去了`、三字前段词+后字，都遵循同一原则。

## 3. 三个核心修复

### 3.1 Candidate.end 是右开区间，消费后置分隔符

`31'12'25112141`：

```text
我要  [0,6)
国    [6,14)
```

全码 `3121534'125221531'25112141`：

```text
我要  [0,18)
国    [18,26)
```

旧测试认为前段 `_end=5/17` 才不吃后段，这是错误验收标准：它留下 `'` 作为续段开头。当前 schema 中 `'` 是 alphabet 字符、delimiter 是空格，消费后置分隔符可让余段直接从笔画开始。

实现：求出当前字编码末尾的右开位置 `e`；若 `raw_input:sub(e+1,e+1)=="'"`，令 `e=e+1`。相邻后段 `start == 前段 end`，不是 `>`。

注意：右开语义本身不意味着每个 Rime 方案都必须吞分隔符；这是当前 BG5 alphabet/分段约定下验证成功的做法。

### 3.2 preedit 和 filter 都必须尊重候选局部范围

旧 translator 和 filter 给每个候选写整串输入的 preedit，局部候选会显示不属于自身的笔画。translator 设置局部 preedit 还不够：filter 重建 Candidate 时必须同样处理，不能再次写回整串。

当 raw 是完整 context.input、start/end 为绝对字节范围时：

```lua
local local_input = raw:sub(cand.start + 1, cand._end)
-- 再把 1..5 转成一丨丿丶乛；分隔符保留
```

不能把局部 raw 当作完整 context.input 按绝对偏移切片。续选 `seg.start > 0` 要专项验证；v7.0 用户的成功反馈不等于全部非零偏移用例已有自动化证明。

filter 不再按整串段数强制要求每个候选具有整串字数：应根据 Candidate 覆盖的子串计算有效段数，**先去掉子串末尾已消费的分隔符**，防止两字词误判为三段。

### 3.3 去重必须包含范围

不要只用 `added[cand_text]`。使用 `type + start + end + text` 作为去重键。`一'一` 等同字不同位置不能互相误删。

只修 Lua 层去重不代表后续 `uniquifier` 一定保留不同范围；今后对同字续选继续检查整个过滤链及真机结果。

## 4. 部件优先不能靠“大词频”模拟

- 旧方案给部首 8,000,000 权重，但普通高频字可超过 60,000,000；因此提升频率不是稳定优先规则。
- 旧 `STROKE_SYMBOLS` 还取消单笔画 exact 优先、安排“第六位”，违反用户要求。
- 当前使用明确 `PRIORITY_COMPONENTS` 类别：匹配部件先于普通汉字，同类内部再按 exact/学习频次/原排序。
- 普通与通配分支都要执行类别优先；部件独立注入，不受普通字 `MAX_PREFIX` 截断影响。
- 不再任意新增“高频字更重要”“笔画符号应该降权”的产品假设。

## 5. 验收层次与可复用命令

```bash
cd /var/minis/workspace/bg5-learning
luac5.4 -p package/lua/*.lua
python3 tests/test_static.py
lua5.4 tests/test_components.lua package/lua
lua5.4 tests/audit_wrong_tail.lua package/lua
lua5.4 tests/test_staged_compose.lua
lua5.4 tests/test_random_staged.lua
```

v7.0 主流程结果：部件前缀 144 项＋通配 5 项通过；错尾 15,620 组 `empty=0 dirty=0 errors=0`；造词模拟 4/4、8/8；压缩双字索引 28,049 项 `missing=0 extra=0 dup=0`。

必须额外核验 translator→filter：前段短词、后段字、局部 preedit、候选范围都保留。只有 translator 列表通过不足以验收。

**候选对象模拟、字符串暂存拼接、commit notifier 模拟，都不能证明真实点击成功。** 必须真机确认：输入→点前段词→后段编码保留→点后段字/词→提交仅有目标文字→无残留笔画。用户对 v7.0 已给出造词成功确认。

Alpine librime 1.12.0 不包含 Hamster 的 Lua 插件；直接运行本方案得到 N=0 是测试环境不支持，不能算产品测试。读取原生源码只能确认语义，不能替代 Hamster 端到端验收。

## 6. 性能优化的纪律与反例

- 不能用短码首字词桶“前30”截断换速度：曾把 `我要` 等合法短码词漏掉；应扫描有效匹配范围，或建立完整可校验索引。
- `pair_prefix_index` 按首字＋次字1/2笔建索引；低频首字回退完整桶；通配不能直接查询字面键 `1?`，首笔确定可借首笔桶再验证，其余回退完整桶。
- 全量常驻索引曾额外耗约7.64 MiB；压缩后 Lua 约60 MiB。该内存数字是 Lua 堆，不是 iOS 进程 RSS，更不能宣称“最优”。
- 先匹配再排序，避免对无关整桶排序；Top120堆筛选必须与完整排序结果比对，尤其同频候选要关注稳定性。
- 一次首次查询、重复热查询、require加载要分开测；不同输入多轮测试，不把整进程耗时当按键延迟。
- 达到缓存上限清空整表不是 LRU；不能用最终结果上限推导扫描耗时有上限。
- 造词正确性优先于优化；真机失败时停止性能微调，先修实际提交闭环。
- 子代理只串行、任务窄、固定源码指纹；超时和部分报告不算完整通过。最终修改后旧报告无效。
- 测试学习库必须隔离；交付时排除测试 user.tsv，不删除用户真实词库。

## 7. 参考资料（来源）

- **第一手验证**：2026-10-14 用户在本次对话确认「造词完美通过，把这次的经验沉淀」，对应 v7.0 包及上文 SHA-256；属于用户报告的元书真机成功。
- **本地实现与测试**：`/var/minis/workspace/bg5-learning/package/lua/{segment_phrase,filter_seg_count,learning}.lua`；`tests/test_components.lua`、`tests/test_random_staged.lua`、`tests/test_staged_compose.lua`、`tests/audit_wrong_tail.lua`。成功快照以 v7.0 zip 为准。
- **上游笔画方案**：https://github.com/zny05/BG5CGQ-Stroke-Rime ，调研基线 commit `181f10fb85c621cdf6ea69012b3ff3bf22e55f28`；本次动态造词为本地衍生实现，不是上游原生功能声明。
- **Rime 1.12.0 Candidate 范围**：https://github.com/rime/librime/blob/1.12.0/src/rime/candidate.h ，`start/end` 明确为 `[start,end)`。
- **Rime 分段关闭**：https://github.com/rime/librime/blob/1.12.0/src/rime/segmentation.cc ，`Segment::Close()` 对部分候选缩短分段到 cand.end。
- **Rime 选择与提交**：https://github.com/rime/librime/blob/1.12.0/src/rime/engine.cc ，`ConcreteEngine::OnSelect()` 推进分段并判断是否到 input.length；https://github.com/rime/librime/blob/1.12.0/src/rime/composition.cc ，`GetPreedit/GetScriptText/GetCommitText`。
- **Rime abc segmentor**：https://github.com/rime/librime/blob/1.12.0/src/rime/gear/abc_segmentor.cc 。
- **Hamster 前端**：https://github.com/ihsiao/Hamster ，本地参考 `/tmp/hamster-src/Packages/HamsterKeyboardKit/Sources/RimeContext/RimeContext.swift` 和 `Packages/RimeKit/Sources/ObjC/irime_api.m`；该仓库是参考链，不能假定其代码与用户当前 Hamster3 构建逐字相同。
- **元书前端资料**：https://github.com/amzxyz/rime-wanxiang/blob/main/docs/doc/hamster3.md ；https://github.com/BlackCCCat/ResourceforHamster 。

记录/整理：2026-10-14。Rime 原生源码版本：1.12.0；验证交付版本：BG5CGQ learning 7.0。没有真机耗时/RSS实测，不把 iSH 性能数字当作元书真机指标。
