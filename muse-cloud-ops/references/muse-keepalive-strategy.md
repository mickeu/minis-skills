# Muse 沙盒容器保活策略参考（muse-guardian）

> 提炼自第三方开源项目 `bytehola/muse-guardian`（https://github.com/bytehola/muse-guardian，linux.do/t/topic/2954987），2026-10-02 分析。该项目给 Muse.ai 沙盒部署「CF 探针 + Hermes 微信机器人 + 三层保活 + MuseAutoApprove 自动审批」。本文只提炼保活架构与可复用经验，供 Muse 云电脑/Muse 沙盒保活方案设计参考；完整部署手册见上游 SKILL.md。

## 核心背景

- 沙盒（Muse/hatch 虚拟机）**重建后系统目录全丢，只有 `$HOME`（`/home/hatch`）持久化**。
- 会丢：`/usr/local/bin/*`、systemd 服务、`sshd`/`cron` 系统组件、root crontab、`/tmp`。
- 不丢：`~/workspace/`、`~/.hermes/`、`~/.local/`、`/home/hatch/hooks/`。
- 因此保活核心 = **一切脚本与离线包放 `$HOME`，重建后自动恢复系统组件**。

## 三层保活架构（核心）

| 层 | 机制 | 周期 | 作用 | 恢复时效 |
|---|---|---|---|---|
| Layer 1 | `watchdog.sh`（沙盒内 cron 看门狗） | 每分钟 | 进程挂了就地拉起 | 1 分钟内 |
| Layer 2a | 平台 hook 探针 `keepalive-tripwire`（跑在沙盒外） | 每 10 秒 | 整机被重建、沙盒内 cron 全灭时的兜底 | 10 秒级发现，约 2 分钟恢复 |
| Layer 2b | 平台原生开机钩子 `home-init`（每次启动跑一次） | 启动时 | 开机即恢复 | 开机后约 100 秒 |

### Layer 1：watchdog.sh（沙盒内看门狗）

- cron 每分钟执行：`* * * * * $HOME/workspace/setup/watchdog.sh`
- 巡检三项：cf-probe 探针（systemd 服务 active）、Hermes 微信网关、sshd。
- **进程活着 ≠ 连接活着**：Hermes 微信网关进程在，但日志里 `poll error` 持续超过 5 分钟 → 判卡死，杀掉重启。
- 实现要点（实测经验）：
  - 单实例锁用**原子 mkdir**，不用 flock（避免 fd 被子进程继承导致锁死）；stale 锁通过 PID+`/proc/<pid>/cmdline` 校验回收。
  - `pgrep -f "[/]watchdog.sh"` 中括号技巧，避免匹配到检查进程自身。
  - 所有日志统一裁剪：任何文件超过 10MB 只保留末尾 10MB（`tail -c` + sed 丢半行）。
  - HOME 加固：若当前 HOME 找不到 setup 目录但 `/home/hatch` 下有，则 `export HOME=/home/hatch` 后继续。

### Layer 2a：keepalive-tripwire（平台 hook 探针）

- 跑在**沙盒外**（平台 hook runtime），沙盒重建也杀不死。每 10 秒执行一段轻量 bash。
- **检测与恢复拆分**：健康时调 `silent`（本轮零 token）；只有 `wake` 才启动完整 LLM worker 执行恢复。
- **退出码契约**（`health-check.sh` 只返回 0/1）：
  - `0` = 健康 → `silent`，清零计数，零 token。
  - `1` = 需要恢复（检查已得出确定性结论）→ **立即 `wake`，无防抖**。
  - 非 0/1 = 检查本身没跑起来（脚本缺失/exec 通道异常）→ 累计连续 3 次才 `wake`（防抖约 30 秒）。
- 连续失败计数存 `~/hooks/state/keepalive-tripwire.json`（$HOME 持久化，重建不丢）。
- 恢复 worker prompt：重跑 `health-check.sh` 确认 → `rc=1` 则后台执行 `restore-all.sh`（等完成，最多 15 分钟）→ 重跑验证 → 只在异常/恢复时给用户发简短通知，健康时完全静默。
- 周期 10 秒未经用户明确批准不得更改。

### Layer 2b：home-init（平台开机钩子）

