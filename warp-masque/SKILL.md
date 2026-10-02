---
name: warp-masque
description: Cloudflare WARP MASQUE 代理协议逆向分析与 warp-go 实现。涵盖注册协议、MASQUE 传输模式（H3/H2）、协议竞速、后量子密钥交换、DNS 解析器架构、连接管理等。当用户提到"WARP"、"MASQUE"、"Cloudflare WARP"、"warp-svc"、"warp-go"、"逆向WARP"、"CF WARP协议"、"MASQUE代理"时触发。
source_url: ""
license: CC-BY-NC-4.0
last_sync: 2026-07-26
---

# WARP MASQUE 代理协议逆向分析

> 逆向对象：`warp-svc`，版本 `2026.3.846.0`，ELF 64-bit x86-64 PIE，未 strip（Rust 符号完整保留），73,761,888 字节
> 完整文档见 `references/warp-masque-reverse-engineering.md`

## 概述

本文档记录两件事：
1. 对 Cloudflare 官方 Linux 守护进程 `warp-svc` 的逆向分析结果
2. `warp-go` 的实现，以及它与官方行为的对照

## 核心内容

### 注册协议（两步流程）

**Step 1** — `POST /v0/reg`（WireGuard 隧道类型）
```json
{
  "key": "<base64(Curve25519 公钥, 32 字节)>",
  "key_type": "curve25519",
  "tunnel_type": "wireguard",
  "install_id": "", "fcm_token": "",
  "tos": "<RFC3339>",
  "model": "PC", "serial_number": "<16 位十六进制>",
  "os_version": "", "locale": "en_US", "warp_enabled": true
}
```

**Step 2** — `PATCH /v0/reg/{id}`（MASQUE 隧道类型）
```json
{
  "key": "<base64(PKIX DER 编码的 ECDSA P-256 公钥)>",
  "key_type": "secp256r1",
  "tunnel_type": "masque"
}
```
带 `Authorization: Bearer <step1 返回的 token>`。

### MASQUE 传输模式

三种模式：`h3_only` / `h2_only` / `h3_with_h2_fallback`
- 对应三个连接器：`SingleProtocolConnector<H3>` / `SingleProtocolConnector<H2>` / `ProtocolRacingConnector`
- 协议竞速：先跑一轮启用 PQ 的 H3/H2 竞速，失败后再跑一轮禁用 PQ 的
- H3（MASQUE）为 Primary，H2 为 Secondary

### 技术栈

| 组件 | 用途 |
|------|------|
| quiche / tokio_quiche | QUIC 传输 |
| hickory-dns | DNS 解析 |
| boring (BoringSSL) | MASQUE 路径 TLS |
| rustls + tokio-rustls | DoH 路径 TLS |
| h2 | DoH 的 HTTP/2 |
| http-capsule | RFC 9297 capsule |

### DNS 解析器

- 四层架构：MultiplexedDohProvider → DnsProxy → 连接池
- 消费级 DoH（4s 超时 / 0 重试）
- 企业级 DoT（端口 853）和 DoH（端口 443）
- 健康追踪：DohHealthTracker，健康比率阈值 0.8

## 参考文件

- `references/warp-masque-reverse-engineering.md` — 完整逆向分析文档（570 行）