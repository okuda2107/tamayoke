from __future__ import annotations
import numpy as np
import random
from game import *
from actor import *
from sprite_component import *
from ball import *
from point_manager import *

class ball_generator(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = np.array([random.random(), 0])
        self.velocity = 0.3
        self.probability: float = 0.0
        self.point_manager: point_manager

    def __del__(self):
        return super().__del__()

    def update_actor(self, delta_time: float) -> None:
        self.position += np.array([self.velocity * delta_time, 0])
        if (self.position[0] < 0 and self.velocity < 0) or (self.position[0] > 1 and self.velocity > 0):
            self.velocity *= -1
        
        if random.random() < self.probability:
            size: float = 0.0
            if self.probability == level1:
                size = 0.2
            elif self.probability == level2:
                size = 0.15
            elif self.probability == lebel3:
                size = 0.1
            actor = ball(self.game, size)
            actor.position = self.position
            file = ''
            if random.random() < 0.5:
                actor.red_white = 1
                file = 'asset/test.png'
            else:
                actor.red_white = 2
                file = 'asset/test.png'
            sc = SpriteComponent(actor)
            temp_radius = actor.radius * self.game.screen_size[0]
            sc.set_image(file, (temp_radius, temp_radius))
            self.point_manager.ball_list.append(actor)

