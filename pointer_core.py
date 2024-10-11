from __future__ import annotations
from typing import TYPE_CHECKING
from pointer_base import PointerBase
from circle_component import Kind

if TYPE_CHECKING:
    from game import Game

class PointerCore(PointerBase):
    def __init__(self, game: Game, index: int):
        super().__init__(game, index, Kind.pointer_core, 120)
        self.set_radius(self.game.screen_size[1] * 0.01)
        self.set_color((255, 255, 162))
