import cv2 as cv

# Read the image
img = cv.imread("resources/img.jpg")
img_resized = cv.resize(img, (800, 600))
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
# Resize the image (corrected dimensions)

# binary = cv.resize(400, 500)
# Convert the image to grayscale

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# Save the grayscale image
cv.imwrite('resources/image_gray.jpg', gray)
cv.imwrite('resources/image_bw.png', binary)


# Optional: Display images (uncomment if needed)
# cv.imshow("Original Image", img_resized)
# cv.imshow("Gray Image", gray)
# cv.waitKey(0)
# cv.destroyAllWindows()
