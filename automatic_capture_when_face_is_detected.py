import cv2
import os

# Set your desired output directory
output_directory = "/home/zero/PycharmProjects/imagecapture auto/imagecpturedautodirectory"

# Initialize image count
image_count = 0

# Load the pre-trained Haar Cascade face classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize your video capture, replace '0' with the appropriate camera index if needed
cap = cv2.VideoCapture(0)

while image_count < 20:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Save the captured image
        image_count += 1
        image_filename = os.path.join(output_directory, f"captured_image_{image_count}.jpg")
        cv2.imwrite(image_filename, frame)
        print(f"Image captured and saved as {image_filename}")

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop if 20 images have been captured
    if image_count == 20:
        break

    # Check for a key press to exit the loop
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
