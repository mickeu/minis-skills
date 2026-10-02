---
name: Codex ChatGPT Web 桥接器
description: 把 ChatGPT Web（含 Pro 订阅）桥接成 Codex 应用原生模型的工具源码库。当用户提到"codex-chatgpt-web"、"ChatGPT Web for Codex"、"Codex 用 ChatGPT 网页"、"白嫖 ChatGPT 额度"、"Luna 模型"、"Temporary Chat 桥接"时触发。提供跨平台启动器安装、配置、模型选型、MCP 全工具链接法。
license: MIT
last_sync: 2026-08-24
---
# Codex ChatGPT Web 桥接器 (codex-chatgpt-web)

## 这是什么
用 **ChatGPT Web（含 Pro 订阅）** 作为 Codex 应用的**原生模型**。在 Codex 模型选择器里多出
"ChatGPT Web — Luna / Instant / Medium / High / Extra High / Pro" 选项，实际走 ChatGPT 网页
登录态（Temporary Chat），**不消耗 API 额度**。

- 项目地址：https://github.com/miuuyy/codex-chatgpt-web
- 作者：miuuyy（作者另有 ChatGPT-Persona-Voice 项目）
- 语言：TypeScript；许可证：MIT
- 创建：2026-07-26；数据同步时 1.4K star，持续更新
- 触发词：Codex 原生模型树里出现 "ChatGPT Web"，或用户问怎么用 ChatGPT 订阅跑 Codex 不花 API 额度

## 原理架构
```
Codex 任务 ──Responses+SSE──▶ codex-chatgpt-web ──内嵌浏览器──▶ ChatGPT
    ▲                                                              │
    └──── Codex 原生 UI、上下文、图片、工具链、MCP 全部保留 ───────┘
```
- Codex 保持原生任务框架、上下文生命周期、UI、流式、追踪、工具循环
- 本地 bridge 只把所选模型的这一次对话，路由到 ChatGPT 全新 Temporary Chat
- Full 模式用 MCP 把 ChatGPT 接回 Codex 任务的工具（文件系统、shell、图片、审批）
- 每任务独立浏览器 tab，至多 5 个并行（防账号流量过载）
- 浏览器角色本地优先：Codex 本地保存任务历史，浏览器从不跨任务复用

## 模型等级（按订阅）
- Free/Go 账号：仅 Luna
- 有推理选择器的账号：Instant / Medium / High / Extra High / Pro（按订阅）
- Pro 与其他 effort 完全同一套 MCP/上下文/图片/追踪合同，无特殊豁免

## 快速启动

### 安装桌面启动器（推荐）
```bash
curl -fsSL https://github.com/miuuyy/codex-chatgpt-web/releases/latest/download/install-launcher.sh | sh
```
Windows: `irm .../install-launcher.ps1 | iex`

完成后在 app 里做三件事：
1. 在启动器内嵌浏览器登录 ChatGPT（登录页/IdP 窗口都在同一私有 profile 内）
2. 跑浏览器冒烟测试
3. 按 "Install models"→ 重启 Codex → 选 "ChatGPT Web — …"

### 从源码运行
```bash
git clone https://github.com/miuuyy/codex-chatgpt-web.git && cd codex-chatgpt-web && bun run app
```

## 源码结构（本地克隆于本技能目录）
- `src/` — 核心源码
  - `adapters/chatgpt-web/` — ChatGPT 网页适配器（browser-worker、turn-broker、mcp-*、markdown、model）
  - `responses/` — Responses 协议（schema、compaction、reasoning-envelope）
  - `bridge.ts` — 主桥接逻辑；`model-catalog.ts` — 模型目录；`chatgpt-web-models.ts`
  - `native-passthrough.ts`、`tunnel.ts` / `tunnel-service.ts`
  - `cli.ts` / `setup.ts` / `doctor.ts` — 命令行与自检
- `launcher/` — Electron 桌面启动器（内嵌浏览器、runtime 安装、更新、控制服务）
- `scripts/` — build-runtime-bundle、build-browser-helper
- `tests/` — 大量合约测试（rolling-checkpoint、compaction-v1、bridge-platform、tunnel 等）

## ⚠️ 使用风险（重要）
- **非官方项目**，用网页登录态绕过 API 限制，违反 OpenAI 服务条款，**有账号封禁风险**
- Temporary Chat 只是隐私模式，**不是本地/匿名推理**，提示词仍由 OpenAI 处理，遵守 OpenAI 临时对话政策
- 数据同步时项目刚满月，作者更新勤，但属于灰色打法，建议小号或非主力账号试用

## 参考
- 源的 README（本项目内已存 README.md / README.zh-CN.md）
- docs/ 有 release-validation 等文档

minis_url: minis://skills/codex-chatgpt-web/SKILL.md