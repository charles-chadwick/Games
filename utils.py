import sys
from xml.etree import ElementTree as xml_res
from xml.etree.ElementTree import ParseError


class XML(object):

    def __init__(self, file_name):
        """
        Loads the XML file
        :param file_name:
        """
        try:
            self._xml = xml_res.parse(file_name)
        except Exception as message:
            raise(Exception(message))

    def loadPlayerXML(self, player_name):

        try:
            result = self._xml.find(f".//Player[@name='{player_name}']")
        except ParseError as message:
            raise ParseError(message)

        return result

    def loadSpriteXML(self, xml_result):

        try:
            result = xml_result.findall("Sprites/Sprite")
        except ParseError as message:
            raise ParseError(message)

        return result
