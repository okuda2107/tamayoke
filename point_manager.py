from __future__ import annotations
import numpy as np
from game import *
from actor import *
from sprite_component import *
from text_component import *
from ball_generator import *
from result import *

point_rate = 100
# 発生確率
level1 = 0.05
level2 = 0.1
lebel3 = 0.3

class point_manager(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        self.position = np.array([0, 0])
        self.time: float = 10.0
        self.score: int = 0
        self.tc = TextComponent(self, 'microsoftsansserif', 30)
        self.tc.set_text('', (255, 255, 255))
        self.ball_list = []
        self.ball_generator: ball_generator

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
                else:
                    self.score -= int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
            if ball.position[0] > 0.5 and ball.position[1] > 1.0:
                if ball.red_white == 2:
                    self.score += int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
                else:
                    self.score -= int(point_rate * self.ball_generator.probability)
                    ball.state = state.dead
                    dead_ball.append(ball)
        for ball in dead_ball:
            self.ball_list.remove(ball)

        if self.time > 30:
            self.ball_generator.probability = level1
        elif self.time > 10:
            self.ball_generator.probability = level2
        else:
            self.ball_generator.probability = lebel3

        if self.time <= 0:
            actor1 = result(self.game, str(self.score), 150)
            actor1.position = np.array([0.4, 0.3])
            self.state = state.dead
            self.game.my_bar.state = state.dead
            self.ball_generator.state = state.dead

        self.tc.set_text('time:' + str(round(self.time, 1)) + ' score:' + str(self.score), (255, 255, 255))
        
