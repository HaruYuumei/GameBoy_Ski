import pygame

GAME_STATE= [
    'MENU',
    'GAME',
    'OPTIONS',
    'EXIT'
]

# GAME PALLETE GAME-BOY LIKE
COLOR_GREEN_ONE = (155,188,15)
COLOR_GREEN_TWO = (139,172,15)
COLOR_GREEN_THREE = (48,98,48)
COLOR_GREEN_FOUR = (15,56,15)
COLOR_BLACK = (0,0,0)

HUD_HEIGHT = 15

TIMEOUT_TIME = pygame.USEREVENT + 1
TIMEOUT_STEP = 100
LEVEL_TIME = 15000

WIDTH,HEIGHT = 800,600

#Player
PLAYER_SPEED = 4
PLAYER_SIDE_SPEED = 6
#Entity
ENTITY_SPEED = {
    'game_background_start' : 1,
    'game_background0' : 4,
    'tree' : 4,
    'tree2' : 4,
    'flag': 4
}
ENTITY_BOOST = 1.75

#Sprites
SPRITE_SIZE = 128

#Background
BACKGROUND_SIZE = (800,600)
