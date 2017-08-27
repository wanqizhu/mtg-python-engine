import pdb
import time
from collections import defaultdict, namedtuple
from sortedcontainers import SortedListWithKey

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
        self.effects = defaultdict(lambda: SortedListWithKey(
                                           [], lambda x : x.timestamp))

    def __repr__(self):
        # pdb.set_trace()
        return '%r in %r' % (self.name,
                             self.zone.zone_type if self.zone else 'None')

    def __str__(self):
        return self.name

    @property
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
    def is_enchantment(self):
        return cardtype.CardType.ENCHANTMENT in self.characteristics.types

    @property
    def power(self):
        return self.characteristics.power if self.is_creature else None

    @property
    def toughness(self):
        return self.characteristics.toughness if self.is_creature else None

    def has_ability(self, ability):
        for effect in self.effects['gainAbility']:
            if ability in effect.value:
                return True

        ability = ability.replace(' ', '_')
        return abilities.StaticAbilities[ability] in self.characteristics.abilities

    def share_color(self, other):
        return bool(set(self.characteristics.color) & set(other.characteristics.color))

    def has_color(self, color):
        return color in self.characteristics.color

    def is_color(self, color):
        """ color is a list"""
        return color == self.characteristics.color


    def change_zone(self, target_zone, from_top=0, shuffle=True):
        current_zone = self.zone
        if current_zone.remove(self):
            if target_zone.is_library:
                return target_zone.add(self, from_top, shuffle)
            else:
                return target_zone.add(self)

        return False
