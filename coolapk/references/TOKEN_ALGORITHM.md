# Token 计算方式

本文档对应当前仓库 [coolapk_token.py](../coolapk_token.py) 的实现，说明 `X-App-Token` 的计算流程。

## 1. 输入参数

- `apk_path`: `coolapk.apk` 路径
- `device`: `X-App-Device`
- `ts`: 秒级 Unix 时间戳
- `version_code`: 例如 `2602111`
- `package`: 例如 `com.coolapk.market`

输出：`X-App-Token`，格式为 `v3...`

## 2. 常量

- 标准 Base64 字典：
  `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`
- `xor` 常量：`0x5A`
- bcrypt cost：`10`

## 3. 计算步骤（逐步）

1. 从 APK 读取 `lib/arm64-v8a/libauth.so`
2. 在 `libauth.so` 中匹配长度 >= 1000 的 base64 文本候选
3. 对每个候选尝试 base64 解码，再逐字节 `xor 0x5A`
4. 用“可打印字符比例最高”选择目标 blob
5. `phase1 = base64_decode(blob)`
6. `phase2 = xor_each_byte(phase1, 0x5A)`
7. 计算索引：
   `idx = ((ts + version_code) % 100) * 4 + 0x80`
8. 取切片：
   `chunk = phase2[idx : idx + 0x80]`
9. 再解码：
   `segment = base64_decode(chunk)`
10. 计算 `md5_device = md5(device).hexdigest()`
11. 组装原文（字节拼接）：
    `plain = package + "&" + segment + "&" + md5_device + "&" + ts + "&" + version_code`
12. 计算密码串：
    `pw = md5(base64(plain)).hexdigest()`
13. 计算盐来源：
    `salt_src = base64(f"{ts:x}/{md5(plain).hexdigest()}").rstrip("=")`
14. 取前 22 位后处理最后 1 位：
    - `salt22 = salt_src[:22]`
    - 把 `salt22` 最后一位在标准 base64 字典中向前偏移 5 位（模 64）
15. 组装 bcrypt setting：
    `setting = "$2y$10$" + salt22`
16. bcrypt：
    `hashed = bcrypt.hashpw(pw, setting)`
17. 最终 token：
    `token = "v3" + base64(hashed).rstrip("=")`

## 4. 伪代码

```text
libauth = read(apk, "lib/arm64-v8a/libauth.so")
blob = best_base64_blob(libauth)
phase1 = b64decode(blob)
phase2 = xor_bytes(phase1, 0x5A)
idx = ((ts + version_code) % 100) * 4 + 0x80
segment = b64decode(phase2[idx:idx+0x80])
plain = package + "&" + segment + "&" + md5(device) + "&" + ts + "&" + version_code
pw = md5(b64(plain))
salt_src = b64(hex(ts) + "/" + md5(plain)).rstrip("=")
salt22 = shift_last_char_minus_5(salt_src[:22])
bcrypt_str = bcrypt(pw, "$2y$10$" + salt22)
token = "v3" + b64(bcrypt_str).rstrip("=")
```

## 5. `Invalid salt` 问题

在 Python `bcrypt` 实现中，某些盐会触发 `Invalid salt`。仓库中的请求脚本通过 `--max-ahead` 做时间戳前探（默认 `+0..+10s`），找到可用盐后继续请求。

涉及脚本：

- [coolapk_poll.py](../coolapk_poll.py)
- [coolapk_latest_posts.py](../coolapk_latest_posts.py)
- [coolapk_feed_detail.py](../coolapk_feed_detail.py)
- [coolapk_feed_replies.py](../coolapk_feed_replies.py)
- [coolapk_last_hour_report.py](../coolapk_last_hour_report.py)

## 6. 升级版本时要复核的点

1. `version_code` 和 `app_version`
2. `libauth.so` 中可用 blob 是否变化
3. `idx` 公式是否变化
4. 盐处理是否变化（尤其最后一位偏移逻辑）
5. 请求头字段是否新增/调整
