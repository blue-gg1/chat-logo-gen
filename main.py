import textwrap, requests, cv2, json
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from random import randint
from bidi.algorithm import get_display


def TextToIcon(Text, TemplateImage, Font, FilePath, CourseSeed):
    # Open image with OpenCV
    im_o = np.zeros((1000,1000,3), np.uint8)

    # im_o = cv2.imread(TemplateImage) # read from image.

    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype(Font,130)

    draw.rectangle( # make the backaround a solid colour
        (0,0,1000,1000),
        fill = (randint(0,50),randint(0,50),randint(0,50)) # make it a dark pallet 
    )

    draw.ellipse( # draw the main circle 
        (20, 20, 1000, 1000), # circle covers the entire image 
        fill = (randint(20,255),randint(20,255),randint(20,255)),  # random colour for the circle. make it a not too dark pallet.
        outline = (randint(0,255),randint(0,255),randint(0,255)), # random colour for the outline 
        width=20
    )

    draw.multiline_text( # place the text
        # (im_p.width / 2, (im_p.height / 2)+40),
        (im_p.width / 2, (im_p.height / 2)), # make it be the middle 
        Text,
        fill="black", # make the text black
        font=monospace,
        align="center",
        anchor="mm", # make it the middle
        stroke_width=4, # add the outline
        stroke_fill="white" # make the outline white
    )


    # old manual placement of the text
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
    # get the json from the shanton:
    # TODO: fake headers to look like a browser (only needed if blocked.)
    ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/"+CourseNumber+"?year="+str(Year)) 

    if ShnatonJson.status_code == 200: # dont trip over the network TODO: make this an assert.
        ShantonObject = json.loads(ShnatonJson.content)
        if ShantonObject[0]['code'] == CourseNumber: # make sure we got the right course. TODO: make this an assert.
            print(CourseNumber + "good")
        else:
            print(CourseNumber + "bad")
            exit()
        return(ShantonObject[0]['name']['he'])
    else:
        exit()

def StringCleaner(NameOfClass):
    # clean up the string
    # TODO: count the amount of spaces as not to insert too many line retuns 

    # StringToBeRevesed = ((NameOfClass[0]['name']['he']).replace(' ', '\n')).replace('(',"}").replace(')',"{")
    # StringToBeRevesed = (((NameOfClass).replace(' ', '\n')).replace('(',"").replace(')',"")).replace("-","")

    StringToBeRevesed = ((NameOfClass).replace(' ', '\n')).replace("-","")
        
    return(StringToBeRevesed)

def AddTextToImageAndDealWithString(Text, OutputFile, Year, CouseNumber):
    StringForImage = ""
    for line in Text.splitlines():
        print(line[::-1])

        # StringForImage += (line[::-1])+"\n"
        StringForImage += get_display(line)+"\n" # revese the string in a way that does not change any latin text
        
    TextToIcon(StringForImage+Year, "Template.png", "fonts/DavidLibre-Bold.ttf", OutputFile, CouseNumber)

def GetCourseFromFile():
    # read the file from disk.
    with open("source",'r') as SourceList:
        SourceData = SourceList.read().splitlines()
    return(SourceData)

def GetDoubleSemesterFromShnaton(CourseNumber: int, Year: int):
    # get the json from the shanton:
    # TODO: fake headers to look like a browser (only needed if blocked.)
    ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/"+CourseNumber+"?year="+str(Year)) 

    if ShnatonJson.status_code == 200: # dont trip over the network TODO: make this an assert.
        ShnatonJsonObject = json.loads(ShnatonJson.content)
        ShnatonId = ShnatonJsonObject[0]['id']   
        print(ShnatonId)
    else:
        exit()

    if (ShnatonJsonObject[0]['coursePeriodName']['en']) == "Semester A or B":
        BothSemester = True
    elif (ShnatonJsonObject[0]['coursePeriodName']['en']) == "Semester A or B":
        BothSemester = False
    else:
        exit()
    print(BothSemester)
    

def GetTestDateFromShnaton(CourseNumber: int, Year: int):
    # get the json from the shanton:
    # TODO: fake headers to look like a browser (only needed if blocked.)
    ShnatonJson = requests.get("https://shnaton.huji.ac.il/api/courses/code/"+CourseNumber+"?year="+str(Year)) 

    if ShnatonJson.status_code == 200: # dont trip over the network TODO: make this an assert.
        ShnatonJsonObject = json.loads(ShnatonJson.content)
        ShnatonId = ShnatonJsonObject[0]['id']   
        print(ShnatonId)
    else:
        exit()
    ShnatonTestJson = requests.get("https://shnaton.huji.ac.il/api/assignments?year="+str(Year)+"&courseId="+str(ShnatonId))

    ShnatonJsonObject = json.loads(ShnatonTestJson.content)


    if ShnatonJsonObject[1]["assignmentDefinition"]["name"]["en"] == "Written test":
        print("cool")
        print('\r\n')

        TestNumber = 0
        for i in ShnatonJsonObject[1]["schedules"]:
            print(TestNumber)
            print(ShnatonJsonObject[1]["schedules"][TestNumber]["startTime"])
            TestNumber += 1


    else:
        print("fuck")
        exit()





# for Course in CourseList:
#     print(Course)
#     CourseName = GetNamesFromShnaton(Course, 2027) # year is used for the api
#     # TextForImage = get_display(CourseName)
#     TextForImage = StringCleaner(CourseName)

#     AddTextToImageAndDealWithString(TextForImage, Course+".png", "2026-2027", Course) # the year here is any text to be added to the bottom of the logo.

CourseList = GetCourseFromFile()
for Course in CourseList:
    print(Course)
    CourseName = GetNamesFromShnaton(Course, 2025) # year is used for the api
    ShnatonId = GetTestDateFromShnaton(Course, 2025)
    GetDoubleSemesterFromShnaton(Course, 2025)
    print(CourseName)


    # TextForImage = StringCleaner(CourseName)

    # AddTextToImageAndDealWithString(TextForImage, Course+".png", "2026-2027", Course) # the year here is any text to be added to the bottom of the logo.