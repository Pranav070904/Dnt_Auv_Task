import cv2
import numpy as np

vid = "adapt_thresh_enhanced.mp4"

cap = cv2.VideoCapture(vid)

if cap.isOpened():
    print("Video Opened")

ret,frame = cap.read()

if ret:
    h,w,l = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_vid = "detect_contour_enhanced.mp4"
    out = cv2.VideoWriter(out_vid, fourcc, 20.0, (w, h))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        contours, heirarchy = cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        external_cont = np.zeros_like(gray)
        print(heirarchy)
        for i in range(len(contours)):
            if heirarchy[0][i][3] != -1:
                cv2.drawContours(external_cont, contours, i, 255, -1)
        blurred = cv2.medianBlur(external_cont, 5)

        out_frame = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
        out.write(out_frame)



cap.release()
out.release()


cv2.destroyAllWindows()
