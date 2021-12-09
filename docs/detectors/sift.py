import numpy as np
import cv2 as cv
img = cv.imread("/home/user/projects/cv_cpp_tutorial/hello/blox.jpeg")
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray,None)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("sift", img)
cv.waitKey()
cv.destroyAllWindows()