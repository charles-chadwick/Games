import pygame
from const import WINDOW_WIDTH, WINDOW_HEIGHT, FRAME_RATE, BACKGROUND_COLOR
from const import Direction, Actions
from players import Player

pygame.init()

class Game(object):

    def __init__(self):

        # Initalize stuff
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.hero = Player("player_blue", (0, 0))

    def loop(self):

        while True:
            self._handleInput()
            self._updateScreen()

    def _handleInput(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]
            ):
                quit() # TODO: Add confirmation dialog

            if event.type == pygame.KEYUP:
                self.hero.move(Direction.NONE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hero.move(Direction.UP)

        if keys[pygame.K_DOWN]:
            self.hero.move(Direction.DOWN)

        if keys[pygame.K_LEFT]:
            self.hero.move(Direction.LEFT)

        if keys[pygame.K_RIGHT]:
            self.hero.move(Direction.RIGHT)


    def _updateScreen(self):

        # Create the background
        self.screen.fill(BACKGROUND_COLOR)

        # Draw any of our players
        self.hero.draw(self.screen)

        # Update and time
        pygame.display.update()
        self.clock.tick(FRAME_RATE)

if __name__ == '__main__':
    game = Game()
    game.loop()