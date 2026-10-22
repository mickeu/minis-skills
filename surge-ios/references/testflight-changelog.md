# Surge iOS TestFlight 版本日志

收录 Surge 5 iOS TestFlight（@SurgeTestFlightFeed）各版本的官方更新说明，便于追溯能力变化与修复。

## 5.102.0 (3875)

**待测试重点**：

- **Peer Access**
  - 移除 `peer-access-passthrough`（因其副作用），行为恢复为上一版本。
  - 针对 Apple 屏幕共享（Apple Screen Sharing）的特殊逻辑已直接内置，无需配置即可使用。
- **规则集**
  - 移除了规则集（rule sets）与域名集（domain sets）的 100 万条（1,000,000）条目上限。
- **修复**
  - 修复 iCloud Drive 同步不再拉取其他设备变更的问题（本地更改仍会上传）。根因是旧版本遗留的锁文件缺少写权限，Surge 现在会自动修复该文件。

官方频道：@SurgeTestFlightFeed

### 与本机环境的关联（2026-10-22）

- 3874 曾默认开启 `peer-access-passthrough`（当 `allow-peer-access=true` 时），导致 Tailscale 入站流量绕过 Surge 引擎、面板统计失效（详见 pitfalls-and-cookbook.md）。当时在配置中手动加了 `peer-access-passthrough = false` 规避。
- 3875 直接**移除**该参数并恢复旧版行为，意味着此前手动加的 `false` 已属废弃参数残留，应删除。本机配置已清理并 reload（commit config-backup `e0fc29d`）。