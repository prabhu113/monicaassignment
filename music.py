import file
import pygame
dictionaries = file.File()
sounds = dictionaries.sounds_dictionary
pygame.init()
pygame.mixer.init()
class Music():
    def __init__(self, level):
        if level == "game":
            self._background = sounds.get("music_game")
            self._bad_collision = pygame.mixer.Sound(sounds.get("bad_collision"))
            self._good_collision = pygame.mixer.Sound(sounds.get("good_collision"))
            self._border_collision = pygame.mixer.Sound(sounds.get("border_collision"))
        else:
            self._background = sounds.get("music_title")

    def play_once(self,id):
        if id == "background":
            sound = self._background
        elif id == "bad collision":
            sound = self._bad_collision
        elif id == "good collision":
            sound = self._good_collision
        elif id == "border collision":
            sound = self._border_collision
        sound.play()
    def play_repeat(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(self._background)
        pygame.mixer.music.play(-1)                     
    def stop_repeat(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()



