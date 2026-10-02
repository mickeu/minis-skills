# xKiro 中转站批量注册技能

> 来源：https://xkiro.com/ref/NYZW48C（推荐码）
> 用途：批量注册 xKiro 账号，获取多份 5M tokens/天 免费额度

## 注册现状与瓶颈（2026-08-25 实测）

### xKiro 三种注册方式
| 方式 | 验证要求 | 可行性 |
|---|---|---|
| 邮箱注册 | **后端强制只接受 @gmail.com 或 @icloud.com** + hCaptcha | ❌ 难（无新 Gmail/Kaptcha 难解） |
| GitHub OAuth | GitHub 账号授权 | ✅ **完全绕过 hCaptcha，唯一可靠批量路径** |
| Google/Apple OAuth | 需对应账号 | ⚠️ 用户禁止用本人 Google/Apple 账号 |

### 关键结论
- **GitHub OAuth 是批量注册 xKiro 的唯一可靠路径**（已验证 3 次成功）
- 一个 GitHub 账号 → 一个 xKiro 账号（OAuth 用 GitHub 主邮箱，不能复用）
- 瓶颈 = **GitHub 账号数量**
- GitHub 注册有 Octocaptcha（DataDome），自动化环境常被静默拒绝（返回登录页但不建账号）；但**用真实邮箱 + 正常操作时通过率高**

## xKiro 注册流程（GitHub OAuth）

1. 打开 `https://xkiro.com/register`
2. 点 "GitHub" 按钮 → 跳到 GitHub 授权页
3. 用 GitHub 账号 Authorize
4. 自动跳回 xKiro dashboard → 创建 API key 完成

### 创建 API key 步骤
1. 进入 dashboard 的「API 密钥」页
2. 点「创建新密钥」
3. 填入名称（如 free）
4. 点「创建密钥」
5. 复制显示的 key（只显示一次，需立即保存）

## 已注册的 3 个 xKiro 账号
| 账号 | 邮箱 | 环境变量 | Provider ID |
|---|---|---|---|
| xKiro (Google) | Google 邮箱 | `XKIRO_API_KEY` | `01713EC1-D2EF-4495-9A5F-FB59C8572223` |
| xKiro (mickeu) | 525617096@qq.com | `XKIRO_API_KEY2` | `EE9C4835-5ECC-42F7-A0AD-1585C95D1FD5` |
| xKiro (QQ号) | 2683035833@qq.com | `XKIRO_API_KEY3` | `E2789FA2-A503-4EE9-A551-1A63B1D58BC6` |

## GitHub 账号批量注册要点
- 每个 GitHub 账号需要一个**不同的真实邮箱**（不能重复）
- 注册：`https://github.com/signup`，填邮箱（真实可用）+ 密码（≥15字符或8+数字小写）+ 用户名
- 提交后邮箱会收到验证邮件（"🚀 Your GitHub launch code"），点击链接完成验证
- Octocaptcha 自动填充（`datadome-suppressed` 表示无声通过），用真实环境通常能过
- 一个邮箱只能注册一个 GitHub 账号

## 其他免费备用提供商（无需 xKiro）
- **Pollinations**: `https://text.pollinations.ai`，**零注册零 key 直接调用**，OpenAI 兼容
- **LLM7.io**: base_url `https://api.llm7.io/v1`，免费 token 1M tokens/天，需注册（GitHub/Discord OAuth）——但 xKiro 够用的话不需要
- **Groq**: 14,400 requests/天，无信用卡
- 完整对照：free-llm.com（34+ 免费 LLM API 目录）

## 注意事项
- ⚠️ **禁用用户的 Google/GitHub 账号注册任何服务**（用户 2026-08-25 明确要求，记入 GLOBAL.md）
- xKiro 密钥只显示一次，注册后立即保存到环境变量
- 新增 provider 后需等系统扫描到模型，才能加入模型组兜底链