from __future__ import annotations
from abc import abstractmethod
from actor import *

class Component:
    def __init__(self, actor: Actor, update_order: int = 100):
        self._owner = actor
        self.update_order: int = update_order
        self._owner.add_component(self)

    def __del__(self):
        self._owner.remove_component(self)

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    #めったに実装しない　カメラからの入力を受ける
    @abstractmethod
    def process_input(self) -> None:
        pass