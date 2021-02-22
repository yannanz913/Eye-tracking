import numpy as n2
import matplotlib.pyplot as plt
import cv2
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class EyeTrackerParameterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pupil_initUI()

        
    def pupil_initUI(self):
        param1 = QLabel('PupilParam1')
        param2 = QLabel('PupilParam2')
        minRadius = QLabel('PupilminRadius')
        maxRadius = QLabel('PupilmaxRadius')
        Threshold = QLabel('PupilThreshold')

        self.param1Edit = QLineEdit()
        self.param2Edit = QLineEdit()
        self.minRadiusEdit = QLineEdit()
        self.maxRadiusEdit = QLineEdit()
        self.ThresholdEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)

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

        self.pybutton = QPushButton('OK', self)
        grid.addWidget(self.pybutton, 6, 1)
        self.pybutton.clicked.connect(self.getint)
        
        self.setLayout(grid)

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Enter Parameters For Detecting Pupil')    

    def getint(self):
        pupilParams = {
           "PupilParam1": 0,
           "PupilParam2": 0,
           "minRadiusEdit": 0,
           "maxRadiusEdit": 0,
           "Threshold": 0
        }
        glintParams = {
           "Glint1": 0,
           "Glint2": 0
        }

        threshold_string = self.ThresholdEdit.text();
        pupilParams["Threshold"] = int(threshold_string)
        print(pupilParams)
        #param1, done1 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'Pupilparam1')
        #param2, done2 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'Pupilparam2')
        #minRadius, done3 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilminRadius')
        #maxRadius, done4 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilmaxRadius')
        #Threshold, done5 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilThreshold')
        #if done1 and done2 and done3 and done4 and done5 : 
            # set parameters to be those in pupil detection function
        #    a=1
        return pupilParams;

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EyeTrackerParameterWindow()
    mainWin.show()
    sys.exit( app.exec_() )

