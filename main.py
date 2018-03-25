#Need to imoprt our own stuff!

import constants
from title_screen import *
from level_manager import *

import pygame
 
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT])
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
level_manager = LevelManager()
level_manager.load_level(TitleScreen())

done = False

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
        #Needs keyboard logic too!
        current_level.handle_keyboard_event(event)



pygame.quit()
