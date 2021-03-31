
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QSettings, QPoint
from PyQt5.QtGui import QIcon, QPixmap
import inspect
import numpy as np
import matplotlib.pyplot as plt
import cv2


class EyeTrackerParameterWindow(QWidget):
    
    def __init__(self, parent = None):
        super().__init__()
        self.initUI()
        self.UpdateClicked = False;
        self.PupilParams = { "Pupil_Param1": 0, "Pupil_Param2": 0, "Pupil_minRadius":0, "Pupil_maxRadius": 1, "Pupil_Threshold": 1};
        self.GlintsParams = { "Glints_minThreshold": 0, "Glints_maxThreshold": 0, "Glints_minArea":0, "Glints_minCircularity": 1, "Glints_minConvexity": 1, "Glints_minInertiaRatio": 1}
        self.SetPupilParams(self.PupilParams);
        self.SetGlintsParams(self.GlintsParams);


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
        global clicked
        if self.pybutton.isEnabled():
            p = self.getparams();
            print(p)
            self.UpdateClicked = True
        else:
            self.UpdateClicked = False


    def getparams(self):
        pupilParams = {
           "Pupil_Param1": 0,
           "Pupil_Param2": 0,
           "Pupil_minRadius": 0,
           "Pupil_maxRadius": 0,
           "Pupil_Threshold": 0
        }
        pupilParams['Pupil_Param1'] = int(self.param1Edit.text());
        pupilParams['Pupil_Param2'] = int(self.param2Edit.text());
        pupilParams['Pupil_minRadius'] = int(self.minRadiusEdit.text());
        pupilParams['Pupil_maxRadius'] = int(self.maxRadiusEdit.text());
        pupilParams['Pupil_Threshold'] = int(self.ThresholdEdit.text());
    
        glintsParams = {
           "Glints_minThreshold": 0,
           "Glints_maxThreshold": 0,
           "Glints_minArea": 0,
           "Glints_minCircularity": 0,
           "Glints_minConvexity": 0,
           "Glints_minInertiaRatio": 0
        }
        glintsParams['Glints_minThreshold'] = int(self.minThresholdEdit.text());
        glintsParams['Glints_maxThreshold'] = int(self.maxThresholdEdit.text());
        glintsParams['Glints_minArea'] = int(self.minAreaEdit.text());
        glintsParams['Glints_minCircularity'] = int(self.minCircularityEdit.text());
        glintsParams['Glints_minConvexity'] = int(self.minConvexityEdit.text());
        glintsParams['Glints_minInertiaRatio'] = int(self.minInertiaRatioEdit.text());
        
        return(pupilParams,glintsParams)

    def SetPupilParams(self, pupilParams):
        self.PupilParams['Pupil_Param1'] = pupilParams['Pupil_Param1'];
        self.PupilParams['Pupil_Param2'] = pupilParams['Pupil_Param2'];
        self.PupilParams['Pupil_minRadius'] = pupilParams['Pupil_minRadius'];
        self.PupilParams['Pupil_maxRadius'] = pupilParams['Pupil_maxRadius'];
        self.PupilParams['Pupil_Threshold'] = pupilParams['Pupil_Threshold'];

        
        # Set the text boxes to have the parameters specified
        self.param1Edit.setText(str(self.PupilParams['Pupil_Param1']));
        self.param2Edit.setText(str(self.PupilParams['Pupil_Param2']));
        self.minRadiusEdit.setText(str(self.PupilParams['Pupil_minRadius']));
        self.maxRadiusEdit.setText(str(self.PupilParams['Pupil_maxRadius']));
        self.ThresholdEdit.setText(str(self.PupilParams['Pupil_Threshold']));


    def SetGlintsParams(self, glintsParams):
        self.GlintsParams['Glints_minThreshold'] = glintsParams['Glints_minThreshold'];
        self.GlintsParams['Glints_maxThreshold'] = glintsParams['Glints_maxThreshold'];
        self.GlintsParams['Glints_minArea'] = glintsParams['Glints_minArea'];
        self.GlintsParams['Glints_minCircularity'] = glintsParams['Glints_minCircularity'];
        self.GlintsParams['Glints_minConvexity'] = glintsParams['Glints_minConvexity'];
        self.GlintsParams['Glints_minInertiaRatio'] = glintsParams['Glints_minInertiaRatio'];

        self.minThresholdEdit.setText(str(self.GlintsParams['Glints_minThreshold']));
        self.maxThresholdEdit.setText(str(self.GlintsParams['Glints_maxThreshold']));
        self.minAreaEdit.setText(str(self.GlintsParams['Glints_minArea']));
        self.minCircularityEdit.setText(str(self.GlintsParams['Glints_minCircularity']));
        self.minConvexityEdit.setText(str(self.GlintsParams['Glints_minConvexity']));
        self.minInertiaRatioEdit.setText(str(self.GlintsParams['Glints_minInertiaRatio']));        
    
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
                                param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)
        pupil_detector = circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('detected pupil',img)

        cv2.waitKey(0)

        return img
