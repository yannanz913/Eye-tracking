import numpy as np
import cv2

image_color= cv2.imread("/Users/vhlab/Desktop/vlcsnap-2021-11-04-14h16m15s871.png")
image_ori = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)

lower_bound = np.array([0,0,10])
upper_bound = np.array([255,255,195])

image = image_color

mask = cv2.inRange(image_color, lower_bound, upper_bound)

# mask = cv2.adaptiveThreshold(image_ori,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY_INV,33,2)

kernel = np.ones((3, 3), np.uint8)

#Use erosion and dilation combination to eliminate false positives. 
#In this case the text Q0X could be identified as circles but it is not.
mask = cv2.erode(mask, kernel, iterations=6)
mask = cv2.dilate(mask, kernel, iterations=3)

closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[0]
def get_contour_precedence(contour, cols):     
	tolerance_factor = 10     
	origin = cv2.boundingRect(contour)     
	return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]
cols = 
contours = get_contour_precedence(contour, cols)
array = []
ii = 1
print(len(contours))
for c in contours:
    print(c)
    (x,y),r = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    r = int(r)
    if r >= 6 and r<=10:
        cv2.circle(image,center,r,(0,255,0),2)
        array.append(center)

cv2.imshow("preprocessed", image_color)
cv2.waitKey(0)
