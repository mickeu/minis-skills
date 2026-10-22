#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
surge-dump.py — 通过 surge-cli + Surge Controller 查看抓包请求的完整 header 与 body。

原理（2026-10-22 实测打通）：
  1. surge-cli feature set capture on         开启 HTTP 抓包（Replica）
  2. surge-cli --raw dump recent              每条记录含 requestHeader / responseHeader / URL / status /
                                               streamHasRequestBody / streamHasResponseBody 等完整字段
  3. retrieve-data <id> <request|response>    返回 "8字节小端长度 + CRLF + body" 的原始数据，
                                               官方 surge-cli 会因 json.loads 二进制而崩溃，这里直连 Controller 读取。

依赖环境变量（与 surge-cli 相同）：
  SURGE_CLI_REMOTE    Controller 地址，默认 127.0.0.1:6170
  SURGE_CLI_PASSWORD  Controller 密码

用法：
  surge-dump.py capture on [--time <秒>]        开启 HTTP 抓包（默认 600s 窗口）
  surge-dump.py capture off                       关闭抓包
  surge-dump.py status                            查看抓包/功能状态
  surge-dump.py list [--limit N] [--keyword <kw>] [--json]   列出最近抓包请求
  surge-dump.py show <id> [--no-body]             查看某请求完整 header + body（自动解 gzip）
  surge-dump.py body <id> <request|response> [-o <file>] [--decompress]  保存/输出原始 body
