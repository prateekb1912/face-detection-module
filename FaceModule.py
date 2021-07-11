import mediapipe as mp
import cv2

class FaceDetector():

    def __init__(self, model_selection=1, min_detect_conf=0.5):
        self.model = model_selection
        self.detection_confidence = min_detect_conf
        
        self.mpFace = mp.solutions.face_detection
        
        # Initialize the FaceDetection object with given parameters
        self.FaceDetect = self.mpFace.FaceDetection(self.detection_confidence)

        # Create a drawing utitlity object to draw the faces on image                                           
        self.mpDraw = mp.solutions.drawing_utils

    def drawFaces(self, img):

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the image through the FaceDetection object
        res = self.FaceDetect.process(img)

        if res.detections:
            for idx, detection in enumerate(res.detections):

                # Get the position of the box bounding the face
                bBoxC = detection.location_data.relative_bounding_box

                # Draw the bounding box on the image using previous details
                ih, iw, ic = img.shape
                bBox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih),\
                    int(bBoxC.width * iw), int(bBoxC.height*ih)
                
                cv2.rectangle(img, bBox, (127, 128, 0), 2)    

                # Display the prediction confidence for the bounding box
                cv2.putText(img, f"{int(detection.score[0]*100)} %",
                            (bBox[0], bBox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 128, 0), 3)
                
        return img