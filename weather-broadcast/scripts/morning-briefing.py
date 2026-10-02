#!/usr/bin/env python3
"""天气播报 V7 — Apple Weather 主源 + 人性化文案 + 豆包TTS
============================================
数据源：apple-weather（和风天气+中国气象局，对县级城市准确）
备选：腾讯天气（wis.qq.com）
TTS：edge-tts 晓晓 → 豆包TTS（不用 apple-speak）
BGM：低音量播报，播完后音乐恢复原声
"""

import json, subprocess, sys, os, time, urllib.request, urllib.parse
from datetime import datetime, timedelta
from lunardate import LunarDate

# ── 路径 ──
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = f"{SKILL_DIR}/assets"
BGM = None
for alt_bgm in [
    f"{ASSETS}/清歌漫谷.mp3",
    "/var/minis/skills/weather-broadcast/assets/清歌漫谷.mp3",
    f"{ASSETS}/birds.mp3",
    "/var/minis/skills/weather-broadcast/assets/birds.mp3",
    "/var/minis/shared/weather-broadcast/birds.mp3",
]:
    if os.path.exists(alt_bgm):
        BGM = alt_bgm
        break
SHARED = "/var/minis/shared/weather-broadcast"
TS = datetime.now().strftime("%Y%m%d-%H%M%S")
os.makedirs(SHARED, exist_ok=True)

# ── 防重复锁（进程锁 + 时间锁） ──
LOCK = "/tmp/weather-broadcast.lock"
DEDUP = "/tmp/weather-broadcast.last"  # 记录上次播报时间，5 分钟内不重复
DEDUP_SECONDS = 300  # 5 分钟

if os.path.exists(LOCK):
    with open(LOCK) as f:
        pid = f.read().strip()
    if pid and os.path.exists(f"/proc/{pid}"):
        print(f"已有播报进程 (PID {pid})，跳过")
        sys.exit(0)

# 时间锁：5 分钟内播过就跳过（防止 AI 超时重试导致重复播放）
if os.path.exists(DEDUP):
    try:
        last = float(open(DEDUP).read().strip())
        elapsed = time.time() - last
        if elapsed < DEDUP_SECONDS:
            print(f"距上次播报仅 {int(elapsed)} 秒（<{DEDUP_SECONDS}s），跳过防重复")
            sys.exit(0)
    except:
        pass  # 文件损坏则忽略

open(LOCK, "w").write(str(os.getpid()))
open(DEDUP, "w").write(str(time.time()))

def _cleanup():
    if os.path.exists(LOCK): os.remove(LOCK)

def cleanup_old_files(max_age_minutes=30):
    """清理 SHARED 目录下超过 max_age_minutes 分钟的临时音频文件。
    保留 birds.mp3 和所有非 .mp3 文件（README、脚本等）。
    在每次播报前执行，确保旧文件不会堆积。"""
    now = time.time()
    max_age = max_age_minutes * 60
    keep = {"birds.mp3", "清歌漫谷.mp3"}
    removed = 0
    for name in os.listdir(SHARED):
        if name in keep:
            continue
        if not name.endswith(".mp3") and name != "broadcast-text.txt":
            continue
        path = os.path.join(SHARED, name)
        if not os.path.isfile(path):
            continue
        try:
            mtime = os.path.getmtime(path)
            age = now - mtime
            if age > max_age:
                os.remove(path)
                removed += 1
        except Exception:
            pass
    if removed:
        log(f"🧹 清理 {removed} 个旧音频文件（>{max_age_minutes}分钟）")

import signal
signal.signal(signal.SIGTERM, lambda *a: (_cleanup(), sys.exit(1)))
signal.signal(signal.SIGINT,  lambda *a: (_cleanup(), sys.exit(1)))
signal.alarm(420)


def log(msg):
    print(f"  {msg}", flush=True)


def run(cmd, timeout=15):
    r = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=timeout)
    if r.returncode != 0: return None
    try: return json.loads(r.stdout)
    except: return r.stdout.strip() or None


