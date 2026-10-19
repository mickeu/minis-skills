---
name: rime-wanxiang-ios
description: 万象拼音 Rime 输入方案（rime-wanxiang）及其 iOS 资源包（ResourceforHamster）的完整知识库。涵盖方案结构（Base/Pro/Lite/Pure）、iOS 前端（元书/仓/Weasel）部署、元书输入法 Hamster3 部署指南、WanxiangSkin 元书皮肤架构与修改 playbook。当用户提到万象拼音、rime-wanxiang、ResourceforHamster、WanxiangSkin、元书输入法、仓输入法、Hamster3、天枢输入法、Rime iOS 部署时使用。
---

# 万象拼音 iOS 生态（rime-wanxiang + ResourceforHamster）

> 用途：为「天枢输入法」改造提供参考。天枢（TianShu，tianshuapp.tech）是本地运行的多角色 AI Agent 工作台，口号"枢转万象"。用户表示后续改天枢输入法时需用本技能库。万象方案与元书皮肤的相关改造方法论沉淀于此。

两个上游仓库：
- **rime-wanxiang**：万象拼音方案本体（方案文件 + 词库 + Lua 扩展 + 文档）
- **ResourceforHamster**：万象在 iOS 前端的资源包（元书皮肤、各前端自定义配置、键盘脚本、皮肤修改 skill）

## 一、万象拼音方案（rime-wanxiang）

「语句流」级全拼/双拼方案，核心是 **万象词库**（来自 `amzxyz/RIME-LMDG`，AI + 海量语料优化，带调拼音标注、词组构成与精准词频），配大量 Lua 扩展。

### 四种发行版本

| 版本 | 定位 | 输入方式 | 词库 | Lua 扩展 | 主方案文件 |
|---|---|---|---|---|---|
| Base | 完整标准版（默认首选） | 全拼+双拼 | 完整带调 | 完整 | `wanxiang.schema.yaml` |
| Pro | 双拼+辅助码增强 | 双拼+多套辅助码 | 独立 Pro 辅助码词库 | 完整增强 | `wanxiang_pro.schema.yaml` |
| Lite | 轻量现代版 | 全拼+双拼 | 无声调 | 保留常用 | `wanxiang_lite.schema.yaml` |
| Pure | 原生兼容版（Win7/fcitx4 无 Lua） | 全拼+双拼 | Pure 专用 | 无 | `wanxiang_pure.schema.yaml` |

### 关键文件（仓库根目录）

- 方案：`wanxiang*.schema.yaml`（含 t9 / t9i / abbrev / english / mixedcode / phrase / reverse 等子方案）
- 词库：`wanxiang.dict.yaml`、`wanxiang_reverse.dict.yaml`（约 6.5MB 反查库）、`dicts/*.dict.yaml`（zi/jichu/lianxiang/renming/diming/duoyin/yixue 等分库）
- 规则：`wanxiang_algebra.yaml`（136KB 转写规则）
- 自定义：`custom/*.custom.yaml`、`custom/aux_code.csv`（辅助码）、`custom/jm_flypy.txt`（小鹤）、`custom/jm_zrm.txt`（自然码）
- Lua 扩展：`lua/wanxiang/*.lua`（super_symbols、super_lookup、super_calculator、super_comment、auto_phrase、custom_phrase、random_tools、unicode_conversion 等数十个）+ `lua/data/`（codex_sym/emoji/english_chinese/chaifen 等数据）
- 配置：`default.yaml`、`weasel.yaml`
- 文档：`docs/doc/*.md`（含 `hamster3.md` iOS 部署、`intro.md` 快速上手、`aux_code.md` 辅助码、`dict_gram` 词库与模型）

## 二、ResourceforHamster（iOS 资源包）

面向 iOS 输入法前端，作者推荐 **元书输入法**（Hamster3）。

### 目录结构

```
Custom_Keyboard/       # 自定义键盘配置（不推荐使用）
Skin_Keyboard/
  万象-元书/            # 元书输入法万象皮肤（推荐，iPad 可用）
     WanxiangSkin/     # 皮肤 Jsonnet 源码工程
     WanxiangSkin-modifier/  # 皮肤修改 skill（SKILL.md + references）
  万象-仓/              # 仓输入法皮肤（不再更新，不推荐）
  雾凇等 archive/
Keyboard_Script/       # 键盘脚本（encode_url/base64/pass_gen/小鹤反查/去空格/提取链接/兑换码）
Input_Method/万象拼音/
  Rime4Hamster/        # 元书自定义配置（含 wanxiang_14/17/18 方案 + custom）
  Rime4Weasel/         # Windows 小狼毫
  Rime4Fcitx5orSquirrel/ # Linux fcitx5 / macOS 鼠须管
Python_Tools/          # 仅适用于仓皮肤修改，不再维护
Fcitx5-CSS-Theme/      # Linux 候选框主题
```

