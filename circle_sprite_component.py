from __future__ import annotations
import pygame
from actor import *
from sprite_component import *

class circle_sprite_component(sprite_component):
    def __init__(self, owner: actor, draw_order: int = 100):
        super().__init__(owner, draw_order)

    def __del__(self):
        super().__del__()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (0, 0, 0), (300, 200), 150)