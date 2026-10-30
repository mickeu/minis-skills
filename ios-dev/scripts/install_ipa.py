#!/usr/bin/env python3
"""Install an already signed IPA.

手动上传 + 发送安装命令（可靠路径）：pymobiledevice3 11.x 的 install_from_local
在等待设备端响应时会无限挂起（实测卡死），改为显式上传 + send_plist + 轮询响应，
设备端正常返回 Progress/Complete。耗时约 10-20s。
"""
import asyncio, os, sys, time, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from session import CoreDeviceSession
from pymobiledevice3.services.afc import AfcService
from pymobiledevice3.services.installation_proxy import InstallationProxyService

STAGING_DIR = "/PublicStaging/0point-install"


async def main(ipa):
    data = open(ipa, "rb").read()
    remote_path = f"{STAGING_DIR}/{uuid.uuid4()}.ipa"
    last = [-1]

    def on_progress(pct):
        p = int(pct)
        if p // 10 != last[0] // 10 or p >= 100:
            print(f"  progress {p}%", flush=True)
            last[0] = p

    async with CoreDeviceSession() as sess:
        print("📱 Tunnel established, uploading IPA", flush=True)
        async with AfcService(sess.rsd) as afc:
            await afc.makedirs(STAGING_DIR)
            t0 = time.time()
            await asyncio.wait_for(afc.set_file_contents(remote_path, data), 180.0)
            print(f"📤 Upload OK ({time.time()-t0:.1f}s)", flush=True)

        inst = InstallationProxyService(sess.rsd)
        await inst.service.send_plist({
            "Command": "Install",
            "ClientOptions": {"PackageType": "Developer"},
            "PackagePath": remote_path,
        })

        while True:
            resp = await asyncio.wait_for(inst.service.recv_plist(), timeout=180.0)
            if not resp:
                raise RuntimeError("设备端安装服务关闭连接")
            if resp.get("Error"):
                raise RuntimeError(f"设备端安装错误: {resp.get('Error')}: {resp.get('ErrorDescription')}")
            pct = resp.get("PercentComplete")
            if pct:
                on_progress(pct)
            if resp.get("Status") == "Complete":
                print("✅ 安装完成", flush=True)
                return


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 install_ipa.py <signed .ipa>\n"
              "Installs the IPA over the local loopback (10.7.0.1); requires: pairing file, loopback VPN, Wi-Fi.")
        sys.exit(0 if len(sys.argv) == 2 else 2)
    if not os.path.isfile(sys.argv[1]):
        sys.exit(f"❌ file not found: {sys.argv[1]}")
    asyncio.run(main(sys.argv[1]))