from __future__ import annotations
from typing import Any, TypeVar
import json
from game import *
from actor import *
from title import *

LEVEL_VERSION = 1

# 生成系関数のマップ
# actor_factory_map = {
#     'Actor': actor.create<Actor>
#     }

def load_level(game: Game, file_name: str) -> bool:
    with open(file_name, 'r') as file_data:
        doc: dict[str, Any] = json.load(file_data)
    version: int = doc['version']
    if version != LEVEL_VERSION:
        print('レベルファイルのバージョンが違います')
        return False
    # load_global_properties(game, doc['globalProperties'])
    load_actors(game, doc['actors'])
    return True

def load_global_properties(game: Game, obj: dict[str, Any]) -> None:
    pass

def load_actors(game: Game, arr: list[dict[str, Any]]) -> None:
    for obj in arr:
        type_name: str = obj['type']
        # 名前と対応する生成系関数を呼び出す
        # actor_factory = actor_factory_map[type_name]
        # actor = actor_factory(game, obj)
        actor = eval(type_name)(game)
        actor.load_properties(obj['properties'])