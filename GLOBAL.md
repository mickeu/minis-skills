# GLOBAL.md — 全局记忆

## 工具调用格式教训（2026-09-03 反复踩坑，务必牢记）
- **绝对不要嵌套 `arguments` 键**。每个工具的参数必须直接用顶层字段：`shell_execute` → `command`；`file_write` → `path`+`content`；`file_edit` → `path`+`old_string`+`new_string`；`file_read` → `path`。
- 一旦把参数包进 `arguments`、`argsToUse`、`parameters` 等任何 wrapper 键，系统会报 "missing required parameter(s)" 拒绝。
- 同一错误连续出现 3 次就立刻停下来，把字段拍平为顶层重试，不要反复用同一种错误嵌套格式。
- 写长文件时内容会被截断：分成多个小段用 append 追加，不要一次写超长。

## 语言约定
- **所有分析、说明、回复一律使用简体中文**，除非用户明确要求英文。技术名词（域名、参数名等）保持原样。

## 模型路由规则（2026-08-15 v3）

处理任务时按类型自动调用相应模型，**所有成对模型（日日新1↔日日新2）都轮询使用**：

- **日常对话/快速问答/默认主力** → `deepseek-v4-flash`（轮询，带思考）
- **生图/画图** → `sensenova-u1-fast`（轮询，自动附 `watermark: false`；默认 1344x3136 竖屏，可改）
- **看图/图片理解/OCR/截图分析** → **视觉兜底链**：跑 `/var/minis/skills/vision-fallback/scripts/vision-read.sh <图片> [问题]`，自动降级 gemini-3-flash-preview → apple-vision OCR。**看图一律走该脚本，无需用户指定引擎**
- **长文本/项目级代码/复杂推理/长文档分析** → `glm-5.2`（轮询，1M 上下文）
- **兜底** → `gemini-3.1-flash-lite`（只在日日新两 key 都不可用时用；PDF/音视频多模态也走它）

轮询约定：同一任务连续调用时，上轮用日日新1、本轮用日日新2 交替；单 key 调不通立即换另一个。

注意事项：
- 所有日日新模型走 OpenAI 兼容接口 `https://token.sensenova.cn/v1`
- u1-fast 只能生图（chat 接口 404）；6.8 在 token.sensenova.cn 上视觉不可用（仅文本）；glm/deepseek 纯文本
- glm-5.2 用 key1 可调用，key2 报 429（需要时轮换 key）
- deepseek 复杂推理时思考可能过长吞输出，复杂任务不选它

## 用户隐私红线
- **禁止使用用户的 Google 邮箱/账号**注册任何服务
- **禁止使用用户的 GitHub 账号（mickeu）**注册任何服务
- 所有注册行为必须用**临时邮箱、全新账号或公开可用的免费方式**

