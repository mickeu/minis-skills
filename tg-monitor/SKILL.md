---
name: TG 监控
description: 运行白嫖监控脚本。把请求转发给主会话执行，不需要自己搭建或运行脚本。
---

用户说"运行监控脚本"时，用 minis-sessions-cli 把消息转发到主会话：

```bash
minis-sessions-cli send --session D42CB996-6930-4222-BF86-6512AF206D0B --source shortcut "运行TG监控"
```

然后回复用户：已转发给主会话，请稍等。