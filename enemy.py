from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
import random
from actor import Actor, state
from enemy_generator import EnemyGenerator

if TYPE_CHECKING:
    from game import Game

class Enemy(Actor):
    def __init__(self, game: Game, parent: EnemyGenerator):
        super().__init__(game)
        self.parent = parent
        self.parent.add_enemy(self)
        self.forward: np.Array = np.nga
        self.speed = random.uniform(0, 1)
        

    def __del__(self):
        super().__del__()
        self.parent.remove_enemy(self)
