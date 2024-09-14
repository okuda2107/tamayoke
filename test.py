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

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.a1 = Actor(self.game)
        self.a1.position = np.array([0, 0])
        csc = CircleSpriteComponent(self.a1)
        csc.color = (255, 83, 182)
        csc.radius = 200
        self.cc1 = CircleComponent(self.a1, Kind.core)
        sphere = Sphere()
        sphere.center = self.a1.position
        sphere.radius = csc.radius
        self.cc1.set_sphere(sphere)
        self.mc = MoveComponent(self.a1)
        self.mc.speed = 100

        a2 = Actor(self.game)
        a2.position = self.game.screen_size * 0.5
        csc = CircleSpriteComponent(a2)
        csc.color = (233, 231, 122)
        csc.radius = 100
        # self.cc2 = CircleComponent(a2, Kind.core)
        # sphere = Sphere()
        # sphere.center = a2.position
        # sphere.radius = csc.radius
        # self.cc2.set_sphere(sphere)
        self.cc2 = BoxComponent(a2)
        box = AABB(np.array([200, 200]))
        self.cc2.set_object_box(box)

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)

    def actor_input(self, event) -> None:
        super().actor_input(event)
        x_vel = 0
        y_vel = 0
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            y_vel -= 1
        if pressed_keys[pygame.K_s]:
            y_vel += 1
        if pressed_keys[pygame.K_a]:
            x_vel -= 1
        if pressed_keys[pygame.K_d]:
            x_vel += 1
        self.mc.set_forward(np.array([x_vel, y_vel]))

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        if intersect(self.cc1.circle, self.cc2.get_world_box()):
            print(self.cc1.circle.radius)
            print(self.cc1.circle)
            print('intersect!!!')
