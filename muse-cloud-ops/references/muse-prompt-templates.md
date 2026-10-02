# Muse 实操指令模板（直接复制可用）

来源：X 推文 @SUOHA_AI（梭哈.AI）《如何合规榨干 Muse 2核8G 虚拟机的算力》，2026-09-27。指令经作者真机跑通，仅供参考，使用时按需修改路径/任务名/周期。

前置知识：持久化目录 `/home/hatch/pdata/`（重启不丢），根目录 `/` 重启清空。见 `muse-sandbox-facts.md`。

---

## 模板 1：初始化持久化工作区

复制发给 Muse：

```text
请在终端中执行以下环境初始化操作：
1. 检查物理算力与存储底座：运行 nproc、free -h 和 df -h，确认可用 CPU、内存与磁盘容量；
2. 搭建持久化自动化目录：在 /home/hatch 下创建持久化脚本工作区 /home/hatch/pdata/scripts 与数据存储目录 /home/hatch/pdata/data；
3. 检查 Python 运行环境：python3 --version 并确认环境状态。
请在终端中执行并逐项打印出真实输出。
```

预期回显：2 核 x86_64、内存约 7.7 GiB、根分区 7.5 GiB + /home/hatch 100 GiB 持久盘、Python 3.12.3。

## 模板 2：让 Muse 编写业务脚本（示例：交易流数据清洗）

复制发给 Muse：

```text
请在持久化目录 /home/hatch/pdata/scripts/ 下编写自动化批处理脚本 pipeline_worker.py：
1. 模拟生成 1000 条包含时间戳、标的代码（AAPL, NVDA, TSLA, MSFT, AMZN）与网络延迟的交易流数据；
2. 采用 Z-Score 算法进行离群点清洗，自动识别出延迟突刺与价格异动，筛选 Top 5 异动事件；
3. 将清洗后的全量数据持久化导出至 /home/hatch/pdata/data/analytics_report.csv，统计指标写入 summary.json。
编写完成后落盘并展示核心代码结构。
```

Muse 会以 root 权限直接写盘，无需手动传文件。

## 模板 3：执行脚本并验证落盘

复制发给 Muse：

```text
请在终端中执行刚刚编写的脚本：
python3 /home/hatch/pdata/scripts/pipeline_worker.py
并在终端中打印前 5 行 csv 数据以及 summary.json 的统计结果。
```

预期：1000 条数据 0.3 秒左右算完，csv 与 json 落盘。

## 模板 4：配置官方定时任务（Scheduled Task，核心）

复制发给 Muse：

```text
请为该脚本配置一个官方定时任务（Scheduled task）：
1. 任务名称：每日数据清洗流水线；
2. 执行周期：每天早晨 6:45（美东时间）自动运行 pipeline_worker.py；
3. 审计机制：每次运行输出写入 /home/hatch/pdata/data/logs/pipeline_YYYY-MM-DD.log，关键指标追加至 audit.log；
4. 告警策略：成功时保持后台静默，脚本异常或异动超过阈值时在会话中主动弹窗预警。
```

配置成功后 Muse 界面生成常驻卡片 `Scheduled task: 每日数据清洗流水线`，关掉浏览器也会按周期自动唤醒执行。

## 模板 5：生成交互式数据看板（Artifact）

复制发给 Muse：

```text
请基于刚才生成的 summary.json 与 analytics_report.csv，直接为我构建一个交互式数据分析与异动监控看板 Artifact，包含核心吞吐指标、Top 5 异动列表与标的筛选交互。
```

预期：右侧工作区渲染交互看板（核心指标平铺、异动进度条、标的筛选按钮）。

## 模板 6：一键健康自检（验收）

复制发给 Muse：

```text
请在终端中执行一键健康自检并向我汇报：
1. 验证持久化工作区：ls -ld /home/hatch/pdata/scripts /home/hatch/pdata/data
2. 验证业务脚本状态：ls -l /home/hatch/pdata/scripts/pipeline_worker.py
3. 验证数据产物与行数：wc -l /home/hatch/pdata/data/analytics_report.csv && cat /home/hatch/pdata/data/summary.json | grep total_records
4. 终端实跑测试：python3 /home/hatch/pdata/scripts/pipeline_worker.py && echo "HEALTH_CHECK_OK: EXIT_CODE=$?"
请逐项打印出终端真实回显。
```

### 判断成功的 4 个硬指标

1. **目录就绪**：`pdata/scripts` 与 `pdata/data` 存在，权限正常
2. **脚本就绪**：`pipeline_worker.py` 大小约 1.2KB ~ 1.5KB，非空
3. **数据就绪**：`analytics_report.csv` 正好 `1001` 行（1000 数据 + 1 表头），`summary.json` 含 `"total_records": 1000`
4. **运行就绪**：最后一行 `HEALTH_CHECK_OK: EXIT_CODE=0`，0.3 秒无报错退出

---

## 使用注意

- 所有指令都通过 Muse 会话对话下发，Muse 自动完成写盘/执行/配置，无需手动传文件
- 业务脚本、任务名称、周期、路径可按实际需求替换，保持结构不变即可
- 长周期任务一律用模板 4（Scheduled Task），不要本地挂机防休眠
- 严格遵守合规红线：不碰反弹 Shell / 公网穿透 / VPN（Sentinel 审查会封号）
- 本文档是第三方教程模板，实际派单时仍要核对 Muse 返回的真实输出，不盲信