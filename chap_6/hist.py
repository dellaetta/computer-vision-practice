import cv2
import logging
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("dataset/plant_one.png")

if img is None:
    logging.error(" Error loading image")
    sys.exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(img.ravel(), bins=256, range=(0, 256), color='black')
plt.show()