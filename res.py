# -*- coding: utf-8 -*-

'''
Simple CLI tool to generate images from given resolution and color

Usage Example:
    python res.py 300x200:darkgreen 200x200:red

Format:
    WIDTHxHEIGHT:COLOR
or:
    WIDTHxHEIGHT
    Color will default to "orange"

Color can be an HTML Color:
    red, black, lightblue, ...
or HEX Colors:
    #eee, #eeeeee, ...

'''

import sys
from PIL import Image
from PIL import ImageColor

def gen(part):
    # defaults
    default_color = "orange"
    color = ImageColor.getrgb(default_color);
    width = 300
    height = 200

    rpart = part.replace(":", "x")
    res = rpart.split("x")

    if(len(res) not in (2,3)):
        print("Parameter is not a resolution (missing 'x')")
        return

    try:
        width  = int(res[0])
        height = int(res[1])
    except ValueError as e:
        print("Parameter is not a resolution (casting to int failed)")
        return

    try:
        if(len(res) == 3):
            color = ImageColor.getrgb(res[2])
    except ValueError as e:
        print("Wrong color. Fallback: " + default_color)

    img = Image.new('RGB', (width, height), color)
    img.save(part + '.png')
    # img.show() ## debug

for part in sys.argv:
    if(part != __file__):
        gen(part)

