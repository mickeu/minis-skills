---
name: rea
description: REA（Reverse Engineer Anything）—— 一个基于 MCP 的逆向工程工具，让 AI Agent 直接分析原生二进制、JavaScript/Electron 应用、.NET 程序集、Android APK、网页、抓包等。当用户提到 REA、morluto/rea、rea-agents、逆向工程 MCP、分析二进制/ASAR/APK/Electron 应用时使用。
---

# REA（Reverse Engineer Anything）

REA 是一个开源逆向工程工具，通过 MCP 把逆向工具链接入 AI Agent。Agent 调用 REA 检查目标、返回**带证据**的分析结果，再据此解释行为、追查代码或编写实现。所有分析均在本地运行，结论附带证据与局限性说明。

官方来源只有三个：**GitHub `morluto/rea`**、**rea.tools 官网**、**npm `rea-agents` 包**。README 明确警告存在仿冒仓库，安装/下载必须走官方来源。

## 快速上手

```bash
# 给 Agent 注册 REA（交互式，可多选 agent）
npx rea-agents setup
```

- setup 会添加 REA 的 MCP server 和对应工作流指令，并备份现有配置，之后需重启 agent。
- 支持 Claude Code、Codex、Cursor、Gemini CLI、Grok Build 等。
- 需要在 Node.js 22.x (>=22.19) / 24.x (>=24.11) / 26+ 和 npm 下运行。

## CLI 使用（不依赖 agent）

```bash
# 一次性分析 JavaScript/Electron 应用目录或 ASAR
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
# 结果包含 modules、imports、Electron boundaries 及其证据

# 全局安装后用 rea 命令
npm install --global rea-agents
rea --help

# 更新
rea update          # 别名 rea --update，同样支持全局输出 flag
npx rea-agents@latest setup   # 更新后需重新跑 setup 刷新 agent 注册
```

更新器最多保留 4 MiB 合并 stdout/stderr；Bun 全局更新需 Bun 1.2.17+。

## 可分析的目标与前置要求

| 目标 | REA 返回什么 | 要求/指南 |
|---|---|---|
| 原生二进制 | 伪代码、汇编、字符串、符号、调用与引用 | Hopper / Ghidra / IDA，见 native analysis |
| 离线 ELF 布局 | 段、节、原始符号/重定位、静态缓解候选 | 调用方提供 pwntools（Linux x64） |
| Go 二进制 | 编译器版本、模块、替换、构建设置 | 内置静态 ELF/PE/thin Mach-O 检查，无需 Go |
| Rust 二进制 | cargo-auditable crate 名/版本/来源/依赖边 | 内置静态检查 |
| WASM 工件 | 验证、段、精确导入导出 WAT 形式 | 调用方提供 WABT 1.0.42 |
| EVM bytecode | 派发选择器、字节偏移、推断参数与可变性 | 本地 raw/hex carrier（Linux x64） |
| SQLite 数据库 | 表、列、索引、视图、触发器、普通行数据 | 本地 DB/WAL 快照，Node 24.x>=24.15 或 26+ 原生 SQLite |
| 记录的 Linux 崩溃 | 原始 notes、每线程寄存器/信号、映射候选 | 调用方提供 pwntools，可选 GDB/pwndbg |
| JavaScript / Electron | 模块、导入、sourcemap、路由、IPC、原生插件关系 | Node.js + npm；Linux 需 procps 兼容 ps；application analysis |
| 网站 | 页面结构、脚本、网络观察、请求截图 | Chrome 系浏览器；browser analysis |
| 网络抓包 | 请求/响应、暴露的 payload、来源位置 | HAR 或 Fiddler SAZ；Linux 用 mitmproxy |
| .NET 程序集 | 元数据、CIL 指令、声明原生依赖、构建对比 | 纯静态，见 managed-code guide |
| Android APK | Manifest、类、反编译方法、引用 | Headless JADX + JDK（Linux/macOS/Windows x64） |
| Android 设备 | 设备、包、进程、日志、dump、截图、APK 传输 | 调用方提供 adb |
| JEB 项目 | 项目单元、artifact 摘要、类型/方法伪代码 | 调用方启动 JEB client 供 MCP |
| Android 资源 | 解码的 manifest、字符串表、locale、版本事实 | 调用方提供 Apktool |
| Flutter 应用 | Dart snapshot 哈希、各 ABI 库摘要、引擎来源 | 纯静态 APK 解析 |
| 固件 | 分区、提取结果、原生分析交接 | Binwalk / Unblob（Linux） |
| 记录的数据包 | 选定字段、重复值、过滤、解码规则 | Linux: TShark 4.x + prlimit |
| 数据包摘要 | 端点、DNS、TLS SNI、协议分布、HTTP 请求 | 调用方提供 tshark + capinfos |
| 记录的逻辑信号 | 解码注释、采样范围、诊断 | Linux: sigrok-cli 0.7.2 + prlimit |
| Apple 应用包 | 文件清单、摘要、plist、bundle 解剖、提取资源 | artifact + JavaScript guide |
| 进程行为 | 终端输出、交互、退出、文件系统观察、运行对比 | Linux/macOS 原生 PTY；process capture |

