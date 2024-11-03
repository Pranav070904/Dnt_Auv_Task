import cv2
import numpy

vid = "Sharpened_dehaze_vid.mp4"

cap = cv2.VideoCapture(vid)

if cap.isOpened():
    print("Video Opened")

ret,frame = cap.read()

if ret:
    h,w,l = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_vid = "adapt_thresh_enhanced.mp4"
    out = cv2.VideoWriter(out_vid, fourcc, 20.0, (w, h))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.medianBlur(gray_frame, 5)
        thresh1 = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,41, 20)
        thresh1_color = cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR)


        out.write(thresh1_color)



cap.release()
out.release()


cv2.destroyAllWindows()
