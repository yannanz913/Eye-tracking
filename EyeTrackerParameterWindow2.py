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

        param1Edit = QLineEdit()
        param2Edit = QLineEdit()
        minRadiusEdit = QLineEdit()
        maxRadiusEdit = QLineEdit()
        ThresholdEdit = QLineEdit()
        editFields = [param1Edit, param2Edit, minRadiusEdit, maxRadiusEdit, ThresholdEdit]
        
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(param1, 1, 0)
        grid.addWidget(param1Edit, 1, 1)

        grid.addWidget(param2, 2, 0)
        grid.addWidget(param2Edit, 2, 1)

        grid.addWidget(minRadius, 3, 0)
        grid.addWidget(minRadiusEdit, 3, 1)

        grid.addWidget(maxRadius, 4, 0)
        grid.addWidget(maxRadiusEdit, 4, 1)

        grid.addWidget(Threshold, 5, 0)
        grid.addWidget(ThresholdEdit, 5, 1)

        self.pybutton = QPushButton('OK', self)
        grid.addWidget(self.pybutton, 6, 1)
        self.pybutton.clicked.connect(self.getint)
        
        self.setLayout(grid)

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Enter Parameters For Detecting Pupil')    

    def getint(self):
        param1, done1 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'Pupilparam1')
        param2, done2 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'Pupilparam2')
        minRadius, done3 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilminRadius')
        maxRadius, done4 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilmaxRadius')
        Threshold, done5 = QtWidgets.QInputDialog.getInt(self, 'Enter Parameters For Detecting Pupil', 'PupilThreshold')
        if done1 and done2 and done3 and done4 and done5 : 
            # set parameters to be those in pupil detection function

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EyeTrackerParameterWindow()
    mainWin.show()
    sys.exit( app.exec_() )
