import cv2 as cv
import numpy as np

# Read the image
img = cv.imread("resources/warp2.png")

# Check if the image is loaded successfully
if img is None:
    print("Error: Image not found. Check the file path!")
else:
    print(f"Original image shape: {img.shape}")

    # Defining points for perspective transformation
    # Ensure you have exactly four points for a valid perspective transform
    point1 = np.float32([[173, 58], [607, 108], [93, 332], [750, 496]])

    # Define the width and height for the transformed image
    width, height = 1228, 624
    point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Calculate the perspective transformation matrix
    matrix = cv.getPerspectiveTransform(point1, point2)

    # Apply the warpPerspective transformation
    out_img = cv.warpPerspective(img, matrix, (width, height))

    # Save and display the output
    cv.imwrite("resources/war_persp.png", out_img)
    cv.imshow("Original", img)
    cv.imshow("Transformed", out_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
