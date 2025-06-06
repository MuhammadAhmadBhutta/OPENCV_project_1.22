# image saving an image writing images
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite

img =cv.imread("resources/img.jpg")
# img = cv.resize(img, (600,800))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imwrite('resoures/image_gray.jpg', gray)

# cv.waitKey(0)
# cv.destroyAllWindows()





