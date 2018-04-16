from __future__ import division
import sys
from time import time, sleep
import threading
import cv2
import dlib
from skimage import io

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()


class webCamGrabber(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Lock for when you can read/write self.image:
        # self.imageLock = threading.Lock()
        self.image = False


        from time import time

        self.cam = cv2.VideoCapture(0)  # set the port of the camera as before
        # self.cam.set(cv.CV_CAP_PROP_FPS, 1)

    def run(self):
        while True:
            start = time()
            # self.imageLock.acquire()
            retval, self.image = self.cam.read()  # return a True bolean and and the image if all go right

            print(type(self.image))
            # import matplotlib.pyplot as plt
            # plt.imshow(image)
            # plt.show()

            # print( "readimage: " + str( time() - start ) )
            # sleep(0.1)


if len(sys.argv[1:]) == 0:

    # Start webcam reader thread:
    camThread = webCamGrabber()
    camThread.start()

    # Setup window for results
    detector = dlib.get_frontal_face_detector()
    win = dlib.image_window()

    while True:
        # camThread.imageLock.acquire()
        if camThread.image is not False:
            print("enter")
            start = time()

            myimage = camThread.image
            for row in myimage:
                for px in row:
                    # rgb expected... but the array is bgr?
                    r = px[2]
                    px[2] = px[0]
                    px[0] = r

            dets = detector(myimage, 0)
            # camThread.imageLock.release()
            print("your faces: %f" % len(dets))
            for i, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    i, d.left(), d.top(), d.right(), d.bottom()))
                print("from left: {}".format(((d.left() + d.right()) / 2) / len(camThread.image[0])))
                print("from top: {}".format(((d.top() + d.bottom()) / 2) / len(camThread.image)))
            print("process: " + str(time() - start))

            start = time()
            win.clear_overlay()
            win.set_image(myimage)
            win.add_overlay(dets)

            print("show: " + str(time() - start))
            # dlib.hit_enter_to_continue()

for f in sys.argv[1:]:
    print("Processing file: {}".format(f))
    img = io.imread(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()

# Finally, if you really want to you can ask the detector to tell you the score
# for each detection.  The score is bigger for more confident detections.
# Also, the idx tells you which of the face sub-detectors matched.  This can be
# used to broadly identify faces in different orientations.
if (len(sys.argv[1:]) > 0):
    img = io.imread(sys.argv[1])
    dets, scores, idx = detector.run(img, 1)
    for i, d in enumerate(dets):
        print("Detection {}, score: {}, face_type:{}".format(
            d, scores[i], idx[i]))
