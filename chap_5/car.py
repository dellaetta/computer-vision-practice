import cv2
import logging
import sys

img = cv2.imread("dataset/parking_lot.jpg")
if img is None:
    logging.error(" Image failed to load")
    sys.exit()

green = img[100:400, 700:1200]
no_green = img[100:400, 0:500]

h, w = img.shape[:2]
print(h)
print(w)

wind = "Display"
cv2.imshow(wind, no_green)

cv2.waitKey(10000)
cv2.destroyAllWindows()
