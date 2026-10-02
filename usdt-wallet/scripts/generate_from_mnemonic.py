#!/usr/bin/env python3
"""
根据用户提供的助记词生成比特币和以太坊钱包
"""

import hashlib
import hmac
import json
import ecdsa

# BIP39 英文助记词表（用于验证）
BIP39_WORDS = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
    "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
    "acoustic", "acquire", "across", "act", "action", "actor", "actress", "actual",
    "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance",
    "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
    "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album",
    "alcohol", "alert", "alien", "all", "alley", "allow", "almost", "alone",
    "alpha", "already", "also", "alter", "always", "amateur", "amazing", "among",
    "amount", "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry",
    "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
    "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april",
    "arch", "arctic", "area", "arena", "argue", "arm", "armed", "armor",
    "army", "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact",
    "artist", "artwork", "ask", "aspect", "asset", "assist", "assume", "asthma",
    "athlete", "atom", "attack", "attend", "attitude", "attract", "auction", "audit",
    "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid",
    "awake", "aware", "awesome", "awful", "awkward", "axis", "baby", "bachelor",
    "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo", "banana",
    "banner", "bar", "barely", "bargain", "barrel", "base", "basic", "basket",
    "battle", "beach", "bean", "beauty", "because", "become", "beef", "before",
    "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit",
    "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike",
    "bind", "biology", "bird", "birth", "bitter", "black", "blade", "blame",
    "blanket", "blast", "bleak", "bless", "blind", "blood", "blossom", "blow",
    "blue", "blur", "blush", "board", "boat", "body", "boil", "bomb",
    "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss",
    "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass",
    "brave", "bread", "breeze", "brick", "bridge", "brief", "bright", "bring",
    "brisk", "broccoli", "broken", "bronze", "broom", "brother", "brown", "brush",
    "bubble", "buddy", "budget", "buffalo", "build", "bulb", "bulk", "bullet",
    "bundle", "bunny", "burden", "burger", "burst", "bus", "business", "busy",
    "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage",
    "cake", "call", "calm", "camera", "camp", "can", "canal", "cancel",
    "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital", "captain",
    "car", "carbon", "card", "cargo", "carpet", "carry", "cart", "case",
    "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category",
    "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement",
    "census", "century", "cereal", "certain", "chair", "chalk", "champion", "change",
    "chaos", "chapter", "charge", "chase", "cheap", "check", "cheese", "chef",
    "cherry", "cheat", "chest", "chicken", "chief", "child", "chimney", "choice",
    "choose", "chronic", "chuckle", "chunk", "churn", "citizen", "city", "civil",
    "claim", "clap", "clarify", "claw", "clay", "clean", "clerk", "clever",
    "cliff", "climb", "clinic", "clip", "clock", "clog", "close", "cloth",
    "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast",
    "coconut", "code", "coffee", "coil", "coin", "collect", "color", "column",
    "combine", "come", "comfort", "comic", "common", "company", "concert", "conduct",
    "confirm", "congress", "connect", "consider", "control", "convince", "cook", "cool",
    "copper", "copy", "coral", "core", "corn", "correct", "cost", "cotton",
    "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack",
    "cradle", "craft", "cram", "crane", "crash", "crater", "crawl", "crazy",
    "cream", "credit", "creek", "crew", "cricket", "crime", "crisp", "critic",
    "crop", "cross", "crouch", "crowd", "crucial", "cruel", "cruise", "crumble",
    "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard", "curious",
    "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad",
    "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn",
    "day", "deal", "debate", "debris", "decade", "december", "decide", "decline",
    "decorate", "decrease", "deer", "defense", "define", "defy", "degree", "delay",
    "deliver", "demand", "demise", "denial", "dentist", "deny", "depart", "depend",
    "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk",
    "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram",
    "dial", "diamond", "diary", "dice", "diesel", "diet", "differ", "digital",
    "dignity", "dilemma", "dinner", "dinosaur", "direct", "dirt", "disagree", "discover",
    "disease", "dish", "dismiss", "disorder", "display", "distance", "divert", "divide",
    "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain",
    "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft",
    "dragon", "drama", "drastic", "draw", "dream", "dress", "drift", "drill",
    "drink", "drip", "drive", "drop", "drum", "dry", "duck", "dumb",
    "dune", "during", "dust", "dutch", "duty", "dwarf", "dynamic", "eager",
    "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo",
    "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight",
    "either", "elbow", "elder", "electric", "elegant", "element", "elephant", "elevator",
    "elite", "else", "embark", "embody", "embrace", "emerge", "emotion", "employ",
    "empower", "empty", "enable", "encourage", "end", "endless", "endorse", "enemy",
    "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough",
    "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode",
    "equal", "equip", "era", "erase", "erode", "erosion", "error", "erupt",
    "escape", "essay", "essence", "estate", "eternal", "ethics", "evidence", "evil",
    "evoke", "evolve", "exact", "example", "excess", "exchange", "excite", "exclude",
    "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit",
    "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend",
    "extra", "eye", "eyebrow", "fabric", "face", "faculty", "fade", "faint",
    "faith", "fall", "false", "fame", "family", "famous", "fan", "fancy",
    "fantasy", "farm", "fashion", "fat", "fatal", "father", "fatigue", "fault",
    "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female",
    "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field",
    "figure", "file", "film", "filter", "final", "find", "fine", "finger",
    "finish", "fire", "firm", "fiscal", "fish", "fit", "fitness", "fix",
    "flag", "flame", "flash", "flat", "flavor", "flee", "flight", "flip",
    "float", "flock", "floor", "flower", "fluid", "flush", "fly", "foam",
    "focus", "fog", "foil", "fold", "follow", "food", "foot", "force",
    "forest", "forget", "fork", "fortune", "forum", "forward", "fossil", "foster",
    "found", "fox", "fragile", "frame", "frequent", "fresh", "friend", "fringe",
    "frog", "front", "frost", "frown", "frozen", "fruit", "fuel", "fun",
    "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy", "gallery",
    "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas",
    "gasp", "gate", "gather", "gauge", "gaze", "general", "genius", "genre",
    "gentle", "genuine", "gesture", "ghost", "giant", "gift", "giggle", "ginger",
    "giraffe", "girl", "give", "glad", "glance", "glare", "glass", "glide",
    "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue", "goat",
    "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern",
    "gown", "grab", "grace", "grain", "grant", "grape", "grass", "gravity",
    "great", "green", "grid", "grief", "grit", "grocery", "group", "grow",
    "grunt", "guard", "guess", "guide", "guilt", "guitar", "gun", "gym",
    "habit", "hair", "half", "hammer", "hamster", "hand", "happy", "harbor",
    "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head",
    "health", "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help",
    "hen", "hero", "hip", "hire", "history", "hobby", "hockey", "hold",
    "hole", "holiday", "hollow", "home", "honey", "hood", "hope", "horn",
    "horror", "horse", "hospital", "host", "hotel", "hour", "hover", "hub",
    "huge", "human", "humble", "humor", "hundred", "hungry", "hunt", "hurdle",
    "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea", "identify",
    "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense",
    "immune", "impact", "impose", "improve", "impulse", "inch", "include", "income",
    "increase", "index", "indicate", "indoor", "industry", "infant", "inflict",
    "inform", "initial", "inject", "inmate", "inner", "innocent", "input", "inquiry",
    "insane", "insect", "inside", "inspire", "install", "intact", "interest", "into",
    "invest", "invite", "involve", "iron", "island", "isolate", "issue", "item",
    "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly",
    "jewel", "job", "join", "joke", "journey", "joy", "judge", "juice",
    "jump", "jungle", "junior", "junk", "just", "kangaroo", "keen", "keep",
    "ketchup", "key", "kick", "kid", "kidney", "kind", "kingdom", "kiss",
    "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife", "knock",
    "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp",
    "language", "laptop", "large", "later", "latin", "laugh", "laundry", "lava",
    "law", "lawn", "lawsuit", "layer", "lazy", "leader", "leaf", "learn",
    "leave", "lecture", "left", "leg", "legal", "legend", "leisure", "lemon",
    "lend", "length", "lens", "leopard", "lesson", "letter", "level", "liberty",
    "library", "license", "life", "lift", "light", "like", "limb", "limit",
    "link", "lion", "liquid", "list", "little", "live", "lizard", "load",
    "loan", "lobster", "local", "lock", "logic", "lonely", "long", "loop",
    "lottery", "loud", "lounge", "love", "loyal", "lucky", "luggage", "lumber",
    "lunar", "lunch", "luxury", "lyrics", "machine", "mad", "magic", "magnet",
    "maid", "mail", "main", "major", "make", "mammal", "man", "manage",
    "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin",
    "marine", "market", "marriage", "mask", "mass", "master", "match", "material",
    "math", "matrix", "matter", "maximum", "maze", "meadow", "mean", "measure",
    "meat", "mechanic", "medal", "media", "melody", "melt", "member", "memory",
    "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message",
    "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind",
    "minimum", "minor", "minute", "miracle", "mirror", "misery", "miss", "mistake",
    "mix", "mixed", "mixture", "mobile", "model", "modify", "mom", "moment",
    "monitor", "monkey", "monster", "month", "moon", "moral", "more", "morning",
    "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie",
    "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music",
    "must", "mutual", "myself", "mystery", "myth", "naive", "name", "napkin",
    "narrow", "nasty", "nation", "nature", "near", "neck", "need", "negative",
    "neglect", "neither", "nephew", "nerve", "nest", "net", "network", "neutral",
    "never", "news", "next", "nice", "night", "noble", "noise", "nominee",
    "noodle", "normal", "north", "nose", "notable", "nothing", "notice", "novel",
    "now", "nuclear", "number", "nurse", "nut", "oak", "obey", "object",
    "oblige", "obscure", "observe", "obtain", "obvious", "occur", "ocean", "october",
    "odor", "off", "offer", "office", "often", "oil", "okay", "old",
    "olive", "olympic", "omit", "once", "one", "onion", "online", "only",
    "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard",
    "order", "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other",
    "outdoor", "outer", "output", "outside", "oval", "oven", "over", "own",
    "owner", "oxygen", "oyster", "ozone", "pact", "paddle", "page", "pair",
    "palace", "palm", "panda", "panel", "panic", "panther", "paper", "parade",
    "parent", "park", "parrot", "party", "pass", "patch", "path", "patient",
    "patrol", "pattern", "pause", "pave", "payment", "peace", "peanut", "pear",
    "peasant", "pelican", "pen", "penalty", "pencil", "people", "pepper", "perfect",
    "permit", "person", "pet", "phone", "photo", "phrase", "physical", "piano",
    "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot", "pink",
    "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic",
    "plate", "play", "please", "pledge", "pluck", "plug", "plunge", "poem",
    "poet", "point", "polar", "pole", "police", "pond", "pony", "pool",
    "popular", "portion", "position", "possible", "post", "potato", "pottery",
    "poverty", "powder", "power", "practice", "praise", "predict", "prefer",
    "prepare", "present", "pretty", "prevent", "price", "pride", "primary", "print",
    "priority", "prison", "private", "prize", "problem", "process", "produce", "profit",
    "program", "project", "promote", "proof", "property", "prosper", "protect", "proud",
    "provide", "public", "pudding", "pull", "pulp", "pulse", "pumpkin", "punch",
    "pupil", "puppy", "purchase", "purity", "purpose", "purse", "push", "put",
    "puzzle", "pyramid", "quality", "quantum", "quarter", "question", "quick", "quit",
    "quiz", "quote", "rabbit", "raccoon", "race", "rack", "radar", "radio",
    "rage", "rail", "rain", "raise", "rally", "ramp", "ranch", "random",
    "range", "rapid", "rare", "rate", "rather", "raven", "raw", "razor",
    "ready", "real", "reason", "rebel", "rebuild", "recall", "receive", "recipe",
    "record", "recycle", "reduce", "reflect", "reform", "region", "regret", "regular",
    "reject", "relax", "release", "relief", "rely", "remain", "remember", "remind",
    "remove", "render", "renew", "rent", "reopen", "repair", "repeat", "replace",
    "report", "require", "rescue", "resemble", "resist", "resource", "response",
    "result", "retire", "retreat", "return", "reunion", "reveal", "review", "reward",
    "rhythm", "rib", "ribbon", "rice", "rich", "ride", "ridge", "rifle",
    "right", "rigid", "ring", "riot", "ripple", "risk", "ritual", "rival",
    "river", "road", "roast", "robot", "robust", "rocket", "romance", "roof",
    "rookie", "room", "rose", "rotate", "rough", "round", "route", "royal",
    "rubber", "rude", "rug", "rule", "run", "runway", "rural", "sad",
    "saddle", "sadness", "safe", "sail", "salad", "salmon", "salon", "salt",
    "salute", "same", "sample", "sand", "satisfy", "satoshi", "sauce", "sausage",
    "save", "say", "scale", "scan", "scare", "scatter", "scene", "scheme",
    "school", "science", "scissors", "scorpion", "scout", "scrap", "screen", "script",
    "scrub", "sea", "search", "season", "seat", "second", "secret", "section",
    "security", "seed", "seek", "segment", "select", "sell", "seminar", "senior",
    "sense", "sentence", "series", "service", "session", "settle", "setup", "seven",
    "shadow", "shaft", "shallow", "share", "shed", "shell", "sheriff", "shield",
    "shift", "shine", "ship", "shiver", "shock", "shoe", "shoot", "shop",
    "short", "shoulder", "shove", "shrimp", "shrug", "shuffle", "shy", "sibling",
    "sick", "side", "siege", "sight", "sign", "silent", "silk", "silly",
    "silver", "similar", "simple", "since", "sing", "siren", "sister", "situate",
    "six", "size", "skate", "sketch", "ski", "skill", "skin", "skirt",
    "skull", "slab", "slam", "sleep", "slender", "slice", "slide", "slight",
    "slim", "slogan", "slot", "slow", "slush", "small", "smart", "smile",
    "smoke", "smooth", "snack", "snake", "snap", "sniff", "snow", "soap",
    "soccer", "social", "sock", "soda", "soft", "solar", "soldier", "solid",
    "solution", "solve", "someone", "song", "soon", "sorry", "sort", "soul",
    "sound", "soup", "source", "south", "space", "spare", "spatial", "spawn",
    "speak", "special", "speed", "spell", "spend", "sphere", "spice", "spider",
    "spike", "spin", "spirit", "split", "sponsor", "spoon", "sport", "spot",
    "spray", "spread", "spring", "spy", "square", "squeeze", "squirrel", "stable",
    "stadium", "staff", "stage", "stairs", "stamp", "stand", "start", "state",
    "stay", "steak", "steel", "stem", "step", "stereo", "stick", "still",
    "sting", "stock", "stomach", "stone", "stool", "story", "stove", "strategy",
    "street", "strike", "strong", "struggle", "student", "stuff", "stumble", "style",
    "subject", "submit", "subway", "success", "such", "sudden", "suffer", "sugar",
    "suggest", "suit", "summer", "sun", "sunny", "sunset", "super", "supply",
    "supreme", "sure", "surface", "surge", "surprise", "surround", "survey", "suspect",
    "sustain", "swallow", "swamp", "swap", "swarm", "swear", "sweet", "swim",
    "swing", "switch", "sword", "symbol", "symptom", "syrup", "system", "table",
    "tackle", "tag", "tail", "talent", "talk", "tank", "tape", "target",
    "task", "taste", "tattoo", "taxi", "teach", "team", "tell", "ten",
    "tenant", "tennis", "tent", "term", "test", "text", "thank", "that",
    "theme", "then", "theory", "there", "they", "thing", "this", "thought",
    "three", "thrive", "throw", "thumb", "thunder", "ticket", "tide", "tiger",
    "tilt", "timber", "time", "tiny", "tip", "tired", "tissue", "title",
    "toast", "tobacco", "today", "toddler", "toe", "together", "toilet", "token",
    "tomato", "tomorrow", "tone", "tongue", "tonight", "tool", "tooth", "top",
    "topic", "topple", "torch", "tornado", "tortoise", "toss", "total", "tourist",
    "toward", "tower", "town", "toy", "track", "trade", "traffic", "tragic",
    "train", "transfer", "trap", "trash", "travel", "tray", "treat", "tree",
    "trend", "trial", "tribe", "trick", "trigger", "trim", "trip", "trophy",
    "trouble", "truck", "true", "truly", "trumpet", "trust", "truth", "try",
    "tube", "tuna", "tunnel", "turkey", "turn", "turtle", "twelve", "twenty",
    "twice", "twin", "twist", "two", "type", "typical", "ugly", "umbrella",
    "unable", "unaware", "uncle", "uncover", "under", "undo", "unfair", "unfold",
    "unhappy", "uniform", "union", "unique", "unit", "universe", "unknown", "unlock",
    "until", "unusual", "unveil", "update", "upgrade", "uphold", "upon", "upper",
    "upset", "urban", "usage", "use", "used", "useful", "useless", "usual",
    "utility", "vacant", "vacuum", "vague", "valid", "valley", "valve", "van",
    "vanish", "vapor", "various", "vast", "vault", "vehicle", "velvet", "vendor",
    "venture", "venue", "verb", "verify", "version", "very", "vessel", "veteran",
    "viable", "vibrant", "vicious", "victory", "video", "view", "village", "vintage",
    "violin", "virtual", "virus", "visa", "visit", "visual", "vital", "vivid",
    "vocal", "voice", "void", "volcano", "volume", "vote", "voyage", "wage",
    "wagon", "wait", "walk", "wall", "walnut", "want", "warfare", "warm",
    "warrior", "wash", "wasp", "waste", "water", "wave", "way", "wealth",
    "weapon", "wear", "weasel", "weather", "web", "wedding", "weekend", "weird",
    "welcome", "well", "west", "wet", "whale", "what", "wheat", "wheel",
    "when", "where", "whip", "whisper", "wide", "width", "wife", "wild",
    "will", "win", "window", "wine", "wing", "wink", "winner", "winter",
    "wire", "wisdom", "wise", "wish", "witness", "wolf", "woman", "wonder",
    "wood", "wool", "word", "work", "world", "worry", "worth", "wrap",
    "wreck", "wrestle", "wrist", "write", "wrong", "yard", "year", "yellow",
    "you", "young", "youth", "zebra", "zero", "zone", "zoo"
]