## 工作习惯
- **每次提交编译前必须多次审查完整代码**：用 file_read/rg 逐个读取新建/修改的文件，至少审查 2 遍，检查语法错误、重复声明、逻辑 bug、路径匹配顺序、参数解码、OAuth 格式等。确认无误后再触发编译。禁止未审查或只审查一遍就提交。发现问题立即修复，不要等编译报错。
- **跑通的操作主动沉淀到技能库**：跑通的工作流/命令链/配置方法，当次更新到对应 SKILL.md 或 references，不等用户提醒。
- **技能库自动记录来源**（2026-10-03 用户指出）：新建/更新技能时，SKILL.md 必须自动包含完整「参考资料（来源）」章节——原文 URL、官方仓库/文档链接、创建/调研日期、版本号与校验信息等，一步到位，不等用户提醒补充。创建完自查一遍来源是否完整再推送。
- **能自己查的不问用户**：文件路径、命令行为、配置语法等先查 mounts/技能库/官方手册或直接测试。
- **记忆和技能库区分**：日常操作细节写每日记忆；通用可复用的方法写技能库；跨会话偏好写 GLOBAL.md。
- **所有配置文件注释要简短**（Surge/Clash/Egern 配置、规则集 .list、模块 .sgmodule、脚本 .js 全适用）：每条规则 1-2 行只说明"为什么需要它"；不写流水账——不标日期、改动来源、备份文件名、推理依据、已删除项说明；行前注释与行内注释不要说同一件事，重复就删一个；长推理写记忆或回复，不进配置。commit message 同样简短：1 句结论 + 关键改动。范例：
```
# > 阿里统计/身份域强制直连（只在 Direct_Supplement 有，ChinaMax 无）
# mmstat.com 同时在 Advertising_All.list，规则集失效会被 REJECT
DOMAIN-SUFFIX,mmstat.com,DIRECT
```
- **新增 provider / API Key 一律先用环境变量**（用户要求，2026-10-03）：先让用户通过 `[设置环境变量](minis://settings/environments?create_key=KEY&create_value=&create_note=...)` 把密钥写入 Minis 环境变量，provider 配置里用 `$$ENV_VAR` 引用（如 `$$EXPLABS_API_KEY`），不要直接把明文 key 写进 provider 配置。特殊情况需直写时也要说明并尽快迁移。
- **GitHub 推送直接走 credential.helper**：`$GITHUB_TOKEN` 已在环境变量，credential.helper 已配好，直接 `git push`。
- **每次任务执行完，主动清理 shared 目录下所有不需要的临时文件**（天气播报的 merged-*.mp3 / voice-*.mp3 / broadcast-text.txt / *.log 等产物）。⚠️ 只删确无用的临时产物，**不盲目删**：保留 birds.mp3、配置/脚本/git 仓库等有用途的文件。注意 `shared` 有**两份镜像**：本地 `/var/minis/shared/` + iCloud 挂载 `/var/minis/mounts/E42E8F36-8C3A-4339-AD9C-51B7F3AB5890/shared/`，两边都要清，只清一个会残留。

## Surge 配置维护规则
- **新增域名规则写进仓库已有规则集文件**（Gemini.list、Direct_Supplement.list 等），推送到 mickeu/surge，**不写死进 Rule.dconf**。
- **blackmatrix7 漏域名就拉下来改**，加到自己的同名规则集文件，Rule.dconf 引用切到 mickeu/surge 版本。
- 改完用 `sh /var/minis/shared/sync-config.sh` 或手动 git 推送。
- **Surge 规则集改动必须同步 MRS 到 Clash 仓库**（2026-10-04 用户要求）：只要 Surge 侧自建规则集（Direct_Supplement/Proxy_Supplement/Advertising_Supplement/Gemini/Apple_All/Apple_Services/AppleIntelligence/Telegram_All/Video_RESOURCE 等）有增删域名，就必须用 `mihomo1190 convert-ruleset` 重新转换成 MRS 推送到 mickeu/Clash 仓库，**ChinaMax_All.list 除外**（ChinaMax 用 blackmatrix7 的 ChinaMax_Classical.yaml 单独转换，不转 Surge 版 list）。MRS 更新后覆写脚本通过同名 URL 自动跟随，Hako 需用户手动重新应用脚本。
- **国内 API 服务必须直连**（云知声/阿里/腾讯等）：走境外代理会被服务端掐断 TLS（`unexpected eof`），导致模型/API 调不通。添加新 provider/服务后先 `surge-cli rule match <域名>` 确认路由，避免被 FINAL 兜底送代理。
- **查真实 IP 用 DoH**：hijack-dns 劫持所有 :53 查询（nslookup 也拿不到真实 IP），用 `https://dns.alidns.com/resolve?name=<域名>&type=A`（走 HTTPS 不被劫持）。
- **WebRTC 泄露修复必须同时处理规则 + DNS 层**（2026-10-02 实测）：国内 STUN（`stun.chat.bilibili.com`/`stun.hitv.com`/`stun.miwifi.com`）会泄露真实 IP，根因是 `always-real-ip` 里的通配 `stun.*` 让 STUN 域名返回真实 IP 而非 fake-ip，导致 UDP 目标走 GEOIP,CN 直连。修复 = ① 三个 STUN 域名加进 `Proxy_Supplement.list` 走 PROXY；② **`always-real-ip` 移除 `stun.*`**（关键，只改规则无效）。游戏/Twilio STUN 有单独条目（`*.stun.playstation.net`、`*.stun.twilio.com`、`stun.syncthing.net`）不受影响。代理节点 UDP relay 部分不可用 = STUN 失败无候选 = 不泄露（可接受）。

