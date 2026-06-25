import cv2
import logging
import sys
import numpy as np

def check_green(img):
    h_ref = 120/2

    # convert to hsv
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # find dist
    img_h = img_hsv[:, :, 0].astype(np.int16)
    img_dist = np.abs(img_h - h_ref) 
    img_dist = np.minimum(img_dist, 180 - img_dist)
    img_vis = cv2.normalize(img_dist, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    if img_vis.mean() < 110:
        return("There is a green car")
    else:
        return("There is not a green car")


# load image
image = cv2.imread("dataset/parking_lot.jpg")
if image is None:
    logging.error(" Image failed to load")
    sys.exit()

# crop to image with green car and without
green = cv2.resize(image[250:400, 1000:1200], None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
no_green = cv2.resize(image[250:400, 0:200], None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

print(check_green(green))
print(check_green(no_green))