### iOS 前端选择

- **元书输入法**（Hamster3）：推荐。App Store `元书输入法` id6744464701。皮肤持续更新，iPad 可用。
- **仓输入法**（Hamster）：App Store id6446617683。皮肤不再更新，不推荐。
- 方案管理工具：`rimeinn/rime-wanxiang-update-tools`（全平台）；iOS 可视化可用作者的另一仓库 `BlackCCCat/Scripting-Scripts`（基于 Scripting App）。

## 三、iOS 部署指南（元书输入法 Hamster3）

> 完整版见 `rime-wanxiang/docs/doc/hamster3.md`。

1. **启用键盘**：设置 → 通用 → 键盘 → 添加「Hamster」→ 开启【允许完全访问】（否则万象 Pro 双拼切换和 Lua 功能不可用）。
2. **建独立目录**：文件 App → `我的 iPhone/元书输入法/RimeUserData/` → 新建文件夹 `wanxiang`。
3. **导入方案**：元书 App →【输入方案】→ 菜单【下载方案】（填 Release `.zip` 链接）或【导入方案】→ 完成后【方案目录切换】到 `wanxiang`。
4. **部署**：【刷新】按钮执行首次部署。注意 `/` 等参与 Rime 编码的按键应由 Rime 处理，不要由前端直接上屏。
5. **文件同步机制**（关键坑）：元书部署前自动把键盘文件同步回应用目录，默认只含 `text`/`userdb`，**不含 `.yaml`**。
   - 路线 A（自动同步斜杠指令产生的 custom）：把 `include_keyboard_rime_files.txt` 复制到 `wanxiang` 目录，并新增一行 `^.*[.]custom.*$`。⚠️ 开启后 custom 文件以键盘端为同步来源，电脑端修改会被键盘旧文件覆盖。
   - 路线 B（手动维护）：不改同步范围，custom 修改手动用文件 App/文本编辑器编辑 `RimeUserData/wanxiang`。
6. **初始输入方式**：Base 默认全拼；Pro 默认自然码双拼。建议执行一次斜杠指令切换（详见 `docs/doc/slash_commands.md`）后回 App 点【刷新】。

## 四、WanxiangSkin 元书皮肤工程

Jsonnet 源码工程，公开配置集中在 `jsonnet/Custom.libsonnet`。

### 特性

- 中文键盘 9/14/17/18/26/27 键；英文统一 26 键
- `enable_layout_switcher`（默认 false）：开启后构建全部布局，经工具栏 `keyboard_switcher` 切换并绑定对应方案（9→wanxiang_t9i、14→wanxiang_14、17→wanxiang_17、18→wanxiang_18、26/27→wanxiang_pro）
- iPhone 横竖屏、iPad 四行/浮动键盘、浅色/深色、iOS 26 风格
- 功能行、预编辑通知、上下划/长按菜单、候选词操作（左移/右移/重置/置顶/移除）、纵向候选
- 中文 26 键 `swipe_assist_mode`（none/up/down/all）滑动大写辅助

### 安装方式

1. **打包皮肤**：Releases 下载 `WanxiangSkin.cskin` → 传到 iPhone → 用元书打开导入 → 皮肤页选「万象键盘」→ 部署配套 Rime 配置后重新部署。也有 iCloud 快捷指令自动下载导入。
2. **源码自定义**：元书开「皮肤开发者模式」→ 导入 `WanxiangSkin/` 目录 → 改 `jsonnet/Custom.libsonnet` → 点皮肤触发生成，或长按皮肤手动运行 `main.jsonnet`（改后必须重新运行，YAML 不会自动更新）。

### 验证命令

```bash
cd <keyboard-root>  # 即 WanxiangSkin 目录
jsonnet jsonnet/main.jsonnet -o /tmp/WanxiangSkin.json
```

内存受限环境报 `FATAL ERROR: memory allocation error` 时，改在电脑或元书开发者模式构建。

## 五、WanxiangSkin 修改方法论（维护 skill 摘要）

> 完整内容见 `references/wanxiangskin-modifier-SKILL.md`、`references/playbooks.md`、`references/file-map.md`（已本地化）。以下为骨架，动手前务必读全。

### 架构边界（不可破坏）