## GitHub 仓库与推送认证
- **mickeu/surge**（公开）：Surge 规则集（.list）+ 脚本（.js）+ 模块（.sgmodule）+ Clash 规则集（.yaml），**不含任何配置文件**
- **mickeu/Clash**（公开）：Clash 规则集（ruleset/*.yaml）+ 脚本，**不含任何配置文件**
- **mickeu/config-backup**（**私有**）：Surge/Clash/Egern 完整配置备份（含节点密码、MITM 证书、API 密钥）。本地：`/var/minis/shared/config-backup/`，Surge 配置在 `Surge/config/`
- **mickeu/minis-memory**（私有）：记忆备份
- **mickeu/minis-skills**（公开）：个人 Minis 技能库。本地工作副本 `/var/minis/shared/minis-skills/`，与本地技能库 `/var/minis/skills/` 保持同步。**以后所有 Minis 技能（上传的 SKILL.md/技能包、新建技能、更新已有技能）安装/创建/修改后，必须同步推送到本仓库**。大体积参考数据（>2MB 二进制/数据文件）不上传，见仓库 .gitignore；推送直接用 `git push`（本地已配置低内存 pack 参数 pack.threads=1 等，勿重置）
- Token 在环境变量 `GITHUB_TOKEN`，credential.helper 已配好，直接 `git push`。
- ⚠️ **配置文件（.conf/.dconf/完整 .yaml 配置/配置片段）只推 config-backup 私库，公共仓库（surge/Clash）一律不推、已有的已删除（2026-10-02）**。规则集文件（.list、payload 形式的 .yaml）、脚本、模块可留在公共仓库。
- ⚠️ github-sync-helper 的 `gh_sync.sh` 不存在，别依赖它。

## Clash 配置项目
用户折腾 **Clash Apple 原生客户端**（Hako 内核 = mihomo），YAML 格式。
- **mickeu/Clash**：本地克隆 `/var/minis/shared/clash-sync/`，规则集在 `ruleset/`（5个自建）
- **良心机场**（liangxin.xyz）不能用 proxy-providers 订阅（flag=clash 返回占位提示），只能用原始订阅链接转换。脚本：`/var/minis/workspace/clash-tools/convert_lx.py`，订阅链接在同目录 README。用户说"更新良心机场节点"就自动跑。
- 极速机场（jsjc.cfd）支持 `flag=shadowrocket`，可用 proxy-providers。
- blackmatrix7 文件名坑：Clash 目录下正确是 `Advertising.yaml`/`Global.yaml`（不是 `_All`）。
- 规则排序：广告→局域网→AI→Apple→微软→Telegram→游戏→流媒体→国内直连→境外兜底→国内四层防线→MATCH
- 地区组：🇯🇵日(11)/🇭🇰港(10)/🇸🇬新(8)/🇺🇸美(7)/🌍其他(3)
- DNS：fake-ip-filter 对齐 Surge always-real-ip；Apple 测速域名用 nameserver-policy 强制国内 DNS
- 常见排查：域名走不通 = 查 DNS（fake-ip-filter + nameserver-policy + rules）+ 出站方向
- **MRS 转换与审计经验**（2026-10-04 全量对比沉淀）：
  - `mihomo1190 convert-ruleset` 支持**反向转换 MRS** 用于审计：`convert-ruleset domain|ipcidr mrs <in.mrs> <out.txt>`
  - MRS domain 类型支持 domain/domain-suffix/**domain-keyword** 三种，Surge 的 `DOMAIN-KEYWORD` 会正确存储，**转换时不能过滤 KEYWORD**（过滤会丢功能）
  - `convert-ruleset ipcidr` 会**自动合并相邻 CIDR**（如两个 /24 → /23），对比 IP 规则需先归一化 CIDR 才能准确判断差异
  - Surge 规则集对比法：提取 DOMAIN/DOMAIN-SUFFIX/DOMAIN-KEYWORD + IP-CIDR/IP-CIDR6，反向转换 MRS 后对比；KEYWORD 算 Surge 侧规则，IP 需 CIDR 归一化

## xKiro 中转站配置
- **Base URL**：`https://api.xkiro.com/v1`，免费 5M token/天，OpenAI/Anthropic 格式均可用
- 三个账号：
  | 账号 | 环境变量 | Provider ID |
  |---|---|---|
  | xKiro (Google) | `XKIRO_API_KEY` | `01713EC1-D2EF-4495-9A5F-FB59C8572223` |
  | xKiro (mickeu) | `XKIRO_API_KEY2` | `EE9C4835-5ECC-42F7-A0AD-1585C95D1FD5` |
  | xKiro (QQ号) | `XKIRO_API_KEY3` | `E2789FA2-A503-4EE9-A551-1A63B1D58BC6` |
- 20 个免费模型（DeepSeek/Mistral/MiniMax/Stealth），全部实测支持视觉输入
- 注册方式：GitHub OAuth 绕过 hCaptcha，瓶颈在 GitHub 账号数。Gmail `+` 别名可裂变新 GitHub 账号但 xKiro OAuth 暂不认。
- 已挂入主力组 + 看图组兜底（mistral-large-2512 视觉兜底）
- 无免费生图模型，生图走日日新 u1-fast

## 网址不通的标准处理流程（端到端自动化，必须走全套）
用户反馈「某网址打不开/无法建立安全连接」时，**禁止**只口头劝、禁止用临时规则糊弄。按以下顺序执行：
1. **连接 Surge 检测**：`surge-cli rule match <域名>` 看命中策略（REJECT/DIRECT/PROXY？）；`surge-cli dns lookup <域名>` 看解析；`surge-cli http probe <URL>` 端到端验证。先用 surge-cli（连你手机上的 Surge），不要求用户贴配置。
2. **判定根因**：REJECT=被广告/规则集拦；DIRECT 但连不上=直连被墙；PROXY 但连不上=节点问题或 DNS 投毒（加 DoH）。
3. **规则集问题就修规则集**（不是临时规则、不是改 Rule.dconf）：把域名加进对应自建规则集文件（`Ad_Whitelist.list` 放被广告误杀的境外正常服务走 PROXY；`Direct_Supplement.list` 放需直连的；`Proxy_Supplement.list` 放需强制代理的），推送 mickeu/surge。规则集文件用 Surge 原生 `//` 行内注释（Surge 正常解析），**但 mihomo 转换需先 `sed 's| //.*||'` 剥离行内注释**再转 MRS。
4. **推送到仓库**：`git commit + push` mickeu/surge（规则集文件）。
5. **同步 MRS 到 Clash 仓库**：自建规则集（除 ChinaMax_All.list 例外）改动后，必须用 `/tmp/mihomo1190 convert-ruleset domain text <过滤后源> <目标.mrs>` 重新转 MRS（命令用法 `convert-ruleset <behavior> <format> <源> <目标>`，注意先剥离 `//` 注释），推送到 mickeu/Clash 的 `ruleset/mrs/`。覆写脚本通过同名 URL 自动跟随，Hako 需用户手动重新应用。
6. **改 Clash 覆写脚本**（仅当规则集结构变化/新增规则集引用时才需要，单纯增删域名一般不用）。
7. **生效**：`surge-cli external-resource update <key>` 强制刷新（CDN 删内容有延迟，先 curl raw 确认传播再 update；key 从 `external-resource list` 取）+ `surge-cli reload`；再用 `rule match` 验证实际命中、用 `http probe` 验证连通。
8. **清理**：清掉本会话可能误加的临时规则（`rule temp remove` / `rule temp flush` 仅清本次加的，保留用户已有项）。

⚠️ 临时规则 `rule temp add` 只作临时验证，**不能当最终修复**——它优先级高但重启 Surge/清缓存即失，且策略名必须严格匹配你的策略组（你的组叫 `PROXY` 不是 `Proxy`，写错即无效）。最终修复一律走规则集。

## Surge 面板脚本工作规则
- **改脚本必换全新文件名**（v1→v2→v3），script-name 和 [Panel] 同步更新。Surge 缓存旧脚本很顽固，改名是唯一可靠强制刷新。
- **generic 面板脚本 `$httpClient` 的 `policy` 参数会超时**（实测确认），正确做法：模块 [Rule] 段加规则让目标域名走 `{{{GROUP}}}` 指定策略组，脚本不指定 policy 只发请求：
```
#!arguments=GROUP:PROXY
[Rule]
DOMAIN-SUFFIX,ip-api.com,{{{GROUP}}}
[Script]
X = type=generic,timeout=15,script-path=...js,argument=group={{{GROUP}}}
[Panel]
X = script-name=X,title="...",content="点击刷新",style=info,update-interval=0
```
- 面板脚本建议加 `setTimeout(finish,9000)` 超时兜底。
- `#!author=` / `#!category=` 可设作者和分类。

## 自建模块命名偏好
所有由我为用户制作的 Surge/Egern 模块，`#!author=mickeu` 且 `#!category=mickeu`。

## 改 Surge 配置的正确流程
**Surge 实际加载的配置在 `/var/minis/mounts/nssurge/`，不是仓库副本。**
1. 先改本地实际加载文件：`/var/minis/mounts/nssurge/Rule.dconf` 等
2. 运行 `sh /var/minis/shared/sync-config.sh`（SYNC_MAP 只含 Rule.dconf）
3. 同步私库 config-backup（含 Script.dconf 等敏感）：`cd /var/minis/shared/config-backup && git add -A && commit && push`
4. `surge-cli reload` 生效
⚠️ 改了只需同步 nssurge 本地 + config-backup 两处（surge 仓库不再保存配置文件）。删除本地脚本时注意 Rule.dconf + Script.dconf 都要删（避免模块替代后 cron 重复执行）。

## Surge 远程规则集生效验证（用户认可，2026-09-30）
CLI 无法直接读取 Surge 已加载规则集内容，验证"实际拉到新版"用**临时特征规则法**：
1. 在规则集文件末尾加一条独特域名（如 `DOMAIN,verify-cache-test-mickeu.example`）
2. 推送 GitHub，轮询 curl `raw.githubusercontent.com` 直到该规则出现（CDN 缓存）
3. `surge-cli external-resource update <key>` 强制刷新对应规则集
4. `surge-cli rule match <特征域名>` 命中对应 RULE-SET 即证明 Surge 实际加载了新版
5. 确认成功后删除临时规则并推送，等 CDN 恢复后再次 update + rule match 确认不再命中（闭环）
⚠️ GitHub CDN 对内容删除的传播有延迟（实测添加秒级可见、删除后数分钟不恢复），删除验证规则后要等 CDN 恢复再刷新确认。

## 已完成模块索引
- **IP 纯净度检测**：`mickeu/surge/IP-Quality.sgmodule` + `Scripts/IP-Quality.js`（规则法，Scamalytics API 评分）
- **网上国网签到**：`mickeu/surge/95598.sgmodule` + `Scripts/95598/95598.js`（cron 签到 + 面板手动签到）
- **codex-chatgpt-web**：技能库 `/var/minis/skills/codex-chatgpt-web/`，ChatGPT Web 桥接 Codex 模型（用户是否在用待确认）

## 签到类模块通用模式
cron 自动签到 + generic 面板手动签到：[Script] 同时放 cron + generic 面板脚本，[Panel] 配面板按钮。面板脚本有 `$request` 分流 → 独立脚本文件；无分流 → 复用原脚本。结果通过 `$notification.post` + `$done` 显示。

## 面板与通知内容拆分
- 面板：`lines` 数组（精简版），`$done` 用
- 通知：`notifyLines` 数组（完整版），`$notification.post` 用
- 适用：多条目展示、面板卡片挤的场景

## 版本更新日志自动入库
用户把 Minis 版本更新日志贴过来时，**自动追加到技能库 `/var/minis/skills/minis-update-log/SKILL.md`**，排在文件最顶部（新的在前），格式参照现有条目：`## 版本 x.y Build N` + 构建号/来源 + 本次更新（新功能 / 问题修复 / 性能优化分组）。写完后简短告知已入库。不用等用户提醒。
