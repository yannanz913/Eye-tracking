from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QPixmap
import EyeDetector
import EyeTrackerImageWindow
import EyeTrackerParameterWindow


App = QApplication(sys.argv)
leftview_window = EyeTrackerImageWindow.EyeTrackerImageWindow()
rightview_window = EyeTrackerImageWindow.EyeTrackerImageWindow()
parameter_window = EyeTrackerParameterWindow.EyeTrackerParameterWindow()
sys.exit(App.exec())


 # property: leftImage, rightImage
 # Setup:
 # build a EyeTrackerParameterWindow
 # build a EyeTrackerImageWindow  for left eye, and for right eye
 # build a set of detectors EyeDetector  ??
 # 
 

 # method called 'Run'
 #    Step 1: checks to see if user has clicked in EyeTrackerParameterWindow
 #            If so, re-builds the detectors
 #    Step 2: applies the detectors to the images
 #    Step 3: stores the detected values to a file
 #    Step 4: load the next images   % should occur even if there is no click
 #      (loop repeats until user quits)





