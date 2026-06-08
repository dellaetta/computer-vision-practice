import cv2
import logging
import time

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # 0 = first webcam, 1 = second webcam
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ret, frame = cam.read()

if ret:
        cv2.imshow("Display", frame)
        cv2.waitKey(10000)
else:
    logging.exception(" An exception occurred while capturing image")

cam.release()
cv2.destroyAllWindows()
