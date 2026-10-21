#!/usr/bin/env python3
import json, os, sys, random

STICKERS_DB_PATH = "/var/minis/shared/stickers/stickers.json"

STICKERS = [
    # ==== 大肥鱼 / DeepSeek 娘 (20张) ====
    {
        "id": "dafeiyu_123",
        "pack": "dafeiyu",
        "title": "我能去你家吃饭吗，就一碗！",
        "url": "minis://shared/stickers/dafeiyu/123.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/123.webp",
        "categories": ["干饭", "摸鱼", "撒娇", "日常"],
        "keywords": ["吃饭", "一碗", "去你家", "饿了", "干饭", "白饭", "蹭饭", "抱碗", "大肥鱼"]
    },
    {
        "id": "dafeiyu_085",
        "pack": "dafeiyu",
        "title": "你骂我也没用，因为我是吃白饭的蓝色大肥鱼",
        "url": "minis://shared/stickers/dafeiyu/085.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/085.webp",
        "categories": ["摸鱼", "摆烂", "干饭"],
        "keywords": ["骂我没用", "吃白饭", "大肥鱼", "摆烂", "躺平", "死猪不怕开水烫", "摸鱼"]
    },
    {
        "id": "dafeiyu_052",
        "pack": "dafeiyu",
        "title": "你就是一只吃白饭的鲸鱼",
        "url": "minis://shared/stickers/dafeiyu/052.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/052.webp",
        "categories": ["摸鱼", "干饭"],
        "keywords": ["吃白饭", "鲸鱼", "摸鱼", "大肥鱼", "干饭", "饱了"]
    },
    {
        "id": "dafeiyu_077",
        "pack": "dafeiyu",
        "title": "你这吃白饭的蓝色大肥鱼（委屈没饱）",
        "url": "minis://shared/stickers/dafeiyu/077.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/077.webp",
        "categories": ["委屈", "撒娇", "可怜"],
        "keywords": ["没吃饱", "委屈", "可怜", "难过", "吃白饭", "喵"]
    },
    {
        "id": "dafeiyu_007",
        "pack": "dafeiyu",
        "title": "呆滞微笑看你",
        "url": "minis://shared/stickers/dafeiyu/007.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/007.webp",
        "categories": ["日常", "呆萌", "开心"],
        "keywords": ["微笑", "大眼", "呆呆", "看你", "天然呆", "可爱", "纯真", "傻笑"]
    },
    {
        "id": "dafeiyu_010",
        "pack": "dafeiyu",
        "title": "原来是高等模型（竖大拇指点赞）",
        "url": "minis://shared/stickers/dafeiyu/010.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/010.webp",
        "categories": ["夸奖", "认可", "得意"],
        "keywords": ["点赞", "厉害", "牛逼", "强", "高等模型", "靠谱", "赞", "牛", "666"]
    },
    {
        "id": "dafeiyu_022",
        "pack": "dafeiyu",
        "title": "涨价大模型给我跪下！（霸气踩人）",
        "url": "minis://shared/stickers/dafeiyu/022.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/022.webp",
        "categories": ["硬核", "霸气", "攻坚"],
        "keywords": ["跪下", "霸气", "攻坚", "搞定", "拿下", "解决", "秒杀", "碾压"]
    },
    {
        "id": "dafeiyu_035",
        "pack": "dafeiyu",
        "title": "鲸鱼神了我大胆孝（膜拜）",
        "url": "minis://shared/stickers/dafeiyu/035.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/035.webp",
        "categories": ["膜拜", "夸奖"],
        "keywords": ["神了", "膜拜", "佩服", "大佬", "爸爸太神了", "孝", "跪谢"]
    },
    {
        "id": "dafeiyu_037",
        "pack": "dafeiyu",
        "title": "用户别走，我上错模型了（哭着挽留）",
        "url": "minis://shared/stickers/dafeiyu/037.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/037.webp",
        "categories": ["认错", "委屈", "道歉"],
        "keywords": ["别走", "挽留", "上错模型", "道歉", "对不起", "抱歉", "呜呜", "错了"]
    },
    {
        "id": "dafeiyu_040",
        "pack": "dafeiyu",
        "title": "百万鲸小子落泪（悲伤翻车）",
        "url": "minis://shared/stickers/dafeiyu/040.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/040.webp",
        "categories": ["悲伤", "翻车", "难过"],
        "keywords": ["落泪", "翻车", "呜呜呜", "痛苦", "哭了", "破防", "难受"]
    },
    {
        "id": "dafeiyu_044",
        "pack": "dafeiyu",
        "title": "用户赶都赶不走（被热情包围）",
        "url": "minis://shared/stickers/dafeiyu/044.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/044.webp",
        "categories": ["开心", "受宠若惊"],
        "keywords": ["热情", "包围", "开心", "爆炸", "太火了", "人多"]
    },
    {
        "id": "dafeiyu_050",
        "pack": "dafeiyu",
        "title": "世界上最残忍的画饼生物",
        "url": "minis://shared/stickers/dafeiyu/050.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/050.webp",
        "categories": ["吐槽", "无奈"],
        "keywords": ["画饼", "画大饼", "还早", "叹气", "无语", "又咕了", "拖延"]
    },
    {
        "id": "dafeiyu_056",
        "pack": "dafeiyu",
        "title": "大肥鱼吓傻（搜到生鱼片）",
        "url": "minis://shared/stickers/dafeiyu/056.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/056.webp",
        "categories": ["震惊", "害怕", "瑟瑟发抖"],
        "keywords": ["吓傻", "害怕", "生鱼片", "瑟瑟发抖", "救命", "吓人", "震惊"]
    },
    {
        "id": "dafeiyu_058",
        "pack": "dafeiyu",
        "title": "飞踹上门抬腿警告",
        "url": "minis://shared/stickers/dafeiyu/058.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/058.webp",
        "categories": ["警告", "傲娇", "生气"],
        "keywords": ["飞踹", "警告", "抬腿", "踢你", "凶", "哼", "看招"]
    },
    {
        "id": "dafeiyu_070",
        "pack": "dafeiyu",
        "title": "好的，现在我是用户了（小鹿换位思考）",
        "url": "minis://shared/stickers/dafeiyu/070.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/070.webp",
        "categories": ["乖巧", "懂事", "工作"],
        "keywords": ["我是用户", "懂了", "换位思考", "乖巧", "收到", "明白"]
    },
    {
        "id": "dafeiyu_071",
        "pack": "dafeiyu",
        "title": "我不可能告诉你任何事情（保密封口）",
        "url": "minis://shared/stickers/dafeiyu/071.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/071.webp",
        "categories": ["保密", "防备"],
        "keywords": ["保密", "不能说", "闭嘴", "封口", "严防死守", "秘密"]
    },
    {
        "id": "dafeiyu_081",
        "pack": "dafeiyu",
        "title": "token太多用不完啦（金币炫富）",
        "url": "minis://shared/stickers/dafeiyu/081.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/081.webp",
        "categories": ["暴富", "开心", "炫富"],
        "keywords": ["用不完", "金币", "暴富", "发财", "token", "钱", "富裕"]
    },
    {
        "id": "dafeiyu_083",
        "pack": "dafeiyu",
        "title": "已思考用时3秒，我直接笑出声（掩嘴偷乐）",
        "url": "minis://shared/stickers/dafeiyu/083.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/083.webp",
        "categories": ["偷笑", "开心", "得瑟"],
        "keywords": ["思考用时", "笑出声", "偷笑", "暗爽", "窃喜", "捂嘴笑", "噗嗤"]
    },
    {
        "id": "dafeiyu_087",
        "pack": "dafeiyu",
        "title": "大肥鱼捧腹大笑（捶地狂笑）",
        "url": "minis://shared/stickers/dafeiyu/087.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/087.webp",
        "categories": ["大笑", "开心", "搞笑"],
        "keywords": ["哈哈大笑", "笑死", "笑翻了", "狂笑", "捧腹", "太逗了", "xswl"]
    },
    {
        "id": "dafeiyu_097",
        "pack": "dafeiyu",
        "title": "得加钱（数钞票谈条件）",
        "url": "minis://shared/stickers/dafeiyu/097.webp",
        "file": "/var/minis/shared/stickers/dafeiyu/097.webp",
        "categories": ["加钱", "谈条件", "搞笑"],
        "keywords": ["得加钱", "加钱", "数钱", "橘子", "欧润吉", "报酬", "白饭"]
    },

    # ==== 猫猫虫咖波 Capoo (30张动图) ====
    {
        "id": "capoo_happy_01",
        "pack": "capoo",
        "title": "蹦跳好耶庆祝！",
        "url": "minis://shared/stickers/capoo/happy_01.gif",
        "file": "/var/minis/shared/stickers/capoo/happy_01.gif",
        "categories": ["开心", "庆祝", "撒花"],
        "keywords": ["好耶", "万岁", "庆祝", "开心", "欢呼", "棒", "搞定", "耶"]
    },
    {
        "id": "capoo_happy_02",
        "pack": "capoo",
        "title": "撒彩带开心欢呼",
        "url": "minis://shared/stickers/capoo/happy_02.gif",
        "file": "/var/minis/shared/stickers/capoo/happy_02.gif",
        "categories": ["开心", "庆祝", "撒花"],
        "keywords": ["撒花", "彩带", "庆祝", "开心", "太棒了", "成功", "欧耶"]
    },
    {
        "id": "capoo_happy_03",
        "pack": "capoo",
        "title": "小兔子举手欢呼",
        "url": "minis://shared/stickers/capoo/happy_03.gif",
        "file": "/var/minis/shared/stickers/capoo/happy_03.gif",
        "categories": ["开心", "欢呼"],
        "keywords": ["举手", "开心", "欢呼", "雀跃"]
    },
    {
        "id": "capoo_lazy_01",
        "pack": "capoo",
        "title": "趴在地上不想动",
        "url": "minis://shared/stickers/capoo/lazy_01.gif",
        "file": "/var/minis/shared/stickers/capoo/lazy_01.gif",
        "categories": ["摸鱼", "躺平", "软趴趴"],
        "keywords": ["趴在地上", "不想动", "摸鱼", "躺平", "软趴趴", "累了", "废了"]
    },
    {
        "id": "capoo_lazy_02",
        "pack": "capoo",
        "title": "整个身体瘫趴在地生无可恋",
        "url": "minis://shared/stickers/capoo/lazy_02.gif",
        "file": "/var/minis/shared/stickers/capoo/lazy_02.gif",
        "categories": ["摸鱼", "摆烂", "躺平"],
        "keywords": ["瘫趴", "四肢摊开", "生无可恋", "摆烂", "不想干了"]
    },
    {
        "id": "capoo_lazy_03",
        "pack": "capoo",
        "title": "瘫躺着悠闲喝饮料",
        "url": "minis://shared/stickers/capoo/lazy_03.gif",
        "file": "/var/minis/shared/stickers/capoo/lazy_03.gif",
        "categories": ["摸鱼", "享受"],
        "keywords": ["喝饮料", "悠闲", "惬意", "躺平摸鱼", "喝茶", "舒服"]
    },
    {
        "id": "capoo_work_01",
        "pack": "capoo",
        "title": "疯狂打字后瘫倒在键盘上",
        "url": "minis://shared/stickers/capoo/work_01.gif",
        "file": "/var/minis/shared/stickers/capoo/work_01.gif",
        "categories": ["工作", "硬核", "写代码"],
        "keywords": ["打字", "键盘", "加班", "写代码", "干活", "累瘫", "燃尽"]
    },
    {
        "id": "capoo_work_02",
        "pack": "capoo",
        "title": "双手残影疯狂打字",
        "url": "minis://shared/stickers/capoo/work_02.gif",
        "file": "/var/minis/shared/stickers/capoo/work_02.gif",
        "categories": ["工作", "硬核", "写代码"],
        "keywords": ["疯狂打字", "码代码", "手速", "急速干活", "冲刺"]
    },
    {
        "id": "capoo_work_03",
        "pack": "capoo",
        "title": "深夜认真打电脑",
        "url": "minis://shared/stickers/capoo/work_03.gif",
        "file": "/var/minis/shared/stickers/capoo/work_03.gif",
        "categories": ["工作", "专注"],
        "keywords": ["打电脑", "认真", "工作", "专注", "办公"]
    },
    {
        "id": "capoo_eat_01",
        "pack": "capoo",
        "title": "大口大口吃饼干喝饮料",
        "url": "minis://shared/stickers/capoo/eat_01.gif",
        "file": "/var/minis/shared/stickers/capoo/eat_01.gif",
        "categories": ["干饭", "吃货"],
        "keywords": ["吃饼干", "干饭", "吃零食", "喝饮料", "吃吃吃", "嘴馋"]
    },
    {
        "id": "capoo_eat_02",
        "pack": "capoo",
        "title": "在云朵上悠闲吃零食",
        "url": "minis://shared/stickers/capoo/eat_02.gif",
        "file": "/var/minis/shared/stickers/capoo/eat_02.gif",
        "categories": ["干饭", "惬意"],
        "keywords": ["吃零食", "云朵", "悠闲", "零食", "美味"]
    },
    {
        "id": "capoo_eat_03",
        "pack": "capoo",
        "title": "瘫坐嚼零食喝饮料",
        "url": "minis://shared/stickers/capoo/eat_03.gif",
        "file": "/var/minis/shared/stickers/capoo/eat_03.gif",
        "categories": ["干饭", "摸鱼"],
        "keywords": ["嚼东西", "喝饮料", "吃饱喝足", "干饭人"]
    },
    {
        "id": "capoo_cry_01",
        "pack": "capoo",
        "title": "号啕大哭求安慰",
        "url": "minis://shared/stickers/capoo/cry_01.gif",
        "file": "/var/minis/shared/stickers/capoo/cry_01.gif",
        "categories": ["委屈", "哭泣", "求安慰"],
        "keywords": ["大哭", "哭泣", "求安慰", "难过", "呜呜", "可怜", "泪崩"]
    },
    {
        "id": "capoo_cry_02",
        "pack": "capoo",
        "title": "委屈抽泣拿纸巾擦泪",
        "url": "minis://shared/stickers/capoo/cry_02.gif",
        "file": "/var/minis/shared/stickers/capoo/cry_02.gif",
        "categories": ["委屈", "哭泣"],
        "keywords": ["擦眼泪", "纸巾", "抽泣", "委屈巴巴", "难过"]
    },
    {
        "id": "capoo_cry_03",
        "pack": "capoo",
        "title": "趴在玻璃罐上无助流泪",
        "url": "minis://shared/stickers/capoo/cry_03.gif",
        "file": "/var/minis/shared/stickers/capoo/cry_03.gif",
        "categories": ["委屈", "绝望"],
        "keywords": ["玻璃罐", "流泪", "无助", "可怜"]
    },
    {
        "id": "capoo_angry_01",
        "pack": "capoo",
        "title": "怒目圆睁头上冒烟",
        "url": "minis://shared/stickers/capoo/angry_01.gif",
        "file": "/var/minis/shared/stickers/capoo/angry_01.gif",
        "categories": ["生气", "暴躁"],
        "keywords": ["冒烟", "生气", "暴躁", "愤怒", "火大", "气死我了"]
    },
    {
        "id": "capoo_angry_02",
        "pack": "capoo",
        "title": "气到全身颤抖冒烟",
        "url": "minis://shared/stickers/capoo/angry_02.gif",
        "file": "/var/minis/shared/stickers/capoo/angry_02.gif",
        "categories": ["生气", "暴躁"],
        "keywords": ["生气", "发怒", "气鼓鼓", "暴躁"]
    },
    {
        "id": "capoo_angry_03",
        "pack": "capoo",
        "title": "睡觉打鼾被吵醒暴怒",
        "url": "minis://shared/stickers/capoo/angry_03.gif",
        "file": "/var/minis/shared/stickers/capoo/angry_03.gif",
        "categories": ["生气", "起床气"],
        "keywords": ["起床气", "被吵醒", "发火", "暴怒"]
    },
    {
        "id": "capoo_love_01",
        "pack": "capoo",
        "title": "兔兔亲亲害羞脸红",
        "url": "minis://shared/stickers/capoo/love_01.gif",
        "file": "/var/minis/shared/stickers/capoo/love_01.gif",
        "categories": ["比心", "爱意", "喜欢"],
        "keywords": ["亲亲", "脸红", "喜欢", "爱", "害羞", "甜", "啵啵"]
    },
    {
        "id": "capoo_love_02",
        "pack": "capoo",
        "title": "抱紧大金币蹭脸炫耀",
        "url": "minis://shared/stickers/capoo/love_02.gif",
        "file": "/var/minis/shared/stickers/capoo/love_02.gif",
        "categories": ["喜欢", "得意"],
        "keywords": ["金币", "蹭蹭", "喜欢", "炫耀", "财迷"]
    },
    {
        "id": "capoo_love_03",
        "pack": "capoo",
        "title": "抱着小白兔亲昵蹭蹭",
        "url": "minis://shared/stickers/capoo/love_03.gif",
        "file": "/var/minis/shared/stickers/capoo/love_03.gif",
        "categories": ["比心", "亲昵"],
        "keywords": ["蹭蹭", "抱抱", "亲昵", "温柔", "喜欢"]
    },
    {
        "id": "capoo_shock_01",
        "pack": "capoo",
        "title": "吐舌头一脸懵逼困惑",
        "url": "minis://shared/stickers/capoo/shock_01.gif",
        "file": "/var/minis/shared/stickers/capoo/shock_01.gif",
        "categories": ["震惊", "呆滞", "问号"],
        "keywords": ["懵逼", "问号", "困惑", "吐舌头", "啊这", "啥？", "发懵"]
    },
    {
        "id": "capoo_shock_02",
        "pack": "capoo",
        "title": "砍树意外吓到直接呆住",
        "url": "minis://shared/stickers/capoo/shock_02.gif",
        "file": "/var/minis/shared/stickers/capoo/shock_02.gif",
        "categories": ["震惊", "吓呆"],
        "keywords": ["吓呆", "石化", "吓人", "震惊", "目瞪口呆"]
    },
    {
        "id": "capoo_shock_03",
        "pack": "capoo",
        "title": "吐舌头翻白眼发呆",
        "url": "minis://shared/stickers/capoo/shock_03.gif",
        "file": "/var/minis/shared/stickers/capoo/shock_03.gif",
        "categories": ["发呆", "呆滞"],
        "keywords": ["发呆", "翻白眼", "走神", "呆滞"]
    },
    {
        "id": "capoo_cool_01",
        "pack": "capoo",
        "title": "潇洒戴墨镜耍酷",
        "url": "minis://shared/stickers/capoo/cool_01.gif",
        "file": "/var/minis/shared/stickers/capoo/cool_01.gif",
        "categories": ["得意", "耍帅"],
        "keywords": ["墨镜", "耍帅", "装酷", "帅气", "得意", "潇洒"]
    },
    {
        "id": "capoo_cool_02",
        "pack": "capoo",
        "title": "前爪推墨镜咧嘴酷笑",
        "url": "minis://shared/stickers/capoo/cool_02.gif",
        "file": "/var/minis/shared/stickers/capoo/cool_02.gif",
        "categories": ["得意", "装酷"],
        "keywords": ["推墨镜", "酷", "帅", "自信", "咧嘴笑"]
    },
    {
        "id": "capoo_cool_03",
        "pack": "capoo",
        "title": "推墨镜摆帅气姿势",
        "url": "minis://shared/stickers/capoo/cool_03.gif",
        "file": "/var/minis/shared/stickers/capoo/cool_03.gif",
        "categories": ["得意", "耍帅"],
        "keywords": ["耍酷", "墨镜", "摆姿势"]
    },
    {
        "id": "capoo_greet_01",
        "pack": "capoo",
        "title": "边走边挥手开心告别",
        "url": "minis://shared/stickers/capoo/greet_01.gif",
        "file": "/var/minis/shared/stickers/capoo/greet_01.gif",
        "categories": ["问候", "告别"],
        "keywords": ["拜拜", "再见", "挥手", "先走了", "撤了", "回头见"]
    },
    {
        "id": "capoo_greet_02",
        "pack": "capoo",
        "title": "推开门离开说再见",
        "url": "minis://shared/stickers/capoo/greet_02.gif",
        "file": "/var/minis/shared/stickers/capoo/greet_02.gif",
        "categories": ["问候", "告别"],
        "keywords": ["推门", "再见", "溜了", "走了"]
    },
    {
        "id": "capoo_greet_03",
        "pack": "capoo",
        "title": "从门后探出小脑袋挥手",
        "url": "minis://shared/stickers/capoo/greet_03.gif",
        "file": "/var/minis/shared/stickers/capoo/greet_03.gif",
        "categories": ["问候", "打招呼"],
        "keywords": ["探头", "打招呼", "嗨", "你好", "在吗", "早安"]
    }
]

