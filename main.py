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


            # draw.text((Row),Chunk,(255,255,255),font=monospace,align='right')

    
    LoopCount = TopOffset
    for Chunk in TextChunks:
        Row = (SideOffSet, LoopCount)
        draw.text((Row),Chunk,(255,255,255),font=monospace,align='center')
        print(Row)
        LoopCount += LineOffset

    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)

# TextToIcon(10, """test
# TEST""", "Template.png","fonts/3270SemiCondensed-Regular.ttf","pfp.jpg")





def TestTextToIcon(Text, TemplateImage, Font, FilePath):
    print(Text)

    # Open image with OpenCV
    # im_o = np.zeros((1000,1000,3), np.uint8)
    im_o = cv2.imread(TemplateImage)


    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype(Font,200)

    draw.text(
        (100,250), # text space
        Text, # the words themeseves 
        (255, 255, 255), # colour in rbg
        font=monospace) # which font

    
    
    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)

StringToBeRevesed = """לוגו ומיתוג"""[::-1]

TestTextToIcon(StringToBeRevesed, "Template.png","fonts/david.ttf","pfp.jpg")
