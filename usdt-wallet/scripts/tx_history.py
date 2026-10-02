#!/usr/bin/env python3
"""
交易记录查询
查看最近的转账记录 / 通过 Etherscan 查询链上交易

用法:
  python3 tx_history.py                     # 查看本地保存的交易记录
  python3 tx_history.py --onchain <地址>     # 通过 Etherscan 查询链上 USDT 转账
  python3 tx_history.py --onchain --limit 20
  python3 tx_history.py --clear             # 清空本地记录
"""

import json
import os
import sys
import time
from urllib.request import Request, urlopen

TX_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "transactions")
TX_FILE = os.path.join(TX_DIR, "recent_transactions.json")

ETHERSCAN_API = "https://api.etherscan.io/api"
USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"


def list_local_txs(limit=10):
    if not os.path.exists(TX_FILE):
        print("📭 暂无本地交易记录")
        return

    with open(TX_FILE) as f:
        txs = json.load(f)

    if not txs:
        print("📭 暂无本地交易记录")
        return

    print(f"📋 最近的交易记录 (共 {len(txs)} 条, 显示前 {min(limit, len(txs))} 条):")
    print("=" * 70)

    for i, tx in enumerate(txs[:limit]):
        status_icon = "⏳" if tx.get("status") == "pending" else "✅"
        ts = tx.get("date", time.strftime("%Y-%m-%d %H:%M", time.localtime(tx.get("timestamp", 0))))
        print(f"  {i+1}. {status_icon} {ts}")
        print(f"     {tx.get('amount', '?')} {tx.get('token', '?')}")
        print(f"     → {tx['to'][:10]}...{tx['to'][-6:]}")
        print(f"     Tx: {tx['tx_hash'][:10]}...{tx['tx_hash'][-6:]}")
        tx_url = f"https://etherscan.io/tx/{tx['tx_hash']}"
        print(f"     {tx_url}")
        print()


def query_onchain(address, limit=10):
    """通过 Etherscan API 查询 USDT 转账"""
    if not (address.startswith("0x") and len(address) == 42):
        print(f"错误: 无效的以太坊地址")
        return

    # 构造查询参数 - 使用 txlist 获取 USDT 合约的转账事件
    params = (
        f"?module=account"
        f"&action=tokentx"
        f"&contractaddress={USDT_CONTRACT}"
        f"&address={address}"
        f"&sort=desc"
        f"&offset={limit}"
        f"&page=1"
    )

    url = ETHERSCAN_API + params

    print(f"⏳ 查询链上 USDT 交易记录...")
    print(f"  地址: {address}")
    print(f"  合约: {USDT_CONTRACT}")
    print()

    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        return

    if data.get("status") != "1":
        print("⚠️  未查到交易记录 (或 API 限制)")
        return

    txs = data.get("result", [])

    if not txs:
        print("📭 该地址无 USDT 转账记录")
        return

    print(f"📋 最新的 {len(txs)} 条 USDT 交易:")
    print("=" * 80)

    for tx in txs:
        timestamp = int(tx.get("timeStamp", 0))
        date_str = time.strftime("%Y-%m-%d %H:%M", time.localtime(timestamp))

        value = int(tx.get("value", 0)) / 10**6
        token_symbol = tx.get("tokenSymbol", "USDT")
        tx_hash = tx.get("hash", "")

        from_addr = tx.get("from", "")
        to_addr = tx.get("to", "")

        tx_type = "➡️ 发送" if from_addr.lower() == address.lower() else "⬅️ 接收"

        print(f"  {date_str}  {tx_type}")
        print(f"  金额: {value:,.2f} {token_symbol}")
        if tx_type == "⬅️ 接收":
            print(f"  来自: {from_addr[:10]}...{from_addr[-6:]}")
        else:
            print(f"  发送至: {to_addr[:10]}...{to_addr[-6:]}")
        print(f"  TxHash: {tx_hash[:10]}...{tx_hash[-6:]}")
        print()

    print(f"  完整记录: https://etherscan.io/token/{USDT_CONTRACT}?a={address}")


def clear_local():
    if os.path.exists(TX_FILE):
        with open(TX_FILE, "w") as f:
            json.dump([], f)
        print("✅ 本地交易记录已清空")
    else:
        print("📭 无记录可清空")


def main():
    args = sys.argv[1:]

    if "--clear" in args:
        clear_local()
        return

    if "--onchain" in args:
        idx = args.index("--onchain")
        address = args[idx + 1] if idx + 1 < len(args) and not args[idx+1].startswith("--") else None
        limit = 10
        if "--limit" in args:
            li = args.index("--limit")
            if li + 1 < len(args):
                try:
                    limit = int(args[li + 1])
                except ValueError:
                    pass

        if not address:
            # 从钱包读取地址
            wallet_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wallet.json")
            if os.path.exists(wallet_file):
                with open(wallet_file) as f:
                    wallet = json.load(f)
                address = wallet["eth_address"]
                print(f"📖 使用钱包地址: {address}")
            else:
                print("错误: 请指定地址或确保 wallet.json 存在")
                sys.exit(1)

        query_onchain(address, limit)
    else:
        list_local_txs()


if __name__ == "__main__":
    main()