import numpy as np
import matplotlib.pyplot as plt
import cv2


class EyeDetector:
    # make creator here
    #   define self variables with defaults like
    #     self.pupilParams (initially set to default values)
    #     self.pupil_circles (initially set to empty)
    
    def build_pupil_detector(self, pupilParams):
        self.pupilParams = pupilParams;

    def apply_pupil_detector(self, img):
        #img_thresholded =  cv2.threshold(img, pupilParams['threshold?? ?'])
        self.pupil_circles = cv2.HoughCircles(img_thresholded,cv2.HOUGH_GRADIENT,1,50,
             param1=self.pupilParams['Pupil_Param1'], param2=self.pupilParams['Pupil_Param2'], 
             minRadius=self.pupilParams['Pupil_minRadius'], maxRadius=self.pupilParams['Pupil_maxRadius'])

    def draw_pupil(self, img):
        # draw the pupil on the img
        return img;

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

        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            self.glint_detector = cv2.SimpleBlobDetector(params)
        else:
            self.glint_detector = cv2.SimpleBlobDetector_create(params)

    def apply_glint_detector(self, img):
        threshold_img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)  # steve wonders if 200 needs to be parameter?
        self.glintpoints = self.glint_detector.detect(threshold_img)

    def draw_glintpoints(self, img):
        img_with_glintpoints = cv2.drawKeypoints(img, self.glintpoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return img_with_keypoints