# ── 常量 ──
SOLAR_TERMS = {(1,5):"小寒",(1,20):"大寒",(2,4):"立春",(2,19):"雨水",
    (3,6):"惊蛰",(3,21):"春分",(4,5):"清明",(4,20):"谷雨",
    (5,6):"立夏",(5,21):"小满",(6,6):"芒种",(6,21):"夏至",
    (7,7):"小暑",(7,23):"大暑",(8,7):"立秋",(8,23):"处暑",
    (9,8):"白露",(9,23):"秋分",(10,8):"寒露",(10,23):"霜降",
    (11,7):"立冬",(11,22):"小雪",(12,7):"大雪",(12,22):"冬至"}

SOLAR_HOLS = {(1,1):"元旦",(2,14):"情人节",(3,8):"妇女节",(4,5):"清明节",
    (5,1):"劳动节",(6,1):"儿童节",(7,1):"建党节",(8,1):"建军节",
    (9,10):"教师节",(10,1):"国庆节",(12,25):"圣诞节"}

LUNAR_HOLS = {(1,1):"春节",(1,15):"元宵节",(5,5):"端午节",
    (7,15):"中元节",(8,15):"中秋节",(9,9):"重阳节"}

LUNAR_DIGITS = ["","一","二","三","四","五","六","七","八","九"]
LUNAR_MONTHS = ["","正月","二月","三月","四月","五月","六月",
                "七月","八月","九月","十月","冬月","腊月"]

WIND_NAMES = ["无风","软风","轻风","微风","和风","清风","强风",
              "疾风","大风","烈风","狂风","暴风","台风"]

WIND_LEVELS = [1, 6, 12, 20, 29, 39, 50, 62, 75, 89, 103, 118]


def wind_name(kmh):
    for i, lim in enumerate(WIND_LEVELS):
        if kmh < lim: return WIND_NAMES[i]
    return "台风"


def wind_level(kmh):
    for i, lim in enumerate(WIND_LEVELS):
        if kmh < lim: return i
    return 12


def beaufort(power_str):
    try:
        level = int(power_str.split("-")[0])
        if 0 <= level <= 12: return WIND_NAMES[level]
    except: pass
    return "微风"


