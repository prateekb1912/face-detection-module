import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("friends.mp4")
pTime = 0

mpFaceDetect = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

faceDetection = mpFaceDetect.FaceDetection(0.75)

while True:
    _, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for idx, detection in enumerate(results.detections):
            bBoxC = detection.location_data.relative_bounding_box

            ih, iw, ic = img.shape
            bBox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih),\
                int(bBoxC.width * iw), int(bBoxC.height*ih)
            
            cv2.rectangle(img, bBox, (127, 128, 0), 2)    
            cv2.putText(img, f"{int(detection.score[0]*100)} %",
                        (bBox[0], bBox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 128, 0), 3)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.imshow("Video", img)

    if cv2.waitKey(12) == 27:
        break
