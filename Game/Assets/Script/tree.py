import random

from Game.Assets.Script.const import ENTITY_SPEED, HEIGHT
from Game.Assets.Script.entity import Entity


#
#   "So, what I'm saying is... I want to be by your side, just be with you Always..."
#                            Can I? Would you let me?"
#
#   - Kazuya - Kanojo Okarishimasu
#


class Tree(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, boost):
        self.sprite_rect.centery += ENTITY_SPEED[self.name] * boost
        if self.sprite_rect.top > HEIGHT:
            self.sprite_rect.center = (random.randint(16, 700), random.randint(-1000, -64))

    def set_position(self, position):
        self.position = position
