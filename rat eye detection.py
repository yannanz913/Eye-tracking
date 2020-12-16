import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/Users/macair/Desktop/rat eye.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cimg = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                            param1=50,param2=50,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected the pupil',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
