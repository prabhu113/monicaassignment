import pygame
import constants

from level_manager import *
from screen import *
from file import *
import good_block_library
import player_library
import bad_block_library
from title_screen import *
from level_manager import *
from constants import *
import random
from music import *
from art import *

class GameScreen(Screen):
    def __init__(self):
        # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
        self.good_blocks = pygame.sprite.Group()
        self.bad_blocks = pygame.sprite.Group()
        self.dictionaries = file.File()
        self.points = self.dictionaries.points_dictionary
        self.art = Art("game")
        self.music = Music("game")


# This is a list of every sprite.
# All blocks and the player block as well.
        self.all_sprites_list = pygame.sprite.Group()
        self.good_sprite_width = 20;
        self.good_sprite_height = 15;
        self.bad_sprite_width = 20;
        self.bad_sprite_height = 15;
        for i in range(50):
    # This represents a block
            block = good_block_library.Good_Block()

    # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH - self.good_sprite_width)
            block.rect.y = random.randrange(SCREEN_HEIGHT - self.good_sprite_height)

    # Add the block to the list of objects
            self.good_blocks.add(block)
            self.all_sprites_list.add(block)
        for i in range(50):
    # This represents a block
            block = bad_block_library.Bad_Block()

    # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH - self.bad_sprite_width)
            block.rect.y = random.randrange(SCREEN_HEIGHT - self.bad_sprite_height)

    # Add the block to the list of objects
            self.bad_blocks.add(block)
            self.all_sprites_list.add(block)
# Create a player
        self.player = player_library.Player(50, 50)
        self.all_sprites_list.add(self.player)

        self.score = 0


    def handle_keyboard_event(self, event):
        self.music.play_repeat()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
                self.music.stop_repeat()
            elif event.key == pygame.K_LEFT:
                self.player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                self.player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                self.player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                self.player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                self.player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                self.player.changespeed(0, -3)

    def update(self):
    # See if the player block has collided with anything.
        good_block_hit_list = pygame.sprite.spritecollide(self.player, self.good_blocks, True)
        bad_block_hit_list = pygame.sprite.spritecollide(self.player, self.bad_blocks, True)

    # Check the list of collisions.
        for block in good_block_hit_list:
            self.music.play_once("good collision")
            self.score += int(self.points.get("good_block"))
    # Check the list of collisions.
        for block in bad_block_hit_list:
            self.music.play_once("bad collision")
            self.score += int(self.points.get("bad_block"))
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(WHITE)

        screen.blit(self.art.get_background(),[0,0])
    # This calls update on all the sprites
        self.all_sprites_list.update()

    # Draw all the spites
        self.all_sprites_list.draw(screen)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(self.score), True, WHITE)

    # Put the image of the text on the screen at 250x250
        screen.blit(text, [0, 0])
    # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
