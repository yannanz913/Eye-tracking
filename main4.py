import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from EyeTrackerParameterWindow import EyeTrackerParameterWindow

from EyeDetector import EyeDetector

 # Step 1: Setup the windows and detectors and variables

global enter_new_params
use_video_capture = false
EyeDetector ed
MainWindow mw
enter_new_params = true

glint_params = ed.default_glint_parameters()
pupil_params = ed.default_pupil_parameters()
pupilDetector = ed.built_pupil_detector(pupil_params)
glintDetector = ed.built_glint_detector(glint_params)

app = QApplication(sys.argv)
paramWindow = EyeTrackerParameterWindow()
paramWindow.SetPupilParams(pupil_params);
paramWindow.SetGlintParams(glint_params)
paramWindow.show()

if use_video_capture:
    cap = cv2.VideoCapture(0)
            
cv2.namedWindow('image')
cv2.createTrackbar('threshold', 'image', 0, 255, nothing)


 # Step 2: run main loop

while True:
   # Step 2.1: if the user clicked in the window, update the objects
   if paramWindow.clicked:
      outParams = mw.GetParams(self)
      # re-build the detectors from the parameters
      pupil_params = {"minThreshold": outParams['PupilMinThreshold'], ...
      rebuildpupilDetector = ed.built_pupil_detector(pupil_params)
      rebuildglintDetector = ed.built_glint_detector(glint_params)

      # re-build the detectors from the parameters
                
      # reads the parameters from the window, and builds the detectors
      # glint_params = (read from the window)
                
      ParamWindow.clicked = False
            
  # Step 2.2: get the video frame
  # grab from the video or read from disk
  if use_video_capture:
      _, frame = cap.read()
  else:
      frame = cv2.imread("/Users/macair/Desktop/VH lab/rat eye2.png", cv2.IMREAD_GRAYSCALE);
    
  # Step 2.3: detect the pupils and glints            
  #pupil_frame = ed.pupil_detector(frame, pupil_detector)
  #keypoints = ed.apply_glint_detector(frame, glints_detector, glint_params);
  #img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

  #if pupil_frame is not None:
  #   glints_frame = ed.glints_detector(frame, glints_detector)
  #   threshold = cv2.getTrackbarPos('threshold', 'image')
  #   cv2.imshow('image', pupil_frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
     break
     cap.release()
     cv2.destroyAllWindows()

