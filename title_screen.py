import pygame
import constants

from level_manager import *
from game_screen import *
from credit_screen import *
from music import *
from art import *
class TitleScreen():
    def __init__(self):
        #Because this text never changes, we can load it in the constructor
        #Otherwise, we may need to move render into draw
        font_big = pygame.font.SysFont('Calibri', 25, True, False)
        font_med = pygame.font.SysFont('Calibri', 20, True, False)
        font_small = pygame.font.SysFont('Calibri', 15, True, False)
        self.music = Music("title")
        self.art = Art("title")
        
        

        #The underscore character indicates that this is a private instance variable
        self._title = font_big.render("Board Outta My Mind",True,constants.BLACK)
        self._authors = font_small.render("By: Taylor, Monica, and Daria",True,constants.BLACK)
        self._credits = font_med.render("For credits press c",True,constants.BLACK)
        self._game_start = font_med.render("To start press p",True,constants.BLACK)
        self._exit = font_med.render("To exit press esc",True,constants.BLACK)

    def handle_keyboard_event(self, event):
        self.music.play_repeat()

        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self.music.stop_repeat()
            elif event.key == pygame.K_p:
                LevelManager().load_level(GameScreen())
            elif event.key == pygame.K_c:
                LevelManager().load_level(CreditScreen())
                

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
        screen.blit(self.art.get_background(), [0, 0])

        # Draw my title text!
        screen.blit(self._title, [200, 20])
        screen.blit(self._authors, [200, 50])
        screen.blit(self._credits, [100, 250])
        screen.blit(self._game_start, [100, 275])
        screen.blit(self._exit, [100, 300])
