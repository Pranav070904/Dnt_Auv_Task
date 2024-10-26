import cv2
import numpy as np


vid = "Thresholding_dehazed.mp4"


cap = cv2.VideoCapture(vid)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


ret, frame = cap.read()
if ret:
    h, w, l = frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    contour_vid = "internal_contours_dehazed.mp4"
    out = cv2.VideoWriter(contour_vid, fourcc, 20.0, (w, h))


    while True:
        ret, frame = cap.read()
        if not ret:
            print("No more frames to read or failed to read frame.")
            break

       
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        contours, hierarchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

       
        internal_contours = np.zeros_like(gray)

    
        for i in range(len(contours)):
            if hierarchy[0][i][3] != -1:
                cv2.drawContours(internal_contours, contours, i, 255, -1)

        
        internal_contours_bgr = cv2.cvtColor(internal_contours, cv2.COLOR_GRAY2BGR)
        out.write(internal_contours_bgr)

        
        cv2.imshow("Internal Contours", internal_contours_bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"Video saved as {contour_vid}")
else:
    print("Error: Could not read the first frame.")


cap.release()
out.release()
cv2.destroyAllWindows()
