import numpy as np
import cv2 as cv
img = cv.imread("/home/user/projects/cv_cpp_tutorial/hello/blox.jpeg")
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
orb = cv.ORB_create()
kp = orb.detect(img,None)
print(len(kp))
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),flags=0)
cv.imshow("orb", img2)
cv.waitKey()
cv.destroyAllWindows()