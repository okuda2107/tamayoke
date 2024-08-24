from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from box_component import BoxComponent
    from circle_component import CircleComponent

class PhysWorld:
    game: Game
    boxes: list[BoxComponent]
    __fires: list[CircleComponent]
    __bombs: list[CircleComponent]
    __pointer: list[CircleComponent]

    def __init__(self, game: Game):
        self.game = game
        self.boxes: list[BoxComponent] = []
        self.__fires: list[CircleComponent] = []
        self.__pointer: list[CircleComponent] = []

    def add_box(self, box: BoxComponent):
        self.boxes.append(box)

    def remove_box(self, box: BoxComponent):
        self.boxes.remove(box)
