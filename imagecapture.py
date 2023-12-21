import cv2
import dlib
import os

# Create a directory to store captured images
output_directory = "captured_images"
os.makedirs(output_directory, exist_ok=True)

# Initialize dlib's face detector
detector = dlib.get_frontal_face_detector()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Counter for captured images
image_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    # Draw rectangles around the faces
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Image Capture', frame)

    # Check for key press (press 'q' to exit the loop)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        # Save the captured image
        image_count += 1
        image_filename = os.path.join(output_directory, f"captured_image_{image_count}.jpg")
        cv2.imwrite(image_filename, frame)
        print(f"Image captured and saved as {image_filename}")

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
