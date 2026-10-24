---
name: iflytek-analysis
description: "讯飞输入法 v15.0.3606 深度技术分析知识库（Phoenix 引擎、词频调频、联想、造词、分词、笔画解码、词库二进制格式、RNN 模型、桥接层/CTRL指令、顺畅连贯机制、云端接口、跨屏、埋点灰度、表情数据系统、安全风控、业务模块/账号支付/加密机制、**键盘布局反编译数据（26键/笔画/符号三面板真实 ini 坐标，跨会话可用）**，含五卷分析 + 反汇编交叉核对结论 + 9 份子代理反汇编报告 + Phoenix 符号精选表）。供 0点输入法（自研输入法，只做笔画+英文+符号，不做拼音）逆向参考与算法透明移植。触发词：讯飞分析、讯飞输入法分析、Phoenix 引擎、词频调频、RnnResort、词库格式、iflytek-analysis、讯飞协议、云输入、联想、造词、顺畅连贯、笔画输入、加密机制、RNN模型结构、讯飞键盘布局、键盘反编译、26键还原、bihuakey、26enkey、symbolkey。"
version: 1.12.0
author: "mickeu"
license: MIT
tools:
  - file_read
  - shell_execute
---

# 讯飞输入法 v15.0.3606 — 深度技术分析知识库

本技能沉淀对讯飞输入法 iOS 版（v15.0.3606）的完整逆向分析成果，是 **0点输入法**（自研输入法）逆向参考与算法透明移植的核心知识库。

---

## 🎯 用途

当用户需要了解讯飞输入法内部机制、或为 0点输入法移植/复刻某一算法（词频调频、联想、造词、分词、笔画解码、云端同步等）时，读取本技能参考资料并按需输出方案。

---

## 📁 参考资料索引

本技能内置四卷核心分析文档 + 反汇编核对结论，存放于本技能目录 `references/`：

