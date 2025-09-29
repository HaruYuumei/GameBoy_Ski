import pygame
from Game.Assets.Scripts.const import WIDTH, HEIGHT, ENTITY_SPEED
from Game.Assets.Scripts.entityfactory import EntityFactory
from Game.Assets.Scripts.player import Player


class GameLevel:
    def __init__(self, screen, name, game_mode):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode

        # self.entity_list : list = []
        # self.entity_list.extend(EntityFactory.get_entity('gameBG'))

        # Level Background
        self.background = pygame.image.load('../Images/game_background.png')
        self.background_rect = self.background.get_frect(center=(WIDTH / 2, HEIGHT / 2))

    def run(self):
        player = Player('Marie', (WIDTH / 2, 450))

        print('Game Level Started!')

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys:
                player.move(keys)

            # Drawing
            self.screen.blit(self.background, self.background_rect)

            # for imgs in self.entity_list:
            #     self.screen.blit(imgs.sprite, imgs.sprite_rect)
            #     imgs.move()

            self.screen.blit(player.getsprite(), player.getspriterect())
            pygame.display.flip()
