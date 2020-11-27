 # Step 1: Open the image

 # Step 2: detect the eye

 # Step 3: show the location of the detected eye

 # Step 4: clean up and quit

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("../../opencv-4.4.0/data/haarcascades/haarcascade_frontalface_default.xml") #the absolute path of haarcascade_frontalface_default.xml
eye_cascade = cv2.CascadeClassifier("../../opencv-4.4.0/data/haarcascades/haarcascade_eye.xml") #the absolute path of haarcascade_eye.xml

img = cv2.imread("/Users/macair/Desktop/eye_image.jpg") # the absolute path of image
gray_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # make the image gray

eyes = eye_cascade.detectMultiScale(gray_face) # detect the eye
for (ex,ey,ew,eh) in eyes: 
    cv2.rectangle(gray_face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2) # display the eye object

cv2.imshow('eye detecting',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