| 文件 | 内容 | 对应卷 |
|---|---|---|
| `NOTES_核心机制分析_第一卷.md` | Phoenix 引擎与核心算法：RNN 精排+调频公式 `score'=weight×(old/102.4)+(1−weight)×count+0.5`、联想三桶分流、造词前缀拆分、分词组合分、笔画混合哈希解码、云输入/英文预测/整句LM 链路、云端接口、接入范围 | 第一卷 |
| `NOTES_深度技术核心分析_第二卷.md` | 343 个 Phoenix 符号模块地图、词库 lit/sym 二进制格式、ncnn RNN 模型、语音/手写引擎、云端接口、跨屏 WebSocket、埋点灰度、表情/花样字数据系统、安全风控、12 条值得抄的设计 | 第二卷 |
| `NOTES_核心机制全量分析_第三卷.md` | 桥接层 + 引擎控制 + 输入法工程架构：XFCoreProcessor 门面、CTRL_* 指令集、人名模式独立子系统、多模态统一解码、键盘布局数据驱动、候选 UI 架构、英文/邮件预测、云拼音协议、剪贴板风控、资源加载模板化、AI 创作 Pro 时间感知、10 条新增可借鉴设计 | 第三卷 |
| `NOTES_顺畅连贯技术路线_第四卷.md` | 顺畅连贯机制：已提交态循环、候选状态机、七大候选数据源（词+斗图+场景+UGC+AutoForecast+语音+灰度）、自动预测、自动选首+标点顶字、动态 bigram 上下文、对 Rime/笔画方案的落地路线（A-G） | 第四卷 |
| `NOTES_反汇编数据核对结论.md` | 用 nm_all 全符号 + strings_all 全字符串 + resfocused ObjC selector 对四卷（重点第四卷）做的权威交叉核对：bigram/hotword/斗图/UGC/场景/剪贴板/自动选首均有硬证据；但 CandidateManager/SubmittedState/AutoForecast 等 Swift 类名查无实据（作者自造参考命名），移植时以机制为准勿照抄类名 | 核对结论 |
| `NOTES_反汇编深度比对报告.md` | 用 backup_bin 原始机器码 + objdump 反汇编，对第一卷核心算法逐条实证：ProcessStroke（24bit 笔画码 + fmix 混合哈希 + 开放寻址线性探测 + 6 字节词项）、CalcCombineScore（组合分 = 基础分+前字计数+首字+5+权重，clamp 0xff）、RnnReScore（RNN 调频 `new=weight*(old/102.4)+(1-weight)*cur+0.5+delta`，权重 clamp≤0.5，old/102.4 用 old*5>>9 近似）、RnnResortBase（排序壳）。附延伸线索：内部回调 0xffffdedc、排序函数 0x100003534、哈希表结构 | 深度比对 |
| `notes/排序_反汇编报告.md` | 子代理深挖排序类函数：SortCore=稳定归并排序壳（插入阈值128/8、比较器 vtable 注入）；Comparator=候选词典序比较器（flags 0x80000/0x10000 → packed rank[29:15] → type==0x0e → rank[14:0]）；ProduceSort=十档候选生产调度（空桶 sentinel=15）；ngram_update=加权增量累计 `delta=value*scale; acc=base+delta`（**反证** EMA 公式）；lattice_addarc=格图弧构造。含可移植到 Rime 的 RankKey 骨架 | 排序 |
| `notes/联想预测_反汇编报告.md` | 子代理深挖联想/预测类函数：AssocCore 正常路径要求输入 **<21 个 UTF-16 码元**（**纠正**第一卷“≥21 才计算”）；候选容器=vector<DecodeNode*> 8B 指针、节点≥56B（+40 type/+44 packedScore/+48 firstChar/+51 textLen）；预测排序键=+44 bits15..29 降序堆式插入；去重要求等长并允许 ±0x20 码元差（ASCII 大小写折叠）；首字符过滤掩码常数 0x81401（U+0041..0054）；Phn_WordAssociation 只是按 +32 key 查全局有序树 | 联想/预测 |
| `notes/词库云同步_反汇编报告.md` | 子代理深挖词库/用户词/云同步：用户词持久化=变长三字段字典（UWD_load 每批枚举16项）；Phoenix 用户词节点最小42B；词频/学习值上限1000；删除用 UTF-16 并保留同步墓碑；HTTP 协议=POST+JSON+Bearer、60s 超时；addr_*Url 只是 32B getter，URL/AES key/IV 不在本批切片（ime.voicecloud.cn 待验证） | 词库/云同步 |
| `notes/笔画规则引擎_反汇编报告.md` | 子代理深挖笔画/几何规则层：`use_geom_rules`=完整函数，Box16 四边界+center/scale，按 Unicode switch 跳表（0x22..0x7a / 0xFF02..0xFF65）逐字判几何条件，命中 `penalty[i]+=0x7fff` 返回 n；`use_stroke_rules`=不完整（截在 0x1000003fc，分支达 0x100001950），首字≥U+4E00 先全项 +300，再按段数/关键点/投影重叠规则。两者是候选产生后的**惩罚后处理层**，非 ProcessStroke 哈希层。含 StrokeGeom 结构（+0x28 起 8 组 int16 关键点）与可移植透明规则表设计 | 笔画/几何规则 |
| `notes/笔画规则引擎_补全_反汇编报告.md` | **use_stroke_rules 完整补全**：函数边界 0x100d55124..0x100d56b90；`RULE_A@0x100d56130`=`penalty[i]+=0x7fff`（**32位环绕加法，非饱和**），`RULE_B@0x100d56140`=仅 `++i` 推进循环不写 penalty；两跳表真实基址 0x100d56b94（U+0021..U+007D）/0x100d56d08（U+513F..U+5238），均为 signed int32 PC-relative，报告含完整 Unicode→case 映射表（ASCII+CJK 各 ~70 项）、40+ case 的可确认规则控制流、旧报告"0x7fff 饱和"修正 | 笔画/几何规则·补全 |
| `notes/英文预测与查询码_反汇编报告.md` | 子代理深挖英文预测/FST/查询码：`ProcessEngComplement`=经 this+0x10 多态处理器生成中间弧→逐弧构造 DecodeNode 追加 vector，limit=(int8)[0x150]+5-(int8)[0x153]；`eng_fst_arc`=ResFstDict **6 字节压缩弧**展开（+0 低24位目标态/高8位标签，+4 为 16 位值；状态表相邻项 bits[24:1] 描述弧区间）；`QueryCodeContext`=ResUserDict 用户词**上下文属性 bitmask OR**查询（2/3 种查询类别、四路分页池 20B 记录、40B 哈希节点 +0x24 的 1 字节 context_flags） | 英文/FST/查询码 |
| `notes/候选生产组装_反汇编报告.md` | **候选生产/组装闭环实锤**：①旧地址 0xffffdedc 真实=**0x10010284b0 `phn::DecodeArcState_Create`**，从对象池分配 40B `DecodeArcState`（写 +0 id/+2 kind/+3 attr/+4/+6 属性/+8 segment/+16 path/+24 arc），**不是直接构造最终 DecodeNode**；ProcessStroke 三调用点，命中后 push_back 到 `vector<DecodeArcState*>`，此阶段无排序。②ProduceSort=0x100fa7518，四个被调函数真实符号：`SortNodes`(0x100fa8464，唯一直接进 Comparator stable_sort 处：ParseScore/LengthScore/Associate/SortStrokeSingleWords)、`GetSortType`(0x100fa9790，返回 0..14/15 sentinel)、`UniqueDecNode`(0x100fb10f0)、`UniqueFullAndSent`(0x100fb3060，按 DecodeNode+33 bit3 合并去重分桶)。③闭环：笔画词项→ProcessStroke→DecodeArcState→后续解码成 DecodeNode 桶→ProduceSort(GetSortType→SortNodes 排序→Unique 去重)。**ProduceSort 及四函数均未调 RnnResortBase**（RNN 是另一阶段）。修正第一卷"命中即组装 DecodeNode 候选"表述 | 候选生产/组装 |
| `notes/排序闭环_RNN调频写入点_反汇编报告.md` | **排序闭环+RNN调频公式逐指令实证（本次最大成果）**：①排序键写入点实锤=`RnnReScore`@0x100f8384c，`bfi w12,#15,#15` 把新分数嵌入 DecodeNode+44(=+0x2c rank) 的 bits[29:15]。②第一卷调频公式完整实证：`new = weight×(old/102.4) + (1−weight)×count + 0.5 + correction`；`old/102.4` 用 `old*5>>9` 定点近似；`weight=min(cfg,0.5)` 按类型再 min 到 C2/C4；`ratio=count/old` ≥5 才走小权重；`correction=(old−count)` 受 type/类型标志调节；结果 bfi 进 rank[29:15]，count 留 rank[14:0]。③DecodeNode 字段定名：+0x20 flags / +0x28 type / +0x2c rank（低15位=count，高15位=RNN分）。④揭示**两条排序入口**：普通候选走 ProduceSort→SortNodes→Comparator；RNN 精排走 RnnResortBase→RnnReScore 写分→Fullmatch/LmScore Comparator stable_sort。含可移植伪 C 与 Rime 落地要点 | 排序/RNN调频 |
| `notes/RNN模型加载与格式_反汇编报告.md` | **RNN 模型加载链+文件格式实证（结论修正：模型不加密）**：①模型文件 `940e67abb4`（4.2MB，从 IPA 提取）熵 5.39、分块 6.88→2.67 渐变、bit 强偏斜 = **量化权重+位变换，非强加密**。②加载链：`RnnInstMgr::Start(0x10103f048)` → IRes_mgr vtable[48] 虚函数(参数22=RNN类型)取资源对象 → 对象 vtable[80] 取数据指针 → 按 `[数据+40]` 类型(1=Float/3=Fix)创建 RnnInstFloat/Fix 实例。③**模型格式=自定义层描述符序列化**：ResRnn 内存 `[+6]`=层数、`[+8]`=层描述符偏移；每层含名字(+0x24)/数据偏移(+8)/数据长度(+12)；层类型串 dense/dict/lstmp/embedding/softm 与 rnn/qik/geo。④**头部 magic 决定量化精度**：`rnn_float`→LoadRes<float,float>、`rnn_16bit_8bit`→<schar,short>、`rnn_8bit`→<schar,schar>、`rnn_16bit`→<short,short>。⑤`RLRnn::load→LoadRes→ParseMatrix(0x100f5850c)/LoadDict(0x100f58880)` **直接解析明文数据，无解密调用**。⑥**★本次重要实证：资源管理器明文读取文件**——`XFPhnResMemCache::loadRes`(0x1009f2b7c)→`0x1009f2794`→`0x1009b55d4` 直接 `fopen(path,"rb")`+`fread` 读全部数据，**无任何 XOR/AES 解密循环**（详见 `notes/rnn_resloader_disasm.md`）。⑦修正此前"解密在资源管理器层（IFlyEncryption XOR）"的推断：**已安装模型文件明文存储**，IFlyEncryption XOR 仅可能用于下载/更新的传输 zip。含 ParseMatrix 头部维度 mul/msub %100 解码实证 | 模型/RNN加载 |
| `notes/候选解码主路径_反汇编报告.md` | **候选解码主路径完整还原（ProcessEmit→DecodeArcState→候选桶）**：①`ProcessEmitDecode_common`(0x1013e5e1c)核心循环逐指令还原：**6 字节词项遍历**（`add x26,x26,#0x6`）→`ldrh w8,[x26,#4]` 取词项ID→查表 `ldrh w8,[x9,w8,uxtw#1]`→`ldrb w9,[x9,x8]` 校验有效位→清零 rank（`stp wzr,wzr,[x19,#44]`）→在 DecodeArcState 链 `madd x9,x8,x17,x9`（x17=0x18 即 24B 步进）定位→遍历链找匹配节点。②**中英文分流依据**：关联对象 `+33 bit1`（`tbnz w8,#1` → 走 `_eng` 否则 `_chn`）。③`ProcessEmitDecode_process_chn`(0x1013e6974)/`_eng`(0x1013e6374) 生成**中间候选并入 vector**，均**不直接调用 ConstructDecodeNode**。④`ConstructDecodeNode`(0x1013acf58) 经 0x10138d564 创建最终节点；`NodeCreator::CreateNode`(0x10138de40) 是**另一条** NodeCreator 路径，不可混同。⑤`SetInfo`(0x10138e0b0) 精确恢复 DecodeNode 字段来源：`+0/+8/+16/+24/+32/+40/+43/+44/+48/+50/+51`。⑥`MergeOne`(0x1013adec4)/`MergeN`(0x1013ad5a4)/`MergeOneForPC`(0x1013adb20) 是**类型/flags/边界驱动的链式组合与回收机制**，不是简单"同词去重保高分"。⑦完整主路径：ProcessStroke→DecodeArcState→ProcessEmitDecode_common→_chn/_eng→ConstructDecodeNode→MergeOne/N→候选桶。含函数地址/大小、寄存器、数据结构偏移、文字 CFG、伪 C、Rime/笔画移植建议；rank 偏移/Merge 精确比较键/英文变体 bit 已标"待验证"未臆测 | 候选解码主路径 |
| `NOTES_业务模块与加密与模型_第五卷.md` | 第五卷（业务模块/加密机制/RNN 模型）：①主 App 五 Tab（首页/AI输入/Biu星球/百变人设/我的）+ Biu星球趣味发送模式包（biubiufun.ini 数据驱动）+ UGC 社区 + 账号体系（SRFAccountService/云备份）+ 会员支付（CBGPaySystem + XFPayCenter IAP 凭证缓存补单）+ 恋爱军师 VIP MVVM；②加密机制熵分析实证：**词库非 AES 级强加密**（96a4d21d0f 词典熵 5.31/6.09、52cd074a7a 小词典熵仅 1.51 几乎无加密，是自研紧凑二进制 + UTF-16LE + 音节索引，strings 读不出仅因 UTF-16）；RNN 模型 940e67abb4 熵 6.36/7.02 分块渐变（2.59→3.53→5.09）疑似量化+位变换非 zlib；加密工具链（IFlyEncryption XOR / IFlyZipData / DeliveryPlanUtil DES / ATMIUAESTool / ATRSANUtil RSA / HiSecret）；③ncnn RNN 结构：Qrnn+Qrnn_final 主排序、LstmLayer 四门、Embed、InstanceNorm/HardSigmoid/SELU/Softmax、MemoryData→Conv/Qrnn→Eltwise→Softmax；提取路径（hook pRnnInst_->Score 前资源解析 / ncnn 内存加载 dump / 反量化 neon_weight_int+vec_softmax_int_fix_imp）；④借鉴要点：趣味功能数据驱动、IAP 补单、灰度控制一切、词库保护用格式而非加密、量化模型防扒 | 第五卷 |
| `phn_symbols.txt` | Phoenix 引擎 C++ 符号精选表（344 行）：核心类 ActiveInstImp/AssociateMgr/DecodeMgr/ResultMgr/InputParser/KeyLayout/LayoutImp/Res_mgr/Res_fuc；资源加载 RL* 系列（RLBaseDict/RLFstDict/RLRnn/RLSyllableMap/RLStrokeTable/RLSimpToTrad/RLUniPinyin/RLContactName/RLNamepTriggerTable/RLUserDict 等 20+ 类）+ Res* 参数类；RNN 门 DnnLayerIaa/Ias/Iff/Iss + LstmLayer 同名四门 + RnnInstFix/RnnInstFloat/RnnInstMgr；SEC_* 事件码（ACTE/ASSE/DECE/EPDE/IPTE/RLTE）；词法操作（ExpandParamMgr/ExpanderFactory/ResultArrange/ResultSort/ResultUnique/ResultScore）；C/D 后缀=构造/析构（逐类配对）；数值内核 calc_int/calc_weight_int/neon_weight_int/sigmoid/softmax/vec_softmax_int_fix_imp/tansion；音节批量处理 syllablebatch_*/syllablepath*/syllablesegment_*；FST 操作 arc_sort/arc_sort_by_score | 符号表 |

