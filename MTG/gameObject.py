from MTG.cardType import *

class Characteristics():
    def __init__(self,
                 name='',
                 mana_cost=None,
                 color=None,
                 types=None,
                 subtype=None,
                 supertype=None,
                 text=None,
                 abilities=None,
                 power=None,
                 toughness=None,
                 loyalty=None):
        self.name = name
        self.mana_cost = mana_cost
        self.color = color
        self.types = types
        self.subtype = subtype
        self.supertype = supertype
        self.text = text
        self.abilities = abilities
        self.power = power
        self.toughness = toughness
        self.loyalty = loyalty


class GameObject():
    def __init__(self, characteristics=Characteristics(), controller=None, zone=None):
        self.characteristics = characteristics
        self.controller = controller
        self.zone = zone

    def is_land(self):
        return CardType.Land in self.types

    def is_creature(self):
        return CardType.Creature in self.types