- `main.jsonnet` 只引用 `build`；键盘入口经 `build/context.libsonnet` 解析设备/布局上下文
- `components` 不引用具体键盘族；`design` 不引用 `components`
- 键盘专属长按/滑动数据在对应键盘族 `data.libsonnet`；`tempPinyin` 可复用拼音 26 键
- `Custom.libsonnet` 是公开配置唯一入口；不重建 `entries/`、`shared/`、`keyboards/common/`

### 修改优先级（从最窄责任层开始）

配置 → `jsonnet/Custom.libsonnet`
构建映射 → `jsonnet/build/`
视觉 → `jsonnet/design/appearance.libsonnet`（颜色/字号/偏移/高度）+ `styleFactories.libsonnet`
按键 → `jsonnet/components/key/`；拼音系统键 → `components/systemKeys/`
功能行 → `components/functionRow/`；工具栏 → `components/toolbar/`；候选栏 → `components/candidates.libsonnet`
键盘专属行为 → `jsonnet/keyboards/<family>/`

### 不可回退的数据

- `components/systemKeys/longPressData.libsonnet` 的 `cn2en.list` 用 `rimeOptionLabel$<option>` 动态标签
- 中文 26 键 KP 标签以 `keyboards/keyboard26/pinyin/data.libsonnet` 为准
- iPad 已调尺寸在 `keyboard26/base/iPadLayout.libsonnet`，无需求不做顺带调整

### 关键功能落点

- 布局切换：受 `Custom.enable_layout_switcher` 总开关控制；关闭时只产出默认布局，工具栏 `keyboard_switcher` 被过滤。⚠️ `keyboardType` 切换只对当前会话有效，收起重开恢复 `pinyin` 主槽——**不要宣称六布局可持久记忆**。
- 滑动辅助：`swipe_assist_mode` 仅中文 26 键，改 `keyboard26/pinyin/swipeAssist.libsonnet`
- 系统键：退格/空格/回车 → `systemKeys/editing.libsonnet`；Shift/中英切换 → `inputMode.libsonnet`；123Button → `keyboardSwitch.libsonnet`；cn2en 长按数据 → `longPressData.libsonnet`
- 回归验证必须覆盖：keyboard_layout 9/14/17/18/26/27、swipe_assist_mode none/up/down/all、light/dark、portrait/landscape、iPhone/iPad

## 六、关联生态

- 万象词库本体：`amzxyz/RIME-LMDG`
- 薄荷拼音（oh-my-rime）：使用万象词库的综合方案
- 鸢鸣万象、李氏三拼、万象虎：万象生态衍生方案
- 万象更新工具：`rimeinn/rime-wanxiang-update-tools`（全平台含 iOS）
- 作者 iOS 方案管理：`BlackCCCat/Scripting-Scripts`（基于 Scripting App）

## 七、天枢笔画输入法参考（BG5CGQ-Stroke-Rime）

> 天枢笔画输入法项目：`mickeu/tianshu-stroke`（基于 Hamster/RIME 的 iOS 键盘开源构建，公开无签名 IPA）。BG5CGQ 是**专为 Hamster 框架做的现成九宫格笔画方案**，天枢基于 Hamster fork，可直接移植/参考。本地副本与参考文件见 `references/bg5cgq-stroke-rime/`。

### 核心资产

- `stroke_bg5cgq.schema.yaml`：Rime 方案定义（数字编码 `alphabet: "12345?'"`，`preedit_format` 把 12345 转笔画图形一丨丿丶乛）
- `stroke_bg5cgq.dict.yaml`：**27,755 字码表 + 20,511 通配变体**
- `hamster.yaml`：九宫格笔画键盘布局（仿百度）+ 深色配色 `stroke_ninegrid_dark`
- 六份文档：使用说明 / 数据源深度分析 / 编码数据推荐 / 详细实施方案 / 部署记录

### 键位（九宫格，数字编码）

```
 ， │ 一(1) │ 丨(2) │ 丿(3) │ ⌫
 。 │ 丶(4) │ 乛(5) │ 分词(6) │ 换行
 ？ │ 通配(7) │ ，(8) │ 。(9) │ 符号
 中英 │ 123 │ 空格 │ 回车
```
上划出数字、下划出符号。编码规范与百度一致：竖钩归竖（丁=12）、提归横（打=121）、捺归点（人=34）。

### 零 Swift 修改（关键优势）

键盘布局、配色、方案**全部通过 YAML 配置**实现，完全复用 Hamster 自定义键盘机制（`keyboards/rows/keys/action.character.char`、`swipe`、`colorSchemas`），无需改 Swift。对天枢这类 fork 项目友好。

