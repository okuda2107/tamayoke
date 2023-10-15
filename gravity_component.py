# 作りかけ
from __future__ import annotations
import pygame
import numpy as np
from actor import *
from move_component import *

class GravityComponent(MoveComponent):
    def __init__(self, owner: Actor):
        super().__init__(owner)
        self.__gravity: float = 1.5

    def __del__(self):
        super().__del__()

    def update(self, delta_time: float):
        self._owner.velocity = self._owner.velocity + np.array([0, self.__gravity * delta_time])
        super().update(delta_time)