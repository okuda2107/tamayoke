from __future__ import annotations
from abc import abstractmethod
from actor import *

class component:
    def __init__(self, actor: actor, update_order: int = 100):
        self.__owner = actor
        self.update_order: int = update_order

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    #めったに実装しない　カメラからの入力を受ける
    @abstractmethod
    def process_input(self) -> None:
        pass