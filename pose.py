from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
import math
from sprite_component import SpriteComponent

if TYPE_CHECKING:
    from pygame import Surface
    from actor import Actor


class Pose(SpriteComponent):
    def __init__(self, owner: Actor, draw_order: int = 10):
        super().__init__(owner, draw_order)
        self.color = (255, 255, 255)
        self.face_radius = 20
        self.radius =10
        self.thickness = 3

    def __del__(self):
        return super().__del__()

    def draw(self, screen: Surface) -> None:
        pose = self._owner.game.mediapipe.result.pose_landmarks

        if pose is None:
            return

        pose = pose.landmark
        screen_size = self._owner.game.screen_size

        # 顔描画
        face = math.sqrt((pose[0].x - pose[7].x) ** 2 + (pose[0].y - pose[7].y) ** 2) * screen_size[0]
        pygame.draw.circle(
            screen,
            self.color,
            (pose[0].x * screen_size[0], pose[0].y * screen_size[1]),
            face,
            self.thickness,
        )

        # 関節描画
        for i in [11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28]:
            pygame.draw.circle(
                screen,
                self.color,
                (pose[i].x * screen_size[0], pose[i].y * screen_size[1]),
                self.radius,
            )

        # 関節間の描画
        line_start = [11, 11, 11, 12, 12, 13, 14, 23, 23, 24, 25, 26]
        line_end = [12, 13, 23, 14, 24, 15, 16, 24, 25, 26, 27, 28]
        for (start, end) in zip(line_start, line_end):
            pygame.draw.line(
                screen,
                self.color,
                (
                    pose[start].x * screen_size[0],
                    pose[start].y * screen_size[1],
                ),
                (
                    pose[end].x * screen_size[0],
                    pose[end].y * screen_size[1],
                ),
                self.thickness,
            )
