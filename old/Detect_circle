import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/Users/macair/Desktop/eye_image2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cimg = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, 
                            minDist=80, param1=110, param2=39, maxRadius=70)

for co, i in enumerate(circles[0, :], start=1):
    cv2.circle(cimg,(i[0],i[1]),2,(255,0,0),2)

plt.imshow(cimg)
plt.show()
