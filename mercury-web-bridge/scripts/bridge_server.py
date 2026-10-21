#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mercury 网页版桥接服务（本地 OpenAI 兼容端点）
=============================================
原理：
  chat.inceptionlabs.ai 有 Vercel Security Checkpoint，只放行真实浏览器。
  Minis 内置浏览器是能通过挑战的客户端。
  本服务收到 OpenAI 格式 /v1/chat/completions 请求后，
  通过 `minis-browser-use execute_js` 驱动一个专用的内置浏览器 tab
  调用网页版 /api/chat，把 SSE 流解析成文本，再以 OpenAI 兼容格式返回。

用法：
  python3 bridge_server.py [port]    默认端口 18080，监听 0.0.0.0
  测试：curl -X POST http://127.0.0.1:18080/v1/chat/completions \
        -H 'Content-Type: application/json' \
        -d '{"model":"mercury-3","messages":[{"role":"user","content":"你好"}]}'

依赖：minis-browser-use 命令（Minis 内置）
"""
import json
import re
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BASE_URL = "https://chat.inceptionlabs.ai"
HOST = "0.0.0.0"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 18080
LOCK = threading.Lock()
BRIDGE_TAB_ID = [None]  # 专用浏览器 tab

MODEL_ALIASES = {
    "mercury-3": "mercury-3",
    "mercury": "mercury-3",
    "mercury-chat": "mercury-3",
}


def run_shell(cmd, timeout=120):
    """执行 shell 命令，返回 stdout"""
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return p.stdout, p.stderr, p.returncode


def _extract_tab_id(text):
    m = re.search(r"tab_id[:=]?\s*(\d+)", text)
    return int(m.group(1)) if m else None


def ensure_bridge_tab():
    """查找或创建保持在 chat.inceptionlabs.ai 的专用 tab，返回其 id"""
    if BRIDGE_TAB_ID[0] is not None:
        return BRIDGE_TAB_ID[0]
    out, _, _ = run_shell("minis-browser-use list_tabs")
    try:
        env = json.loads(out)
        text = env.get("data", {}).get("text", "") or out
    except Exception:
        text = out
    m = re.search(r"Tab (\d+):[^\n]*chat\.inceptionlabs\.ai", text)
    if m:
        BRIDGE_TAB_ID[0] = int(m.group(1))
    else:
        out2, _, _ = run_shell(f"minis-browser-use new_tab --url {BASE_URL}/")
        tid = _extract_tab_id(out2)
        if tid is None:
            raise RuntimeError(f"无法创建专用浏览器 tab: {out2}")
        BRIDGE_TAB_ID[0] = tid
    return BRIDGE_TAB_ID[0]


def build_bridge_js(messages, reasoning_effort="low", web_search=False):
    """构造要注入浏览器的 JS，把 OpenAI messages 转成网页版 parts 格式"""
    parts_messages = []
    for m in messages:
        role = m.get("role", "user")
        content = m.get("content") or ""
        if isinstance(content, list):
            text_parts = [p for p in content if p.get("type") == "text"]
            content = " ".join(p.get("text", "") for p in text_parts) if text_parts else ""
        parts_messages.append({
            "role": role,
            "parts": [{"type": "text", "text": content}],
            "id": "msg-" + uuid.uuid4().hex[:10],
        })

    payload = {
        "reasoningEffort": reasoning_effort,
        "webSearchEnabled": bool(web_search),
        "voiceMode": False,
        "timezone": "Asia/Shanghai",
        "language": "zh-CN",
        "id": "bridge-" + uuid.uuid4().hex[:12],
        "messages": parts_messages,
        "trigger": "submit-message",
    }

    js = r"""
