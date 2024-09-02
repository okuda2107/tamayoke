from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state
from text_component import TextComponent
from playground import PlayGround

if TYPE_CHECKING:
    from game import Game

class Count(Actor):
    def __init__(self, game: Game, core: int, pointer: list[int]):
        super().__init__(game)
        self.position = [0.5, 0.5]
        self.tc = TextComponent(self, 100)
        self.tc.set_color((255, 255, 255))
        self.tc.set_text('3')
        self.timer = 3
        self.core = core
        self.pointer = pointer

    def __del__(self):
        super().__del__()
    
    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.timer -= delta_time
        if self.timer <= -1:
            self.state = state.dead
            PlayGround(self.game, self.core, self.pointer)
        elif self.timer <= 0:
            self.tc.set_text('Go!!!')
        elif self.timer <= 1:
            self.tc.set_text('1')
        elif self.timer <= 2:
            self.tc.set_text('2')
