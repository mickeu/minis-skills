# Surge iOS 实测坑位与菜谱（2026-08-17 实测沉淀）

来源：Surge 5.102.0 (3819) TestFlight 实机验证。与官方文档不一致/文档未覆盖处以此文件为准。

## 1. 外部脚本资源更新机制（最容易踩）

**症状**：改了远程脚本内容、push 后 `surge-cli reload`，Surge 仍跑旧版。

**实测真相**：
- `surge-cli reload` **不强制重新下载远程脚本**（external-resource 的 updatedAt 不会刷新，仍加载旧缓存）
- `external-resource update <key>` 对**已 ready 的条目是"假更新"**：只刷 updatedAt 时间戳，不重新下载内容（304/缓存）
- **只有 ready:False 的新条目才会真正下载**（新 URL / reload 后未就绪的条目）

**可靠工作流**（改脚本内容后）：
1. **改 URL**：script-path 加版本参数 `?v=N`（或换文件名）——强制成为新条目
2. `surge-cli reload`（必要时两次）→ `external-resource list` 确认条目出现（ready:False）
3. `external-resource update <完整32位key>`（**key 不能截断**，否则报 Define not found）→ ready:True
4. `surge-cli script run <cron名>` 看输出确认加载的是新内容

**判断是否生效**：`external-resource list` 看 updatedAt 是否=本次操作时间；script run 输出的行为特征是否符合新版。

## 2. cron/event 脚本触发源判定

**症状**：cron 脚本一执行就"0 输出"，logbook 显示"执行完毕 13ms"假象。

**实测真相**：
- cron 触发环境：`$event`、`$cronexp` **变量未声明**——直接引用 `$event && $event.name` 抛 ReferenceError，脚本静默崩溃、零输出
- `typeof $event !== 'undefined' && $event && $event.name === 'network-changed'` 才安全（typeof 防护）
- `surge-cli script run <cron名>` 调试通道可能注入 mock $event（误走 event 分支）——调试假象，勿据此判断
- `surge-cli script evaluate <path> cron <timeout>` 的 mock 环境：$event/$cronexp 均 undefined

## 3. MITM CA 证书管理（B 方案：Keystore + include 抽离）

**症状**：问"ca-p12 能不能像 Egern 写文件名"——不能。

**实测真相**：
- ca-p12 **只认 base64 内嵌**；写文件名会被解析成残留值（实测变 "Surge"），/v1/mitm/ca 报 404
- 删除 ca-p12/ca-passphrase 后，即使 Keychain 有 Surge Generated CA 且系统已信任，**Surge 也不会自动采用**
- **/v1/mitm/ca 是验证端点**：HTTP 200 + DER 证书 = CA 正常；404 "mitm ca has not been configured" = 缺 CA
  ```sh
  curl -s -H "X-Key: $KEY" http://127.0.0.1:6171/v1/mitm/ca -o ca.der
  openssl x509 -inform DER -in ca.der -noout -fingerprint -sha1 -subject
  ```

**B 方案（配置干净）**：
- 主配置：
  ```
  [MITM]
  #!include mitm-ca.conf

  [Keystore]
  #!include mitm-ca.conf
  ```
- mitm-ca.conf（配置目录，与 .conf 同级）：
  ```
  [MITM]
  h2 = true
  ca-keystore-name = surge-ca

  [Keystore]
  surge-ca = type=p12, base64=<P12 base64>, password=<pass>
  ```
- Keystore item 语法：`name = type=p12, base64=<b64>, password=<pass>`（type 可省略，有 password 默认 p12）
- **#!include 语义**：只合并"当前段对应的文件段"，文件里其他段不自动注入——MITM 和 Keystore 两段必须各自 include 同一文件
- 改证书只动 mitm-ca.conf；指纹验证不变则设备信任链不受影响
- App 页面的"Surge Generated CA"显示是从配置读的，不代表 Keychain 自动采用

## 4. 测速接口（8-16 起验证）

- `/v1/policies/test`（单节点测速）对 Trojan/Hysteria2 返回空，不可靠
- `/v1/policy_groups/test`（组测速）可靠，但**必须串行**（Surge 单测速任务并发限制，并行导致部分组返回空）
- 组测速返回 `{"available":[...]}`：无 available 字段 = 测速无结果（超时/冲突），此时**不要**把当前选中判为不可用（保守跳过）
- 无延迟数据接口：组测速/单测速均拿不到 RTT 排序，无法在脚本里做"挑最快"

