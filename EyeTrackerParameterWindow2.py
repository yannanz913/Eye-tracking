import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
import numpy as np
import matplotlib.pyplot as plt
import cv2

class EyeTrackerParameterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        
    def initUI(self):
        
        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Input Parameters')

        label1 = QLabel("Enter parameters for detecting pupil:")
        param1 = QLabel('Pupil_Param1')
        param2 = QLabel('Pupil_Param2')
        minRadius = QLabel('Pupil_minRadius')
        maxRadius = QLabel('Pupil_maxRadius')
        Threshold = QLabel('Pupil_Threshold')

        label2 = QLabel("Enter parameters for detecting glints:")
        minThreshold = QLabel('Glints_minThreshold')
        maxThreshold = QLabel('Glints_maxThreshold')
        minArea = QLabel('Glints_minArea')
        minCircularity = QLabel('Glints_minCircularity')
        minConvexity = QLabel('Glints_minConvexity')
        minInertiaRatio = QLabel('Glints_minInertiaRatio')

        self.param1Edit = QLineEdit()
        self.param2Edit = QLineEdit()
        self.minRadiusEdit = QLineEdit()
        self.maxRadiusEdit = QLineEdit()
        self.ThresholdEdit = QLineEdit()
        self.minThresholdEdit = QLineEdit()
        self.maxThresholdEdit = QLineEdit()
        self.minAreaEdit = QLineEdit()
        self.minCircularityEdit = QLineEdit()
        self.minConvexityEdit = QLineEdit()
        self.minInertiaRatioEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 2)
        
        grid.addWidget(param1, 1, 0)
        grid.addWidget(self.param1Edit, 1, 1)

        grid.addWidget(param2, 2, 0)
        grid.addWidget(self.param2Edit, 2, 1)

        grid.addWidget(minRadius, 3, 0)
        grid.addWidget(self.minRadiusEdit, 3, 1)

        grid.addWidget(maxRadius, 4, 0)
        grid.addWidget(self.maxRadiusEdit, 4, 1)

        grid.addWidget(Threshold, 5, 0)
        grid.addWidget(self.ThresholdEdit, 5, 1)

        grid.addWidget(minThreshold, 1, 2)
        grid.addWidget(self.minThresholdEdit, 1, 3)

        grid.addWidget(maxThreshold, 2, 2)
        grid.addWidget(self.maxThresholdEdit, 2, 3)

        grid.addWidget(minArea, 3, 2)
        grid.addWidget(self.minAreaEdit, 3, 3)

        grid.addWidget(minCircularity, 4, 2)
        grid.addWidget(self.minCircularityEdit, 4, 3)

        grid.addWidget(minConvexity, 5, 2)
        grid.addWidget(self.minConvexityEdit, 5, 3)

        grid.addWidget(minInertiaRatio, 6, 2)
        grid.addWidget(self.minInertiaRatioEdit, 6, 3)

        
        self.pybutton = QPushButton('OK', self)
        grid.addWidget(self.pybutton, 7, 3)
        self.pybutton.clicked.connect(self.clickMethod_ok)        

        self.setLayout(grid)
        

    def clickMethod_ok(self,type):
        type.cv2.HoughCircles()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EyeTrackerParameterWindow()
    mainWin.show()
    sys.exit( app.exec_() )        

    
class EyeDetector:

    def pupil_detector(self):
        img = cv2.imread("/Users/elainezhu/Desktop/VH lab/rat eye.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cimg = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                param1=50,param2=50,minRadius=0,maxRadius=0)
        pupil_detector = circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('detected pupil',img)

        cv2.waitKey(0)

        return img

