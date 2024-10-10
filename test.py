from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from actor import Actor
from sprite_component import SpriteComponent
import pygame
import numpy as np
from mediapipe_input import MediapipeInput
from pose import Pose
from pointer import Pointer
from core import Core
from enemy import Enemy
from enemy_generator import EnemyGenerator
from collision import Sphere, intersect, AABB
from circle_component import CircleComponent, Kind
from box_component import BoxComponent
from move_component import MoveComponent
from circle_sprite_component import CircleSpriteComponent
from text_component import TextComponent
from result import Result
from anim_sprite_component import AnimSpriteComponent

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        actor = Actor(self.game)
        actor.position = self.game.screen_size * [0.5, 0.5]
        csc = CircleSpriteComponent(actor)
        csc.radius = 5
        csc.color = (233, 233, 0)
        csc = CircleSpriteComponent(actor, draw_order=1000)


    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)

    # def actor_input(self, event) -> None:
    #     super().actor_input(event)
    #     x_vel = 0
    #     y_vel = 0
    #     pressed_keys = pygame.key.get_pressed()
    #     if pressed_keys[pygame.K_w]:
    #         y_vel -= 1
    #     if pressed_keys[pygame.K_s]:
    #         y_vel += 1
    #     if pressed_keys[pygame.K_a]:
    #         x_vel -= 1
    #     if pressed_keys[pygame.K_d]:
    #         x_vel += 1
    #     self.mc.set_forward(np.array([x_vel, y_vel]))

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