## 5. 其他待用菜谱

- MTProto IPv6 自动判定：`GET /v1/profiles/current?sensitive=0` 返回 `{"profile":"全文"}`，解析 `[MTProto]` 段 `ipv6 = true`（secret 等敏感字段会被脱敏）
- $httpClient 签名：`$httpClient.get({url, policy, timeout}, cb)`——**options 对象必须放第一个参数**（放第二参数报 "n is not a function"），timeout 单位是秒
- 节点 v6 能力实测：`$httpClient.get({url:'https://[2606:4700:4700::1111]/', policy:'节点名', timeout:5}, cb)`——能握手 = 该节点支持 IPv6 出口
- `surge-cli script run` 只支持 cron 脚本（event 不行）
- 配置 reload 有时要两次才真正刷新（ca-p12 变更后观察 profiles/current 确认）

## 6. 实例：网上国网 95598.js 更新流程（2026-08-17 落地）

- 配置：Script.dconf 挂载 `script-path=https://raw.githubusercontent.com/mickeu/surge/main/Scripts/95598/95598.js`，`script-update-interval=86400`（24小时自动检查，改成 86400 是用户要求；内容变了不保证拉到，仍需手动）
- **改完代码立即生效**：
  ```sh
  surge-cli external-resource list   # 找 95598 条目的 32 位 key（当前: d2edba8ec9e269ea74ce95acd51b03d0）
  surge-cli external-resource update <key>
  surge-cli external-resource list   # 确认 updatedAt=本次时间
  ```
- 仍未生效（假更新坑）：script-path URL 加 `?v=N` 换新条目再 update
- 95598.js 头部注释含完整配置示例（中文占位符，无真实凭据）；脚本按段名命名 → Scripts/95598/95598.js（**不是**"网上国网"中文名）；无 sgmodule 模块（用户明确不需要模块，直接 Script.dconf 引用）
## 7. 实例：PingMe 签到多脚本合并单模块（2026-08-25 落地，成功）

**需求**：把"抓Cookie"（http-request）+ "签到/视频"（cron）+ "参数同步"（generic）三个脚本合并为一个模块，加策略组参数。

**成果模块**：`mickeu/surge/PingMe.sgmodule`（名"PingMe 签到整合版"，author/category=mickeu）
- 脚本复用仓库已有文件：`Scripts/PingMe/pingme_capture.js`、`PingMeSignin.js`、`pingme_sync.js`
- **一个 `[Script]` 段可混放不同类型脚本**（http-request + cron + generic），没有冲突；cron 任务在 Surge 界面显示为独立定时任务。

**多编辑参数（3个，逗号分隔）**：
```
#!arguments=capture:true,PingMePolicy:PROXY,cron:0 */3 * * *
#!arguments-desc=...（用 \n 换行，多参数说明1️⃣2️⃣3️⃣序号）
```
- 参数模板占位符可替换到 `[Rule]`、`argument`、`cronexp` 等任意文本字段
- **cron 可编辑**：`PingMe签到 = type=cron,cronexp="{{{cron}}}",...`

**策略组规则（规则法）**：
```
[Rule]
DOMAIN-SUFFIX,api.pingmeapp.net,{{{PingMePolicy}}}
```
- PingMePolicy 可填 DIRECT / PROXY / AIGC 等任意组名

**cron 表达式速查**（5段：分 时 日 月 周）：
- 每天15:29 → `29 15 * * *`
- 每天15:31 → `31 15 * * *`
- 两个时段合并 → `29,31 15 * * *`
- 每3小时 → `0 */3 * * *`
- 无"25点"（0-23）；`29 */15 * * *` 小时位 15 不整除 24，实际=每小时29分跑一次（易误用）

**注意**：`#!arguments` 多参数逗号分隔写法已验证生效（命名/分类 `#!author=mickeu` `#!category=mickeu`，见 SKILL.md 模块命名约定）。

## 8. 配置变更的正确流程（2026-08-25 教训沉淀）

**核心事实**：Surge 实际加载的配置文件在 `/var/minis/mounts/nssurge/`，不是仓库工作副本。改配置顺序：

