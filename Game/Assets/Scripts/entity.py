from abc import ABC, abstractmethod
import pygame

from Game.Assets.Scripts.const import ENTITY_BOOST


#
#   "I tought if she saw what death looked like,
#   she'd stop saying she wanted to kill herself."
#
#   -Yuzuru Nishimiya, Koe no Katachi
#


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        super().__init__()
        self.name = name
        self.position = position

        self.sprite = pygame.image.load('Game/Assets/Images/' + name + '.png')
        self.sprite_rect = self.sprite.get_frect(center=(position[0], position[1]))
        self.speed = ENTITY_BOOST
        self.collided = False

    @abstractmethod
    def move(self, *args, **kwargs):
        pass
