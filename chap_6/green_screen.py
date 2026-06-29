import cv2
import logging
import sys
import numpy as np

# get background color
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
ret, frame = cam.read()
if not ret:
    logging.error(" Issue with camera")
    sys.exit()

# change depending on desired color
bgcolor = frame[700, 640]
bgcolor = (0,0,0)

img = cv2.imread("dataset/pigeon.jpg")
if img is None:
    logging.error(" Error image not found")
    sys.exit()

h, w = frame.shape[:2]
img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
print(img.shape[:2])

# live camera
while True:

    ret, frame = cam.read()
    if not ret:
        logging.error(" Issue with camera")
        break

    # get mask
    frame = cv2.flip(frame, 1)
    dist = cv2.absdiff(frame, bgcolor)
    dist = cv2.cvtColor(dist, cv2.COLOR_BGR2GRAY)
    mask = cv2.cvtColor(((dist > 50).astype(np.uint8) * 255), cv2.COLOR_GRAY2BGR)

    # get shirt
    bg = cv2.subtract(img, mask)
    not_bg = cv2.subtract(frame, cv2.bitwise_not(mask))
    frame = cv2.add(bg, not_bg)

    cv2.imshow("Live camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()