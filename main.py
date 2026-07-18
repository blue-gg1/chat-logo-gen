import textwrap, requests, cv2, json
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
    monospace = ImageFont.truetype(Font,150)

    draw.text(
        (90,250), # text space
        Text, # the words themeseves 
        (0, 0, 0), # opacity in rbg ?
        font=monospace, # which font
        align='center') 

    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)


ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/80131?year=2027")

ShantonObject = json.loads(ShnatonJson.content)
print(ShantonObject[0]['code'])

if ShantonObject[0]['code'] == '80131':
    print("good")
else:
    print("bad")

print(ShantonObject[0]['name']['he'])


# StringToBeRevesed = (ShantonObject[0]['name']['he']).replace(' ', '\n')[::-1]

StringToBeRevesed = ((ShantonObject[0]['name']['he']).replace(' ', '\n')).replace('(',"(").replace(')',"(")


StringForImage = ""
for line in StringToBeRevesed.splitlines():
    print(line[::-1])
    StringForImage += (line[::-1])+"\n"


TestTextToIcon(StringForImage, "Template.png","fonts/Huji-Bold.otf","pfp.jpg")