### 与天枢现有原型（StrokePrototype，hspnz 字母五键）对比

| 维度 | 天枢 hspnz 原型 | BG5CGQ |
|---|---|---|
| 编码键 | 字母 `h s p n z` | 数字 `1-5` |
| 码表 | 少量示例词组 | 27,755 字 |
| 通配符 | ❌ 未实现 | ✅ 20,511 个 `?` 变体 |
| 分词 | 仅 `'` 分隔符 | ✅ 6 键 + 词组组合 |
| 上下划 | 无 | ✅ 数字/符号 |
| 配色 | 2 个原型色 | ✅ 深色九宫格皮肤 |

### 移植到天枢要点

1. **确认 fork 版本兼容**：天枢基线 Hamster commit 的 `Models.swift` 是否支持 `swipe`、`colorSchemas`、通配键（天枢原型已用 swipe/percentage，大概率兼容，需核对）
2. **布局取舍**：接受九宫格数字布局 → 直接移植 BG5CGQ；保留 hspnz 字母布局 → 改 `speller/alphabet` 和键盘 `char` 映射
3. **集成方式**：`stroke_bg5cgq.schema.yaml` + `.dict.yaml` 打进天枢 SharedSupport，`hamster.yaml` 笔画键盘段合并进天枢 `hamster.custom.yaml`

## 八、重签名后方案目录不生效排查（元书/天枢类输入法）

> 2026-10-12 实战结论。天枢输入法（元书 Hamster3 的 fork，去订阅重签名版）出现「下载方案/压缩包导入显示成功，但方案目录切换为空」，App Store 原版正常。

### 症状
- 「下载方案」显示成功，但「方案目录切换」列表为空
- 「压缩包导入」（用元书打开 zip）也不生效
- 关闭 iCloud 后，iOS 文件 App 的「我的 iPhone」下不出现「元书输入法」文件夹

### 根因（关键）
- **Info.plist 的 `UIFileSharingEnabled = False`、`LSSupportsOpeningDocumentsInPlace = False`**
- → iOS 不在「我的 iPhone」建立 App 文件夹 → `RimeUserData` 不可见、方案无法正常落盘 → 方案目录切换为空
- 容易被误判为 iCloud 容器权限缺失（二进制引用 `iCloud.com.ihsiao.apps.Hamster3`，而新描述文件 `icloud-container-identifiers` 为空）——但**这不是主因**

### 修复
1. 基于可正常安装的版本重新解压
2. 修改主 app + 插件 Info.plist：`UIFileSharingEnabled=True`、`LSSupportsOpeningDocumentsInPlace=True`
3. **不注入任何额外 entitlements**（保持描述文件原始权限）
4. zsign 用原描述文件 + 证书重新签名
5. 安装后文件 App「我的 iPhone」出现元书文件夹 → 方案下载/导入恢复正常

### 反例（装不上）
- 强行用 zsign `-e` 注入 `icloud-container-identifiers`（描述文件没有该权限）→ iOS 直接拒绝安装。描述文件权限是 Apple 后台签发的，**不能靠注入补**。

## 九、BG5CGQ 动态分段造词：真机成功基线

**2026-10-14 用户确认 v7.0「造词完美通过」。** 遇到笔画造词、短码词＋后段字、选词后残留笔画、单笔画/偏旁优先级时，先读 [成功实现与验收纪律](references/bg5-staged-compose.md)。

- 前段短码能成词也要保留；整词命中不应吞前段词和后段候选。
- 当前分段约定下，部分候选消费后置分隔符：`31'12'25112141` 的「我要」范围 `[0,6)`，后段「国」`[6,14)`；不是旧模拟测试的 end=5。
- translator 与 filter 均使用候选局部 preedit；filter 按候选覆盖子段计数，并忽略已消费的末尾分隔符。
- 单笔画、既有偏旁部首显式类别优先，不靠提高词频模拟；同字不同范围按 type/start/end/text 去重。
- 模拟候选/暂存拼接不等于真实点击。v7.0 用户已确认造词真机通过，后续不得在未完成新版本端到端验证时沿用该结论。
- 成功 zip SHA-256：`a65e80d12c46e36b1e9aaf09ef60fdd6b7497c3d9f2322a5605d39bbc0d4b606`；完整来源、复现命令、性能反例见引用文档。

## 十、免电脑穿透沙盒查看真机方案（coredevice-toolkit，2026-10-18 实测）

利用 `coredevice-toolkit` 技能的 `cdtk-fs`，无需电脑即可直接读取元书输入法（自签/改签版）沙盒内「实际生效」的方案与皮肤，适合排查「设备上跑的和源码不一致」「方案目录为空」等场景。

