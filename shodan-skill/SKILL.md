---
name: shodan-skill
description: Shodan 搜索引擎高级交互技能，支持搜索、扫描、网络告警和 DNS 查询。当用户提到"Shodan"、"网络测绘"、"端口扫描"、"资产搜索"、"漏洞搜索"、"搜索引擎查设备"、"查IP"、"查域名"、"网络侦查"时触发。
metadata: {"openclaw":{"emoji":"🔍","requires":{"bins":["python3","pip"]}}}
source_url: https://github.com/OpenMinis/MinisSkills/pull/75
source_repo: https://github.com/OpenMinis/MinisSkills
license: MIT
last_sync: 2026-07-26
---

# Shodan 技能

基于官方 Python 库的 Shodan API 综合封装，支持网络测绘、漏洞扫描和资产监控。

## 安装

### 1. 安装依赖

```bash
pip install shodan
```

### 2. 配置 API 密钥

```bash
shodan init <你的_API_KEY>
```

技能会自动读取 `SHODAN_API_KEY` 环境变量或 `~/.config/shodan/api_key` 配置文件。

## 使用方式

所有命令统一通过 `{baseDir}/scripts/shodan_skill.py` 调用，输出 JSON 格式，便于程序解析。

### 1. 高级搜索

支持搜索过滤器（`vuln:`、`port:` 等）和 Facets 统计。

```bash
python3 {baseDir}/scripts/shodan_skill.py search "<查询语句>" --limit <条数> --page <页码> --facets <统计维度>
```

- `--facets`：逗号分隔的统计维度，例如 `country:5,org:5`（前5个国家/组织）

### 2. 统计计数（不消耗查询额度）

获取匹配结果总数，不消耗查询额度。

```bash
python3 {baseDir}/scripts/shodan_skill.py count "<查询语句>" --facets <统计维度>
```

### 3. 主机详情

查询指定 IP 的详细信息。

```bash
python3 {baseDir}/scripts/shodan_skill.py host <IP地址> [--history] [--minify]
```

### 4. 按需扫描（消耗扫描额度）

请求 Shodan 扫描指定网络。

```bash
python3 {baseDir}/scripts/shodan_skill.py scan <IP列表>
```

`<IP列表>`：单个 IP、CIDR 网段或逗号分隔的 IP 列表。

### 5. 网络告警

监控网络资产，发现新暴露时通知。

| 操作 | 命令 |
|------|------|
| 列出所有告警 | `python3 {baseDir}/scripts/shodan_skill.py alert_list` |
| 创建告警 | `python3 {baseDir}/scripts/shodan_skill.py alert_create <名称> <IP范围>` |
| 查看告警详情 | `python3 {baseDir}/scripts/shodan_skill.py alert_info <告警ID>` |

### 6. DNS 与域名

| 操作 | 命令 |
|------|------|
| 域名信息 | `python3 {baseDir}/scripts/shodan_skill.py dns_domain <域名>` |
| 域名解析 | `python3 {baseDir}/scripts/shodan_skill.py dns_resolve <主机名列表>` |

### 7. 账户与工具

| 操作 | 命令 |
|------|------|
| 账户信息 | `python3 {baseDir}/scripts/shodan_skill.py profile` |
| 本机 IP | `python3 {baseDir}/scripts/shodan_skill.py myip` |
| 扫描端口列表 | `python3 {baseDir}/scripts/shodan_skill.py ports` |
| 扫描协议列表 | `python3 {baseDir}/scripts/shodan_skill.py protocols` |

### 8. 查询目录（已保存的查询）

| 操作 | 命令 |
|------|------|
| 搜索已保存的查询 | `python3 {baseDir}/scripts/shodan_skill.py query_search "<关键词>"` |
| 热门标签 | `python3 {baseDir}/scripts/shodan_skill.py query_tags` |

### 9. 通知器

| 操作 | 命令 |
|------|------|
| 列出通知器 | `python3 {baseDir}/scripts/shodan_skill.py notifier_list` |

### 10. 漏洞搜索

在 Shodan Exploits 数据库中搜索 CVE 和 PoC。

```bash
python3 {baseDir}/scripts/shodan_skill.py exploit_search "<查询语句>"
```

### 11. 实时流

接入 Shodan Firehose 获取实时网络数据流，可使用 `--ports` 或 `--alert` 过滤。

```bash
python3 {baseDir}/scripts/shodan_skill.py stream --limit 10
```

### 12. 趋势分析

使用 count + facets 分析全球资产分布趋势。

```bash
python3 {baseDir}/scripts/shodan_skill.py count "apache" --facets "country"
```

### 13. 速查手册

| 操作 | 命令 |
|------|------|
| 搜索过滤器列表 | `python3 {baseDir}/scripts/shodan_skill.py filters` |
| 数据字典（Banner 字段） | `python3 {baseDir}/scripts/shodan_skill.py datapedia` |

## 使用示例（自然语言触发）

安装完成后，你可以直接对我说：

- "用 Shodan 搜索日本有漏洞的 IIS 服务器"
- "统计全球运行 OpenSSH 7.4 的设备数量"
- "查询 IP 1.2.3.4 的详细信息"
- "监控 192.168.1.0/24 网段，新端口开放时通知我"
- "搜索 CVE-2019-0708 的漏洞利用代码"
- "实时监听端口 23 的数据流"

## 来源与更新

- 来源仓库：https://github.com/OpenMinis/MinisSkills
- 来源链接：https://github.com/OpenMinis/MinisSkills/pull/75
- 许可证：MIT
- 最后同步：2026-07-26
- 检查更新命令：
  ```bash
  curl -sL "https://api.github.com/repos/OpenMinis/MinisSkills/pulls/75" | grep -o '"updated_at": "[^"]*"' | head -1
  ```
