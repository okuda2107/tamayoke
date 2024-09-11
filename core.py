from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
import random
from actor import Actor
from collision import Sphere
from sprite_component import SpriteComponent
from move_component import MoveComponent
from circle_component import CircleComponent, Kind

if TYPE_CHECKING:
    from game import Game

class Core(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        rng = np.random.default_rng()
        mc = MoveComponent(self)
        mc.set_forward(rng.uniform(-1, 1, 2))
        mc.speed = 0.1
        sc = SpriteComponent(self)
        sc.set_image('asset/red.png', (200, 200))
        cc = CircleComponent(self, Kind.core)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = sc.image_size[0] / self.game.screen_size[0]
        cc.set_sphere(sphere)

    def __del__(self):
        return super().__del__()
