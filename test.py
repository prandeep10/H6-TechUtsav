import face_recognition
import cv2
import os

# Load known faces
knowns_folder = "knowns/"
known_faces = []
known_names = []

for filename in os.listdir(knowns_folder):
    image = face_recognition.load_image_file(os.path.join(knowns_folder, filename))
    face_encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(face_encoding)
    known_names.append(os.path.splitext(filename)[0])

# Initialize video capture from webcam
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1680)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 790)

# Loop through frames
while True:
    # Read frame from video capture
    ret, frame = video_capture.read()

    # Convert frame from BGR (OpenCV default) to RGB (face_recognition default)
    rgb_frame = frame[:, :, ::-1]

    # Find faces in frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through detected faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare face encoding with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        # Find best match
        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        # Draw box around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw label with name below face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.7, (255, 255, 255), 1)

    # Display resulting frame
    cv2.imshow('Video', frame)

    # Exit loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close window
video_capture.release()
cv2.destroyAllWindows()
