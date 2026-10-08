---
name: music-identify 音频识曲
description: 音频识曲工具——调用 Shazam 公开免费 API 识别 MP3/M4A/AAC/WAV 音频的歌曲信息，无需注册或 API key，含实测踩坑记录。
---
# music-identify — 音频识曲（Shazam 免费 API，无需 key）

拿到一段音频（MP3/M4A/AAC/WAV）想知道是什么歌，用这个。走 Shazam 公开 API，库最大、免费、不需要注册或 API key。

## 什么时候用
- 用户发来音频文件问「什么歌」「这是什么曲子」
- 音频**没有元数据标签**（iTunes/Apple Music 30 秒试听预览通常就是这样）
- 不要用 SFSpeech（`apple-speech`）先尝试转歌词——**如果歌是非中/英文（西班牙语等），设备没装对应识别器，会返回极低置信度垃圾**，白费轮次。

## 关键坑（全部实测踩过的）
1. **先 `apk add py3-numpy`**，再 `pip install --only-binary=:all: --no-cache-dir shazamio`。不先装 numpy，pip 会去编译、超时挂掉。
   装完 `pip list | grep shazam` 能看到 `shazamio 0.4.0.1`。pip 末尾报 `InvalidVersion: 'python-4.10.0'` 是 pip 自己的 bug，**不影响安装**，忽略。
2. **ffprobe 在这个 iSH/Alpine 环境上是坏的**：对某些 M4A 一律 exit 256 / 空 JSON，而 `ffmpeg` 转码完全正常。所以 **pydub 的 `AudioSegment.from_file()` 会炸**（它调 mediainfo_json → ffprobe，报 `JSONDecodeError`）。
   绕法：**自己用 ffmpeg 转 raw PCM，再用 `from_raw`**，pydub 就不碰 ffprobe 了。
3. **ffmpeg 写 raw PCM 必须带 `-f s16le`**。只写 `-c:a pcm_s16le` 会 rc=234 且产出 0 字节。
4. **`AudioSegment.from_raw()` 这个 pydub 版本要 `BytesIO`，不能直接传 `bytes`**（传 bytes 报 `'bytes' object has no attribute 'read'`）。
5. **shazamio 0.4.0.1 的方法名是 `recognize_song(data)`，不是 `recognize`**（老版本 API 不同）。
6. **`send_recognize_request` 只返回 `{id, offset, timeskew, frequencyskew}`，没有歌名**。
7. **`shazam.track_about(id)` 会 404**（`text/html` 而非 JSON），是地域限制。**改用网页**：`https://www.shazam.com/track/<id>`，`curl -s -4 --http1.1` 抓下来，页面里的 **JSON-LD `<script type="application/ld+json">`** 有 `name` / `byArtist` / `genre` / `duration` / `inAlbum`。
8. 注意区分：JSON-LD 的 `datePublished` 是 **Shazam 收录日期，不是歌曲发行日期**，别当发行年用。

## 跑法
```bash
# 1. 依赖（多数持久，跑一次即可）
apk add py3-numpy
pip install --only-binary=:all: --no-cache-dir shazamio

# 2. 识别（脚本见同目录 identify.py，改 SRC 路径即可）
python3 identify.py "/path/to/audio.mp3"

# 3. 查歌名（拿到 id 后）
curl -s -4 --http1.1 -A "Mozilla/5.0" "https://www.shazam.com/track/<ID>" | grep -oE '<title>[^<]*</title>'
```

## 判定语言（省事办法）
如果 SFSpeech 中文和英文都返回低置信度碎片，**先怀疑是非中英文歌**，直接跳去 Shazam 指纹，别在转写上耗轮次。
`apple-speech transcribe --language <locale>` 对设备上没装的识别器返回 `User denied access to speech recognition`（错误码 `internal_error`），可用来探测哪些语言可用。

