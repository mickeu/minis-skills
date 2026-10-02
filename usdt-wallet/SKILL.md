---
name: usdt-wallet
description: Monika 的 USDT 钱包管理 skill。当用户提到"USDT"、"钱包"、"余额"、"转账"、"wallet"、"充值"、"比特币"、"eth地址"、"gas"、"交易记录"、"打钱"时触发。管理钱包信息、查询余额、生成地址、USDT 转账、Gas 估算、交易记录查询。
source_url: https://github.com/OpenMinis/MinisSkills/pull/75
source_repo: https://github.com/OpenMinis/MinisSkills
license: MIT
last_sync: 2026-07-26
---

# USDT 钱包管理

## 钱包信息

钱包信息存储在 `wallet.json`，包含助记词、私钥、以太坊地址、比特币地址。

| 字段 | 值 |
|------|-----|
| 以太坊地址 | `0xe823...Be0a` |
| 比特币地址 | `1HXAU...KDE` |
| 网络 | Ethereum Mainnet (Chain ID: 1) |
| USDT 合约 | `0xdAC17F958D2ee523a2206206994597C13D831ec7` |

交易记录存储在 `transactions/recent_transactions.json`（最近 50 条）。

## 操作速查

| 操作 | 命令 |
|------|------|
| 查看钱包 | 读取 `wallet.json` |
| 查余额 (USDT + ETH) | `python3 scripts/check_usdt_balance.py` |
| 查余额 (ETH + BTC) | `python3 scripts/check_balance.py --wallet` |
| 查全部 (USDT + ETH + BTC) | `python3 scripts/check_usdt_balance.py --all` |
| 查任意地址 USDT | `python3 scripts/check_usdt_balance.py <地址>` |
| 转账 USDT | `python3 scripts/transfer_usdt.py <接收地址> <金额>` |
| Gas 市场报告 | `python3 scripts/gas_estimator.py` |
| 估算转账费用 | `python3 scripts/gas_estimator.py --transfer` |
| 交易记录 (本地) | `python3 scripts/tx_history.py` |
| 交易记录 (链上) | `python3 scripts/tx_history.py --onchain <地址>` |
| 验证地址 | `python3 scripts/utils.py validate <地址>` |
| 生成校验和 | `python3 scripts/utils.py checksum <地址>` |
| 生成新钱包 | `python3 scripts/generate_from_mnemonic.py "<助记词>"` |

## 脚本详细说明

### 1. USDT 转账 `scripts/transfer_usdt.py`

核心功能：**ERC-20 USDT 转账**。使用钱包私钥签名交易，通过公共 RPC 节点广播。

```bash
# 基本转账
python3 scripts/transfer_usdt.py 0xRecipientAddress 10.5

# 测试模式（模拟，不广播）
python3 scripts/transfer_usdt.py --test --to 0xRecipientAddress --amount 1.0

# 仅估算 Gas
python3 scripts/transfer_usdt.py --estimate-gas --to 0xRecipientAddress --amount 100

# 指定网络
python3 scripts/transfer_usdt.py --to 0xRecipientAddress --amount 10 --chain ethereum
```

转账流程：
1. 加载 `wallet.json` 获取私钥
2. 获取链上 nonce / gas price / chain id
3. 构建 ERC-20 `transfer(address,uint256)` calldata
4. 估算 gas limit
5. 显示费用摘要并请求确认
6. EIP-155 签名 (keccak256 + secp256k1 + RLP)
7. 广播到 Ethereum 网络
8. 保存交易记录到本地

**安全提示**：交易需要 ETH 作为 Gas 手续费。发送前会显示完整的费用明细。测试模式不会广播任何交易。

### 2. USDT 余额查询 `scripts/check_usdt_balance.py`

通过 `eth_call` 调用 USDT 合约的 `balanceOf(address)` 函数，实时查询链上余额。

