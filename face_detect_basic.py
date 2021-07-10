import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("friends.mp4")
pTime = 0 

mpFaceDetect = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

faceDetection = mpFaceDetect.FaceDetection()

while True:
    _, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for idx,detection in enumerate(results.detections):
            
            cv2.putText(img, f"{int(detection.score[0]*100)} %", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.imshow("Video", img)

    if cv2.waitKey(15) == 27:
        break
