from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from actor import Actor
from sprite_component import SpriteComponent
import pygame
import numpy as np
from mediapipe_input import MediapipeInput
from pose import Pose

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        # sc = SpriteComponent(self)
        # sc.set_image('asset/pointer.png', (20, 20))
        p = Pose(self)

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)

    def actor_input(self, event) -> None:
        super().actor_input(event)
        pose = self.game.mediapipe.detect_pose()
        if pose != None:
            self.position = np.array([pose.pose_landmarks.landmark[15].x, pose.pose_landmarks.landmark[15].y])
        
    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)

