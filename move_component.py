from __future__ import annotations
from game import *
#作りかけ
from actor import *
from component import *

class move_component(component):
    def __init__(self, owner: actor):
        super().__init__(owner)
    
    def __del__(self):
        super().__del__()

    def update(self, delta_time: float):
        position = self._owner.position
        self._owner.position += self._owner.velocity * delta_time