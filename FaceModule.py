import mediapipe as mp


class FaceDetector():

    def __init__(self, model_selection=1, min_detect_conf=0.5):
        self.model = model_selection
        self.detection_confidence = min_detect_conf

        self.mpFace = mp.solutions.face_detection
        self.FaceDetect = self.mpFace.FaceDetection(self.model,
                                                    self.detection_confidence)
                                                    
