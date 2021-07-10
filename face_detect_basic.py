import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("friends.mp4")


pTime = 0 
while True:
    _, img = cap.read()

    cv2.imshow("Video", img)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {fps}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)

    if cv2.waitKey(1) == 27:
        break
