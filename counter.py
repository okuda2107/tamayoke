from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state

if TYPE_CHECKING:
    from game import Game

class Counter(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.cores: list[Core] = []
        self.pointers: list[Pointer] = []
        self.counter = Actor(self.game)
        self.counter.position = self.game.screen_size * [0.45, 0.4]
        self.counter_text = TextComponent(self.counter, 100)
        self.counter_text.set_color((255, 255, 255))
        self.counter_text.set_font('asset/DSEG14ClassicMini-Italic.ttf')
        self.counter_text.set_text('3')
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
