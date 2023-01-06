from PIL import Image, ImageDraw
import face_recognition
import cv2
import math

image_path = "/home/adam/PycharmProjects/facialRecognition/zygomaticus.jpg"
new_image = "/home/adam/PycharmProjects/facialRecognition/test.jpg"
image_output = Image.open(image_path)
test_image = ImageDraw.Draw(image_output)

image = face_recognition.load_image_file(image_path)
face_landmarks_list = face_recognition.face_landmarks(image)

# List of each landmark used below.
landmarks = ['chin', 'left_eyebrow', 'right_eyebrow', 'top_lip', 'bottom_lip',
             'left_eye', 'right_eye', 'nose_bridge', 'nose_tip']

for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        test_image.line(face_landmarks[facial_feature], width=5, fill="cyan")

# Palpebral Fissure Length (PFL)
test_image.line([face_landmarks_list[0]["left_eye"][0],
                 face_landmarks_list[0]["left_eye"][3]], width=5, fill="violet")
test_image.line([face_landmarks_list[0]["right_eye"][0],
                 face_landmarks_list[0]["right_eye"][3]], width=5, fill="violet")
pfl_left = math.sqrt(pow(face_landmarks_list[0]["left_eye"][3][0] -
                         face_landmarks_list[0]["left_eye"][0][0], 2) +
                     pow(face_landmarks_list[0]["left_eye"][3][1] -
                         face_landmarks_list[0]["left_eye"][0][1], 2))
pfl_right = math.sqrt(pow(face_landmarks_list[0]["right_eye"][3][0] -
                          face_landmarks_list[0]["right_eye"][0][0], 2) +
                      pow(face_landmarks_list[0]["right_eye"][3][1] -
                          face_landmarks_list[0]["right_eye"][0][1], 2))
pfl = max(pfl_left, pfl_right)
pix_mm = 28.2875 / pfl  # Avg. PFL = 28.2875mm

# Zygomaticus Major (ZMM)
test_image.line([face_landmarks_list[0]["chin"][0],
                 face_landmarks_list[0]["top_lip"][0]], width=5, fill="violet")
test_image.line([face_landmarks_list[0]["chin"][16],
                 face_landmarks_list[0]["top_lip"][6]], width=5, fill="violet")
zmm_left = math.sqrt(pow(face_landmarks_list[0]["chin"][0][0] -
                         face_landmarks_list[0]["top_lip"][0][0], 2) +
                     pow(face_landmarks_list[0]["chin"][0][1] -
                         face_landmarks_list[0]["top_lip"][0][1], 2))
zmm_right = math.sqrt(pow(face_landmarks_list[0]["chin"][16][0] -
                          face_landmarks_list[0]["top_lip"][6][0], 2) +
                      pow(face_landmarks_list[0]["chin"][16][1] -
                          face_landmarks_list[0]["top_lip"][6][1], 2))
zmm = max(zmm_left, zmm_right) * pix_mm
print(zmm)

image_output.save(new_image)