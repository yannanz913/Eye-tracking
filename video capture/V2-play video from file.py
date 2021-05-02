import numpy as np
import cv2
cap = cv2.VideoCapture("/Users/elainezhu/Desktop/1034:4436818477654845.mp4")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("recorded video",frame)
    else:
        print("successful")
        break
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imshow('Qtcam-21_02_17:12_35_53.avi',gray)
cap.release()
cv2.destroyAllWindows()

