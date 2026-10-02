#!/usr/bin/env python3
"""Shodan 搜索引擎技能 - CLI 工具

提供 Shodan API 的完整功能封装，包括搜索、扫描、告警、DNS 等。
所有输出均为 JSON 格式，便于程序解析。
"""
import sys
import json
import shodan
import os
import argparse

# 尝试从环境变量或配置文件获取 API 密钥
API_KEY = os.environ.get('SHODAN_API_KEY')
CONFIG_FILE = os.path.expanduser('~/.config/shodan/api_key')

if not API_KEY:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                API_KEY = f.read().strip()
        except:
            pass

if not API_KEY:
    print(json.dumps({"error": "未找到 Shodan API 密钥，请设置 SHODAN_API_KEY 环境变量或运行 'shodan init <key>'"}))
    sys.exit(1)

try:
    api = shodan.Shodan(API_KEY)
except Exception as e:
    print(json.dumps({"error": f"Shodan API 初始化失败: {str(e)}"}))
    sys.exit(1)


def cmd_host(args):
    """查询主机详情"""
    try:
        host = api.host(args.ip, history=args.history, minify=args.minify)
        print(json.dumps(host, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_search(args):
    """高级搜索"""
    try:
        limit = args.limit if args.limit else 20
        page = args.page if args.page else 1
        results = api.search(args.query, limit=limit, page=page, facets=args.facets)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_count(args):
    """统计计数（不消耗查询额度）"""
    try:
        results = api.count(args.query, facets=args.facets)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_scan(args):
    """按需扫描（消耗扫描额度）"""
    try:
        scan = api.scan(args.ips)
        print(json.dumps(scan, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_alert_list(args):
    """列出所有网络告警"""
    try:
        alerts = api.alerts()
        print(json.dumps(alerts, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_alert_create(args):
    """创建网络告警"""
    try:
        alert = api.create_alert(args.name, args.ip)
        print(json.dumps(alert, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_alert_info(args):
    """查看告警详情"""
    try:
        info = api.alert_info(args.id)
        print(json.dumps(info, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_dns_domain(args):
    """域名信息查询"""
    try:
        domain = api.dns.domain_info(args.domain)
        print(json.dumps(domain, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_dns_resolve(args):
    """域名解析"""
    try:
        hostnames = args.hostnames.split(',')
        resolved = api.dns.resolve(hostnames)
        print(json.dumps(resolved, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_profile(args):
    """获取账户信息"""
    try:
        profile = api.info()
        print(json.dumps(profile, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_myip(args):
    """获取本机公网 IP"""
    try:
        ip = api.tools.myip()
        print(json.dumps({"ip": ip}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_ports(args):
    """列出 Shodan 扫描的端口"""
    try:
        ports = api.ports()
        print(json.dumps(ports, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_protocols(args):
    """列出 Shodan 扫描的协议"""
    try:
        protocols = api.protocols()
        print(json.dumps(protocols, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_query_search(args):
    """搜索已保存的查询"""
    try:
        results = api.queries(query=args.query)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_query_tags(args):
    """列出热门标签"""
    try:
        tags = api.query_tags(size=args.limit)
        print(json.dumps(tags, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_notifier_list(args):
    """列出通知器"""
    try:
        notifiers = api.notifiers()
        print(json.dumps(notifiers, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_exploit_search(args):
    """搜索漏洞利用代码"""
    try:
        results = api.exploits.search(args.query, limit=args.limit)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_filters(args):
    """列出常见搜索过滤器（速查）"""
    filters = {
        "通用": ["after", "before", "asn", "city", "country", "geo", "hash", "has_ipv6", "has_screenshot", "hostname", "ip", "isp", "net", "org", "os", "port", "postal", "product", "region", "state", "version", "vuln"],
        "HTTP": ["http.component", "http.component_category", "http.favicon.hash", "http.html", "http.html_hash", "http.robots_hash", "http.securitytxt", "http.status", "http.title", "http.waf"],
        "SSL/TLS": ["ssl", "ssl.alpn", "ssl.cert.alg", "ssl.cert.expired", "ssl.cert.extension", "ssl.cert.fingerprint", "ssl.cert.issuer.cn", "ssl.cert.pubkey.bits", "ssl.cert.serial", "ssl.cert.subject.cn", "ssl.chain_count", "ssl.cipher.bits", "ssl.cipher.name", "ssl.cipher.version", "ssl.ja3s", "ssl.jarm", "ssl.version"],
        "云服务": ["cloud.provider", "cloud.region", "cloud.service"],
        "Telnet": ["telnet.option", "telnet.do", "telnet.dont", "telnet.will", "telnet.wont"],
        "NTP": ["ntp.op_code"],
        "SSH": ["ssh.cipher", "ssh.fingerprint", "ssh.hassh", "ssh.kex", "ssh.mac", "ssh.type"],
        "截图": ["screenshot.label"]
    }
    print(json.dumps(filters, indent=2, ensure_ascii=False))


def cmd_datapedia(args):
    """列出 Banner 数据字段说明（数据字典）"""
    datapedia = {
        "ip_str": "IP 地址（字符串形式）",
        "port": "端口号",
        "transport": "传输协议（tcp/udp）",
        "data": "主 Banner 数据",
        "hostnames": "主机名列表",
        "domains": "域名列表",
        "location": {
            "city": "城市",
            "country_name": "国家名称",
            "country_code": "2位国家代码",
            "latitude": "纬度",
            "longitude": "经度"
        },
        "org": "组织机构名称",
        "isp": "互联网服务提供商",
        "asn": "自治系统编号",
        "os": "操作系统",
        "http": {
            "title": "网站标题",
            "html": "HTML 内容",
            "server": "服务器头信息",
            "status": "HTTP 状态码",
            "favicon": "Favicon 数据（哈希值、位置）"
        },
        "ssl": {
            "cert": "证书详情",
            "cipher": "加密套件详情",
            "versions": "支持的 SSL/TLS 版本"
        },
        "cpe": "通用平台枚举",
        "vulns": "漏洞列表（CVE 编号）"
    }
    print(json.dumps(datapedia, indent=2, ensure_ascii=False))


def cmd_stream(args):
    """实时数据流"""
    try:
        limit = args.limit if args.limit else 10
        count = 0

        if args.ports:
            stream = api.stream.ports(args.ports.split(','))
        elif args.alert:
            stream = api.stream.alert(args.alert)
        else:
            stream = api.stream.banners()

        print(f"[*] 正在接收 {limit} 条实时 Banner 数据...", file=sys.stderr)

        for banner in stream:
            print(json.dumps(banner, ensure_ascii=False))
            count += 1
            if count >= limit:
                break
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def cmd_trends(args):
    """趋势分析（基于 count + facets）"""
    try:
        results = api.count(args.query, facets=args.facets)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))


def main():
    parser = argparse.ArgumentParser(description="Shodan 搜索引擎技能 - CLI")
    subparsers = parser.add_subparsers(dest="command", help="要执行的命令")

    # 主机详情
    host_parser = subparsers.add_parser("host", help="查询主机详情")
    host_parser.add_argument("ip", help="IP 地址")
    host_parser.add_argument("--history", action="store_true", help="显示历史数据")
    host_parser.add_argument("--minify", action="store_true", help="精简响应")

    # 搜索
    search_parser = subparsers.add_parser("search", help="高级搜索")
    search_parser.add_argument("query", help="搜索查询语句")
    search_parser.add_argument("--limit", type=int, help="结果数量限制")
    search_parser.add_argument("--page", type=int, help="页码")
    search_parser.add_argument("--facets", help="统计维度（逗号分隔，例如 country,org）")

    # 计数
    count_parser = subparsers.add_parser("count", help="统计匹配结果数量（不消耗额度）")
    count_parser.add_argument("query", help="搜索查询语句")
    count_parser.add_argument("--facets", help="统计维度")

    # 实时流
    stream_parser = subparsers.add_parser("stream", help="实时数据流")
    stream_parser.add_argument("--ports", help="按端口过滤")
    stream_parser.add_argument("--alert", help="按告警 ID 过滤")
    stream_parser.add_argument("--limit", type=int, default=10, help="接收 N 条后停止")

    # 趋势分析（count + facets 的别名）
    trends_parser = subparsers.add_parser("trends", help="趋势分析（统计维度）")
    trends_parser.add_argument("query", help="搜索查询语句")
    trends_parser.add_argument("--facets", help="统计维度", default="country,org,os,product,port")

    # 扫描
    scan_parser = subparsers.add_parser("scan", help="按需扫描（消耗扫描额度）")
    scan_parser.add_argument("ips", help="IP 地址或 IP 列表/CIDR 网段")

    # 告警
    subparsers.add_parser("alert_list", help="列出所有告警")

    alert_create_parser = subparsers.add_parser("alert_create", help="创建告警")
    alert_create_parser.add_argument("name", help="告警名称")
    alert_create_parser.add_argument("ip", help="监控的 IP/CIDR 网段")

    alert_info_parser = subparsers.add_parser("alert_info", help="查看告警详情")
    alert_info_parser.add_argument("id", help="告警 ID")

    # DNS
    dns_domain_parser = subparsers.add_parser("dns_domain", help="域名信息查询")
    dns_domain_parser.add_argument("domain", help="域名")

    dns_resolve_parser = subparsers.add_parser("dns_resolve", help="域名解析")
    dns_resolve_parser.add_argument("hostnames", help="逗号分隔的主机名列表")

    # 账户与工具
    subparsers.add_parser("profile", help="获取账户信息")
    subparsers.add_parser("myip", help="获取本机公网 IP")
    subparsers.add_parser("ports", help="列出 Shodan 扫描的端口")
    subparsers.add_parser("protocols", help="列出 Shodan 扫描的协议")

    # 查询目录
    query_search_parser = subparsers.add_parser("query_search", help="搜索已保存的查询")
    query_search_parser.add_argument("query", help="搜索关键词")

    query_tags_parser = subparsers.add_parser("query_tags", help="列出热门标签")
    query_tags_parser.add_argument("--limit", type=int, default=10, help="标签数量")

    # 通知器
    subparsers.add_parser("notifier_list", help="列出通知器")

    # 漏洞搜索
    exploit_search_parser = subparsers.add_parser("exploit_search", help="搜索漏洞利用代码")
    exploit_search_parser.add_argument("query", help="搜索查询语句")
    exploit_search_parser.add_argument("--limit", type=int, default=10, help="结果限制")

    # 速查手册
    subparsers.add_parser("filters", help="列出常见搜索过滤器")
    subparsers.add_parser("datapedia", help="列出常见 Banner 字段说明")

    args = parser.parse_args()

    if args.command == "host":
        cmd_host(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "count":
        cmd_count(args)
    elif args.command == "stream":
        cmd_stream(args)
    elif args.command == "trends":
        cmd_trends(args)
    elif args.command == "scan":
        if ',' in args.ips:
            args.ips = args.ips.split(',')
        cmd_scan(args)
    elif args.command == "alert_list":
        cmd_alert_list(args)
    elif args.command == "alert_create":
        cmd_alert_create(args)
    elif args.command == "alert_info":
        cmd_alert_info(args)
    elif args.command == "dns_domain":
        cmd_dns_domain(args)
    elif args.command == "dns_resolve":
        cmd_dns_resolve(args)
    elif args.command == "profile":
        cmd_profile(args)
    elif args.command == "myip":
        cmd_myip(args)
    elif args.command == "ports":
        cmd_ports(args)
    elif args.command == "protocols":
        cmd_protocols(args)
    elif args.command == "query_search":
        cmd_query_search(args)
    elif args.command == "query_tags":
        cmd_query_tags(args)
    elif args.command == "notifier_list":
        cmd_notifier_list(args)
    elif args.command == "exploit_search":
        cmd_exploit_search(args)
    elif args.command == "filters":
        cmd_filters(args)
    elif args.command == "datapedia":
        cmd_datapedia(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()