1. **改本地 nssurge 配置**：`/var/minis/mounts/nssurge/Rule.dconf` / `Script.dconf` 等
2. **同步公开仓库**：`sh /var/minis/shared/sync-config.sh`（自动 diff + 推送 Rule.dconf 等可公开文件到 mickeu/surge）
3. **同步私库**：`cd /var/minis/shared/config-backup && git add -A && commit && push`（含 Script.dconf/Proxy.dconf/mitm-ca.dconf 等敏感信息）
4. **reload**：`surge-cli reload`

**sync-config.sh 机制**：SYNC_MAP 映射 nssurge 本地文件→仓库路径，只 diff 有变更才推送；用 `x-access-token` 方式一次性 token 推送，不写死 URL。

**⚠️ 常见错误**：只改 `/var/minis/shared/surge-sync/Config/Rule.dconf`（仓库副本）却以为配置生效了 = 本地 Surge 还没变。**改配置必须从 nssurge 本地出发。**

## 9. cron 表达式不能放进 #!arguments 参数（2026-08-25 重复踩坑）

**坑位**：`#!arguments=cron:0 */3 * * *` 里的 cron 值含**空格**，Surge 把空格当参数分隔符，导致：
- 参数被截断（只识别到 `cron:0`，剩下 `*/3 * * *` 变成多余参数）
- **严重时整个 `[Script]` 段解析失败**，脚本不注册，连 http-request 抓Cookie 也失效（贴吧模块整体失败的根因）

**对比 PingMe**：PingMe 也用了 `cron:0 */3 * * *`，但意外地能注册脚本——这个差异未完全确认，不要依赖"有时能成功"。

**正确做法**：**cron 定时不做成模块参数**。把 cronexp 直接写死在 `[Script]` 段的 `cronexp="30 0,12 * * *"`，用户要改定时在 Surge 脚本界面直接改 cronexp。

历史记录：git commit 621e900（2026-07-30）就是"修复cron表达式逗号被解析为参数分隔符"——当时已踩过，8-25 重复踩了一次。

**教训**：改前先看 git log 历史，避免重复踩坑。

## 10. 实例：百度贴吧签到多脚本合并单模块 + 手动签到面板（2026-08-25 落地）

**需求**：合并抓Cookie（http-request）+ 签到（cron），加手动签到面板，cron 定时参数可编辑。

**成果模块**：`mickeu/surge/TieBa.sgmodule`（名"百度贴吧签到整合版"，author/category=mickeu）
- 3 脚本 + 1 面板：
  - `百度贴吧[Cookie]` http-request（抓Cookie，引 TieBa.js）
  - `百度贴吧签到` cron（定时，引 TieBa.js，靠 $request 判定分流）
  - `百度贴吧签到面板` generic（**手动签到**，引 TieBaPanel.js，点面板刷新执行，结果直接显示面板）
  - `[Panel]` 面板按钮"🀄 贴吧签到"
- 参数：`cookie_enabled`（抓参开关）+ `cron`（签到定时）

**关键：cron 定时必须用独立脚本文件，避免与 http-request 同 URL**
- 抓Cookie 和 cron 用同一个 `TieBa.js`（靠 `typeof $request` 判定分流）——但 Surge "加载自" 界面会**去重**同 script-path 的脚本，导致 cron 脚本在界面不显示（虽注册成功仍会定时跑）
- 手动签到面板**必须用独立脚本文件**（TieBaPanel.js），因为：
  - 面板 generic 环境下 `$done()` 需传面板对象才能显示结果，cron 环境忽略
  - 独立文件让"加载自"界面能显示，且面板可单独绑定

**面板脚本签到逻辑**：复用 mainSign 逻辑，但用 `$done({title, content, icon, "icon-color"})` 输出到面板，同时 `$notification.post` 弹通知。核心：读 `$persistentStore` Cookie → 拉贴吧列表 → 逐个签到 → 汇总结果面板显示。

**手动测试签到**：面板点刷新即执行签到，不必等 cron。对需要临时验证的签到类脚本，面板是最好测试入口。

**经验**：模块里"加载自"界面按 script-path 去重显示——**一个脚本文件多个用途（http-request + cron）时界面只显示一条**，但功能都正常；要界面分别显示 + 面板手动执行，用独立脚本文件。

