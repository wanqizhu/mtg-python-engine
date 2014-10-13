from enum import Enum

class Supertype(Enum):
    """Represents supertypes of cards in the game"""
    BASIC = 0
    LEGENDARY = 1
    SNOW = 2
    WORLD = 3

class CardType(Enum):
    """Represents types of cards in the game"""
    ARTIFACT = 0
    CREATURE = 1
    ENCHANTMENT = 2
    INSTANT = 3
    LAND = 4
    PLANESWALKER = 5
    SORCERY = 6
    TRIBAL = 7

class LandType(Enum):
    """Represents types of lands"""
    PLAINS = 0
    ISLAND = 1
    SWAMP = 2
    MOUNTAIN = 3
    FOREST = 4
