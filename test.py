from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game

from actor import Actor
from component import Any
from box_component import BoxComponent
from collision import AABB
from sprite_component import SpriteComponent

class Test(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        # button
        sc = SpriteComponent(self)
        sc.set_image('asset/title.png', (0.5, 0.6))
        bc = BoxComponent(self)
        box = AABB(self.position, sc.image_size)
        bc.set_object_box(box)

        # player
        actor = Actor(self.game)
        sc = SpriteComponent(actor)
        sc.set_image('asset/pointer.png', (0.1, 0.1))
        bc = BoxComponent(actor)
        box = AABB(actor.position, sc.image_size)
        bc.set_object_box(box)

    def __del__(self):
        super().__del__()

    def load_properties(self, obj: dict[str, Any]) -> None:
        return super().load_properties(obj)

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        
