from MTG.cardType import *
from MTG.abilities import *

class Characteristics():
    def __init__(self,
                 name='',
                 mana_cost=None,
                 color=None,
                 types=[],
                 subtype=[],
                 supertype=[],
                 text='',
                 abilities=[],
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

    def __repr__(self):
        return str(self.__dict__)


class GameObject():
    def __init__(self, characteristics=Characteristics(), controller=None, owner=None, zone=None):
        self.characteristics = characteristics
        self.controller = controller
        self.owner = owner
        self.zone = zone
        self.previousState = None

    def __repr__(self):
        return self.characteristics.name + ' in ' + str(self.zone if self.zone else 'None')


    def name(self):
        return self.characteristics.name
        
    def manacost(self):
        return self.characteristics.mana_cost

    def is_land(self):
        return CardType.LAND in self.characteristics.types

    def is_creature(self):
        return CardType.CREATURE in self.characteristics.types

    def is_instant(self):
        return CardType.INSTANT in self.characteristics.types

    def has_ability(self, ability):
        return StaticAbilities[ability] in self.characteristics.abilities