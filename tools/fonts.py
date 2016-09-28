"""Draw operations"""
from utils.functions import command
import re
import tempfile
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import session
import os


@command("draw", store=False)
def draw_font(code, full):
    """Draw code (arg chars converted to filled-char; others to space)"""
    if type(code) is list:
        t = "\n".join(code)
    else:
        t = code

    for f in full:
        t = t.replace(f, '\u2593')

    rows = [re.sub(r'[^\u2593]', '\u2591', row) for row in t.split('\n')]

    print(os.path.abspath("raw/font.ttf"))
    font = ImageFont.truetype(os.path.abspath("tools/raw/font.ttf"), 12)
    w, h = font.getsize(rows[0])
    image = Image.new("RGB", (w, h * len(rows)), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), '\n'.join(rows), font=font, fill="black")
    fd, name = tempfile.mkstemp()
    image.save(name, format='PNG')

    return session.ImageCode(name)
