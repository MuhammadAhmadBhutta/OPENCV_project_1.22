# basic function or manipulation in open cv

import cv2 as cv
import numpy as np

img = cv.imread("resources/Mypic.jpg")


#resize 
resized_img = cv.resize(img, (720,480))


# gray
gray_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

# Black and White img
(thresh, binary) = cv.threshold(resized_img, 127,255,cv.THRESH_BINARY)

# blurred image 
blurr_img = cv.GaussianBlur(resized_img, (33,33),0) 

# edge detection 
edge_img = cv.Canny(resized_img, 53,53)

# thickness of lines
mat_kernel = np.ones((3,3),np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel),iterations=1)

# Make thinner outline 
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)

# corpping we will use numpy library not open cv
print("The size of our image is:", img.shape)
cropped_img = resized_img[0:500, 150:350]



cv.imshow("Original",resized_img)
cv.imshow("resized_img", resized_img)
cv.imshow("gray",gray_img)
cv.imshow("Binray",binary)
cv.imshow("Blur",blurr_img)
cv.imshow("edge",edge_img)
cv.imshow("Dilated",dilated_img)
cv.imshow("Erosion",ero_img)
cv.imshow("Cropped",cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
