#!/usr/bin/env python3
import argparse
import base64
import hashlib
import re
import time
import zipfile

import bcrypt

STD_B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def _find_blob(libauth_bytes: bytes) -> bytes:
    # libauth contains one long base64 blob used by getToken.
    # choose the one that decodes and XOR(0x5A) yields mostly printable bytes.
    candidates = re.findall(rb"[A-Za-z0-9+/]{1000,}", libauth_bytes)
    best = None
    best_score = -1.0
    for cand in candidates:
        try:
            dec = base64.b64decode(cand, validate=True)
        except Exception:
            continue
        if not dec:
            continue
        x = bytes(b ^ 0x5A for b in dec)
        printable = sum(1 for c in x if 32 <= c < 127)
        score = printable / len(x)
        if score > best_score:
            best_score = score
            best = cand
    if best is None:
        raise RuntimeError("Could not locate token blob in libauth.so")
    return best


def _shift_last_char_minus_5(s: str) -> str:
    idx = STD_B64.index(s[-1])
    return s[:-1] + STD_B64[(idx - 5) % 64]


def generate_token(apk_path: str, device: str, ts: int, version_code: int, package: str) -> str:
    with zipfile.ZipFile(apk_path, "r") as zf:
        libauth = zf.read("lib/arm64-v8a/libauth.so")

    blob = _find_blob(libauth)
    phase1 = base64.b64decode(blob)
    phase2 = bytes(b ^ 0x5A for b in phase1)

    idx = ((ts + version_code) % 100) * 4 + 0x80
    if idx >= len(phase2):
        raise RuntimeError(f"index out of range: idx={idx}, blob_len={len(phase2)}")

    chunk = phase2[idx : idx + 0x80]
    segment = base64.b64decode(chunk)

    md5_device = hashlib.md5(device.encode("utf-8")).hexdigest().encode("ascii")

    plain = (
        package.encode("utf-8")
        + b"&"
        + segment
        + b"&"
        + md5_device
        + b"&"
        + str(ts).encode("ascii")
        + b"&"
        + str(version_code).encode("ascii")
    )

    pw = hashlib.md5(base64.b64encode(plain)).hexdigest().encode("ascii")

    salt_src = base64.b64encode(
        f"{ts:x}/{hashlib.md5(plain).hexdigest()}".encode("ascii")
    ).decode("ascii").rstrip("=")

    # Match native output exactly: take first 22 chars and shift final char by -5.
    salt22 = _shift_last_char_minus_5(salt_src[:22])
    setting = f"$2y$10${salt22}".encode("ascii")

    hashed = bcrypt.hashpw(pw, setting)
    token = "v3" + base64.b64encode(hashed).decode("ascii").rstrip("=")
    return token


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate CoolApk X-App-Token from APK + device id")
    parser.add_argument("--apk", default="coolapk.apk", help="Path to coolapk.apk")
    parser.add_argument("--device", required=True, help="X-App-Device value")
    parser.add_argument("--ts", type=int, default=int(time.time()), help="Unix timestamp (seconds)")
    parser.add_argument("--version-code", type=int, default=2602111, help="App versionCode")
    parser.add_argument("--package", default="com.coolapk.market", help="Package name")
    args = parser.parse_args()

    token = generate_token(
        apk_path=args.apk,
        device=args.device,
        ts=args.ts,
        version_code=args.version_code,
        package=args.package,
    )
    print(token)


if __name__ == "__main__":
    main()
