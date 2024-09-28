from __future__ import annotations
from typing import TYPE_CHECKING
from text_component import TextComponent
from actor import Actor, state
import level_loader

if TYPE_CHECKING:
    from game import Game

class Result(Actor):
    def __init__(self, game: Game, text: str):
        super().__init__(game)
        self.position = self.game.screen_size * [0.25, 0.4]
        tc = TextComponent(self, 100)
        tc.set_font('asset/DSEG14ClassicMini-Italic.ttf')
        tc.set_color((255, 255, 255))
        tc.set_text(text)
        self.timer = 0

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.timer += delta_time
        if self.timer > 3:
            self.state = state.dead
            level_loader.load_level(self.game, 'asset/entrypoint.json')
