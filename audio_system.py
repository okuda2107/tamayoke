import pygame

class AudioSystem:
    def __init__(self):
        self.sound_by_name: dict[str, pygame.mixer.Sound] = {}

    def set_sound(self, file_name: str) -> None:
        temp = pygame.mixer.Sound(file_name)
        self.sound_by_name[file_name] = temp

    def play(self, key: str) -> None:
        self.sound_by_name[key].play()