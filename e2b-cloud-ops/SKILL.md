---
name: e2b-cloud-ops
description: 在 E2B（AI Agent 云沙箱平台）上执行云端任务，Minis 通过 E2B API 自动创建沙箱、运行 Python/shell 命令、上传下载文件、回收结果，实现免费云服务器全自动派单。E2B 免费层一次性送 $100 使用额度，按秒计费，无需公网隧道。当用户提到 E2B、云沙箱、免费云服务器、云端跑代码、云端派单、爬虫服务器、下载服务器、转码服务器时使用。
---

# E2B 云沙箱派单（e2b-cloud-ops）

把「免费云服务器」变成 Minis 的一只手：用户在 Minis 里说任务，Minis 调 E2B API 秒开云端沙箱执行（Python/shell/爬虫/下载/转码），结果直接收回来，用完全自动销毁。免费层 $100 一次性额度，按秒计费，不需要公网隧道、不需要 MCP 穿透。

## 一、注册与配置

1. 打开 https://e2b.dev → Sign in → 用邮箱或 GitHub 登录（用户自己的账号，Minis 不代注册）
2. Dashboard → 项目（默认 Personal Project，区域 US-WEST-1）
3. 创建 API Key：https://console.e2b.dev/?tab=keys → Create API Key → 复制 `e2b_...`（只显示一次）
4. 把 Key 保存到 Minis 环境变量 `E2B_API_KEY`（用户通过 [环境变量设置页](minis://settings/environments?create_key=E2B_API_KEY&create_value=) 粘贴保存）
5. 安装 SDK：`pip install e2b`（iSH Alpine 已验证可装，纯 Python）

## 二、免费额度规则（2026-10-05 官方定价核实）

- Hobby 免费层 = **$100 一次性 usage credit**，按秒计费，**不按天/周/月重置**，用完为止
- **时效性：官方文档（Billing、FAQ、服务条款）均未给这 $100 设定有效期**，属账户一次性赠金，无过期日；用完会 blocked，需添加支付方式继续（2026-10-05 查证）
- 计费单价：默认 2 vCPU 沙箱 $0.000028/秒 ≈ $0.1/小时；1 vCPU $0.000014/s、4 vCPU $0.000056/s
- $100 ≈ 992 小时连续运行（2 vCPU），日常派单几分钟一次可用数月
- 免费层限制：单会话最长 1 小时、最多 20 并发沙箱、默认 2 vCPU
- 不开沙箱不扣费；沙箱销毁后停止计费

## 三、派单工具（scripts/e2b-run.py）

```bash
# 执行 shell 命令
python3 /var/minis/skills/e2b-cloud-ops/scripts/e2b-run.py --cmd "pip install requests && python3 a.py"

# 直接执行 Python 代码（自动写入沙箱再运行）
python3 e2b-run.py --py "import requests; print(requests.get('https://httpbin.org/ip').json())"

# 上传本地文件后执行（可多次 --file）
python3 e2b-run.py --file /path/local.py --cmd "python3 local.py"

# 保持沙箱存活（打印 sandbox_id，供后续复用；用完手动 --kill）
python3 e2b-run.py --cmd "python3 server.py" --keep

# 销毁指定沙箱
python3 e2b-run.py --kill <sandbox_id>

# 列出运行中沙箱
python3 e2b-run.py --list
```

输出：沙箱 ID、标准输出、错误输出、退出码，任务完默认自动销毁。

## 四、常用任务模板

- **云端爬虫**：`--py "pip install requests beautifulsoup4; 抓取目标页并打印/保存结果"`，结果可写入文件再用 `sbx.files.download` 取回
- **下载文件**：`--cmd "curl -LO <url> && ls -la"`，需要结果文件用 SDK 下载
- **视频转码**：`--cmd "apt-get install -y ffmpeg && ffmpeg -i in.mp4 -vcodec h264 out.mp4"`（Debian 12 默认源可用）
- **批量 Python/数据分析**：上传脚本 + 数据文件，`--cmd "python3 script.py"`，取回输出
- **编译任务**：gcc/rust/go 均可 apt/curl 安装（Debian 12）

## 五、注意事项

- `E2B_API_KEY` 是敏感凭证：只存在于 Minis 环境变量，不写入脚本/记忆/对话；脚本从 `os.environ` 读取
- 长任务：沙箱单会话最长 1 小时，超时需要分片或自建服务保持；进程在沙箱内运行，退出 Minis 不影响云端执行，但结果需下次查询
- 结果回收：目前工具打印文本输出；文件结果可让任务把文件内容 base64 打印，或升级工具用 `sbx.files.download` 落盘到 /var/minis/workspace
- 与 Muse 的关系：E2B 是 Muse 路线验证失败（无公网入口 + VM 网关仅 Meta 内网可解析）后的替代方案，见 muse-cloud-ops 技能 1.7 节
- 隐私：沙箱是美国机房（Google Cloud IP），访问国内服务需自行评估；不要在沙箱里保存敏感凭据

## 参考资料（来源）

- E2B 官网：https://e2b.dev
- E2B 定价（免费额度/单价）：https://e2b.dev/pricing （2026-10-05 核实）
- E2B Billing & limits 官方文档（$100 one-time credits、无有效期）：https://docs.e2b.dev/billing
- E2B FAQ（用完额度行为）：https://docs.e2b.dev/faq/index
- API Key 文档：https://docs.e2b.dev/api-key （Key 在 console.e2b.dev/?tab=keys）
- E2B Python SDK：https://e2b.dev/docs （pip install e2b，同步 API）
- 创建/实测日期：2026-10-05；派单工具实测通过（Debian 12 / Python 3.11 / pip 安装 requests / 网络出口正常）