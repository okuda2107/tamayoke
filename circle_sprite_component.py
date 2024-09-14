from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from actor import Actor
from sprite_component import SpriteComponent

if TYPE_CHECKING:
    from pygame import Surface

class CircleSpriteComponent(SpriteComponent):
    def __init__(self, owner: Actor, draw_order: int = 100):
        super().__init__(owner, draw_order)
        self.color = (255, 255, 255)
        self.radius = 10

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(
            screen,
            self.color,
            (self._owner.position[0], self._owner.position[1]),
            self.radius
        )
