# how to detect specific colors inside python


import cv2 as cv
import numpy as np 


img = cv.imread('resources/img.jpg')


# convert in hsv (Hue, Saturation, value)
# hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# sliders
def slider():
    pass

path = "resources/img.jpg"

# path1 = cv.resize(path,480,720)


cv.namedWindow("Bars")
cv.resizeWindow("Bars", 900,300)

cv.createTrackbar("Hue Min","Bars", 0,179,slider)
cv.createTrackbar("Hue Max","Bars", 0,179,slider)
cv.createTrackbar("Sat Min","Bars", 0,255,slider)
cv.createTrackbar("Sat Max","Bars", 255,255,slider)
cv.createTrackbar("Val Min","Bars", 0,255,slider)
cv.createTrackbar("Val Max","Bars", 255,255,slider)

img = cv.imread(path)
hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# hue_min = cv.getTrackbarPos("Hue Min", "Bars")
# print(hue_min)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos("Hue Min", "Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Bars")
    Sat_min = cv.getTrackbarPos("Sat Min", "Bars")
    Sat_max = cv.getTrackbarPos("Sat Max", "Bars")
    Val_min = cv.getTrackbarPos("Val Min", "Bars")
    Val_max = cv.getTrackbarPos("Val Max", "Bars")
    print(hue_min,hue_max,Sat_min,Sat_max,Val_min,Val_max)

    # to see these chanes inside an image
    lower = np.array([hue_min,Sat_min,Val_min])
    upper = np.array([hue_max,Sat_max,Val_max])
    mask_img = cv.inRange(hsv_img,lower,upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)

    # cv.imshow("Original", img) 
    # cv.imshow("HSV",hsv_img)
    cv.imshow("Mask", mask_img)
    cv.imshow("Final Output", out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()