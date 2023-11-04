from __future__ import annotations
from typing import Any
import numpy as np
from component import Any
from game import *
from text_component import *
import level_loader

class result(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = np.array([0, 0])
        self.time = 0

    def update_actor(self, delta_time: float) -> None:
        self.time += delta_time
        if self.time > 3:
            level_loader.load_level(self.game, 'asset/title.json')
            self.state = state.dead
            self.sub_text.state = state.dead

    def load_properties(self, obj: dict[str, Any]) -> None:
        super().load_properties(obj)
        score_size = obj.get('scoreSize')
        if score_size == None:
            score_size = 150
        tc = TextComponent(self, 'microsoftsansserif', score_size)
        tc.set_text(str(self.game.point), (239, 241, 250))
        text_size = obj.get('textSize')
        if text_size == None:
            text_size = 30
        self.sub_text = Actor(self.game)
        tc = TextComponent(self.sub_text, 'microsoftsansserif', text_size)
        tc.set_text('Your Score is', (239, 241, 250))
        text_pos = obj.get('textPos')
        if text_pos == None:
            text_pos = [0.3, 0.1]
        self.sub_text.position = np.array(text_pos)
        