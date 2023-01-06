from PIL import Image, ImageDraw  # Drawing tools
import face_recognition  # Facial Recognition
import cv2  # Neural Network

vid = cv2.VideoCapture(0)  # define a video capture object

# Compression
compression = 1  # Compression: Uncompressed = 1
decompression = 3 / compression  # Keep output frame 3x uncompressed size

# File Paths
live_path = "/home/adam/PycharmProjects/test/frame.jpg"


def raw_feed():
    raw_output = Image.open(live_path)  # Selects raw image for drawing
    raw_image = ImageDraw.Draw(raw_output)

    image = face_recognition.load_image_file(live_path)  # Gathers landmark data from raw image
    face_landmarks_list = face_recognition.face_landmarks(image)  # Turns landmark data into an array of sorts.
    for face_landmarks in face_landmarks_list:
        for facial_feature in face_landmarks.keys():
            raw_image.line(face_landmarks[facial_feature], width=1)  # How the landmarks are drawn can be changed
    raw_output.save(live_path)

    # Output raw input
    image = cv2.imread(live_path)
    enlarged = cv2.resize(image, (0, 0), fx=decompression, fy=decompression)
    cv2.imshow("Camera Input", enlarged)


while True:
    ret, frame = vid.read()  # Video capture frame

    # Raw feed
    live_frame = cv2.resize(frame, (0, 0), fx=compression, fy=compression)  # Compresses frame
    cv2.imwrite("frame.jpg", live_frame)

    # Detect face
    face_load = face_recognition.load_image_file(live_path)
    face_locations = face_recognition.face_locations(face_load)  # Gathers individual face locations in image

    # Draw landmarks
    if face_locations:  # Only performs if face is detected.
        raw_feed()
    else:
        image = cv2.imread(live_path)
        enlarged = cv2.resize(image, (0, 0), fx=decompression, fy=decompression)
        cv2.imshow("Camera Input", enlarged)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit
        break


vid.release()  # Kills all open frames
cv2.destroyAllWindows()