### 前置
- 元书必须是**自签/侧载/开发调试安装**版（如 `com.l8U.4jzG` 改签版）——`house_arrest` 对 App Store 正式应用拒绝访问（报 `InstallationLookupFailed`），这是系统安全策略，非工具问题。
- Surge 回环反射已配置（`10.7.0.1 = reflect`）、配对文件在 `/var/minis/workspace/cdtk/`。

### 实测命令
```bash
cd /var/minis/workspace/cdtk && sleep 2   # 连续调用需等待协议栈清理

# 元书沙盒结构
cdtk-fs app ls com.l8U.4jzG /                          # 根：Documents/Library/SystemData/tmp
cdtk-fs app ls com.l8U.4jzG Documents                  # RimeSharedSupport/RimeUserData/Skins/Backup/Logs
cdtk-fs app ls com.l8U.4jzG Documents/RimeUserData     # 方案目录列表
cdtk-fs app ls com.l8U.4jzG Documents/RimeUserData/BG5CGQ-WanXiang-Rime  # 方案文件清单
cdtk-fs app cat com.l8U.4jzG Documents/RimeUserData/BG5CGQ-WanXiang-Rime/user.yaml  # 看用户状态
```

### 实测到的设备方案结构（iOS 27，2026-10-18）
`Documents/RimeUserData/` 下有两个方案目录：`BG5CGQ-WanXiang-Rime` 与 `rime-ice`。
`BG5CGQ-WanXiang-Rime/` 含 33 项，关键文件：
- 主方案：`stroke_bg5cgq_learning.schema.yaml`、`wanxiang.schema.yaml`、`wanxiang_orig.schema.yaml`
- 码表：`stroke_bg5cgq.dict.yaml`（~79 MB）、`stroke_bg5cgq_single.dict.yaml`、`wanxiang_reverse.dict.yaml`（~6.5 MB）、`custom_phrase*.dict.yaml`
- 依赖：`predict.db`（~7.5 MB）、`wanxiang_algebra.yaml`、`wanxiang_symbols.yaml`、`opencc/`、`lua/`
- 配置：`hamster.yaml`（~76 KB）、`default.custom.yaml`、`wanxiang.custom.yaml`

### 坑
- 连续 `cdtk-fs` 调用之间加 `sleep 2~3`，避免 pmd-pytcp 协议栈 ARP Cache 竞态报错。
- 沙盒读取是只读穿透，不要直接改沙盒内文件；提取用 `cdtk-fs app pull`，修改仍走文件 App / 挂载目录工作副本流程。

### 2026-10-19 深度审查补充（重要）

**⚠️ 方案目录名带冲突后缀**：设备上实际目录名是 `BG5CGQ-WanXiang-Rime (1)`（iOS 文件冲突自动加 ` (1)`），内层才是方案根。Rime 实际 userDataPath（app.log 确认）= `Documents/RimeUserData/BG5CGQ-WanXiang-Rime (1)/BG5CGQ-WanXiang-Rime/`。直接 `cdtk-fs app ls .../BG5CGQ-WanXiang-Rime` 会报 `AfcFileNotFoundError`；用 python 脚本 `listdir` + `repr()` 才能看清真实目录名。zip 还带入 `__MACOSX` 残留。

**设备实际版本比技能库 v8.0 新**（哈希对比 v8.0 zip 结论）：
- `lua/learning.lua` 设备是 **v11**（新增 30 天半衰期时间衰减遗忘机制，选错的词自动降权/清除），技能库 v8.0 计算器版 zip 是 v10。
- `lua/filter_seg_count.lua`（按有效笔画码段计数 + 纯分词符全量放行）、`lua/head_words.lua`（848→2189 行，并入语料新词）、`lua/words.lua`（8.9MB 真实语料校准词频）、`lua/segment_phrase.lua`（新增 ngram 容错加载 `pcall`）均比 v8.0 新。
- ⚠️ **技能库 `references/bg5cgq-dynamic/v8.0/` 存档落后于设备实际，需要把设备增强版 lua 回存为 v8.1+**，否则从技能库恢复会丢时间衰减等新功能。
- 设备生效 schema：`stroke_bg5cgq_learning.schema.yaml` v8.0 增强完整版（7006B），含预测/ngram/上下文调频/字符集过滤/简繁切换/局部提交/自定义置顶词。

**皮肤审查**：Skins 下 `多功能大包-计算版-v106`（light/dark 双主题 ×15 布局 + sound + resources）。⚠️ 目录名 v106 但 `config.yaml` 内 `name: 多功能大包-计算版-v105`，版本号未同步，需修正。

