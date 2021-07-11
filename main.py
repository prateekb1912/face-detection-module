from FaceModule import FaceDetector
import cv2
import time

cap = cv2.VideoCapture("friends.mp4")
pTime = 0

faceDetector = FaceDetector(min_detect_conf=0.85)

while True:
    _, img = cap.read()

    img = faceDetector.drawFaces(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (109, 225, 212), 3)

    cv2.imshow("Face Detection Example", img)

    if cv2.waitKey(12) == 27:
        break
