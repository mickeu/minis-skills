#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
参照 Surge 配置生成 sing-box 完整配置。
- 节点来源：订阅解析后的 /tmp/sub.decoded（hysteria2/trojan/vless/vmess）
- 规则集：MetaCubeX/meta-rules-dat sing 分支 .srs 二进制（最适合 sing-box）
- 策略组/DNS/分流对齐 Surge 配置
"""
import json, re, sys
from urllib.parse import urlparse, parse_qs, unquote

RAW = open("/tmp/sub.decoded", "r").read()
NODES_RAW = [l.strip() for l in RAW.splitlines() if l.strip()]

# ---- 节点解析 ----
def parse_hysteria2(url):
    # hysteria2://password@host:port?sni=..&insecure=..&mport=..#name
    u = urlparse(url)
    frag = unquote(u.fragment) if u.fragment else ""
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    password = unquote(u.username) if u.username else ""
    host = u.hostname
    port = u.port
    ob = {
        "type": "hysteria2",
        "tag": frag,
        "server": host,
        "server_port": port,
        "password": password,
        "tls": {
            "enabled": True,
            "server_name": q.get("sni", ""),
            "insecure": q.get("insecure") == "1",
        },
    }
    # mport 端口跳跃 -> server_ports
    if "mport" in q:
        m = q["mport"]
        # 形如 50000-53000 -> sing-box "50000:53000"
        if "-" in m:
            a, b = m.split("-", 1)
            ob["server_ports"] = [f"{a}:{b}"]
    return ob

def parse_trojan(url):
    u = urlparse(url)
    frag = unquote(u.fragment) if u.fragment else ""
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    password = unquote(u.username) if u.username else ""
    host = u.hostname
    port = u.port or 443
    tls_enabled = True  # trojan 默认 TLS
    ob = {
        "type": "trojan",
        "tag": frag,
        "server": host,
        "server_port": port,
        "password": password,
        "tls": {
            "enabled": tls_enabled,
            "server_name": q.get("sni") or q.get("peer") or "",
            "insecure": q.get("allowInsecure") == "1",
        },
    }
    if q.get("fp"):
        ob["tls"]["utls"] = {"enabled": True, "fingerprint": q["fp"]}
    # transport ws
    if q.get("type") == "ws":
        transport = {"type": "ws"}
        if q.get("path"):
            transport["path"] = q["path"]
        headers = {}
        if q.get("host"):
            headers["Host"] = q["host"]
        if headers:
            transport["headers"] = headers
        ob["transport"] = transport
    return ob

def parse_vless(url):
    u = urlparse(url)
    frag = unquote(u.fragment) if u.fragment else ""
    q = {k: v[0] for k, v in parse_qs(u.query).items()}
    uuid = unquote(u.username) if u.username else ""
    host = u.hostname
    port = u.port
    ob = {
        "type": "vless",
        "tag": frag,
        "server": host,
        "server_port": port,
        "uuid": uuid,
    }
    if q.get("flow"):
        ob["flow"] = q["flow"]
    # security: reality / tls / none
    sec = q.get("security", "")
    if sec == "reality":
        ob["tls"] = {
            "enabled": True,
            "server_name": q.get("sni") or q.get("servername") or "",
            "utls": {"enabled": True, "fingerprint": q.get("fp", "chrome")},
            "reality": {
                "enabled": True,
                "public_key": q.get("pbk", ""),
                "short_id": q.get("sid", ""),
            },
        }
    elif sec == "tls":
        ob["tls"] = {"enabled": True, "server_name": q.get("sni", ""),
                     "insecure": q.get("allowInsecure") == "1",
                     "utls": {"enabled": True, "fingerprint": q.get("fp", "chrome")}}
    # transport
    t = q.get("type", "")
    if t == "ws":
        transport = {"type": "ws"}
        if q.get("path"):
            transport["path"] = q["path"]
        if q.get("host"):
            transport["headers"] = {"Host": q["host"]}
        ob["transport"] = transport
    # ws path 可能空 -> 默认 /
    return ob

def parse_vmess(url):
    # vmess://base64(json)
    b64 = url[len("vmess://"):]
    # 补 padding
    b64 += "=" * (-len(b64) % 4)
    raw = b64
    import base64
    try:
        j = json.loads(base64.b64decode(raw).decode("utf-8", "replace"))
    except Exception:
        j = json.loads(base64.b64decode(raw + "==").decode("utf-8", "replace"))
    tag = j.get("ps", "vmess")
    ob = {
        "type": "vmess",
        "tag": tag,
        "server": j.get("add"),
        "server_port": int(j.get("port", 443)),
        "uuid": j.get("id"),
        "security": j.get("scy", "auto"),
        "alter_id": int(j.get("aid", 0)),
    }
    if j.get("tls") in ("tls", "1", 1):
        ob["tls"] = {"enabled": True, "server_name": j.get("sni", "") or j.get("host", ""),
                     "insecure": j.get("verify_cert") in (False, "0", 0)}
        if j.get("fp"):
            ob["tls"]["utls"] = {"enabled": True, "fingerprint": j["fp"]}
    net = j.get("net", "")
    if net == "ws":
        transport = {"type": "ws"}
        if j.get("path"):
            transport["path"] = j["path"]
        if j.get("host"):
            transport["headers"] = {"Host": j["host"]}
        ob["transport"] = transport
    return ob

PARSERS = {
    "hysteria2://": parse_hysteria2,
    "trojan://": parse_trojan,
    "vless://": parse_vless,
    "vmess://": parse_vmess,
}

outbounds = []
errors = []
for line in NODES_RAW:
    matched = False
    for prefix, fn in PARSERS.items():
        if line.startswith(prefix):
            try:
                ob = fn(line)
                outbounds.append(ob)
                matched = True
            except Exception as e:
                errors.append(f"{line[:40]}... : {e}")
            break
    if not matched:
        errors.append(f"未知协议: {line[:40]}")

print(f"解析成功 {len(outbounds)} 个节点，失败 {len(errors)} 个", file=sys.stderr)
for e in errors:
    print("  ERR:", e, file=sys.stderr)

# 节点 tag 列表
all_tags = [o["tag"] for o in outbounds]

# ---- 地区分组（按 tag 正则筛选，对齐 Surge smart 组逻辑）----
import re as _re
def region_group(tag_prefix, pattern):
    p = _re.compile(pattern)
    tags = [o["tag"] for o in outbounds if p.search(o["tag"])]
    return tags

us_tags = region_group("us", r"🇺🇸|美国|US|United")
jp_tags = region_group("jp", r"🇯🇵|日本|JP|Japan")
sg_tags = region_group("sg", r"🇸🇬|新加坡|SG|Singapore")
hk_tags = region_group("hk", r"🇭🇰|香港|HK|Hong")
gb_tags = region_group("gb", r"🇬🇧|英国|UK|Britain")

# ---- 配置主体 ----
config = {}

# log
config["log"] = {
    "level": "info",
    "timestamp": True,
}

# http_clients（1.14+ 替代 download_detour）
config["http_clients"] = [
    {"tag": "proxy", "detour": "PROXY"},
]

# DNS：参照 Surge 防泄露设计（sing-box 1.12+ 新 DNS server 格式）
# bootstrap 国内 UDP 解析 DoH 域名稳；上游境外 DoH 出口境外（DNS leak test 无中国旗）
config["dns"] = {
    "servers": [
        # 国内 DoH，默认走空 direct 出站（直连），用 dns-bootstrap 解析其域名
        {
            "type": "https",
            "tag": "dns-local",
            "server": "223.5.5.5",
            "server_port": 443,
            "domain_resolver": "dns-bootstrap",
        },
        # 境外 DoH，经 PROXY 出站（防泄露）
        {
            "type": "https",
            "tag": "dns-proxy",
            "server": "1.1.1.1",
            "server_port": 443,
            "domain_resolver": "dns-bootstrap",
            "detour": "PROXY",
        },
        # 系统/本地 DNS（bootstrap，纯 UDP，解析上面两个 DoH 的域名）
        {
            "type": "local",
            "tag": "dns-bootstrap",
        },
        # FakeIP 独立 server（1.12+ 新格式）
        {
            "type": "fakeip",
            "tag": "dns-fakeip",
            "inet4_range": "198.18.0.0/15",
            "inet6_range": "fc00::/18",
        },
    ],
    "rules": [
        # 广告域名拒答
        {"rule_set": "geosite-category-ads-all", "action": "reject"},
        # 国内域名用国内 DoH 直连解析
        {"rule_set": ["geosite-cn", "geosite-geolocation-cn"], "action": "route", "server": "dns-local"},
        # 代理域名用境外 DoH 经代理解析（防泄露）
        {"rule_set": ["geosite-geolocation-!cn", "geosite-gfw"], "action": "route", "server": "dns-proxy"},
        # 其余域名走 FakeIP（避免真实 DNS 解析，由 sing-box 自行匹配规则后决定是否代理解析）
        {"query_type": ["A", "AAAA"], "action": "route", "server": "dns-fakeip"},
    ],
    "final": "dns-proxy",
    "strategy": "prefer_ipv4",
    "reverse_mapping": True,
}

# inbounds：TUN + mixed
config["inbounds"] = [
    {
        "type": "tun",
        "tag": "tun-in",
        "address": ["172.18.0.1/30"],
        "mtu": 9000,
        "auto_route": True,
        "strict_route": True,
        "stack": "system",
    },
    {
        "type": "mixed",
        "tag": "mixed-in",
        "listen": "127.0.0.1",
        "listen_port": 2080,
    },
]

# outbounds：节点 + 策略组
obs = []

# direct / block / dns-out
obs.append({"type": "direct", "tag": "direct"})
obs.append({"type": "block", "tag": "block"})

# 所有真实节点
obs.extend(outbounds)

# 地区 urltest 组
def urltest(tag, members):
    if not members:
        return None
    return {
        "type": "urltest",
        "tag": tag,
        "outbounds": members,
        "url": "https://www.gstatic.com/generate_204",
        "interval": "3m",
        "tolerance": 50,
        "interrupt_exist_connections": False,
    }

for tag, members in [
    ("🇺🇸 美国节点", us_tags),
    ("🇯🇵 日本节点", jp_tags),
    ("🇸🇬 新加坡节点", sg_tags),
    ("🇭🇰 香港节点", hk_tags),
    ("🇬🇧 英国节点", gb_tags),
]:
    g = urltest(tag, members)
    if g:
        obs.append(g)

# 服务策略组（selector，对齐 Surge）
def selector(tag, members, default=None):
    return {
        "type": "selector",
        "tag": tag,
        "outbounds": members,
        "default": default or members[0],
        "interrupt_exist_connections": False,
    }

# PROXY 主组
proxy_members = [t for t in ["🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点", "🇭🇰 香港节点", "🇬🇧 英国节点"]] + all_tags
obs.append(selector("PROXY", proxy_members, "🇺🇸 美国节点"))

# AIGC（AI 服务，默认日本/新加坡，对齐 Surge）
obs.append(selector("AIGC", [t for t in ["🇯🇵 日本节点", "🇸🇬 新加坡节点", "🇺🇸 美国节点", "🇭🇰 香港节点"] if t]))
obs.append(selector("Telegram", [t for t in ["🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点", "🇭🇰 香港节点"] if t]))
obs.append(selector("GlobalMedia", [t for t in ["🇯🇵 日本节点", "🇸🇬 新加坡节点", "🇭🇰 香港节点", "🇺🇸 美国节点"] if t]))
obs.append(selector("YouTube", [t for t in ["🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"] if t]))
obs.append(selector("Netflix", ["PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("Disney+", ["PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("Spotify", ["PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("TikTok", ["🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("BiliBili", ["direct", "🇭🇰 香港节点"]))
obs.append(selector("Apple", ["direct", "PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("Microsoft", ["direct", "PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))
obs.append(selector("Game", ["direct", "PROXY", "🇭🇰 香港节点", "🇺🇸 美国节点", "🇯🇵 日本节点", "🇸🇬 新加坡节点"]))

config["outbounds"] = obs

# 规则集定义（MetaCubeX meta-rules-dat sing 分支 .srs）
SRSPREFIX = "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/sing/geo"
def rs(tag, kind, name):
    return {
        "type": "remote",
        "tag": tag,
        "format": "binary",
        "url": f"{SRSPREFIX}/{kind}/{name}.srs",
        "http_client": "proxy",
        "update_interval": "168h0m0s",
    }

rule_sets = [
    rs("geosite-category-ads-all", "geosite", "category-ads-all"),
    rs("geosite-private", "geosite", "private"),
    rs("geoip-private", "geoip", "private"),
    rs("geosite-openai", "geosite", "openai"),
    rs("geosite-anthropic", "geosite", "anthropic"),
    rs("geosite-google", "geosite", "google"),
    rs("geosite-apple", "geosite", "apple"),
    rs("geosite-apple-cn", "geosite", "apple@cn"),
    rs("geosite-apple-intelligence", "geosite", "apple-intelligence"),
    rs("geosite-microsoft", "geosite", "microsoft"),
    rs("geosite-telegram", "geosite", "telegram"),
    rs("geosite-youtube", "geosite", "youtube"),
    rs("geosite-netflix", "geosite", "netflix"),
    rs("geosite-disney", "geosite", "disney"),
    rs("geosite-spotify", "geosite", "spotify"),
    rs("geosite-tiktok", "geosite", "tiktok"),
    rs("geosite-bilibili", "geosite", "bilibili"),
    rs("geosite-category-games", "geosite", "category-games"),
    rs("geosite-blizzard", "geosite", "blizzard"),
    rs("geosite-category-media-cn", "geosite", "category-media-cn"),
    rs("geosite-cn", "geosite", "cn"),
    rs("geosite-geolocation-cn", "geosite", "geolocation-cn"),
    rs("geosite-geolocation-!cn", "geosite", "geolocation-!cn"),
    rs("geosite-gfw", "geosite", "gfw"),
    rs("geosite-tld-cn", "geosite", "tld-cn"),
    rs("geoip-cn", "geoip", "cn"),
    rs("geoip-telegram", "geoip", "telegram"),
]

# route rules：对齐 Surge 规则顺序
rules = [
    # 广告拦截
    {"rule_set": "geosite-category-ads-all", "action": "reject", "method": "default"},
    # 局域网直连
    {"rule_set": ["geosite-private", "geoip-private"], "action": "route", "outbound": "direct"},
    {"ip_is_private": True, "action": "route", "outbound": "direct"},
    # AI 服务（OpenAI/Claude/Google Gemini）走 AIGC
    {"rule_set": ["geosite-openai", "geosite-anthropic", "geosite-google"], "action": "route", "outbound": "AIGC"},
    # Apple Intelligence 必须先于 Apple 走代理
    {"rule_set": "geosite-apple-intelligence", "action": "route", "outbound": "AIGC"},
    # Apple 服务（中国可直连部分用 cn 组直连，其余走 Apple 组）
    {"rule_set": "geosite-apple-cn", "action": "route", "outbound": "direct"},
    {"rule_set": "geosite-apple", "action": "route", "outbound": "Apple"},
    # 微软
    {"rule_set": "geosite-microsoft", "action": "route", "outbound": "Microsoft"},
    # Telegram
    {"rule_set": "geosite-telegram", "action": "route", "outbound": "Telegram"},
    {"rule_set": "geoip-telegram", "action": "route", "outbound": "Telegram"},
    # 游戏
    {"rule_set": ["geosite-category-games", "geosite-blizzard"], "action": "route", "outbound": "Game"},
    # 流媒体
    {"rule_set": "geosite-youtube", "action": "route", "outbound": "YouTube"},
    {"rule_set": "geosite-netflix", "action": "route", "outbound": "Netflix"},
    {"rule_set": "geosite-disney", "action": "route", "outbound": "Disney+"},
    {"rule_set": "geosite-spotify", "action": "route", "outbound": "Spotify"},
    {"rule_set": "geosite-tiktok", "action": "route", "outbound": "TikTok"},
    {"rule_set": "geosite-bilibili", "action": "route", "outbound": "BiliBili"},
    {"rule_set": "geosite-category-media-cn", "action": "route", "outbound": "direct"},
    # 中国直连四层
    {"rule_set": "geosite-tld-cn", "action": "route", "outbound": "direct"},
    {"rule_set": "geosite-geolocation-cn", "action": "route", "outbound": "direct"},
    {"rule_set": "geosite-cn", "action": "route", "outbound": "direct"},
    {"rule_set": "geoip-cn", "action": "route", "outbound": "direct"},
    # 境外兜底代理
    {"rule_set": ["geosite-geolocation-!cn", "geosite-gfw"], "action": "route", "outbound": "PROXY"},
]

config["route"] = {
    "rule_set": rule_sets,
    "rules": rules,
    "final": "PROXY",
    "auto_detect_interface": True,
    "default_domain_resolver": "dns-local",
    "default_http_client": "proxy",
}

# experimental：缓存 + clash api（selector 控制需要）
config["experimental"] = {
    "cache_file": {"enabled": True, "path": "cache.db"},
    "clash_api": {
        "external_controller": "127.0.0.1:9090",
        "default_mode": "rule",
    },
}

# 输出
out = json.dumps(config, ensure_ascii=False, indent=2)
with open("/var/minis/workspace/sing-box-gen/config.json", "w") as f:
    f.write(out)
print("写入 /var/minis/workspace/sing-box-gen/config.json")
print(f"outbounds: {len(obs)}, rules: {len(rules)}, rule_sets: {len(rule_sets)}")
