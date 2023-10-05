from __future__ import annotations
import pygame
from actor import *
from move_component import *

class gravity_component(move_component):
    def __init__(self, owner: actor):
        super().__init__(owner)
        self.__gravity: float = 1.5

    def __del__(self):
        super().__del__()

    def update(self, delta_time: float):
        self._velocity = (self._velocity[0], self._velocity[1] + self.__gravity * delta_time)
        super().update(delta_time)