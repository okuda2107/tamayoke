from __future__ import annotations
from game import *
from actor import *

class bar(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.length: float = 0.0

    def __del__(self):
        super().__del__()

    def actor_input(self) -> None:
        result = self.game.mediapipe.detect_pose()
        if result != None:
            self.rotation = ((result.pose_landmarks.landmark[16].y - result.pose_landmarks.landmark[15].y) * self.game.screen_size[1]) / ((result.pose_landmarks.landmark[16].x - result.pose_landmarks.landmark[15].x) * self.game.screen_size[0])