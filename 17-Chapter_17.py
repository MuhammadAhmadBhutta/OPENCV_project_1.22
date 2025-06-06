# joining two images

import cv2 as cv
import numpy as np 


img = cv.imread("resources/img.jpg")


# stacking sme image

#1- Horizntal
hor_img = np.hstack((img,img))

#2-Vertical stack

ver_img = np.vstack((img,img))



# cv.imshow("Horizontal", hor_img)
cv.imshow("Vertical", ver_img)

cv.waitKey(0)
cv.destroyAllWindows()


#prablams
#you can only stack images with same shape (width,height,color channel)
# we can not reszie the stack image (function)
# same number of channels np function
(600,500,3)
# assiment
# you have to define a function to stack multiple images of diferent sizes and tunes

