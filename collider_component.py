# 作りかけ
from __future__ import annotations
import pygame
from actor import *
from component import *

class ColliderComponent(Component):
    def __init__(self, owner: Actor):
        super().__init__(owner)
        self._owner.game.physics.add_collider(self._owner.sprite)
    
    def __del__(self):
        super().__del__()
        self._owner.game.physics.remove_collider(self._owner.sprite)

    def process_input(self, delta_time: float):
        contact_actors = self._owner.game.physics.isCollisiton(self._owner.sprite)
        