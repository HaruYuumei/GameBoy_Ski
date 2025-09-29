import pygame

from Game.Assets.Scripts.const import PLAYER_SPEED, WIDTH, HEIGHT
from Game.Assets.Scripts.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        Entity.__init__(self, name, position)

    #movement for character
    def move(self, key):
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            if self.sprite_rect.left > 8:
                self.sprite_rect.centerx -= PLAYER_SPEED
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            if self.sprite_rect.right < WIDTH -8:
                self.sprite_rect.centerx += PLAYER_SPEED
        if key[pygame.K_UP] or key[pygame.K_w]:
            if self.sprite_rect.top > 8:
                self.sprite_rect.centery -= PLAYER_SPEED
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            if self.sprite_rect.bottom < HEIGHT -8:
                self.sprite_rect.centery += PLAYER_SPEED

    def getsprite(self):
        return self.sprite

    def getspriterect(self):
        return self.sprite_rect
