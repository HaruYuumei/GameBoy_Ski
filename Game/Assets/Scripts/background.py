from Game.Assets.Scripts.const import ENTITY_SPEED, HEIGHT, WIDTH
from Game.Assets.Scripts.entity import Entity

#
#   "It's not Yamada's heart that I don't understand. It's my own heart.
#   Even though I really wanted it, I figured I couldn't get it anyway,so...
#   I was just looking for reasons to hate it.
#   Because letting yourself like something that much is scary..."
#
#   - Ichikawa -  The dangers in my heart, Karte 43
#


class Background(Entity):
    def move(self, boost):
        self.sprite_rect.centery += ENTITY_SPEED[self.name] * boost
        if self.sprite_rect.top > HEIGHT:
            self.sprite_rect.center = (WIDTH/2,-HEIGHT/2)
    pass


def __init__(self, name, position):
    super().__init__(name, position)


def set_position(self, position):
    self.position = position
