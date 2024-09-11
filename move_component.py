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
        self.forward = direction / np.linalg.norm(direction, ord=2)

# 反射も含めた 反射含めるのあんまりよくない気がする．責務が...
    def update(self, delta_time: float):
        pre_position = copy.deepcopy(self._owner.position)
        self._owner.position = self._owner.position + self.forward * self.speed * delta_time
        if ((self._owner.position <= np.zeros(2)) | (np.ones(2) <= self._owner.position)).any() and ((np.zeros(2) < pre_position) & (pre_position < np.ones(2))).any():
            if self._owner.position[0] <= 0 or self._owner.position[0] >= 1:
                self.forward[0] *= -1
            if self._owner.position[1] <= 0 or self._owner.position[1] >= 1:
                self.forward[1] *= -1
