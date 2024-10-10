from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state
from text_component import TextComponent

if TYPE_CHECKING:
    from game import Game

class Counter(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = self.game.screen_size * [0.45, 0.4]
        tc = TextComponent(self, 100)
        tc.set_color((255, 255, 255))
        tc.set_font('asset/DSEG14ClassicMini-Italic.ttf')
        tc.set_text('3')
        self.start_flag = False
        self.timer = 3

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.timer -= delta_time
        if self.timer <= -1:
            self.state = state.dead
        elif self.timer <= 0:
            self.counter_text.set_text('Go!!!')
        elif self.timer <= 1:
            self.counter_text.set_text('1')
        elif self.timer <= 2:
            self.counter_text.set_text('2')
