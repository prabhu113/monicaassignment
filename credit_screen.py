import pygame
import constants

from level_manager import *
from screen import *
from music import *

class CreditScreen(Screen):
    def __init__(self):
        font_big = pygame.font.SysFont('Calibri', 25, True, False)
        font_small = pygame.font.SysFont('Calibri', 15, True, False)
        self.music = Music("credit")
        background = self.music._background
        self.music.play_repeat()

        self._title = font_big.render("Board Outta My Mind by:",True,constants.BLACK)
        self._author1 = font_small.render("Taylor Ruhoff - Art/Sound Engineer",True,constants.BLACK)
        self._author2 = font_small.render("Monica Timmerman - Gameplay Engineer",True,constants.BLACK)
        self._author3 = font_small.render("Daria Schuett - File Management Engineer",True,constants.BLACK)
        self._graphics = font_big.render("Graphics and Images Provided by:",True,constants.BLACK)
        self._graphic1 = font_small.render("Game Screen Background: Untitled by Pixabay",True,constants.BLACK)
        self._graphic2 = font_small.render("Title Screen Background: Monopoly board on brown wooden table top by Ylanite Koppens",True,constants.BLACK)
        self._graphic3 = font_small.render("All other sprites: Boardgame pack by Kenny",True,constants.BLACK)
        self._sounds = font_big.render("Sounds and Music Provided by:",True,constants.BLACK)
        self._sound1 = font_small.render("Background Game Music: Sayonara by Greek555",True,constants.BLACK)
        self._sound2 = font_small.render("Background Music: Escape1 by neolein",True,constants.BLACK)
        self._sound3 = font_small.render("Good Collision Sound: Collision by Mafon2",True,constants.BLACK)
        self._sound4 = font_small.render("Bad Collision Sound: Glass Smashing by InspectorJ",True,constants.BLACK)
        self._sound5 = font_small.render("Border Collision Sound: Cat Screaming by InspectorJ",True,constants.BLACK)
        self._exit = font_big.render("To return to the title screen press esc",True,constants.BLACK)

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self.music.stop_repeat()

    def update(self):
        pass
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
     
        # Draw everything
        screen.blit(self._title, [10, 0])
        screen.blit(self._author1, [10, 25])
        screen.blit(self._author2, [10, 50])
        screen.blit(self._author3, [10, 75])
        screen.blit(self._graphics, [10, 100])
        screen.blit(self._graphic1, [10, 125])
        screen.blit(self._graphic2, [10, 150])
        screen.blit(self._graphic3, [10, 175])
        screen.blit(self._sounds, [10, 200])
        screen.blit(self._sound1, [10, 225])
        screen.blit(self._sound2, [10, 250])
        screen.blit(self._sound3, [10, 275])
        screen.blit(self._sound4, [10, 300])
        screen.blit(self._sound5, [10, 325])
        screen.blit(self._exit, [10, 350])
        
