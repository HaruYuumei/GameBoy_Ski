import random

import pygame

from Game.Assets.Scripts.const import ENTITY_SPEED, HEIGHT, WIDTH
from Game.Assets.Scripts.entity import Entity


class Tree(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, boost):
        self.sprite_rect.centery += ENTITY_SPEED[self.name] * boost
        if self.sprite_rect.top > HEIGHT:
            self.sprite_rect.center = (random.randint(16,WIDTH-16),random.randint(-600,-8))
    pass





def set_position(self, position):
    self.position = position
