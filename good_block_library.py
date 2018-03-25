import random
import block_library
from constants import *
from art import *


class Good_Block(block_library.Block):
    def __init__(self):
        self.art = Art("game")
        super().__init__(self.art.get_sprite("good_block"), 10, 10)

    def update(self):
        random_x_change = random.randrange(7) - 3
        random_y_change = random.randrange(7) - 3
        if(self.rect.x + random_x_change < 0 or self.rect.x + random_x_change > SCREEN_WIDTH - self.width):
            random_x_change = random_x_change * -1
        if (self.rect.y + random_y_change < 0 or self.rect.y + random_y_change > SCREEN_HEIGHT - self.height):
            random_y_change = random_y_change * -1
        self.rect.x +=  random_x_change
        self.rect.y +=  random_y_change

