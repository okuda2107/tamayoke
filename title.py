from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor
from sprite_component import SpriteComponent
from collision import AABB
from pointer import Pointer
from box_component import BoxComponent

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
        sc.set_image('asset/entrypoint.png', (200, 150))
        bc = BoxComponent(self.button)
        box = AABB(sc.image_size, self.game.screen_size)
        bc.set_object_box(box)
