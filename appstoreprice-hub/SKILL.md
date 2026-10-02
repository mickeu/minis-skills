---
name: AppStore 价格查询
description: >-
  查询 App Store 全球各地区应用价格的技能，通过 appstoreprice.org 获取数据。
  使用 Minis 内置浏览器（minis-browser-use CLI）在页面上下文中直接调用网站原生签名函数，
  无需 API Key、无需自行实现签名算法。支持：按名称搜索应用、查询单个 App 所有地区价格、
  获取最便宜地区排行、分页浏览应用列表。
  当用户提到"App Store 价格"、"哪个区最便宜"、"土耳其区价格"、"appstoreprice"、
  "app 比价"、"App Store 低价区"、"订阅哪个区划算"，或任何需要查询 iOS/macOS App
  跨地区价格对比的场景，必须触发本技能。
source_url: https://appstoreprice.org
license: MIT
last_sync: 2026-07-26
---
# appstoreprice-hub

查询 [appstoreprice.org](https://appstoreprice.org) 的 App Store 全球价格数据。

> **数据来源**：[appstoreprice.org](https://appstoreprice.org)，由 [@qingnianxiaozhe](https://x.com/qingnianxiaozhe) 维护的非官方比价网站，实时抓取并对比全球各地区 App Store 价格。非 Apple 官方数据，价格每日更新。

## 原理

网站为 Next.js App Router，通过两种方式访问数据：

1. **REST API**（搜索/列表）：需要 FNV-1a 签名头 `X-Timestamp` + `X-Signature`
2. **RSC 页面流**（价格详情）：`fetch(url, { headers: { RSC: '1' } })` 直接解析

签名函数已内嵌在页面 webpack module（当前为 `22463`）中，直接在网站页面上下文里复用，无需自行实现。module ID 可能随网站部署更新变化，参见故障排查。

## 执行方式：minis-browser-use CLI

**始终使用 `minis-browser-use` CLI + shell 脚本执行**，不要用 `browser_use` tool call。

好处：JS 代码从文件读取直接传给进程，不会占用 agent 上下文。

### 标准模板

**所有步骤必须在同一个 `shell_execute` 调用里完成**，避免跨调用的 tab 状态失效。
业务逻辑用 `file_write` 写入临时文件再拼接，不用 heredoc（BusyBox ash 遇到花括号/引号容易解析出错）。

```bash
# 前提：用 file_write 把业务逻辑写入 /tmp/asp_logic.js，然后：

minis-browser-use navigate --url "https://appstoreprice.org/zh/apps" \
  && minis-browser-use wait_for_dom_stable --timeout 8 \
  && minis-browser-use execute_js --script "$(cat /var/minis/skills/appstoreprice-hub/scripts/api.js /tmp/asp_logic.js)"
```

> **为什么合并到一个 shell_execute？** `minis-browser-use` 的浏览器 tab 在两次 `shell_execute` 之间可能失效（tab 被回收），第二次调用时会报 `webpackChunk_N_E not found`。同一进程内串行执行可保证 tab 状态稳定。

## API 速查

`AppStorePriceAPI()` 返回 `{ search, list, prices, prices_all }`：

| 方法 | 参数 | 返回 |
|---|---|---|
| `search(query, page=1, limit=20)` | 关键词 | `{ apps, hasMore, total }` |
| `list(page=1, limit=20)` | 页码/每页数 | `{ apps, hasMore, total }` |
| `prices(appStoreId, locale='zh')` | App Store ID | **第一个** tier 的价格数组，按 priceUsd 升序 |
| `prices_all(appStoreId, locale='zh')` | App Store ID | **所有** tier 的价格数组列表（多 tier 订阅必用，如 Claude Pro/Max） |

`prices` / `prices_all` 每条：`{ region, regionName, currency, price, priceUsd, priceCny }`

> ⚠️ **多 tier 订阅**（如 ChatGPT Plus/Pro、Claude Pro/Max 等）必须用 `prices_all()`，`prices()` 只返回第一个订阅档位。

常用地区代码：`US` 美国、`TR` 土耳其、`NG` 尼日利亚、`PK` 巴基斯坦、`EG` 埃及、`AR` 阿根廷、`VN` 越南、`JP` 日本、`KR` 韩国、`CN` 中国、`HK` 香港

## 典型业务逻辑

### 多 tier 订阅

```js
const asp = AppStorePriceAPI();
const sr = await asp.search('Claude');
const app = sr.apps.find(a => a.developer?.includes('Anthropic'));
const tierNames = ['Claude Pro（月付）', 'Claude Max 5x（月付）', 'Claude Max 20x（月付）', 'Claude Pro（年付）'];
const allTiers = await asp.prices_all(app.appStoreId);
return allTiers.map((prices, i) => {
  const sorted = [...prices].sort((a, b) => a.priceUsd - b.priceUsd);
  const usPrice = prices.find(p => p.region === 'US')?.priceUsd;
  return {
    tier: tierNames[i] || `Tier ${i+1}`,
    usPriceUsd: usPrice,
    cheapestTop5: sorted.slice(0, 5).map(p => ({
      ...p, saveVsUS: usPrice ? Math.round((1 - p.priceUsd / usPrice) * 100) + '%' : 'N/A'
    }))
  };
});
```

### 最便宜 Top N

```js
const asp = AppStorePriceAPI();
const sr = await asp.search('ChatGPT');
const app = sr.apps[0];
const all = await asp.prices(app.appStoreId);
const topN = all.sort((a, b) => a.priceUsd - b.priceUsd).slice(0, 10);
const usPrice = all.find(p => p.region === 'US')?.priceUsd;
return { appName: app.name, topN: topN.map(p => ({
  ...p, saveVsUS: usPrice ? Math.round((1 - p.priceUsd / usPrice) * 100) + '%' : 'N/A'
}))};
```

### 指定地区价格

```js
const asp = AppStorePriceAPI();
const sr = await asp.search('Notion');
const all = await asp.prices(sr.apps[0].appStoreId);
return all.find(p => p.region === 'TR'); // 替换地区代码即可
```

## 结果展示规范

用 Markdown 表格展示，含：地区（国旗 emoji + 名称）、货币、原价、USD 等值、CNY 等值。
有对比场景时标注与美区折扣：`节省 = (1 - priceUsd / usPrice) * 100`。

## 故障排查

**签名函数未加载**：确认已 navigate 到 appstoreprice.org 页面并 wait_for_dom_stable。
`api.js` 会动态扫描所有 webpack module，通过函数体含 `X-Timestamp`/`X-Signature` 字符串来定位签名函数，无需 hardcode module ID。

**签名函数未找到（网站大改版）**：若报 "签名函数未找到"，说明签名头 key 名称可能已变更。
执行以下命令检查新特征：
```bash
minis-browser-use execute_js --script "
const define=(t,d)=>{for(const k in d) Object.defineProperty(t,k,{get:d[k],enumerable:true})};
const hits=[];
for(const [,m] of self.webpackChunk_N_E){
  if(!m) continue;
  for(const k of Object.keys(m)){
    try{
      const e={};m[k]({exports:e},e,{d:define});
      for(const fn of Object.values(e)){
        if(typeof fn!=='function') continue;
        const s=fn.toString();
        if(s.includes('X-') && s.length<800) hits.push({module:k,src:s.slice(0,200)});
      }
    }catch(e){}
  }
}
return hits.slice(0,5);
"
```
根据输出更新 `api.js` 中 `_getSignFn` 的特征字符串检测条件。
