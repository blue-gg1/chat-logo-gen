import textwrap
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np


def TextToIcon(Chunks, Text, TemplateImage, Font, FilePath):
    TextChunks = textwrap.wrap(Text, Chunks)
    print(TextChunks)

    # Open image with OpenCV
    # im_o = np.zeros((1000,1000,3), np.uint8)
    im_o = cv2.imread(TemplateImage)


    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype(Font,200)

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

TextToIcon(20, """test\r\ntest""", "Template.png","fonts/3270SemiCondensed-Regular.ttf","pfp.jpg")



