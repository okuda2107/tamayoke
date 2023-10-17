from __future__ import annotations
from abc import abstractmethod
from enum import Enum
import numpy as np
import pygame
from game import *
from component import *

class state(Enum):
    active = 1
    dead = 2

class Actor:
    def __init__(self, game: Game):
        self.game = game
        self.position = np.array([0.0, 0.0])
        self.velocity = np.array([0.0, 0.0])
        self.scale: float = 0.0
        self.rotation: float = 0.0 # 傾き
        self.state: state = state.active
        self.__components: list[Component] = []
        self.sprite = pygame.sprite.Sprite()
        self.game.add_actor(self)

    def __del__(self):
        self.game.remove_actor(self)
        for comp in self.__components:
            comp.__del__()

    def update(self, delta_time: float) -> None:
        if self.state == state.active:
            self.update_components(delta_time)
            self.update_actor(delta_time)

    def update_components(self, delta_time: float) -> None:
        for comp in self.__components:
            comp.update(delta_time)

    @abstractmethod
    def update_actor(self, delta_time: float) -> None:
        pass

    def process_input(self) -> None:
        if self.state == state.active:
            for comp in self.__components:
                comp.process_input()
            self.actor_input()

    @abstractmethod
    def actor_input(self) -> None:
        pass

    def add_component(self, component: Component) -> None:
        my_order: int = component.update_order
        index = -1
        for comp in self.__components:
            index += 1
            if my_order < comp.update_order:
                break
        self.__components.insert(index, component)

    def remove_component(self, component: Component) -> None:
        if component in self.__components:
            self.__components.remove(component)