# 构造集合用于快速检查
BIP39_SET = set(BIP39_WORDS)

def validate_mnemonic(words):
    """验证助记词是否有效"""
    for w in words:
        if w not in BIP39_SET:
            return False, f"无效的单词: {w}"
    if len(words) not in [12, 15, 18, 21, 24]:
        return False, f"助记词数量应为12/15/18/21/24，当前: {len(words)}"
    return True, "有效"

def mnemonic_to_seed(mnemonic_words, passphrase=""):
    """助记词 → 种子 (BIP39)"""
    mnemonic_str = " ".join(mnemonic_words)
    salt = ("mnemonic" + passphrase).encode('utf-8')
    return hashlib.pbkdf2_hmac('sha512', mnemonic_str.encode('utf-8'), salt, 2048)

def derive_key(seed, path):
    """从种子派生私钥 (简化 BIP32)"""
    # 使用 HMAC-SHA512 派生
    key = hmac.new(b"Bitcoin seed", seed, hashlib.sha512).digest()
    return key[:32]

def private_to_public_key(private_key_bytes):
    """私钥 → 公钥 (secp256k1)"""
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return b'\x04' + vk.to_string()

def public_key_to_eth_address(public_key_bytes):
    """公钥 → 以太坊地址 (Keccak-256)"""
    keccak_hash = hashlib.sha3_256(public_key_bytes[1:]).digest()
    address_bytes = keccak_hash[-20:]
    
    # EIP-55 校验和
    address = address_bytes.hex()
    address_hash = hashlib.sha3_256(address.encode()).digest()
    
    checksum_address = "0x"
    for i, char in enumerate(address):
        if char in '0123456789':
            checksum_address += char
        else:
            if address_hash[i // 2] >> (4 * (1 - i % 2)) & 8:
                checksum_address += char.upper()
            else:
                checksum_address += char
    
    return checksum_address

def public_key_to_btc_address(public_key_bytes):
    """公钥 → 比特币地址 (P2PKH)"""
    # SHA-256
    sha = hashlib.sha256(public_key_bytes).digest()
    
    # RIPEMD-160
    ripemd = hashlib.new('ripemd160', sha).digest()
    
    # 添加版本字节 (0x00 = 主网)
    versioned = b'\x00' + ripemd
    
    # 双重 SHA-256 校验
    checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
    
    # Base58Check 编码
    binary_addr = versioned + checksum
    
    return encode_base58(binary_addr)

def encode_base58(b):
    """Base58Check 编码"""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    
    # 统计前导零
    leading_zeros = 0
    for byte in b:
        if byte == 0:
            leading_zeros += 1
        else:
            break
    
    # 转换
    num = int.from_bytes(b, 'big')
    result = ""
    while num > 0:
        num, remainder = divmod(num, 58)
        result = alphabet[remainder] + result
    
    # 补回前导零
    return '1' * leading_zeros + result


# ===== 主程序 =====

words = ["assume", "night", "behind", "above", "short", "soap", 
         "system", "manage", "perfect", "invite", "equal", "diesel"]

print("=" * 60)
print("🔑 使用助记词生成钱包")
print("=" * 60)

# 验证
valid, msg = validate_mnemonic(words)
print(f"\n📝 助记词: {' '.join(words)}")
print(f"✅ 验证: {msg}")

# 生成种子
seed = mnemonic_to_seed(words)
print(f"\n🌱 种子 (前32字节): {seed[:32].hex()}...")

# 派生私钥
private_key = derive_key(seed, "m")
print(f"\n🔐 私钥: {private_key.hex()}")

# 生成公钥
public_key = private_to_public_key(private_key)
print(f"📌 公钥 (65字节): {public_key[:10].hex()}...")

# 以太坊地址
eth_address = public_key_to_eth_address(public_key)
print(f"\n📱 以太坊地址 (ERC-20):")
print(f"   {eth_address}")

# 比特币地址
btc_address = public_key_to_btc_address(public_key)
print(f"\n📱 比特币地址:")
print(f"   {btc_address}")

print("\n" + "=" * 60)
print("✅ 钱包生成完成")
print("=" * 60)