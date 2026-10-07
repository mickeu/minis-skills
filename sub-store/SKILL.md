---
name: Sub-Store 订阅管理器
description: Sub-Store 高级订阅管理器知识库。支持 QX/Loon/Surge/Stash/Egern/Shadowrocket/Clash/Sing-Box 等代理工具，核心功能包括订阅转换、格式化、过滤/排序/重命名/脚本处理、多订阅合并、本地节点托管。当用户提到「Sub-Store」「订阅转换」「订阅管理」「订阅格式化」「sub-store」时触发。
source_url: https://github.com/sub-store-org/Sub-Store
source_repo: https://github.com/sub-store-org/Sub-Store
license: AGPL-3.0
last_sync: 2026-10-01
---
# Sub-Store 完整知识库

> 作者：Peng-YM | ⭐10,098 | 语言：JavaScript
> GitHub: https://github.com/sub-store-org/Sub-Store
> 官方前端: https://sub-store.vercel.app
> 文档站: https://sub-store-org.github.io/doc/
> Telegram 频道: https://t.me/sub_store
> CLI 管理工具：https://github.com/sub-store-org/Sub-Store-Manager-Cli

---

## 一、仓库架构（7 个仓库）

| 仓库 | ⭐ | 语言 | 大小 | 说明 |
|------|----|------|------|------|
| [Sub-Store](https://github.com/sub-store-org/Sub-Store) | ⭐10,098 | JS | 11.5MB | 核心后端，订阅转换/处理引擎 |
| [Sub-Store-Front-End](https://github.com/sub-store-org/Sub-Store-Front-End) | ⭐370 | Vue | 3.8MB | PWA 前端（Vite + Vue 3） |
| [Sub-Store-Manager-Cli](https://github.com/sub-store-org/Sub-Store-Manager-Cli) | ⭐139 | Go | 138KB | Docker CLI 管理工具 |
| [Sub-Store-Front-End-New](https://github.com/sub-store-org/Sub-Store-Front-End-New) | ⭐1 | Vue | 622KB | 新前端实验版 |
| [doc](https://github.com/sub-store-org/doc) | ⭐1 | CSS | 32KB | VitePress 文档站 |
| [resource](https://github.com/sub-store-org/resource) | ⭐0 | Shell | 9KB | 静态资源 |
| [.github](https://github.com/sub-store-org/.github) | ⭐0 | - | 5KB | 组织配置 |

---

## 二、核心功能

1. **格式转换**：在各代理工具格式之间互相转换
2. **订阅格式化**：过滤、排序、重命名、脚本处理
3. **多订阅合并**：将多个订阅合并为一个
4. **本地节点托管**：通过 sub.store 本地服务托管节点/文件
5. **定时同步**：自动同步配置到私有 Gist
6. **缓存处理**：定时处理耗时较长的订阅以更新缓存

---

## 三、各平台配置与安装

### 3.1 Surge 模块

**安装地址：**
```
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Surge.sgmodule
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Surge-ability.sgmodule
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Surge-Noability.sgmodule
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Surge-Beta.sgmodule
```

**核心脚本下载地址：**
```
https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-0.min.js
https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-1.min.js
https://github.com/sub-store-org/Sub-Store/releases/latest/download/cron-sync-artifacts.min.js
```

**Surge 模块配置参数：**

| 参数 | 默认值 | 说明 |
|------|--------|------|
| ability | http-client-policy | 测落地能力 |
| cronexp | 55 23 * * * | 同步定时任务 cron 表达式 |
| sync | Sub-Store Sync | 自定义定时任务名（设为 # 取消） |
| timeout | 900 | 脚本超时（秒） |
| engine | auto | 脚本引擎（auto/jsc） |
| produce | # Sub-Store Produce | 定时处理订阅任务名（设为 # 取消） |
| produce_cronexp | 50 */6 * * * | 处理订阅定时 |
| sync_success_notify | true | 同步成功通知 |
| produce_sub | - | 需定时处理的单条订阅名（多个用逗号分隔） |
| produce_col | - | 需定时处理的组合订阅名（多个用逗号分隔） |
| cors | https://sub-store.vercel.app,http://substore.stash,https://substore.stash | 浏览器跨域来源 |

**Surge 配置示例（完整）：**

```ini
#!name=Sub-Store
#!desc=支持 Surge 正式版的参数设置功能
#!category=订阅管理
#!arguments=ability:http-client-policy,cronexp:55 23 * * *,sync:"Sub-Store Sync",timeout:900,engine:auto,produce:"# Sub-Store Produce",produce_cronexp:50 */6 * * *,sync_success_notify:true,cors:"https://sub-store.vercel.app,http://substore.stash,https://substore.stash"

[MITM]
hostname = %APPEND% sub.store

[Script]
Sub-Store Core = type=http-request, pattern=^https?:\/\/sub\.store\/((download)|api\/(preview|sync|(utils\/node-info))), script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-1.min.js, requires-body=true, timeout=900, engine=auto
Sub-Store Simple = type=http-request, pattern=^https?:\/\/sub\.store, script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-0.min.js, requires-body=true, timeout=900, engine=auto
Sub-Store Sync = type=cron, cronexp="55 23 * * *", wake-system=1, timeout=900, script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/cron-sync-artifacts.min.js, engine=auto
```

### 3.2 Loon 插件

**安装地址：**
```
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Loon.plugin
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Loon-parser.plugin
```

**Loon 配置示例：**

```ini
#!name=Sub-Store
#!desc=高级订阅管理工具
#!openUrl=https://sub.store
#!author=Peng-YM
#!icon=https://raw.githubusercontent.com/58xinian/icon/master/Sub-Store1.png

[Argument]
cron=input, "55 23 * * *", tag=定时参数
sync_success_notify=switch, true, tag=同步成功通知
cors=input, "https://sub-store.vercel.app,http://substore.stash,https://substore.stash", tag=CORS允许来源

[Rule]
DOMAIN,sub-store.vercel.app,PROXY

[MITM]
hostname=sub.store

[Script]
http-request ^https?:\/\/sub\.store script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-0.min.js, requires-body=true, timeout=900, tag=Sub-Store Simple
http-request ^https?:\/\/sub\.store\/((download)|api\/(preview|sync|(utils\/node-info))) script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-1.min.js, requires-body=true, timeout=900, tag=Sub-Store Core
cron {cron} script-path=https://github.com/sub-store-org/Sub-Store/releases/latest/download/cron-sync-artifacts.min.js, timeout=900, tag=Sub-Store Sync
```

### 3.3 Quantumult X 配置

**安装地址：**
```
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/QX.snippet
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/QX-Task.json
```

**QX 配置示例：**

```ini
hostname=sub.store

^https?:\/\/sub\.store\/((download)|api\/(preview|sync|(utils\/node-info))) url script-analyze-echo-response https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-1.min.js
^https?:\/\/sub\.store url script-analyze-echo-response https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-0.min.js
```

### 3.4 Stash 覆写

**安装地址：**
```
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Stash.stoverride
```

**Stash 配置示例：**

```yaml
name: Sub-Store
desc: 高级订阅管理工具 @Peng-YM
icon: https://raw.githubusercontent.com/cc63/ICON/main/Sub-Store.png

http:
  mitm:
    - sub.store
  script:
    - match: ^https?:\/\/sub\.store
      name: sub-store-0
      type: request
      require-body: true
      max-size: -1
      timeout: 900
    - match: ^https?:\/\/sub\.store\/((download)|api\/(preview|sync|(utils\/node-info)))
      name: sub-store-1
      type: request
      require-body: true
      max-size: -1
      timeout: 900
```

### 3.5 Egern 配置

**安装地址：**
```
https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/config/Egern.yaml
```

**Egern 配置示例：**

```yaml
name: Sub-Store
description: "同步配置的定时 cronexp: 55 23 * * *"
icon: https://raw.githubusercontent.com/cc63/ICON/main/Sub-Store.png
compat_arguments:
  cronexp: 55 23 * * *
  sync: "Sub-Store Sync"
  produce_cronexp: 50 */6 * * *
  sync_success_notify: true
  cors: "https://sub-store.vercel.app,http://substore.stash,https://substore.stash"

scriptings:
  - http_request:
      name: Sub-Store Core
      match: ^https?:\/\/sub\.store\/((download)|api\/(preview|sync|(utils\/node-info)))
      script_url: https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-1.min.js
      body_required: true
      timeout: 900
  - http_request:
      name: Sub-Store Simple
      match: ^https?:\/\/sub\.store
      script_url: https://github.com/sub-store-org/Sub-Store/releases/latest/download/sub-store-0.min.js
      body_required: true
      timeout: 900
```

### 3.6 Shadowrocket 配置

通过 Sub-Store 前端（https://sub-store.vercel.app）生成订阅链接后，在 Shadowrocket 中添加订阅即可。

---

## 四、安全说明

### sub.store 域名风险

`sub.store` 仅用于模块脚本重写 MitM 规则，并非官方拥有的公共域名。

**防护措施：**

```ini
[Host]
sub.store = 127.0.0.1
```

### CORS 白名单

后端 API 支持可配置的浏览器 CORS 白名单：

- Node/服务器部署：使用环境变量 `SUB_STORE_CORS_ALLOWED_ORIGINS`（默认 `*`）
- 代理 App 模块：使用 `cors` 模块参数
- 多个来源用逗号分隔，设为 `*` 接受任意来源访问的风险

---

## 五、脚本列表（scripts/）

| 脚本 | 说明 | 下载地址 |
|------|------|---------|
| demo.js | 脚本示例 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/demo.js` |
| fancy-characters.js | 花体字符转换 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/fancy-characters.js` |
| ip-flag.js | IP 旗帜显示 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/ip-flag.js` |
| ip-flag-node.js | IP 旗帜节点版 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/ip-flag-node.js` |
| media-filter.js | 媒体过滤 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/media-filter.js` |
| revert.js | 订阅回退 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/revert.js` |
| tls-fingerprint.js | TLS 指纹 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/tls-fingerprint.js` |
| udp-filter.js | UDP 过滤 | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/udp-filter.js` |
| vmess-ws-obfs-host.js | VMess WS 伪装 Host | `https://raw.githubusercontent.com/sub-store-org/Sub-Store/master/scripts/vmess-ws-obfs-host.js` |

---

## 实战：节点名加后缀区分同名字节点

两个机场订阅节点同名时，客户端（Surge/Clash 等）会去重导致只显示一个机场的节点。给其中一个订阅的所有节点加后缀即可区分。

### 方式一：原生「重命名」操作（免脚本）

订阅编辑页 → 节点操作 → 添加操作 → 类型选「重命名」：
- 正则表达式：`(.*)`
- 新名称：`$1 A机场`

`(.*)` 捕获原节点名，`$1` 引用原名，末尾追加后缀。

### 方式二：脚本操作

给其中一个订阅添加「脚本操作」，粘贴 `scripts/add-suffix.js`（本技能目录）：

```javascript
function operator(proxies) {
  const { suffix = 'A机场', sep = ' ', overwrite = 'false' } = $arguments || {};
  return proxies.map(p => {
    if (!p.name) return p;
    if (overwrite !== 'true' && p.name.includes(suffix)) return p;
    p.name = `${p.name}${sep}${suffix}`;
    return p;
  });
}
```

- 「参数」字段可填：`suffix=B机场&sep= | `（远程链接则用 `#suffix=B机场`）
- `overwrite=true` 强制追加，默认自动跳过已包含后缀的节点，防止重复运行叠加
- 官方脚本 API：`function operator(proxies)` 中 `proxies` 为节点数组，可遍历修改后 `return`
- 官方文档：https://sub-store-org.github.io/doc/script/examples.html

### 实战：节点测活过滤失败节点

拉取订阅时对每个节点做连通性检测，失败的节点不输出，只有测活通过的节点才会被客户端拉取到。

**推荐脚本**：xream/scripts `availability.js`（仅支持 Surge/Loon/Egern 环境，Sub-Store 跑在 Surge 模块中可用）

```
https://raw.githubusercontent.com/xream/scripts/main/surge/modules/sub-store-scripts/check/availability.js#show_latency=true&keep_incompatible=true&status=204&url=http%3A%2F%2Fconnectivitycheck.platform.hicloud.com%2Fgenerate_204&timeout=2000&retries=1&retry_delay=1000&concurrency=10
```

**关键参数**（编辑页可视化参数编辑不需要 encodeURIComponent，链接方式需要）：
- `timeout`：单次请求超时毫秒，默认 5000；调小可更快筛掉慢节点
- `retries` / `retry_delay`：重试次数 / 重试延时（毫秒），默认 1 / 1000
- `concurrency`：并发数，默认 10
- `url`：测速 URL，默认 `http://connectivitycheck.platform.hicloud.com/generate_204`
- `status`：期望状态码正则，默认 204
- `show_latency`：节点名前显示延迟 `[123] 节点名`
- `keep_incompatible`：保留当前客户端不兼容的协议，默认不保留
- `cache=true`：开启测活缓存，配合「定时处理订阅」预热，避免客户端拉取超时

**注意**：
- ⚠️ **必须加 `cache=true` 并配合「定时处理订阅」**，否则每次客户端拉取订阅都会实时全量测活，后端处理变慢会导致客户端请求超时（实测 Surge 更新外部组报 -1001 请求超时 / Failed to parse remote resource data）
- 推荐参数：`timeout=2000&retries=0&retry_delay=1000&concurrency=20&show_latency=true&keep_incompatible=true&cache=true`（关闭重试、提高并发，配合缓存）
- 脚本 `return validProxies`，只输出测活通过（状态码匹配）的节点；失败/超时节点被过滤
- 过滤结果是基于脚本运行时的网络环境，当前网络连不上的节点（如某些专线）会被移除，不代表节点永久失效
- 可与加后缀脚本叠加使用（操作按顺序执行），先加后缀再测活，输出节点名带后缀且均为可用节点
- 说明帖：https://t.me/zhetengsha/1210 ；脚本源码：https://github.com/xream/scripts/blob/main/surge/modules/sub-store-scripts/check/availability.js

## 六、核心后端架构（backend/）

```
backend/
├── src/
│   ├── main.js                    # 主入口
│   ├── constants.js               # 常量定义
│   ├── core/
│   │   ├── app.js                 # 核心引擎（基于 OpenAPI）
│   │   ├── proxy-utils/           # 代理工具函数
│   │   └── rule-utils/            # 规则工具函数
│   ├── products/
│   │   ├── sub-store-0.js         # 基础版本输出
│   │   ├── sub-store-1.js         # 完整版本输出
│   │   ├── resource-parser.loon.js # Loon 资源解析器
│   │   ├── proxy-utils.esm.js     # 代理工具 ESM 版本
│   │   └── cron-sync-artifacts.js # 定时同步脚本
│   ├── restful/                   # REST API（23 个端点）
│   │   ├── index.js               # API 入口
│   │   ├── subscriptions.js       # 订阅管理
│   │   ├── collections.js         # 组合订阅管理
│   │   ├── sync.js                # 同步
│   │   ├── preview.js             # 预览
│   │   ├── download.js            # 下载
│   │   ├── parser.js              # 解析器
│   │   ├── settings.js            # 设置
│   │   ├── artifacts.js           # 产物管理
│   │   ├── archives.js            # 归档
│   │   ├── file.js                # 文件
│   │   ├── sort.js                # 排序
│   │   ├── token.js               # Token 管理
│   │   ├── logs.js                # 日志
│   │   ├── module.js              # 模块
│   │   ├── miscs.js               # 杂项
│   │   ├── node-info.js           # 节点信息
│   │   ├── age.js / age-output.js # 时效管理
│   │   ├── response.js / response-transformer.js  # 响应处理
│   │   ├── ignore-failed-remote-sub.js # 忽略失败订阅
│   │   └── errors/                # 错误处理
│   ├── utils/                     # 工具函数
│   └── vendor/                    # 第三方依赖（含 OpenAPI）
├── dist/                          # 编译输出
├── config/                        # 各平台配置
├── scripts/                       # 示例脚本
└── docs/brainstorms/              # 设计文档
```

---

## 七、Sub-Store-Manager-CLI（Docker 管理工具）

项目地址：https://github.com/sub-store-org/Sub-Store-Manager-CLI

- ⭐139 | Go | 138KB
- 基于 Docker 的命令行管理工具

### 安装

```bash
curl -sSL https://sub-store-org.github.io/resource/ssm/install.sh | bash
```

### 命令

```bash
# 创建并运行后端容器
ssm new
# 创建前端容器
ssm new -i
# 自定义名称
ssm new -n my-sub-store
# 指定版本
ssm new -v v1.0.0
# 指定端口
ssm new -p 3000
# 查看容器列表
ssm ls
# 删除容器
ssm delete
```

### 安全特性

从 v0.0.12 开始，ssm 自动为后端服务容器创建随机哈希前缀防止被扫描：

```
http://localhost:3000/4424703b2bae575f0861bf07eafa
```

使用 `ssm ls` 查看容器对应的哈希前缀。

---

## 八、Sub-Store-Front-End（PWA 前端）

项目地址：https://github.com/sub-store-org/Sub-Store-Front-End

- ⭐370 | Vue 3 + Vite + TypeScript
- 在线使用：https://sub-store.vercel.app
- API 后端地址：https://sub.store

### 目录结构

```
src/              # 源码
public/           # 静态资源
scripts/          # 构建脚本
vercel.json       # Vercel 部署配置
vite.config.ts    # Vite 构建配置
```

### 环境变量

```env
# 开发环境
VITE_PORT = 8888
VITE_PUBLIC_PATH = '/'

# 生产环境
VITE_API_URL = 'https://sub.store'
```

---

## 九、后端 API 端点（RESTful）

Sub-Store 后端提供 23 个 REST API 端点：

| 端点 | 说明 |
|------|------|
| `/api/subscriptions` | 订阅管理（CRUD） |
| `/api/collections` | 组合订阅管理 |
| `/api/sync` | 同步配置 |
| `/api/preview` | 预览订阅内容 |
| `/api/download` | 下载订阅 |
| `/api/parser` | 解析器 |
| `/api/settings` | 设置管理 |
| `/api/artifacts` | 产物管理 |
| `/api/archives` | 归档管理 |
| `/api/file` | 文件管理 |
| `/api/sort` | 排序 |
| `/api/token` | Token 管理 |
| `/api/logs` | 日志查询 |
| `/api/module` | 模块管理 |
| `/api/node-info` | 节点信息 |
| `/api/age` | 时效管理 |
| `/api/response` | 响应处理 |

---

## 十、FAQ

### sub.store 安全吗？

`sub.store` 是模块重写 MitM 使用的域名，不是官方拥有的公共域名。建议在配置中添加 `sub.store = 127.0.0.1` 到 `[Host]` 段以防止数据泄露。官方前端地址是 `https://sub-store.vercel.app`。

### 如何部署后端？

推荐使用 Sub-Store-Manager-CLI（Docker）部署，或者手动部署 Node.js 后端。

### 支持哪些代理工具？

Surge、Quantumult X、Loon、Stash、Egern、Shadowrocket，以及通过订阅转换支持的 Clash/Mihomo、Sing-Box 等。

### 如何使用脚本功能？

在 Sub-Store 前端中，可以为订阅配置脚本处理，支持 JavaScript 脚本对节点进行过滤、排序、重命名等操作。