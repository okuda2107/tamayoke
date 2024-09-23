import mediapipe as mp
import cv2

class MediapipeInput:
    def __init__(self, cam_num):
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
            static_image_mode=False, #Falseにしたら最初に捉えた人物にlandmarkを置き続けて処理が軽くなる？
        )
        self.cap = cv2.VideoCapture(cam_num)

    def initialize(self) -> bool:
        if not self.cap.isOpened():
            print('failed to initialize camera')
            return False
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
        self.result = self.pose.process(image)

def camera_check():
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    # For webcam input:
    holistic = mp_holistic.Holistic(
        min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = holistic.process(image)
        # Draw landmark annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        cv2.imshow('MediaPipe Holistic', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    holistic.close()
    cap.release()

# camera_check()
