# imports
import cv2
import sys

# check for external arguments for non-default video sources
s = 0 # default index, webcam
# check for supplied arguments
if len(sys.argv) > 1:
    s = sys.argv[1] # get the video source

source = cv2.VideoCapture(s)

# create a preview window
win_name = "Camera Preview"

# create a resizable preview window
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# start a loop and display the video frames
while cv2.waitKey(1) != 27: # wait for the escape key
    has_frame, frame = source.read()
    # has_frame detects problems with the capture source

    # if there are problems we should break from the loop
    if not has_frame:
        break

    # display the frame
    cv2.imshow(win_name, frame)

# close the video capture device
source.release()
# close the preview window
cv2.destroyWindow()