import cv2
import logging
import sys

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
frame_weight = 0.2

ret, last_img = cam.read()
if not ret:
    logging.error(" Live image not captured")
    sys.exit()

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error(" Live image not captured")
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.add(cv2.multiply(frame, frame_weight), cv2.multiply(last_img, 1 - frame_weight))

    cv2.imshow("Live camera", frame)
    last_img = frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()