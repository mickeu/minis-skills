---
name: iflytek-analysis
description: "讯飞输入法 v15.0.3606 深度技术分析知识库（Phoenix 引擎、词频调频、联想、造词、分词、笔画解码、词库二进制格式、RNN 模型、桥接层/CTRL指令、顺畅连贯机制、云端接口、跨屏、埋点灰度、表情数据系统、安全风控、业务模块/账号支付/加密机制、**键盘布局反编译数据（26键/笔画/符号三面板真实 ini 坐标，跨会话可用）**，含五卷分析 + 反汇编交叉核对结论 + 18 份反汇编报告 + Phoenix 符号精选表 + **键盘布局全量数据（13套键盘×6分辨率 75个ini全解码，跨会话可用）**）。供 0点输入法（自研输入法，只做笔画+英文+符号，不做拼音）逆向参考与算法透明移植。触发词：讯飞分析、讯飞输入法分析、Phoenix 引擎、词频调频、RnnResort、词库格式、iflytek-analysis、讯飞协议、云输入、联想、造词、顺畅连贯、笔画输入、加密机制、RNN模型结构、讯飞键盘布局、键盘反编译、26键还原、bihuakey、26enkey、symbolkey、讯飞皮肤、皮肤配色、color.ini、theme_info。"
version: 1.15.0
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
| `notes/键盘布局数据全量清单.md` | **键盘布局数据全量解码（2026-10-24 新增，123KB/762行）**：`iOS系统布局/` 全部 75 个 ini、2177 个键/列表定义，13 套键盘（26cnkey/26enkey/9key/9key_double/9numkey/9enkey/bihuakey/handkey/13cnkey_cl/cnNumkey/enNumkey/cnFuhaoboard/enFuhaoboard）完整按键表（375 基准），6 档分辨率（320/375/414/568/667/736）差异，PANEL/HW_FRAME/行列/尺寸/间距统计，STAT/POP/DH/CODE/BACK_STYLE 全局值域及语义，bihuakey 笔画键盘专项，handkey 手写区域，Symbol.plist 解码，经典/点划布局族差异，特殊键识别索引 | 键盘布局数据 |
| `notes/键盘布局生成逻辑_反汇编报告.md` | **布局生成逻辑反汇编（2026-10-24 新增）**：INI 文本→分节二维字典→KeyStructGenerator/CandKeyStructGenerator→运行时键结构对象。逐函数解读：IniFileParser_parseIni 分节/键值解析/大小写选项/重复section覆盖；KeyStructGenerator_structWithDic 字段读取+对象构造+CGRectFromString/UIEdgeInsetsFromString+子图frame；POP/DH/STAT/CODE/TAG 类型默认值存储；mapStringToString 控制流；主键与候选栏键差异；完整字段映射表+数据流图+可移植伪C | 布局生成逻辑 |
| `notes/键盘映射核心逻辑_反汇编报告.md` | **键盘映射核心反汇编（2026-10-24 新增，24KB/491行）**：InputKey/OutputMap/Layout/LayoutCoord/KeyMap 结构体字段恢复；26键/9键中心坐标生成与查询算法；KeyMapping+公共映射子函数控制流；默认及自定义双拼映射链；256项模糊拼音代换表+bitmask规则；点击/26键滑动/9键滑动纠错公式；LayoutImp接口层与KeyLayout核心层关系；按键事件到Phoenix候选解码完整数据流；可移植C伪代码 | 键盘映射核心 |
| `notes/键盘类型管理与切换逻辑_反汇编报告.md` | **键盘类型管理与切换反汇编（2026-10-24 新增，23KB/502行）**：KeyboardTypeManager_getNewKBType 参数ABI/9项跳表/安全模式/插件覆盖；键盘类型值与布局族证据分级表；KeyboardConfig 单例/状态字段/动态方法解析；GlobalKeyManager 下一键盘/指定切换/重建/弱引用视图链路；FileParser 空实现与IniFileParser completion解析链；高度增量公式/设备分支/布局缩放/单手镜像；用户操作到显示完整时序；可移植伪C | 类型管理/切换 |
| `notes/RNN反量化算法_反汇编报告.md` | **int8→float 缩放反量化算法逐指令实证（修正：反量化不在 Parser 层，而在运行时 GEMM 内核）**：①`ParserDnnlayer<T,T0>`/`ParserWeightBias<T,T0>` 只是**序列化结构解析**（搜索 `"dense"`/`"bias"`(0x73616962) magic 标签、建层对象、拷字段），`Iff` 与 `Ias`/`Iaa` 代码几乎逐字节相同，**模板类型差异不产生反量化指令**。②真正反量化在 `RnnInstFix::DnnOp`(0x1013f303c)→`MatrixMulThreadPool::mul_thr_sgemm_int8`(0x100bf871c)→`build_tasks_int8`(0x100bf9a1c) 派发→`service`(0x100bfffd0) 线程→GEMM 内核。③GEMM 内核跳板 `fmul s0,s1,s0`=**两个矩阵 scale 相乘**；主循环 `gemm_main_A`(0x100bf7ae0)/`B`(0x100bf7c9c) 用 `smull`(int8×int8→int16)+`sadalp`(→int32) NEON 定点累加，最后 `scvtf`(int32→float)→`fmadd acc×scale ±0.5`(符号舍入)→`fcvtzs` 写回 int32。④输出层 `DnnOp` 内联：`out=clamp(round(查表×scale+0.5),0,127)`，scale 存层对象偏移 1780。⑤算法=**对称线性量化（仅 scale，无 zero-point）**：`C=round(Σint8×int8 × (scale_a×scale_b))`，输出保持 int32 定点。**修正旧建议**（反汇编 ParserWeightBias 看反量化已证伪）。含全部真实地址、指令解读、公式、产物归档（notes/rnn_quant/*.asm） | 模型/RNN反量化 |
| `notes/候选解码主路径_反汇编报告.md` | **候选解码主路径完整还原（ProcessEmit→DecodeArcState→候选桶）**：①`ProcessEmitDecode_common`(0x1013e5e1c)核心循环逐指令还原：**6 字节词项遍历**（`add x26,x26,#0x6`）→`ldrh w8,[x26,#4]` 取词项ID→查表 `ldrh w8,[x9,w8,uxtw#1]`→`ldrb w9,[x9,x8]` 校验有效位→清零 rank（`stp wzr,wzr,[x19,#44]`）→在 DecodeArcState 链 `madd x9,x8,x17,x9`（x17=0x18 即 24B 步进）定位→遍历链找匹配节点。②**中英文分流依据**：关联对象 `+33 bit1`（`tbnz w8,#1` → 走 `_eng` 否则 `_chn`）。③`ProcessEmitDecode_process_chn`(0x1013e6974)/`_eng`(0x1013e6374) 生成**中间候选并入 vector**，均**不直接调用 ConstructDecodeNode**。④`ConstructDecodeNode`(0x1013acf58) 经 0x10138d564 创建最终节点；`NodeCreator::CreateNode`(0x10138de40) 是**另一条** NodeCreator 路径，不可混同。⑤`SetInfo`(0x10138e0b0) 精确恢复 DecodeNode 字段来源：`+0/+8/+16/+24/+32/+40/+43/+44/+48/+50/+51`。⑥`MergeOne`(0x1013adec4)/`MergeN`(0x1013ad5a4)/`MergeOneForPC`(0x1013adb20) 是**类型/flags/边界驱动的链式组合与回收机制**，不是简单"同词去重保高分"。⑦完整主路径：ProcessStroke→DecodeArcState→ProcessEmitDecode_common→_chn/_eng→ConstructDecodeNode→MergeOne/N→候选桶。含函数地址/大小、寄存器、数据结构偏移、文字 CFG、伪 C、Rime/笔画移植建议；rank 偏移/Merge 精确比较键/英文变体 bit 已标"待验证"未臆测 | 候选解码主路径 |
| `notes/解码词项遍历与ProcessStroke哈希_反汇编分析.md` | **词项遍历逻辑逐指令分析 + ProcessStroke 哈希算法验证（2026-10-24 新增）**：①`ProcessEmitDecode_common`(0x1013e5e1c) 6 字节词项遍历逐指令还原：词项布局=**偏移0低24bit笔画码 + 偏移4 16bit词项ID**；循环 `add x26,x26,#0x6` 步进 → `ldrh w8,[x26,#4]` 取词项ID → `ldrh w8,[x9,w8,uxtw#1]` 半字查表得索引 → `ldrb w9,[x9,x8]` 校验有效位 → `stp wzr,wzr,[x19,#44]` 清零 rank → DecodeArcState 链 `madd x9,x8,x17,x9`(x17=0x18=24B步进) 定位 → 遍历链匹配候选节点指针数组（8字节元素）→ 关联对象 `+33 bit1` 分流 `process_chn`(0x1013e6974)/`process_eng`(0x1013e6374)。②**ProcessStroke(0x10102a5d4) 哈希算法验证**：`mvn→lsl#21→eor lsr#24→mul 0x109(265)→eor lsr#14→mul 0x15(21)→eor lsr#28→mul 0x80000001` = **MurmurHash3 风格 64 位 fmix 混合**；`hash & (size-1)` 取桶 + 开放寻址线性探测；词项节点结构 `[+8]=64bit哈希值`、`[+16]=16bit词id`。新增反汇编产物 `notes/decodepath/ProcessStroke.asm`（15133B） | 解码遍历/笔画哈希 |
| `notes/常用语面板_反汇编报告.md` | **工具→常用语 三合一面板（常用语/快捷回复/剪贴板）完整还原 + 快捷回复词句全量提取**：①容器架构=`UIPanelViewController`（`createBasePanelViewControllerWithType:` 0x1001ad9f8 跳转表按 type 创建子 VC），三个子 VC=常用语`UICommonPhrasePanelViewController`/快捷回复`UIGreetingPanelViewController`/剪贴板`UIClipboardPanelViewController`，`showPanelWithType:` 仅由容器内部调用（xref 2 处）。②快捷回复多子项=`UIQuickReplyPanel` 的 `cateList`(分类tab)+`localContentList`(词句列表)，`rebuildCategoryList`(0x1000052f0)/`rebuildContentList`(0x100004ff0)/`p_onMenuTapped:`(0x100005f18)/`list:didSelectAtIndex:isUserTouch:`(0x10000601c)。③数据源=`ss/quickReply.plist`，**AES-256-CBC** 加密（Key=`j9f7zblqg6hsm5t0e2dr3k1o4p8cxnvy` IV=`3y4k9j2zq8s0l1d6`），解密链 `ss_arrayWithContentsOfFile:`(0x100418b10)→`ss_dictionaryWithContentsOfFile:`(0x1004197c8)→`Cryptor`(0x10044b1d8)；QuickReplyItem 字段=title/uid/contents。④**快捷回复内置词句全量（7分类80句）**已提取：表白13/夸夸14/群聊10/打鸡血13/回复红包10/回复谢谢11/回复祝福9，见 `notes/快捷回复词句.txt` + `notes/quickReply.plist`。⑤常用语数据=`CommonPhraseDataManager` NSCoder 归档（用户自定义）+`p_defaultCommonPhrases` 默认数据。源码工程目录剪贴板 Swift 文件位于 `程序/UI层/面板/常用语面板/剪贴板/`，证实剪贴板为常用语面板子模块 | 常用语面板/快捷回复/剪贴板 |
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
# /var/minis/skills/iflytek-analysis/references/notes/键盘布局数据全量清单.md
# /var/minis/skills/iflytek-analysis/references/notes/键盘布局生成逻辑_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/键盘映射核心逻辑_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/键盘类型管理与切换逻辑_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/rnn_resloader_disasm.md
# /var/minis/skills/iflytek-analysis/references/notes/候选解码主路径_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/解码词项遍历与ProcessStroke哈希_反汇编分析.md
# /var/minis/skills/iflytek-analysis/references/notes/RNN反量化算法_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/rnn_quant/*.asm（RNN 量化/GEMM 21 个反汇编中间产物）
# /var/minis/skills/iflytek-analysis/references/notes/常用语面板_反汇编报告.md
# /var/minis/skills/iflytek-analysis/references/notes/快捷回复词句.txt
# /var/minis/skills/iflytek-analysis/references/notes/quickReply.plist
# /var/minis/skills/iflytek-analysis/references/讯飞键盘布局反编译数据.md
# /var/minis/skills/iflytek-analysis/references/讯飞皮肤数据总索引.md   ← 讯飞皮肤入口（涉及皮肤先读此文件）
# /var/minis/skills/iflytek-analysis/references/讯飞键盘配色规格.md
# /var/minis/skills/iflytek-analysis/references/skin/   ← 皮肤 color.ini（浅/深配色字段）+ theme_info.ini（多套主题）
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
> **涉及讯飞皮肤时，先读 `references/讯飞皮肤数据总索引.md`（一站式入口，索引全部皮肤/配色/布局/分析数据）。**

#### 10a. 皮肤配色与主题系统（2026-10-24 新增，跨会话可用）
- **皮肤总索引**：`references/讯飞皮肤数据总索引.md`（涉及皮肤先读此文件，含全部数据路径清单）
- **配色规格**：`references/讯飞键盘配色规格.md`（6张参考图 PIL 像素采样，日夜两套精确 hex）
- **皮肤配色系统 color.ini**：`references/skin/light_color.ini`(37KB) + `dark_color.ini`(20KB)（App 级配色字段定义，`[xxx.color] color_value=rrggbb`，含基础色/品牌色/容器/文本层级/按钮/导航/标签栏等）
- **皮肤主题包 theme_info.ini**：`references/skin/{SystemTheme,white,black,NightShift,mutiletheme,mutiletheme_night,customedskin}_info.ini`（多套主题定义）
- **原始路径**：`/var/minis/shared/myime/skin/`（同上，跨会话可读）

#### 10b. 键盘布局坐标

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

## 📦 素材与产物归档清单（2026-10-24 完整归档，跨会话可调用）

> 本技能 references/ 下**已完整归档**全部逆向分析产物（报告 + 反汇编 + 模型 + 工具脚本），跨会话直接 `file_read` 技能库路径即可调用，无需再访问 shared。大体积二进制/IPA/符号表保持 shared 持久目录（跨会话可读），路径见下。

### 1. 反汇编报告（references/notes/，14 份）
全部已入技能库：排序、排序闭环_RNN调频、联想预测、词库云同步、笔画规则引擎、笔画规则引擎_补全、英文预测与查询码、候选生产组装、候选解码主路径、RNN模型加载与格式、rnn_resloader_disasm、**常用语面板**、**RNN反量化算法**、**键盘布局数据全量清单**、**键盘布局生成逻辑**、**键盘映射核心逻辑**、**键盘类型管理与切换逻辑** + 7 份卷文档。RNN 量化/GEMM 反汇编中间产物在 `rnn_quant/` 子目录（21 个 .asm）。键盘反汇编切片在 `references/disasm_keyboard/`（38 份 .asm + `full/` 完整版）。完整索引见上方「参考资料索引」表。常用语面板目录下另有 `快捷回复词句.txt`（7分类80句全量）与 `quickReply.plist`（解密后 XML）。

### 2. 解码主路径反汇编产物（references/notes/decodepath/，28 个文件）
- 14 个函数 `.asm`（objdump 反汇编，vma 已调整）+ `.bin`（原始机器码）：
  ProcessEmit / ProcessArcOut / ProcessArcOut_word / ProcessEmitDecode_cache / ProcessEmitDecode_common / ProcessEmitDecode_process_eng / ProcessEmitDecode_process_chn / ConstructDecodeNode / ConstructDecodeNodeInScene / MergeN / MergeOne / MergeOneForPC / CreateNode / SetInfo
- 提取方法：`python3 /tmp/extract2.py <bin> <start_hex> <end_hex> <out.bin>`（file_offset = vaddr - 0x100004000 + 0x4000），`objdump -D -b binary -m aarch64 --adjust-vma=<函数地址>` 反汇编

### 3. RNN 模型素材（references/rnn_model/，5 个文件）
- `rnn_model_940e67abb4.bin`（4.2MB 模型原文件）
- `rnn_load.asm`（RLRnn::load 反汇编 478 行）、`parse_matrix.bin`、`rnn_loadres_f.bin`、`rnn_start.bin`

### 4. 函数裸机器码切片（references/backup_bin/，93 个 .bin）
- 100+ 函数原始机器码（AIChatMessage_encode / AIInstructionRunner_run / RnnReScore / CalcCombineScore / ProcessStroke 等），objdump -b binary 直接反汇编

### 5. 云同步反汇编（references/asms_cloud_sync.txt，245KB）
- 云同步 15 函数反汇编全文（Lex_onSync / uploadData / downloadData / deleteData / cloud_prepare / merge / requestResponse 等）

### 6. 反汇编工具脚本（references/tools/，6 个）
- `dis.sh` / `dis.py` / `dis2.py` / `analyze_dis.py` / `batch_dis.py` / `objc_methods.py`（提取函数字节、批量反汇编、ObjC 方法定位）

### 7. 键盘布局反编译数据（references/disasm_keyboard/，38 个文件 + references/讯飞键盘布局反编译数据.md）
- 26键/笔画九宫格/符号面板 真实坐标与 CODE（详见第 10 节），配合 `/var/minis/shared/myime/ime_res/*.ini`

### 8. 大体积素材（保持 shared 持久目录，跨会话可读，不复制进技能库）
- `/var/minis/shared/iflytek_analysis/bin/iFlytekInput`（46MB，输入法扩展主二进制，SHA256 bfd785b4...c0f4）
- `/var/minis/shared/iflytek_analysis/bin/iFlytekIME`（89MB，主 App 二进制，**含全部解码符号**，真实地址 0x1013exxxx 系）
- `/var/minis/shared/iflytek_analysis/ipa/iflytek_v15.0.3606.ipa`（194MB 原始安装包）
- `/var/minis/shared/iflytek_analysis/symbols/`（nm_all_full.txt 17MB、nm_demangled.txt 17MB、objc_selectors.txt 等 12 个）
- `/var/minis/shared/iflytek_analysis/strings_all_full.txt`（15MB，349744 行全字符串）
- `/var/minis/shared/iflytek_analysis/README_素材清单.md`（素材总清单）

---

## 📚 参考资料（来源）

- **来源**：用户上传《讯飞输入法核心机制分析（第一卷，记忆恢复版）》《讯飞输入法深度技术核心分析（第二卷）》《讯飞输入法核心机制全量分析（第三卷）》《讯飞输入法顺畅连贯技术路线（第四卷）》《讯飞输入法业务模块与加密与模型（第五卷）》+ `phn_symbols.txt`（Phoenix C++ 符号精选表）+ 会话逆向分析成果（通过 llvm-nm -C 定位符号、objdump 反汇编 iFlytekInput 二进制提取）
- **目标二进制**：讯飞输入法 iOS v15.0.3606，`iFlytekIME.app/PlugIns/iFlytekInput.appex/iFlytekInput`（46MB Mach-O arm64）
- **反编译方法**：`llvm-nm -C` 定位 vaddr → `extract_func.py <name> <vaddr_hex> <len_hex>` 按 fileoff（=vaddr-0x100000000）`dd` 提取 → `objdump -D -b binary -m aarch64 --adjust-vma=<vaddr>` 反汇编
- **交叉核对/深度比对依据**：`/tmp/nm_all.txt`（31MB 全符号）+ `/tmp/strings_all.txt`（17MB 全字符串）+ `symbols/resfocused.txt`（ObjC selector）+ `backup_bin/*.bin`（原始机器码反汇编）
- **创建日期**：2026-10-23；**版本**：1.15.0（新增「解码词项遍历与ProcessStroke哈希」反汇编分析：`ProcessEmitDecode_common` 6字节词项遍历逐指令还原（词项布局=偏移0低24bit笔画码+偏移4 16bit词项ID、半字查表、有效位校验、清零rank、DecodeArcState 24B步进链遍历、关联对象+33 bit1中英文分流），并反汇编 ProcessStroke(0x10102a5d4) 验证 **MurmurHash3 风格 64 位 fmix 哈希 + 开放寻址探测**，新增产物 notes/decodepath/ProcessStroke.asm；1.14.0 新增「RNN反量化算法」反汇编报告：**int8→float 反量化在运行时 GEMM 内核（非 Parser 层）**，`smull/sadalp` int32 定点累加 + `scvtf→fmadd acc×(scale_a×scale_b)±0.5→fcvtzs`，输出层 `clamp(round(查表×scale+0.5),0,127)`，含全部真实地址与 21 个反汇编产物 notes/rnn_quant/；1.13.0 新增「常用语面板」反汇编报告：工具→常用语三合一面板（常用语/快捷回复/剪贴板）容器架构 UIPanelViewController + createBasePanelViewControllerWithType 跳转表 + 快捷回复子项实现 + **ss/quickReply.plist AES-256-CBC 解密**（Key/IV 已确认）+ **快捷回复内置词句全量 7 分类 80 句提取**（notes/快捷回复词句.txt + notes/quickReply.plist）；1.12.0 新增「素材与产物归档清单」章节：全部反汇编产物/RNN模型/工具脚本完整归档进 references/，标注大体积素材路径跨会话可调用；1.11.0 新增「候选解码主路径」反汇编报告：ProcessEmitDecode_common 6字节词项遍历→中英文分流(+33 bit1)→ConstructDecodeNode→MergeOne/N 候选桶完整还原；1.10.0 新增 RNN 资源加载/文件读取反汇编实证：**模型明文读取不加密**，修正此前"解密在资源管理器"推断；1.9.0 含 RNN 模型加载链报告；1.8.0 含版本管理规则（版本号只增不减、内容只追加）；1.7.0 含笔画规则补全 + 候选生产组装 + 排序闭环 RNN 调频写入点 三份新报告；1.6.0 含第五卷 + phn_symbols.txt 符号精选表；1.5.0 含第三、四卷 + 反汇编核对结论 + 深度比对报告 + 联想预测/排序/词库云同步/笔画规则引擎/英文预测查询码 五份子代理报告）
- **关联产物**：
  - `/var/minis/shared/iflytek_analysis/`（分析文档 + 完整 Mach-O 二进制 + 符号/字符串表 + backup_bin + 子代理报告 双保险副本）
  - `/var/minis/skills/iflytek-analysis/references/`（本技能全部文档 + 报告 + 反汇编产物 + RNN 模型 + 工具脚本，含 notes/decodepath、backup_bin、rnn_model、tools、disasm_keyboard、asms_cloud_sync 等子目录，191+ 文件，完整归档）
- **完整二进制**：`/var/minis/shared/iflytek_analysis/bin/iFlytekInput`（46MB，SHA256 bfd785b4...c0f4），IPA 源 `/var/minis/shared/iflytek_analysis/ipa/iflytek_v15.0.3606.ipa`（SHA256 8851769e...da8f）
- **来源文档版本**：第一卷（记忆恢复版，7292B）；第二卷（用户上传 12000B）；第三卷（用户上传 14476B）；第四卷（用户上传 11582B）；第五卷（用户上传 10503B，2026-10-24）；phn_symbols.txt（用户上传 5530B / 344 行，2026-10-24）
- **范围过滤**：第五卷与 phn_symbols.txt 均已核验为纯讯飞内容（Phoenix 符号/讯飞业务模块），无需剔除其它平台内容