**python 脚本直连坑**：`coredevice_session` 装在 site-packages 但 `tls_psk_proxy.js` 只在技能 `scripts/`，python 直连会报 `FileNotFoundError: 未找到 tls_psk_proxy.js`。解决：`cp /var/minis/skills/coredevice-toolkit/scripts/tls_psk_proxy.js /usr/lib/python3.12/site-packages/`。审查产物在 `/var/minis/workspace/元书审查/sandbox/`（lua v11、schema、custom、词表）。

## 十一、元书皮肤双排工具栏与候选栏经验（2026-10-14 用户真机确认）

**背景**：为「多功能大包」皮肤加两排工具栏、压缩候选卡片高度，反复调整真机无变化，最终通过**换新皮肤名导入**解决。经验沉淀如下。

### 双排工具栏正确做法
1. **不要用额外 gap 行控制两排间距**：HStack/VStack 不支持直接 `insets`；在 `toolbarLayout` 中间插入 gap 行（如 `toolbarRowGapStyle: {size: {height: 2.5}}`）会被当作普通行参与高度分配，导致两排之间出现不可控的大间距。
2. **两排直接相邻**：`toolbarLayout` 只放两个 HStack 即可，两排之间无间隔行。
3. **用按钮背景的上下 insets 控制视觉间距**：工具栏按钮背景（`toolbarButtonBackgroundStyleKS` 等）的 `insets: {top: 1, bottom: 1}` 让图标贴近卡片边缘，两排视觉贴合；卡片背景高度不变。
4. **工具栏卡片高度 = toolbarHeight / 行数**：每排高度由 `toolbarHeight` 均分，改 `toolbarHeight` 即可整体缩放卡片。

### 候选栏高度与工具栏联动
- 元书「横向候选文字栏尺寸与工具栏尺寸相同」：`toolbarHeight` 过高会导致候选栏被拉高。
- **独立固定候选栏高度**：给 `horizontalCandidates` 设置 `size: {width: 7/8, height: 30}`，候选栏高度不再跟随工具栏。
- **候选区做成固定卡片**：`horizontalCandidatesStyle.backgroundStyle` 指向自定义几何卡片。**背景建议直接复用工具栏卡片同款渐变**（`candidateCardBackgroundStyle = toolbarButtonBackgroundStyleKS` 去掉 `insets`）：日间 `#FDFDFF→#F6F7FB`、夜间 `#3F3F40→#383839`，`cornerRadius: 10`、阴影同款，使候选区与其他卡片视觉统一（用户确认"好看多了"）。
- **候选区贴近打字区**：`horizontalCandidatesStyle.insets: {top: 0, bottom: 0}`，`keyboardStyle.insets.top` 压到 2。

### 元书 `#次选上屏` / `#三选上屏` 的正确配置（2026-10-15 用户真机确认「搞定」）
- **官方语义**（仓输入法「自定义键盘」文档）：`#次选上屏` = 候选文字列表中次选文字上屏；`#三选上屏` = 第三位候选文字上屏。
- **皮肤侧**：空格键 `swipeUpAction: {shortcut: '#次选上屏'}`、`swipeDownAction: {shortcut: '#三选上屏'}`（元书内置 Noctua / Write_2026 的空格键就是 `swipeUpAction: {shortcut: '#次选上屏'}`）。
- **方案侧必须用 `editor.bindings` 配置空格键**（照抄元书内置方案 rime-ice），否则 `#次选上屏` 选中候选后空格键无法上屏：
  ```yaml
  key_binder:
    import_preset: default   # 不要自定义 space 的 key_binder 绑定（会干扰）
  editor:
    bindings:
      space: confirm          # 空格键：上屏候选项
      Return: commit_raw_input
      BackSpace: revert
      Escape: cancel
  ```
- **踩坑记录**：用 key_binder `{when: has_menu, accept: space, send: Select}` + `{when: composing, accept: space, send: Commit}` 时，`#次选上屏` 选中候选后轻点空格不上屏；改用 rime-ice 的 `editor` 配置后用户真机确认「搞定」。
- 参考：元书内置方案包（rime-ice_1.zip）`rime_ice.schema.yaml` 的 `editor` 配置；元书内置皮肤 `Noctua/Write_2026` 的 `spaceButton`。

### 移植皮肤背景消除工具栏色差（2026-10-15 用户真机确认「完美」）
**场景**：把另一款皮肤（如内置皮肤 Write_2026/森林集）的背景移植到大包皮肤，要求「不换按键、只要背景」，且键盘/候选区/工具栏三者背景无色差。

