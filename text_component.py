from __future__ import annotations
import pygame
from actor import *
from sprite_component import *

# シンプルにmicrosoftsansserifでいいかな
class TextComponent(SpriteComponent):
    def __init__(self, owner: Actor, size: int):
        super().__init__(owner)
        self.font = pygame.font.SysFont('microsoftsansserif', size)
        self.size = size
        self.color = (0, 0, 0)
        self.text: pygame.Surface = self.font.render('', True, self.color)

    def set_text(self, text: str):
        self.text = self.font.render(text, True, self.color)

    def set_color(self, color: tuple[int, int, int]):
        self.color = color

    def set_font(self, font: str):
        self.font = pygame.font.SysFont(font, self.size)

    def draw(self, screen: pygame.Surface) -> None:
        position = self._calc_disp_position()
        screen.blit(self.text, tuple(position))
