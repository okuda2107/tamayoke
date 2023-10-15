# 作りかけ
# 依存ファイル
# move_component
# gravity_component
# collider_component
from __future__ import annotations
import pygame
from actor import *

class Physics:
    def __init__(self):
        self.colliders = pygame.sprite.Group()

    def __del__(self):
        self.colliders.clear()

    def add_collider(self, collider: pygame.sprite.Sprite):
        self.colliders.add(collider)

    def remove_collider(self, collider: pygame.sprite.Sprite):
        self.colliders.remove(collider)

    def isCollision(self, collider: pygame.sprite.Sprite) -> list[pygame.sprite.Sprite]:
        return pygame.sprite.spritecollide(collider, self.colliders, False)
    
# actorにvelocityを持たせたくない
# move_componentを持たせた人だけ速度成分を持つ
# moveを継承してgravityとかcolliderとかが"同じ"速度成分をいじって欲しかった
# 実際はgravityとかcolliderとかが"別々の"速度成分をいじってしまう
# 速度成分が別々でも結局positionを足し合わせるから変わらんくね
# 感覚的には同じvelocityをいじってそのvelが求まり切ってからpositionに変換したかった
# physicsで一括管理？physicsへの依存度が高くなる
# physicsは他actorとの関係により物理挙動が決まる計算を補助する立ち位置でありたい．actorの速度成分がcomponentごとに別々やからっていう理由でphysicsに任せるのは違うかも