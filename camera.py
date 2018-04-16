import cv2
# import threading

# WHITE = [255, 255, 255]
# face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml')
# eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml')

# captured_frames = []
# processed_frames = []


# def FileRead():
#     Info = open("Names.txt", "r")  # Open th text file in readmode
#     Detail = []
#     while True:
#         Line = Info.readline()
#         # print(Line)
#         if Line == '':
#             break
#         Detail.append(Line.split(","))
#     return Detail
#
#
# Details = FileRead()
#
#
# def ID2Name(ID, conf):
#     if ID > 0 and conf > 2000:
#         NameString = Details[ID-1]
#     else:
#         NameString = [0, 'unknown', 'XXXX', 'XX-XXX', 'NO']
#
#     return NameString
#
#
# def DispID(x, y, w, h, NAME, Image, conf):
#     name = "Name: " + NAME[1]
#     # confidence = int(conf)
#     empcode = "Employee Code: " + NAME[2]
#     designation = "Designation: " + NAME[3]
#     allow = NAME[4]
#     allow = allow[:-1]
#     if allow == 'yes':
#         authorized = "Authorized"
#         color = (0, 0, 0)
#     else:
#         authorized = "Unauthorized"
#         color = (255, 255, 255)
#     # draw_box(Image, x, y, w, h, color)
#     cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     overlay = Image.copy()
#     cv2.rectangle(overlay, (x + w + 50, y), (x + w + 250, y + h), (0, 0, 255), -2)
#     cv2.rectangle(overlay, (x + w + 50, y), (x + w + 250, y + h), color, 1)
#     opacity = 0.2
#     cv2.addWeighted(overlay, opacity, Image, 1 - opacity, 0, Image)
#     cv2.putText(Image, name, (x + w + 50, y + 20), cv2.FONT_HERSHEY_DUPLEX, .4, color)
#     # cv2.putText(Image, confidence, (x + w + 50, y + 100), cv2.FONT_HERSHEY_DUPLEX, .4, color)
#     cv2.putText(Image, empcode, (x + w + 50, y + 40), cv2.FONT_HERSHEY_DUPLEX, .4, color)
#     cv2.putText(Image, designation, (x + w + 50, y + 60), cv2.FONT_HERSHEY_DUPLEX, .4, color)
#     cv2.putText(Image, authorized, (x + w + 50, y + 80), cv2.FONT_HERSHEY_DUPLEX, .4, color)
#
#
# recognise = cv2.face.EigenFaceRecognizer_create(25, 4000)  # creating EIGEN FACE RECOGNISER
# recognise.read("Recogniser/trainingDataEigan.xml")                              # Load the training data


# class VideoCamera(object):
#     def __init__(self):
#         # self.video = cv2.VideoCapture(0)
#         self.video = cv2.VideoCapture()
#         self.video.open("rtsp://admin:12345@103.59.59.10:554/h264/ch7/main/av_stream")
#
#     def __del__(self):
#         self.video.release()
#
#     # def get_frame(self):
#     #     success, image = self.video.read()
#     #     if success:
#     #         captured_frames.append(image)
#     #         print("frame captured")
#
#     def get_frame(self):
#         # success, image = self.video.read()
#         # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         # # faces = face_cascade.detectMultiScale(image, 1.3, 5)
#         # for (x, y, w, h) in faces:
#         #     gray_face = cv2.resize((gray[y:y + h, x:x + w]), (110, 110))
#         #     # gray_face = cv2.resize((image[y:y + h, x:x + w]), (110, 110))
#         #     eyes = eye_cascade.detectMultiScale(gray_face)
#         #     for (ex, ey, ew, eh) in eyes:
#         #         # draw_box(image, x, y, w, h)
#         #         cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         #         # ID, conf = recognise.predict(gray_face)  # Determine the ID of the photo
#         #         # # print("confidence= {}".format(conf))
#         #         # NAME = ID2Name(ID, conf)
#         #         # DispID(x, y, w, h, NAME, gray, conf)
#         #         # # DispID(x, y, w, h, NAME, image)
#         #
#         # ret, jpeg = cv2.imencode('.jpg', gray)
#         # return jpeg


