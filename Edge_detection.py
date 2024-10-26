import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Sharpened_vid.mp4")


if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter("edges_output.mp4", fourcc, fps, (frame_width, frame_height), isColor=False)

while True:

    ret, frame = cap.read()


    if not ret:
        print("Finished processing video.")
        break


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    edges = cv.Canny(gray, 120, 130)

    out.write(edges)


    cv.imshow("Edges", edges)


    if cv.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv.destroyAllWindows()
