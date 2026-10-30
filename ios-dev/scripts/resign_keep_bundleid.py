#!/usr/bin/env python3
"""
resign_keep_bundleid.py — 保持原包名的 iOS 重签（复现 LCSign / 轻松签 / 全能签 的能力）

用法:
    python3 resign_keep_bundleid.py <input.ipa> [output.ipa]
    python3 resign_keep_bundleid.py <input.ipa> --install      # 签完直接装

原理（关键，别再搞错）:
    1. **保留 App 原 CFBundleIdentifier，绝不改包名**
    2. 只把签名 entitlements 设为描述文件的 Entitlements（application-identifier = <team>.<profileAppID>）
    3. 用 p12 签名
    → iOS 安装校验的是 entitlements（匹配描述文件 ✅），系统按 CFBundleIdentifier 区分 App
    → 因此一份描述文件可签任意包名的 App，且各 App 保持原包名、互不覆盖

    ⚠️ 常见错误：把 CFBundleIdentifier 改成描述文件的 App ID 去"迁就"它 → 所有 App 撞同一 ID → 互相覆盖。
       正确做法是改 entitlements，不是改包名。
"""
import glob
import os
import plistlib
import shutil
import subprocess
import sys
import tempfile
import zipfile

KEYS = os.path.expanduser("~/.ios-signer/keys")
P12 = os.path.join(KEYS, "dev.legacy.p12")          # legacy 格式（rcodesign 0.29 读得了）
PROFILE = os.path.join(KEYS, "dev.mobileprovision")  # 描述文件
PASSFILE = os.path.join(KEYS, "p12.pass")            # 密码（600）


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_install = "--install" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    ipa = os.path.abspath(args[0])
    out = os.path.abspath(args[1]) if len(args) > 1 else os.path.splitext(ipa)[0] + "-signed.ipa"
    for f in (P12, PROFILE, PASSFILE):
        if not os.path.exists(f):
            sys.exit(f"❌ 缺少签名资产: {f}")

    work = tempfile.mkdtemp(prefix="resign-")
    with zipfile.ZipFile(ipa) as z:
        z.extractall(work)
    apps = glob.glob(os.path.join(work, "Payload", "*.app"))
    if not apps:
        sys.exit("❌ IPA 里找不到 Payload/*.app")
    app = apps[0]

    # 1) 原包名保留
    with open(os.path.join(app, "Info.plist"), "rb") as f:
        bid = plistlib.load(f).get("CFBundleIdentifier")
    print(f"✅ 保留原包名: {bid}")

    # 2) entitlements 用描述文件那套
    raw = subprocess.run(
        ["openssl", "smime", "-inform", "DER", "-verify", "-noverify", "-in", PROFILE],
        capture_output=True).stdout
    ent = plistlib.loads(raw)["Entitlements"]
    ent["com.apple.security.application-groups"] = ["group.W98A28M8HV.DF7vj"]
    ent_path = os.path.join(work, "ent.plist")
    with open(ent_path, "wb") as f:
        plistlib.dump(ent, f)
    print(f"✅ 签名 entitlements application-identifier: {ent.get('application-identifier')}")

    # 3) 塞入描述文件（主 App + 所有扩展）
    shutil.copyfile(PROFILE, os.path.join(app, "embedded.mobileprovision"))
    for appex in glob.glob(os.path.join(app, "PlugIns", "*.appex")):
        shutil.copyfile(PROFILE, os.path.join(appex, "embedded.mobileprovision"))

    # 4) 清旧签名
    for cs in glob.glob(os.path.join(app, "**", "_CodeSignature"), recursive=True):
        shutil.rmtree(cs, ignore_errors=True)

    # 5) rcodesign 签名（rcodesign 读不了 stdin 密码，用 600 临时文件）
    with open(PASSFILE) as f:
        password = f.read()
    pw = os.path.join(work, ".pw")
    with open(pw, "w") as f:
        f.write(password)
    os.chmod(pw, 0o600)
    r = subprocess.run(
        ["rcodesign", "sign", "--p12-file", P12, "--p12-password-file", pw,
         "--entitlements-xml-file", ent_path, "--timestamp-url", "none", app],
        capture_output=True, text=True)
    os.remove(pw)
    if r.returncode != 0:
        sys.exit(f"❌ 签名失败:\n{r.stderr[-800:]}")

    # 6) 打包（zip -qry 保留符号链接）
    os.path.exists(out) and os.remove(out)
    subprocess.run(["zip", "-qry", out, "Payload"], cwd=work, check=True)
    print(f"📦 {out}")

    # 7) 可选安装
    if do_install:
        here = os.path.dirname(os.path.abspath(__file__))
        env = dict(os.environ, CDTK_PAIRING_FILE=os.environ.get(
            "CDTK_PAIRING_FILE", os.path.expanduser("~/.cdtk/pairing/pairing.plist")))
        r = subprocess.run([sys.executable, os.path.join(here, "install_ipa.py"), out],
                           env=env, capture_output=True, text=True)
        print(r.stdout[-400:] if r.returncode == 0 else f"❌ 安装失败:\n{(r.stdout+r.stderr)[-500:]}")

    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
