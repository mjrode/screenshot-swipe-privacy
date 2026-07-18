#!/usr/bin/env python3
"""Deterministic blog cover compositor for Screenshot Swipe.

Composites a 1200x675 cover: brand light-cyan background, bold title on the
left, and a marketing screenshot (which shares the same #CFF7FF background)
bleeding off the right edge.

Usage:
  python3 scripts/make-cover.py "Title line one|Title line two" path/to/shot.png out/cover.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

BG = (207, 247, 255)         # #CFF7FF — matches App Store marketing frames
TITLE = (12, 42, 51)         # dark slate-cyan
EYEBROW = (8, 126, 164)      # cyan-700

FONT_CANDIDATES = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]


def load_font(size, bold=True):
    for path in FONT_CANDIDATES:
        try:
            if path.endswith(".ttc"):
                # index 1 is the Bold face in Helvetica.ttc
                return ImageFont.truetype(path, size, index=1 if bold else 0)
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    title_arg, shot_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    lines = title_arg.split("|")

    W, H = 1200, 675
    im = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(im)

    # Screenshot on the right, scaled to full height, bleeding off the edge
    shot = Image.open(shot_path).convert("RGB")
    scale = H / shot.height
    sw = int(shot.width * scale)
    shot = shot.resize((sw, H), Image.LANCZOS)
    im.paste(shot, (W - sw + 60, 0))

    # Eyebrow + title on the left
    eyebrow_font = load_font(30)
    title_font = load_font(64)
    x = 70
    y = 180
    draw.text((x, y), "SCREENSHOT SWIPE BLOG", font=eyebrow_font, fill=EYEBROW)
    y += 70
    for line in lines:
        draw.text((x, y), line, font=title_font, fill=TITLE)
        y += 82

    im.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
