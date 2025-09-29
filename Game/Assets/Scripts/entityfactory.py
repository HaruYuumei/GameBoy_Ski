import random

import pygame

from Game.Assets.Scripts.background import Background
from Game.Assets.Scripts.const import *


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'gameBG':
                list_bg = []
                for i in range(2):
                    list_bg.append(Background(f'tile{i}', (random.randint(0,WIDTH), 0)))
                    list_bg.append(Background(f'tile{i}', (random.randint(0,WIDTH), HEIGHT - SPRITE_SIZE)))
                return list_bg
        return None
