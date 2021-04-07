from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QPixmap

class EyeTrackerImageWindow(QDialog):
  
    def __init__(self):
        super().__init__()
        self.title = "left eye tracking"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("/Users/elainezhu/Desktop/VH lab/rat eye.png")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()

    
App = QApplication(sys.argv)
window = EyeTrackerImageWindow()
sys.exit(App.exec())
