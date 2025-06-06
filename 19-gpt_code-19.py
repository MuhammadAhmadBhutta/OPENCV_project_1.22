# Step-1: Import Libraries
import cv2 as cv
import numpy as np

# Step-2: Define a function to find coordinates
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:  # Left mouse button click
        print(x, '', y)  # Print coordinates in the console
        
        # Define font and overlay text on the image
        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(img, f"{x}, {y}", (x, y), font, 1, (255, 0, 0), thickness=2)
        
        # Display the updated image
        cv.imshow("image", img)

# Final function to read and display the image
if __name__ == "__main__":
    # Reading an image
    img = cv.imread("resources/warp2.png", 1)
    
    if img is None:
        print("Error: Image not found. Check the file path!")
    else:
        # Display the image
        cv.imshow("image", img)
        
        # Setting mouse callback function
        cv.setMouseCallback("image", find_coord)
        
        # Wait for user interaction
        cv.waitKey(0)
        cv.destroyAllWindows()
