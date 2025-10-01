from pygame import *
from Game.Assets.Scripts.const import *


class GameLevelEnd:
    def run(self, player_score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.blit(self.background, self.background_rect)

            # HUD
            self.text_menu(24, f"SCORE: {player_score:.2f}!", COLOR_BLACK, (WIDTH/2, HEIGHT / 2))

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
        self.background = pygame.image.load('../Images/game_background_start.png')
        self.background_rect = self.background.get_frect(center=(WIDTH / 2, HEIGHT / 2))

        self.clock = pygame.time.Clock()
