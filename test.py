from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from actor import Actor
from sprite_component import SpriteComponent
import pygame
import numpy as np
from mediapipe_input import MediapipeInput
from pose import Pose
from pointer import Pointer

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        # actor = Pointer(self.game, 15)
        # sc = SpriteComponent(actor)
        # sc.set_image('asset/pointer.png', (20, 20))
        p = Pose(self)

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)
