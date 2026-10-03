---
name: Clash 控制器
description: 通过 mihomo/Hako RESTful API 实时监控和控制 Clash，对标 surge-ios。支持状态/连接/流量/规则查询、节点与策略组切换、节点测速、DNS 查询、配置重载。当用户提到 Clash、Hako、mihomo、切换节点、查看连接、实时流量、规则匹配、节点测速、Clash 控制器时使用。
---

# Clash 控制器（mihomo / Hako RESTful API）

通过 `clash-cli`（封装 mihomo RESTful API）在 Minis 内实时监控和控制 Clash，能力对标 `surge-ios`。Clash 配置语法参考 `clash-config` 技能，本文档只管运行态操作。

## 1. 入口授权（前提检查）

- **Clash/Hako 必须正在运行（VPN 开启）**，`external-controller` 才会监听端口。未启动时 `clash-cli` 报「连接失败」。
- 默认 API 地址 `http://127.0.0.1:9090`（iSH 已验证可直通 iOS 本机 localhost）。
- secret 从环境变量 `CLASH_SECRET` 读取；未设置则免认证直接访问。
- 入口检查：`clash-cli status` 能返回版本、模式、内存、策略组即通过。

```bash
clash-cli status
# mihomo 1.19.32  meta=True
# mode=rule  mixed-port=7890  tun=True stack=gVisor
# 内存 31MB  inuse=0KB
# 策略组 13 个：
#   PROXY → AUTO
```

## 2. 状态检查

| 命令 | 说明 |
|---|---|
| `clash-cli status` | 版本/模式/内存 + 所有策略组当前选择 |
| `clash-cli proxies` | 列全部代理条目（含叶子节点与策略组） |
| `clash-cli proxies <组>` | 查看某策略组当前选择、类型、成员列表 |
| `clash-cli traffic [秒]` | 实时流量 SSE（默认 3 秒，显示瞬时速率+累计） |
| `clash-cli connections [N]` | 活跃连接列表（host→策略组→命中规则→上下行），默认前 20 |
| `clash-cli configs` | 当前运行配置（端口/tun/dns 等） |
| `clash-cli rules [N]` | 规则列表（默认前 10） |

## 3. 常用任务

- **查当前选中节点**：`clash-cli proxy get <组>`（如 `PROXY`）
- **切换节点/策略**：`clash-cli proxy set <组> <节点>`（组内任意成员名，含 DIRECT）
  ```bash
  clash-cli proxy set PROXY DIRECT    # 直连
  clash-cli proxy set PROXY AUTO      # 切回自动测速组
  ```
- **节点测速**：`clash-cli test <节点名> [url] [timeout_ms]`；对组内全部节点测速 `clash-cli grouptest <组名> [url] [timeout_ms]`
- **DNS 查询**：`clash-cli dns query <域名> [type]`（走 mihomo 内部 DNS，返回 Answer 数组）
- **日志**：`clash-cli logs [秒数] [level]`（SSE，默认 3 秒）
- **规则命中分析**：mihomo 无 `rule match` 端点，看每连接命中规则用 `clash-cli connections`（最后一列显示匹配的规则名）

## 4. 影响边界（写操作）

- **写操作**：`proxy set`、`conn close <id|all>`、`reload`、PATCH `/configs` 会改变运行状态，执行前先确认目标名存在（`proxy get`）。
- `conn close all` 会断开全部连接（SSH/下载会被打断）。
- `reload` 重载配置可能导致短暂断线，配置改动应先推送到 `config-backup` 私库再 reload。
- 修改后的完整配置只推私有仓库 `mickeu/config-backup`（含节点密码），**绝不推公共仓库**。

## 5. 交付维护

- 脚本：`skills/clash-controller/scripts/clash-cli`，已 symlink 到 `/usr/local/bin/clash-cli`，可直接 `clash-cli ...` 调用。
- 修改脚本后必须 `python3 -m py_compile clash-cli` 校验语法，并用 `clash-cli status` 冒烟测试。
- 变更后同步推送 `mickeu/minis-skills`（含 SKILL.md、scripts、references）。

## 6. 本机环境补充

- **Hako external-controller 实测可用**（2026-10-03，mihomo 1.19.32）：`127.0.0.1:9090` 监听并响应全部 RESTful API，读+写均通过。技能库 `clash-config` 中「carried and inert」推断已推翻。
- **iSH 127.0.0.1 = iOS 本机 localhost**（用 Surge `127.0.0.1:6171` 对照验证），可访问 iOS 上任何监听 127.0.0.1 的服务。
- 环境变量：`CLASH_API`（默认 `http://127.0.0.1:9090`）、`CLASH_SECRET`、`CLASH_TIMEOUT`（默认 8）。
- Hako 的 `external-controller` 保持 `127.0.0.1` 绑定即可；**勿改 `0.0.0.0`**（`allow-lan: true` 且无 secret 时局域网内可被访问，有风险）。
- 关联技能：`clash-config`（配置字段/语法）、`surge-ios`（Surge 控制器，命令可对照）。

## 参考资料（来源）

- mihomo（MetaCubeX）GitHub：https://github.com/MetaCubeX/mihomo （实测版本 1.19.32）
- mihomo Wiki：https://wiki.metacubex.one/
- Clash 原始 RESTful API 文档：https://clash.gitbook.io/doc/restful-api
- Hako（Clash Apple 原生客户端）：App Store「Hako」
- 实测与创作日期：2026-10-03（读/写 API 全通：/version /configs /proxies /connections /rules /traffic SSE /memory SSE /dns/query，`PUT /proxies/:name` 切换节点返回 204）
- 校验：`clash-cli` 通过 `python3 -m py_compile`，核心命令实测通过（status/traffic/connections/rules/proxy get/set/test/dns）