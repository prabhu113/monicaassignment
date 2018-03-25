
import pygame
from art import *
import constants
from block_library import *
from music import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0, 255)
GREEN = (0,255,0)



class Player(Block):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        art = Art("game")
        """Constructor function"""
        # Call the parent's constructor
        super().__init__(art.get_sprite("player"),15,15)
        self.music = Music("game")




        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.music.play_once("border collision")
            self.rect.x = SCREEN_WIDTH / 2
            self.rect.y = SCREEN_HEIGHT / 2
        if self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT - self.rect.width:
            self.music.play_once("border collision")
            self.rect.x = SCREEN_WIDTH / 2
            self.rect.y = SCREEN_HEIGHT / 2

