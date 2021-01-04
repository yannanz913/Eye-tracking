import cv2
import numpy as np

im = cv2.imread("/Users/macair/Desktop/VH lab/rat eye2.png", cv2.IMREAD_GRAYSCALE)
retval, threshold = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)

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

ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
  detector = cv2.SimpleBlobDetector(params)
else:
  detector = cv2.SimpleBlobDetector_create(params)
  
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(threshold)

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
