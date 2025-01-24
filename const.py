from enum import Enum
import pygame

GAME_XML_FILE_PATH = "res/space-game.xml"
GAME_PLAYER_SPRITE_PATH = "res/player"

FRAME_RATE = 40
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
BACKGROUND_COLOR = (50, 20, 50)

class Direction(Enum):

    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    NONE = None

class Actions(Enum):

    FIRE = pygame.K_SPACE