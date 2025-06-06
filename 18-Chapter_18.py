# how to change the prespective of an image
import cv2 as cv 
import numpy as np

img = cv.imread("resources/warp2.png")

print(img.shape)


#defining points 
point1 = np.float32([[173,58],[607,108],[93,332],[168,564],[455,425],[750,496]])

width = 1228
height = 614
width,height=1228,624
point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv.getPerspectiveTransform(point1,point2)

out_img = cv.warpPerspective(img,matrix, (width,height))

cv.imwrite("resources/war_persp.png",out_img)
cv.imshow("Original", img)
cv.imshow("transformed", out_img)
cv.waitKey(0)
cv.destroyAllWindows()

