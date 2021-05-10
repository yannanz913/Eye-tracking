import cv2
import numpy as np
import sys

class EyeDetector:

    circles = np.uint16([]);
    pupilParams = [];

    def build_pupil_detector(self, pupilParams):
        self.pupilParams = pupilParams
        self.circles = []; 


    def apply_pupil_detector(self,img):
        # img_thresholded =  cv2.threshold(img, pupilParams['threshold?? ?'])
        # create a trackbar instead of including img_thresholded?
        try:
            self.pupil_circles = np.uint16(np.around(cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50,
                                              param1=50, param2=50, minRadius=0, maxRadius=0)))
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
