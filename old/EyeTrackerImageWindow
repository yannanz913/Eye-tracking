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
        self.labelImage = QLabel(self)
        pixmap = QPixmap("rat eye.png")
        self.labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()

   def displayImage(self, img)
	# implement
        # self.labelimage = QPixmap(img);
        # self.show()
