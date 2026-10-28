---
name: decrypt-stream
description: App 脱壳 IPA 下载源 — 用户问「在哪下载某 App / 哪个站可以下 App」时，去 decrypt.stream 搜索并下载脱壳 IPA（iOS/tvOS/visionOS）。支持按 App 名称、Bundle ID、App Store 链接搜索，提供历史版本与二进制直链。触发词：下载App、在哪下App、IPA下载、脱壳IPA、decrypt.stream、解密版App。
---

# decrypt.stream — App 脱壳 IPA 下载源

用户询问「哪里可以下载某个 App / 给我下个 IPA」时，首选本技能去 **decrypt.stream** 搜索并下载脱壳（去 FairPlay DRM）IPA。覆盖 iOS / tvOS / visionOS，提供「最近解密」「Top 免费」「历史版本」「Binaries only」等能力。

## 站点要点

- 主页：`https://decrypt.stream/`
- 搜索支持：**App 名称 / Bundle ID / App Store 链接**，结果使用 **US 区**（`region=us`）
- 下载产物为**未签名 IPA**（需用 Feather / 轻松签 / LCSign 等自签后安装；也可用本机 `ios-dev` 技能 `resign_keep_bundleid.py` 重签）
- 无需登录即可搜索与下载（Open access）
- 文件通常较大（几十 ~ 几百 MB），下载注意磁盘空间

## 使用流程

### 1. 搜索定位 App（走页面交互，无 GET 搜索 URL）

搜索是页内 JS 表单提交，URL 不变，**必须用浏览器交互**：

1. `navigate https://decrypt.stream/`
2. 在 `#q` 输入框输入 App 名称 / Bundle ID / App Store 链接（`type` action）
3. 点击 `#searchBtn` 搜索按钮
4. 结果卡片直接渲染在页内，从卡片读取：App 名、开发商、版本号、大小、**Bundle ID**（卡片 `id` 属性形如 `card-ph.telegra.Telegraph`）

### 2. 解析 Bundle ID

每张 App 卡的 DOM id 就是 bundle ID（如 `#card-ph.telegra.Telegraph`），下载链接也直接暴露：

```html
Download        → /api/v1/download/ph.telegra.Telegraph?region=us
Binaries only   → /api/v1/download/ph.telegra.Telegraph/binaries?region=us
App details     → /app/ph.telegra.Telegraph?region=us&platform=ios
```

### 3. 直链下载 IPA（curl 即可，无需登录）

```bash
# 完整 IPA（含 icon/资源/二进制，去 DRM）
curl -L -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15" \
  "https://decrypt.stream/api/v1/download/<bundle_id>?region=us" -o "<App名>_<版本>_decrypted.ipa"

# 只要二进制（无 App 图标/元数据，体积更小，适合逆向）
curl -L -A "Mozilla/5.0" \
  "https://decrypt.stream/api/v1/download/<bundle_id>/binaries?region=us" -o "<App名>_binaries.ipa"
```

响应为 `application/octet-stream`，HTTP 200，`Content-Disposition` 带真实 IPA 文件名。实测 `ph.telegra.Telegraph` 返回 ~105MB。

### 4. 后续处理

- **逆向**：脱壳包直接可用于提取二进制/词库/资源（参考 `iflytek-analysis` 等逆向技能）。
- **安装**：未签名 IPA 需自签。本机用 `ios-dev` 技能重签安装：`resign_keep_bundleid.py <in.ipa> --install`（保持原包名 + 描述文件 entitlements）。

## 注意事项

- 搜索**必须**走浏览器交互（`#q` + `#searchBtn`），不要臆造 GET 搜索 URL（`/search?q=` 会 404）。
- Bundle ID 大小写敏感，填错返回 404；从页面卡片 DOM id 取最稳。
- 默认 `region=us`；如需其他区可尝试改 `region=` 参数。
- 大文件下载建议后台执行并校验 SHA256。
- 下载的 IPA 版权归原开发商，脱壳 IPA 仅用于个人研究/侧载，请遵守当地法规与开发者条款。

## 参考资料（来源）

- 站点：https://decrypt.stream/ （iOS/tvOS/visionOS 脱壳 IPA 归档，Open access）
- 来源类型：用户提供，2026-10-28 收藏。
- 实测验证（2026-10-28）：
  - 搜索表单 `#q`/`#searchBtn`，页内 JS 提交，URL 不变
  - 直链下载 `GET /api/v1/download/<bundle_id>?region=us` 无需登录，HTTP 200
  - 示例：`ph.telegra.Telegraph` 返回 `Telegram（额外样本）_13.1.1_ios_decrypted.ipa`（105,790,791 字节）
  - `/search?q=` 与错误 bundle ID 均返回 404