# coverting video to gray or Black and White
import cv2 as cv

# Load the video
cap = cv.VideoCapture('resources/video.mp4')

while (True):
    (ret, frame) = cap.read()
    graframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(graframe, 127, 255, cv.THRESH_BINARY)
    if ret:
        # Display the video frame
        cv.imshow("Video", binary)

        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
    

# Release the video and close all windows
cap.release()
cv.destroyAllWindows()
