import cv2

# Path to the input video
vid = "footage.mp4"

# Create a VideoCapture object
cap = cv2.VideoCapture(vid)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


ret, frame = cap.read()


if ret:

    h, w, l = frame.shape


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    Hist_eq = "Hist_equalized.mp4"
    out = cv2.VideoWriter(Hist_eq, fourcc, 20.0, (w, h))


    while True:
        ret, frame = cap.read()

        if not ret:
            print("No more frames to read or failed to read frame.")
            break

        b_channel, g_channel, r_channel = cv2.split(frame)#equalizing histograms on each of the three channels
        b_eq = cv2.equalizeHist(b_channel)
        g_eq = cv2.equalizeHist(g_channel)
        r_eq = cv2.equalizeHist(r_channel)


        img_eq_color = cv2.merge((b_eq, g_eq, r_eq))

        
        out.write(img_eq_color)

    print(f"Video saved as {Hist_eq}")

else:
    print("Error: Could not read the first frame.")

# Release
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
