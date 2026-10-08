---
name: masque-server
description: 高性能 MASQUE 代理服务器，用 Rust 编写，支持 HTTP/3 (QUIC) 承载 TCP/UDP/IP 流量，支持自包含操作捆绑包部署。
---
# masque-server

> 高性能 MASQUE 代理服务器，用 Rust 编写，支持 HTTP/3 (QUIC) 承载 TCP/UDP/IP 流量。

## 来源
- **GitHub**: [Vincent-bin/masque-server](https://github.com/Vincent-bin/masque-server)
- **记录时间**: 2026-10-01
- **当前版本**: v0.13.0（2026-09-02 发布）

> **v0.13.0 更新**（2026-09-02）：新增 guarded bootstrap 与 macOS probe releases；提供自包含操作捆绑包（self-contained operations bundle）。

## 核心能力

- **协议支持**：
  - CONNECT（TCP 流）
  - CONNECT-UDP（RFC 9298，HTTP Datagrams）
  - CONNECT-IP（RFC 9484，需 Linux TUN 集成）
- **传输层**：
  - HTTP/3 over UDP（默认）
  - HTTP/2 Extended CONNECT + Cloudflare/usque CONNECT-IP 方言作为 QUIC 阻断时的回退
- **认证**：
  - HTTP Basic（Argon2id 密码哈希）
  - TLS 客户端证书（公钥白名单）
  - 两种模式互斥，但可开多个监听器分别服务
- **策略与控制**：
  - CIDR allow/deny 策略（TCP/UDP 目标）
  - 每源 IP 连接数限制 + Basic 认证并发限制
  - 自适应 QUIC Retry
- **性能优化**（仅 Linux）：
  - SO_REUSEPORT 多核分片
  - UDP GRO/GSO，recvmmsg/sendmmsg
  - TUN 卸载支持
- **运维**：
  - SIGHUP 热重载 TLS 证书链（不中断已有连接）
  - `add-listener` 子命令动态添加监听器（交互式/脚本化）
  - `doctor` 子命令只读检查 CONNECT-IP 前置条件（TUN、转发、路由、防火墙、NAT）
  - Prometheus 指标 + Grafana 仪表板（打包静态资产）
  - JSON 结构化日志 + systemd 就绪/看门狗
  - 原子配置校验，失败不生效
- **部署**：
  - Linux x86_64 静态发布包 + systemd installer
  - 一键安装脚本 `install-latest.sh`（支持升级，自动备份回滚）
  - 安装时可选 Basic / client_cert / 双模式

## 快速开始（摘自 README）

```bash
# 构建
cargo build --release --bin masque-server

# 生成 Argon2id 密码哈希
printf '%s' 'your-password' | target/release/masque-server hash-password

# 配置 TOML（参考 deploy/config/masque.toml），然后启动
target/release/masque-server --config ./masque.toml
```

### 添加新监听器
```bash
masque-server --config /etc/masque/masque.toml add-listener
```
可指定 `--transport http2|http3`、地址、认证模式等，脚本友好。

### CONNECT-IP 前置检查
```bash
sudo masque-server --config /etc/masque/masque.toml doctor
```
只读，不改系统状态。

### 一键 Linux 安装
```bash
curl -fsSL https://raw.githubusercontent.com/Vincent-bin/masque-server/main/install-latest.sh | sudo sh
```
安装/升级均可用，不覆盖已有配置。

## 注意事项

- **生产目标**：仅 Linux（CONNECT-IP、多分片、GSO/GRO、TUN 依赖 Linux 特性）。
- macOS 仅用于便携式 HTTP/2/HTTP/3 测试，不能跑 CONNECT-IP。
- 配置变更前用 `check-config` 校验，避免启动失败。
- 热重载 TLS 只换证书密钥，不换监听端口或认证模式。
- 认证模式 fail-closed：Basic 模式没有用户名/哈希会拒绝启动。

## 相关链接

- 仓库：[Vincent-bin/masque-server](https://github.com/Vincent-bin/masque-server)
- 文档目录：`docs/`（仓库内）
- 发布包：Releases 页面下载 `masque-v*-linux-x86_64.tar.gz`