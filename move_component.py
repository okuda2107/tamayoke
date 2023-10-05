from __future__ import annotations
from game import *
from actor import *
from component import *

class move_component(component):
    def __init__(self, owner: actor):
        super().__init__(owner)
        self.velocity: tuple[float, float] = (0.0, 0.0)

    def update(self, delta_time: float):
        position = self._owner.position
        self._owner.position = (
            position[0] + self.velocity[0] * delta_time,
            position[1] + self.velocity[1] * delta_time
            )