读取方式：
```bash
# 在会话中读取时，用 file_read 直接读取以下路径：
# /var/minis/skills/iflytek-analysis/references/NOTES_核心机制分析_第一卷.md
# /var/minis/skills/iflytek-analysis/references/NOTES_深度技术核心分析_第二卷.md
# /var/minis/skills/iflytek-analysis/references/NOTES_核心机制全量分析_第三卷.md
# /var/minis/skills/iflytek-analysis/references/NOTES_顺畅连贯技术路线_第四卷.md
# /var/minis/skills/iflytek-analysis/references/NOTES_反汇编数据核对结论.md
# /var/minis/skills/iflytek-analysis/references/NOTES_反汇编深度比对报告.md
# /var/minis/skills/iflytek-analysis/references/NOTES_业务模块与加密与模型_第五卷.md
# /var/minis/skills/iflytek-analysis/references/phn_symbols.txt
# /var/minis/skills/iflytek-analysis/references/notes/排序_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/联想预测_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/词库云同步_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/笔画规则引擎_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/笔画规则引擎_补全_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/候选生产组装_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/排序闭环_RNN调频写入点_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/RNN模型加载与格式_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/rnn_resloader_disasm.md
# /var/minis/skills/iflytek-analysis/references/notes/候选解码主路径_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/讯飞键盘布局反编译数据.md
```

