import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread("/Users/vhlab/Desktop/vlcsnap-2021-11-04-14h16m15s871.png")
imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#make picture gray
blurred = cv2.GaussianBlur(imgg, (7, 7), 0)
#_, imgk = cv2.threshold(blurred, 0, 200, 0 | cv2.THRESH_OTSU)
imgk = cv2.adaptiveThreshold(blurred, 255,
	cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 10)
#imgk = cv2.erode(imgk, None, iterations=2)
#imgk = cv2.dilate(imgk, None, iterations=4)
#imgk = cv2.medianBlur(imgk, 5)
imgf=np.zeros_like(imgk)
imgt=imgk<255
imgf[imgt]=imgg[imgt]
#imgf[img]=imgg[img]
#print(imgf)
pupilParams = {"Pupil_dp": 1, "Pupil_minDist": 150, "Pupil_Param1": 30, "Pupil_Param2": 15, "Pupil_minRadius": 20, "Pupil_maxRadius": 60,
                            "Pupil_Threshold": 0}
circles = cv2.HoughCircles(imgf,cv2.HOUGH_GRADIENT, dp=pupilParams['Pupil_dp'], minDist=pupilParams['Pupil_minDist'], param1=pupilParams['Pupil_Param1'],param2=pupilParams['Pupil_Param2'],minRadius=pupilParams['Pupil_minRadius'],maxRadius=pupilParams['Pupil_maxRadius'])
print(circles)
mycircles = np.round(circles[0, :]).astype("int")
#print(circles)
#print(mycircles)
for (x, y, r) in mycircles:
                    cv2.circle(imgg, (x, y), r, (36, 255, 12), 3)
for i in mycircles:
                    r = int(i[2])
                    x = int(i[0])
                    y = int(i[1])
                    # with open('data stored.txt', 'w+') as f:
                    print("center of pupil", (x, y))
                    print("radius of pupil", r)
cv2.imshow('my image',imgk)
cv2.waitKey(0)
cv2.destroyAllWindows()
