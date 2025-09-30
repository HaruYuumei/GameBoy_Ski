import sys

import pygame
from Game.Assets.Scripts.const import *
from Game.Assets.Scripts.game_level import GameLevel
from Game.Assets.Scripts.menu import *

class Game:
    def __init__(self):

        #initializing
        print('Game initializing...')

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game Boy Ski!")
        self.game_state = GAME_STATE[0]


    def run(self):
        print('Game running...')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            match self.game_state:
                case 'MENU':
                    # GAME MENU HERE
                    menu = Menu(self.screen)
                    self.game_state = menu.run()
                case 'GAME':
                    # GAME RUNS HERE
                    level = GameLevel(self.screen,'Level','singleplayer').run()
                    pass
                case 'OPTIONS':
                    # OPTIONS MENU HERE
                    pass
                case 'EXIT':
                    # QUIT HERE
                    pygame.quit()
                    quit()
