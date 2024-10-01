from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
import numpy as np
from sprite_component import SpriteComponent

if TYPE_CHECKING:
    from actor import Actor

class AnimSpriteComponent(SpriteComponent):
    def __init__(self, owner: Actor, draw_order: int = 100):
        super().__init__(owner, draw_order)
        self.anim_sprites = []
        self.fps = 0.0
        self.current_frame = 0.0

    def set_anim_sprites(self, filenames: list[str], size):
        for filename in filenames:
            sprite = pygame.sprite.Sprite()
            sprite.image = pygame.image.load(filename).convert_alpha()
            sprite.image = pygame.transform.scale(sprite.image, size)
            sprite.rect = sprite.image.get_rect()
            sprite.rect.center = self._owner.position
            self.anim_sprites.append(sprite)
        self.image_size = np.array([size[0], size[1]])
        self.sprite = self.anim_sprites[0]
        self.original_sprite = self.anim_sprites[0]

    def update(self, delta_time: float) -> None:
        if len(self.anim_sprites) > 0:
            self.current_frame += self.fps * delta_time
            while self.current_frame >= len(self.anim_sprites):
                self.current_frame -= len(self.anim_sprites)
            self.sprite = self.anim_sprites[int(self.current_frame)]
            self.original_sprite = self.anim_sprites[int(self.current_frame)]

    def set_sprite(self, index: int):
        while index >= len(self.anim_sprites):
            index -= len(self.anim_sprites)
        self.sprite = self.anim_sprites[index]
        self.original_sprite = self.anim_sprites[index]
