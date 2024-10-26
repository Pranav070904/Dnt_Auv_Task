import cv2
import numpy as np


vid = "dehazed_footage.mp4"


cap = cv2.VideoCapture(vid)


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


ret, frame = cap.read()

if ret:

    h, w, l = frame.shape


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    thresh = "Thresholding_dehazed.mp4"
    out = cv2.VideoWriter(thresh, fourcc, 20.0, (w, h))


    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break


        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        retu, img_thresh = cv2.threshold(frame,50,200,cv2.THRESH_BINARY)
        img_thresh = cv2.cvtColor(img_thresh,cv2.COLOR_GRAY2BGR)

        out.write(img_thresh)


else:
    print("Error: Could not read the first frame.")


cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
