import cv2
import logging
import sys
import numpy as np

# create go and stop layers
def stoplayer(frm, h, w, div=5):
    layer = np.zeros((h, w, 4), dtype=np.uint8)

    points = np.array([ (2*w//div, h//div), (3*w//div, h//div), (4*w//div, 2*h//div), (4*w//div, 3*h//div), 
        (3*w//div, 4*h//div), (2*w//div, 4*h//div), (1*w//div, 3*h//div), (1*w//div, 2*h//div)], dtype=np.int32)

    cv2.fillPoly(layer, [points], (0, 0, 255, 75))
    cv2.putText(layer, "STOP", (w//2 - 80, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255, 255), 3, cv2.LINE_AA)

    return layer

def golayer(frm, h, w, div=5):
    layer = np.zeros((h, w, 4), dtype=np.uint8)

    cv2.circle(frame, (w/2, h/2), 200, (0, 255, 0), thickness=-1)
    cv2.putText(layer, "G)", (w//2, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255, 255), 3, cv2.LINE_AA)

    return layer

cam = cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
ret, frame = cam.read()
if not ret:
    logging.error(" Issue with camera")
    sys.exit()

h, w = frame.shape[:2]
screensize = h * w
divsor = 5
threshold = 150
min_blob = .10 * screensize
max_blob = .80 * screensize

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error(" Issue with camera")
        break
    cv2.flip(frame, 1)

    blobs = 

    layer = golayer()

    cv2.imshow("Live camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()