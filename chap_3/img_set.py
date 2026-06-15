import cv2
import logging

cam = cv2.VideoCapture(0)
cam_imgs = []

for x in range(10):
    ret, frame = cam.read()
    if ret:
        if x >= 2:
            cam_imgs.append(frame)
            cv2.waitKey(1000)
        print(f"Photo {x} taken")
    else: 
        logging.error("Photo not caputred")

for x in cam_imgs:
    cv2.imshow("Display", x)
    cv2.waitKey(3000)


cam.release()
cv2.destroyAllWindows()

