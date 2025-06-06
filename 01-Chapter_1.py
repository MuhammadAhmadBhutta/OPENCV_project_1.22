#Reading an image and Displaying it
# library import
import cv2 as cv


img = cv.imread("resources/360_F_617474687_rqPZ5p5HxD9RZUajSDBYlffpq9PIs8oY.jpg")

cv.imshow("pehill image", img)

cv.waitKey(0)

cv.waitKey(0)
cv.destroyAllWindows()



