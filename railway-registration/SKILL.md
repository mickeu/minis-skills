---
name: Railway 注册与 API 令牌
description: Railway（railway.com）云平台的注册、登录与 API 令牌获取完整流程。覆盖：邮箱注册（必须真实邮箱，一次性/临时邮箱域名会被静默拦截）、无密码登录机制（仅邮箱验证码/GitHub/Google/SSO）、获取 API Token 的网页路径、免费计划（无需信用卡）、四种部署方式（GitHub/CLI/Docker/模板）、GraphQL API 调用示例。当用户提到 Railway 注册、Railway token、Railway API、Railway 免费计划、railway 登录时使用。
---

# Railway 注册与 API 令牌

## 关键结论（2026-10-20 实测）

- **域名**：Railway 使用 `railway.com`（不是 railway.app）
- **注册无需信用卡**：官方定价页明确 Free 计划 **"No credit card required"**
- **⚠️ 临时邮箱不可用**：Railway **静默拦截一次性/临时邮箱域名**（提交后显示 "Check your email" 但永远收不到验证邮件）。实测被拦截的域名：`maxxspace.com`(mail.tm)、`juicehour.com`(temp-mail.org)、`tempmailgrab.com`、`jbsze.net`(10minutemail)。**必须使用真实邮箱**。
- **无密码登录**：Railway **没有账号密码**（官方社区明确 "Railway does not have account passwords"）。登录方式仅三种：邮箱验证码链接、GitHub OAuth、Google OAuth、SSO。
- **API Token 有效**：从 `railway.com/account/tokens` 生成，用于 Railway GraphQL API 与 CLI。

## 一、注册流程（真实邮箱）

1. 打开 **https://railway.com/login**
2. 点击 **"Log in using email"**（位于 GitHub 按钮下方）
3. 在邮箱输入框填入真实邮箱（如 QQ 邮箱）
4. 等待 **Cloudflare Turnstile** 人机验证完成——按钮会先禁用，需等几秒（可能 6~13 秒）变可用后才可点击
5. 点击 **"Continue with Email"**（若按钮仍禁用，说明 Turnstile 未通过，等待或点击验证框"请验证您是真人"）
6. 邮箱收到 Railway 的 **"Login code"** 邮件（验证码 6 位数字，20 分钟有效，**邮件内无链接**）
7. 页面会**跳转/弹出验证码输入窗口**，输入收到的 6 位数字
8. 登录成功，进入 Railway 控制台

### 邮箱验证码要点
- 邮件主题类似 "Login code"，发件人 Railway
- 验证码有效期 20 分钟，邮件里只有纯文本验证码 + 安全警告，**没有点击登录链接**
- 页面提交邮箱后会显示 "Check your email for the verification code"，随后跳转到验证码输入页

## 二、登录机制（无密码）

Railway 不支持邮箱密码登录，只能：

| 方式 | 说明 |
|---|---|
| 邮箱验证码 | 每次登录收邮件取 6 位码 |
| GitHub OAuth | 一键登录（需绑定 GitHub）|
| Google OAuth | 一键登录（需绑定 Google）|
| SSO | 企业/团队单点登录 |

可在 **Account Settings → Connections** 绑定 GitHub/Google，之后一键登录，免去每次收验证码。

## 三、获取 API Token

- **网页路径**：**https://railway.com/account/tokens**
- 步骤：登录 Railway → 右上角头像 → **Account Settings → Tokens** → **Generate Token**
- 字段：
  - **Name**：令牌命名（如 `minis`）
  - **Workspace**：选 **`My Projects`**（可访问项目；`No workspace` 只有账号级权限）
- 点击 **Create Token** 后令牌只显示一次，**需立即复制**
- Token 格式：`UUID`（如 `7d87f37a-...`）或 `rail_...` 开头
- **用途**：调用 Railway GraphQL API、Railway CLI 登录
- **安全**：令牌等同账号钥匙，用后可在 Tokens 页面删除

## 四、免费计划（无需信用卡）

| 项目 | 免费计划 (Free) |
|---|---|
| 价格 | $0/月 |
| 信用卡 | **不需要** |
| 试用 | 30 天试用含 **$5 credits** |
| 之后 | 每月约 **$1 免费额度** |
| 资源上限 | 1 vCPU / 0.5GB RAM 每服务，0.5GB 卷存储 |
| 适用 | 轻量、间歇使用的个人项目（机器人、静态站、小 API、定时任务、开发用数据库）|

计费按秒：内存 $0.00000386/GB·s，CPU $0.00000772/vCPU·s，服务停止不收费。

## 五、部署方式

| 方式 | 需要 GitHub？ | 说明 |
|---|---|---|
| GitHub 仓库 | ✅ 必须 | 从仓库部署 + 自动部署（官方：需关联 GitHub 账号）|
| Railway CLI | ❌ 不需要 | `railway init` + `railway up` 本地推代码 |
| Docker 镜像 | ❌ 不需要 | 填镜像名直接部署（Docker Hub/GHCR 等）|
| 模板 | ❌ 不需要 | 650+ 现成模板一键部署 |

## 六、GraphQL API 调用

- **端点**：`https://backboard.railway.app/graphql/v2`
- **认证头**：`Authorization: Bearer <token>`
- Token 从环境变量 `$RAILWAY_TOKEN` 读取（不要硬编码到脚本/仓库）

### 常用查询
```bash
TOKEN="$RAILWAY_TOKEN"
# 项目列表
curl -s -X POST "https://backboard.railway.app/graphql/v2" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"query":"query { projects { edges { node { id name } } } }"}'
```

### 常用 mutation（从 introspection 获取的字段名）
- `projectCreate`：创建项目
- `serviceCreate`：创建服务
- `variableUpsert`：添加/更新环境变量
- `variableDelete`：删除变量
- `serviceInstanceDeploy` / `serviceInstanceDeployV2`：部署

### 脚本
- `scripts/railway_api.sh`：封装 GraphQL 查询/mutation 的辅助脚本
- 用法：`RAILWAY_TOKEN=... ./railway_api.sh 'query { projects { edges { node { id name } } } }'`

## 七、自动化交互注意事项（浏览器操作踩坑）

- Railway 页面有 **Cloudflare Turnstile** 人机验证，按钮会先禁用。用 `execute_js` 直接 `.click()` 可能不触发 React 提交；**必须用原生 `type` 输入 + 等待按钮启用后真实点击**（`browser_use` 的 click coordinate）。
- Turnstile 组件可能渲染在浏览器层（非页面 DOM），`execute_js` 找不到 iframe，自动化绕过困难。
- 提交邮箱后页面跳转到验证码输入页，验证码输入框在跳转后的页面（不是原地）。
- 若用 browser_use 登录遇到 Turnstile 卡死，**改用 API Token 方案**（用户从网页生成 token，用 GraphQL API 操作），不要死磕网页登录。

## 参考资料（来源）

- Railway 官网：https://railway.com
- Railway 定价页（免费计划无信用卡）：https://railway.com/pricing
- Railway 官方文档：https://docs.railway.com
- Quick Start（三种部署方式）：https://docs.railway.com/quick-start
- Railway 社区登录说明（无密码）：https://station.railway.com
- 本技能创建日期：2026-10-20
- 实测环境：Minis (iSH) + browser_use + Railway GraphQL API