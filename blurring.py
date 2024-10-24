import cv2
import numpy as np


vid = "footage.mp4"


cap = cv2.VideoCapture(vid)


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


ret, frame = cap.read()


if ret:

    h, w, l = frame.shape


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    blur_vid = "blurring_vid.mp4"
    out = cv2.VideoWriter(blur_vid, fourcc, 20.0, (w, h))


    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break


        img_blur = cv2.GaussianBlur(frame, (5, 5), 0)


        out.write(img_blur)

    print(f"Video saved as {blur_vid}")

else:
    print("Error: Could not read the first frame.")


cap.release()
out.release()


cv2.destroyAllWindows()
