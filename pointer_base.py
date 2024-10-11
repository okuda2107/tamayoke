from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from actor import Actor
from circle_sprite_component import CircleSpriteComponent
from circle_component import CircleComponent, Kind
from collision import Sphere

if TYPE_CHECKING:
    from game import Game

class PointerBase(Actor):
    def __init__(self, game: Game, index: int, kind, draw_order=100):
        super().__init__(game)
        self.index = index
        self.position = self.game.screen_size * [-1, -1]
        self.csc = CircleSpriteComponent(self, draw_order)
        self.cc = CircleComponent(self, kind)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = self.csc.radius
        self.cc.set_sphere(sphere)

    def set_radius(self, radius):
        self.csc.radius = radius
        self.cc.circle.radius = radius

    def set_color(self, color: tuple[int, int, int]):
        self.csc.color = color

    def __del__(self):
        return super().__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        if self.game.mediapipe.result.pose_landmarks != None:
            point = self.game.mediapipe.result.pose_landmarks.landmark[self.index]
            self.position = self.game.screen_size * np.array([point.x, point.y])
        else:
            self.position = self.game.screen_size * [-1, -1]
