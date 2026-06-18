import cv2
import logging
import sys
import numpy as np

tv = cv2.imread("dataset/tv.jpg")
if tv is None:
    logging.error(" Image not found")
    sys.exit()
w,h = tv.shape[:2]

src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
tv_coor = np.float32([[221, 130], [341, 130], [341, 202], [212, 208]])
h,w = tv.shape[:2]

mask = np.ones((h, w), dtype=np.uint8) * 255
M = cv2.getPerspectiveTransform(src, tv_coor)
mask = cv2.warpPerspective(mask, M, (w, h))

cv2.imshow("Display", mask)

cv2.waitKey(10000)
cv2.destroyAllWindows()


""" 
mouse_x, mouse_y = 0, 0
clicked_x, clicked_y = None, 0
current_frame = None
WINDOW = "Display"

def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    global clicked_x, clicked_y

    mouse_x, mouse_y = x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_x, clicked_y = x, y
    

cv2.namedWindow(WINDOW)
cv2.setMouseCallback(WINDOW, mouse_callback)

while True:
    frame = tv.copy()
    cv2.putText(frame, f"mouse: ({mouse_x}, {mouse_y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.putText(frame, f"clicked: ({clicked_x if clicked_x != None else 0}, {clicked_y})", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow(WINDOW, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

#cv2.waitKey(10000)
cv2.destroyAllWindows()

"""
