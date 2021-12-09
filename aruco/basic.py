import numpy as np
import cv2

RED = (0,0,255)
CAMERA_ID = 2
cap = cv2.VideoCapture(CAMERA_ID)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
camera_matrix = np.array([[1300., 0., 600], [0., 1300., 480.], [0., 0., 1.]], dtype=np.float32)
dist_coeffs = np.array([-2.4, 0.95, -0.0004, 0.00089, 0.], dtype=np.float32)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, dictionary)
    
    if len(corners) > 0:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids, RED)
        rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(
            corners,
            0.02,
            camera_matrix,
            dist_coeffs)
        cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvec=rvec, tvec=tvec, length=0.01)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()