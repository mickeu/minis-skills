"""设备码生成 — 对应 DeviceInfo.CreateDeviceCode()

⚠️ 本地补丁（2026-10-23）：上游默认 device 码是 qiuyurs/coolApkAPI 的共享硬编码值，
所有 coolapk-mcp 用户共用同一个，已被酷安风控标记为"设备登录账号过多"（接口返回 -415）。
本补丁改为每次生成随机设备码，读操作（搜索/热榜/用户/话题/二手）实测稳定可用。
注意：随机设备码对写操作（点赞/回复/关注）不如共享默认码可靠，写操作建议用真实登录 Cookie。
"""

import base64
import os


def generate_device_code() -> str:
    """生成随机设备码（Base64 风格长串，约 134 字符）。

    酷安 X-App-Device 接受随机长字符串。共享默认码会被风控 -415，必须用随机值。
    """
    return base64.b64encode(os.urandom(100)).decode("ascii").rstrip("=")