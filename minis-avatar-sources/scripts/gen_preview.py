#!/usr/bin/env python3
"""把圆形透明头像拼成带名字的预览网格图（棋盘格背景展示透明效果）"""
import os, glob
from PIL import Image, ImageDraw, ImageFont

SRC = "/var/minis/shared/avatar-candidates/circle"
OUTP = "/var/minis/shared/avatar-candidates/circle_preview.png"
CELL_W, CELL_H = 220, 250   # 每格宽高（含名字区）
COLS = 6
files = sorted(glob.glob(os.path.join(SRC, "circle_*.png")))
rows = (len(files) + COLS - 1) // COLS
W, H = COLS * CELL_W, rows * CELL_H
# 棋盘格背景
CHECK = 16
bg = Image.new("RGB", (W, H), (235, 235, 235))
d = ImageDraw.Draw(bg)
for y in range(0, H, CHECK):
    for x in range(0, W, CHECK):
        if (x//CHECK + y//CHECK) % 2 == 0:
            d.rectangle([x, y, x+CHECK-1, y+CHECK-1], fill=(255,255,255))

# 尝试找字体
def get_font(size):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/dejavu/DejaVuSans.ttf",
              "/system/fonts/DroidSansFallback.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

font = get_font(16)

for i, f in enumerate(files):
    col, row = i % COLS, i // COLS
    x0, y0 = col * CELL_W, row * CELL_H
    name = os.path.basename(f).replace("circle_", "").replace("_sticker.png", "")
    im = Image.open(f).convert("RGBA").resize((160, 160), Image.LANCZOS)
    # 居中粘贴到格子顶部
    px = x0 + (CELL_W - 160)//2
    py = y0 + 8
    # 临时图层合成到背景
    bg.paste(im, (px, py), im)
    # 名字
    d.text((x0 + CELL_W//2, y0 + 180), name, fill=(40,40,40), font=font, anchor="mm")

bg.save(OUTP)
print(f"预览图已保存: {OUTP}  ({W}x{H}, {len(files)}张)")
