import random
import block_library
from art import *
from constants import *

screen_width = 700
class Bad_Block(block_library.Block):
    def __init__(self):
        self.art = Art("game")
        super().__init__(self.art.get_sprite("bad_block"), 10, 10)
    def update(self):
        self.rect.x = self.rect.x - 3
        if(self.rect.x < 0):
            self.rect.x = SCREEN_WIDTH