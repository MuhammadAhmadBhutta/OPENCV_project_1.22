# split your video into frames or image sequence
# video (frames)

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("resources/video.mp4")


frameNr = 0


while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"resources/frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+2
cap.release()
