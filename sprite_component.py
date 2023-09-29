from __future__ import annotations
from abc import abstractmethod
import pygame
from game import *
from actor import *
from component import *

class sprite_component(component):
    def __init__(self, owner: actor, draw_order: int = 100):
        super().__init__(owner)
        self.draw_order = draw_order
        self._owner.game.add_sprite(self)

    def __del__(self):
        super().__del__()
        self._owner.game.remove_sprite(self)

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    def _calc_disp_position(self) -> tuple[int, int]:
        return (
            int(self._owner.position[0] * self._owner.game.screen_size[0]), 
            int(self._owner.position[1] * self._owner.game.screen_size[1])
        )