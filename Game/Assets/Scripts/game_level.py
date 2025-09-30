import random

import pygame

from Game.Assets.Scripts.entity_factory import Entity_Factory
from Game.Assets.Scripts.const import WIDTH, HEIGHT, PLAYER_SPEED
from Game.Assets.Scripts.player import Player
from Game.Assets.Scripts.tree import Tree


class GameLevel:
    def __init__(self, screen, name, game_mode):
        self.screen = screen
        self.name = name
        self.game_mode = game_mode
        self.distance = 0

        # Level Backgrounds
        self.background = pygame.image.load('../Images/game_background_start.png')
        self.background_rect = self.background.get_frect(center=(WIDTH / 2, HEIGHT / 2))

        # Flags

        self.tree_list = []
        for i in range(10):
            self.tree_list.append(Entity_Factory.getentity('tree',(random.randint(16,WIDTH-16),random.randint(-600,-8))))

        for i in range(10):
            self.tree_list.append(
                Entity_Factory.getentity('tree2', (random.randint(16, WIDTH - 16), random.randint(-600, -8))))

        self.backgrounds = [
            Entity_Factory.getentity('game_background0',(WIDTH / 2, -HEIGHT / 2)),
            Entity_Factory.getentity('game_background0', (WIDTH / 2, -900))
        ]


        self.clock = pygame.time.Clock()

    def run(self):
        player = Player('Player_Sprite', (WIDTH / 2, HEIGHT - 64))

        print('Game Level Started!')
        boost = 1
        while True:

            if boost > 1:
                self.distance += 0.1
            else:
                self.distance += 0.1 * boost / 10
            #print(f'Distance: {self.distance}')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        boost = 1.75
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        boost = 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        boost = 0.45
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        boost = 1

            keys = pygame.key.get_pressed()
            if keys:
                player.move(keys)

                # Mover o background!
            if self.background_rect.top < HEIGHT:
                self.background_rect.top += PLAYER_SPEED * boost
            self.screen.blit(self.background, self.background_rect)


            for bgs in self.backgrounds:
                self.screen.blit(bgs.sprite, bgs.sprite_rect)
                bgs.move(boost)

            for trees in self.tree_list:
                self.screen.blit(trees.sprite, trees.sprite_rect)
                trees.move(boost)

            self.screen.blit(player.getsprite(), player.getspriterect())
            pygame.display.flip()
            self.clock.tick(60)