- 静态 JS/.NET 检查只读文件、不运行应用；运行时抓取会按用户权限交互运行目标，各运行时指南会说明影响。
- 原生二进制离线检查还支持调用方提供的 GNU objdump 和 Rizin。REA **不安装**任何 provider。
- 大二进制可调 `REA_GHIDRA_STARTUP_TIMEOUT_MS` / `REA_HOPPER_STARTUP_TIMEOUT_MS` 提高启动超时。
- 版本变化快，npm 最新发布里可能有新功能，看 GitHub releases。

## iSH / Alpine 环境实测（2026-10-18，Minis 本机）

在 Minis 的 iSH（Alpine 3.21）中试装 rea@6.7.0：

- `npm install --global rea-agents` 成功，`rea --help` 正常。
- `rea doctor`：node 健康（v22.23.2），但 host 判定 `unsupported_host`（Alpine 不在 apt/dnf/pacman 支持列表）；Ghidra/Hopper/IDA/JADX/Kuna 均未配置（需按官方指南补）。
- **静态 JS 分析可用**：`rea analyze-javascript-application <目录> --json` 能正常解析 CJS/ESM、依赖图、调用流、数据流，输出完整 JSON（含证据与局限性）。
- 进程所有权检查在 iSH 上受限：分析结束报 `cleanup_incomplete`（`process ownership token could not be read for 5 live process(es): environment_errno_ENOENT`，即读 `/proc/<pid>/environ` 失败），但不影响已生成的分析结果。
- **路径坑**：分析目标不要放 `/var/minis/` 挂载目录（rea 内部 `realpath` 报 ENOENT）；复制到 rootfs 原生路径（如 `/tmp/xxx`）即可正常分析。`ls`/`existsSync` 正常但 `realpath` 失败是挂载目录的典型表现。
- 分析前先 `apk add procps` 提供 GNU ps。

## Linux owned-process 前置要求

在 Linux 上，Ghidra、JADX、固件工具启动和静态 JS/Electron 分析需要 procps 兼容的 `ps` 在 REA 的 PATH 上（用于进程所有权检查）。恢复步骤见 `docs/installation.md` 的 "Linux owned-process prerequisite"。Alpine/BusyBox 环境可装 `procps`。

## 参考资料（来源）

- **GitHub 仓库**：https://github.com/morluto/rea （README 各语言版，2026-10-18 抓取）
- **官网**：https://rea.tools （含 Guides、Showcases、FAQ、Documentation）
- **npm 包**：`rea-agents`
- **文档目录**：仓库内 `docs/installation.md`（含 Linux owned-process 前置、provider 配置等）、`docs/` 下各类分析指南
- **案例**：DX-Ball 声像计算重建（3,205 条 x86 用例通过）、Notion Electron 剪贴板桥、TH04 恢复子弹环计算等
- **创建/调研日期**：2026-10-18
- **安装来源校验**：仅认 `morluto/rea`、rea.tools、npm `rea-agents` 三个官方来源，警惕仿冒仓库