from __future__ import annotations
from game import *
from actor import *
from component import *

class move_component(component):
    def __init__(self, owner: actor):
        super().__init__(owner)
        self._velocity: tuple[float, float] = (0.0, 0.0)
    
    def __del__(self):
        super().__del__()

    def update(self, delta_time: float):
        position = self._owner.position
        self._owner.position = (
            position[0] + self._velocity[0] * delta_time,
            position[1] + self._velocity[1] * delta_time
            )