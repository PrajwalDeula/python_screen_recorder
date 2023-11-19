import numpy as np
import cv2
import pyautogui
import time
from win32api import GetSystemMetrics

#parameters to create a screensize of resolution
height = GetSystemMetrics(0)
width = GetSystemMetrics(1)
dim = (height, width)

#import VideoWriter library to save the recorded frame
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("final.mp4",f,30.0,dim)

#duration or time for recording
start_time = time.time()
dur = 60
end_time = start_time + dur

#loop to capture and record the screen
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()

