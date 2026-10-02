#!/usr/bin/env python3
"""
通用钱包余额查询脚本
支持查询 ETH 和 BTC 余额

用法:
  python3 check_balance.py <地址>
  python3 check_balance.py 0xe823... 或 1HXAU...
  python3 check_balance.py --wallet  (使用 wallet.json 中的地址)
"""
import json
import urllib.request
import sys
import os

WALLET_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wallet.json")

def is_eth_address(addr):
    return addr.startswith("0x") and len(addr) == 42

def is_btc_address(addr):
    # 简单判断：1或3开头，或bc1开头
    return (addr.startswith("1") or addr.startswith("3") or addr.startswith("bc1")) and len(addr) >= 26

def check_eth_balance(address):
    """通过公共 Ethereum RPC 查询 ETH 余额"""
    rpc_urls = [
        "https://rpc.ankr.com/eth",
        "https://eth.llamarpc.com",
        "https://ethereum.publicnode.com",
    ]
    
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }).encode()
    
    for rpc_url in rpc_urls:
        try:
            req = urllib.request.Request(
                rpc_url,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0"
                }
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
                if "result" in data:
                    balance_wei = int(data["result"], 16)
                    balance_eth = balance_wei / 1e18
                    return balance_eth, None
        except Exception:
            continue
    
    return None, "所有 RPC 节点查询失败"

def check_btc_balance(address):
    """通过 blockchain.info 查询 BTC 余额"""
    url = f"https://blockchain.info/q/addressbalance/{address}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            balance_satoshis = int(resp.read().strip())
            balance_btc = balance_satoshis / 1e8
            return balance_btc, None
    except Exception as e:
        return None, str(e)

def load_wallet():
    with open(WALLET_FILE, 'r') as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        print("用法: python3 check_balance.py <地址>")
        print("      python3 check_balance.py --wallet")
        print("")
        print("示例:")
        print("  python3 check_balance.py 0xe823494b7a3297009bb459a6B05DfAe7FC5aBe0a")
        print("  python3 check_balance.py 1HXAUZUKuXdo3R1Y2HJMvQRGF5hkenoKDE")
        sys.exit(1)
    
    arg = sys.argv[1]
    
    if arg == "--wallet":
        wallet = load_wallet()
        addresses = {
            "ETH": wallet["eth_address"],
            "BTC": wallet["btc_address"]
        }
    else:
        addr = arg
        if is_eth_address(addr):
            addresses = {"ETH": addr}
        elif is_btc_address(addr):
            addresses = {"BTC": addr}
        else:
            print(f"无法识别地址类型: {addr}")
            sys.exit(1)
    
    print("=" * 50)
    print("钱包余额查询")
    print("=" * 50)
    
    for coin, addr in addresses.items():
        print(f"\n{coin} 地址: {addr}")
        if coin == "ETH":
            balance, error = check_eth_balance(addr)
            if error:
                print(f"余额: 查询失败 - {error}")
            else:
                print(f"余额: {balance:.6f} {coin}")
        elif coin == "BTC":
            balance, error = check_btc_balance(addr)
            if error:
                print(f"余额: 查询失败 - {error}")
            else:
                print(f"余额: {balance:.8f} {coin}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()