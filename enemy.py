from __future__ import annotations
from typing import TYPE_CHECKING
import random
import numpy as np
from actor import Actor
from sprite_component import SpriteComponent
from move_component import MoveComponent
from collision import Sphere
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
        mc = MoveComponent(self)
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
