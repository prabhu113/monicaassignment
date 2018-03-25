import pygame
import random

import file
from file import *
import good_block_library
import player_library
import bad_block_library
from title_screen import *
from level_manager import *
import constants
from constants import *


# Instance of dictionary
dictionaries = file.File()
points = dictionaries.points_dictionary

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_blocks = pygame.sprite.Group()
bad_blocks = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
good_sprite_width = 20;
good_sprite_height = 15;
bad_sprite_width = 20;
bad_sprite_height = 15;
for i in range(50):
    # This represents a block
    block = good_block_library.Good_Block(GREEN, good_sprite_width, good_sprite_height)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width - good_sprite_width)
    block.rect.y = random.randrange(screen_height- good_sprite_height)

    # Add the block to the list of objects
    good_blocks.add(block)
    all_sprites_list.add(block)
for i in range(50):
    # This represents a block
    block = bad_block_library.Bad_Block(RED, bad_sprite_width, bad_sprite_height)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width - bad_sprite_width)
    block.rect.y = random.randrange(screen_height - bad_sprite_height)

    # Add the block to the list of objects
    bad_blocks.add(block)
    all_sprites_list.add(block)
# Create a player
player = player_library.Player(50, 50)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

level_manager = LevelManager()
level_manager.load_level(TitleScreen())

score = 0

# -------- Main Program Loop -----------
while not done:
    current_level = level_manager.get_current_level()

    #We've left the TitleScreen - Exit the game
    if current_level == None:
        break
    
    #Needs Game Logic
    current_level.update()
    current_level.draw(screen)
 
    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        current_level.handle_keyboard_event(event)
            # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # --- Game logic

    # This calls update on all the sprites
    all_sprites_list.update()
    # Clear the screen
    screen.fill(WHITE)



    # See if the player block has collided with anything.
    good_block_hit_list = pygame.sprite.spritecollide(player, good_blocks, True)
    bad_block_hit_list = pygame.sprite.spritecollide(player, bad_blocks, True)

    # Check the list of collisions.
    for block in good_block_hit_list:
        score += int(points.get("good_block"))
        # Check the list of collisions.
    for block in bad_block_hit_list:
        score += int(points.get("bad_block"))
    # Draw all the spites
    all_sprites_list.draw(screen)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(score), True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [0, 0])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
