import textwrap, requests, cv2, json
from PIL import Image, ImageFont, ImageDraw
import numpy as np


def TextToIcon(Text, TemplateImage, Font, FilePath):
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
        # (90,220), # text space
        (180,200), # text space
        Text, # the words themeseves 
        (0, 0, 0), # opacity in rbg ?
        font=monospace, # which font
        align='center') 

    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)

def GetNamesFromShnaton(CourseNumber: int, Year: int):
    ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/"+CourseNumber+"?year="+str(Year))
    ShantonObject = json.loads(ShnatonJson.content)
    if ShantonObject[0]['code'] == CourseNumber:
        print(CourseNumber + "good")
    else:
        print(CourseNumber + "bad")
    return(ShantonObject[0]['name']['he'])

def FUCKTheAcademyoftheHebrewLanguage(NameOfClass):
    # StringToBeRevesed = ((NameOfClass[0]['name']['he']).replace(' ', '\n')).replace('(',"}").replace(')',"{")
    StringToBeRevesed = ((NameOfClass).replace(' ', '\n')).replace('(',"}").replace(')',"{")
    return(StringToBeRevesed)

def AddTextToImmage(Text, OutputFile):
    StringForImage = ""
    for line in Text.splitlines():
        print(line[::-1])
        StringForImage += (line[::-1])+"\n"
    TextToIcon(StringForImage, "Template.png", "fonts/Huji-Bold.otf", OutputFile)


def GetCourseFromFile():
    with open("source",'r') as SourceList:
        SourceData = SourceList.read().splitlines()
    return(SourceData)

CourseList = GetCourseFromFile()

for Course in CourseList:
    print(Course)
    CourseName = GetNamesFromShnaton(Course, 2027)
    TextForImage = FUCKTheAcademyoftheHebrewLanguage(CourseName)
    AddTextToImmage(TextForImage, Course+".png")