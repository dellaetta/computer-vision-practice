import cv2
import logging
import sys
import numpy as np

img = cv2.imread("dataset/pisa.jpg")
if img is None:
    logging.error(" Image not found")
    sys.exit()

h,w = img.shape[:2]
shear_x = 0.12

shear = np.float32([[1, shear_x, 0], [0, 1, 0]])
img = cv2.warpAffine(img, shear, (w, h))

cv2.imshow("Display", img) 

cv2.waitKey(10000)
cv2.destroyAllWindows()

"""
Notes
- Applies affine transform (shear)
-   x_new = x_old + shear_x ⋅ y_old
    y_new = y_old
"""