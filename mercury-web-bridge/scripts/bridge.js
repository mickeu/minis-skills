// 桥接测试：从 shell 通过 execute_js 调用网页版 /api/chat
const sr = await fetch('/api/session', {credentials:'include'});
const sj = await sr.json();
const resp = await fetch('/api/chat', {
  method: 'POST',
  headers: {'Content-Type': 'application/json', 'x-session-token': sj.token},
  body: JSON.stringify({
    reasoningEffort: 'low', webSearchEnabled: false, voiceMode: false,
    timezone: 'Asia/Shanghai', language: 'zh-CN',
    id: 'bridge-shell-' + Date.now(),
    messages: [{role: 'user', parts: [{type: 'text', text: '回复两个字：好的'}], id: 'm1'}],
    trigger: 'submit-message'
  })
});
const text = await resp.text();
let answer = '';
for (const line of text.split('\n')) {
  if (!line.startsWith('data: ')) continue;
  const data = line.slice(6);
  if (data === '[DONE]') continue;
  try { const o = JSON.parse(data); if (o.type === 'text-delta' && o.delta) answer += o.delta; } catch (e) {}
}
return JSON.stringify({ok: true, status: resp.status, answer: answer});