import mediapipe as mp
import cv2

CAMERA_NUMBER = 0

class input_camera:
    def __init__(self):
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=True,
        )
        self.cap = cv2.VideoCapture(CAMERA_NUMBER)

    def initialize(self) -> bool:
        return self.cap.isOpened()
    
    def shutdown(self) -> None:
        self.cap.release()