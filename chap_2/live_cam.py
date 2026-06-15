import cv2
import logging

cam = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
mouse_x, mouse_y = 0, 0
clicked_x, clicked_y = None, 0
current_frame = None
b, g, r = 0, 0, 0
WINDOW = "Live Camera"

def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    global clicked_x, clicked_y
    global b, g, r
    global current_frame

    mouse_x, mouse_y = x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_x, clicked_y = x, y
        b, g, r = current_frame[y, x]
    

cv2.namedWindow(WINDOW)
cv2.setMouseCallback(WINDOW, mouse_callback)

while True:
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break

    current_frame = frame

    cv2.putText(frame, f"mouse: ({mouse_x}, {mouse_y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.putText(frame, f"clicked: ({clicked_x if clicked_x != None else 0}, {clicked_y})", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.putText(frame, f"rgb: ({r}, {g}, {b})", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    if clicked_x != None:
        cv2.circle(frame, (clicked_x, clicked_y), 10, (0, 0, 255), thickness=-1)

    cv2.imshow(WINDOW, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()
