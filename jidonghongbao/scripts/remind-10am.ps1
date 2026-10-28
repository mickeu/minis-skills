# 双11 整点抢红包提醒（每日 09:53 弹窗）
# 由用户明确要求创建；只负责提醒，不自动操作浏览器、不绕过领取授权。
# 活动期：2026.10.12 - 2026.11.11，11.11 后可删除计划任务（卸载命令见 SKILL.md「定时开抢接入」）。
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show(
    "10:00 京东整点加码活动，还有 7 分钟。`n`n打开你的 AI 工具，说一句：开抢`n流程会自动执行：先扫日常大额券，踩点刷新等整点弹层。",
    "双11 抢红包提醒",
    [System.Windows.Forms.MessageBoxButtons]::OK,
    [System.Windows.Forms.MessageBoxIcon]::Information
) | Out-Null
