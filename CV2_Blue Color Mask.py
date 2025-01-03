# Only blue color detection
# Note: Press ESCAPE(ESC) on keyboard to close the o/p window of this project

import cv2          # We installed 'pip install opencv-python' for cv2 package
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue color
    low_blue = np.array([94, 80, 2])  # lowest hue would be - 161,155,84( how do i found this i tested before and found this)
    high_blue = np.array([126, 255, 255])
    # mask = cv2.inRange(hsv_frame, low_red, high_red)

    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)  # we create maskk on hsv frame and then low red or high red
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("Frame", frame)
    # cv2.imshow('Red mask', mask)
    cv2.imshow('Red', blue)

    key = cv2.waitKey(1)
    if key == 27:
        break



