# ballとbarが依存している
from __future__ import annotations
import math
import numpy as np
from game import *
from actor import *
from gravity_component import *
from sprite_component import *


class ball(Actor):
    def __init__(self, game: Game, radius: float):
        super().__init__(game)
        self.radius: float = radius # 縦方向の長さ
        gc = GravityComponent(self)
        sc = SpriteComponent(self)
        temp_radius = self.radius * self.game.screen_size[0]
        sc.set_image('asset/test.png', (temp_radius, temp_radius))

    def __del__(self):
        super().__del__()

# 仮
    def actor_input(self) -> None:
        contact_actors = self.game.physics.isCollision(self.sprite)
        for actor in contact_actors:
            actor_pos = np.array([actor.center.x / self.game.screen_size[0], actor.center.y / self.game.screen_size[1]])
            normal /= np.linalg.norm(self.position - actor_pos)
            normal_vel = np.dot(normal, self.velocity)
            self.velocity -= 1.5 * normal_vel * normal
        
        # 球が線の横にあたっているか
        line_vec = np.array([math.cos(math.atan(self.game.my_bar.rotation)), -1 * math.sin(math.atan(self.game.my_bar.rotation))])
        b = self.position - self.game.my_bar.position
        distance = abs(np.cross(b, line_vec))
        # 線分の時端より遠くに球が無いか
        edge_plus = self.game.my_bar.position + line_vec * self.game.my_bar.length / 2
        edge_minus = self.game.my_bar.position + line_vec * self.game.my_bar.length / 2 * -1
        dot_plus = np.dot(edge_plus, self.position)
        dot_minus = np.dot(edge_minus, self.position)

        # 球が遠くにあるけど端と接触しているか
        dist_pos_to_edge_plus = np.sum((edge_plus - self.position) ** 2)
        dist_pos_to_edge_minus = np.sum((edge_minus - self.position) ** 2)

        interval = self.game.my_bar.position - self.position # 要注意
        proj = np.dot(interval, line_vec) * line_vec
        normal = interval - proj
        x = np.linalg.norm(interval - proj)
        normal = normal / x
        
        if (distance <= self.radius and dot_plus >= 0 and dot_minus >= 0 and np.dot(normal, self.velocity) > 0) or dist_pos_to_edge_plus <= self.radius ** 2 or dist_pos_to_edge_minus <= self.radius ** 2:
            normal_vel = np.dot(normal, self.velocity)
            if normal_vel <= 0.05:
                self.position -= distance * -1 *normal
                self.position += self.radius * -1 * normal
                return
            self.velocity -= 1.3 * normal_vel * normal
            
# https://yttm-work.jp/collision/collision_0006.html
# ここまで