- 平台每 60 秒轮询 `/home/hatch/hooks/definitions/` 下的钩子定义。
- 钩子脚本必须 `source "${HATCH_HOOK_RUNTIME:?}"` 并调用 `silent`/`wake`/`log`。
- **`/home/hatch/init.sh` 必须 `chmod 700` 可执行才会生效**——这是启用开关。
- 用 `/run`（tmpfs，重启清零）里的 `started` 标记实现「每次启动恰好跑一次」；`flock` 防并发。
- 每次启动只跑一次、**失败不重试**（`started` 先落盘），失败兜底交给 hook 探针。
- `init.sh` 内容 = 直接 exec `restore-all.sh`（复用恢复逻辑）。

## 配套组件

### 持久化布局

- 7 个脚本全部落盘 `~/workspace/setup/`：`watchdog.sh`、`health-check.sh`、`restore-all.sh`、`lib-pkgs.sh`、`restore-hermes.sh`、`backup-hermes.sh` + 安装脚本。
- **离线包缓存**：cron/openssh 依赖闭包（deb）+ cf-probe 二进制缓存到 `$HOME`，重建后无网也能装回系统组件（国内沙盒 GitHub 常不可达，离线缓存是必需项）。

### health-check.sh（健康检查，统一判据）

- 检查：cf-probe systemd 服务 active、Hermes 网关进程存活、sshd 进程存活、cron 进程存活且 crontab 里有看门狗。
- 区分「重建」还是「普通故障」：`/usr` 关键二进制都没了 → 重建。

### restore-all.sh（重建后一键恢复，幂等）

- 顺序：基础包（cron/openssh，优先离线缓存）→ Hermes → cf-probe → cron 看门狗 → sshd → 看门狗终检。
- 单实例锁（原子 mkdir + 超时 stale 回收）；等待 apt/dpkg 锁最多 10 分钟（重建后平台可能在做包 reconciling）。
- 离线 deb 安装：只装缺失包，dpkg 跑两遍解决 pre-depends 顺序；避免降级镜像自带版本。

### MuseAutoApprove（外联审批自动批准，HITL 自动化）

- 逆向复刻 muse.ai 客户端协议（Noise 加密 WebSocket RPC），纯 Node.js 无浏览器。
- 自动登录（无需读邮箱验证码）→ 会话永续（每 5 分钟 token touch，30 天滚动续期）→ 实时轮询审批 → 默认 `allow_always + destination_domain`（永久放行，落库 durable network_rule）。
- 自愈：会话过期自动重登、断线自动重连、网络抖动自动重试。
- **接入保活**：watchdog.sh 追加巡检段（进程不在且预检通过 → 拉起；日志 15 分钟没动 → 判卡死 TERM）；restore-all.sh 追加启动段（重建后自动拉起）。
- 维护模式：`data/muse-daemon.stop` 存在则保活跳过（不跟用户抢）。
- Node 必须装 `$HOME/.local`（重建保留），不能只装系统目录。

## 可复用的关键经验

1. **进程活着不等于连接活着**：轮询类守护要检查日志时间戳/错误持续时长判断卡死，不能只 `pgrep`。
2. **检测与恢复拆分**：高频轻量探针（shell、零 token）只做检测，恢复由低频 LLM worker 做，成本可降几个数量级（旧方案每分钟 LLM 巡检约 1,434 万 input/天）。
3. **退出码即契约**：用退出码区分「确定性故障（立即恢复）」和「不确定状态（防抖累计）」。
4. **恢复脚本必须幂等**，重复触发安全；用原子 mkdir 做锁（避免 flock 的 fd 继承问题）。
5. **离线兜底**：重建后网络不可靠，安装脚本/二进制必须本地缓存一份。
6. **平台能力分层**：沙盒内看门狗 → 平台 hook 探针 → 平台开机钩子，逐层兜底；hook/钩子只能由平台侧 Agent 创建。
7. **合规注意**：微信机器人/Hermes 存在封号风险（社区反馈），保活策略本身无风险；MuseAutoApprove 属平台 HITL 自动化，但改造平台协议需自担风险。技能库既有的合规红线仍适用（不部署反弹 Shell/公网穿透）。