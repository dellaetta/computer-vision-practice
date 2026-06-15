import cv2
import logging
import sys

# load in images
img = cv2.imread("dataset/person_color.ppm")
if img is None:
    logging.error(" Color image not found")
    sys.exit()
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

depth = cv2.imread("dataset/person_depth.pgm", cv2.IMREAD_GRAYSCALE)
if depth is None:
    logging.error(" Depth image not found")
    sys.exit()
depth = cv2.rotate(depth, cv2.ROTATE_90_COUNTERCLOCKWISE)

# convert depth to binary 
#_, mask = cv2.threshold(depth, 20, 255, cv2.THRESH_BINARY_INV) # mask for background
mask = cv2.inRange(depth, 175, 200) # mask for person walking across screen
fore_only = cv2.bitwise_and(img, img, mask=mask) # remove background

cv2.imshow("Foreground", fore_only) # show result

cv2.waitKey(10000)
cv2.destroyAllWindows()

