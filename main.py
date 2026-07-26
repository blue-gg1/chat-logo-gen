import textwrap, requests, cv2, json
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from random import randint
from bidi.algorithm import get_display


def TextToIcon(Text, TemplateImage, Font, FilePath, CourseSeed):
    # Open image with OpenCV
    im_o = np.zeros((1000,1000,3), np.uint8)

    # im_o = cv2.imread(TemplateImage)


    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype(Font,125)

    draw.rectangle(
        (0,0,1000,1000),
        fill = (randint(0,50),randint(0,50),randint(0,50))
    )

    draw.ellipse(
        (20, 20, 1000, 1000), 
        fill = (randint(0,255),randint(0,255),randint(0,255)), 
        outline = (randint(0,255),randint(0,255),randint(0,255)),
        width=10
    )

    draw.multiline_text(
        # (im_p.width / 2, (im_p.height / 2)+40),
        (im_p.width / 2, (im_p.height / 2)),
        Text,
        fill="black",
        font=monospace,
        align="center",
        anchor="mm",
        stroke_width=7,
        stroke_fill="white"
    )
    # draw.text(
    #     # (90,220), # text space
    #     (100,100), # text space GOOD for 1000x1000
    #     Text, # the words themeseves 
    #     # (0, 0, 0), # opacity in rbg ?
    #     fill="white",
    #     # (255,255,255), # opacity in rbg ?
    #     font=monospace, # which font
    #     align='center',
    #     anchor="la"
    #     ) 


    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)

def GetNamesFromShnaton(CourseNumber: int, Year: int):
    ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/"+CourseNumber+"?year="+str(Year))

    if ShnatonJson.status_code == 200:
        ShantonObject = json.loads(ShnatonJson.content)
        if ShantonObject[0]['code'] == CourseNumber:
            print(CourseNumber + "good")
        else:
            print(CourseNumber + "bad")
            exit()
        return(ShantonObject[0]['name']['he'])
    else:
        exit()

def FUCKTheAcademyoftheHebrewLanguage(NameOfClass):
    # StringToBeRevesed = ((NameOfClass[0]['name']['he']).replace(' ', '\n')).replace('(',"}").replace(')',"{")
    StringToBeRevesed = (((NameOfClass).replace(' ', '\n')).replace('(',"").replace(')',"")).replace("-","")
        
    return(StringToBeRevesed)

def AddTextToImage(Text, OutputFile, Year, CouseNumber):
    StringForImage = ""
    for line in Text.splitlines():
        print(line[::-1])
        # StringForImage += (line[::-1])+"\n"
        # StringForImage += (line[::-1])+"\n"
        StringForImage += get_display(line)+"\n"
        
    TextToIcon(StringForImage+Year, "Template.png", "fonts/Alef-Bold.ttf", OutputFile, CouseNumber)


def GetCourseFromFile():
    with open("source",'r') as SourceList:
        SourceData = SourceList.read().splitlines()
    return(SourceData)

CourseList = GetCourseFromFile()

for Course in CourseList:
    print(Course)
    CourseName = GetNamesFromShnaton(Course, 2027)
    # TextForImage = get_display(CourseName)
    TextForImage = FUCKTheAcademyoftheHebrewLanguage(CourseName)

    AddTextToImage(TextForImage, Course+".png", "2026-2027", Course)