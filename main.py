from moviepy.editor import *
from pytube import YouTube
import webbrowser
import random
import pyautogui
import pyperclip
import os
import time
import sys

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

inputs = [] 
input1 = input("Enter the Youtube Short URL: ") 
while input1 != "": 
	inputs.append(input1) 
	input1 = input("Enter the Youtube Short URL: ")

for i in inputs:
    print("Searching for " + i)
    '''
    Un-comment the following if you want to see the video open in your browser.

    try:
        urL=i
        chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(urL)
        time.sleep(5)
        pyautogui.press('escape')
        pyautogui.press('space')
    except webbrowser.Error as e:
        print(e)
    time.sleep(1)
    '''
    Download(i)


vidNames=["vid1", "vid2", "vid3", "vid4", "vid5"]
vidCount=0

path=r'C://Users//inhor//Downloads//Python_Projects//auto-yt-shorts'
for filename in os.listdir(path):
    if not os.path.isfile(filename):
        continue

    basename, extension = os.path.splitext(filename)
    if ',' not in basename:
        continue # Ignore

    target_name = f'{vidNames[vidCount]}{extension}'
    os.rename(
        os.path.join(TARGET_DIR, filename),
        os.path.join(TARGET_DIR, target_name)
    )
    vidCount+=1

#mcs = random.randint(5, 247)
#mc = VideoFileClip("mc.mp4", audio=False).subclip(mcs, mcs+50)
#mc.write_videofile("output.mp4")
#clip1 = VideoFileClip("myvideo.mp4").margin(10)
#clip1.set_position("center")

Fvid1=VideoFileClip("vid1.mp4")
Fvid2=VideoFileClip("vid2.mp4")
Fvid3=VideoFileClip("vid3.mp4")
Fvid4=VideoFileClip("vid4.mp4")
Fvid5=VideoFileClip("vid5.mp4")

combined=concatenate_videoclips([Fvid1, Fvid2, Fvid3, Fvid4, Fvid5])
combined.write_videofile("output.mp4")