"""
import argparse
import gzip
import json
import os
import socket
import struct
import subprocess
import sys
import zlib
from datetime import datetime

REMOTE_DEFAULT = "127.0.0.1:6170"


def cli(args):
    """Run surge-cli and return its stdout text."""
    cmd = ["surge-cli"] + args
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"surge-cli {' '.join(args)} failed: {p.stderr.strip() or p.stdout.strip()}")
    return p.stdout


def cli_json(args):
    """Run surge-cli --raw and parse leading JSON object."""
    out = cli(["--raw"] + args)
    start = out.find("{")
    end = out.rfind("}")
    if start < 0 or end < 0:
        raise RuntimeError(f"no JSON in surge-cli output: {out[:300]}")
    return json.loads(out[start:end + 1])


# ---------- capture 控制 ----------

def capture_on(time_sec):
    cli(["set", f"ReplicaSessionParameters.timeLimit={int(time_sec)}"])
    res = cli_json(["feature", "set", "capture", "on"])
    print(f"capture: {'On' if res.get('enabled') else 'Off'}  (timeLimit={time_sec}s)")
    return 0 if res.get("enabled") else 1


def capture_off():
    res = cli_json(["feature", "set", "capture", "off"])
    print(f"capture: {'On' if res.get('enabled') else 'Off'}")
    return 0


def status():
    obj = cli_json(["feature", "list"])
    feats = obj.get("features", obj)
    if not isinstance(feats, dict):
        print(json.dumps(obj, ensure_ascii=False))
        return 0
    for k, v in feats.items():
        print(f"{k}: {'On' if v else 'Off'}")
    return 0


# ---------- 列表 ----------

def _fmt_time(ts):
    if not ts:
        return ""
    return datetime.fromtimestamp(ts).strftime("%H:%M:%S")


def _short(line, n=46):
    line = line.replace("\r\n", " ")
    return line if len(line) <= n else line[: n - 1] + "…"


def list_recent(limit, keyword, as_json):
    obj = cli_json(["dump", "recent"])
    reqs = obj.get("requests", [])
    if keyword:
        kw = keyword.lower()
        reqs = [r for r in reqs if kw in json.dumps(r, ensure_ascii=False).lower()]
    if limit:
        reqs = reqs[:limit]
    if as_json:
        print(json.dumps(reqs, ensure_ascii=False, indent=2))
        return 0
    if not reqs:
        print("(no captured requests)")
        return 0
    hdr = f"{'ID':<7} {'TIME':<9} {'METHOD':<7} {'STATUS':<14} {'POLICY':<28} {'URL'}"
    print(hdr)
    print("-" * len(hdr))
    for r in reqs:
        method = r.get("method", "") or ""
        status = r.get("status", "")
        url = _short(r.get("URL", ""))
        policy = r.get("policyName", "") or r.get("originalPolicyName", "")
        print(f"{r.get('id',''):<7} {_fmt_time(r.get('startDate')):<9} {method:<7} {status:<14} {_short(policy,26):<28} {url}")
    return 0


# ---------- body 获取（直连 Controller） ----------

def _controller_connect():
    remote = os.environ.get("SURGE_CLI_REMOTE", REMOTE_DEFAULT)
    password = os.environ.get("SURGE_CLI_PASSWORD", "")
    if not password:
        raise RuntimeError("SURGE_CLI_PASSWORD not set")
    host, _, port_s = remote.rpartition(":")
    s = socket.create_connection((host, int(port_s)), timeout=15)
    s.settimeout(30)
    fp = s.makefile("rwb", buffering=0)
    fp.write(password.encode() + b"\r\n")
    welcome = fp.readline()
    if b"Welcome" not in welcome:
        s.close()
        raise RuntimeError(f"controller auth failed: {welcome!r}")
    return s, fp


def retrieve_raw(record_id, which):
    """Return raw bytes from retrieve-data (length-prefixed format)."""
    s, fp = _controller_connect()
    try:
        fp.write(f'retrieve-data "{record_id}" {which}\r\n'.encode())
        chunks = []
        while True:
            try:
                b = s.recv(65536)
            except socket.timeout:
                break
            if not b:
                break
            chunks.append(b)
        data = b"".join(chunks)
    finally:
        try:
            s.close()
        except OSError:
            pass
    return data


def parse_body(raw):
    """Strip the 8-byte little-endian length + CRLF prefix."""
    if len(raw) >= 10 and raw[8:10] == b"\r\n":
        length = struct.unpack("<Q", raw[:8])[0]
        return raw[10:10 + length]
    return raw


def decode_body(body, content_encoding):
    enc = (content_encoding or "").strip().lower()
    if enc in ("gzip", "x-gzip") and body[:2] == b"\x1f\x8b":
        return gzip.decompress(body)
    if enc in ("deflate",):
        try:
            return zlib.decompress(body)
        except zlib.error:
            return zlib.decompress(body, -zlib.MAX_WBITS)
    return body


def _content_encoding(headers_text):
    for line in (headers_text or "").split("\r\n"):
        if line.lower().startswith("content-encoding:"):
            return line.split(":", 1)[1].strip()
    return ""


# ---------- 查看单条 ----------

def show_record(record_id, no_body):
    reqs = cli_json(["dump", "recent"]).get("requests", [])
    rec = next((r for r in reqs if r.get("id") == int(record_id)), None)
    if rec is None:
        print(f"[warn] id {record_id} 不在 recent 中（可能已滚动出缓存），仅能取 body。", file=sys.stderr)
    else:
        print(f"ID       : {rec.get('id')}")
        print(f"URL      : {rec.get('URL')}")
        print(f"Method   : {rec.get('method')}   Status: {rec.get('status')}   Failed: {rec.get('failed')}")
        print(f"Policy   : {rec.get('policyName')}  (orig: {rec.get('originalPolicyName')})")
        print(f"Rule     : {rec.get('rule')}   Remote: {rec.get('remoteAddress')}")
        print(f"Time     : {_fmt_time(rec.get('startDate'))} -> {_fmt_time(rec.get('completedDate'))}")
        print(f"Bytes    : in={rec.get('inBytes')} out={rec.get('outBytes')}")
        rh = rec.get("requestHeader", "")
        resph = rec.get("responseHeader", "")
        has_req_body = rec.get("streamHasRequestBody")
        has_resp_body = rec.get("streamHasResponseBody")
        print()
        print("===== REQUEST HEADER =====")
        print(rh or "(empty)")
        if has_req_body and not no_body:
            raw = retrieve_raw(record_id, "request")
            body = parse_body(raw)
            print("\n----- REQUEST BODY -----")
            print(_preview(decode_body(body, _content_encoding(rh))))
        elif not no_body:
            print("\n(no request body)")
        print()
        print("===== RESPONSE HEADER =====")
        print(resph or "(empty)")
        if has_resp_body and not no_body:
            raw = retrieve_raw(record_id, "response")
            body = parse_body(raw)
            print("\n----- RESPONSE BODY -----")
            print(_preview(decode_body(body, _content_encoding(resph))))
        elif not no_body:
            print("\n(no response body)")
        # 连接详情
        notes = rec.get("notes") or []
        if notes:
            print("\n----- CONNECTION NOTES -----")
            for n in notes:
                print(" ", n)
    return 0


def _preview(data):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return f"(binary, {len(data)} bytes) hex head: {data[:64].hex()}"
    if len(text) > 8000:
        return text[:8000] + f"\n... (truncated, total {len(text)} chars)"
    return text


def body_cmd(record_id, which, out, decompress):
    raw = retrieve_raw(record_id, which)
    body = parse_body(raw)
    if decompress:
        # 需要 header 判断编码；从 recent 找记录
        enc = ""
        try:
            reqs = cli_json(["dump", "recent"]).get("requests", [])
            rec = next((r for r in reqs if r.get("id") == int(record_id)), None)
            if rec:
                hdr = rec.get("responseHeader") if which == "response" else rec.get("requestHeader")
                enc = _content_encoding(hdr)
        except Exception:
            pass
        try:
            body = decode_body(body, enc)
        except Exception as e:
            print(f"[warn] decompress failed: {e}", file=sys.stderr)
    if out:
        with open(out, "wb") as f:
            f.write(body)
        print(f"{len(body)} bytes -> {out}")
    else:
        sys.stdout.buffer.write(body)
        sys.stdout.buffer.flush()
    return 0


# ---------- 主入口 ----------

def main():
    ap = argparse.ArgumentParser(description="Surge 抓包 header/body 查看器", prog="surge-dump.py")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("capture", help="控制 HTTP 抓包")
    p.add_argument("action", choices=["on", "off"])
    p.add_argument("--time", type=int, default=600, help="抓包窗口秒数（默认600）")
    p.set_defaults(fn=lambda a: capture_on(a.time) if a.action == "on" else capture_off())

    p = sub.add_parser("status", help="查看抓包状态")
    p.set_defaults(fn=lambda a: status())

    p = sub.add_parser("list", help="列出最近抓包请求")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--keyword", default=None)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=lambda a: list_recent(a.limit, a.keyword, a.json))

    p = sub.add_parser("show", help="查看单条完整 header + body")
    p.add_argument("id", type=int)
    p.add_argument("--no-body", action="store_true")
    p.set_defaults(fn=lambda a: show_record(a.id, a.no_body))

    p = sub.add_parser("body", help="保存/输出原始 body")
    p.add_argument("id", type=int)
    p.add_argument("which", choices=["request", "response"])
    p.add_argument("-o", "--out", default=None)
    p.add_argument("--decompress", action="store_true")
    p.set_defaults(fn=lambda a: body_cmd(a.id, a.which, a.out, a.decompress))

    args = ap.parse_args()
    try:
        return args.fn(args)
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())