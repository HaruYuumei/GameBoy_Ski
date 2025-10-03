import pygame

from Game.Assets.Scripts.const import PLAYER_SIDE_SPEED, WIDTH
from Game.Assets.Scripts.entity import Entity

#   " Kita-san Black I hate you, It's because of you that I've come this far,
#    Because you were there, I made it to today without giving up.
#    Kita-san Black, The truth is...
#                    I...I've always...Loved you.
#
#   - Cheval Grand - UmaMusume Pretty derby, S3-Ep12

class Player(Entity):
    def __init__(self, name, position):
        Entity.__init__(self, name, position)
        self.health = 5

    #movement for character
    def move(self, key):
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if self.sprite_rect.left > 8:
                self.sprite_rect.centerx -= PLAYER_SIDE_SPEED
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if self.sprite_rect.right < WIDTH -8:
                self.sprite_rect.centerx += PLAYER_SIDE_SPEED

    def getsprite(self):
        return self.sprite

    def getspriterect(self):
        return self.sprite_rect

    def hit_damage(self):
        self.health = self.health - 1