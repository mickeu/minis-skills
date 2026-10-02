---
name: AppStore IAP 价格排行
version: 1.1.0
description: 通用查询 iOS/App Store 应用内购或订阅在各地区的价格，并换算成人民币排名；当用户询问任何 App 的 iOS 内购价格、App Store 哪个地区最便宜、订阅地区价、换算人民币 Top N（如 Claude/ChatGPT/Perplexity/Netflix/Spotify/YouTube 等）时触发。优先联网获取最新价格表和汇率，输出最便宜地区排名、人民币金额和来源。
source_url: https://opentherank.com
license: MIT
last_sync: 2026-07-26
---
# App Store IAP Price Ranking

用于查询任意 App 的 iOS/App Store 内购或订阅地区价格，并换算成人民币排名。Claude 只是常见案例；本 skill 应通用于任何可查到 App Store IAP 地区价的 App。

## 触发示例

- “查询 Claude 用 iOS 内购价格换算成人民币之后最便宜的 10 个地区”
- “ChatGPT iOS Plus 哪个区最便宜”
- “Perplexity App Store 年费地区价人民币排名”
- “Netflix / Spotify / YouTube iOS 订阅各区价格”
- “某某 app 内购换算人民币 Top 20”

## 标准流程

1. 识别用户要查的对象：
   - App 名称，例如 Claude、ChatGPT、Perplexity、Netflix、Spotify、YouTube。
   - 平台：默认 iOS/App Store 内购。
   - 计划/商品：若用户未指定，选择该 App 最常见的月付订阅档；若有多个同名计划，先说明采用的计划，必要时追问。
   - 排名数量：默认 Top 10。
2. 联网获取该 App 的 App Store/IAP 地区价格表。优先搜索/来源：
   - OpenTheRank：`<app> Price by Country App Store OpenTheRank`
   - AppPriceLens：`<app> Global Prices AppPriceLens`
   - Sensor Tower / App Store listing / 官方价格页 / 其他可核验价格表
   - Claude 特例可优先：`https://opentherank.com/ai-pricing/claude/`
3. 读取页面中的地区表，尽量提取：排名、地区/国家、计划/商品名、本地货币价、美元折算价、税费说明、更新时间。
4. 获取 USD→CNY 当前汇率。优先使用公开接口，例如：
   - `https://open.er-api.com/v6/latest/USD` 的 `rates.CNY`
   - 如接口失败，可用浏览器搜索“USD CNY exchange rate”并说明汇率来源。
5. 按用户指定计划和数量排序输出：
   - 默认排序：人民币折算价从低到高。
   - 默认换算：若来源已有美元折算，`人民币 = 美元折算价 * USD_CNY`；若只有本地货币价，先用可靠汇率转 USD 或直接转 CNY，并标注汇率来源。
   - 金额保留 2 位小数。
6. 输出表格字段：排名、地区、iOS 内购本地价、美元折算、人民币约；若美元折算不可得，可改为“人民币约/汇率来源”。
7. 结尾注明：数据来源 URL、价格更新时间、汇率、实际扣款可能受 App Store 税费/礼品卡汇率/手续费影响。

## 推荐实现

优先用 `browser_use` 打开价格来源并 `get_text`；如果页面动态渲染，使用 `wait_for_dom_stable`、`scroll_and_collect` 或搜索结果摘要辅助。再用 `shell_execute` 或 Python 脚本完成汇率抓取和计算。不要只凭记忆回答。

示例汇率脚本应写入文件后运行，避免 heredoc：

```python
import urllib.request, json
url = 'https://open.er-api.com/v6/latest/USD'
data = json.load(urllib.request.urlopen(url, timeout=10))
print(data['rates']['CNY'])
```

## 回答格式

```markdown
按 <来源> 的 <App> iOS/App Store <计划/商品> 地区价格表（更新：<月份/日期>）和当前汇率 1 USD ≈ <rate> RMB 粗算，最便宜 <N> 个地区如下：

| 排名 | 地区 | iOS 内购本地价 | 美元折算 | 人民币约 |
|---:|---|---:|---:|---:|
| 1 | 尼日利亚 NG | ₦14,900/月 | $10.94 | ¥74.26/月 |
...

来源：<URL>
注意：实际扣款可能受 App Store 税费、汇率、礼品卡汇率/手续费影响。
```

## 注意事项

- 若用户明确要求“最新”，必须重新联网查询。
- 若用户要求年付、Max、Plus、Pro、Family、Team 等具体计划，不要复用其他计划价格；重新提取对应列。
- 如果找不到完整地区价格表，给出已核验地区的排名，并明确“非完整榜单”。
- 不要提供规避地区限制、虚假地址等操作建议；只做价格信息查询和换算。
