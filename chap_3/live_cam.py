import cv2
import logging

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break

    cv2.imshow("Live Camera", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
