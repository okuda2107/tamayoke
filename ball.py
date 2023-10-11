from __future__ import annotations
import math
import numpy as np
from game import *
from actor import *

class bar(actor):
    def __init__(self, game: game):
        super().__init__(game)

    def __del__(self):
        super().__del__()

# 仮
    def actor_input(self) -> None:
        contact_actors = self.game.physics.isCollision(self.sprite)
        for actor in contact_actors:
            actor_pos = np.array([actor.rect.x / self.game.screen_size[0], actor.rect.y / self.game.screen_size[1]])
            normal = self.position - actor_pos
            normal_vel = np.dot(normal, self.velocity)
            self.velocity = self.velocity - 2 * normal_vel * normal
        
        line_vec = np.array([math.cos(math.atan(self.rotation)), math.sin(math.atan(self.rotation))])
        b = self.position - self.game.my_bar.position
        distance = np.cross(line_vec, b)
        if distance <= self.sprite.radius:
            normal # 法線ベクトルどう求める？
# https://yttm-work.jp/collision/collision_0006.html
# ここまで