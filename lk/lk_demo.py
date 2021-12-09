import cv2
import numpy as np

import cv2
import numpy as np
from typing import NamedTuple



class TRacker():
    def __init__(self):
        self.frame = None
        self.frame_gray = None
        self.old_gray = None
        self.p0 = None
        self.roi = None
        self.feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

    def click_and_crop(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            offset = 10
            x0 = max(0, x-offset)
            y0 = max(0, y-offset)
            x1 = min(600, x+offset)
            y1 = min(400, y+offset)
            self.roi = ROI(x0,x1,y0,y1)
            # track_frame = self.frame_gray[y0:y1, x0:x1]
            # self.old_gray = self.frame_gray.copy()
            # self.p0 = cv2.goodFeaturesToTrack(track_frame, mask=None, **self.feature_params)
            # for i in range(self.p0.shape[0]):
            #     self.p0[i][0][0] = self.p0[i][0][0] + x
            #     self.p0[i][0][1] = self.p0[i][0][1] + y

            # print(self.p0)

    def lucas_kanade_method(self, video_path):
        cap = cv2.VideoCapture(video_path)
        # params for ShiTomasi corner detection
        
        # Parameters for lucas kanade optical flow
        lk_params = dict(
            winSize=(15, 15),
            maxLevel=2,
            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
        )
        # Create some random colors
        color = np.random.randint(0, 255, (100, 3))
        # Take first frame and find corners in it
        ret, old_frame = cap.read()
        self.old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        # self.p0 = cv2.goodFeaturesToTrack(self.old_gray, mask=None, **self.feature_params)
        # Create a mask image for drawing purposes
        mask = np.zeros_like(old_frame)
        # Blue color in BGR
        color = (255, 0, 0)
        
        # Line thickness of 2 px
        thickness = 2
        
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        
        while True:
            ret, self.frame = cap.read()
            if not ret:
                break
            self.frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            # calculate optical flow
            if self.p0 is not None:
                self.frame = cv2.rectangle(self.frame, self.roi.p0, self.roi.p1, color, thickness)
                p1, st, err = cv2.calcOpticalFlowPyrLK(
                    self.old_gray, self.frame_gray, self.p0, None, **lk_params
                )
                # Select good points
                good_new = p1[st == 1]
                good_old = self.p0[st == 1]
                
                # draw the tracks
                for i, (new, old) in enumerate(zip(good_new, good_old)):
                    a, b = new.ravel()
                    a, b = int(a), int(b)
                    c, d = old.ravel()
                    c, d = int(c), int(d)
                    mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
                    self.frame = cv2.circle(self.frame, (a, b), 5, color[i].tolist(), -1)
                self.frame = cv2.add(self.frame, mask)
                self.p0 = good_new.reshape(-1, 1, 2)
            cv2.imshow("image", self.frame)
            k = cv2.waitKey(500) & 0xFF
            if k == 27:
                break
            if k == ord("c"):
                mask = np.zeros_like(old_frame)
            # Now update the previous frame and previous points
            self.old_gray = self.frame_gray.copy()
            
    

    


if __name__ == "__main__":
    cv2.namedWindow("image")
    t = TRacker()
    cv2.setMouseCallback("image", t.click_and_crop)
    t.lucas_kanade_method("/home/user/projects/opencv_cookbook/lk/traffic.mp4")
    cv2.destroyAllWindows()