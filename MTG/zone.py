from enum import Enum

__author__ = 'Michael'

from MTG.game_object import GameObject

class ZoneType(Enum):
    LIBRARY = 0
    HAND = 1
    BATTLEFIELD = 2
    GRAVEYARD = 3
    STACK = 4
    EXILE = 5
    COMMAND = 6

class Zone(object):
    def __init___(self, elements:list=None):
        """
        @param elements: The elements this zone starts out containing
        @type elements: list[GameObject]
        """
        if elements is None:
            self.elements = []
        else:
            self.elements = elements
        
    def add(self, obj):
        """
        Add the specified object to this zone
        @param obj: The object to add to the zone
        @type obj: GameObject
        """
        self.elements.append(obj)

    def remove(self, obj):
        """
        Remove the specified object from this zone
        @param obj: The object to remove
        @type obj: GameObject
        @return: True if the object was present and removed, False otherwise
        @rtype: bool
        """
        try:
            self.elements.remove(obj)
            return True
        except ValueError:
            return False

    def __bool__(self):
        return bool(self.elements)

class Battlefield(Zone):
    pass

class Stack(Zone):
    def pop(self):
        return self.elements.pop()

class Hand(Zone):
    pass