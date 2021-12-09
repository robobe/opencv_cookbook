import cv2
import numpy as np
from typing import NamedTuple

feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

class ROI(NamedTuple):
    x0: int
    x1: int
    y0: int
    y1: int

    @property
    def p1(self):
        return (self.x0,self.y0)

    @property
    def p2(self):
        return (self.x1,self.y1)

def click_and_crop(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            offset = 10
            x0 = max(0, x-offset)
            y0 = max(0, y-offset)
            x1 = min(300, x+offset)
            y1 = min(300, y+offset)
            global roi
            roi = ROI(x0,x1,y0,y1)
            track_frame = raw[y0:y1, x0:x1]
            p0 = cv2.goodFeaturesToTrack(raw, mask=None, **feature_params)
            # for i in range(p0.shape[0]):
            #     p0[i][0][0] = p0[i][0][0] + x-offset
            #     p0[i][0][1] = p0[i][0][1] + y-offset
            # cv2.imshow("frame", track_frame)
            print(p0)

roi = ROI(50,100,50,100)
raw = None
def run():
    global raw
    raw = np.zeros((300,300), np.uint8)
    while True:
        cv2.rectangle(raw, roi.p1, roi.p2, (255,0,0), 2)
        cv2.imshow("image", raw)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break


if __name__ == "__main__":
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    run()