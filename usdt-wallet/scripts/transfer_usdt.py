#!/usr/bin/env python3
"""
USDT (ERC-20) 转账脚本
使用钱包私钥签名并广播 USDT 转账交易

用法:
  python3 transfer_usdt.py <接收地址> <金额>          # 使用 wallet.json 签名转账
  python3 transfer_usdt.py --to <地址> --amount <金额> # 同上
  python3 transfer_usdt.py --test                     # 模拟转账（不广播）
  python3 transfer_usdt.py --estimate-gas             # 仅估算 gas
"""

import json
import os
import sys
import time
from urllib.request import Request, urlopen

# --- 配置 ---
WALLET_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wallet.json")

# USDT 合约地址 (Ethereum Mainnet)
USDT_CONTRACT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# 可用的 Ethereum RPC 端点
RPC_URLS = [
    "https://rpc.ankr.com/eth",
    "https://eth.llamarpc.com",
    "https://ethereum.publicnode.com",
]

# 支持的链信息
CHAINS = {
    "ethereum": {"chain_id": 1, "name": "Ethereum Mainnet"},
    "sepolia": {"chain_id": 11155111, "name": "Sepolia Testnet"},
}

# ERC-20 transfer 函数选择器: keccak256("transfer(address,uint256)") 的前 4 字节
TRANSFER_SELECTOR = bytes.fromhex("a9059cbb")


def keccak256(data):
    """计算 keccak256 哈希"""
    from Crypto.Hash import keccak as keccak_mod
    k = keccak_mod.new(digest_bits=256)
    k.update(data)
    return k.digest()


def abi_encode_address(addr):
    """将地址编码为 32 字节 ABI 格式 (左补零)"""
    addr = addr.lower().replace("0x", "")
    return bytes.fromhex(addr.rjust(64, "0"))


def abi_encode_uint256(value):
    """将 uint256 编码为 32 字节 ABI 格式 (左补零)"""
    h = hex(int(value))[2:].rstrip("L")
    return bytes.fromhex(h.rjust(64, "0"))


def build_transfer_data(to_address, amount):
    """构建 ERC-20 transfer(address,uint256) 的 calldata"""
    # USDT 使用 6 位小数
    amount_scaled = int(amount * 10**6)
    data = TRANSFER_SELECTOR
    data += abi_encode_address(to_address)
    data += abi_encode_uint256(amount_scaled)
    return data


