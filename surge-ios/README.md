# surge-ios（Minis 技能）

在 Minis 中通过 Surge iOS 的 External Controller / HTTP API 检查和控制本机 Surge。

## 安装

1. 解压到 `/var/minis/skills/surge-ios/`。
2. `chmod +x /var/minis/skills/surge-ios/scripts/*.py && ln -sf /var/minis/skills/surge-ios/scripts/surge_cli.py /usr/local/bin/surge-cli`
3. Surge iOS 中开启 External Controller（默认 `127.0.0.1:6170`），在 Minis 设置 → 环境变量添加 `SURGE_CLI_PASSWORD`。
4. 可选：开启 HTTP API（`127.0.0.1:6171`）并添加 `SURGE_HTTP_API_KEY`，用于 metrics 和未配置节点测试。

依赖：系统 `python3`，无第三方包。

## 说明

- `references/command-reference.md` 摘自 Surge Mac 应用内置的官方 CLI 参考（版本见 `references/UPSTREAM_VERSION`），§1.1 改为 Minis 说明；版权归 Surge 官方。
- `surge-cli --check` 会把指定文件上传到 Surge 官方在线校验服务。
