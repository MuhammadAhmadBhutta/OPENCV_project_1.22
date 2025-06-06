# Setting of cam or video


import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10, 100) # 10 is the key to set brightness
cap.set(3, 720) # Width key is 3
cap.set(4, 1080) # Heigth key is 4

while (True):
    rat, frame = cap.read()
    if rat == True:
        cv.imshow("frame", frame)
        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()