---

## 🔑 最核心可移植资产速览

### 1. 词频调频公式（讯飞精华，第一卷 1.1）
```
score' = weight × (old_score / 102.4) + (1 − weight) × count + 0.5
```
- `weight` 由 `ratio=计数A/计数B` 选择（ratio≥5 且类型1→min(freq,C2)；类型2→min(freq,C4)；否则 min(freq,0.5)）
- 排序键层次：`[DecodeNode+32 bit19 特殊标志] → [高15位新分数] → [bit16 标志] → [低15位计数小者优先]`
- 本质 = 指数加权移动平均 + 稳定归并排序（SortCore：n≤128 插入排序，更大递归归并）

### 2. 联想三桶分流（第一卷 1.2）
- `AssocCore`：逐码位展开 → 按节点类型分流「普通/拼音/连续联想」三桶 → 合并排序；码≥21 才计算
- `PredictInstance`：候选按分数二分插入降序（≤10 个丢低分）
- `FilterPredictResult`：首字符位掩码过滤 + 逐 uint16 去重保高分

### 3. 造词/用户词学习（第一卷 1.3）
- `AddWord`+`InsertWord`：**前缀拆分插入**，用户词最长 32 码
- `Decay`：热度衰减 `系数=min(1,(now-ts)/阈值*0.5)`
- 用户词典：`key % bucket` 哈希桶 + 链式探测，查询时类型标志 OR 进结果加权