# --- RLP 编码 ---
def rlp_encode(item):
    if isinstance(item, int):
        if item == 0:
            return b"\x80"
        data = item.to_bytes((item.bit_length() + 7) // 8 or 1, "big")
        return rlp_encode(data)
    elif isinstance(item, bytes):
        length = len(item)
        if length == 0:
            return b"\x80"
        if length == 1 and item[0] < 0x80:
            return item
        if length < 56:
            return bytes([0x80 + length]) + item
        len_bytes = length.to_bytes((length.bit_length() + 7) // 8, "big")
        return bytes([0xB7 + len(len_bytes)]) + len_bytes + item
    elif isinstance(item, list):
        payload = b"".join(rlp_encode(i) for i in item)
        length = len(payload)
        if length < 56:
            return bytes([0xC0 + length]) + payload
        len_bytes = length.to_bytes((length.bit_length() + 7) // 8, "big")
        return bytes([0xF7 + len(len_bytes)]) + len_bytes + payload
    else:
        raise TypeError(f"RLP 不支持的类型: {type(item)}")


# --- JSON-RPC ---
def rpc_call(method, params, rpc_url=None):
    urls = [rpc_url] if rpc_url else RPC_URLS
    for url in urls:
        try:
            payload = json.dumps({
                "jsonrpc": "2.0", "method": method,
                "params": params, "id": 1
            }).encode()
            req = Request(url, data=payload, headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0"
            })
            with urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                if "error" in data:
                    continue
                return data["result"]
        except Exception:
            continue
    return None


def get_nonce(address):
    r = rpc_call("eth_getTransactionCount", [address, "pending"])
    return int(r, 16) if r else None


def get_gas_price():
    r = rpc_call("eth_gasPrice", [])
    return int(r, 16) if r else None


def estimate_gas(from_addr, to_addr, data_hex):
    tx = {"from": from_addr, "to": to_addr, "data": "0x" + data_hex.hex()}
    r = rpc_call("eth_estimateGas", [tx])
    return int(r, 16) if r else None


def get_chain_id():
    r = rpc_call("eth_chainId", [])
    return int(r, 16) if r else 1


def send_raw_transaction(signed_tx_hex):
    return rpc_call("eth_sendRawTransaction", ["0x" + signed_tx_hex.hex()])


# --- ECDSA 签名 (EIP-155) ---
def ecdsa_sign(tx_hash, private_key_hex, chain_id):
    """使用 cryptography 库进行 secp256k1 签名，返回 (v, r, s)"""
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import ec as ec_module

    pk_bytes = bytes.fromhex(private_key_hex.replace("0x", ""))
    pk_int = int.from_bytes(pk_bytes, "big")

    private_key = ec.derive_private_key(pk_int, ec.SECP256K1(), default_backend())

    # 使用 Prehashed 签名
    signature = private_key.sign(
        tx_hash,
        ec.ECDSA(ec_module.utils.Prehashed())
    )

    r, s = decode_dss_signature(signature)

    # 尝试两种 v 值 (EIP-155)
    pub_key = private_key.public_key()
    for rec_id in [0, 1]:
        v = chain_id * 2 + 35 + rec_id
        try:
            pub_key.verify(
                signature,
                tx_hash,
                ec.ECDSA(ec_module.utils.Prehashed())
            )
            return v, r, s
        except Exception:
            continue

    # fallback
    return chain_id * 2 + 35, r, s


# --- 主逻辑 ---
def load_wallet():
    with open(WALLET_FILE) as f:
        return json.load(f)


def print_summary(from_addr, to_addr, amount, gas_price_gwei, gas_limit,
                  total_eth, contract, chain_name):
    print(f"\n{'=' * 60}")
    print(f"  📋 USDT 转账确认")
    print(f"{'=' * 60}")
    print(f"  网络:       {chain_name}")
    print(f"  合约:       {contract}")
    print(f"  代币:       USDT (ERC-20)")
    print(f"  源地址:     {from_addr}")
    print(f"  目标地址:   {to_addr}")
    print(f"  金额:       {amount:.2f} USDT")
    print(f"  Gas 价格:   {gas_price_gwei:.2f} Gwei")
    print(f"  Gas 限制:   {gas_limit:,}")
    print(f"  Gas 费:     {total_eth:.8f} ETH ≈ ${total_eth * 3500:.2f}")
    print(f"{'=' * 60}\n")


def ask_confirm():
    """询问用户确认"""
    try:
        resp = input("确认发送? [y/N]: ").strip().lower()
        return resp in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        return False


def save_tx_record(tx_hash, from_addr, to_addr, amount, token, status):
    tx_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "transactions")
    os.makedirs(tx_dir, exist_ok=True)
    tx_file = os.path.join(tx_dir, "recent_transactions.json")

    record = {
        "tx_hash": tx_hash,
        "from": from_addr,
        "to": to_addr,
        "amount": amount,
        "token": token,
        "status": status,
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    txs = []
    if os.path.exists(tx_file):
        with open(tx_file) as f:
            txs = json.load(f)
    txs.insert(0, record)
    txs = txs[:50]
    with open(tx_file, "w") as f:
        json.dump(txs, f, indent=2)
    return tx_file


def main():
    # 检查依赖
    try:
        from Crypto.Hash import keccak
        from cryptography.hazmat.primitives.asymmetric import ec
    except ImportError:
        print("错误: 请安装必要的库: apk add py3-pycryptodomex py3-cryptography")
        sys.exit(1)

    if len(sys.argv) < 2 or "--help" in sys.argv or "-h" in sys.argv:
        print("用法:")
        print("  python3 transfer_usdt.py <接收地址> <金额>")
        print("  python3 transfer_usdt.py --to <地址> --amount <金额> [--chain ethereum]")
        print("  python3 transfer_usdt.py --test --to <地址> --amount 1.0")
        print("  python3 transfer_usdt.py --estimate-gas --to <地址> --amount 1.0")
        print("")
        print("示例:")
        print("  python3 transfer_usdt.py 0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B 10.5")
        print("  python3 transfer_usdt.py --test --to 0xRecipientAddress --amount 1.0")
        sys.exit(1)

    args = sys.argv[1:]
    test_mode = "--test" in args
    estimate_only = "--estimate-gas" in args

    # 解析参数
    to_address = None
    amount = None
    chain = "ethereum"

    i = 0
    while i < len(args):
        a = args[i]
        if a == "--to" and i + 1 < len(args):
            to_address = args[i + 1]
            i += 2
        elif a == "--amount" and i + 1 < len(args):
            try:
                amount = float(args[i + 1])
            except ValueError:
                print(f"错误: 无效金额 '{args[i+1]}'")
                sys.exit(1)
            i += 2
        elif a == "--chain" and i + 1 < len(args):
            chain = args[i + 1]
            i += 2
        elif a in ("--test", "--estimate-gas", "--help", "-h"):
            i += 1
        else:
            i += 1

    # 从位置参数读取
    pos_args = [a for a in args if not a.startswith("--")]
    if to_address is None and len(pos_args) >= 1:
        to_address = pos_args[0]
    if amount is None and len(pos_args) >= 2:
        try:
            amount = float(pos_args[1])
        except ValueError:
            pass

    if not to_address:
        print("错误: 请指定接收地址")
        sys.exit(1)
    if not amount or amount <= 0:
        print("错误: 请指定有效的转账金额 (> 0)")
        sys.exit(1)

    to_address = to_address.strip()
    if not (to_address.startswith("0x") and len(to_address) == 42):
        print(f"错误: 无效的以太坊地址: {to_address}")
        sys.exit(1)

    # 加载钱包
    wallet = load_wallet()
    from_address = wallet["eth_address"]
    private_key = wallet["private_key"]

    chain_id = CHAINS.get(chain, {}).get("chain_id", 1)
    chain_name = CHAINS.get(chain, {}).get("name", f"Chain ID {chain_id}")

    print(f"🔗 网络: {chain_name}")
    if test_mode:
        print("🧪 测试模式 — 不会广播交易")

    # 获取链上数据
    print("\n⏳ 获取链上信息...")

    nonce = get_nonce(from_address)
    if nonce is None:
        print("❌ 无法获取 nonce")
        sys.exit(1)
    print(f"  Nonce: {nonce}")

    real_chain_id = get_chain_id() or chain_id
    gas_price = get_gas_price()
    if gas_price is None:
        print("⚠️  无法获取 gas price，使用默认值 15 Gwei")
        gas_price = 15_000_000_000
    gas_price_gwei = gas_price / 1e9

    tx_data = build_transfer_data(to_address, amount)

    gas_limit = estimate_gas(from_address, USDT_CONTRACT, tx_data)
    if gas_limit is None:
        print("⚠️  无法估算 gas，使用默认值 65000")
        gas_limit = 65000

    total_eth_fee = gas_price * gas_limit / 1e18

    print_summary(from_address, to_address, amount, gas_price_gwei,
                  gas_limit, total_eth_fee, USDT_CONTRACT, chain_name)

    if estimate_only:
        print("✅ Gas 估算完成")
        return

    if test_mode:
        print("✅ 测试模式 — 交易未发送")
        return

    # 确认
    if not ask_confirm():
        print("❌ 用户取消")
        sys.exit(1)

    # 签名
    print("\n⏳ 签名交易...")

    tx_payload = [
        nonce, gas_price, gas_limit,
        bytes.fromhex(USDT_CONTRACT.replace("0x", "").lower()),
        0,  # value = 0 (USDT 转账)
        tx_data,
        real_chain_id, 0, 0
    ]

    encoded_unsigned = rlp_encode(tx_payload)
    tx_hash = keccak256(encoded_unsigned)

    v, r, s = ecdsa_sign(tx_hash, private_key, real_chain_id)

    final_tx = [
        nonce, gas_price, gas_limit,
        bytes.fromhex(USDT_CONTRACT.replace("0x", "").lower()),
        0,
        tx_data,
        v, r, s
    ]

    encoded_signed = rlp_encode(final_tx)

    # 广播
    print("⏳ 广播交易...")
    tx_hash_result = send_raw_transaction(encoded_signed)

    if tx_hash_result:
        tx_path = save_tx_record(
            tx_hash_result, from_address, to_address,
            amount, "USDT", "pending"
        )
        print(f"\n✅ 交易已发送!")
        print(f"  TxHash: {tx_hash_result}")
        print(f"  查看: https://etherscan.io/tx/{tx_hash_result}")
        print(f"  交易记录已保存: {tx_path}")
        return tx_hash_result
    else:
        print("\n❌ 交易广播失败")
        print("  可能的原因:")
        print("  - ETH 余额不足以支付 gas 费")
        print("  - 非预期 nonce (钱包在其他地方有交易)")
        print("  - RPC 节点不可用")
        sys.exit(1)


if __name__ == "__main__":
    main()