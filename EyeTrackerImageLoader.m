import numpy as np
import matplotlib.pyplot as plt
import cv2

class EyeTrackerImageLoader:

    def __init__(self, mode):
        # If mode is 0, the class will load files
        # If mode is 1, the class will take captures
        self.mode = mode;

    def getImage(self, cameraNumber)
        # cameraNumber 1 is left camera
        # cameraNumber 2 is right camera
        
        if mode=0:
            if cameraNumber=1:
	            img = cv2.imread('eye_image.jpg');
            else:
	            img = cv2.imread('eye_image.jpg');
        else
            if cameraNumber=1:
	            img = cv2.videocapture(camera1); # modify so it is correct
            else:
	            img = cv2.videocapture(camera2); # modify so it is correct




  





