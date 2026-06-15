import cv2
import time

cam = cv2.VideoCapture(0)

numFrames = 10

for x in range(0, numFrames + 1):
    ret, frame = cam.read()

    if x != 0:
        filepath = "photos/time_lapse/image-" + str(x) + ".jpg"
        cv2.imwrite(filepath, frame)
        print(f"Saved photo_{x} to {filepath}")

    time.sleep(1)

cam.release()