def lunar_day(d):
    if d in (10,20,30): return ["","初十","二十","三十"][d//10]
    if d > 20: return f"二十{LUNAR_DIGITS[d-20]}"
    if d > 10: return f"十{LUNAR_DIGITS[d-10]}"
    return f"初{LUNAR_DIGITS[d]}"


def greeting(h):
    if h < 6: return "凌晨"
    if h < 9: return "早上"
    if h < 12: return "上午"
    if h < 14: return "中午"
    if h < 17: return "下午"
    if h < 20: return "傍晚"
    return "晚上"


# ── 天气数据：apple-weather 主源 → 腾讯备选 ──

def fetch_weather():
    """获取定位 → apple-weather → 腾讯备选，返回 (current, today, tomorrow)"""
    # 尝试自动定位，若在隆回职业中专附近则自动修正以保证精度
    try:
        loc_res = subprocess.run(["apple-location", "current", "--compact", "-q"],
                                 capture_output=True, text=True, timeout=5)
        loc = json.loads(loc_res.stdout)
        # 使用标准坐标
        lat, lng = loc["latitude"], loc["longitude"]
        
        # 坐标校准逻辑：如果检测到的位置在职业中专附近（约2公里内），强制修正
        target_lat, target_lng = 27.135397, 111.010810
        diff_lat = abs(lat - target_lat)
        diff_lng = abs(lng - target_lng)
        if diff_lat < 0.02 and diff_lng < 0.02:
            lat, lng = target_lat, target_lng
            log(f"📍 自动定位 ({lat:.4f}, {lng:.4f}) 已校准至职业中专")
        else:
            log(f"📍 自动定位 ({lat:.4f}, {lng:.4f})")
    except:
        lat, lng = 27.135397, 111.010810
        log(f"📍 使用默认定位：隆回职业中专 ({lat:.4f}, {lng:.4f})")

    # ── 主源：apple-weather ──
    cur_data = run(f"apple-weather current --lat {lat} --lng {lng} --compact")
    day_data = run(f"apple-weather daily --lat {lat} --lng {lng} --days 3 --compact")

    if cur_data and cur_data.get("ok") and day_data and day_data.get("ok"):
        ob = cur_data["data"]
        days = day_data["data"]["daily"]

        kw = ob.get("condition", "多云")
        ws = ob.get("wind_speed_kmh", 0)
        d = ob.get("wind_direction", "无风")

        current = {
            "temp": round(ob["temperature_c"]),
            "feels": round(ob["apparent_temperature_c"]),
            "humidity": round(ob["humidity"] * 100),
            "weather": kw,
            "wind_dir": d,
            "wind_speed_kmh": round(ws, 1),
            "wind_name": wind_name(ws),
            "wind_level": wind_level(ws),
            "wind_power": str(wind_level(ws)),
            "precip": round(ob.get("precipitation_mm", 0), 1),
            "uv_index": round(ob.get("uv_index", 0)),
            "visibility_km": round(ob.get("visibility_km", 0), 1),
        }

        today = {}
        tomorrow = {}
        today_str = datetime.now().strftime("%Y-%m-%d")
        found_today = False
        for d in days:
            if d["date"] == today_str:
                today = {
                    "high": round(d["high_c"]),
                    "low": round(d["low_c"]),
                    "weather": d.get("condition", "多云"),
                    "precip": round(d["precip_chance"] * 100),
                    "wind_dir": current["wind_dir"],
                    "wind_name": current["wind_name"],
                    "wind_power": current["wind_power"],
                    "uv_index": round(d.get("uv_index", 0)),
                }
                found_today = True
            elif not found_today and today == {}:
                continue
            elif tomorrow == {}:
                tomorrow = {
                    "high": round(d["high_c"]),
                    "low": round(d["low_c"]),
                    "weather": d.get("condition", "多云"),
                    "precip": round(d["precip_chance"] * 100),
                    "wind_dir": current["wind_dir"],
                    "wind_name": current["wind_name"],
                    "wind_power": current["wind_power"],
                    "uv_index": round(d.get("uv_index", 0)),
                }

        if not today:
            today = {"high": current["temp"], "low": current["temp"]-3,
                     "weather": current["weather"], "precip": 0,
                     "wind_dir": current["wind_dir"], "wind_name": current["wind_name"],
                     "wind_power": current["wind_power"]}

        log(f"☀️ apple-weather: {current['temp']}°C 体感{current['feels']}°C {current['weather']} 湿度{current['humidity']}%")
        if today: log(f"📊 今日: {today['low']}-{today['high']}°C {today['weather']} 降水概率{today['precip']}%")
        if tomorrow: log(f"📅 明日: {tomorrow['low']}-{tomorrow['high']}°C {tomorrow['weather']} 降水概率{tomorrow['precip']}%")
        return current, today, tomorrow

    # ── 备选：腾讯天气 ──
    log("apple-weather 不可用，切腾讯天气")
    addr = loc.get("data", {}).get("address", {}) if loc and loc.get("ok") else {}
    province = addr.get("administrative_area", "湖南")
    city = addr.get("locality", "邵阳")
    county = addr.get("sub_locality", "隆回")

    params = urllib.parse.urlencode({
        "source": "pc", "weather_type": "observe|forecast_1h",
        "province": province, "city": city, "county": county,
    })
    try:
        req = urllib.request.Request(
            f"https://wis.qq.com/weather/common?{params}",
            headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        log(f"× 腾讯天气失败: {e}")
        sys.exit(1)

    if data.get("status") != 200:
        log(f"× 腾讯天气异常: {data.get('message')}")
        sys.exit(1)

    ob = data["data"].get("observe", {})
    f1h = data["data"].get("forecast_1h", {})

    current = {
        "temp": int(ob.get("degree", 0)),
        "humidity": int(ob.get("humidity", 50)),
        "weather": ob.get("weather", "多云"),
        "wind_dir": ob.get("wind_direction_name", "无风"),
        "wind_power": ob.get("wind_power", "1-3"),
        "precip": float(ob.get("precipitation", 0)),
        "uv_index": 0,
    }
    current["wind_name"] = beaufort(current["wind_power"])
    current["wind_level"] = int(current["wind_power"].split("-")[0]) if current["wind_power"] else 2
    current["feels"] = round(current["temp"] + max(0, (current["humidity"]-50)*0.15) - current["wind_level"]*0.3)
    current["wind_speed_kmh"] = current["wind_level"] * 8

    now = datetime.now()
    today_str = now.strftime("%Y%m%d")
    tomorrow_str = (now + timedelta(days=1)).strftime("%Y%m%d")

    today_hours = [h for k, h in sorted(f1h.items(), key=lambda x: int(x[0])) if h.get("update_time","").startswith(today_str)]
    tomorrow_hours = [h for k, h in sorted(f1h.items(), key=lambda x: int(x[0])) if h.get("update_time","").startswith(tomorrow_str)]

    def day_stats(hours):
        if not hours:
            return {"high": current["temp"], "low": current["temp"]-3,
                    "weather": current["weather"], "precip": 0,
                    "wind_dir": current["wind_dir"], "wind_power": current["wind_power"]}
        temps = [int(h.get("degree", 0)) for h in hours]
        ws = [h.get("weather", "") for h in hours if h.get("weather")]
        dw = [h.get("weather", "") for h in hours if 6 <= int(k) <= 18]
        mw = max(set(dw), key=dw.count) if dw else (ws[0] if ws else "多云")
        rh = sum(1 for h in hours if any(kw in h.get("weather","") for kw in ["雨","雪","雷"]))
        return {"high": max(temps), "low": min(temps), "weather": mw,
                "precip": min(100, rh*20),
                "wind_dir": hours[0].get("wind_direction", ""),
                "wind_power": hours[0].get("wind_power", "1-3")}

    today = day_stats(today_hours)
    tomorrow = day_stats(tomorrow_hours) if tomorrow_hours else {}

    log(f"☀️ 腾讯: {current['temp']}°C 体感{current['feels']}°C {current['weather']} 湿度{current['humidity']}%")
    return current, today, tomorrow


# ── 文案生成 ──

def build_text(cur, today, tomorrow):
    now = datetime.now()
    ld = LunarDate.from_solar_date(now.year, now.month, now.day)
    wk = "星期" + "一二三四五六日"[now.weekday()]

    temp = cur["temp"]
    feels = cur["feels"]
    hum = cur["humidity"]
    weather = cur["weather"]
    wind_dir = cur["wind_dir"]
    wind_name = cur.get("wind_name", "微风")

    high = today["high"]
    low = today["low"]
    precip = today["precip"]

    t_str = f"{now.hour}点{now.minute}分" if now.minute else f"{now.hour}点"
    greet = greeting(now.hour)

    # 节日/节气
    extra = ""
    bits = []
    if (now.month, now.day) in SOLAR_HOLS: bits.append(SOLAR_HOLS[(now.month, now.day)])
    if (ld.month, ld.day) in LUNAR_HOLS: bits.append(LUNAR_HOLS[(ld.month, ld.day)])
    if ld.month == 12 and ld.day in (29, 30): bits.append("除夕")
    if (now.month, now.day) in SOLAR_TERMS: bits.append(SOLAR_TERMS[(now.month, now.day)])
    if bits: extra = "，" + "、".join(bits)
    lunar = f"{LUNAR_MONTHS[ld.month]}{lunar_day(ld.day)}"

    # 第1段：问候 + 时间
    p1 = f"{greet}好呀。现在是{t_str}，{now.month}月{now.day}日，农历{lunar}{extra}，{wk}。"

    # 第2段：天气状况
    cond = weather
    if "雨" in cond:
        p2 = f"外面正下着{cond}，湿漉漉的。{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，出门记得带伞。"
    elif "雪" in cond:
        p2 = f"外面{cond}，白茫茫一片！{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，路面可能结冰，注意防滑。"
    elif "雾" in cond:
        p2 = f"今天有雾，能见度不太好。{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，开车慢一点。"
    elif "晴" in cond:
        p2 = f"今天天气晴朗，{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，"
    elif "云" in cond:
        p2 = f"今天{cond}，{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，"
    elif "阴" in cond:
        p2 = f"今天阴天，天色有点暗。{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，"
    else:
        p2 = f"今天{cond}。{wind_dir}，{wind_name}，当前温度{temp}度，体感温度{feels}度，"

    # 第3段：体感建议
    diff = high - low
    if feels >= 38:
        p3 = f"体感都快40度了，跟蒸笼一样，不是非要出去的话千万别出门，小心中暑。空调西瓜安排上，照顾好自己。"
    elif feels >= 35:
        p3 = f"热得够呛，这个点出门就是找罪受。不是非出去不可就待屋里吧，实在要出去一定做好防晒、带足水。"
    elif feels >= 33:
        p3 = f"挺热的，不是必须出门的话建议别往外跑，户外活动真的吃不消，多喝水。"
    elif feels >= 30:
        p3 = f"有点闷热，动一动就出汗，注意补水。"
    elif feels >= 26:
        p3 = f"挺舒服的，适合出门走走。"
    else:
        p3 = f"比较凉快，出门记得带件外套。"

    if hum > 80: p3 += f"湿度{hum}%，闷得慌，体感比实际温度高不少。"
    elif hum > 65: p3 += f"湿度{hum}%，有点潮。"
    elif hum < 40: p3 += f"湿度{hum}%，偏干，记得多喝水。"
    else: p3 += f"湿度{hum}%，还行。"

    # 第4段：温差 + 降水
    if diff > 8: p4 = f"今天{low}到{high}度，温差{diff}度，早晚凉中午热，最好随身带件外套。"
    elif diff > 5: p4 = f"今天{low}到{high}度，温差不算大。"
    else: p4 = f"今天气温{low}到{high}度，全天温差小，比较稳定。"

    if precip >= 70: p4 += "大概率有雨，出门一定带伞。"
    elif precip >= 40: p4 += "可能有雨，最好带把伞以防万一。"
    elif precip >= 15: p4 += "可能会飘点雨，建议带把伞。"
    else: p4 += "今天基本不下雨，不用操心这个。"

    # 第5段：明天预告
    p5 = ""
    if tomorrow:
        tc = tomorrow.get("weather", "多云")
        tl, th = tomorrow["low"], tomorrow["high"]
        tp = tomorrow["precip"]
        if tp >= 60: p5 = f"明天{tc}，{tl}到{th}度，大概率有雨，提前准备。"
        elif tp <= 15: p5 = f"明天{tc}，{tl}到{th}度，天气还不错。"
        else: p5 = f"明天{tc}，{tl}到{th}度，可能有雨，留意一下。"

    # 第6段：收尾
    if feels >= 35: p6 = "今天确实热得够呛，照顾好自己，别中暑了。"
    elif feels >= 33: p6 = "天热，多喝水，注意休息。"
    elif now.hour < 9: p6 = "新的一天开始了，祝你有好心情！"
    elif now.hour < 12: p6 = "上午好，祝你元气满满！"
    elif now.hour < 14: p6 = "中午了，午饭吃好点儿，下午才有力气。"
    elif now.hour < 18: p6 = "下午好，加油，再坚持坚持就下班了！"
    else: p6 = "今晚好好休息，别熬夜，晚安！"

    return f"{p1}{p2}{p3}{p4}{p5}{p6}"


# ── 语音合成 ──

def tts(text):
    voice_mp3 = f"{SHARED}/voice-{TS}.mp3"
    txt_file = f"{SHARED}/broadcast-text.txt"
    with open(txt_file, "w") as f:
        f.write(text)

    # 1) edge-tts 晓晓
    if subprocess.run(["which", "edge-tts"], capture_output=True).returncode == 0:
        log("edge-tts 晓晓合成中...")
        r = subprocess.run(
            ["edge-tts", "--voice", "zh-CN-XiaoxiaoNeural", "--rate=+10%",
             "--file", txt_file, "--write-media", voice_mp3],
            capture_output=True, text=True, timeout=60,
        )
        if r.returncode == 0 and os.path.exists(voice_mp3) and os.path.getsize(voice_mp3) > 1000:
            log(f"✓ 晓晓合成 ({os.path.getsize(voice_mp3)//1024}KB)")
            return voice_mp3
        log("edge-tts 失败，切豆包")

    # 2) 豆包TTS
    api_key = os.environ.get("DOUBAO_TTS_API_KEY")
    if api_key:
        log("豆包TTS合成中...")
        try:
            r = subprocess.run(
                ["uv", "run", "--script", "--cache-dir", "/root/.cache/uv",
                 "/var/minis/skills/doubao-tts/scripts/tts.py",
                 "--text", text, "--output", voice_mp3],
                capture_output=True, text=True, timeout=120,
            )
            if r.returncode == 0 and os.path.exists(voice_mp3) and os.path.getsize(voice_mp3) > 1000:
                log(f"✓ 豆包TTS合成 ({os.path.getsize(voice_mp3)//1024}KB)")
                return voice_mp3
            log(f"豆包失败: {r.stderr[:200]}")
        except Exception as e:
            log(f"豆包异常: {e}")
    else:
        log("豆包API Key未配置，跳过")

    log("⚠ 语音合成全部失败，无音频输出")
    return None


# ── BGM 拼接 ──

def merge_bgm(voice_path):
    if not BGM or not os.path.exists(BGM) or os.path.getsize(BGM) < 50000:
        return voice_path

    merged = f"{SHARED}/merged-{TS}.mp3"
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", voice_path],
        capture_output=True, text=True, timeout=10,
    )
    try:
        voice_dur = float(r.stdout.strip())
    except:
        voice_dur = 30

    bgm_dur = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", BGM],
        capture_output=True, text=True, timeout=10).stdout.strip() or 180)
    voice_end = min(voice_dur, bgm_dur - 2)

    r = subprocess.run(
        ["ffmpeg", "-i", voice_path, "-i", BGM,
         "-filter_complex",
         f"[1:a]atrim=0:{voice_end},asetpts=N/SR/TB,volume=0.15[bgm_low];"
         f"[1:a]atrim={voice_end}:{bgm_dur},asetpts=N/SR/TB,volume=0.85[bgm_high];"
         f"[0:a][bgm_low]amix=inputs=2:duration=first:dropout_transition=2[part1];"
         f"[part1][bgm_high]concat=n=2:v=0:a=1[out]",
         "-map", "[out]", merged, "-y"],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode == 0 and os.path.exists(merged):
        log(f"✓ BGM拼接完成 ({os.path.getsize(merged)//1024}KB)")
        return merged
    log("BGM拼接失败，用纯语音")
    return voice_path


# ── 播放 ──

def play(path):
    r = subprocess.run(["apple-player", "play", path, "--compact"],
                       capture_output=True, text=True, timeout=10)
    try:
        sid = json.loads(r.stdout)["data"]["session_id"]
        log(f"播放已启动 (session={sid[:8]}...)，不等播完")
    except:
        log("播放启动失败")
    # 不再轮询等待，立即返回。原因：轮询 180s 会导致 AI 超时重试 → 重复播放


# ── 主流程 ──

def main():
    dry_run = "--dry-run" in sys.argv
    cleanup_old_files(max_age_minutes=30)
    log("获取天气数据...")
    cur, today, tomorrow = fetch_weather()

    log("生成文案...")
    text = build_text(cur, today, tomorrow)
    print(f"\n{'─'*50}\n{text}\n{'─'*50}\n")

    if dry_run:
        print(json.dumps({"success": True, "text": text}))
        return

    voice = None
    final = None
    try:
        log("语音合成...")
        voice = tts(text)
        if voice:
            log("混音...")
            final = merge_bgm(voice)
            log("播放...")
            play(final)
        else:
            log("无音频输出，文案已打印")
    finally:
        for f in [voice, final, f"{SHARED}/broadcast-text.txt"]:
            if f and os.path.exists(f):
                os.remove(f)
                log(f"清理 {os.path.basename(f)}")

    print(json.dumps({"success": True, "text": text}))


if __name__ == "__main__":
    main()