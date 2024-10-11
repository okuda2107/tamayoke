from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from pointer_base import PointerBase
from circle_sprite_component import CircleSpriteComponent
from circle_component import CircleComponent, Kind
from collision import Sphere

if TYPE_CHECKING:
    from game import Game

class Pointer(PointerBase):
    def __init__(self, game: Game, index: int):
        super().__init__(game, index, Kind.pointer, 90)
        self.set_radius(self.game.screen_size[1] * 0.08)
        self.set_color((233, 231, 122))
