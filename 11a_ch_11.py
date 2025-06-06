# Writing video from cam
import cv2 as cv
import numpy as np
# 
cap = cv.VideoCapture(0)

# writing format, codec, video object and filr output 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/cam_video.mp4", cv.VideoWriter_fourcc("M","J",'P','G'), 30,(frame_width, frame_height),isColor=False)

#cv.VideoWriter() chake in internat
while (True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret:
        out.write(gray_frame)
        # Display the video frame
        cv.imshow("Video", gray_frame)

        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
    

# Release the video and close all windows
cap.release()
out.release()
cv.destroyAllWindows()
