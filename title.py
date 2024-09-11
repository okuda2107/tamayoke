from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state
from sprite_component import SpriteComponent
from collision import AABB, intersect
from box_component import BoxComponent
from circle_component import Kind
from pointer import Pointer
from count import Count

if TYPE_CHECKING:
    from game import Game

class Title(Actor):
    def __init__(self, game: Game):
        super().__init__(game)

        self.pointer = [Pointer(self.game, 15), Pointer(self.game, 16)]

        self.logo = Actor(self.game)
        self.logo.position = [0.5, 0.4]
        sc = SpriteComponent(self.logo)
        sc.set_image('asset/title.png', (200, 150))

        self.button = Actor(self.game)
        self.button.position = [0.5, 0.6]
        sc = SpriteComponent(self.button)
        sc.set_image('asset/red.png', (200, 150))
        bc = BoxComponent(self.button)
        box = AABB(sc.image_size, self.game.screen_size)
        bc.set_object_box(box)

    def __del__(self):
        super().__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        for p in self.game.physics.circles[Kind.pointer.value]:
            if intersect(p.circle, self.game.physics.boxes[0].get_world_box()):
                self.state = state.dead
                for p in self.pointer:
                    p.state = state.dead
                self.logo.state = state.dead
                self.button.state = state.dead
                Count(self.game, 1, [15, 16])
