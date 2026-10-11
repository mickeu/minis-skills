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

## 参考资料（来源）

- **rime-wanxiang**：https://github.com/amzxyz/rime-wanxiang ，调研于 2026-10-12，commit `abb8cde7682028dca76d3d449562b6854b33efaf`（2026-10-11 "dict: 词库调整"），文档 `docs/doc/hamster3.md`、`docs/doc/intro.md`
- **ResourceforHamster**：https://github.com/BlackCCCat/ResourceforHamster ，调研于 2026-10-12，commit `6a3e1aea4f392a0616608cb095196062da70b1bf`（2026-10-08 "反查custom patch更新"），含 `Skin_Keyboard/万象-元书/WanxiangSkin` 与 `WanxiangSkin-modifier`
- **BG5CGQ-Stroke-Rime**：https://github.com/zny05/BG5CGQ-Stroke-Rime ，调研于 2026-10-12，commit `181f10fb85c621cdf6ea69012b3ff3bf22e55f28`（2026-08-27 "v1.0 仿百度九宫格笔画"）。子模块：deps/chinese-stroke `cd2b264`、deps/rime-stroke `1e8fff9`、deps/Chinese-characters-code-table `8db2c1c`。数据源：yukunqian/chinese-stroke（10,087 字）、yefeijiang/Chinese-characters-code-table（11,091 字）、rime/rime-stroke（6,577 字）、rime-essay 语料、通用规范汉字表加权。天枢笔画输入法项目：https://github.com/mickeu/tianshu-stroke
- 元书输入法 App Store：https://apps.apple.com/us/app/元书输入法/id6744464701
- 仓输入法 App Store：https://apps.apple.com/us/app/仓输入法/id6446617683
- 天枢（TianShu）：https://www.tianshuapp.tech （本地多角色 AI Agent 工作台，后续改造对象）
- 万象更新工具：https://github.com/rimeinn/rime-wanxiang-update-tools