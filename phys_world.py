from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from box_component import BoxComponent
    from circle_component import CircleComponent, Kind

class PhysWorld:
    def __init__(self, game: Game):
        self.game = game
        self.boxes: list[BoxComponent] = []
        self.circles: list[list[CircleComponent]] = [[], [], []]

    def add_box(self, box: BoxComponent):
        self.boxes.append(box)

    def remove_box(self, box: BoxComponent):
        self.boxes.remove(box)

    def add_circle(self, circle: CircleComponent, kind: Kind):
        self.circles[kind.value].append(circle)

    def remove_circle(self, circle: CircleComponent, kind: Kind):
        self.circles[kind.value].remove(circle)
