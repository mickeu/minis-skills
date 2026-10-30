#!/bin/bash
# fix_runner_icons.sh
# 修复 iCTRL UITests-Runner 以及类似 XCTest-Runner 应用白图标问题
# 核心原理：
# 1. 补齐通知专用 (20pt @2x 40x40, @3x 60x60)、设置 (29pt)、Spotlight (40pt)、主屏 (60pt @2x 120x120, @3x 180x180) 全套物理 PNG
# 2. Info.plist 显式声明 CFBundleIcons 与 CFBundleIcons~ipad，使用 CFBundleIconFiles 映射纯物理文件名
# 3. 严禁声明 CFBundleIconName: "AppIcon"，否则 iOS 会强制寻找 Assets.car 导致散落 PNG 失效回退为白网格
# 4. 严禁塞入外部应用的 Assets.car，否则主屏图标会被篡改
# 5. 重新签名安装后，若系统缓存未及时刷新，需重启设备触发 IconServices 缓存重建

set -e

INPUT="$1"
OUTPUT="$2"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: $0 <input.ipa> <output.ipa>" >&2
    exit 1
fi

TMP_DIR=$(mktemp -d /tmp/fix_icon_XXXXXX)
trap 'rm -rf "$TMP_DIR"' EXIT

unzip -q "$INPUT" -d "$TMP_DIR"
APP_DIR=$(find "$TMP_DIR/Payload" -mindepth 1 -maxdepth 1 -name "*.app" | head -1)

if [ -z "$APP_DIR" ]; then
    echo "Error: No .app found in Payload" >&2
    exit 1
fi

python3 - <<PY
import os, zlib, struct, plistlib, zipfile
from PIL import Image

app_dir = "$APP_DIR"

# 1. 提取或解码基础图标 (处理 CgBI 苹果私有 PNG 格式)
icon_src = os.path.join(app_dir, 'AppIcon60x60@2x.png')
if not os.path.exists(icon_src):
    # 尝试寻找任意 png
    for f in os.listdir(app_dir):
        if 'icon' in f.lower() and f.endswith('.png'):
            icon_src = os.path.join(app_dir, f)
            break

def decode_cgbi(data):
    if len(data) < 8 or data[:8] != b'\x89PNG\r\n\x1a\n':
        return data
    pos = 8
    chunks = []
    width, height = None, None
    has_cgbi = False
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8]
        chunk_data = data[pos+8:pos+8+length]
        pos += 12 + length
        if chunk_type == b'CgBI':
            has_cgbi = True
            continue
        if chunk_type == b'IHDR':
            width, height = struct.unpack('>II', chunk_data[:8])
        chunks.append((chunk_type, chunk_data))

    if not has_cgbi:
        return data

    idat_data = b''.join([cd for ct, cd in chunks if ct == b'IDAT'])
    decompressed = zlib.decompress(idat_data, -zlib.MAX_WBITS)
    row_bytes = 1 + width * 4
    raw_pixels = bytearray()
    for y in range(height):
        filter_byte = decompressed[y*row_bytes:y*row_bytes+1]
        raw_pixels += filter_byte
        row = decompressed[y*row_bytes+1:(y+1)*row_bytes]
        new_row = bytearray()
        for x in range(0, len(row), 4):
            b, g, r, a = row[x:x+4]
            if a > 0 and a < 255:
                r = min(255, int(r * 255 / a))
                g = min(255, int(g * 255 / a))
                b = min(255, int(b * 255 / a))
            new_row.extend([r, g, b, a])
        raw_pixels += new_row

    new_idat = zlib.compress(raw_pixels)
    out = bytearray(b'\x89PNG\r\n\x1a\n')
    for ct, cd in chunks:
        if ct == b'IDAT':
            continue
        if ct == b'IEND':
            out += struct.pack('>I', len(new_idat)) + b'IDAT' + new_idat + struct.pack('>I', zlib.crc32(b'IDAT' + new_idat) & 0xffffffff)
        out += struct.pack('>I', len(cd)) + ct + cd + struct.pack('>I', zlib.crc32(ct + cd) & 0xffffffff)
    return bytes(out)

raw_data = open(icon_src, 'rb').read()
clean_data = decode_cgbi(raw_data)
import io
base_img = Image.open(io.BytesIO(clean_data)).convert('RGB')

# 2. 生成规范物理尺寸
sizes = {
    'AppIcon20x20@2x.png': (40, 40),
    'AppIcon20x20@3x.png': (60, 60),
    'AppIcon29x29@2x.png': (58, 58),
    'AppIcon29x29@3x.png': (87, 87),
    'AppIcon40x40@2x.png': (80, 80),
    'AppIcon40x40@3x.png': (120, 120),
    'AppIcon60x60@2x.png': (120, 120),
    'AppIcon60x60@3x.png': (180, 180),
    'AppIcon20x20@2x~ipad.png': (40, 40),
    'AppIcon29x29@2x~ipad.png': (58, 58),
    'AppIcon40x40@2x~ipad.png': (80, 80),
    'AppIcon76x76@2x~ipad.png': (152, 152),
    'AppIcon83.5x83.5@2x~ipad.png': (167, 167),
}

for fname, sz in sizes.items():
    base_img.resize(sz, Image.Resampling.LANCZOS).save(os.path.join(app_dir, fname), 'PNG')

# 3. 移除外来/冲突 Assets.car
car_path = os.path.join(app_dir, 'Assets.car')
if os.path.exists(car_path):
    os.remove(car_path)

# 4. 修改 Info.plist
pl_path = os.path.join(app_dir, 'Info.plist')
with open(pl_path, 'rb') as f:
    pl = plistlib.load(f)

pl['CFBundleDisplayName'] = pl.get('CFBundleDisplayName') or 'iCTRL'
pl['CFBundleIcons'] = {
    'CFBundlePrimaryIcon': {
        'CFBundleIconFiles': ['AppIcon20x20', 'AppIcon29x29', 'AppIcon40x40', 'AppIcon60x60']
    }
}
pl['CFBundleIcons~ipad'] = {
    'CFBundlePrimaryIcon': {
        'CFBundleIconFiles': ['AppIcon20x20', 'AppIcon29x29', 'AppIcon40x40', 'AppIcon76x76', 'AppIcon83.5x83.5']
    }
}

with open(pl_path, 'wb') as f:
    plistlib.dump(pl, f)
PY

# 5. 打包新 IPA
cd "$TMP_DIR"
zip -qr "$OUTPUT" Payload
echo "Fix complete: $OUTPUT"
