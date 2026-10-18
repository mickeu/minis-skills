## 小浣熊多账号模块维护备忘（2026-10-18）

**模块**：`mickeu/surge/RaccoonOpenAI-Multi.sgmodule` + `Scripts/raccoon-openai-multi.js`（多账号 OpenAI 反代 + 每日批量签到）

**签到身份头（两种方案，可切换）**：
- **手机 App 端（当前使用）**：`randomCheckinHeaders()` 返回 `X-Client-Platform: app-android/app-ios`（随机）、`X-Client-Version: v1.0.3`、随机设备 ID、手机 UA。贴近真实手机使用，防风控更好。
- **桌面端（原版 LinkPass888 备选）**：`desktopHeaders()` = `X-Client-Platform: desktop-windows`、`X-Client-Version: v1.0.0`。若手机端被风控不行，改回 `randomCheckinHeaders()` 的平台/版本/UA 为桌面端即可。

**切换方法**：改 `Scripts/raccoon-openai-multi.js` 里 `randomCheckinHeaders()` 的 `X-Client-Platform` / `X-Client-Version` / `User-Agent`，推送 mickeu/surge 后 `surge-cli external-resource update <key>`（key 用 `surge-cli external-resource list` 搜 raccoon-openai-multi 获取）。

**原版模块（桌面端身份）**：`LinkPass888/Surge/main/sgmodule/小浣熊OpenAI反代.sgmodule`，脚本 `LinkPass888/Surge/main/js/raccoon-openai.js`，签到端点 `/api/web/office/v3/setting_info`。

**关键调研结论（Agent2API 逆向 + APK 确认）**：
- 小浣熊 API **无设备 ID 字段**，客户端身份只靠 `X-Client-Platform` + `X-Client-Version` 两个头。
- 桌面/手机端认同一把 Bearer token（JWT 无平台字段）。
- 手机端首登奖励：`POST /api/web/mobile/v1/login/points/grant`（app-android 头，一次性 +3000，与桌面端互不共享额度）。
- 每日积分发放：`GET /api/web/office/v3/setting_info` 触发（按天幂等）；`GET /api/web/points/v1/bills` 核对入账；`GET /api/web/points/v1/balance` 查余额。
- 签到时序：串行 + 账号间随机 1-3s 延时防风控。

**实测（2026-10-18）**：手机端身份头签到 6 账号全部正常（err 全 None），账号3~6 首次各 +6300，账号1/2 幂等无新增。

**参考资料**：
- https://github.com/weiang12345/agent2api （raccoon 适配器）
- https://github.com/LinkPass888/Surge （原版模块）