## 11. 实例：网上国网签到模块（用户名密码参数 + 面板手动签到）（2026-08-25 落地）

**需求**：把网上国网 cron 签到脚本（95598.js）做成模块，用户名密码做成可编辑参数，加面板手动签到。

**成果模块**：`mickeu/surge/95598.sgmodule`（名"网上国网签到"，author/category=mickeu）
- 6 个编辑参数：
  - `username` / `password`（必填，账号密码）
  - `debug` / `show_recent_usage` / `notify_all_accounts`（功能开关）
  - `cron`（签到定时）
- 2 脚本 + 1 面板：
  - `网上国网[定时]` cron（引 95598.js，123KB 压缩脚本）
  - `网上国网签到面板` generic（面板手动签到，引同一个 95598.js，结果通过通知显示）
  - `[Panel]` 面板按钮"⚡ 网上国网"

**关键**：`argument` 参数用 `{{{参数名}}}` 模板替换后拼接成 query-string 格式：
```
argument=username={{{username}}}&password={{{password}}}&debug={{{debug}}}&show_recent_usage={{{show_recent_usage}}}&notify_all_accounts={{{notify_all_accounts}}}
```
- 与 95598.js 内部 `$argument` 按 `&` 和 `=` 解析的格式完全兼容
- 用户填的参数值会替换到双花括号位，然后拼成完整的 query-string 传给脚本

**脚本复用**：同一个 95598.js 同时用于 cron 和 generic 面板——cron 下自动跑签到，generic 面板下点一下就执行签到（面板环境 $request 不存在，脚本走签到逻辑）。结果通过 `$notification.post` 弹通知，面板不显示详细结果。

**密码安全**：账号密码明文存在 Surge 模块配置中，和之前 Script.dconf 直写密码风险一致。模块不公开分享。

**删除本地配置**：本地 nssurge/Script.dconf 里的网上国网 cron 脚本已删除（由模块替代），同步到 config-backup 私库。

## 12. 通用模式：签到类模块加面板手动签到（2026-08-25 沉淀）

贴吧、95598 都用了同一个模式：**cron 自动签到 + generic 面板手动签到**。

**模式结构**：
```
[Script]
签到任务 = type=cron,cronexp="{{{cron}}}",script-path=...js,...
签到面板 = type=generic,timeout=120,script-path=...js,...

[Panel]
签到面板 = script-name=签到面板,title="xxx 签到",content="点击签到",style=info,update-interval=0
```

**两种面板脚本处理方式**：
- **贴吧（TieBa.js 有 $request 分流）**：面板必须用**独立脚本文件**（TieBaPanel.js），因为原脚本靠 `typeof $request` 判断抓Cookie/签到，generic 面板环境 `$request` 行为不确定，独立脚本避免误判。且独立文件让"加载自"界面能分别显示。
- **95598（无 $request 分流）**：面板**直接复用原脚本**（95598.js），因为脚本内部没有 `$request` 判定，generic 环境下直接走签到逻辑。

**面板脚本两种结果输出**：
- 结果通过 `$notification.post` 弹通知（贴吧 + 95598 都有）
- 结果通过 `$done({title, content, icon, "icon-color"})` 显示在面板（贴吧有，95598 没有——因为 95598.js 是压缩脚本不好改）

**核心价值**：面板手动签到让用户不必等 cron 定时，点一下就能验证签到是否正常——**对所有签到类脚本都适用**。

## 13. 面板与通知内容拆分显示（2026-08-25 沉淀）

**需求**：签到面板卡片内容太长（每个贴吧"已经签到，当前等级X,经验Y"），面板卡片挤不下，但通知和日志又需要完整信息。

**做法**：面板脚本里建两个数组，分别构建面板文本和通知文本：
```js
var lines = [], notifyLines = [];
// 面板用精简版
lines.push('【' + bar + '】已经签到，当前等级' + level);
// 通知用完整版
notifyLines.push('【' + bar + '】已经签到，当前等级' + level + ',经验' + exp);

var panelContent = lines.join("\n");
var notifyContent = notifyLines.join("\n");

// 通知弹完整版
$notification.post('签到', '', notifyContent);
// 面板显示精简版
$done({ title: "签到", content: panelContent, ... });
```

**console.log 一般输出完整版**（通知版），方便调试。

