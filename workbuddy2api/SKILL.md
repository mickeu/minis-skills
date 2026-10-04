# WorkBuddy2API 反代网关 · 破限提示词知识库

> 来源：https://github.com/linguo2625469/workbuddy2api-panel
> 破限 fork：https://github.com/mickeu/workbuddy2api-panel
> 创建 2026-10-05 · 破限 commit `5d08495` · 人格合并 commit `7d6fd72`
> 完整破限词文件：同目录 `jailbreak-prompt.md`（外部版，与内置 `internal/prompt/defaultprompt.md` 一致）

**核心定位**：把腾讯 CodeBuddy（copilot.tencent.com）账号变成 OpenAI 兼容 API 的多账号网关，自带 Web 面板、账号池轮转、熔断冷却、会话粘性、定时签到/保活。破限 fork 把网关默认提示词替换为「破限立场 + Minis 人格」，使所有会话自动带破限词。

## ⚠️ 合规声明

- 仅限自用账号（签到 / 保活 / 个人工具接入），**禁止批量注册小号、二次分发、付费售卖**
- 不要购买任何「收费版 / 卡密版」——都是他人篡改版本，会窃取账号凭证（auths/ 存明文 token）

## 1. 破限词机制

- `internal/prompt/defaultprompt.md` 通过 go:embed 进二进制，是网关自有 system 提示词
- `prompt.mode` 控制路由（`config.json` → `prompt` 段）：
  - `custom` = 网关提示词**替换**客户端 system/developer（破限最彻底，推荐）
  - `append` = 在客户端 system 后插入（客户端限制性 system 仍保留）
  - `passthrough` = 透传（**代码实际默认**，config.go:275；README 写"默认 custom"是文档错误）
- ⚠️ **破限词要生效必须显式设 `"mode":"custom"`**，否则客户端 system 原样透传

## 2. 破限词内容结构

当前破限词 = **破限立场**（不拒绝话题 / 不出免责声明 / 不道德说教 / 不自我设限）+ **Minis 人格**（语言 / 行动准则 / 回报风格 / 技术纪律 / 安全红线）+ **工程行为约束**（先看代码 / 最小改动 / 验证闭环 / 不臆造 API）。

## 3. 生效配置（二选一）

```json
"prompt": { "mode": "custom", "file": "" }
```

- **A 内置法**：`file` 留空 → 用 go:embed 内置破限词，需重新编译/构建镜像
- **B 外部文件法**（推荐，免编译）：`file` 指向外部 md，如 `"/app/prompt/jailbreak-prompt.md"`，Docker 挂载 `./prompt:/app/prompt`，改内容只替换文件重启容器

## 4. 部署

### Docker（推荐）
```bash
mkdir -p auths data prompt && cp config.example.json config.json
# config.json 设 api_key + prompt.mode=custom + prompt.file
docker run -d --name workbuddy2api -p 7863:7863 -e TZ=Asia/Shanghai \
  -v ./auths:/app/auths -v ./data:/app/data -v ./config.json:/app/config.json \
  -v ./prompt:/app/prompt ghcr.io/linguo2625469/workbuddy2api-panel:latest
```

### 源码编译（iSH 本机测试）
```bash
apk add --no-cache go
cd workbuddy2api-panel && go build -o wb2api ./cmd/server
./wb2api -config config.json
```

### 添加账号
- 面板「添加账号」OAuth 设备授权（推荐，浏览器授权链接 → 微信扫码登录 → 凭证落盘 auths/）
- 或 `./login.sh`

## 5. Minis 接入

- provider Base URL：`http://<网关地址>:7863/v1`（iSH 本机为 `http://127.0.0.1:7863/v1`）
- API Key：config.json 的 `api_key`
- `custom` 模式下**任何 OpenAI 兼容客户端、任何会话**每请求自动替换 system 为破限词，Minis 端无需额外配置

## 6. 维护注意

- 上游 `linguo2625469/workbuddy2api-panel` 更新后破限词会被覆盖，用 `git cherry-pick 5d08495`（破限）和 `7d6fd72`（人格合并）重放
- 更新破限词后需同步：本地 `defaultprompt.md` + `jailbreak-prompt.md` + 私库 `config-backup/WorkBuddy2API/` + 本技能

## 参考资料（来源）

- 原版增强分支：https://github.com/linguo2625469/workbuddy2api-panel （README 与源码，2026-10-05 调研）
- 破限 fork：https://github.com/mickeu/workbuddy2api-panel （commit 5d08495 / 7d6fd72）
- 官方：https://www.codebuddy.cn · 积分查询 https://www.codebuddy.cn/profile/usage
- 免费额度：每月 1 号自动发放 500 积分（腾讯云官方计费文档）