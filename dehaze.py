import cv2
import math
import numpy as np


def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()


def apply_threshold(matrix, low_value=255, high_value=255):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)
    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)
    return matrix


def simplest_cb(img, percent):
    assert img.shape[2] == 3
    assert percent > 0 and percent < 100

    half_percent = percent / 200.0
    channels = cv2.split(img)

    out_channels = []
    for channel in channels:
        assert len(channel.shape) == 2

        height, width = channel.shape
        vec_size = width * height
        flat = channel.reshape(vec_size)
        flat = np.sort(flat)

        n_cols = flat.shape[0]
        low_val = flat[math.floor(n_cols * half_percent)]
        high_val = flat[math.ceil(n_cols * (1.0 - half_percent))]

        thresholded = apply_threshold(channel, low_val, high_val)
        normalized = cv2.normalize(thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX)
        out_channels.append(normalized)

    return cv2.merge(out_channels)


def dehaze_video(input_video, output_video, percent):
    # Open the input video
    cap = cv2.VideoCapture(input_video)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame to get video properties
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read the first frame.")
        return

    # Get the height, width, and layers (channels)
    h, w, l = frame.shape

    # Define the codec and create the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, 20.0, (w, h))

    # Loop through all the frames
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Finished processing video or failed to read frame.")
            break

        # Apply simplest color balance for dehazing
        dehazed_frame = simplest_cb(frame, percent)

        # Write the dehazed frame to the output video
        out.write(dehazed_frame)

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# Main script to process the video
if __name__ == '__main__':
    input_video = 'footage.mp4'  # Path to input video
    output_video = 'dehazed_footage.mp4'  # Path to output dehazed video
    percent = 1  # Percentage for color balance (1-100)

    # Call the dehazing function
    dehaze_video(input_video, output_video, percent)
    print(f"Video saved as {output_video}")
