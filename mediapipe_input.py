import mediapipe as mp
import cv2

CAMERA_NUMBER = 0

class mediapipe_input:
    def __init__(self):
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=False, #Falseにしたら最初に捉えた人物にlandmarkを置き続けて処理が軽くなる？
        )
        self.cap = cv2.VideoCapture(CAMERA_NUMBER)

    def initialize(self) -> bool:
        return True
    
    def shutdown(self) -> None:
        self.cap.release()

    def detect_pose(self):
        if not self.cap.isOpened(): return
        success, image = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            return
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        result = self.pose.process(image)
        
        if not result.pose_landmarks: return
        
        return result