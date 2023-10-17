from __future__ import annotations
import numpy as np
from game import *
from actor import *
from sprite_component import *
from title import *
from pointer import *
from bar import *
from ball_generator import *
from point_manager import *

class entrypoint(Actor):
    def __init__(self, game: Game, radius: float):
        super().__init__(game)
        self.position = np.array([0.5, 0.6])
        self.radius = radius
        self.pointer1: pointer
        self.pointer2: pointer
        self.title: title
        self.flag = False
        self.counter = 2
        sc = SpriteComponent(self)
        temp_radius = self.radius * self.game.screen_size[0]
        sc.set_image("asset/test.png", (temp_radius, temp_radius))

    def actor_input(self) -> None:
        if self.radius < np.linalg.norm(self.position - self.pointer1.position) and self.radius < np.linalg.norm(self.position - self.pointer2.position):
            self.flag = False
            self.counter = 2
        else:
            self.flag = True
    
    def update_actor(self, delta_time: float) -> None:
        if not self.flag: return
        print(self.counter)
        self.counter -= delta_time
        self.text = str(self.counter)
        if self.counter < 0:
            self.game.my_bar = bar(self.game)
            actor1 = ball_generator(self.game)
            actor2 = point_manager(self.game)
            self.state = state.dead
            self.title.state = state.dead
            self.pointer1.state = state.dead
            self.pointer2.state = state.dead