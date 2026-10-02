#!/usr/bin/env python3
"""
Gas 费用估算工具
查看当前 Ethereum 网络 Gas 价格

用法:
  python3 gas_estimator.py              # 查看当前 Gas 价格
  python3 gas_estimator.py --transfer   # 估算 USDT 转账费用
  python3 gas_estimator.py --to <地址> --amount 10.5  # 指定转账参数估算
"""

import json
import os
import sys
from urllib.request import Request, urlopen

RPC_URLS = [
    "https://rpc.ankr.com/eth",
    "https://eth.llamarpc.com",
    "https://ethereum.publicnode.com",
]

USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
WALLET_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wallet.json")

TRANSFER_SELECTOR = bytes.fromhex("a9059cbb")


def keccak256(data):
    from Crypto.Hash import keccak
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()


def abi_encode_address(addr):
    addr = addr.lower().replace("0x", "")
    return bytes.fromhex(addr.rjust(64, "0"))


def abi_encode_uint256(value):
    h = hex(int(value))[2:].rstrip("L")
    return bytes.fromhex(h.rjust(64, "0"))


def build_transfer_data(to_address, amount):
    amount_scaled = int(amount * 10**6)
    data = TRANSFER_SELECTOR
    data += abi_encode_address(to_address)
    data += abi_encode_uint256(amount_scaled)
    return data


def rpc_call(method, params):
    for url in RPC_URLS:
        try:
            payload = json.dumps({
                "jsonrpc": "2.0", "method": method,
                "params": params, "id": 1
            }).encode()
            req = Request(url, data=payload, headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0"
            })
            with urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                if "error" in data:
                    continue
                return data["result"]
        except Exception:
            continue
    return None


def get_gas_price():
    r = rpc_call("eth_gasPrice", [])
    return int(r, 16) if r else None


def get_max_priority_fee():
    r = rpc_call("eth_maxPriorityFeePerGas", [])
    return int(r, 16) if r else None


def get_latest_block():
    r = rpc_call("eth_getBlockByNumber", ["latest", False])
    return r


def estimate_gas(from_addr, to_addr, data_hex):
    tx = {"from": from_addr, "to": to_addr, "data": "0x" + data_hex.hex()}
    r = rpc_call("eth_estimateGas", [tx])
    return int(r, 16) if r else None


def print_gas_info():
    """打印当前 Gas 市场信息"""
    gas_price = get_gas_price()
    priority_fee = get_max_priority_fee()
    block = get_latest_block()

    print("⛽ Ethereum Gas 市场报告")
    print("=" * 50)

    if gas_price:
        base_fee = int(block.get("baseFeePerGas", "0x0"), 16) if block else 0
        print(f"  当前 Gas 价格:  {gas_price / 1e9:.2f} Gwei ({gas_price / 1e18:.8f} ETH)")
        if base_fee:
            print(f"  基础费 (Base):   {base_fee / 1e9:.2f} Gwei")
        if priority_fee:
            print(f"  优先费 (Tip):    {priority_fee / 1e9:.2f} Gwei")

        # 估算不同操作的 Gas 费用
        print()
        print("  常见操作费用估算:")
        print(f"  简单 ETH 转账 (21000 gas):")
        print(f"    ≈ {gas_price * 21000 / 1e18:.8f} ETH (${gas_price * 21000 / 1e18 * 3500:.2f})")
        print(f"  USDT 转账 (≈65000 gas):")
        print(f"    ≈ {gas_price * 65000 / 1e18:.8f} ETH (${gas_price * 65000 / 1e18 * 3500:.2f})")
        print(f"  合约交互 (≈100000 gas):")
        print(f"    ≈ {gas_price * 100000 / 1e18:.8f} ETH (${gas_price * 100000 / 1e18 * 3500:.2f})")

        if block:
            block_num = int(block.get("number", "0x0"), 16)
            print(f"\n  最新区块: #{block_num:,}")
    else:
        print("  ❌ 无法获取 Gas 价格")

    print("=" * 50)


def estimate_transfer(to_address=None, amount=None):
    """估算 USDT 转账的 Gas 费用"""
    if not os.path.exists(WALLET_FILE):
        print("错误: wallet.json 不存在")
        return

    with open(WALLET_FILE) as f:
        wallet = json.load(f)

    from_addr = wallet["eth_address"]

    if not to_address:
        to_address = "0x0000000000000000000000000000000000000001"
    if not amount:
        amount = 1.0

    if not (to_address.startswith("0x") and len(to_address) == 42):
        print("错误: 无效的地址")
        return

    gas_price = get_gas_price()
    if gas_price is None:
        print("❌ 无法获取 Gas 价格")
        return

    tx_data = build_transfer_data(to_address, amount)
    gas_limit = estimate_gas(from_addr, USDT_CONTRACT, tx_data)

    if gas_limit is None:
        gas_limit = 65000
        print("⚠️  使用默认 Gas 限制: 65000")
    else:
        print(f"  Gas 限制 (估算): {gas_limit:,}")

    total_eth = gas_price * gas_limit / 1e18
    total_usd = total_eth * 3500

    print()
    print(f"  📊 USDT 转账费用估算")
    print(f"  {'=' * 40}")
    print(f"  目标地址: {to_address}")
    print(f"  转账金额: {amount:.2f} USDT")
    print(f"  Gas 费:   {total_eth:.8f} ETH")
    print(f"  折合 USD: ~${total_usd:.2f}")
    print(f"  建议签名超时: gas_price * 1.2 = {gas_price * 1.2 / 1e9:.2f} Gwei")
    print(f"  {'=' * 40}")


def main():
    args = sys.argv[1:]

    if "--transfer" in args or "--tx" in args:
        to_addr = None
        amount = None

        if "--to" in args:
            idx = args.index("--to")
            if idx + 1 < len(args):
                to_addr = args[idx + 1]
        if "--amount" in args:
            idx = args.index("--amount")
            if idx + 1 < len(args):
                try:
                    amount = float(args[idx + 1])
                except ValueError:
                    pass

        estimate_transfer(to_addr, amount)
    else:
        print_gas_info()


if __name__ == "__main__":
    main()