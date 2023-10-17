from __future__ import annotations
import numpy as np
from game import *
from text_component import *
import title

class result(Actor):
    def __init__(self, game: Game, s: str, size: int):
        super().__init__(game)
        self.position = np.array([0, 0])
        self.time = 0
        tc = TextComponent(self, 'microsoftsansserif', size)
        tc.set_text(s, (255, 255, 255))
        self.sub_text = Actor(self.game)
        tc = TextComponent(self.sub_text, 'microsoftsansserif', 30)
        tc.set_text('Your Score is', (255, 255, 255))
        self.sub_text.position = np.array([0.3, 0.1])

    def update_actor(self, delta_time: float) -> None:
        self.time += delta_time
        if self.time > 3:
            actor = title.title(self.game)
            self.state = state.dead
            self.sub_text.state = state.dead