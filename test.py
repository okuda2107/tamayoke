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
from core import Core
from enemy import Enemy
from enemy_generator import EnemyGenerator

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        parent = EnemyGenerator(self.game)
        # sc = SpriteComponent(parent)
        # sc.set_image('asset/white.png', (20, 20))
        # actor = Enemy(self.game, parent)
        # actor.mc.forward = np.array([0, 1])
        # actor = Core(self.game)
        # actor.position = [0.5, 0.5]

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)
