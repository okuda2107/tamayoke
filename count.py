from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state
from text_component import TextComponent
from playground import PlayGround

if TYPE_CHECKING:
    from game import Game

class Count(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = [0.5, 0.5]
        self.tc = TextComponent(self, 100)
        self.color = (255, 255, 255)
        self.tc.set_text('3', self.color)
        self.timer = 3

    def __del__(self):
        super().__del__()
        del self.tc
        PlayGround(self.game)
    
    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.timer -= delta_time
        if self.timer <= -1:
            self.state = state.dead
        elif self.timer <= 0:
            self.tc.set_text('Go!!!', self.color)
        elif self.timer <= 1:
            self.tc.set_text('1', self.color)
        elif self.timer <= 2:
            self.tc.set_text('2', self.color)
