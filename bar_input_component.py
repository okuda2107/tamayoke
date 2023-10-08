from __future__ import annotations
from input_camera import *
from game import *
from actor import *
from component import *

class bar_input_component(component):
    def __init__(self, owner: actor):
        super().__init__(owner)
        self.camera = self._owner.game.input_camera
        self.output_angle: float = 0.0

    def process_input(self) -> None:
        success, image = self.camera.cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            return
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        result = self.camera.pose.process(image)
        
        if not result.pose_landmarks: return

        self.output_angle = ((result.pose_landmarks.landmark[16].y - result.pose_landmarks.landmark[15].y) * self._owner.game.screen_size[1]) / ((result.pose_landmarks.landmark[16].x - result.pose_landmarks.landmark[15].x) * self._owner.game.screen_size[0])