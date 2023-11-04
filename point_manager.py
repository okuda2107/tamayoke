from __future__ import annotations
from typing import Any
import numpy as np
from component import Any
from game import *
from actor import *
from sprite_component import *
from text_component import *
from ball_generator import *
from bar import *
from result import *
import level_loader

point_rate = 100
# 発生確率
level1 = 0.05
level2 = 0.1
lebel3 = 0.3

class point_manager(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = np.array([0, 0])
        self.time: float = 60.0
        self.score: int = 0
        self.ball_list = []
        self.ball_generator: ball_generator
        self.game.audio_system.set_sound('asset/error.wav')
        self.game.audio_system.set_sound('asset/pop.wav')
        self.game.audio_system.bgm('asset/get.mp3')

    def __del__(self):
        return super().__del__()

    def update_actor(self, delta_time: float) -> None:
        self.time -= delta_time
        dead_ball = []
        for ball in self.ball_list:
            if ball.position[0] < 0.5 and ball.position[1] > 1.0:
                if ball.red_white == 1:
                    self.score += int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
                    self.game.audio_system.play('asset/pop.wav')
                else:
                    self.score -= int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
                    self.game.audio_system.play('asset/error.wav')
            if ball.position[0] > 0.5 and ball.position[1] > 1.0:
                if ball.red_white == 2:
                    self.score += int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
                    self.game.audio_system.play('asset/pop.wav')
                else:
                    self.score -= int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
                    self.game.audio_system.play('asset/error.wav')
        for ball in dead_ball:
            self.ball_list.remove(ball)

        if self.time > 30:
            self.ball_generator.probability = level1
        elif self.time > 10:
            self.ball_generator.probability = level2
        else:
            self.ball_generator.probability = lebel3

        if self.time <= 0:
            self.game.point = self.score
            level_loader.load_level(self.game, 'asset/result.json')
            self.state = state.dead
            self.game.my_bar.state = state.dead
            self.ball_generator.state = state.dead
            for ball in self.ball_list:
                ball.state = state.dead

        self.tc.set_text('time:' + str(round(self.time, 1)) + ' score:' + str(self.score), (239, 241, 250))
        
    def load_properties(self, obj: dict[str, Any]) -> None:
        super().load_properties(obj)
        self.game.my_bar = bar(self.game)
        actor1 = ball_generator(self.game)
        text_size = obj.get('timerSize')
        if text_size == None:
            text_size = 80
        self.tc = TextComponent(self, 'microsoftsansserif', text_size)
        self.tc.set_text('', (239, 241, 250))
        actor1.point_manager = self
        self.ball_generator = actor1