import cv2
import  numpy as np


vid = "footage.mp4"


cap = cv2.VideoCapture(vid)


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


ret, frame = cap.read()


if ret:

    h, w, l = frame.shape


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    shi = "Sharpened_vid.mp4"
    out = cv2.VideoWriter(shi, fourcc, 20.0, (w, h))


    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        img_sharp = cv2.filter2D(frame, -1, kernel)

        out.write(img_sharp)

    print(f"Video saved as {shi}")

else:
    print("Error: Could not read the first frame.")


cap.release()
out.release()


cv2.destroyAllWindows()
