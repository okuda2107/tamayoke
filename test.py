from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from actor import Actor
from component import Any
from box_component import BoxComponent
from collision import AABB
from sprite_component import SpriteComponent
import pygame
import numpy as np

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        # button
        self.position = [0.5, 0.3]
        sc = SpriteComponent(self)
        sc.set_image('asset/title.png', (200, 200))
        bc = BoxComponent(self)
        box = AABB(self.position, sc.image_size)
        bc.set_object_box(box)

        # player
        actor = Actor(self.game)
        actor.position = [0.5, 0.6]
        sc = SpriteComponent(actor)
        sc.set_image('asset/pointer.png', (10, 10))
        bc = BoxComponent(actor)
        box = AABB(actor.position, sc.image_size)
        bc.set_object_box(box)

        self.speed = 1.0

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)

    def process_input(self, event) -> None:
        super().process_input(event)
        x_vel = 0.0
        y_vel = 0.0
        for e in event:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    y_vel += self.speed
                if e.key == pygame.K_s:
                    y_vel -= self.speed
                if e.key == pygame.K_a:
                    x_vel -= self.speed
                if e.key == pygame.K_d:
                    x_vel += self.speed
        self.velocity = np.array([x_vel, y_vel])

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.position = self.position + self.velocity * delta_time
        intersect()
