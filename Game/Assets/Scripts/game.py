from Game.Assets.Scripts.game_level import GameLevel
from Game.Assets.Scripts.game_level_end import GameLevelEnd

from Game.Assets.Scripts.menu import *


##
##  You don't like who you are now, so you go.
##  Even if you are scared, you want to change
##  the self you hate...
##
##  - Neiru Aonuma -  Wonder Egg Priority
##

class Game:
    def __init__(self):

        # initializing
        print('Game initializing...')

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game Boy Ski!")
        self.game_state = GAME_STATE[0]
        self.player_score = 0

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
                    self.player_score = GameLevel(self.screen, 'Level').run()
                    self.game_state = 'SCORE'
                case 'SCORE':
                    self.game_state = GameLevelEnd(self.screen, 'game_level_end').run(self.player_score)
                case 'OPTIONS':
                    # OPTIONS MENU HERE
                    pass
                case 'EXIT':
                    # QUIT HERE
                    pygame.quit()
                    quit()
