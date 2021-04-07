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
        pixmap = QPixmap("rat eye.png")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()

    
App = QApplication(sys.argv)
window = EyeTrackerImageWindow()
sys.exit(App.exec())

class EyeDetector:
    def build_pupil_detector(circles):
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                    param1=pupilParams['Pupil_Param1'], param2=pupilParams['Pupil_Param2'], minRadius=pupilParams['Pupil_minRadius'], maxRadius=pupilParams['Pupil_maxRadius'])

    def pupil_detector(img, pupil_detector):
        img = cv2.imread("rat eye.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cimg = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        pupil_detector = circles

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
        return img

    def Main():
        left_pupil_tracking = EyeTrackerImageWindow(QDialog)
        pupil_detecting = EyeDetector()
        left_pupil_tracking.InitWindow(self,pupil_detecting)
