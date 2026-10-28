# 双11 晚 8 点整点抢红包提醒（每日 19:53 弹窗）
# 由用户明确要求创建；只负责提醒，不自动操作浏览器、不绕过领取授权。
# 活动期：2026.10.12 - 2026.11.11，11.11 后可删除计划任务（卸载命令见 SKILL.md「定时开抢接入」）。
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show(
    "20:00 京东晚 8 点大红包场，还有 7 分钟。`n`n打开你的 AI 工具，说一句：开抢`n流程复用早 10 点已验证打法：T-7 分钟进场，踩点刷新，按页面横幅玩法执行。",
    "双11 晚8点抢红包提醒",
    [System.Windows.Forms.MessageBoxButtons]::OK,
    [System.Windows.Forms.MessageBoxIcon]::Information
) | Out-Null
