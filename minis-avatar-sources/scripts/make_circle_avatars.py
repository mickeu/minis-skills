#!/usr/bin/env python3
"""把透明宠物贴纸批量处理成 512x512 圆形透明头像：圆外 alpha=0，圆内保留原样"""
import os, sys
from PIL import Image, ImageDraw, ImageChops

SRC = "/tmp/stickers-repo/pets"
OUT = "/var/minis/shared/avatar-candidates/circle"
os.makedirs(OUT, exist_ok=True)

def make_circle(path, out, size=512):
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    side = min(w, h)
    # 居中偏上裁剪成方形
    left = (w - side) // 2
    top = int(h * 0.15)
    top = max(0, min(top, h - side))
    im = im.crop((left, top, left + side, top + side)).resize((size, size), Image.LANCZOS)
    # 圆形遮罩：圆内 255，圆外 0（完全透明）
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    r, g, b, a = im.split()
    # 新的 alpha = 圆形遮罩（圆外透明）；圆内保留原图 alpha（精灵周边本就透明）
    # 用 multiply：mask 与 原 alpha 相乘，圆内 alpha 不变，圆外 0
    new_a = ImageChops.multiply(mask, a)
    Image.merge("RGBA", (r, g, b, new_a)).save(out)
    return out

if __name__ == "__main__":
    names = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    ok = fail = 0
    for n in names:
        p = os.path.join(SRC, n)
        if not os.path.exists(p):
            print("缺:", p); fail += 1; continue
        base = os.path.splitext(n)[0]
        make_circle(p, os.path.join(OUT, f"circle_{base}.png"))
        ok += 1
    print(f"完成 {ok} 张 -> {OUT}（失败 {fail}）")
