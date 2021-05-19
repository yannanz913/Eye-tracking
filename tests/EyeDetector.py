import cv2
import numpy as np
import sys

class EyeDetector:

    circles = np.uint16([])
    pupilParams = []
    glintsParams = []
    glintpoints = []


    def build_pupil_detector(self, pupilParams):
        self.pupilParams = pupilParams
        self.circles = []

    def apply_pupil_detector(self,img):
        # img_thresholded =  cv2.threshold(img, pupilParams['threshold?? ?'])
        # create a trackbar instead of including img_thresholded?
        try:
            self.pupil_circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,
                                              param1=['Pupil_Param1'], param2=['Pupil_Param2'], minRadius=['Pupil_minRadius'], maxRadius=['Pupil_maxRadius'])))
        except:
            print ("Unexpected error:" , sys.exc_info()[0])

    def draw_pupil(self,img):
        # check to make sure circles is not empty
        if self.circles.size:
           # draw the pupil on the img
           for i in self.circles[0, :]:
               cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
               cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
           # need to be returned using cv2.imshow
        return img

    def build_glints_detector(self, glintsParams):
        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = glintsParams['Glints_minThreshold']
        params.maxThreshold = glintsParams['Glints_maxThreshold']

        params.filterByArea = True
        params.minArea = glintsParams['Glints_minArea']

        params.filterByCircularity = True
        params.minCircularity = glintsParams['Glints_minCircularity']

        params.filterByConvexity = True
        params.minConvexity = glintsParams['Glints_minConvexity']

        params.filterByInertia = True
        params.minInertiaRatio = glintsParams['Glints_minInertiaRatio']

        self.glintpoints = []

        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            self.glint_detector = cv2.SimpleBlobDetector(params)
        else:
            self.glint_detector = cv2.SimpleBlobDetector_create(params)

    def apply_glints_detector(self, img):
        try:
            self.glintpoints = self.glint_detector.detect(img)
        except:
            print ("Unexpected error:" , sys.exc_info()[0])

    def draw_glintpoints(self, img):
        img_with_glintpoints = cv2.drawKeypoints(img, self.glintpoints, np.array([]), (0, 0, 255),
                                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return img_with_glintpoints
