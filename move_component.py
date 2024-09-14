from __future__ import annotations
from typing import TYPE_CHECKING
import copy
import numpy as np
from actor import Actor
from component import Component

if TYPE_CHECKING:
    from game import Game

class MoveComponent(Component):
    def __init__(self, owner: Actor):
        super().__init__(owner)
        self.speed: float = 0.0
        self.forward: np.ndarray = np.array([0.0, 0.0])

    def __del__(self):
        super().__del__()

    # 正規化してくれる
    def set_forward(self, direction: np.ndarray):
        if  np.linalg.norm(direction, ord=2) != 0:
            self.forward = direction / np.linalg.norm(direction, ord=2)
        else:
            self.forward = np.array([0.0, 0.0])

    def update(self, delta_time: float):
        self._owner.position = self._owner.position + self.forward * self.speed * delta_time