## 免费指纹库的坑
- **audd.io**（`POST https://api.audd.io/ -F file=@x.mp3`，无需 key）用 **AudD 自己的小库**，返回 `{"status":"success","result":null}` = 它库里没有，**不代表歌不存在**，别用它下结论。
- **chromaprint `fpcalc`**：`apk add chromaprint` 能装上（1.5.1），但**这个环境里对 raw/WAV/MP3 全部静默 exit 1、零输出**，二进制是坏的，别浪费时间。而且 AcoustID 查询还要 app key。
- **Shazam 库最大，但会误报**，见下一节的验证方法。

## ⚠️ Shazam 会误报——必须做音频验证
实测案例：用户 30s 片段，Shazam 返回 `match_count=1` = DtMF by Bad Bunny。这是**误报**。真歌是爱妃驾到《踏遍青山（心里亮堂）》。

误报信号（本例全中）：
- `matches` 数组里没有 score/confidence 字段，只有 `id` + `offset`
- `timeskew`/`frequencyskew` 都接近 0（0.00006 量级）—— 真匹配也不该这么"完美"
- 用户听后说对不上

**验证方法（唯一可靠）**：拿到候选的**完整曲**，把用户片段在完整曲上滑动做归一化互相关。峰值 ≥0.9 = 确认；0.05 上下 = 不相关。

```bash
# 网易云搜索（无需登录）
curl -sL -A "$UA" -H "Referer: https://music.163.com/" \
  "http://music.163.com/api/search/get/web?s=KEY&type=1&offset=0&total=true&limit=20"
# 下载完整曲（非 VIP 免费曲可用）
curl -sL -A "$UA" -H "Referer: https://music.163.com/" \
  "http://music.163.com/song/media/outer/url?id=<trackId>.mp3" -o full.mp3
```
互相关要用**滑动窗口**（片段 30s 扫完整曲 200s），别只取两者前半段。实现要点：clip 归一到单位 RMS，FFT 全长求 xcorr，用 cumsum 算曲子窗口能量做逐点归一化。自检标准：自相关（加静音偏移）应 ≈0.95，完全对齐应 =1.0 —— **没做自检就下结论是耍流氓**。

**锁定原作**：同一首歌在网易云/iTunes 有很多版本（Cover/DJ 版/烟嗓版），**比 `duration`(ms)** 能直接对上原作（本例网易云爱妃驾到版与 iTunes 均为 211320ms）。

## 搜歌词找候选（比指纹更靠谱的前置步骤）
- **SFSpeech 转写碎片当线索**：本例中文转写出 `岁月`(0.29)，正好命中歌词「岁月不老步子铿锵」
- **YouTube 视频标题里常直接写歌词原文**（`curl -A <UA> -b "CONSENT=YES+1" "https://www.youtube.com/results?search_query=KEY"`，注意是 `\x22` 转义 + `videoWithContextRenderer` + 斜杠 `\/` 也要反转义）
- **Baidu 能搜出歌词片段和专辑/演唱者归属**（`www.baidu.com/s?wd=KEY`）；Google 和 Bing 在这个环境返回空页
- **yt-dlp 下载 YouTube 会被 403**（即使装了 deno JS runtime），别指望
- 酷我 `search.kuwo.cn/r.s` 现在返回空结果；B 站搜索要 WBI 签名

## 返回结果解读
`offset` = 命中点在音频里的秒数（例：offset 16.77 表示片段第 16.77 秒处的特征匹配上了）。30 秒试听预览里命中点靠后很正常，因为预览开头可能还不是 hook。

**iTunes 30s 试听互相关低 ≠ 不是同一首**：试听和用户的 30s 片段可能覆盖歌曲的不同 30 秒。本例 DtMF 试听、以及 42 首 iTunes 候选试听全部 corr<0.07，但其中 1 首（真歌的爱妃驾到版）是唯一用完整曲验证通过的。**必须拿完整曲验证。**
