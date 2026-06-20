import cv2
import logging
import sys
import numpy as np

# read in image
tv = cv2.imread("dataset/tv.jpg")
if tv is None:
    logging.error(" Image not found")
    sys.exit()

# set up coordinates for tv
h, w = tv.shape[:2]
src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
tv_coor = np.float32([[182, 242], [459, 250], [460, 479], [182, 497]])

# prep warp
M = cv2.getPerspectiveTransform(src, tv_coor)

# create mask that is white where live image should be
mask = np.zeros((h, w), dtype=np.uint8)
cv2.fillPoly(mask, [tv_coor.astype(np.int32)], 255)

cam = cv2.VideoCapture(0)
disp = "Display"

while True:
    # get image from webcam
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break
    
    # warp live feed into tv
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (w, h))
    frame = cv2.warpPerspective(frame, M, (w,h))

    # add tv background
    result = tv.copy()
    result[mask == 255] = frame[mask == 255]   

    cv2.imshow(disp, result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")
cv2.destroyAllWindows()

