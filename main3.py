import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from EyeTrackerParameterWindow import EyeTrackerParameterWindow

class EyeDetector:
    def built_pupil_detector(circles):
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                    param1=50,param2=50,minRadius=0,maxRadius=0)

    def pupil_detector(img, pupil_detector):
        img = cv2.imread("/Users/macair/Desktop/VH lab/rat eye.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cimg = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        pupil_detector = circles

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        return img

    def default_glint_parameters():
        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = 10
        params.maxThreshold = 255
        
        params.image_min_threshold = 200;
        params.image_max_threshold = 255;
        params.image_threshold_type = cv2.THRESH_BINARY_INV;

        params.filterByArea = True
        params.minArea = 1000

        params.filterByCircularity = True
        params.minCircularity = 0.001

        params.filterByConvexity = True
        params.minConvexity = 0.001

        params.filterByInertia = True
        params.minInertiaRatio = 0.001
        
        return params       
    
    def built_glints_detector(params)
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            glints_detector = cv2.SimpleBlobDetector(params)
        else:
            glints_detector = cv2.SimpleBlobDetector_create(params)
        return glints_detector
        
    def apply_glint_detector(img, glints_detector, params):
        retval, threshold = cv2.threshold(img, params.image_min_threshold, params.image_max_threshold, params.threshold_type);
        keypoints = glints_detector.detect(threshold)
        return keypoints;

    def main():
        global enter_new_params
        use_video_capture = false
        EyeDetector ed
        MainWindow mw
        enter_new_params = true
        glint_params = ed.default_glint_parameters()
        pupilDetector = ed.built_pupil_detector(pupil_params)
        glintDetector = ed.built_glint_detector(glint_params)
        
        if use_video_capture:
            cap = cv2.VideoCapture(0)
            
        cv2.namedWindow('image')
        cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

        while True:
            if enter_new_params:
                outParams = mw.getparams(self)
                # re-build the detectors from the parameters
                pupil_params = {"minThreshold": outParams['PupilMinThreshold'], ...
                rebuildpupilDetector = ed.built_pupil_detector(pupil_params)
                rebuildglintDetector = ed.built_glint_detector(glint_params)

                # re-build the detectors from the parameters
                
                # reads the parameters from the window, and builds the detectors
                # glint_params = (read from the window)
                
                
                enter_new_params = false
            
            if use_video_capture:
                _, frame = cap.read()
            else:
                frame = cv2.imread("/Users/macair/Desktop/VH lab/rat eye2.png", cv2.IMREAD_GRAYSCALE);
                
            pupil_frame = ed.pupil_detector(frame, pupil_detector)
            keypoints = ed.apply_glint_detector(frame, glints_detector, glint_params);
            img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            if pupil_frame is not None:
                glints_frame = ed.glints_detector(frame, glints_detector)
                threshold = cv2.getTrackbarPos('threshold', 'image')
            cv2.imshow('image', pupil_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def nothing(x):
        pass