### 4. 词库二进制格式（第二卷 2）
- 统一框架：`"lit\n" + u32le 数据段长度 + "sym\n" + 魔数 0x03058807 + 16字节校验 + 统计字段 + [音节索引区] + [词条数据区] + "ver\n"+版本`
- 词条记录：`[音节码 u16] [词频/数据 u16] [词条 UTF-16LE ...]`
- 内容全部加密/混淆，防扒

### 5. RNN 精排模型（第二卷 3）
- 内嵌完整 ncnn 算子库；`RnnInstFloat`（高端浮点）/`RnnInstFix`（低端定点）
- 推理链路：`AddHistory → Push → Score → ArrangeResultWithRnn`
- 开关：`setRnnOpenEb`（灰度）

### 6. 云端接口（第一、二卷）
| 接口 | 用途 |
|---|---|
| `ups.xfyun.cn/v2/users/unique_user` | 用户唯一标识（画像） |
| `ime.voicecloud.cn` | IME 后端主站 |
| `100ime-evo.xfyun.cn/individuation/iat/content\|upload` | 个性化语音模型下发/上传 |
| `s3.voicecloud.cn` | 静态资源 CDN |
| `100ime-iat-api.xfyun.cn` | 语音听写 API |
| `srf.xunfei.cn/app/` | 语音合成 |

