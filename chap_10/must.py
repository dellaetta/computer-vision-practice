import cv2
import logging 
import sys

stache = cv2.imread("dataset/mustache.png")
if stache is None:
    logging.error(" Error loading in image")
    sys.exit()

nose_cascade = cv2.CascadeClassifier("dataset/haarcascade_mcs_nose.xml")
if nose_cascade is None:
    logging.error(" Error loading in nose xml")
    sys.exit()

face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    if not ret:
        logging.error("Live image not captured")
        break
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    if len(faces) > 0:
        face = max(faces, key=lambda f: f[2] * f[3], default=(0, 0, 0, 0))
        x, y, w, h = face
        frame_face = frame[y:y+h, x:x+w]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if frame_face.size > 0:
            frame_face_gray = cv2.cvtColor(frame_face, cv2.COLOR_BGR2GRAY)
            noses = nose_cascade.detectMultiScale(frame_face_gray)
            if len(noses) > 0:
                for (x, y, w, h) in noses:
                    cv2.rectangle(frame_face, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow("Display", frame_face)
        else:
            cv2.imshow("Display", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Window closed")

cam.release()
cv2.destroyAllWindows()