**核心：让键盘、候选区、工具栏共用同一张背景图，而不是各用各的。**
1. **背景用元书内置共享资源直接引用，无需复制图片**：内置皮肤（如 Write_2026）引用的 `file: "bj"` 等资源不在皮肤包里，是元书 App 内置资源，新皮肤直接写 `file: "bj"` 即可生效，不要试图从皮肤包找/复制该 png。
2. **统一背景引用**（照抄源皮肤写法）：
   - `keyboardBackgroundStyle`：`fileImage` + `file:"bj", image:"IMG2"`（键盘背景）
   - `toolbarBackgroundStyle`：同上 `bj` IMG2（工具栏背景）
   - `preeditBackgroundStyle`（候选区背景）：`fileImage` + `file:"bj", image:"IMG1"`
   - 三者同源同图切片 → 工具栏与键盘/候选区之间无缝无色差。
3. **候选区内嵌到键盘背景**（消除候选区独立色块）：移除 `horizontalCandidatesStyle.backgroundStyle`，候选区直接嵌在键盘背景上，不再独立一块卡片。
4. **候选栏固定高度**：给 `horizontalCandidates` 设置 `size: {width: 7/8, height: 30}`（或按需），候选栏高度不再被 `toolbarHeight` 拉高，避免上方大片空白。
5. **只改目标按键**：若只需去掉某个按钮的卡片背景（如候选区末尾下拉按钮 expandButton），仅删该按钮的 `backgroundStyle`，保留 `action`/`foregroundStyle`，且**只改目标键盘文件**（如仅 pinyin_9 的 light/dark×横竖屏 4 个文件），其它键盘文件不要动。
6. **换新皮肤名导入**（见下「同名皮肤缓存坑」），否则旧缓存导致看起来没变化。

### 同名皮肤缓存坑（最重要）
- **元书按皮肤名缓存旧版**：同一皮肤名反复导入新 `.cskin`，元书可能继续使用旧缓存，改参数后真机显示毫无变化。
- **解决：换新皮肤名导入**（ZIP 根目录 + `config.yaml` 的 `name` 同步改新名字，如「多功能大包-紧凑版」），作为新皮肤加载即可看到修改。
- 修改挂载目录 `/var/minis/mounts/Skins/<皮肤名>/` 后，元书不会自动热更新，仍需重新导入 `.cskin` 或重新选择皮肤。

### 产物
- `/var/minis/workspace/多功能大包.cskin`（SHA-256 `839273415bd39fd8de2d06b319aa0d5d504b4e43ad6ca76fee3ac75beaa40cc0`）
- `/var/minis/workspace/多功能大包-紧凑版.cskin`（SHA-256 `b47a5a71888b7bfa5873c2864b899ebbf817baea881edeaca48bfaa4d3ef9869`，用户确认效果正确）
- `/var/minis/workspace/多功能大包-计算版-v72.cskin`（2026-10-15 移植 2026 背景完成版，SHA-256 `6f1bd77fa93251c9d63a35535a1b64de4dfc4f2f601011a688e8b36dbba98444`，用户确认「漂亮/完美」）

## 十一、元书皮肤工具栏/候选字/符号键盘定制经验（2026-10-15 v72 实战沉淀）

### 工具栏单排化与高度/间距调整
- **双排改单排**：`toolbarLayout` 只保留一个 HStack；`toolbarHeight` 从双排高度（如 80）改为单排高度（35 左右合适，28 会压扁按钮）。
- **工具栏左右对齐打字区键盘**：`toolbarStyle.insets.left/right` 与 `keyboardStyle.insets.left/right` 保持一致（如都是 4）。
- **按键间距**：按钮背景样式（`toolbarButtonBackgroundStyleKS` / `KS__nkt_48x40`）的 `insets.left/right` 控制按钮卡片间距（7→2 卡片变宽、间距变小）。
- **滑动工具条卡片间距**：同样改按钮背景样式 `KS` 的 insets（不是 `toolbarSlideButtons.insets`！后者只控制集合整体边距）。竖屏滑动按钮用 `toolbarButtonBackgroundStyleKS`，横屏第一排按钮也用 KS，需分别改。

### 键盘整体下移/压缩
- **键盘 4 行整体下移半个键位**：把 `keyboardHeight` 改为原来的 `3.5/4`（竖屏 216→189，横屏 160→140），行样式保持 `1/4` 自动均分，键盘整体变矮半键、随之整体下移，工具栏保持贴键盘顶部。改行样式反而会破坏均分。

