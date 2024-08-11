from __future__ import annotations
from abc import abstractmethod
from typing import Any
from actor import *
from enum import Enum

# level_loadする時にactorのcomponent配列を走査してそのcomponentを既に持っているかIDを使って判定する
class TypeID(Enum):
    t_component = 0
    t_sprite_component = 1

# componentを生成する関数のジェネリクス(actorと同様)

class Component:
    def __init__(self, actor: Actor, update_order: int = 100):
        self._owner = actor
        self.update_order: int = update_order
        self._owner.add_component(self)

    def __del__(self):
        self._owner.remove_component(self)

    @abstractmethod
    def get_type(self):
        return TypeID.t_component
    
    @abstractmethod
    def load_properties(self, obj: dict[str, Any]) -> None:
        update_order_data = obj.get('updateOrder')
        if update_order_data != None:
            self.update_order = update_order_data

    @abstractmethod
    def update(self, delta_time: float) -> None:
        pass

    #めったに実装しない　カメラからの入力を受ける
    @abstractmethod
    def process_input(self, event) -> None:
        pass
