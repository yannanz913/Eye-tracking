import cv2
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib as plt


# init part
pupilparams = cv2.SimpleBlobDetector_Params()
pupilparams.filterByArea = True
pupilparams.maxArea = 40000 # Tried using from 300 - 3000 and can't get a detection
pupilparams.minArea = 3000
pupilparams.filterByCircularity = False
pupilparams.filterByColor = False
pupilparams.filterByConvexity = False
pupilparams.filterByInertia = False
pupildetector = cv2.SimpleBlobDetector_create(pupilparams)

glintparams = cv2.SimpleBlobDetector_Params()
glintparams.filterByArea = True
glintparams.maxArea = 1000 # Tried using from 300 - 3000 and can't get a detection
glintparams.minArea = 300
glintparams.filterByCircularity = False
glintparams.filterByColor = False
glintparams.filterByConvexity = False
glintparams.filterByInertia = False
glintdetector = cv2.SimpleBlobDetector_create(glintparams)

eyeparams = cv2.SimpleBlobDetector_Params()
eyeparams.filterByArea = False
#eyeparams.maxArea = 200000 # Tried using from 300 - 3000 and can't get a detection
#eyeparams.minArea = 4000
eyeparams.filterByCircularity = False
eyeparams.filterByColor = False
eyeparams.filterByConvexity = False
eyeparams.filterByInertia = True
eyeparams.minInertiaRatio = 0.5
eyedetector = cv2.SimpleBlobDetector_create(eyeparams)


def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray_frame = gray_frame[100:300,180:420]
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    print(keypoints)
    return img,keypoints


def nothing(x):
    pass


#def main():
#    frame = cv2.imread("/Users/vhlab/Desktop/vlcsnap-2021-11-04-14h16m15s871.png")
#    img2,keypoints = blob_process(frame, 30, detector)
#    eye = cv2.drawKeypoints(frame, keypoints, frame, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#    cv2.imshow('image', frame)
#    cv2.waitKey()
#    cv2.destroyAllWindows()

def main():
    cap = cv2.VideoCapture("/Users/docviv/Desktop/MATLAB/Eye-tracking/videos/Qtcam-21_11_16_11_19_05.avi")
    while True:
        _, frame = cap.read()
        alpha = 1
        beta = 0
        frame = alpha*frame + beta
        #cv2.imshow('contrast', frame)
        pupil_img,pupil_keypoints = blob_process(frame, 90, pupildetector)
        contours, hierarchy = cv2.findContours(pupil_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for i,contour in enumerate(contours):
            if cv2.contourArea(contour) > 1000 and cv2.contourArea(contour) < 10000:
                #cv2.drawContours(frame, contours, i, (0,255,0), 3)
                ellipse = cv2.fitEllipse(contour)
                cv2.ellipse(frame,ellipse,(0,255,0),2)
        glint_img,glint_keypoints = blob_process(frame, 120, glintdetector)
        eye_img,eye_keypoints = blob_process(frame, 120, eyedetector)
        # eye_pupil = cv2.drawKeypoints(frame, pupil_keypoints, frame, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # eye_glints = cv2.drawKeypoints(frame, glint_keypoints, frame, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # eye_whole = cv2.drawKeypoints(frame, eye_keypoints, frame, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
