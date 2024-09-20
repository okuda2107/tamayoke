from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
import random
from actor import Actor
from collision import Sphere, AABB
from circle_sprite_component import CircleSpriteComponent
from move_and_turn_component import MoveAndTurnComponent
from circle_component import CircleComponent, Kind


if TYPE_CHECKING:
    from game import Game

class Core(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = self.game.screen_size * 0.5
        rng = np.random.default_rng()
        box = AABB(np.array([0, 0]))
        box.min_pos = self.game.screen_size * [0.2, 0.2]
        box.max_pos = self.game.screen_size * [0.8, 0.8]
        mc = MoveAndTurnComponent(self, box)
        mc.set_forward(rng.uniform(-1, 1, 2))
        mc.speed = 100
        csc = CircleSpriteComponent(self)
        csc.color = (255, 83, 182)
        csc.radius = self.game.screen_size[1] * 0.05
        cc = CircleComponent(self, Kind.core)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = csc.radius
        cc.set_sphere(sphere)

    def __del__(self):
        return super().__del__()
