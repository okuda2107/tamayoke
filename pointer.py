from __future__ import annotations
from typing import TYPE_CHECKING
from actor import Actor
from sprite_component import SpriteComponent
from circle_component import CircleComponent, Kind
from collision import Sphere

if TYPE_CHECKING:
    from game import Game

class Pointer(Actor):
    def __init__(self, game: Game):
        super().__init__(game)
        sc = SpriteComponent(self)
        sc.set_image('asset/pointer.png', (200, 200))
        cc = CircleComponent(self, Kind.pointer)
        sphere = Sphere()
        sphere.center = self.position
        sphere.radius = sc.image_size[0] / self.game.screen_size[0]
        cc.set_sphere(sphere)
       
    def __del__(self):
        return super().__del__()

    def actor_input(self, event) -> None:
        pass
        # pose = self.game.mediapipe.detect_pose()
        # if pose != None:
        #     self.position = np.array([pose.pose_landmarks.landmark[self.index].x, pose.pose_landmarks.landmark[self.index].y])
