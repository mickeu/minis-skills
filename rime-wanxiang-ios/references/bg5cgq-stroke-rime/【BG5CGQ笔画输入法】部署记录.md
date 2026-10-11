# 【BG5CGQ笔画输入法】iPhone 部署记录

> 部署日期: 2026-08-25
> 目标: App Store 版「仓输入法」(iPhone, WiFi文件管理 http://10.1.1.147)

---

## 六、v2 功能升级 (2026-08-25 晚)

笔画输入验证通过后，新增 5 项功能：

### 功能实现一览

| # | 需求 | 实现方式 | 状态 |
|---|------|---------|------|
| 1 | 上划出数字 | swipe up + `processByRIME: true`：有候选时选第N候选，无编码时数字上屏 | ✅ 已部署 |
| 2 | 下划出符号 | swipe down + `processByRIME: false`：符号直接上屏（1@ 2# 3$ 4% 5& 6* 7+ 8- 9/） | ✅ 已部署 |
| 3 | 动态词频 | schema 启用 `enable_user_dict: true` + `userdb`，Rime 自动记录选字频率调频 | ✅ 已部署 |
| 4 | 词组联想 | 新增 `stroke_bg5cgq_words.dict.yaml`（5,394 条简体二字词），`table_translator@words` 挂载 | ✅ 已部署 |
| 5 | 编码区显示笔画图形 | `preedit_format: [xlit/12345/一丨丿丶乛/]`，编码区数字实时转笔画图形 | ✅ 已部署 |

### 功能 1 设计细节：上划数字的双态行为

```
有候选时: 上划数字 → Rime selector 默认行为 → 选择第 N 个候选
无编码时: 上划数字 → processKey 失败 → insertTextPatch → 数字直接上屏
```
与百度输入法行为一致，一举两得。

### 功能 4 设计细节：词组联想

- **编码规则**：字1前4笔 + 分词符(`) + 字2前4笔，如 `我们 = 3121'3242`
- **触发方式**：输入字1笔画 → 按分词键(6) → 输入字2笔画 → 候选栏显示词组
- **数据来源**：维基语料二字词，简体过滤，频次≥3000，共 5,394 条
- **冲突处理**：同码词组按频次排序（"就是"优先），冲突率 23% 无碍使用
- **优先级**：`initial_quality: 100` 使词组在候选栏优先展示

### 功能 5 说明

按键 label 本就是笔画图形（一丨丿丶乛）；本项将**编码区**的数字编码也实时转换为笔画图形：
输入 `31215` → 编码区显示 `丿一丨一丿`，分词符 `'` 和通配 `?` 保持原样。

### 部署文件清单（v2）

| 文件 | 大小 | 变更 |
|------|------|------|
| Rime/stroke_bg5cgq.schema.yaml | 2,759 B | +words 翻译器 +preedit_format +user_dict |
| Rime/stroke_bg5cgq_words.dict.yaml | 119,401 B | 新增词组库 |
| Rime/hamster.yaml | 62,798 B | +18 处 swipe 划动配置 |

### 手机端操作

1. 重新部署（会编译词组库生成 `stroke_bg5cgq_words.table.bin`）
2. 测试要点：
   - 上划「一」键：无编码时输入 `1`；先输 `2512` 出候选后上划 `2` → 选第2候选
   - 下划「一」键：直接输入 `@`
   - 输入 `3121` + 分词键 + `3242` → 候选出现「我们」
   - 编码区显示笔画图形而非数字

---

## 七、v3 问题修复 (2026-08-26)

v2 部署后实测反馈 6 个问题，根因分析与修复：

| # | 问题 | 根因 | 修复 |
|---|------|------|------|
| 1 | 下划符号 ✓ | — | 正常 |
| 2 | 上划数字无效 | `KeySwipe.processByRIME` 默认 `false`（走 insertSymbol 直接上屏）；我们显式设 `true` 走 rime processKey，数字被引擎吞掉 | 上划数字改 `processByRIME: false`（与内置仓颉键盘行为一致） |
| 3 | 中英切换无效 | `#中英切换` 只切换 rime 的 ascii_mode（编码模式），不切换键盘布局 | 改为 `keyboardType(alphabetic)` 切换到英文26键；英文键盘底部「中」键可切回 |
| 4 | 词组联想无效 | **librime 部署任务只编译主 translator 的词典**，命名翻译器 `table_translator@words` 的词典不自动编译（日志证实：只有 `preparing dictionary 'stroke_bg5cgq'`，无 words） | 词组直接合并进主码表 `stroke_bg5cgq.dict.yaml` |
| 5 | 空格名"BG5CGQ笔画输入" | 空格显示的是 rime schema 的 `name` 字段 | schema `name` 改为「BG5CGQ笔画」 |
| 6 | 分词键无效 | 同 #4（词组库未编译，编码含 `'` 无词组可匹配） | 同 #4；另确认 `'` 在 alphabet 中可进入编码区，rime 按 key 精确匹配 |

### 词组库 v2 重建

初次提取时「我们」等高频词被简体过滤规则误杀（维基语料存的是繁体「我們」）。改为**先繁简转换再统计**：

- 词组数：5,394 → **7,257** 条
- Top10：就是、一个、但是、这个、所以、可以、我们、因为、如果、自己
- 编码规则不变：字1前4笔 + `'` + 字2前4笔（如 我们=`3121'3242`，你好=`3235'5315`）

### 其他调整

- 删除废弃的 `stroke_bg5cgq_words.dict.yaml`
- schema `max_phrase_length: 2`（配合 enable_sentence 连续组词）
- 移除无效的 `table_translator@words` 配置

### v3 部署清单

| 文件 | 大小 | 校验 |
|------|------|------|
| stroke_bg5cgq.schema.yaml | 2.2KB | ✓ |
| stroke_bg5cgq.dict.yaml（含7257词组） | 1139KB | ✓ |
| hamster.yaml（v4 布局） | 61KB | ✓ |

### 待验证

1. 重新部署（主码表变更会触发重编译，需等待编译完成）
2. 上划数字直接上屏
3. 「中英」键切换英文26键 ↔ 底部「中」键切回
4. 输入 `3235` + 分词键 + `5315` → 候选出现「你好」
5. 空格键显示「BG5CGQ笔画」
6. 连续联想：选「你好」后继续输入下一词编码

---

## 八、v4 词组增强与键位修正 (2026-08-26)

### 实测反馈与处理

| # | 反馈 | 处理 |
|---|------|------|
| 1 | 二字分词出词 ✓ | 正常（`3235'5315`→你好 已验证） |
| 2 | 多字连续分词缺失 | 词库扩充 3/4 字词 |
| 3 | 词组调频 | Rime userdb 原生支持（已启用 `enable_user_dict`），选词后自动记录，无需额外开发 |
| 4 | 部分编码输入 | `enable_completion` 前缀匹配已支持（如输 `3235'53` 即可出「你好」） |
| 5 | 上划数字键位错乱 | v4 布局把 6-9 放在了通配/，/。/符号键上划；v5 改为与键位序号对齐 |
| 6 | 下划符号调整 | 按新映射表重配 |

### 词组库 v3：opencc 全量转换（10,996 条）

用 opencc-js 完整繁简转换替代手工映射表，修复「選擇/雖然/問題」等繁体词漏转问题：

| 词长 | 条数 | 频次门槛 | 编码规则 |
|------|------|---------|---------|
| 2 字 | 7,156 | ≥3000 | 字1前4笔 `'` 字2前4笔 |
| 3 字 | 3,294 | ≥2000 | 每字前4笔，`'` 分隔 |
| 4 字 | 546 | ≥3000 | 每字前4笔，`'` 分隔 |

多字连续分词：`4354'3212'354` → 为什么；`525'4125'2511'4543` → 也就是说。
部分编码：`enable_completion` 前缀匹配，每字可只输部分笔画。
词组调频：选词后 Rime userdb 自动记录（首次选词生成 `stroke_bg5cgq.userdb`）。

### 键位修正 (v5 布局)

**上划数字**（与键位序号对齐）：

| 键 | 一 | 丨 | 丿 | 丶 | 乛 | 分词 | 通配 | ， | 。 | 符号 |
|----|----|----|----|----|----|------|------|----|----|------|
| 上划 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |

**下划符号**：

| 键 | 一 | 丨 | 丿 | 丶 | 乛 | 分词 | 通配 | ， | 。 |
|----|----|----|----|----|----|------|------|----|----|
| 下划 | @ | ： | / | ！ | （ | ） | " | - | _ |

### v4 部署清单

| 文件 | 大小 | 校验 |
|------|------|------|
| stroke_bg5cgq.dict.yaml（10,996 词组） | 1251KB | ✓ |
| hamster.yaml（v5 布局） | 61KB | ✓ |

### 待验证

1. 重新部署（主码表重编译，等待完成）
2. 上划数字 1-0 与键位对齐
3. 下划符号按新表
4. 三字词：`4354` + 分词 + `3212` + 分词 + `354` → 为什么
5. 部分编码：`3235` + 分词 + `53` → 你好（前缀匹配）
6. 词组调频：选「你好」几次后，再次输入时排序提升

---

## 九、v6 联想与调频深度分析 (2026-08-26)

### librime-predict 源码分析结论

**机制**（https://github.com/rime/librime-petect）：
- `predictor`（processor）：监听上屏事件，用 `commit_history` 最后一词查 predict.db
- `predict_translator`（translator）：把联想候选注入候选栏
- `predict.db`：DoubleArray Trie 二进制库（key=上屏词, value=候选词列表+权重），由 `tools/make_predict_data`（Rust）从词频语料生成
- 触发条件：`prediction` switch 开启 + 上屏词类型非 punct/raw/thru

**关键事实——AppStore 版 Hamster 未编译该插件**：

手机日志（`RIMELogger/rime.hamster.INFO`）注册组件完整列表中：
- ❌ 无 `predictor`、无 `predict_translator`
- 仅加载 core/dict/gears 三个内置 module

→ **schema 里配 `predictor` 不会生效**（未知组件被忽略）。联想功能需要 LibrimeKit 编译 librime 时加入 `-DRIME_PLUGINS=librime-predict`，属于 App 层变更，只能等官方版本更新（或自签编译）。

v6 schema 已做**前瞻性预留**：`prediction` switch、注释掉的 `predictor`/`predict_translator` 配置块，未来 App 支持后取消注释即用。

### 动态词频调整（已可用，无需插件）

librime 内置 userdb 机制（源码验证 `table_translator.cc` Memorize → `user_dictionary.cc` UpdateEntry）：

```
选字/选词上屏 → UpdateEntry(编码+词, commits+1, formula_d 衰减累积)
下次输入同码 → userdb LookupWords 前缀命中 → 权重参与排序
```

- 单字调频 ✓（选「你」几次后，输 3235 时「你」排前）
- 码表词组调频 ✓（custom_code 含分词符，userdb key 前缀匹配）
- 造词 ✓（v6 新增 `enable_encoder + encode_commit_history + max_phrase_length: 4`：连续上屏的词自动组合成新词记录，如连续选「你好」「吗」→ 记录「你好吗」）

**注意**：`stroke_bg5cgq.userdb` 在**首次选词后**才生成——目前手机上还没有此目录属正常现象。

### 词组联想的当前替代

AppStore 版可用的"类联想"能力（无需插件）：
1. **部分编码连续分词**：`3235` + 分词 + `53` → 你好（enable_completion 前缀匹配）
2. **连续上屏造词**：选过「你好」后，userdb 记录，下次 `3235'5315` 直接排前
3. **真·一词联想**（上屏「你」自动出「好」）：依赖 librime-predict 插件，AppStore 版暂不可用

### v6 部署清单

| 文件 | 变更 | 校验 |
|------|------|------|
| stroke_bg5cgq.schema.yaml | version 1.2；+prediction switch；+enable_encoder/encode_commit_history/max_phrase_length 4；+predictor 预留配置 | ✓ |

### 待验证

1. 重新部署（version 变更触发 schema 重载，table.bin 无变化不重编译，很快）
2. 单字调频：同一字连续选 2-3 次，再次输入观察排序
3. 词组调频：选「你好」后重输 `3235'5315` 观察排序
4. 造词：连续选「你好」+「吗」后，输入 `3235'5315'2525`（部分编码）看是否出现「你好吗」

---

## 十一、v10 键位修复：换行键 + 数字键盘布局 (2026-08-26)

### 变更清单

| # | 变更 | 验证 |
|---|------|------|
| 1 | **换行键**：`shortcutCommand sendKeys Return` → `enter` | ✓ |
| 2 | **数字键盘左侧**：新增 `*` `/` `+` 三键 | ✓ |
| 3 | **数字键盘右侧**：`.` → `-`，`@` → `=` | ✓ |

### 换行键修复说明

原配置用 `shortcutCommand sendKeys Return`（绕过 RIME 引擎直发 Return 键），在 iOS 键盘扩展中因候选态拦截而失效。改为 `enter`（标准 RIME primary action）后，走 `textDocumentProxy.insertText("\n")` 正常换行。

### 数字键盘布局 (numericNineGrid)

```
row0: *  1  2  3  backspace
row1: /  4  5  6  -
row2: +  7  8  9  =
row3: returnLastKeyboard  0  space  enter
```

### v10 部署清单

| 文件 | 大小 | 校验 |
|------|------|------|
| hamster.yaml（含 numericNineGrid 键盘） | 74KB | ✓ 一致 |

### 待验证

1. **重新部署**（触发 YAML 加载）
2. 笔画键盘 row1 右侧「换行」键 → 在输入框中按回车，应正常换行
3. 按「123」切换数字键盘 → 左侧出现 `*` `/` `+`，右侧 `.` 变 `-`，`@` 变 `=`
4. 数字键盘底部「换行」键 → 正常换行

---

## 十、v7 调频失效根因修复：码表频次归一化 (2026-08-26)

### 用户反馈

动态词频调整无任何效果——频繁选的字不会排到前面。

### 根因（librime 源码级量化分析）

不是"词频数据库基数太大干扰"，而是**量级碾压**：

```
librime 候选排序链路 (源码验证):
  MergedTranslation::Elect → Translation::Compare → Candidate::compare
  → 同位置候选按 quality 降序

quality 计算 (TableTranslation::Peek):
  码表候选  = exp(weight) + initial_quality
  userdb候选 = exp(weight) + initial_quality + 0.5 (user phrase 加成)

码表编译 (dict_compiler.cc:257):
  weight = log(码表中的频次值)
  → 我们存的是绝对频次 (一=429078)
  → weight = log(429078) = 12.97
  → quality = exp(12.97) = 429078 (!!)

userdb 候选 (user_dictionary.cc CreateDictEntry):
  weight = log(formula_p(commits/tick...))
  → 选 1~10 次: quality ≈ 1.5
```

**43 万 vs 1.5**——userdb 候选的 quality 被码表绝对频次完全碾压，选过的字永远排不到前面。这正是用户观察到的现象。

### 修复：码表频次归一化

将码表 weight 列从绝对频次改为**归一化概率** `freq/total`（总频次 2.334e8）：

| 字 | 原频次 | 归一化 weight | quality |
|----|--------|--------------|---------|
| 一 | 429078 | 5.80e-4 | ≈1.00058 |
| 你 | — | 4.17e-3 | ≈1.00417 |
| 我们 | — | 2.05e-3 | ≈1.00205 |

修复后量级：
- 码表候选 quality 全部落在 **1.0001~1.005**（字间相对顺序保持，概率单调）
- userdb 候选 quality ≈ **1.5**（+0.5 user phrase 加成）→ **稳超所有码表候选**
- userdb 段内部按 commits 权重排序（`SortRange` 按 entry weight）→ 选得越多越靠前

### v7 部署清单

| 文件 | 变更 | 校验 |
|------|------|------|
| stroke_bg5cgq.dict.yaml | 59262 条目频次全部归一化（绝对频次→概率） | ✓ 1881KB |

schema 无需变更（v6 的 `initial_quality: 1.0` 正好作为归一化后的基准值）。

### 待验证

1. **重新部署**（码表变更触发重编译 table.bin/prism.bin，约 1-2 分钟）
2. 单字调频：选「你」2-3 次 → 输 `3235`，「你」应排到候选前几名
3. 词组调频：选「我们」→ 输 `3121'3242`，「我们」应排前
4. 码表默认顺序不变：未选过的字仍按语料频率排序

### 遗留说明

- userdb 数据存于键盘扩展的 AppGroup 目录（`AppGroup/InputSchema/Rime/stroke_bg5cgq.userdb`），文件服务器（Documents）看不到，属正常
- 若调频仍无效，下一步排查方向：键盘扩展 `hasFullAccess` 状态（决定 userdb 写入 AppGroup 还是沙盒）

---

## 十一、v8 词组联想：librime-predict 完整启用 (2026-08-26)

### 关键信息修正

与 Hamster 开发者确认：**AppStore 版已编译 librime-predict 插件**（无须 Pro 版）。
之前"未内置"的判断源于日志截断（INFO 日志仅 4361 字节，组件注册列表不完整），予以纠正。

### librime-predict 深度分析（源码级）

**组件架构**（predict_module.cc 注册两个组件）：
- `predictor`（processor）：监听 `context->update_notifier`，上屏一词后用 `commit_history` 最后一词查库
- `predict_translator`（translator）：响应 `prediction` tag 的空段，输出联想候选

**触发条件**（predictor.cc OnContextUpdate）：
1. `prediction` switch 开启（schema 配 `reset: 1` 默认开启）
2. composition 为空（即刚上屏完）
3. 上屏类型非 punct/raw/thru（标点/原始输入不联想）
4. `max_iterations` 未超限（连续联想次数）

**数据格式**（predict_db.cc）：
- `predict.db`：MappedFile 二进制 = Metadata + Darts DoubleArray（key trie）+ StringTable（value trie）
- key = 上屏词（`$` 表示句首），value = 联想候选列表（按权重降序）
- 文本源格式：`key\t候选\t权重`（predict.txt，54.5 万行）

**配置要求**（官方 README）：
- `predictor` 必须在 `engine/processors` 中 `key_binder` 之前
- `predict_translator` 加到 `engine/translators`

### 部署内容

| 文件 | 说明 | 校验 |
|------|------|------|
| Rime/predict.db | 官方联想库 7,529,528B（rime/librime-predict release data-1.0，54.5万条 key→候选） | ✓ 字节一致 |
| stroke_bg5cgq.schema.yaml v1.3 | processors 首位加 `predictor`；translators 加 `predict_translator`；`prediction` switch（reset:1）；`predictor:` 配置块（db/max_candidates:9/max_iterations:1） | ✓ |

predict.db 数据特征：简繁混合语料（简体为主），覆盖 `我→的不要是`、`你→的不是說`、句首 `$→我第在不你` 等。

### 联想工作流（部署后）

```
输入 3235 → 选「你」上屏
  → predictor 查 predict.db[你] → 的/不/是/說...
  → 候选栏直接显示联想候选（无需输入编码）
  → 点选「的」上屏 → predictor 查 predict.db[的] → 人/时候/一...（连续联想, max_iterations:1 时停一次）
  → 按删除键 → 清除联想段
```

### 待验证

1. 重新部署（schema 变更触发重编译）
2. 输 `3235` 选「你」→ 候选栏应立即出现「的/不/是…」联想词
3. 点选联想词 → 继续出现下一轮联想
4. 删除键 → 联想清除，回到正常输入

### 已知限制与后续优化

- 官方 predict.db 为简繁混合语料，部分联想候选是繁体（說/機/個）
- 后续可用 essay.txt 词频自建简体纯净版 predict.db（需编译 build_predict 工具或实现 darts-clone 格式）
- `max_iterations: 1`：联想一轮后停止；改 `0` 为不限次数连续联想

---

## 十二、v8 联想未生效排查 (2026-08-26)

### 实测结果

- ✅ 动态词频调整已正常工作（v7 归一化修复生效）
- ❌ 词组联想仍未生效

### 排查过程（日志 + 源码 + 官方文档三线验证）

**1. 手机日志（决定性证据）**：
```
I20260826 18:39:01 registering component: predictor           ← 插件已编译!
I20260826 18:39:01 registering component: predict_translator  ← 开发者确认属实
```
之前"未编译"的判断是日志截断导致的误判，已纠正。

**2. build 产物核验**（全部正确）：
- `engine/processors` 首位 `predictor` ✓
- `engine/translators` 含 `predict_translator` ✓
- `prediction` switch（reset: 1）✓
- `predictor:` 配置块（db/max_candidates/max_iterations）✓

**3. librime 源码级触发链路**（全部通畅）：
```
选候选 → ConfirmCurrentSelection → Commit
  → commit_notifier（history push）→ Clear → update_notifier
  → Predictor::OnContextUpdate（composition 空 ✓ prediction ✓）
  → PredictAndUpdate → db.Lookup(上屏词) → CreatePredictSegment
  → update_notifier → Engine::Compose → predict_translator 填充 menu
Hamster: candidateListWithIndex → composition().back().menu → 联想候选
```

**4. Hamster 官方文档**（ihsiao.com/apps/hamster/docs）：无联想专页；确认「重新部署」后自动 Sandbox→AppGroup 同步（`syncSandboxUserDataDirectoryToAppGroup(override: true)`）。

**5. 锁定唯一未验证环节**：predict.db 的加载位置。

`PredictEngineComponent` 用 `CreateResourceResolver({predict_db, "", ""})`：
- root = `user_data_dir`（键盘完全访问时 = `AppGroup/InputSchema/Rime/`）
- fallback = `shared_data_dir`（= `AppGroup/InputSchema/SharedSupport/`）

若 predict.db 两处都找不到 → `Create` 返回 nullptr → `Predictor` 静默失效（正是观察到的现象）。

### 处置：predict.db 双位置部署

| 位置 | 主App路径（文件服务器可见） | 部署后同步到（键盘） | 校验 |
|------|---------------------------|--------------------|------|
| userDataDir | `Documents/Rime/predict.db` | `AppGroup/InputSchema/Rime/` | ✓ 7,529,528B |
| sharedDataDir | `Documents/SharedSupport/predict.db` | `AppGroup/InputSchema/SharedSupport/` | ✓ 7,529,528B |

### 测试步骤（重要：必须彻底重启键盘进程）

1. 重新部署
2. **杀掉键盘进程**（关键！predict.db 在键盘进程启动时加载，进程存活期间不会重载）：
   - 上滑退出所有 App → 或重启手机 → 或切换到系统键盘后再切回
3. 输 `3235` 选「你」→ 候选栏应立即出现「的/不/是」联想候选
4. 点联想词 → 继续下一轮联想（max_iterations: 1 时一轮后停）

### 若仍不生效的下一步

- 键盘进程日志不可见（只写主 App 目录），无法直接看 `failed to load predict db` 错误
- 备选方案：向开发者索取键盘侧日志开关，或改用 Hamster「自定义键盘」方案由 App 层实现联想 UI
- 另一备选：用 essay.txt 词频自建简体 predict.db 时一并排查格式兼容性

---

## 一、部署前状态侦查

通过文件服务器 API 侦查发现：

| 项 | 状态 |
|----|------|
| Rime/stroke_bg5cgq.schema.yaml | ❌ 缺失 |
| Rime/stroke_bg5cgq.dict.yaml | ❌ 缺失 |
| Rime/build/stroke_bg5cgq.*.bin | ⚠️ 有旧编译产物（说明曾部署过，源文件被删） |
| Rime/default.custom.yaml | ✓ 已含 stroke_bg5cgq 方案 |
| Rime/hamster.yaml | ⚠️ 0 字节空文件（有隐患） |
| SharedSupport/hamster.app.yaml | ✓ useKeyboardType 已设为 "BG5CGQ笔画" |
| SharedSupport/hamster_keyboards.yaml | ❌ 无 BG5CGQ笔画 布局（App Store 版内置配置） |

**关键发现：**
1. App Store 版将键盘布局拆分到 `SharedSupport/hamster_keyboards.yaml`，主 `hamster.yaml` 通过 `__include: hamster_keyboards:/keyboards` 引用
2. 配置加载优先级：`SharedSupport/hamster.yaml` → `Rime/hamster.yaml`(覆盖) → `Rime/hamster.custom.yaml` → `UserDefaults`(UI操作)
3. `deepMerge` 语义：**数组字段整体替换**（用户 `keyboards` 数组会替换内置全部键盘）
4. App Store 版配色字段名与开源版不同：`button_foreground_color`（非 `button_front_color`）

## 二、已执行的部署操作

### 1. 上传 Rime 方案文件（tus 协议：POST 创建 → PATCH 写数据）

| 文件 | 大小 | MD5 校验 |
|------|------|---------|
| Rime/stroke_bg5cgq.schema.yaml | 2,282 B | 13a144ff… ✓ 一致 |
| Rime/stroke_bg5cgq.dict.yaml | 1,005,619 B | 13e6d67a… ✓ 一致 |

### 2. 上传 Rime/hamster.yaml（60,290 B）

内容 = 手机内置 4 键盘（仓颉/大千注音/声笔trime/声笔46）+ BG5CGQ笔画 布局 + 配色配置：

```yaml
keyboards:
  - name: "仓颉"          # ← 内置，保留
  - name: "大千注音"       # ← 内置，保留
  - name: "声笔trime"     # ← 内置，保留
  - name: "声笔46"        # ← 内置，保留
  - name: "BG5CGQ笔画"    # ← 新增
    ...

keyboard:
  enableColorSchema: true
  useColorSchemaForLight: stroke_ninegrid_dark
  useColorSchemaForDark: stroke_ninegrid_dark
  colorSchemas:
    - schemaName: stroke_ninegrid_dark   # 9宫格笔画输入 仿百度深色
      ...
```

> 注意：因数组整体替换语义，必须包含内置 4 键盘，否则它们会丢失。

### 3. 配色字段名适配

App Store 版配色字段：`button_foreground_color` / `button_pressed_foreground_color` / `button_swipe_foreground_color`

## 三、手机端待完成操作（需手动）

1. **重新部署**：打开「仓输入法」App → 输入法设置 → 重新部署
   （Rime 将重新编译 stroke_bg5cgq，生成新的 table.bin/prism.bin）
2. **切换方案**：键盘上长按 🌐 或在设置中切换到「BG5CGQ笔画输入」
3. **键盘类型**：设置 → 键盘 → 使用键盘类型 → `custom(BG5CGQ笔画)`
   （hamster.app.yaml 已预设，通常无需改动）
4. **配色**（可选）：若想使用仿百度深色配色，在设置中确认配色方案为「9宫格笔画输入」
   注意：当前皮肤为「原生·仿微信·笔画·测试」(.hskin 皮肤系统)，皮肤优先级高于配色方案

## 四、验证要点

部署后测试：

| 测试 | 预期 |
|------|------|
| 按 一 键 | 候选显示：在 有 不 都 要…（首笔可选字） |
| 输入 2512 | 首选「中」 |
| 输入 3121534 | 首选「我」 |
| 输入 31215 + 分词 + 31 | 词组模式（enable_sentence 自动组词） |
| 按 通配 键 | 输入 ?，如 3?21534 匹配「我」 |
| 按 ，。键 | 标点直接上屏 |

## 五、故障排查

| 症状 | 原因 | 解决 |
|------|------|------|
| 部署报错/方案列表无 stroke_bg5cgq | dict.yaml 语法错误 | 查看 RIMELogger 目录日志 |
| 键盘显示为普通26键 | hamster.yaml 中无 BG5CGQ笔画 或 YAML 解析失败 | 检查 Rime/hamster.yaml |
| 按键无反应 | processByRIME 配置或 alphabet 不匹配 | 确认 alphabet: "12345?'" |
| 候选乱序 | table.bin 未重新编译 | 强制重新部署 |
