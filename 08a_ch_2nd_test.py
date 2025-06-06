# coverting video to gray or Black and White and saving video
import cv2 as cv

# Load the video
cap = cv.VideoCapture('resources/video.mp4')

# writing format, codec, video object and filr output 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/out_video.mp4", cv.VideoWriter_fourcc("M","J",'P','G'), 10,(frame_width, frame_height),isColor=False)


while (True):
    (ret, frame) = cap.read()
    graframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret:
        out.write(graframe)
        # Display the video frame
        cv.imshow("Video", graframe)

        # Exit on pressing 'q'
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break
    

# Release the video and close all windows
cap.release()
out.release()
cv.destroyAllWindows()
