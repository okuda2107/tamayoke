from __future__ import annotations
from typing import TYPE_CHECKING

from sprite_component import SpriteComponent

if TYPE_CHECKING:
    from pygame import Surface
    from actor import Actor

class Pose(SpriteComponent):
    def __init__(self, owner: Actor, draw_order: int = 100):
        super().__init__(owner, draw_order)
        self.color = (0, 0, 0)
        self.radius = 20
        self.thickness = 8

    def __del__(self):
        return super().__del__()
    
    def draw(self, screen: Surface) -> None:
        pass
