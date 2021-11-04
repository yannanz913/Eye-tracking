import cv2
import numpy as np
import sys
import EyeTrackerParameterWindow
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QGridLayout, QApplication
import traceback

App = QApplication(sys.argv)
# paramWindow = EyeTrackerParameterWindow.EyeTrackerParameterWindow()

class EyeDetector:

    circles = np.uint16([])
    pupilParams = []
    glintsParams = []
    glintpoints = []

    def build_pupil_detector(self, pupilParams):
        self.pupilParams = pupilParams

    def apply_pupil_detector(self,img):
        # lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        # l, a, b = cv2.split(lab)
        # clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        # cl = clahe.apply(l)
        #
        # limg = cv2.merge((cl, a, b))
        #
        # final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        #
        # cimg = final.copy()
        # final = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
        # final = cv2.medianBlur(final, 5)
        # print(final)

        # img_thresholded =  cv2.threshold(img, pupilParams['threshold?? ?'])
        # create a trackbar instead of including img_thresholded?
        try:
            # self.pupil_circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,
            #                                   param1=['Pupil_Param1'], param2=['Pupil_Param2'], minRadius=['Pupil_minRadius'], maxRadius=['Pupil_maxRadius'])))
            print ("These are the parameters I know:")
            print(self.pupilParams)
            print ("About to call HoughCircles")
            print (self.pupilParams['Pupil_maxRadius'])

            imgf=np.zeros_like(img)
            imgt=img<100
            imgf[imgt]=img[imgt]
            self.circles = cv2.HoughCircles(imgf,cv2.HOUGH_GRADIENT, dp=self.pupilParams['Pupil_dp'], minDist=self.pupilParams['Pupil_minDist'], param1=self.pupilParams['Pupil_Param1'],
                                            param2=self.pupilParams['Pupil_Param2'],minRadius=self.pupilParams['Pupil_minRadius'],maxRadius=self.pupilParams['Pupil_maxRadius'])
            print ("Finished HoughCircles")
            # self.circles = cv2.HoughCircles(final, cv2.HOUGH_GRADIENT, 1, 50,
            #                            param1=50, param2=50, minRadius=30, maxRadius=73)
            if self.circles is not None:
                # print("circle detected")
                mycircles = np.round(self.circles[0, :]).astype("int")
                for (x, y, r) in mycircles:
                    cv2.circle(img, (x, y), r, (36, 255, 12), 3)
                for i in mycircles:
                    r = int(i[2])
                    x = int(i[0])
                    y = int(i[1])
                    # with open('data stored.txt', 'w+') as f:
                    print("center of pupil", (x, y))
                    print("radius of pupil", r)

        except:
            # with open('data stored.txt', 'w+') as f:
            traceback.print_exc()
#            print ("Unexpected error:" , sys.exc_info()[0])

    def draw_pupil(self,img):
        # check to make sure circles is not empty
        if self.circles is not None:
            # print("circle detected")
            mycircles = np.round(self.circles[0, :]).astype("int")
            for (x, y, r) in mycircles:
                cv2.circle(img, (x, y), r, (36, 255, 12), 3)
            for i in mycircles:
                r = int(i[2])
                x = int(i[0])
                y = int(i[1])
                # with open('data stored.txt', 'w+') as f:
                print("center of pupil", (x, y))
                print("radius of pupil", r)

        return img

    def build_glints_detector(self, glintsParams):
        self.glintsParams = glintsParams

    def apply_glints_detector(self, img):
        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = self.glintsParams['Glints_minThreshold']
        params.maxThreshold = self.glintsParams['Glints_maxThreshold']

        params.filterByArea = True
        params.minArea = self.glintsParams['Glints_minArea']

        params.filterByCircularity = True
        params.minCircularity = self.glintsParams['Glints_minCircularity']

        params.filterByConvexity = True
        params.minConvexity = self.glintsParams['Glints_minConvexity']

        params.filterByInertia = True
        params.minInertiaRatio = self.glintsParams['Glints_minInertiaRatio']

        # self.glintpoints = []
        print("These are the parameters I know:")
        print(self.glintsParams)

        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            self.glint_detector = cv2.SimpleBlobDetector(params)
        else:
            self.glint_detector = cv2.SimpleBlobDetector_create(params)

        print("about to call SimpleBlobDetector")
        try:
            self.glint_detector = cv2.SimpleBlobDetector_create()
            self.glintpoints = self.glint_detector.detect(img)
            for keyPoint in self.glintpoints:
                x = keyPoint.pt[0]
                y = keyPoint.pt[1]
                # with open('data stored.txt', 'w+') as f:
                print(x, y)
        except:
            # with open('data stored.txt', 'w+') as f:
            traceback.print_exc()

    def draw_glintpoints(self, img):
        img = cv2.drawKeypoints(img, self.glintpoints, np.array([]), (0, 0, 255),
                                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #cv2.imshow("Eye-tracking", img_with_glintpoints)
        return img
