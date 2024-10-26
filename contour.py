import cv2
import numpy as np

# Path to the input video
vid = "Thresholding_dehazed.mp4"

# Create a VideoCapture object
cap = cv2.VideoCapture(vid)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame to get video properties
ret, frame = cap.read()
if ret:
    h, w, l = frame.shape
    # Define the codec and create the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    contour_vid = "internal_contours_dehazed.mp4"
    out = cv2.VideoWriter(contour_vid, fourcc, 20.0, (w, h))

    # Process each frame
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No more frames to read or failed to read frame.")
            break

        # Convert frame to grayscale if it’s not already
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find contours
        contours, hierarchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        # Initialize an empty image to draw internal contours
        internal_contours = np.zeros_like(gray)

        # Draw internal contours
        for i in range(len(contours)):
            if hierarchy[0][i][3] != -1:  # Only draw if contour has a parent
                cv2.drawContours(internal_contours, contours, i, 255, -1)

        # Convert the internal contours image to BGR to save as video
        internal_contours_bgr = cv2.cvtColor(internal_contours, cv2.COLOR_GRAY2BGR)
        out.write(internal_contours_bgr)

        # Display the result for debugging
        cv2.imshow("Internal Contours", internal_contours_bgr)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print(f"Video saved as {contour_vid}")
else:
    print("Error: Could not read the first frame.")

# Release VideoCapture and VideoWriter objects
cap.release()
out.release()
cv2.destroyAllWindows()
