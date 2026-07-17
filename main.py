import random, string, subprocess, json, time, textwrap
from datetime import datetime, date, timezone 
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def generate_random_alphanumeric(length):
    characters = string.ascii_uppercase
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def TEXT_TO_ICON(Chunks, Text, FilePath):
    TextChunks = textwrap.wrap(Text, Chunks)
    print(TextChunks)

    # Open image with OpenCV
    # im_o = np.zeros((1000,1000,3), np.uint8)
    im_o = cv2.imread("Template.png")


    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype("fonts/Huji-Bold.otf",200)

    TopOffset = 300
    SideOffSet = 150
    LineOffset = 0


    LoopCount = TopOffset
    for Chunk in TextChunks:
        Row = (SideOffSet, LoopCount)
        draw.text((Row),Chunk,(255,255,255),font=monospace,align='right')
        print(Row)
        LoopCount += LineOffset

    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)

TEXT_TO_ICON(20, """
1 ןובשח             
""", "pfp.jpg")



