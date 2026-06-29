import cv2
import logging
import sys
import numpy as np

trans = 0.4

# create go and stop layers
def stoplayer(frame, h, w, div=5):
    overlay = frame.copy()

    points = np.array([ (2*w//div, h//div), (3*w//div, h//div), (4*w//div, 2*h//div), (4*w//div, 3*h//div), 
        (3*w//div, 4*h//div), (2*w//div, 4*h//div), (1*w//div, 3*h//div), (1*w//div, 2*h//div)], dtype=np.int32)

    cv2.fillPoly(overlay, [points], (0, 0, 255))
    cv2.putText(overlay, "STOP", (w//2 - 80, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255, 255), 3, cv2.LINE_AA)
    overlay = cv2.addWeighted(overlay, trans, frame, 1 - trans, 0)

    return overlay

def golayer(frame, h, w):
    overlay = frame.copy()

    cv2.circle(overlay, (w//2, h//2), 200, (0, 255, 0), thickness=-1)
    cv2.putText(overlay, "GO", (w//2, h//2), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255, 255), 3, cv2.LINE_AA)

    overlay = cv2.addWeighted(overlay, trans, frame, 1 - trans, 0)

    return overlay

cam = cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
ret, frame = cam.read()
if not ret:
    logging.error(" Issue with camera")
    sys.exit()

h, w = frame.shape[:2]
screensize = h * w
divsor = 5
threshold = 230
min_blob = .007 * screensize
max_blob = .10 * screensize

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error(" Issue with camera")
        break
    frame = cv2.flip(frame, 1)

    # convert to binary
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary_frame = cv2.threshold(gray_frame, 220, 255, cv2.THRESH_BINARY)

    # find blobs
    contours, _ = cv2.findContours(binary_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    blobs = [
        c for c in contours
        if min_blob <= cv2.contourArea(c) <= max_blob
    ]

    for b in blobs:
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [b], 255)

        mean_bgr = cv2.mean(frame, mask=mask)[:3]
        avg_color = sum(mean_bgr)/3

        if avg_color >= threshold:
            draw_frame = stoplayer(frame, h, w)
        else: 
            draw_frame = golayer(frame, h, w)
            #draw_frame = cv2.drawContours(draw_frame, blobs, -1, (0, 255, 0), 2)

    cv2.imshow("Live camera", draw_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()

"""
Notes:
    Thresholds VERY finicky, if having issues play with the blob sizes and thresholds
"""