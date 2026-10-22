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
    """确保存在一个保持在 chat.inceptionlabs.ai 的专用 tab，返回其 id。
    每次调用都会重新检查，若 tab 被关闭或被导航走则自动恢复。"""
    out, _, _ = run_shell("minis-browser-use list_tabs")
    try:
        env = json.loads(out)
        text = env.get("data", {}).get("text", "") or out
    except Exception:
        text = out
    # 1) 优先复用任意已在 chat.inceptionlabs.ai 的 tab
    m = re.search(r"Tab (\d+):[^\n]*chat\.inceptionlabs\.ai", text)
    if m:
        BRIDGE_TAB_ID[0] = int(m.group(1))
        return BRIDGE_TAB_ID[0]
    # 2) 若缓存 tab 还在但被导航走了，把它导航回 chat 页
    if BRIDGE_TAB_ID[0] is not None:
        m2 = re.search(rf"Tab {BRIDGE_TAB_ID[0]}:", text)
        if m2:
            run_shell(f"minis-browser-use navigate --tab-id {BRIDGE_TAB_ID[0]} --url {BASE_URL}/")
            return BRIDGE_TAB_ID[0]
    # 3) 缓存失效，新建专用 tab
    out2, _, _ = run_shell(f"minis-browser-use new_tab --url {BASE_URL}/")
    tid = _extract_tab_id(out2)
    if tid is None:
        raise RuntimeError(f"无法创建专用浏览器 tab: {out2}")
    BRIDGE_TAB_ID[0] = tid
    return BRIDGE_TAB_ID[0]


MAX_JS_LEN = 90000  # 安全阈值，远小于 iSH 的 ARG_MAX(128KB)


def _normalize_content(content, max_chars):
    """把 OpenAI content（字符串或 parts 数组）转成纯文本，并限长"""
    if isinstance(content, list):
        text_parts = [p for p in content if p.get("type") == "text"]
        content = " ".join(p.get("text", "") for p in text_parts) if text_parts else ""
    content = str(content or "")
    if len(content) > max_chars:
        return content[:max_chars] + "\n…[已截断]"
    return content


def build_bridge_js(messages, reasoning_effort="low", web_search=False, max_len=MAX_JS_LEN):
    """构造要注入浏览器的 JS。
    若消息过长，自动截断（保留最近若干条 + 限制每条长度 + 逐步压缩），
    避免命令行参数超过 iSH 的 ARG_MAX(128KB) 导致 'Argument list too long'。"""

    def build(max_msgs, max_chars):
        msgs = messages[-max_msgs:] if max_msgs < len(messages) else messages
        parts_messages = []
        for m in msgs:
            role = m.get("role", "user")
            # 网页版 /api/chat 只接受 user/assistant 角色，其他角色（system/developer/tool）
            # 会导致网页版后端返回 500。统一映射为 user，避免报错。
            if role not in ("user", "assistant"):
                role = "user"
            content = _normalize_content(m.get("content"), max_chars)
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
        return payload

    template = r"""
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

    # 从宽松到严格逐步压缩，确保最终 JS 长度不超过 max_len
    for max_msgs in [15, 10, 8, 6, 4, 3, 2, 1]:
        for max_chars in [8000, 6000, 4000, 2500, 1500, 800, 400, 200]:
            payload = build(max_msgs, max_chars)
            js = template.replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))
            if len(js) <= max_len:
                return js
    # 极端兜底：只保留最后一条用户消息，限很短
    payload = build(1, 150)
    return template.replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False))


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

    def _send_stream(self, completion):
        """以 OpenAI 兼容 SSE 流式格式发送回答"""
        content = completion["choices"][0]["message"]["content"]
        cid = completion["id"]
        created = completion["created"]
        model = completion["model"]
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()

        def emit(obj):
            self.wfile.write(f"data: {json.dumps(obj, ensure_ascii=False)}\n\n".encode("utf-8"))
            self.wfile.flush()

        emit({"id": cid, "object": "chat.completion.chunk", "created": created, "model": model,
              "choices": [{"index": 0, "delta": {"role": "assistant"}, "finish_reason": None}]})
        step = 20
        for i in range(0, len(content), step):
            emit({"id": cid, "object": "chat.completion.chunk", "created": created, "model": model,
                  "choices": [{"index": 0, "delta": {"content": content[i:i + step]}, "finish_reason": None}]})
        emit({"id": cid, "object": "chat.completion.chunk", "created": created, "model": model,
              "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]})
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()
        # 流结束，关闭连接，避免客户端一直等待导致“卡住”
        self.close_connection = True

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
        stream = bool(req.get("stream", False))
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
        # 估算输入 token（网页版不返回真实 usage，按字符数/4 估算，让 Minis 用量面板能统计）
        prompt_chars = 0
        for m in messages:
            c = m.get("content", "")
            if isinstance(c, str):
                prompt_chars += len(c)
            elif isinstance(c, list):
                prompt_chars += sum(len(p.get("text", "")) for p in c if isinstance(p, dict))
        prompt_tokens = max(1, prompt_chars // 4)
        completion_tokens = max(1, len(answer) // 4)
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
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
                "prompt_tokens_details": {"cached_tokens": 0},
                "completion_tokens_details": {"reasoning_tokens": 0},
            },
        }
        if stream:
            self._send_stream(completion)
        else:
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