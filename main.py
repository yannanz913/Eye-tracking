import numpy as np
import matplotlib.pyplot as plt
import cv2
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
     
    def clickMethod(self, checked=True):
        for field in self.editFields:
            field.clear()
        if self.pybutton.isEnabled():
            EyeDetector.pupil_detector(img, pupil_detector)
            checked = False
        else
            checked = True
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

    
class EyeDetector:
    def build_pupil_detector(circles):
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                    param1=50,param2=50,minRadius=0,maxRadius=0)

    def pupil_detector(img, pupil_detector):
        img = cv2.imread("/Users/macair/Desktop/VH lab/rat eye.png")
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

    def build_glints_detector(params):
        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = 10
        params.maxThreshold = 255

        blur = cv2.GaussianBlur(im,(5,5),0)

        params.filterByArea = True
        params.minArea = 1000

        params.filterByCircularity = True
        params.minCircularity = 0.001

        params.filterByConvexity = True
        params.minConvexity = 0.001

        params.filterByInertia = True
        params.minInertiaRatio = 0.001

    def glints_detector(img, glints_detector):
        img = cv2.imread("/Users/macair/Desktop/VH lab/rat eye2.png", cv2.IMREAD_GRAYSCALE)
        retval, threshold = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            glints_detector = cv2.SimpleBlobDetector(params)
        else:
            glints_detector = cv2.SimpleBlobDetector_create(params)
  
        glints_detector = cv2.SimpleBlobDetector_create()
        keypoints = glints_detector.detect(threshold)

        img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return img_with_keypoints

    def main():
        cap = cv2.VideoCapture(0)
        cv2.namedWindow('image')
        cv2.createTrackbar('threshold', 'image', 0, 255, nothing)
        while True:
            _, frame = cap.read()
            pupil_frame = detect_pupil(img, glints_detector)
            if pupil_frame is not None:
                glints_frame = detect_glints(img, glints_detector)
                threshold = cv2.getTrackbarPos('threshold', 'image')
            cv2.imshow('image', pupil_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def nothing(x):
        pass
