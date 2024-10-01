from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor, state
from sprite_component import SpriteComponent
from anim_sprite_component import AnimSpriteComponent
import level_loader
from collision import AABB, intersect
from box_component import BoxComponent
from circle_component import Kind
from pointer import Pointer

if TYPE_CHECKING:
    from game import Game

class Title(Actor):
    def __init__(self, game: Game):
        super().__init__(game)

        self.pointer = [Pointer(self.game, 15), Pointer(self.game, 16)]

        self.logo = Actor(self.game)
        self.logo.position = self.game.screen_size * [0.5, 0.4]
        sc = SpriteComponent(self.logo)
        sc.set_image('asset/title.png', (200, 150))

        self.button = Actor(self.game)
        self.button.position = self.game.screen_size * [0.5, 0.6]
        self.anim = AnimSpriteComponent(self.button)
        filenames = []
        for i in range(69):
            filenames.append('asset/start/start' + str(i) + '.png')
        self.anim.set_anim_sprites(filenames, [200, 150])
        self.anim.fps = len(self.anim.anim_sprites) / 2
        self.timer = 0.0
        bc = BoxComponent(self.button)
        box = AABB(self.anim.image_size)
        bc.set_object_box(box)

    def __del__(self):
        super().__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        flag = False
        for p in self.game.physics.circles[Kind.pointer.value]:
            if intersect(p.circle, self.game.physics.boxes[0].get_world_box()):
                flag = True
                if self.timer > 2:
                    self.state = state.dead
                    for p in self.pointer:
                        p.state = state.dead
                    self.logo.state = state.dead
                    self.button.state = state.dead
                    level_loader.load_level(self.game, 'asset/level1.json')
                    return
                self.timer += delta_time
                self.button.state = state.active

        if not flag:
            self.timer = 0.0
            self.button.state = state.paused
            self.anim.current_frame = 0
            self.anim.set_sprite(0)
