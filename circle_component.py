from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum
from component import Component

if TYPE_CHECKING:
    from actor import Actor
    from collision import Sphere

class Kind(Enum):
    core = 0
    enemy =1
    pointer = 2

class CircleComponent(Component):
    def __init__(self, owner: Actor, kind: Kind):
        super().__init__(owner)
        self.circle: Sphere = None
        self._owner.game.physics.add_circle(self, kind)

    def __del__(self):
        return super().__del__()

    def update(self, delta_time: float):
        self.circle.center = self._owner.position

    def set_sphere(self, model: Sphere):
        self.circle = model

    def get_owner(self):
        return self._owner
