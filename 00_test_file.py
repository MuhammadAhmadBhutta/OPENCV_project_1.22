import cv2 as cv
import numpy as np

img = cv.imread("resources/Mypic.jpg")
resized_img = cv.resize(img, (720,480))
print("The size of our image is:", img.shape)

cropped_img = img[0:500, 0:350]

cv.imshow("Original",img)
cv.imshow("Cropped",cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