const payload = __PAYLOAD__;
const sr = await fetch('/api/session', {credentials:'include'});
const sj = await sr.json();
const resp = await fetch('/api/chat', {
  method:'POST',
  headers:{'Content-Type':'application/json','x-session-token':sj.token},
  body: JSON.stringify(payload)
});
const text = await resp.text();
if(resp.status !== 200){
  return JSON.stringify({ok: false, status: resp.status, body: text.slice(0,600)});
}
let answer='';
let reasoning='';
for (const line of text.split('\n')) {
  if(!line.startsWith('data: ')) continue;
  const data = line.slice(6);
  if(data === '[DONE]') continue;
  try{
    const o = JSON.parse(data);
    if(o.type === 'text-delta' && o.delta) answer += o.delta;
    if(o.type === 'reasoning-delta' && o.delta) reasoning += o.delta;
  }catch(e){}
}
return JSON.stringify({ok: true, status: resp.status, reasoning: reasoning, answer: answer});
"""
    return js.replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))


def call_mercury(messages, reasoning_effort="low", web_search=False):
    """核心桥接：驱动专用浏览器 tab 调用网页版 API，返回回答文本"""
    with LOCK:
        tab_id = ensure_bridge_tab()
        js = build_bridge_js(messages, reasoning_effort, web_search)
        script_path = "/tmp/mercury_bridge_latest.js"
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(js)
        cmd = f'minis-browser-use execute_js --tab-id {tab_id} --script "$(cat {script_path})"'
        out, err, rc = run_shell(cmd, timeout=120)
        sys.stderr.write(f"[bridge] tab_id={tab_id} rc={rc}\n[bridge] out={out[:600]}\n")
        if rc != 0:
            raise RuntimeError(f"execute_js 失败: {err[:500]}")
        try:
            env = json.loads(out)
            text = env.get("data", {}).get("text", "")
            if not text:
                raise RuntimeError(f"execute_js 无返回: {out[:500]}")
            return json.JSONDecoder().raw_decode(text.strip())[0]
        except json.JSONDecodeError:
            raise RuntimeError(f"无法解析 execute_js 输出: {out[:800]}")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s\n" % (fmt % args))

    def _send(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_POST(self):
        if self.path.rstrip("/") not in ("/v1/chat/completions", "/chat/completions"):
            self._send(404, {"error": {"message": "Not Found", "type": "invalid_request_error"}})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length) if length else b""
            req = json.loads(raw.decode("utf-8")) if raw else {}
        except Exception as e:
            self._send(400, {"error": {"message": f"Bad JSON: {e}", "type": "invalid_request_error"}})
            return

        model = req.get("model", "mercury-3")
        messages = req.get("messages", [])
        reasoning = req.get("reasoning_effort", req.get("reasoningEffort", "low"))
        web_search = bool(req.get("web_search", req.get("webSearchEnabled", False)))
        if reasoning not in ("instant", "low", "medium", "high"):
            reasoning = "low"

        try:
            result = call_mercury(messages, reasoning_effort=reasoning, web_search=web_search)
            if not result.get("ok"):
                raise RuntimeError(f"桥接返回异常: {json.dumps(result, ensure_ascii=False)[:600]}")
        except Exception as e:
            self._send(502, {"error": {"message": f"Bridge failed: {e}", "type": "server_error"}})
            return

        answer = result.get("answer", "")
        completion = {
            "id": "chatcmpl-" + uuid.uuid4().hex[:16],
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model,
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": answer},
                "finish_reason": "stop",
            }],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": max(1, len(answer) // 4),
                "total_tokens": max(1, len(answer) // 4),
            },
        }
        self._send(200, completion)

    def do_GET(self):
        self._send(200, {
            "status": "ok",
            "service": "mercury-web-bridge",
            "note": "POST /v1/chat/completions (OpenAI compatible)",
        })


def main():
    try:
        ensure_bridge_tab()
    except Exception as e:
        print(f"警告：无法初始化浏览器 tab：{e}", file=sys.stderr)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Mercury 网页版桥接服务运行中: http://{HOST}:{PORT}/v1/chat/completions")
    server.serve_forever()


if __name__ == "__main__":
    main()