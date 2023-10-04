from __future__ import annotations
from abc import abstractmethod
import pygame
from game import *
from actor import *
from component import *

#衝突判定も含めます
class sprite_component(component):
    def __init__(self, owner: actor, draw_order: int = 100):
        super().__init__(owner)
        self.draw_order = draw_order
        self.sprite = pygame.sprite.Sprite()
        self.width: int = 0
        self.height: int = 0
        self._owner.game.add_sprite(self)

    def __del__(self):
        super().__del__()
        self._owner.game.remove_sprite(self)

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        position = self._calc_disp_position()
        self.sprite.rect = Rect(
            position[0],
            position[1], 
            self.width, 
            self.height
        )
        self.sprite.image = pygame.transform.rotate(self.sprite.image, self._owner.rotation)
        screen.blit(self.sprite.image, self.sprite.rect)

    def set_image(self, file_name: str) -> None:
        self.sprite.image = pygame.image.load(file_name).convert_alpha()
        self.width = self.sprite.image.get_width()
        self.height = self.sprite.image.get_height()
        position = self._calc_disp_position()
        self.sprite.rect = Rect(
            position[0],
            position[1], 
            self.width, 
            self.height
        )

    def _calc_disp_position(self) -> tuple[int, int]:
        return (
            int(self._owner.position[0] * self._owner.game.screen_size[0]), 
            int(self._owner.position[1] * self._owner.game.screen_size[1])
        )