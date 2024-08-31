from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor
from pointer import Pointer

if TYPE_CHECKING:
    from game import Game

class Title(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.pointer = [Pointer(self.game, 15), Pointer(self.game, 16)]
        self.logo = Actor(self.game)
        bc = BoxComponent()
