from pygame import *

from Game.Assets.Scripts.DBProxy import DBProxy
from Game.Assets.Scripts.const import *


#
#   "After she made that miracle happen, I said to her...
#   I was sure there was no God.
#   but if there is one, it must be You."
#
#   -Violet Evergarden S1-Ep7, 17:36s
#


class GameLevelEnd:
    def run(self, player_score):
        print('Score Running...')

        database_proxy = DBProxy('DBScore')
        database_proxy.save(player_score)

        scores = [row[1] for row in database_proxy.retrieve_top3()]

        print(scores)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'MENU'

            self.screen.blit(self.background, self.background_rect)

            # HUD

            self.text_menu(24, f"last run Score: {player_score:.2f}!", COLOR_BLACK, (WIDTH / 2, 150))

            for i, score in enumerate(scores):
                y_pos = 200 + (i * 50)
                self.text_menu(24, f"#{i + 1} Score: {score:.2f}!", COLOR_BLACK, (WIDTH / 2, y_pos))

            self.text_menu(24, f"Press Enter to return!", COLOR_BLACK, (WIDTH / 2, 400))

            pygame.display.flip()
            self.clock.tick(60)

    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(text_surface, text_rect)

    def __init__(self, screen, name):
        self.screen = screen
        self.name = name

        # Level Backgrounds
        self.background = pygame.image.load('Game/Assets/Images/game_background_start.png')
        self.background_rect = self.background.get_frect(center=(WIDTH / 2, HEIGHT / 2))

        self.clock = pygame.time.Clock()
