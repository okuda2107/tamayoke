from __future__ import annotations
from abc import abstractmethod
import pygame
import math
from game import *
from actor import *
from component import *

#衝突判定も含めます
class SpriteComponent(Component):
    def __init__(self, owner: Actor, draw_order: int = 100):
        super().__init__(owner)
        self.draw_order = draw_order
        self.sprite = pygame.sprite.Sprite()
        self.original_sprite = pygame.sprite.Sprite()
        self._owner.sprite = self.sprite
        self.image_size = np.array([0, 0])
        self._owner.game.add_sprite(self)

    def __del__(self):
        super().__del__()
        self._owner.game.remove_sprite(self)

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        position = self._calc_disp_position()
        self.sprite.image = pygame.transform.rotate(self.original_sprite.image, math.degrees(math.atan(self._owner.rotation)))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.center = position
        screen.blit(self.sprite.image, self.sprite.rect)

    def set_image(self, file_name: str, size: tuple[int, int]) -> None:
        self.sprite.image = pygame.image.load(file_name).convert_alpha()
        self.original_sprite.image = pygame.image.load(file_name).convert_alpha()
        self.sprite.image = pygame.transform.scale(self.sprite.image, size)
        self.original_sprite.image = pygame.transform.scale(self.sprite.image, size)
        self.image_size[0] = size[0]
        self.image_size[1] = size[1]
        position = self._calc_disp_position()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.center = position
        self.original_sprite.rect = self.original_sprite.image.get_rect()
        self.original_sprite.rect.center = position

    def _calc_disp_position(self):
        return self._owner.position * self._owner.game.screen_size