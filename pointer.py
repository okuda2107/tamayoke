from __future__ import annotations
import numpy as np
from mediapipe_input import *
from game import *
from actor import *
from sprite_component import *

class pointer(Actor):
    def __init__(self, game: Game, index: int, radius: float):
        super().__init__(game)
        self.radius = radius
        self.index = index
        sc = SpriteComponent(self)
        temp_radius = self.radius * self.game.screen_size[0]
        sc.set_image("asset/test.png", (temp_radius, temp_radius))

    def __del__(self):
        return super().__del__()

    def actor_input(self) -> None:
        pose = self.game.mediapipe.detect_pose()
        if pose != None:
            self.position = np.array([pose.pose_landmarks.landmark[self.index].x, pose.pose_landmarks.landmark[self.index].y])