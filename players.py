import pygame
from pygame.sprite import Sprite
from utils import XML
from const import GAME_PLAYER_SPRITE_PATH, GAME_XML_FILE_PATH
from const import Direction, Actions

class Player(Sprite):

    def __init__(self, player_name, coordinates):

        super().__init__()

        self.coordinates = coordinates
        self.player_name = player_name

        self._current_sprite_index = 0
        self._sprites = []
        self._time_since_last_sprite = -1
        self._xml = XML(GAME_XML_FILE_PATH)

        self._load()

    def _load(self):

        # First, get the player XML res
        player_xml_res = self._xml.loadPlayerXML(self.player_name)

        # Load the data here
        self._velocity = int(player_xml_res.attrib["velocity"])

        # Next get the sprites
        sprites =self._xml.loadSpriteXML(player_xml_res)

        for sprite in sprites:
            try:
                image = pygame.image.load(f"{GAME_PLAYER_SPRITE_PATH}/{sprite.attrib['src']}")
            except pygame.error as message:
                raise pygame.error(message)

            self._sprites.append(image)

    def draw(self, screen : pygame.Surface):
        """
        Draw the current sprite on the screen
        :param screen:
        :return:
        """
        image = self._sprites[self._current_sprite_index]
        screen.blit(image, self.coordinates, image.get_rect())

    def move(self, direction):
        """
        Move the sprite in a specific direction
        :param direction:
        :return:
        """

        # First, check to see if we are stopped
        if direction == Direction.NONE:
            # Set the new sprite index
            self._current_sprite_index = 0
            return

        # Set the new coordinates
        x, y = self.coordinates

        if direction == Direction.UP:
            y -= self._velocity

        if direction == Direction.DOWN:
            y += self._velocity

        if direction == Direction.LEFT:
            x -= self._velocity

        if direction == Direction.RIGHT:
            x += self._velocity

        # Set the new sprite index. Currently, it's hardcoded but this will change
        self._current_sprite_index = 2
        self.coordinates = (x, y)