### 候选字大小
- `candidateStyle.textFontSize` 控制候选字大小；`split.textFontSize` 是候选字备注字号，竖屏需同步改。
- 候选字调大后必须同步调高 `horizontalCandidates.size.height`（如 40 号字配 52 高度），否则放不下。

### 滑动工具栏（horizontalSymbols）新增自定义按键
- 数据源 `horizontalSymbolsToolbarButtonsDataSource` 数组元素格式：`{action, label, styleName}`。
- 新增按键需配套两个样式：`<按钮名>SlideStyle`（`backgroundStyle: toolbarButtonBackgroundStyleKS` + `foregroundStyle: <按钮名>SlideForegroundStyle`）和 `<按钮名>SlideForegroundStyle`（前景样式）。
- 插入位置直接调整数组顺序即可（如粘贴后、X 前）。
- 图标可用 `systemImage`（SF Symbols，如 `textformat.123`、`globe`）或 `text`（如 "123" 细体 `fontWeight: light`、fontSize 16），或自定义图片资源（`fileImage` + resources png）。

### 符号键盘整体替换（把另一款皮肤的符号键盘整个搬过来）
- 直接复制源皮肤的符号键盘 yaml（如 `symbolic_portrait.yaml`）覆盖目标皮肤同名文件（light/dark）。
- **必须同时复制依赖资源**：源皮肤 yaml 里 `"file": "xxx"` 引用的 png+yaml 全部复制到目标皮肤 resources（light/dark），否则缺图。
- 内置资源（`bj`、`ax_*.png` 动画帧）无需复制，元书 App 内置。
- `config.yaml` 的 `symbolic` 映射同步改成源皮肤方式（如 iPhone/iPad 竖屏 `symbolic_portrait`、横屏 `numeric_9_landscape`），并删除不再引用的旧文件（如 `symbolic_ios_*.yaml`）。
- 替换后检查：新 yaml 引用的所有 file 在目标皮肤 resources 都存在。

### 符号键盘底部按钮换简约图标
- 底部返回/上翻/下翻/锁定按钮前景从 `fileImage` 换成 `systemImage`：`return`、`chevron.up`、`chevron.down`、`lock`/`lock.open`，字号 17，颜色浅色 `#1C1E23`/深色 `#EBEBF5`，高亮 `#3B6FD8`。
- 九宫格「符号」切换键（回车键上方）可用 `systemImage: "at"`（@ 图标）替代文字「符号」，清晰且好看。

## 参考资料（来源）

- **rime-wanxiang**：https://github.com/amzxyz/rime-wanxiang ，调研于 2026-10-12，commit `abb8cde7682028dca76d3d449562b6854b33efaf`（2026-10-11 "dict: 词库调整"），文档 `docs/doc/hamster3.md`、`docs/doc/intro.md`
- **ResourceforHamster**：https://github.com/BlackCCCat/ResourceforHamster ，调研于 2026-10-12，commit `6a3e1aea4f392a0616608cb095196062da70b1bf`（2026-10-08 "反查custom patch更新"），含 `Skin_Keyboard/万象-元书/WanxiangSkin` 与 `WanxiangSkin-modifier`
- **BG5CGQ-Stroke-Rime**：https://github.com/zny05/BG5CGQ-Stroke-Rime ，调研于 2026-10-12，commit `181f10fb85c621cdf6ea69012b3ff3bf22e55f28`（2026-08-27 "v1.0 仿百度九宫格笔画"）。子模块：deps/chinese-stroke `cd2b264`、deps/rime-stroke `1e8fff9`、deps/Chinese-characters-code-table `8db2c1c`。数据源：yukunqian/chinese-stroke（10,087 字）、yefeijiang/Chinese-characters-code-table（11,091 字）、rime/rime-stroke（6,577 字）、rime-essay 语料、通用规范汉字表加权。天枢笔画输入法项目：https://github.com/mickeu/tianshu-stroke
- 元书输入法 App Store：https://apps.apple.com/us/app/元书输入法/id6744464701
- 仓输入法 App Store：https://apps.apple.com/us/app/仓输入法/id6446617683
- 天枢（TianShu）：https://www.tianshuapp.tech （本地多角色 AI Agent 工作台，后续改造对象）
- 万象更新工具：https://github.com/rimeinn/rime-wanxiang-update-tools
- 2026-10-12 实战：天枢输入法重签名后「方案目录切换为空」的根因与修复（文件共享未开启），产物 `天枢输入法_v6_文件共享.ipa`（用户确认方案下载成功）。详见本技能库「八、重签名后方案目录不生效排查」及 `ios-iap-removal` 技能库。