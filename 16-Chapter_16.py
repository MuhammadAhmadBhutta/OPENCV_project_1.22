# saving HD recording of cam steaming

import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)
# resolution hd (1280x720)
def hd_resolution():
    cap.set(3,1280)
    cap.set(4,720)
def sd_resolution():
    cap.set(3,640)
    cap.set(4,480)
def fhd_resolution():
    cap.set(3,1920)
    cap.set(4,1080)

# how to change and fix the frame rate to 30fps
#sd_resolution()
hd_resolution()
#fhd_resolution()


# writing format, codec, video object and filr output 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/cam_video.mp4", cv.VideoWriter_fourcc("M","J",'P','G'), 30,(frame_width, frame_height))

#cv.VideoWriter() chake in internat
while (True):
    (ret, frame) = cap.read()
    if ret:
        out.write(frame)
        # Display the video frame
        cv.imshow("Video", frame)

        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
    

# Release the video and close all windows
cap.release()
out.release()
cv.destroyAllWindows()
