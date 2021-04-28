import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#if selecting a second camera, pass 1\

cv2.namedWindow('left eye')
cv2.createTrackbar('threshold', 'left eye', 0, 255, nothing)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    
    # Our operations on the frame come here
    # if needed:
    #ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('left eye',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