### 7. 桥接层 / CTRL 指令集（第三卷，可借鉴设计①）
- `XFCoreProcessor` 门面：UI 与 Phoenix 引擎间 Facade，转发到 PinyinProcessor/InputDefaultCore/PhnCore
- 主链路：`processKey/SwypePoints → phn::DecodeInst 束搜索 → 候选 → choose/syllableChoose/CTRL_SINGER_WORD_FILTER(以词定字) → 上屏 + 云 cookie 反馈 + bigram 学习`
- `control(CTRL_*)`：引擎能力抽象为指令，UI 只发指令不关心实现（CTRL_CHOOSE_WORD/PINYIN/ENGWORD、CTRL_SINGER_WORD_FILTER、CTRL_EXPAND_UNCOMMON、CTRL_SET_CONTENT 等）
- 人名模式独立子系统：独立触发表/音节路径/候选/过滤链（SurnameFilter/SingerWordFilter）
- 键盘布局纯数据驱动：ini [KEYn] 字段语义（ID/BACK_STYLE/FRAME/STAT/CODE/CENTER/TAG/DH 点划），`structWithDic:` 运行时生成键结构

### 8. 顺畅连贯机制（第四卷，路线落地到 Rime/笔画）
- 核心闭环：上屏不是终点而是下次输入起点（已提交态循环）
- 七大候选数据源：候选词 + 斗图 + 场景助手 + UGC + AutoForecast + 语音 + 灰度
- 自动选首：真实 ObjC 方法 `promptFirstCandidateWithString:innerCode:innerLen:` + `p_autoSelectAllIfNeed`（注意：**不是**第四卷写的 `onCandidateWordAutoSelectFirst`）
- 动态上下文：`user_words_num_`、`%s|punc bigram %d %d`、`pbigram_incode`
- 对 Rime/笔画方案的落地优先级：P0 = 路线B(运行时用户 bigram 缓存) + 路线C(标点顶字+自动选首增强)；P1 = A(上屏后自动预测) + D(候选输出状态机)；P2 = F(热词动态更新) + G(多数据源混合)
- ⚠️ **第四卷 Swift 类名（CandidateManager/SubmittedState/SubmittedDataCombiner/AutoForecast/CandidateNext 等）在反汇编符号/字符串池查无实据，是作者自造参考命名，移植时以机制为准，勿照抄类名**（详见 `NOTES_反汇编数据核对结论.md`）

### 9. 加密机制实证 + RNN 模型结构（第五卷，2026-10-24 新增）
- **词库保护策略 = 格式而非加密**：熵分析实证（主词典 96a4d21d0f 熵 5.31/6.09、小词典 52cd074a7a 熵 1.61/1.51）——自研紧凑二进制（音节码 u16 + 词频 u16 + **UTF-16LE 词条**）+ 音节索引；`strings` 读不出词条仅因 UTF-16 编码，**完全可逆解析**，不是 AES 级加密
- **RNN 模型 940e67abb4**（4.2MB）熵 6.36/7.02、分块熵渐变（头 2.59→中 3.53→尾 5.09），非 zlib/gzip → **量化权重 + 自定义位变换**（ncnn 量化 bin 特征）；模型结构无独立 .param，编译进二进制内存加载
- **网络结构**：主排序 Qrnn（Quasi-RNN，快于 LSTM 适合移动端）+ 辅助 LSTM 四门（DnnLayerIaa/Ias/Iff/Iss）+ Embed + InstanceNorm/HardSigmoid/SELU/Softmax；数据流 MemoryData(历史)→Conv/Qrnn→Eltwise→Softmax
- **提取路径**：①hook `pRnnInst_->Score` 前的资源解析 dump 解密后权重 ②ncnn 内存加载 dump Net 结构 ③`neon_weight_int`/`vec_softmax_int_fix_imp` 符号提示推理已定点化，权重可直接反量化
- **加密工具链**（勿混淆用途）：`IFlyEncryption XOREncryption:`（内部数据）/ `IFlyZipData Encryption:`（压缩+加密）/ `DeliveryPlanUtil encryptUseDES:key:`（delivery_plan.dat）/ `ATMIUAESTool`+`BUCocoaSecurity`+`CSJNetworkSecurity`（广告 SDK）/ `ATRSAUtility`/`CryptoUtil`/`RSAProcess`（请求签名）/ `HiSecret`（XFIMECoreLib）
- **逆向成本评估**：词库=低成本（写解析器提取 UTF-16 词条）；本地 AI 规则 JSON（keystore/address_config）=高熵强加密需 key 派生逆向；RNN 模型=中高成本
- **业务模块速查**：五 Tab=Biu星球趣味发送（biubiufun.ini 模式包，与键盘布局同款数据驱动）+ UGC 社区 + 百变人设（createpro_bbrenshe 下发配置）+ SRFAccountService 账号 + CBGPaySystem/XFPayCenter 支付（IAP 凭证缓存补单：resPurchased+needUploadReceipt）+ 恋爱军师 LoveVipChat MVVM；GrayControlManager 灰度控制一切（含恋爱军师 AI 头像/昵称/首条消息）

