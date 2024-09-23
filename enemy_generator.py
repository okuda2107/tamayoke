from __future__ import annotations
from typing import TYPE_CHECKING
import random
import numpy as np
from actor import Actor
from enemy import Enemy

if TYPE_CHECKING:
    from game import Game

class EnemyGenerator(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.enemies: list[Enemy] = []
        self.position = self.game.screen_size * np.array([random.uniform(0, 1), 0])
        self.target_pos = np.array([0, 0])
        self.speed = 1000
        self.forward = np.array([1, 0])

    def __del__(self):
        super().__del__()
        while self.enemies:
            e = self.enemies.pop(0)
            e.__del__()

    def update_actor(self, delta_time: float) -> None:
        super().update_actor(delta_time)
        # 画面端をキープ
        if self.position[0] >= self.game.screen_size[0] and (self.forward == np.array([1, 0])).all():
            self.position = self.game.screen_size * np.array([1, 0])
            self.forward = np.array([0, 1])
        if self.position[1] >= self.game.screen_size[1] and (self.forward == np.array([0, 1])).all():
            self.position = self.game.screen_size * np.array([1, 1])
            self.forward = np.array([-1, 0])
        if self.position[0] <= 0 and (self.forward == np.array([-1, 0])).all():
            self.position = self.game.screen_size * np.array([0, 1])
            self.forward = np.array([0, -1])
        if self.position[1] <= 0 and (self.forward == np.array([0, -1])).all():
            self.position = np.array([0, 0])
            self.forward = np.array([1, 0])

        # enemyを生成
        if random.uniform(0, 1) < 0.05:
            e = Enemy(self.game, self)
            e.mc.set_forward(self.target_pos - self.position)

        self.position = self.position + self.forward * self.speed * delta_time

    def add_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def remove_enemy(self, enemy: Enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
