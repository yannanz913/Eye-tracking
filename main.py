import numpy as np
import cv2
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QSettings, QPoint
from PyQt5.QtGui import QIcon, QPixmap
import EyeDetector
import EyeTrackerParameterWindow
from subprocess import Popen, PIPE

global enter_new_params
enter_new_params = True

ed_left = EyeDetector.EyeDetector()
App = QApplication(sys.argv)
paramWindow = EyeTrackerParameterWindow.EyeTrackerParameterWindow()

pupil_params = paramWindow.PupilParams
glint_params = paramWindow.GlintsParams

paramWindow.SetPupilParams(pupil_params)
paramWindow.SetGlintsParams(glint_params)
paramWindow.show()

pupil_paramsW,glint_paramsW = paramWindow.getparams()
print (pupil_paramsW)
# re-build the detectors from the parameters
rebuildpupilDetector = ed_left.build_pupil_detector(pupil_paramsW)
rebuildglintDetector = ed_left.build_glints_detector(glint_paramsW)

cap = cv2.VideoCapture("/Users/elainezhu/Desktop/output0708.avi")
while (cap.isOpened()):
    ret, frame = cap.read()
    # frame = frame[220:720, 650:1370]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret:
        cv2.imshow("recorded video", frame)
        ed_left.apply_pupil_detector(frame)
        ed_left.apply_glints_detector(frame)
        frame=ed_left.draw_pupil(frame)
        frame=ed_left.draw_glintpoints(frame)
        print("about to show recording video")
        cv2.imshow("recorded video", frame)

        if paramWindow.clickMethod_ok(type):
            pupil_paramsW, glint_paramsW = paramWindow.getparams()
            # re-build the detectors from the parameters
            rebuildpupilDetector = ed_left.build_pupil_detector(pupil_paramsW)
            rebuildglintDetector = ed_left.build_glints_detector(glint_paramsW)
            paramWindow.clicked = False
            enter_new_params = False
    else:
        print("successful")
        break
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # cv2.imshow('Qtcam-21_02_17:12_35_53.avi',gray)

    # p = Popen(['main.py', 'arg1'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode

# def main():
#     f= open("data stored.txt","w+")
#     for i in range(100):
#         f.write("This is line %d\r\n" % (i+1))
#     f.close()
# if __name__== "__main__":
#   main()

cap.release()
cv2.destroyAllWindows()
