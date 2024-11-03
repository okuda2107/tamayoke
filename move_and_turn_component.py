from __future__ import annotations
from typing import TYPE_CHECKING
import copy
from actor import Actor
from move_component import MoveComponent
from collision import AABB, intersect

if TYPE_CHECKING:
    pass

class MoveAndTurnComponent(MoveComponent):
    def __init__(self, owner: Actor, box: AABB):
        super().__init__(owner)
        self.box = box

    def update(self, delta_time: float):
        super().update(delta_time)
        if not self.box.contains(self._owner.position):
            flag = False
            if self._owner.position[0] <= self.box.min_pos[0] or self._owner.position[0] >= self.box.max_pos[0]:
                self.forward[0] *= -1
                flag = True
            if self._owner.position[1] <= self.box.min_pos[1] or self._owner.position[1] >= self.box.max_pos[1]:
                self.forward[1] *= -1
                flag = True

