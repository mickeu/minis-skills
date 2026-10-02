#!/usr/bin/env python3
"""
USDT (ERC-20) 余额查询脚本
支持查询任意地址的 USDT 余额

用法:
  python3 check_usdt_balance.py                    # 查询钱包中的地址
  python3 check_usdt_balance.py <地址>             # 查询指定地址
  python3 check_usdt_balance.py --all              # 查 USDT + ETH + BTC
"""

import json
import os
import sys
from urllib.request import Request, urlopen

WALLET_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wallet.json")

USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

RPC_URLS = [
    "https://rpc.ankr.com/eth",
    "https://eth.llamarpc.com",
    "https://ethereum.publicnode.com",
]

# keccak256("balanceOf(address)")
BALANCE_SELECTOR = bytes.fromhex("70a08231")


def keccak256(data):
    from Crypto.Hash import keccak
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()


def abi_encode_address(addr):
    addr = addr.lower().replace("0x", "")
    return bytes.fromhex(addr.rjust(64, "0"))


def build_balance_data(address):
    return BALANCE_SELECTOR + abi_encode_address(address)


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


def call_contract(data_hex):
    """通过 eth_call 查询合约"""
    tx = {"to": USDT_CONTRACT, "data": "0x" + data_hex.hex()}
    result = rpc_call("eth_call", [tx, "latest"])
    if result:
        return result
    return None


def get_usdt_balance(address):
    """查询 USDT 余额 (6位小数)"""
    data = build_balance_data(address)
    result = call_contract(data)
    if result and result != "0x":
        try:
            balance_raw = int(result, 16)
            return balance_raw / 10**6
        except (ValueError, TypeError):
            return None
    return 0.0


def get_eth_balance(address):
    """查询 ETH 余额"""
    result = rpc_call("eth_getBalance", [address, "latest"])
    if result:
        try:
            return int(result, 16) / 1e18
        except (ValueError, TypeError):
            return None
    return None


def load_wallet():
    with open(WALLET_FILE) as f:
        return json.load(f)


def main():
    try:
        from Crypto.Hash import keccak
    except ImportError:
        print("错误: 请安装 py3-pycryptodomex")
        sys.exit(1)

    args = sys.argv[1:]
    show_all = "--all" in args

    if len(args) == 0 or show_all or args[0] == "--wallet":
        wallet = load_wallet()
        address = wallet["eth_address"]
        btc_address = wallet["btc_address"]
        print(f"💰 Monika 钱包 ({wallet.get('note', '')})")
    else:
        address = args[0].strip()
        btc_address = None
        if not (address.startswith("0x") and len(address) == 42):
            print(f"错误: 无效的以太坊地址")
            sys.exit(1)
        print(f"💰 地址: {address}")

    print("=" * 50)

    print(f"\n  USDT (ERC-20): ", end="", flush=True)
    usdt = get_usdt_balance(address)
    if usdt is not None:
        print(f"{usdt:,.2f} USDT")
    else:
        print("❌ 查询失败")

    print(f"  ETH:           ", end="", flush=True)
    eth = get_eth_balance(address)
    if eth is not None:
        print(f"{eth:.6f} ETH")
    else:
        print("❌ 查询失败")

    if show_all and btc_address:
        print(f"  BTC:           {btc_address}")

    print()
    print(f"  合约地址: {USDT_CONTRACT}")
    print("=" * 50)


if __name__ == "__main__":
    main()