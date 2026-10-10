# Hako 覆写脚本（Override Script）

> Hako iOS/macOS 客户端（Hako-Client）的功能，**不属于 mihomo 内核**。  
> 来源：Hako-Client 源码 `Sources/ConfigUI/ScriptEngine.swift`、`Sources/ConfigUI/ScriptSettings.swift`、`Sources/AppArchitecture/ProfileAdvancedOverridesDomain.swift`（HEAD `b0583224`，2026-09-07）。以下结论均来自源码逐行核对，非文档推测。

## 一、本质与定位

Hako 的"覆写脚本"= 在**订阅下载后、内核解析前**，用 **JavaScriptCore (JSContext)** 跑一段用户 JS，对完整配置对象做任意变换。等价于把 mihomo 老内核的 `experimental.preprocess-script` 放到 App 外壳实现——**Hako 内核（ProjectClash/Clash-Legacy，原 TokenPLS/Hako）的 `experimental` 段已砍掉 `preprocess-script`**，只留 `quic-go-disable-gso/ecn`、`ip4p-enable`，所以**只能通过 App 的"覆写脚本"入口实现配置预处理**，写配置文件 `preprocess-script:` 字段无效。

## 二、接口规范（必须遵守，否则 Hako 拒绝）

```javascript
function main(config) {
  // config 是配置对象(JS Object), 已由 App 用 yamlToJSON 转好
  // 可任意修改 config 的字段: config.proxies / config.rules / config['proxy-groups'] / config['log-level'] 等
  return config;  // 必须返回配置对象
}
```

**硬校验（`ScriptEngine.swift`，不满足直接报错）**：

| 校验 | 报错文案 |
|---|---|
| 脚本必须定义 `main` 且是 function | `script must define main(config)` |
| `main(config)` 返回不能是 null | `script must return the config object` |
| 返回不能是 array | 同上 |
| 返回必须是 object | 同上 |
| 执行超 5 秒会被强制中止 | `The script ran too long and was stopped` |
| 脚本抛异常 | `script threw: <msg>` |
| JSContext 不可用 | `script engine unavailable` |

App 还会在调用 `main` 前自动做一件事：**若 config 是 object 且没有 `proxy-providers` 字段，自动补 `config['proxy-providers'] = {}`**（源码 `(function(){var config=JSON.parse(...); if(config['proxy-providers']===undefined) config['proxy-providers']={}; ...})`）——所以脚本里直接用 `config.proxies` 即可，不必关心这个补丁。

## 三、Profile 的三种覆写模式（`Profile.OverwriteMode`）

`Profile.swift` 定义 `enum OverwriteMode: String { case standard; case script; case custom }`：

| 模式 | 入口 | 干什么 |
|---|---|---|
| `standard` | 结构化覆写（Swift `CustomOverwriteSpec`）| UI 表单编辑 proxy-groups/rules，不做 JS |
| **`script`** | 覆写脚本（本文件主题）| 选一个本地 JS 脚本，跑 `main(config)` |
| `custom` | —— | 保留枚举值 |

UI 入口：Hako 配置详情页 → **覆写脚本** → **手动**（直接粘贴 JS）或 **URL 导入**（`https://.../xxx.js`）。界面占位符就是 `https://example.com/script.js`。

`ProfileAdvancedOverridesDomain.swift`：选 script 模式但未指定脚本 → `Choose a local script before using Script mode.`

## 四、关键坑：JSContext 不要用正则字面量

JSContext（JavaScriptCore）对**跨行或含特殊字符的正则字面量**解析不稳，会报：

```
SyntaxError: Unterminated regular expression literal
```

**避免**这种写法（在 Hako 里会炸）：
```javascript
var re = /剩余流量|距离.*重置|.../i;   // ❌ 字面量，长正则容易 unterminated
```

**改用**字符串拼接 + `new RegExp`：
```javascript
var junk = '剩余流量|距离.*重置|套餐到期'
         + '|请每月|每月更.?新|更新.*订阅'
         + '|更换客户端|clashmeta客户端|...';
var re = new RegExp(junk, 'i');   // ✅ 字符串构造，稳
```

字符串方式对中文/竖线/特殊字符更宽容，JSContext 解析稳定。

## 五、实战范例：过滤机场「非法伪节点」

机场订阅常塞进"剩余流量/套餐到期/请更换客户端/ios-小火箭"等假节点（连不上、无 server 字段或仅占位），在客户端节点列表里是垃圾。用覆写脚本一次性剔除，**以后无论加载什么订阅都自动过滤**。

```javascript
function main(config) {
  // 要剔除的节点名特征（新增机场只需往这里加词）
  var junk = '剩余流量|距离.*重置|套餐到期|请每月|每月更.?新|更新.*订阅'
           + '|更换客户端|客户端已过时|客户端太旧|请更换|新版.*客户端'
           + '|clashmeta客户端|clashverge客户端|shadowrocket客户端|小火箭客户端'
           + '|ios-小火箭|安卓-|安卓客户端|电脑-|win电脑|macos-'
           + '|ipv6免流|免流.*host|教程.*有下载|占位|测试节点|失效|停用|维护中';
  var junkRe = new RegExp(junk, 'i');

  if (!Array.isArray(config.proxies)) return config;

  config.proxies = config.proxies.filter(function (p) {
    var name = (p && p.name) ? String(p.name) : '';
    return !junkRe.test(name);
  });

  return config;
}
```

**已验证（2026-09-22）**：
- 白嫖机场订阅 46 节点 → 保留 37（剔除 9：剩余流量×2/距离重置/套餐到期/请每月更/更换客户端/clashmeta客户端/clashverge客户端/ios-小火箭/ipv6免流）
- 极速机场订阅 27 节点 → 保留 24（剔除 3：剩余流量/距离重置/套餐到期）
- 真节点完整保留，0 残留非法节点

## 六、其它常用覆写片段

```javascript
// 改日志级别
config['log-level'] = 'warning';

// 给节点名打前缀
config.proxies = config.proxies.map(function(p){
  p.name = '[订阅] ' + p.name; return p;
});

// 在规则最前面插一条
config.rules = ['MATCH,DIRECT'].concat(config.rules || []);

// 强制所有节点开启 UDP
config.proxies.forEach(function(p){ p.udp = true; });

// 删除某个策略组
config['proxy-groups'] = config['proxy-groups'].filter(function(g){
  return g.name !== '不要的组名';
});
```

## 七、与内核 `proxy-providers.exclude-filter` 的关系

| 维度 | 覆写脚本 | `proxy-providers.exclude-filter` |
|---|---|---|
| 作用范围 | 整份配置（含内联 proxies + 所有 provider 拉来的节点） | 单个 provider 拉取的节点 |
| 类型 | JS 函数，任意逻辑 | 单条正则字符串 |
| 触发时机 | 订阅下载后、解析前 | provider 拉取后、入组前 |
| 配置文件可见 | 否（App 外壳管理） | 是（写进 yaml） |
| 适合场景 | 跨多机场统一过滤、复杂改名/重组 | 单 provider 简单正则剔除 |

两者**可并用**：`exclude-filter` 处理 provider 内节点，覆写脚本兜底处理内联节点和跨订阅统一规则。
