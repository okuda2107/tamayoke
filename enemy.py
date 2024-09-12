from __future__ import annotations
from typing import TYPE_CHECKING
import random
import numpy as np
from actor import Actor
from sprite_component import SpriteComponent
from move_and_turn_component import MoveAndTurnComponent
from collision import Sphere, AABB
from circle_component import CircleComponent, Kind

if TYPE_CHECKING:
    from game import Game
    from enemy_generator import EnemyGenerator

class Enemy(Actor):
    def __init__(self, game: Game, parent: EnemyGenerator):
        super().__init__(game)
        self.parent = parent
        self.parent.add_enemy(self)
        self.position = parent.position
        rng = np.random.default_rng()
        box = AABB(np.array([0, 0]))
        box.min_pos = [-0.1, -0.1]
        box.max_pos = [1.1, 1.1]
        mc = MoveAndTurnComponent(self, box)
        mc.speed = 0.1
        mc.set_forward(rng.uniform(-1, 1, 2))
        sc = SpriteComponent(self)
        sc.set_image('asset/white.png', (20, 20))
        cc = CircleComponent(self, Kind.enemy)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = sc.image_size[0] / self.game.screen_size[0]
        cc.set_sphere(sphere)

    def __del__(self):
        super().__del__()
        self.parent.remove_enemy(self)
