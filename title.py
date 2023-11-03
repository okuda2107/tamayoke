from __future__ import annotations
from typing import Any
import numpy as np
from component import Any
from game import *
from actor import *
from text_component import *
from entrypoint import *
from pointer import *

class title(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.game.audio_system.bgm('asset/Cosmic_Fantasy.mp3')

    def __del__(self):
        return super().__del__()
    
    def load_properties(self, obj: dict[str, Any]) -> None:
        super().load_properties(obj)
        start_size = obj.get('startSize')
        if start_size != None:
            actor1 = entrypoint(self.game, start_size)
        else: actor1 = entrypoint(self.game, 0.1)
        actor2 = pointer(self.game, 15, 0.01)
        actor3 = pointer(self.game, 16, 0.01)
        actor1.title = self
        actor1.pointer1 = actor2
        actor1.pointer2 = actor3