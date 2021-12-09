import numpy as np
import cv2 as cv
img = cv.imread("/home/user/projects/cv_cpp_tutorial/hello/blox.jpeg")
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(gray,None)
print(len(kp))
img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
cv.imshow("sift", img2)
cv.waitKey()
cv.destroyAllWindows()