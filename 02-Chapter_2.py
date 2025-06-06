#Resizing

# library import
import cv2 as cv


img = cv.imread("resources/360_F_617474687_rqPZ5p5HxD9RZUajSDBYlffpq9PIs8oY.jpg")
img1 = cv.resize(img,(1920,1080))

cv.imshow("pehill image", img)
cv.imshow("Doosri image", img1)

cv.waitKey(0)
cv.destroyAllWindows()








