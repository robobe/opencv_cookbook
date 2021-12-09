import numpy as np
from io import BytesIO
from PIL import Image
from cairosvg import svg2png
import cv2

ppath = '/home/user/projects/opencv_cookbook/arcuo/aruco-4.svg'
file = open(ppath, mode='r')
# read all lines at once
svg_data = file.read()
# close the file
file.close()



png = svg2png(bytestring=svg_data)

pil_img = Image.open(BytesIO(png)).convert('RGBA')
pil_img.save('/home/user/projects/opencv_cookbook/arcuo/aruco-4.png')

cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGBA2BGRA)
cv2.imwrite('cv.png', cv_img)