from __future__ import annotations
import math
import numpy as np
from Game import *
from Actor import *
from GravityComponent import *
from MoveComponent import *


class ball(Actor):
    def __init__(self, game: Game, radius: float):
        super().__init__(game)
        self.radius: float = radius
        gc = GravityComponent(self)
        mc = MoveComponent(self)

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
        
        # 球が線の横にあたっているか
        line_vec = np.array([math.cos(math.atan(self.rotation)), math.sin(math.atan(self.rotation))])
        b = self.position - self.game.my_bar.position
        distance = np.cross(line_vec, b)

        # 線分の時端より遠くに球が無いか
        edge_plus = line_vec * self.game.my_bar.length
        edge_minus = line_vec * self.game.my_bar.length * -1
        dot_plus = np.dot(edge_plus, self.position)
        dot_minus = np.dot(edge_minus, self.position)

        # 球が遠くにあるけど端と接触しているか
        dist_pos_to_edge_plus = edge_plus - self.position
        dist_pos_to_edge_minus = edge_minus - self.position

        if (distance <= self.radius and dot_plus >= 0 and dot_minus >= 0) or dist_pos_to_edge_plus <= self.radius or dist_pos_to_edge_minus <= self.radius:
            interval = self.game.my_bar.position - self.position # 要注意
            proj = np.dot(interval, line_vec) * line_vec
            normal = interval - proj
            normal_vel = np.dot(normal, self.velocity)
            self.velocity = self.velocity - 2 * normal_vel * normal
            
# https://yttm-work.jp/collision/collision_0006.html
# ここまで