import cv2
import logging
import sys
import numpy as np 

# load in image
img = cv2.imread("dataset/coins.png")
if img is None:
    logging.error(" Image failed to load")
    sys.exit()

# set up inital values
coin_counter = {0.01: 0, 0.05: 0, 0.1: 0, 0.25: 0}
min_size = 1000
diameters = np.array([
    [18.50, 0.01], # should be 19.05 but need to fix threshold
    [20.21, 0.05], # should be 21.21 but need to fix threshold
    [17.4, 0.10], # should be 17.91 but need to fix threshold
    [24.26, 0.25]
])

# find coins
working_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, working_img = cv2.threshold(working_img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(working_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
coins = [
    c for c in contours
    if min_size <= cv2.contourArea(c)
]

# use quarter to calibrate 
max_diameter = 0
for c in coins:
    diameter = 2 * np.sqrt(cv2.contourArea(c) / np.pi) 
    max_diameter = diameter if diameter > max_diameter else max_diameter

px2mm = diameters[3, 0] / max_diameter

# find the values of each coin
for c in coins:
    diameter_mm = cv2.minEnclosingCircle(c)[1] * 2 * px2mm
    dist = np.abs(diameter_mm - diameters[:, 0])
    index = np.where(dist == np.min(dist))[0][0]
    
    for key, value in list(coin_counter.items()):
        if key == diameters[index, 1]:
            coin_counter[key] += 1

# display the image
cv2.drawContours(img, coins, -1, (0, 255, 0), 3)
coin_value = sum(key * value for key, value in coin_counter.items())
img = cv2.putText(img, f"Coins value: {round(coin_value, 2)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
cv2.imshow("Display", img)
cv2.waitKey(100000)

print("Window closed")
cv2.destroyAllWindows()
