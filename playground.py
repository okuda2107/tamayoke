from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from actor import Actor, state
from collision import intersect
from circle_component import Kind
from core import Core
from pointer import Pointer
from text_component import TextComponent

if TYPE_CHECKING:
    from game import Game

class PlayGround(Actor):
    def __init__(self, game: Game, core = 1, pointer = [15, 16]):
        super().__init__(game)
        self.cores: list[Core] = []
        self.pointers: list[Pointer] = []
        rng = np.random.default_rng()
        for _ in range(core):
            core = Core(self.game)
            core.position = rng.uniform(0.1, 0.9, 2)
            self.cores.append(core)
        for p in pointer:
            self.pointers.append(Pointer(self.game, p))
        self.enemy_gen = EnemyGenerator(self.game)
        self.timer = 0
        self.actor = Actor(self.game)
        self.actor.position = [0, 0]
        self.tc = TextComponent(self.actor, 80)
        self.tc.set_color((255, 255, 255))
        self.tc.set_text('Time: ' + str(round(self.timer, 1)))

    def __del__(self):
        super().__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        self.timer += delta_time
        self.tc.set_text('Time: ' + str(round(self.timer, 1)))
        circles = self.game.physics.circles
        for p in circles[Kind.pointer.value]:
            for c in circles[Kind.core.value]:
                if intersect(p.circle, c.circle):
                    self.next_scene()
                    return
                for e in circles[Kind.enemy.value]:
                    if intersect(p.circle, e.circle):
                        e.get_owner().state = state.dead
                    if intersect(c.circle, e.circle):
                        self.next_scene()
                        return

    def next_scene(self):
        self.actor.state = state.dead
        for c in self.cores:
            c.state = state.dead
        for p in self.pointers:
            p.state = state.dead
        self.enemy_gen.state = state.dead
        for e in self.enemy_gen.enemies:
          e.state = state.dead
        # Result(self.game)
