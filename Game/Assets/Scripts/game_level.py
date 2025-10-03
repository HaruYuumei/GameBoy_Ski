import random

from pygame import *

from Game.Assets.Scripts.entity_factory import Entity_Factory
from Game.Assets.Scripts.const import *
from Game.Assets.Scripts.player import Player


# Does being a girl or a boy matter when you really like something?
# - Kitagawa Marin  - Sono Bisque Doll Wa Koi Wo Suru


class GameLevel:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.score = 0
        self.distance = 0
        self.timeout = LEVEL_TIME  # 15s
        pygame.time.set_timer(TIMEOUT_TIME, TIMEOUT_STEP)  # 100ms

        # Level Backgrounds
        self.background = pygame.image.load('Game/Assets/Images/game_background_start.png')
        self.background_rect = self.background.get_frect(center=(WIDTH / 2, HEIGHT / 2))

        # Flags

        self.tree_list = []
        for i in range(8):
            self.tree_list.append(
                Entity_Factory.getentity('tree', (random.randint(16, WIDTH - 16), random.randint(-600, -8))))

        for i in range(6):
            self.tree_list.append(
                Entity_Factory.getentity('tree2', (random.randint(16, WIDTH - 16), random.randint(-600, -8))))

        self.backgrounds = [
            Entity_Factory.getentity('game_background0', (WIDTH / 2, -HEIGHT / 2)),
            Entity_Factory.getentity('game_background0', (WIDTH / 2, -900))
        ]

        self.flags = []
        for i in range(2):
            self.flags.append(Entity_Factory.getentity('flag', (WIDTH / 2, 601)))

        self.clock = pygame.time.Clock()

    def run(self):
        player = Player('Player_Sprite', (WIDTH / 2, HEIGHT - 64))

        print('Game Level Started!')
        boost = 1
        while True:

            # verify collisions with trees
            for i in range(len(self.tree_list)):
                if player.sprite_rect.colliderect(self.tree_list[i].sprite_rect):
                    if not self.tree_list[i].collided:
                        print(f'Collision With tree!')
                        player.hit_damage()
                        if player.health <= 0:
                            # game end
                            print('Game Over!')
                            print(f'Score: {self.score:.1f}')
                            return self.score

                        self.tree_list[i].collided = True
                else:
                    self.tree_list[i].collided = False

            # Collision with flags
            for i in range(len(self.flags)):
                if player.sprite_rect.colliderect(self.flags[i].sprite_rect):
                    if not self.flags[i].collided:
                        print(f'Collision With Flag!')
                        # Add time to Timer!
                        self.timeout += 3000
                        # Add score points!
                        self.score += 1 * self.distance
                        print(f'{self.score:.1f}')

                        self.flags[i].collided = True
                else:
                    self.flags[i].collided = False

            if boost > 1:
                self.distance += 0.1
            else:
                self.distance += 0.1 * boost / 10

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

                if event.type == TIMEOUT_TIME:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return self.score

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

            for flag in self.flags:
                self.screen.blit(flag.sprite, flag.sprite_rect)
                flag.move(boost)

            # HUD
            self.text_menu(24, f"Health: {player.health}", COLOR_BLACK, (650, HUD_HEIGHT))
            self.text_menu(24, f"Distance: {self.distance:.2f} Meters", COLOR_BLACK, (200, HUD_HEIGHT))
            self.text_menu(24, f"Timer: {self.timeout / 1000:.1f}s ", COLOR_BLACK, (150, HUD_HEIGHT + 40))

            self.screen.blit(player.getsprite(), player.getspriterect())
            pygame.display.flip()
            self.clock.tick(60)

    def text_menu(self, text_size: int, text: str, text_color: tuple, text_center_pos):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.screen.blit(text_surface, text_rect)
