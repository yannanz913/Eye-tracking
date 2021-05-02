import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    _, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('left eye',frame)
cap.release()
cv2.destroyAllWindows()