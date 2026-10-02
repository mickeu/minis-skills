#!/usr/bin/env python3
"""音频识曲：走 Shazam 公开 API（免费、无需 key）。

用法: python3 identify.py <audio.mp3|mp4a|wav|aac> [shazam_id]

流程: ffmpeg 转 16kHz mono raw PCM -> pydub from_raw -> shazamio 签名 ->
      send_recognize_request 拿 id -> curl Shazam 网页 JSON-LD 拿歌名。

绕开了两个坑:
  1) pydub from_file 调 ffprobe 会炸（ffprobe 在此环境坏） -> 用 from_raw + BytesIO
  2) ffmpeg 写 raw PCM 必须带 -f s16le，否则 0 字节
"""
import asyncio, json, subprocess, sys, traceback, urllib.request, re, html
from io import BytesIO

def get_pcm(src: str, out: str = "/tmp/_mid_pcm.pcm") -> str:
    r = subprocess.run(
        ["ffmpeg", "-y", "-i", src, "-ar", "16000", "-ac", "1",
         "-c:a", "pcm_s16le", "-f", "s16le", out],
        capture_output=True, text=True)
    if r.returncode != 0 or __import__("os").path.getsize(out) == 0:
        raise RuntimeError("ffmpeg 失败: " + (r.stderr or "")[-400:])
    return out


async def recognize(src: str):
    from pydub import AudioSegment
    from shazamio.api import Shazam

    pcm = get_pcm(src)
    raw = open(pcm, "rb").read()
    print(f"# PCM {len(raw)} bytes -> {len(raw)/(16000*2):.2f}s", file=sys.stderr)

    seg = AudioSegment.from_raw(BytesIO(raw), sample_width=2,
                                frame_rate=16000, channels=1)

    shazam = Shazam()
    seg = Shazam.normalize_audio_data(seg)
    sg = Shazam.create_signature_generator(seg)
    sig = sg.get_next_signature()
    if len(sg.input_pending_processing) < 128:
        return None
    while not sig:
        sig = sg.get_next_signature()
    res = await shazam.send_recognize_request(sig)
    matches = res.get("matches", [])
    if not matches:
        return None
    m = matches[0]
    print(f"# match_count={len(matches)} id={m['id']} offset={m['offset']:.2f}s", file=sys.stderr)
    return m["id"]


def song_info(track_id: str):
    """Shazam 网页 JSON-LD，拿歌名/歌手/专辑。API 的 track_about 404，用网页。"""
    url = f"https://www.shazam.com/track/{track_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    s = html.unescape(urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace"))
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', s, re.S):
        try:
            d = json.loads(m.group(1))
        except Exception:
            continue
        if isinstance(d, dict) and d.get("name"):
            out = {
                "song": d.get("name"),
                "artist": d.get("byArtist"),
                "genre": d.get("genre"),
                "duration": d.get("duration"),
                "album": d.get("inAlbum", {}).get("name") if isinstance(d.get("inAlbum"), dict) else None,
                "shazam_listing_date": d.get("datePublished"),  # 收录日，非发行日
            }
            return out
    return None


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/song.mp3"
    tid = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        tid = tid or asyncio.run(recognize(src))
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    if not tid:
        print("NO MATCH — Shazam 库里没有这首")
        sys.exit(0)
    info = song_info(tid)
    print(json.dumps(info or {"shazam_id": tid}, ensure_ascii=False, indent=2))
