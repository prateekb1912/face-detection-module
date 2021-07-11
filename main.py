from FaceModule import FaceDetector
import cv2
import time
import argparse

# Add command-line arguments parser
parser = argparse.ArgumentParser(
    description="Use the face detector module to use in your projects")

parser.add_argument('--video', '-V',
                    type = str, nargs = 1,
                    help = "Input video to draw detected faces on, if skipped uses the webcam",
                    default = 'webcam',
                    required = False)

parser.add_argument('--conf', '-C',
                    type = float, nargs = 1,
                    help = 'Minimum confidence required to draw faces on',
                    default=0.85,
                    required=False)

args = vars(parser.parse_args())

if args['video'] == 'webcam':
    video = 0
else:
    video = args['video'][0]

cap = cv2.VideoCapture(video)
pTime = 0

if type(args['conf']) == list:
    args['conf'] = args['conf'][0]

faceDetector = FaceDetector(min_detect_conf = args['conf'])

while True:
    _, img = cap.read()

    if video == 1:
        img = cv2.flip(img, 1)

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
