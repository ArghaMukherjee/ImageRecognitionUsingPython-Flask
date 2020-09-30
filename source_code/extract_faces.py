import face_recognition
import pandas as pd
import sys
image1 = face_recognition.load_image_file(r'images/image1.jpg')
image2 = face_recognition.load_image_file(r'images/image2.jpg')
face_coordinates = []
face_landmarks = []
face_coordinates.append(face_recognition.face_locations(image1))
face_coordinates.append(face_recognition.face_locations(image2))

face_encodings = face_recognition.face_encodings(image1)
# face_distance = face_recognition.face_distance(image1,image2)
# face_compare = face_recognition.compare_faces(image1,image2)
face_landmarks.append(face_recognition.face_landmarks(image1))
face_landmarks.append(face_recognition.face_landmarks(image2))

# print("Face coordinates : ",face_coordinates)
# print("Face encodings :",face_encodings)
# print("Face distance :",face_distance)
# print("Face compare :",face_compare)
print(face_landmarks[0])
print(face_landmarks[1])
df = pd.DataFrame(face_landmarks)
print(df)
print(df.describe())
# df.to_csv('face_data.txt',encoding='UTF-8',sep='|')
# df.to_json('face_data.json')