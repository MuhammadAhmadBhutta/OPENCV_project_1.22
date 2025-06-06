# how to capture a webcam inside python

# Step-1 import libraries
import cv2 as cv 
import numpy as np

# Step-2 Read the frame from Camera 
cap = cv.VideoCapture(0) # webcam no.1
# if (cap.isOpened() == False):
#     print("There is an error")


# read untill the end
# Step-3 Display the cam frame by frame 
while(cap.isOpened()):
    #capture frame by
    ret, frame = cap.read()
    if ret == True:
        # to display frame
        cv.imshow("Frame",frame)
        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break        

# Step-4 release or close windows
cap.release()
cv.destroyAllWindows()