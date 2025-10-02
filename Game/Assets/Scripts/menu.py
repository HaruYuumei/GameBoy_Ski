import pygame
from pygame import Font, Surface, Rect

from Game.Assets.Scripts.const import *


class Menu:
    def __init__(self, screen):
        print('Game Menu Starting...')
        self.screen = screen
        self.background = pygame.image.load('../Images/game_background_start.png')
        self.background_rect = self.background.get_frect(center=(WIDTH/2,HEIGHT/2))

    def run(self):
        print('Game Menu running...')
        menu_option = 1
        while True:
            #drawing
            self.screen.blit(self.background, self.background_rect)
            self.text_menu(62, "Game Boy Ski!", COLOR_BLACK, (WIDTH / 2, HEIGHT / 8))

            for texts in range(1,len(GAME_STATE)):
                if texts == menu_option:
                    self.text_menu(26, GAME_STATE[texts], COLOR_GREEN_THREE, (WIDTH / 2, 200 + 40 * texts))
                else:
                    self.text_menu(24, GAME_STATE[texts], COLOR_BLACK, (WIDTH / 2, 200 + 40 * texts))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option <= 0:
                            menu_option = 4

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option >= 5:
                            menu_option = 1

                    if event.key == pygame.K_RETURN:
                        return GAME_STATE[menu_option]


    def text_menu(self,text_size: int,text:str,text_color:tuple,text_center_pos):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(text_surface, text_rect)