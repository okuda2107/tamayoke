from __future__ import annotations
from game import Game
from box_component import BoxComponent
from circle_component import CircleComponent

class PhysWorld:
    game: Game
    __boxes: list[BoxComponent]
    __fires: list[CircleComponent]
    __bombs: list[CircleComponent]
    __pointer: list[CircleComponent]

    def __init__(self, game: Game):
        self.game = game
        self.__boxes: list[BoxComponent] = []
        self.__fires: list[CircleComponent] = []
        self.__pointer: list[CircleComponent] = []

    def add_box(self, box: BoxComponent):
        self.__boxes.append(box)

    def remove_box(self, box: BoxComponent):
        self.__boxes.remove(box)
