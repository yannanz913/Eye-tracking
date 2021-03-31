import numpy as n2
import matplotlib.pyplot as plt
import cv2
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class EyeTrackerParameterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pupil_initUI()

        self.clicked = False;
        
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
        self.pybutton.clicked.connect(self.clickMethod)
        
        self.setLayout(grid)

        self.setGeometry(500, 500, 550, 500)
        self.setWindowTitle('Enter Parameters For Detecting Pupil')    
     
    def clickMethod(self):
        global clicked
        #for field in self.editFields:
        #    field.clear()
        if self.pybutton.isEnabled():
            self.clicked = True
            p = self.getparams();
            print(p)
        else:
            self.clicked = False

    def getparams(self):
        QtWidgets.QInputDialog.setInputMode()
        outParams = {'PupilThreshold': 0, \
            'PupilParam1': 0, \
            'PupilParam2': 0, \
	    'PupilminRadius': 0, \
	    'PupilmaxRadius': 0, \
	    }
        p1 = QtWidgets.QInputDialog.getInt(self, self.param1Edit(),
                                   self.ThresholdEdit("PupilThreshold"), 0, -10000, 10000, 1, ok)
        p2 = QtWidgets.QInputDialog.getInt(self, self.param2Edit(),
                                   self.param1Edit("PupilParam1"), 0, -10000, 10000, 2, ok)
        p3 = QtWidgets.QInputDialog.getInt(self, self.param2Edit(),
                                   self.param2Edit("PupilParam2"), 0, -10000, 10000, 3, ok)
        p4 = QtWidgets.QInputDialog.getInt(self, self.param2Edit(),
                                   self.minRadiusEdit("PupilminRadius"), 0, -10000, 10000, 4, ok)
        p5 = QtWidgets.QInputDialog.getInt(self, self.param2Edit(),
                                   self.maxRadiusEdit("PupilmaxRadius"), 0, -10000, 10000, 5, ok)
	
        if ok:
    	     doubleLabel.setText(QString("$%1").arg(p1))
		#and so on...
	
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EyeTrackerParameterWindow()
    mainWin.show()
    sys.exit( app.exec_() )

    
