import numpy as np
import matplotlib.pyplot as plt
import cv2


class EyeDetector:
    def build_pupil_detector(circles):
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                        param1=pupilParams['Pupil_Param1'], param2=pupilParams['Pupil_Param2'], minRadius=pupilParams['Pupil_minRadius'], maxRadius=pupilParams['Pupil_maxRadius'])

    def pupil_detector(img, pupil_detector):
        img = cv2.imread("rat eye.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cimg = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 5)
        pupil_detector = circles

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                
        cv2.imshow('detected pupil',img)
        cv2.waitKey(0)

    def build_glints_detector(params):
        params = cv2.SimpleBlobDetector_Params()

        params.minThreshold = glintsParams['Glints_minThreshold']
        params.maxThreshold = glintsParams['Glints_maxThreshold']
    
        blur = cv2.GaussianBlur(im,(5,5),0)

        params.filterByArea = True
        params.minArea = glintsParams['Glints_minArea']

        params.filterByCircularity = True
        params.minCircularity = glintsParams['Glints_minCircularity']

        params.filterByConvexity = True
        params.minConvexity = glintsParams['Glints_minConvexity']
    
        params.filterByInertia = True
        params.minInertiaRatio = glintsParams['Glints_minInertiaRatio']

    def glints_detector(im,im_with_keypoints):
        im = cv2.imread("rat eye2.png", cv2.IMREAD_GRAYSCALE)
        retval, threshold = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)
            
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            detector = cv2.SimpleBlobDetector(params)
        else:
            detector = cv2.SimpleBlobDetector_create(params)
  
        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(threshold)

        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow("detected glints", im_with_keypoints)
        cv2.waitKey(0)

class Main:
    def main():
        cap = cv2.VideoCapture(0)
        cv2.namedWindow('image')
        cv2.createTrackbar('threshold', 'image', 0, 255, nothing)
        while True:
            _, frame = cap.read()
            pupil_frame = detect_pupil(img, glints_detector)
        if pupil_frame is not None:
            glints_frame = detect_glints(im,im_with_keypoints)
            threshold = cv2.getTrackbarPos('threshold', 'image')
        cv2.imshow('image', pupil_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()

    def nothing(x):
        pass

