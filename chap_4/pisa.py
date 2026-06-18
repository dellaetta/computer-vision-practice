import cv2
import logging
import sys
import numpy as np

img = cv2.imread("dataset/pisa.jpg")
if img is None:
    logging.error(" Image not found")
    sys.exit()

h,w = img.shape[:2]
shift = 35

src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
dst = np.float32([[0, 0], [w, 0], [w + shift, h], [0 + shift, h]])

warp = cv2.getPerspectiveTransform(src, dst)
img = cv2.warpPerspective(img, warp, (w, h))

cv2.imshow("Display", img) 

cv2.waitKey(10000)
cv2.destroyAllWindows()