import cv2
import logging
import random

cam = cv2.VideoCapture(0)
WINDOW = "Display"
cv2.namedWindow(WINDOW)
rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
counter = 0

# Inital image
for x in range(3):               
    ret, frame = cam.read()
    if ret:
        if x == 2:
            cv2.putText(frame, "Left click to save a photo", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, rand_color, 2) 
            cv2.imshow(WINDOW, frame)
            cv2.waitKey(3000)
    else: 
        logging.error("Photo not caputred")

# Left click definition
def mouse_callback(event, x, y, flags, param):
    global counter

    if event == cv2.EVENT_LBUTTONDOWN:
        filepath = "photos/photo_booth/image-" + str(counter) + ".jpg"
        cv2.imwrite(filepath, frame)
        print(f"Saved photo_{counter} to {filepath}")
        counter = counter + 1

cv2.setMouseCallback(WINDOW, mouse_callback)  

# Live
while True:
    ret, frame = cam.read()
    if not ret:
        logging.error("Photo not caputred")
        break
    
    cv2.putText(frame, f"Photos taken: {counter}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, rand_color, 2)
    cv2.imshow(WINDOW, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()