**适用场景**：面板卡片空间有限，又不想丢失通知/日志的完整信息。通知和日志面向"查看详情"，面板面向"快速浏览"。

## 14. 面板脚本：既要自定义图标又要执行逻辑（2026-08-25 关键经验）

**需求**：PingMe 面板要显示 P 图标（p.circle），同时点面板要能真正执行签到。

**踩坑**：
- `$httpAPI("POST","/v1/scripting/evaluate",{script_text/url})` 触发签到 → **generic 面板里不生效**（点面板没反应）
- 面板脚本只返回图标不触发逻辑 → 签不到
- Env 框架脚本 `.done({})` 不返回自定义图标 → 面板显示默认 info 的 i

**正确方案**：面板脚本 = **原脚本完整副本 + 完成回调返回图标**。
- 复制 PingMeSignin.js → PingMePanelSignin.js
- 改完成回调：
```js
startTasks().then(r => {
    var isPanel = (typeof $script !== 'undefined' && $script.type === 'generic');
    if (isPanel) {
        $.done({ title:"🔄 PingMe 签到", content:"签到完成，详见通知", icon:"p.circle", "icon-color":"#007AFF" });
    } else {
        $.done();
    }
});
```
- `$script.type === 'generic'` 判断是面板环境，`.done({icon...})` 返回自定义图标
- cron 用原版脚本不受影响

**核心规律**：面板脚本"显示图标 + 执行逻辑"二合一 = 直接复用/复制原逻辑脚本，在完成点按环境返回图标。**别用 evaluate 触发，直接执行**。

## 15. 压缩脚本面板加自定义图标：$done 覆盖法（2026-08-25 成功）

**适用**：脚本是压缩/webpack bundle（如 95598.js，120KB），无法像 PingMeSignin.js 那样"复制+改完成回调"。

**方法**：复制原脚本为 Panel 版，在 IIFE（`(()=>{`）执行**前**插入一段覆盖全局 `$done`：
```js
(function(){
  if (typeof $script !== 'undefined' && $script.type === 'generic') {
    var _o = $done;
    $done = function(o){
      try {
        var obj = o || {};
        _o({ title: obj.title || "网上国网", content: obj.body || "点此签到/查账单", icon: "g.circle", "icon-color": "#007AFF" });
      } catch(e) { _o(o); }
    };
  }
})();
```
- 关键：在 webpack IIFE **之前**覆盖全局 `$done`，webpack 内部 `$done(e)` 会解析到覆盖版
- 仅 `$script.type==='generic'`（面板）时覆盖，cron 环境不受影响
- 面板脚本指向这个 Panel 版，generic 下既执行原签到逻辑又返回自定义图标

**验证**：`surge-cli script evaluate <Panel.js> generic 5` 结果返回 `{"icon":"g.circle","icon-color":"#007AFF",...}`，签到逻辑正常执行（cron mock 走原 $done）。

**模块**：95598整合.sgmodule（网上国网签到，author/category=mickeu），面板脚本 95598Panel.js。

**通用**：任何压缩脚本要面板加图标，都用这个"IIFE 前覆盖 $done"法。

## 规则审计：不改配置的出口对照

`surge-cli http probe <url> [policy]` 可为单次 HEAD 指定策略，无需临时规则或切组。先 `rule match` 记录实际命中，再比较默认请求与显式 `PROXY` 请求；修复后必须不带策略再测，证明真实分流生效。输出只保留 status/policy/rule/duration-ms，不回显 Set-Cookie 等响应头。

- 国内 IP 不必然必须直连，国外 IP 不必然必须代理；静态集合交集仅为候选。
- 广告在 Proxy_Supplement 之前：被 REJECT 的境外正常服务要放 Ad_Whitelist，不能只加代理补充。
- `external-resource update` 后，新增域名实际命中新规则集即可证明该条已生效，不必额外植入测试域名。

### 参考资料（来源）
- 官方 CLI：https://manual.nssurge.com/tools/cli.html
- 官方规则：https://manual.nssurge.com/rules/overview.html
- 实测：2026-10-09，Surge iOS 5.102.0 build 3864，Controller 25；Steam/Copilot 默认直连失败、显式 PROXY 200，更新规则后默认请求 200。规则修复提交：https://github.com/mickeu/surge/commit/c1880c1
