import cv2 as cv

# Load the video
cap = cv.VideoCapture('resources/video.mp4')
# cap = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)
# Indicator for successful video loading
if not cap.isOpened():
    print("Error: Unable to open video file.")
else:
    print("Playing video...")

# Reading and playing the video
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Display the video frame
        cv.imshow("Video", frame)

        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            print("Exiting on user request.")
            break
    else:
        print("End of video or error in reading frame.")
        break

# Release the video and close all windows
cap.release()
cv.destroyAllWindows()
