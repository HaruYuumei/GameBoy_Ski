from Game.Assets.Scripts.const import *
from Game.Assets.Scripts.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.sprite_rect.centery += ENTITY_SPEED[self.name]
        if self.sprite_rect.bottom >= HEIGHT + SPRITE_SIZE:
            self.sprite_rect.top = -SPRITE_SIZE
        pass
