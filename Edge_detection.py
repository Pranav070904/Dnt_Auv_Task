import cv2 as cv
import numpy as np

# Open the video file
cap = cv.VideoCapture("Sharpened_vid.mp4")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the frame width, height, and frames per second (fps)
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

# Define the codec and create VideoWriter object to save the video with edges
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter("edges_output.mp4", fourcc, fps, (frame_width, frame_height), isColor=False)

while True:
    # Read the next frame
    ret, frame = cap.read()

    # Break the loop if there are no frames left
    if not ret:
        print("Finished processing video.")
        break

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv.Canny(gray, 120, 130)
    # Write the frame with edges to the output video
    out.write(edges)

    # Display the result frame with edges (optional)
    cv.imshow("Edges", edges)

    # Wait for 30 ms and break if 'q' is pressed
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects and close all OpenCV windows
cap.release()
out.release()
cv.destroyAllWindows()
