import cv2
import logging
import sys
import numpy as np

# load image
img = cv2.imread("dataset/parking_lot.jpg")
if img is None:
    logging.error(" Image failed to load")
    sys.exit()

# crop to image with green car and without
green = cv2.resize(img[250:400, 1000:1200], None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
no_green = cv2.resize(img[250:400, 0:200], None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)


h_ref, s_ref, v_ref = 120/2, 100, 100

# convert to hsv
green_hsv = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
no_green_hsv = cv2.cvtColor(no_green, cv2.COLOR_BGR2HSV)

# find dist
green_h = green_hsv[:, :, 0].astype(np.int16)
green_dist = np.abs(green_h - h_ref) 
green_dist = np.minimum(green_dist, 180 - green_dist)
green_vis = cv2.normalize(green_dist, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

no_green_h = no_green_hsv[:, :, 0].astype(np.int16) 
no_green_dist = np.abs(no_green_h - h_ref) 
no_green_dist = np.minimum(no_green_dist, 180 - no_green_dist)
no_green_vis = cv2.normalize(no_green_dist, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

"""
# find distance away from green
grn = np.array([53, 112, 29], dtype=np.float32)
dist = np.linalg.norm(no_green.astype(np.float32) - grn, axis=2) # calc color distance

# normalize
dist = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX)
dist = dist.astype(np.uint8)
""" 

cv2.imshow("a", green)
cv2.imshow("b", green_hsv)
cv2.imshow("c", green_vis)
cv2.imshow("e", no_green)
cv2.imshow("f", no_green_hsv)
cv2.imshow("g", no_green_vis)

cv2.waitKey(100000)
cv2.destroyAllWindows()

"""
cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
mouse_x, mouse_y = 0, 0
current_frame = None
b, g, r = 0, 0, 0
WINDOW = "Live Camera"

def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    global b, g, r
    global current_frame

    mouse_x, mouse_y = x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = current_frame[y, x]
    

cv2.namedWindow(WINDOW)
cv2.setMouseCallback(WINDOW, mouse_callback)

while True:
    frame = green.copy()
    current_frame = frame
    
    cv2.putText(frame, f"rgb: ({r}, {g}, {b})", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow(WINDOW, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()
"""
