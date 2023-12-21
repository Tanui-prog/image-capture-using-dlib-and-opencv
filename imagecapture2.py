import cv2
import os

# Set your desired output directory
output_directory = ("/home/zero/PycharmProjects/imagecapture auto/image")

# Initialize image count
image_count = 0

# Initialize your video capture, replace '0' with the appropriate camera index if needed
cap = cv2.VideoCapture(0)

while image_count < 20:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Wait for the 'c' key to be pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        # Save the captured image
        image_count += 1
        image_filename = os.path.join(output_directory, f"captured_image_{image_count}.jpg")
        cv2.imwrite(image_filename, frame)
        print(f"Image captured and saved as {image_filename}")

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
