import random, string, ffmpeg, subprocess, requests, json, time, textwrap
from datetime import datetime, date, timezone 
import cv2
# from PIL import Image, ImageFont, ImageDraw
import numpy as np


NATO_LIST = []
NATO_FILES_LIST = []
BUMPER_FILE_LIST = []


def SET_VARS():
    global now_filename
    global NAME_LETTER_MP3
    global NAME_MUSAK_MP3
    global NAME_ICON_PNG
    global now
    global this_hour
    now = datetime.now(timezone.utc)
    today = date.today()
    this_year = str(today.year)
    this_month = str(today.month)
    this_day = str(today.day)
    this_hour = str(int(now.strftime("%H"))+1)
    now_filename = this_year+"-"+this_month+"-"+this_day+"-"+this_hour
    NAME_LETTER_MP3 = now_filename+"-LETTERS-TEST.mp3"
    NAME_MUSAK_MP3 = now_filename+"-MUSAK-TEST.mp3"
    NAME_ICON_PNG = now_filename+"-ICON-TEST.png"


def generate_random_alphanumeric(length):
    characters = string.ascii_uppercase
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def concat_mp3s(mp3_files, output_path):
    try:
        # Create input streams for all files
        input_args = [ffmpeg.input(mp3_file) for mp3_file in mp3_files]
        # Apply the concat filter (v=0 for no video, a=1 for one audio stream)
        audio_output = ffmpeg.concat(*input_args, v=0, a=1).output(output_path)
        # Run the command
        ffmpeg.run(audio_output, overwrite_output=True)
        print(f"Successfully concatenated files to {output_path}")

    except ffmpeg.Error as e:
        print(f"FFmpeg error: {e.stderr.decode()}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def NATO_MP3(amount_of_letters):
    global NATO_LETTER_STRING
    NATO_LETTER_STRING = generate_random_alphanumeric(amount_of_letters)
    print(f"Random alphanumeric string: {NATO_LETTER_STRING}")
    for i in NATO_LETTER_STRING:
        # print(FILES_NATO_MAPPING[i])
        NATO_FILES_LIST.append(FILES_NATO_MAPPING[i])
    concat_mp3s(NATO_FILES_LIST, NAME_LETTER_MP3)

def FINAL_FILE(bumperMP3, lettersmMP3):
    concat_mp3s([bumperMP3,lettersmMP3,bumperMP3], now_filename+".mp3")


def TEXT_TO_ICON(Chunks, Text, FilePath):
    NATO_chunks = textwrap.wrap(Text, Chunks)
    print(NATO_chunks)

    # Open image with OpenCV
    im_o = np.zeros((1000,1000,3), np.uint8)

    # Make into PIL Image
    im_p = Image.fromarray(im_o)

    # Get a drawing context
    draw = ImageDraw.Draw(im_p)
    monospace = ImageFont.truetype("3270SemiCondensed-Regular.ttf",200)

    TopOffset = -31
    SideOffSet = 0
    LineOffset = 120


    LoopCount = TopOffset
    for Chunk in NATO_chunks:
        Row = (SideOffSet, LoopCount)
        draw.text((Row),Chunk,(255,255,255),font=monospace,align='right')
        print(Row)
        LoopCount += LineOffset

    # #Save image
    result_o = np.array(im_p)
    cv2.imwrite(FilePath, result_o)


# SET_VARS()
# NATO_MP3(128)
TEXT_TO_ICON(11, "LOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUMLOREMIPSUM", "pfp.jpg")






