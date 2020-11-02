import cv2
import numpy as np

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    img = cv2.imread(“eye image.jpg”)

    cv2.imshow('my image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    def detect_eyes(img, classifier):
        gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        eyes = cascade.detectMultiScale(gray_frame, 1.3, 5) # detect eyes
        width = np.size(image, 1) # get face frame width
        height = np.size(image, 0) # get face frame height

        for (x, y, w, h) in eyes:
            eyecenter = w/2
            eye_frame = img[y:y + h, x:x + w]


    detector_params = cv2.SimpleBlobDetector_Params()
    detector_params.filterByArea = True
    detector_params.maxArea = 1500
    detector = cv2.SimpleBlobDetector_create(detector_params)
