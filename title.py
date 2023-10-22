from __future__ import annotations
import numpy as np
from game import *
from actor import *
from text_component import *
from entrypoint import *
from pointer import *

class title(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        sc = SpriteComponent(self)
        sc.set_image('asset/title.png', tuple(self.game.screen_size * np.array([0.5, 0.6])))
        # actor1 = entrypoint(self.game, 0.1)
        # actor2 = pointer(self.game, 15, 0.01)
        # actor3 = pointer(self.game, 16, 0.01)
        # actor1.title = self
        # actor1.pointer1 = actor2
        # actor1.pointer2 = actor3

    def __del__(self):
        return super().__del__()