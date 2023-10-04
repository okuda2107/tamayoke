from __future__ import annotations
import pygame
from actor import *
from sprite_component import *

class circle_sprite_component(sprite_component):
    def __init__(self, owner: actor, draw_order: int = 100):
        super().__init__(owner, draw_order)
        self.color: tuple[int, int, int] = (0, 0, 0)
        self.radius: int = 0
    def __del__(self):
        super().__del__()

    def draw(self, screen: pygame.Surface) -> None:
        disp_position = self._calc_disp_position()
        pygame.draw.circle(screen, self.color, disp_position, self.radius)