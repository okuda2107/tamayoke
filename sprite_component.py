from __future__ import annotations
from abc import abstractmethod
from typing import Any, TypeVar
import numpy as np
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

    def get_type(self):
        return TypeID.t_sprite_component
    
    def load_properties(self, obj: dict[str, Any]) -> None:
        super().load_properties(obj)
        sprite_data = obj.get('sprite')
        if sprite_data != None:
            file_name = sprite_data.get('fileName')
            size = sprite_data.get('size')
            if file_name != None and size != None:
                self.set_image(file_name, tuple(self._owner.game.screen_size * np.array(size)))
        draw_order_data = obj.get('drawOrder')
        if draw_order_data != None:
            self.draw_order = draw_order_data

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