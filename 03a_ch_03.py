# library import
import cv2 as cv

# Read and resize the image
img = cv.imread("resources/360_F_617474687_rqPZ5p5HxD9RZUajSDBYlffpq9PIs8oY.jpg")
img1 = cv.resize(img, (1920, 1080))

# Conversion to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display code
cv.imshow("Original Image", img1)  # Updated to display resized image
cv.imshow("Gray Image", gray_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()