```bash
# 查询钱包地址的 USDT + ETH 余额
python3 scripts/check_usdt_balance.py

# 查询所有余额 (USDT + ETH + BTC)
python3 scripts/check_usdt_balance.py --all

# 查询任意地址
python3 scripts/check_usdt_balance.py 0xdAC17F958D2ee523a2206206994597C13D831ec7
```

### 3. Gas 估算 `scripts/gas_estimator.py`

查看当前 Ethereum 网络 Gas 市场行情，估算各类操作的成本。

```bash
# Gas 市场报告（实时价格 + 常见操作费用估算）
python3 scripts/gas_estimator.py

# 估算一笔 USDT 转账的具体费用
python3 scripts/gas_estimator.py --transfer --to 0xRecipientAddress --amount 100
```

### 4. 交易记录 `scripts/tx_history.py`

支持本地保存的交易记录和链上历史查询。

```bash
# 查看本地交易记录
python3 scripts/tx_history.py

# 通过 Etherscan 查询链上 USDT 交易
python3 scripts/tx_history.py --onchain 0xYourAddress

# 指定查询条数
python3 scripts/tx_history.py --onchain --limit 20

# 清空本地记录
python3 scripts/tx_history.py --clear
```

### 5. 地址验证 `scripts/utils.py`

地址格式校验、EIP-55 校验和转换。

```bash
# 验证地址
python3 scripts/utils.py validate 0xe823494b7a3297009bb459a6B05DfAe7FC5aBe0a

# 生成校验和格式
python3 scripts/utils.py checksum 0xe823494b7a3297009bb459a6b05dfae7fc5abe0a
```

### 6. 余额查询 (原) `scripts/check_balance.py`

原有的 ETH/BTC 通用余额查询，支持任意地址识别。

```bash
python3 scripts/check_balance.py --wallet
python3 scripts/check_balance.py 0xAddress
python3 scripts/check_balance.py 1BTCAddress
```

### 7. 钱包生成 `scripts/generate_from_mnemonic.py`

根据助记词生成 ETH + BTC 地址（BIP39/BIP32/BIP44）。

```bash
python3 scripts/generate_from_mnemonic.py "your mnemonic phrase here"
```

## 技术说明

### USDT 转账流程

```
用户输入 (to, amount)
  → 构建 ERC-20 calldata (function selector + ABI 编码)
  → 获取 nonce, gasPrice, chainId
  → 估算 gasLimit (eth_estimateGas)
  → 显示摘要 → 确认
  → RLP 编码 [nonce, gas, gasLimit, usdt_contract, 0, data, v, r, s]
  → keccak256 哈希
  → secp256k1 ECDSA 签名 (EIP-155)
  → eth_sendRawTransaction
  → 保存交易记录
```

### USDT 精度

USDT 使用 6 位小数 (10^6)，转账金额按此精度缩放。

### 依赖

```bash
# Ethereum 密码学
apk add py3-pycryptodomex py3-cryptography py3-ecdsa
```

- `py3-pycryptodomex`: keccak256 哈希
- `py3-cryptography`: secp256k1 ECDSA 签名
- `py3-ecdsa`: BIP32/BIP44 密钥派生 (wallet generation)

### RPC 端点

使用公共 Ethereum RPC（按优先级）：
1. `rpc.ankr.com/eth` (推荐)
2. `eth.llamarpc.com`
3. `ethereum.publicnode.com`

## 安全

钱包信息包含敏感数据（私钥、助记词），**不在对话中明文显示**。所有私钥操作在本地完成，不经过第三方。

转账时 Gas 费用使用 ETH 支付，请确保钱包有足够 ETH。

## 来源与更新

- 来源仓库：https://github.com/OpenMinis/MinisSkills
- 来源链接：https://github.com/OpenMinis/MinisSkills/pull/75
- 许可证：MIT
- 最后同步：2026-07-26
- 检查更新命令：
  ```bash
  curl -sL "https://api.github.com/repos/OpenMinis/MinisSkills/pulls/75" | grep -o '"updated_at": "[^"]*"' | head -1
  ```
