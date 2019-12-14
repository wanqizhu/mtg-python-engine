import pdb
import time
import math
from collections import defaultdict, namedtuple
from sortedcontainers import SortedListWithKey

from MTG import cardtype
from MTG import static_abilities
from MTG import utils


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
    is_player = False
    is_token = False

    target_criterias = None  # if targets, this is a list of boolean functions
    target_prompts = None  # list of strings
    targets_chosen = None

    def __init__(self, characteristics=None,
                 controller=None, owner=None, zone=None, 
                 previousState=None):
        if not characteristics:
            characteristics = Characteristics()
        self.characteristics = characteristics
        self.controller = controller
        self._owner = owner
        self.zone = zone
        self.previousState = previousState
        self.effects = defaultdict(lambda: SortedListWithKey(
                                           [], lambda x : x.timestamp))

        self.timestamp = self.game.timestamp if self.game else None


    def __repr__(self):
        return '%r in %r (ID: %r)' % (self.name,
                         self.zone.zone_type if self.zone is not None else 'None',
                         id(self))

    def __str__(self):
        return str(self.name)

    def __eq__(x, y):
        return isinstance(y, x.__class__) and x.__repr__() == y.__repr__()

    def __hash__(self):
        return hash(self.__repr__())

    @property
    def owner(self):
        return self._owner if self._owner else self.controller

    @property
    def game(self):
        return self.controller.game if self.controller else None

    @property
    def is_permanent(self):
        return self.zone.zone_type == 'BATTLEFIELD' if self.zone else False

    @property
    def is_spell(self):
        # TODO: what about abilities?
        return self.zone.zone_type == 'STACK' if self.zone else False

    @property
    def name(self):
        return self.characteristics.name

    @property
    def raw_manacost(self):
        return self.characteristics.mana_cost

    @property
    def manacost(self):
        cost = self.controller.mana.determine_costs(self.characteristics.mana_cost)
        # reduce/add costs
        if self.effects['additionalCost']:
            pass

        for effect in self.effects['reduceCost']:
            pass
            # TODO

        return cost

    # @property
    # def CMC(self):

    @property
    def is_land(self):
        return cardtype.CardType.LAND in self.characteristics.types

    @property
    def is_basic_land(self):
        return (cardtype.CardType.LAND in self.characteristics.types
                and cardtype.SuperType.BASIC in self.characteristics.supertype)

    @property
    def is_creature(self):
        return cardtype.CardType.CREATURE in self.characteristics.types

    @property
    def is_instant(self):
        return cardtype.CardType.INSTANT in self.characteristics.types

    @property
    def is_sorcery(self):
        return cardtype.CardType.SORCERY in self.characteristics.types

    @property
    def is_artifact(self):
        return cardtype.CardType.ARTIFACT in self.characteristics.types

    @property
    def is_enchantment(self):
        return cardtype.CardType.ENCHANTMENT in self.characteristics.types

    @property
    def is_aura(self):
        return self.is_enchantment and 'Aura' in self.characteristics.subtype

    @property
    def is_equipment(self):
        return self.is_artifact and 'Equipment' in self.characteristics.subtype


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
        return static_abilities.StaticAbilities[ability] in self.characteristics.abilities

    def share_color(self, other):
        return bool(set(self.characteristics.color) & set(other.characteristics.color))

    def has_color(self, color):
        return color in self.characteristics.color

    def is_color(self, color):
        """ color is a list"""
        return color == self.characteristics.color

    @property
    def is_monocolored(self):
        return len(self.characteristics.color) == 1

    @property
    def is_multicolored(self):
        return len(self.characteristics.color) > 1

    @property
    def is_colorless(self):
        return len(self.characteristics.color) == 0

    def has_subtype(self, subtype):
        return subtype in self.characteristics.subtype

    def exile(self):
        self.change_zone(self.owner.exile)


    ### Targeting ###

    def targets(self):
        targets_chosen = utils.choose_targets(self)
        if isinstance(targets_chosen, list):
            self.targets_chosen = targets_chosen
        return targets_chosen


    ''' Returns a list of booleans, signifying each target's legality '''
    def target_legality(self):
        if (not isinstance(self.targets_chosen, list) or 
            not isinstance(self.target_criterias, list)):
            return []

        return [c(self, t) for c, t in 
                zip(self.target_criterias, self.targets_chosen)]

    def has_valid_target(self):
        if self.target_criterias is None:
            return True

        # for each target criteria, check if at least one TARGETABLE OBJECT
        # somewhere satisfies this criteria (i.e. is targetable)
        for crit in self.target_criterias:
            has_valid_target = False
            for _zone in ['battlefield', 'stack',
                          'graveyard', 'exile']:
                has_valid_target = self.game.apply_to_zone(lambda _: True, _zone, lambda card: crit(self, card))
                if has_valid_target:
                    break

            # see if it can target players
            if not has_valid_target:
                has_valid_target = self.game.apply_to_players(lambda p: crit(self, p))

            if not has_valid_target:
                print(f"{self}: No valid targets.")
                return False

        return True


    def choose_targets(self):
        targets_chosen = utils.choose_targets(self)
        if isinstance(targets_chosen, list):
            self.targets_chosen = targets_chosen

        return targets_chosen


    def change_zone(self, target_zone, from_top=0, shuffle=True,
                    status_mod=None, modi_func=None):
        if target_zone == self.zone:
            return False

        current_zone = self.zone
        if not current_zone:
            c = self
        else:
            if current_zone.remove(self):
                if current_zone.is_battlefield and self.original_card:
                    self.controller.remove_static_effect(self)
                    c = self.original_card  # shift from permanent back to card
                    c.previousState = self
                else:
                    c = self
            else:
                return False

        if target_zone.is_public:
            self.timestamp = self.game.timestamp  # reset timestamp

        if target_zone.is_library:
            return target_zone.add(c, from_top, shuffle)
        elif target_zone.is_battlefield:
            return target_zone.add(c, status_mod, modi_func)
        else:
            return target_zone.add(c)