### 10. 键盘布局反编译数据（2026-10-24 新增，跨会话可用，用于 0点输入法键盘还原）

> ⭐ **全部坐标/尺寸/符号/CODE 均从 IPA 内 ini 文件真实提取，非看图推测。** 用户明确要求"先反编译再还原"，故此数据为还原键盘的唯一权威依据。

- **数据文件**：`references/讯飞键盘布局反编译数据.md`（跨会话用 `file_read` 直接读取）
- **原始 ini**：`/var/minis/shared/myime/ime_res/`（`26enkey.ini` `bihuakey.ini` `symbolkey.ini`，从 IPA `主键盘布局/iOS系统布局/{375,428}/` 解压）
- **三面板真实布局**：
  1. **26键英文** `26enkey.ini`（WIDTH=428 HEIGHT=246）：字母键 W=33 H=42、SUB=右上角 ASCII 符号（a=126→~、s=33→!、d=64→@、f=35→#、g=37→%、h=39→'、j=38→&、k=42→*、l=63→?；z=40→(、x=41→)、c=45→-、v=95→_、b=58→:、n=59→;、m=47→/）、shift/delete 宽 48、SUMMER 空格 W=150、底行 切换(48)/123(48)/，(33)/SUMMER(150)/。(33)/英文(27)/发送(42)
  2. **笔画九宫格** `bihuakey.ini`（375×216）：左符号列 LIST1 FRAME{3,6,69,153} CELL{63,37.5} 8符号 ， 。 ？ ！ ~ … ： 、；九宫格 75×53 三列(X=75/150/225)+右功能列(X=300)；底行 123{3,162,75,48}/0SUMMER{78,162,225,48}/中文{303,162,72,48}/发送{375,162,72,48}
  3. **符号面板** `symbolkey.ini`（375×216）：分类列 CAT0-4（X=3 W=60 H=37）常用(sel)/中文/英文/表情/返回；符号区 4列(X=69/147/225/303)×5行(Y=6/47/88/129/170) 键 W=72 H=37：( ) , . / ? ! | . / ~ # * + / / @ [ ] / 功能键
- **工具栏** 6 图标确认（ini TOOLBAR 段）：home（房子）/list（列表）/mic（麦克风）/check（对勾）/emoji（笑脸）/gem（宝石）
- **关键字段语义**：`FRAME={{x,y},{w,h}}` 位置尺寸；`SUB` 右上角符号（ASCII 码）；`CODE` 按键码；`STAT` 状态位；`BACK_STYLE` 背景样式 ID；`DH` 点划（长按上划出符号）
- **跨会话调用约定**：还原键盘前先 `file_read /var/minis/skills/iflytek-analysis/references/讯飞键盘布局反编译数据.md` 取真实坐标；若需原始 ini 细节读 `/var/minis/shared/myime/ime_res/*.ini`；配色见 `/var/minis/shared/myime/配色规格.md`（小浣熊识图+PIL 像素分析，6 张参考图日夜两套）

---

## 🚧 接入红线（用户明确拍板）

- 0点输入法只接入讯飞云端：**用户词/词频同步、云输入、云候选**
- **不触碰 AI 调用**（如讯飞星火等 AI 能力）
- 登录须用**用户本人账号的合法凭据**，不伪造他人身份、不绕过鉴权获取未授权数据
- 相关 iOS 层类：`UserWordRuntimeRecorder`、`UserConfig::isUserWordAutoUpload`、`LexiconSyncProcessor`、`UserWordDelManager`、`IMEAddressConfig`

---

## 🎯 范围规则（用户明确拍板，2026-10-23）

- **只做讯飞输入法的分析**。后续上传的分析文档/文件里若有其它（非讯飞）内容，一律排除，不纳入。
- 0点输入法定位：**只做笔画输入**（+英文26键 + 符号面板），不做拼音方案。

---

## 📌 版本管理规则（用户明确拍板，2026-10-24）

- **版本号只增不减**：后续任何追加内容（新报告、新章节、新索引行、新读取路径）都只能让 `version:` 字段**递增**（如 1.8.0 → 1.9.0 → 1.10.0），**绝不回退/倒改版本号**（例如 1.7.0 不能被改回 1.6.0，即使要"修正"旧内容也不能降低版本）。
- **内容只追加不覆盖**：新增分析/报告一律**追加**到索引与读取路径末尾，不删除旧行、不覆盖旧内容；如需修正旧结论，在对应行后**追加**更正说明并升版本，而非改写旧行。
- **每次修改后立即验证**：改完必须 `rg -n '^version:'` 核对版本号，并 `diff` 技能库副本与 config-backup 副本一致，防止版本被外部机制覆盖回退。

