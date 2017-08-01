from enum import Enum
import random


from MTG.gameObject import GameObject

class ZoneType(Enum):
    LIBRARY = 0
    HAND = 1
    BATTLEFIELD = 2
    GRAVEYARD = 3
    STACK = 4
    EXILE = 5
    # COMMAND = 6

class Zone(object):
    def __init__(self, elements:list=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = elements
        
    def add(self, obj):
        self.elements.append(obj)

    def remove(self, obj):
        try:
            self.elements.remove(obj)
            return True
        except ValueError:
            return False

    def pop(self, pos=-1):
        return self.elements.pop(pos)

    def size(self):
        return len(self.elements)

    def show(self):
        for elem in self.elements:
            print(elem, elem.name())

    def __bool__(self):
        return bool(self.elements)



class Battlefield(Zone):
    pass

class Stack(Zone):
    pass

class Hand(Zone):
    pass

class Graveyard(Zone):
    pass

class Exile(Zone):
    pass

class Library(Zone):
    def shuffle(self):
        random.shuffle(self.elements)
    pass