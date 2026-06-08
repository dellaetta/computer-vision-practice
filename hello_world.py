import cv2
import logging

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION) # 0 = first webcam, 1 = second webcam

# repeat to allow camera to warm up
for _ in range(3):
    ret, frame = cam.read()

if ret:
        # ?, text, position (x,y), font scale, color, thickness
        cv2.putText(frame, "Hello World!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (199,21,133), 3) 
        cv2.imshow("Display", frame)
        cv2.waitKey(10000)
else:
    logging.error("Image not captured")

cam.release()
cv2.destroyAllWindows()
