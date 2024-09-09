from __future__ import annotations
from typing import TYPE_CHECKING
import random
from actor import Actor, state

if TYPE_CHECKING:
    from game import Game
    from enemy import Enemy

class EnemyGenerator(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.enemies: list[Enemy] = []
        self.speed = 1
        
    def __del__(self):
        super().__del__()
        while self.enemies:
            e = self.enemies.pop(0)
            e.__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        if random.uniform(0, 1) < 0.05:
            pass

    def add_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def remove_enemy(self, enemy: Enemy):
        self.enemies.remove(enemy)
