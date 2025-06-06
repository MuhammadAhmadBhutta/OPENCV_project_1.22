# How to draw lines , and shapes in pyton


import cv2 as cv
import numpy as np


# Draw a canvas

img = np.zeros((600,600)) # black
img1 = np.ones((600,600))

# print size 
# print("The size of our canvas is:", img.shape)
# print(img)

#adding colors to the canvas

colored_img = np.zeros((600,600, 3), np.uint8) #color channel addition 

colored_img[:] = 255,0,210  #color comlete image 

colored_img[150:230,100:500] = 255,160,10 # part of image to be colord
# adding line 

cv.line(colored_img,(0,0),(colored_img.shape[0], colored_img.shape[1]),(255,0,0),3) # croosed line
cv.line(colored_img, (100,100),(300,300),(255,255,50),3) # part line


#adding rectangles 
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255),3) # draw
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255),cv.FILLED) #fill


# adding circle
cv.circle(colored_img, (400,300),50 , (255,100,0),5)
cv.circle(colored_img, (400,300),50 , (255,100,0),cv.FILLED)

# adding text
cv.putText(colored_img,"Python pratice on vs code", (200,500), cv.FONT_HERSHEY_COMPLEX,0.8 , (255,255,0), 2)



# cv.imshow("Black",img)
# # cv.imshow("White",img1)
cv.imshow("Colored",colored_img)
cv.waitKey(0)
cv.destroyAllWindows()