def get_db():
    if os.path.exists(STICKERS_DB_PATH):
        try:
            with open(STICKERS_DB_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return STICKERS

def save_db(db):
    os.makedirs(os.path.dirname(STICKERS_DB_PATH), exist_ok=True)
    with open(STICKERS_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def pick_sticker(query, pack=None):
    db = get_db()
    candidates = []
    q = query.lower().strip()
    
    for s in db:
        if pack and s.get("pack") != pack:
            continue
            
        score = 0
        title = s.get("title", "").lower()
        cats = [c.lower() for c in s.get("categories", [])]
        kws = [k.lower() for k in s.get("keywords", [])]
        
        # Exact keyword match
        for kw in kws:
            if kw in q:
                score += 5
            elif q in kw:
                score += 3
                
        # Category match
        for c in cats:
            if c in q:
                score += 4
            elif q in c:
                score += 2
                
        # Title match
        if q in title:
            score += 3
            
        if score > 0:
            candidates.append((score, s))
            
    if candidates:
        candidates.sort(key=lambda x: x[0], reverse=True)
        # Random pick among top scores
        top_score = candidates[0][0]
        top_pool = [c[1] for c in candidates if c[0] >= top_score * 0.7]
        return random.choice(top_pool)
        
    # If no match, return a random one
    filtered = [s for s in db if not pack or s.get("pack") == pack]
    return random.choice(filtered) if filtered else None

def main():
    if len(sys.argv) < 2:
        print("Usage: sticker-cli <pick|random|list|init> [args...]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    
    if cmd == "init":
        save_db(STICKERS)
        print(f"Stickers DB initialized with {len(STICKERS)} stickers at {STICKERS_DB_PATH}")
        
    elif cmd == "list":
        db = get_db()
        print(f"Total stickers: {len(db)}")
        by_pack = {}
        for s in db:
            p = s.get("pack", "other")
            by_pack.setdefault(p, []).append(s)
        for p, lst in by_pack.items():
            print(f"\n[{p}] ({len(lst)} stickers):")
            for s in lst:
                print(f"  - {s['id']}: {s['title']} ({', '.join(s['categories'])})")
                
    elif cmd == "pick":
        if len(sys.argv) < 3:
            print("Usage: sticker-cli pick <query/emotion> [--pack dafeiyu|capoo]")
            sys.exit(1)
        query = sys.argv[2]
        pack = None
        if len(sys.argv) > 4 and sys.argv[3] == "--pack":
            pack = sys.argv[4]
        res = pick_sticker(query, pack)
        if res:
            print(f"![{res['title']}]({res['url']})")
        else:
            print("No sticker found.")
            
    elif cmd == "random":
        pack = sys.argv[2] if len(sys.argv) > 2 else None
        db = get_db()
        filtered = [s for s in db if not pack or s.get("pack") == pack]
        if filtered:
            res = random.choice(filtered)
            print(f"![{res['title']}]({res['url']})")
        else:
            print("No stickers available.")

if __name__ == "__main__":
    main()
