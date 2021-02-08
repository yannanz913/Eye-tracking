import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

needUpdate = false;

class EyeTrackerParameterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        param1 = QLabel('param1')
        param2 = QLabel('param2')
        minRadius = QLabel('minRadius')
        maxRadius = QLabel('maxRadius')
        Threshold = QLabel('Threshold')

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

        pybutton = QPushButton('OK', self)
        grid.addWidget(pybutton, 6, 1)
        pybutton.clicked.connect(self.clickMethod)
        
        self.setLayout(grid)

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Enter Parameters For Detecting Pupil')    
     
    def clickMethod(self):
        global clicked
        for field in self.editFields:
            field.clear()
        if self.pybutton.isEnabled():
            EyeDetector.pupil_detector(img, pupil_detector)
            clicked = True
        else
            clicked = False

    def getparams(self):
        outParams = {'PupilThreshold': 0, \
            'PupilParam1': 0, \
            'PupilParam2:: 0, \  
            #and so on...
        p, okPressed = QInputDialog.getparams(self, #inputs)
        if okPressed:
            outParams['PupilThreshold'] = int(self.param1Edit.text);
            # and so on...
            #set inputs to be new params
        return outParams
	
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

    
