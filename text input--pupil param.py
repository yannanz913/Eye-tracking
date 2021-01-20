import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        param1 = QLabel('param1')
        param2 = QLabel('param2')
        minRadius = QLabel('minRadius')
        maxRadius = QLabel('maxRadius')

        param1Edit = QLineEdit()
        param2Edit = QLineEdit()
        minRadiusEdit = QLineEdit()
        maxRadiusEdit = QLineEdit()

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

        pybutton = QPushButton('OK', self)
        grid.addWidget(pybutton, 5, 1)
        pybutton.clicked.connect(self.clickMethod)
        
        self.setLayout(grid)

        self.setGeometry(400, 400, 450, 400)
        self.setWindowTitle('Enter Parameters For Detecting Pupil')    


            
    def clickMethod(self):

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
        