---

## 📝 工作流建议

1. 用户询问讯飞机制/移植需求时，先读对应卷文档（file_read 上述 references 路径）
2. 若需参考反编译二进制：`/var/minis/shared/iflytek_analysis/bin/iFlytekInput`（完整 Mach-O，2026-10-24 用户重新提供 IPA 后提取，46MB）或 `/var/minis/shared/iflytek_analysis/backup_bin/`（100+ 函数 .bin 切片）
3. 若需符号/字符串表：`/var/minis/shared/iflytek_analysis/symbols/`（nm_all_full.txt 20.7万、nm_demangled.txt、objc_selectors.txt、lexsyms.txt、main_res_strings.txt 等）+ `strings_all_full.txt`
4. 反汇编命令：`llvm-nm -C $BIN | grep -i <name>`；`llvm-objdump -D --macho --arch=arm64 $BIN --start-address=<vaddr> --stop-address=<vaddr+len>`
5. 输出移植方案时标注可复用算法与透明实现要点

---

## 📚 参考资料（来源）

- **来源**：用户上传《讯飞输入法核心机制分析（第一卷，记忆恢复版）》《讯飞输入法深度技术核心分析（第二卷）》《讯飞输入法核心机制全量分析（第三卷）》《讯飞输入法顺畅连贯技术路线（第四卷）》《讯飞输入法业务模块与加密与模型（第五卷）》+ `phn_symbols.txt`（Phoenix C++ 符号精选表）+ 会话逆向分析成果（通过 llvm-nm -C 定位符号、objdump 反汇编 iFlytekInput 二进制提取）
- **目标二进制**：讯飞输入法 iOS v15.0.3606，`iFlytekIME.app/PlugIns/iFlytekInput.appex/iFlytekInput`（46MB Mach-O arm64）
- **反编译方法**：`llvm-nm -C` 定位 vaddr → `extract_func.py <name> <vaddr_hex> <len_hex>` 按 fileoff（=vaddr-0x100000000）`dd` 提取 → `objdump -D -b binary -m aarch64 --adjust-vma=<vaddr>` 反汇编
- **交叉核对/深度比对依据**：`/tmp/nm_all.txt`（31MB 全符号）+ `/tmp/strings_all.txt`（17MB 全字符串）+ `symbols/resfocused.txt`（ObjC selector）+ `backup_bin/*.bin`（原始机器码反汇编）
- **创建日期**：2026-10-23；**版本**：1.11.0（新增「候选解码主路径」反汇编报告：ProcessEmitDecode_common 6字节词项遍历→中英文分流(+33 bit1)→ConstructDecodeNode→MergeOne/N 候选桶完整还原；1.10.0 新增 RNN 资源加载/文件读取反汇编实证：**模型明文读取不加密**，修正此前"解密在资源管理器"推断；1.9.0 含 RNN 模型加载链报告；1.8.0 含版本管理规则（版本号只增不减、内容只追加）；1.7.0 含笔画规则补全 + 候选生产组装 + 排序闭环 RNN 调频写入点 三份新报告；1.6.0 含第五卷 + phn_symbols.txt 符号精选表；1.5.0 含第三、四卷 + 反汇编核对结论 + 深度比对报告 + 联想预测/排序/词库云同步/笔画规则引擎/英文预测查询码 五份子代理报告）
- **关联产物**：
  - `/var/minis/shared/iflytek_analysis/`（分析文档 + 完整 Mach-O 二进制 + 符号/字符串表 + backup_bin + 子代理报告 双保险副本）
  - `/var/minis/skills/iflytek-analysis/references/`（本技能十二份文档）
- **完整二进制**：`/var/minis/shared/iflytek_analysis/bin/iFlytekInput`（46MB，SHA256 bfd785b4...c0f4），IPA 源 `/var/minis/shared/iflytek_analysis/ipa/iflytek_v15.0.3606.ipa`（SHA256 8851769e...da8f）
- **来源文档版本**：第一卷（记忆恢复版，7292B）；第二卷（用户上传 12000B）；第三卷（用户上传 14476B）；第四卷（用户上传 11582B）；第五卷（用户上传 10503B，2026-10-24）；phn_symbols.txt（用户上传 5530B / 344 行，2026-10-24）
- **范围过滤**：第五卷与 phn_symbols.txt 均已核验为纯讯飞内容（Phoenix 符号/讯飞业务模块），无需剔除其它平台内容