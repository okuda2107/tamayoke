"""this module has flamework of game"""

from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
import numpy as np
from audio_system import AudioSystem
from phys_world import PhysWorld
from mediapipe_input import MediapipeInput, camera_check
import level_loader
from pose import Pose
from actor import Actor, state

if TYPE_CHECKING:
    from sprite_component import SpriteComponent

class Config:
    def __init__(self) -> None:
        self.camera_flag = False
        self.camera_num = 0

class Game:
    """this class is base of game"""
    def __init__(self):
        self.__is_running: bool = True
        self.__is_updating_actors: bool = False
        self.__ticks_counts: pygame.time.Clock
        self.physics = PhysWorld(self)
        self.mediapipe = None
        self.audio_system = AudioSystem()
        self.__screen = None
        self.config = Config()
        self.screen_size = np.array([1300, 700]) # (1300, 700)
        self.__actors: list[Actor] = []
        self.__pending_actors: list[Actor] = []
        self.__sprites: list[SpriteComponent] = []

    def initialize(self) -> bool:
        """this method initial game"""
        result = pygame.init()
        if result[1] != 0:
            print(pygame.get_error())
            return False
        level_loader.load_game_properties(self, 'asset/GameProperty.json')
        self.mediapipe = MediapipeInput(self.config.camera_num)
        if self.config.camera_flag:
            camera_check()
            return False
        pygame.display.set_caption("tama.yoke")
        # self.__screen = pygame.display.set_mode(self.screen_size, pygame.FULLSCREEN)
        self.__screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        self.screen_size = np.array(self.__screen.get_size())
        if self.__screen is None:
            print(pygame.get_error())
            return False
        if not self.mediapipe.initialize():
            print(pygame.get_error())
            return False
        self.__ticks_counts = pygame.time.Clock()
        self.__load_data()
        return True

    def run_loop(self) -> None:
        while self.__is_running:
            self.__process_input()
            self.__update_game()
            self.__generate_output()

    def __process_input(self) -> None:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.__is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__is_running = False
        self.__is_updating_actors = True
        for actor in self.__actors:
            actor.process_input(event_list)
        self.__is_updating_actors = False
        # モーションの入力
        self.mediapipe.detect_pose()

    def __update_game(self) -> None:
        delta_time: float = self.__ticks_counts.tick_busy_loop(25) / 1000
        if delta_time > 0.05:
            delta_time = 0.05
        self.__is_updating_actors = True
        for actor in self.__actors:
            actor.update(delta_time)
        self.__is_updating_actors = False
        for pending in self.__pending_actors:
            self.__actors.append(pending)
        self.__pending_actors.clear()
        dead_actors: list[Actor] = []
        for actor in self.__actors:
            if actor.state == state.dead:
                dead_actors.append(actor)
        for actor in dead_actors:
            actor.__del__()
        dead_actors.clear()

    def __generate_output(self) -> None:
        self.__screen.fill((43, 45, 49))
        for sprite in self.__sprites:
            sprite.draw(self.__screen)
        pygame.display.update()

    def shutdown(self) -> None:
        self.mediapipe.shutdown()
        pygame.quit()

    def add_actor(self, actor: Actor) -> None:
        if self.__is_updating_actors:
            self.__pending_actors.append(actor)
        else:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor) -> None:
        if actor in self.__pending_actors:
            self.__pending_actors.remove(actor)
        if actor in self.__actors:
            self.__actors.remove(actor)

    # draw_orderが大きいほうから描画されるので，手前から小さい順に並ぶ
    def add_sprite(self, sprite_comp: SpriteComponent) -> None:
        my_draw_order: int = sprite_comp.draw_order
        index = -1
        for sprite in self.__sprites:
            index += 1
            if my_draw_order < sprite.draw_order:
                break
        self.__sprites.insert(index, sprite_comp)

    def remove_sprite(self, sprite_comp: SpriteComponent) -> None:
        if sprite_comp in self.__sprites:
            self.__sprites.remove(sprite_comp)

    def __load_data(self) -> None:
        level_loader.load_level(self, 'asset/entrypoint.json')
        # level_loader.load_level(self, 'asset/test.json')
        actor = Actor(self)
        Pose(actor)
