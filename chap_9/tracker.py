import cv2
import logging
import numpy as np
import math

cam = cv2.VideoCapture(0)
prev_xy = None
prev_size = 100

def findCenter(shape):
        cx = int(cv2.moments(shape)["m10"] / cv2.moments(shape)["m00"])
        cy = int(cv2.moments(shape)["m01"] / cv2.moments(shape)["m00"])
        return (cx, cy)

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break
    frame = cv2.flip(frame, 1)

    # find distance and dilate
    kernel = np.ones((3, 3), np.uint8)
    dist = cv2.cvtColor(cv2.absdiff(frame, (52,64,235)), cv2.COLOR_BGR2GRAY)
    dist = cv2.dilate(dist, kernel, iterations=2)

    # convert to binary
    _, binary = cv2.threshold(dist, 25, 255, cv2.THRESH_BINARY_INV)

    # find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if prev_size:
        x = [
            c for c in contours
            if prev_size * 0.5 <= cv2.contourArea(c)
        ]
    else:
        x = [
            c for c in contours
            if 100 <= cv2.contourArea(c)
        ]

    if x:
        if prev_xy:
            # finds the x with the smallest dist away from the previous x
            nearest = min(x, key=lambda i: math.hypot(findCenter(i)[0] - prev_xy[0], findCenter(i)[1] - prev_xy[1]))
            """
                - math.hypot finds the distance
                - m00 = area of contour
                - m10 = sum of all x-coor
                - m01 = sum of all y-coor
            """

            prev_xy = (findCenter(nearest)[0], findCenter(nearest)[1])
            prev_size = cv2.moments(nearest)["m00"]

            cv2.drawContours(frame, nearest, -1, (0, 255, 0), 3)
        else:
            prev_xy = (findCenter(x[-1])[0], findCenter(x[-1])[1])
            prev_size = prev_size = cv2.moments(x[-1])["m00"]
    else:
        cv2.putText(frame, "No x found", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        
    cv2.imshow("Display", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()