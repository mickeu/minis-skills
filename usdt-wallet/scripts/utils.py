#!/usr/bin/env python3
"""
地址验证工具
验证以太坊地址格式，支持 EIP-55 校验和

用法:
  python3 utils.py validate <地址>          # 验证地址格式
  python3 utils.py checksum <地址>          # 显示 EIP-55 校验和地址
"""

import hashlib
import sys


def keccak256(data):
    from Crypto.Hash import keccak
    k = keccak.new(digest_bits=256)
    k.update(data)
    return k.digest()


def to_checksum_address(address):
    """将地址转换为 EIP-55 校验和格式"""
    address = address.lower().replace("0x", "")
    if len(address) != 40:
        raise ValueError("地址长度无效 (需要40个十六进制字符)")

    hashed = keccak256(address.encode("ascii")).hex()
    checksummed = "0x"

    for i, c in enumerate(address):
        if c.isdigit():
            checksummed += c
        else:
            # 如果哈希对应位置的 nibble >= 8，大写
            if int(hashed[i], 16) >= 8:
                checksummed += c.upper()
            else:
                checksummed += c

    return checksummed


def validate_address(address):
    """验证地址格式，检查 EIP-55 校验和"""
    if not address:
        return False, "地址为空"

    address = address.strip()

    if not address.startswith("0x"):
        return False, "地址必须以 0x 开头"

    hex_part = address[2:]
    if len(hex_part) != 40:
        return False, f"地址长度错误: 需要40个十六进制字符，收到 {len(hex_part)}"

    try:
        int(hex_part, 16)
    except ValueError:
        return False, "地址包含无效的十六进制字符"

    # 检查 EIP-55 校验和
    # 如果地址全是小写或全是大写，视为有效但建议使用正确的大小写
    if hex_part == hex_part.lower() or hex_part == hex_part.upper():
        checksummed = to_checksum_address(address)
        return True, f"有效地址 (建议使用校验和格式: {checksummed})"

    # 验证校验和
    expected = to_checksum_address(address)
    if address == expected:
        return True, "有效地址 (EIP-55 校验和验证通过)"
    else:
        return False, f"校验和错误。正确格式: {expected}"


def main():
    try:
        from Crypto.Hash import keccak
    except ImportError:
        print("错误: 请安装 py3-pycryptodomex")
        sys.exit(1)

    if len(sys.argv) < 3:
        print("用法:")
        print("  python3 utils.py validate <地址>")
        print("  python3 utils.py checksum <地址>")
        print()
        print("示例:")
        print("  python3 utils.py validate 0xe823494b7a3297009bb459a6B05DfAe7FC5aBe0a")
        print("  python3 utils.py checksum 0xe823494b7a3297009bb459a6b05dfae7fc5abe0a")
        sys.exit(1)

    command = sys.argv[1]
    address = sys.argv[2]

    if command == "validate":
        is_valid, msg = validate_address(address)
        if is_valid:
            print(f"✅ {msg}")
        else:
            print(f"❌ {msg}")
            sys.exit(1)

    elif command == "checksum":
        try:
            result = to_checksum_address(address)
            print(f"原始: {address}")
            print(f"校验和: {result}")
        except Exception as e:
            print(f"❌ 错误: {e}")
            sys.exit(1)

    else:
        print(f"未知命令: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()