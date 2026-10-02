# Exa 知识库

Exa 官方技术文档完整语料库（llms.txt 格式，2026 年抓取）。**来源**：Exa 官方文档站 https://docs.exa.ai/ （语料入口 https://docs.exa.ai/llms.txt）。当用户询问 Exa 的各类 API、产品、集成、SDK 时触发。

## 触发场景

用户提到：**「exa ai」**、Exa、Exa Search、Exa Contents、Exa Agent、Websets、Monitors、Exa Connect、Code Search、Company Search、People Search、News Search、exa-mcp、exa-py、exa-js、Deep Search、Agent Skills（exa-labs）等。

> 用户明确约定：发「exa ai」即触发本技能。

## 文档位置

- 完整语料库：`/var/minis/skills/exa-knowledge/docs/exa-docs-full.md`（24,222 行，约 1MB）

## 查询方法

文档是单一大文件。根据所需内容用 grep/sed 定位章节，再读取关键段落：

```bash
# 定位某个产品/主题在主章节中的行号
grep -n "^# Exa Search API\|^# Contents API\|^# Websets" docs/exa-docs-full.md

# 读取某个章节（例如搜索 "Search API Reference" 起始行）
grep -n "^# Search API Reference" docs/exa-docs-full.md
```

## Exa 产品与对应主章节索引

| 产品 | 文档章节 | 说明 |
|---|---|---|
| **Search API** | `# Exa Search API` / `# Search API Reference` / `# Search Best Practices` | 网页搜索，Deep Search 多步推理 |
| **Contents API** | `# Contents API` / `# Contents API Reference` / `# Contents Retrieval` / `# Crawling Subpages` | 从 URL 提取 LLM 可用内容，pdf/JS 渲染页等 |
| **Exa Agent** | `# Exa Agent` / `# Examples` / `# Cancel a run` 等 | 多步网页研究、建清单、富集，结构化输出 |
| **Websets** | `# Websets` / `# Websets Reference (For Your Coding Agent)` / `# How Websets Works` / `# Criteria vs Enrichments` | 复杂全网找数据，自动搜索+验证+富集 |
| **Monitors** | `# Monitors` / `# Monitors API Reference` | 定时搜索，结果推送 webhook |
| **Exa Connect** | `# Exa Connect` / `# Agent API Connect` | 接 premium 数据源（Fiber.ai/Similarweb/Polymarket/Particle/FinancialDatasets/Jinko 等） |
| **Code Search** | `# Code Search` / `# Code Search Reference` | 代码检索 |
| **Company Search** | `# Company Search` / `# Company Search Reference` | 公司检索 |
| **People Search** | `# People Search` / `# People Search Reference` | 人物检索 |
| **News Search** | `# News Search` / `# News Search Reference` | 新闻检索 |
| **OpenAI 兼容** | `# OpenAI SDK Compatibility` / `# OpenAI Tool Calling` | 可作 OpenAI drop-in 替换 |
| **Anthropic** | `# Anthropic Tool Calling` | Claude tool use |
| **MCP Server** | `# Web Search MCP` | 接 Claude/Cursor/Codex/VS Code |
| **Agent Skills** | `# Agent Skills`（+ Build with Exa / Exa Search / Exa Contents / Lead Generation / Company Research） | 可装进 Claude Code/Cursor/Codex |
| **SDK** | `# Python SDK` / `# JavaScript SDK` / `# Python SDK Specification` / `# TypeScript SDK Specification` / `# Python and TS Cheat Sheets` | exa-py / exa-js |
| **Batch API** | `# Batch API` | 批量请求 |
| **Error Codes** | `# Error Codes` | 错误码对照 |
| **Rate Limits** | `# Rate Limits` | 限流 |
| **Pricing** | `# Pricing` / `# Pay with MPP (Tempo)` / `# Pay with x402` | 定价与支付方式 |
| **API Keys** | `# Create API Key` 等 | key 管理（dashboard） |

## 关键信息速查

- **API Base**：`https://api.exa.ai`（搜到 `/search`、`/contents`、`/answer` 等端点；可用 OpenAPI spec 精确定位，见下）
- **OpenAPI 规范**：`# OpenAPI Specification` 章节给出 `https://exa.ai/docs/exa-spec.json / .yaml`，请求/响应 schema 以 spec 为准
- **文档通用后缀**：Exa docs 页面 Markdown 可用（URL 追加 `.md`），方便直接抓取单个页面更新
- **免费额度**：新账号 $20 送，每月 $10 免费额度，免绑支付方式，覆盖所有 API 端点
- **语音 Agent**：Exa 提供 voice agent 构建文档（`# Building a Voice Agent with Exa`）

## 网络代理注意

访问 Exa 文档/API 域名（exa.ai / api.exa.ai）时注意 Surge 分流规则是否命中规则集。若直连超时，考虑走 PROXY。

## 维护

文档为抓取快照。版本更新时用：
```bash
curl -sL https://exa.ai/docs/llms-full.txt > /var/minis/skills/exa-knowledge/docs/exa-docs-full.md
```
