import pdb

from MTG import cardtype
from MTG import abilities


class Characteristics():
    def __init__(self,
                 name='',
                 mana_cost='',
                 color=[],
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

    # see if this matches another Characteristics() instance
    def satisfy(self, criteria):
        if criteria is None:
            return True

        for c in criteria.__dict__:
            value = criteria.__dict__[c]
            # if value is not None, check if it matches
            if value and value != self.__dict__[c]:
                return False

        return True


class GameObject():
    def __init__(self, characteristics=Characteristics(),
                 controller=None, owner=None, zone=None, previousState=None):
        self.characteristics = characteristics
        self.controller = controller
        self.owner = owner
        self.zone = zone
        self.previousState = previousState
        if self.controller:
            self.game = self.controller.game

    def __repr__(self):
        # pdb.set_trace()
        return 'gameobject.GameObject %r in %r' % (self.name(),
                                                   self.zone if self.zone else 'None')

    def name(self):
        return self.characteristics.name

    def manacost(self):
        return self.characteristics.mana_cost

    @property
    def is_land(self):
        return cardtype.CardType.LAND in self.characteristics.types

    @property
    def is_creature(self):
        return cardtype.CardType.CREATURE in self.characteristics.types

    @property
    def is_instant(self):
        return cardtype.CardType.INSTANT in self.characteristics.types

    @property
    def is_artifact(self):
        return cardtype.CardType.ARTIFACT in self.characteristics.types

    @property
    def power(self):
        return self.characteristics.power if self.is_creature else None

    @property
    def toughness(self):
        return self.characteristics.toughness if self.is_creature else None

    def has_ability(self, ability):
        return abilities.StaticAbilities[ability] in self.characteristics.abilities

    def share_color(self, other):
        return bool(set(self.characteristics.color) & set(other.characteristics.color))

    def has_color(self, color):
        return color in self.characteristics.color

    def is_color(self, color):
        return color == self.characteristics.color
