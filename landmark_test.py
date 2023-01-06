from PIL import Image, ImageDraw  # Drawing tools
import face_recognition  # Facial Recognition
import cv2  # Neural Network

vid = cv2.VideoCapture(0)  # define a video capture object

# Compression
compression = 1  # Compression: Uncompressed = 1
decompression = 3 / compression  # Keep output frame 3x uncompressed size

# File Paths
live_path = "/home/adam/PycharmProjects/facialRecognition/frame.jpg"
template_path = "/home/adam/PycharmProjects/facialRecognition/template.jpg"
output_path = "/home/adam/PycharmProjects/facialRecognition/output.jpg"
text_file = open("facial_coordinates.txt", "w+")  # Output facial data file

# Creates template
ret, frame = vid.read()
frame_size = cv2.resize(frame, (0, 0), fx=1, fy=1)
cv2.imwrite("frame.jpg", frame_size)
image = Image.open("/home/adam/PycharmProjects/facialRecognition/frame.jpg")
width, height = image.size
template = Image.new('RGB', (width, height), color='black')
template.save('template.jpg')
cv2.imwrite('template.jpg', cv2.resize(cv2.imread(template_path), (0, 0), fx=compression, fy=compression))

# List of each landmark used below.
landmarks = ['chin', 'left_eyebrow', 'right_eyebrow', 'top_lip', 'bottom_lip',
             'left_eye', 'right_eye', 'nose_bridge', 'nose_tip']


def raw_feed():
    template_output = Image.open(template_path)  # Selects output image for drawing
    template_image = ImageDraw.Draw(template_output)

    image = face_recognition.load_image_file(live_path)  # Gathers landmark data from raw image
    face_landmarks_list = face_recognition.face_landmarks(image)  # Turns landmark data into an array of sorts.
    for face_landmarks in face_landmarks_list:
        template_image.line(face_landmarks['left_eyebrow'], fill="blue", width=1)
        template_image.line(face_landmarks['right_eyebrow'], fill="blue", width=1)
        template_image.polygon(face_landmarks['top_lip'], fill="blue")
        template_image.line(face_landmarks['top_lip'], fill="blue", width=1)
        template_image.polygon(face_landmarks['bottom_lip'], fill="blue")
        template_image.line(face_landmarks['bottom_lip'], fill="blue", width=1)
        template_image.polygon(face_landmarks['left_eye'], fill="blue")
        template_image.line(face_landmarks['left_eye'], fill="blue", width=1)
        template_image.polygon(face_landmarks['right_eye'], fill="blue")
        template_image.line(face_landmarks['right_eye'], fill="blue", width=1)

        for landmark in landmarks:
            for point in face_landmarks[landmark]:
                template_image.point(point, fill="white")  # Draws dots on each landmark point

    template_output.save(output_path)

    # Output template
    image = cv2.imread(output_path)
    enlarged = cv2.resize(image, (0, 0), fx=decompression, fy=decompression)
    cv2.imshow("Output", enlarged)


# Gathers facial data on last recorded frame
def coordinate_data():
    last_image = face_recognition.load_image_file(live_path)  # Gathers landmark data from last recorded image
    face_landmarks_list = face_recognition.face_landmarks(last_image)
    for face_landmarks in face_landmarks_list:
        for landmark in landmarks:
            iteration = 1
            for point in face_landmarks[landmark]:
                output = str(landmark) + str(iteration) + ": " + str(point) + "\n"
                text_file.write(output)
                iteration += 1


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

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit
        break


coordinate_data()
text_file.close()  # Closes text file instance
vid.release()  # Kills all open frames
cv2.destroyAllWindows()
