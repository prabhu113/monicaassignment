
import file
import pygame
import constants
from constants import *

dictionaries = file.File()
graphics = dictionaries.images_dictionary

class Art():
    def __init__(self, level):
        if level == "game":
            self._background = pygame.image.load(graphics.get("background_game"))
            self._player = pygame.image.load(graphics.get("player"))
            self._good_block = pygame.image.load(graphics.get("good_block"))
            self._bad_block = pygame.image.load(graphics.get("bad_block"))
        elif level == "credit" or level == "title":
            self._background = pygame.image.load(graphics.get("background_title"))

    def get_sprite(self, id):
        if id == "player":
            image = self._player
        elif id == "good_block":
            image = self._good_block
        elif id == "bad_block":
            image = self._bad_block
        return image

    def get_background(self):
        return self._background
   
