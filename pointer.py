from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from actor import Actor
from sprite_component import SpriteComponent
from circle_component import CircleComponent, Kind
from collision import Sphere

if TYPE_CHECKING:
    from game import Game

class Pointer(Actor):
    def __init__(self, game: Game, index: int):
        super().__init__(game)
        self.index = index
        self.position = [-1, -1]
        sc = SpriteComponent(self)
        sc.set_image('asset/pointer.png', (150, 150))
        cc = CircleComponent(self, Kind.pointer)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = sc.image_size[0] / self.game.screen_size[0]
        cc.set_sphere(sphere)
       
    def __del__(self):
        return super().__del__()
    
    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        if self.game.mediapipe.result.pose_landmarks != None:
            point = self.game.mediapipe.result.pose_landmarks.landmark[self.index]
            self.position = np.array([point.x, point.y])
        else:
            self.position = [-1, -1]
