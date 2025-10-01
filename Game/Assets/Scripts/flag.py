import random


from Game.Assets.Scripts.const import ENTITY_SPEED, HEIGHT
from Game.Assets.Scripts.entity import Entity


class Flag(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)
        self.hit = False

    def move(self, boost):
        self.sprite_rect.centery += ENTITY_SPEED[self.name] * boost
        if self.sprite_rect.top > HEIGHT:
            self.sprite_rect.center = (random.randint(16, 720), random.randint(-1000, -64))

    pass


def set_position(self, position):
    self.position = position
