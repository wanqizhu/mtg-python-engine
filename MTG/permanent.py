import sys
import pdb
import math
from collections import defaultdict, namedtuple
from sortedcontainers import SortedListWithKey
from functools import reduce


from MTG import gameobject
from MTG import zone
from MTG import cardtype
from MTG import mana
from MTG import triggers
from MTG import play


class Status():
    def __init__(self):
        self.tapped = False
        self.flipped = False
        self.face_up = True
        self.phased_in = True
        self.summoning_sick = True
        self.damage_taken = 0
        self.is_attacking = []
        self.is_blocking = []
        self.counters = defaultdict(lambda: 0)

    def __repr__(self):
        return str(self.__dict__)


class Modifier():
    def __init__(self, target, modifications=[], to_apply=True):
        """
        Modifications is a list of tuples
            (name-of-method-to-modify, modified-value-or-function,
                (optional) add_on=False)

        If add_on is True and we're modifying a value, then the modification
         will be added on to the original value

        So (characteristics.power, 4, True) buffs creature by +4/+0, whereas
           (characteristics.power, 4) sets base power to 4

        """
        self.target = target
        self.original_methods = {}
        self.modified_methods = {}
        self.applied = True

        self.add(modifications, to_apply)

    @property
    def method_names(self):
        return self.original_methods.keys()

    def apply(self):
        """Essentially, what setattr() is doing is:

            reduce(...) gets to the object
             which actually contains the attribute/method we want to change

            so if name is 'tap' or any 1st level method of Permanent, it just return self.target

            but if name is 'characteristics.power', then it returns self.target[characteristics]

            Then, it performes 'target.name = modification' through setattr(...)

             where target is the target returned by reduce(getattr(...)) above
             and name is only the last part of name -- the actual name of the method

        This is akin to finding the path-to-file, then changing the file from that directory

        e.g. we're given a full path, and then we call
         setattr(path-to-directory, filename, value-to-assign)

        In the case where name is just a 1st level method, this call is equivalent to
         setattr(self.target, name, modification)

        Or: eval('self.target.' + name + ' = ' + modification)

        """
        for name, modification in self.modified_methods.items():
            setattr(
                reduce(getattr, name.split('.')[:-1], self.target),
                name.split('.')[-1],
                modification)

        self.applied = True

    def reset(self):
        for name, original in self.original_methods.items():
            setattr(
                reduce(getattr, name.split('.')[:-1], self.target),
                name.split('.')[-1],
                original)
        self.applied = False

    def add(self, modifications, to_apply=True):
        for name, modification, *is_add_on in modifications:
            """The reason why we use reduce is so we can parse names like

            characteristics.power

            Essentially, if name refers to a method of Permanent (e.g. 'tap'),
            then a simple getattr/setattr call will suffice (e.g. getattr(self.target, 'tap'))

            But that doesn't work with 'characteristics.power'

            So we need to chain getattr/setattr using reduce
            """


            self.original_methods[name] = reduce(getattr, name.split('.'),
                                                 self.target)

            if is_add_on and is_add_on[0] is True:
                modification += self.original_methods[name]

            self.modified_methods[name] = modification

            if to_apply:
                setattr(
                    reduce(getattr, name.split('.')[:-1], self.target),
                    name.split('.')[-1],
                    modification)

        if to_apply and self.applied:
            self.applied = True
        else:
            self.applied = False


# used in Permanent().effects
Effect = namedtuple('Effect', ['value', 'source', 'expiration', 'timestamp'])


class Permanent(gameobject.GameObject):
    def __init__(self, characteristics, controller, owner=None, original_card=None, status=None, modifications=[]):
        self.characteristics = characteristics
        self.controller = controller
        self.game = controller.game
        self.owner = owner if owner else controller
        self.zone = zone.ZoneType.BATTLEFIELD
        self.original_card = original_card
        self.attributes = original_card.attributes
        self.modifier = Modifier(self, modifications)
        # sort by timestamp
        # each self.effects[name] is a sortedlist of Effect = namedtuple
        # each tuple always ends with (..., EXPIRATION_TIME, TIMESTAMP)
        self.effects = defaultdict(lambda: SortedListWithKey(
                                           [], lambda x : x.timestamp))

        if status is None:
            self.status = Status()
        else:
            self.status = status

        if original_card:
            self.activated_abilities = original_card.activated_abilities
            self._activated_abilities_costs_validation = original_card._activated_abilities_costs_validation
            self._activated_abilities_costs = original_card._activated_abilities_costs
            self._activated_abilities_effects = original_card._activated_abilities_effects
            self.trigger_listeners = original_card.trigger_listeners

        # add to battlefield
        self.controller.battlefield.add(self)
        # pdb.set_trace()
        print("making permanent... {}\n".format(self))

    def __repr__(self):
        return (super(Permanent, self).__repr__() + ' controlled by '
                + str(self.controller if self.controller else 'None'))

    def activate_ability(self, num=0):
        # if self._activated_abilities_costs_validation[num](self):
        print("activating...")
        self._activated_abilities_effects[num](self)
        return True
        # return False

    def clear_modifier(self):
        """Clears end-of-turn effects"""
        self.modifier.reset()

    def add_effect(self, name, value, source=None, expiration=math.inf):
        eff = Effect(value, source, expiration, self.controller.game.timestamp)
        self.effects[name].add(eff)
        self.check_effect_expiration()

    def check_effect_expiration(self, name=None):
        time = self.controller.game.timestamp
        if name is None:
            for category in self.effects.values():
                for eff in category[:]:
                    if eff.expiration < time:
                        category.remove(eff)
                        print("%r has expired" % eff)
        else:
            for eff in self.effects[name]:
                if eff.expiration < time:
                    self.effects[name].remove(eff)
                    print("%r has expired" % eff)


    def tap(self):
        self.status.tapped = True

    def untap(self):
        if (self.status.tapped):
            self.status.tapped = False
            # self.untapTrigger()

    # power/toughness layering -- see rule 613.3
    @property
    def power(self):
        if self.is_creature:
            return self._calculate_pt()[0]
        else:
            return None

    @property
    def toughness(self):
        if self.is_creature:
            return self._calculate_pt()[1]
        else:
            return None

    def _calculate_pt(self):
        # layer 7a
        power = self.characteristics.power
        toughness = self.characteristics.toughness

        # layer 7b
        for effect in self.effects['setPT']:
            if effect.value[0] != '*':  # keep it as is
                power = effect.value[0]
            if effect[1] != '*':
                toughness = effect.value[1]

        # layer 7c
        for effect in self.effects['modifyPT']:
            power += effect.value[0]
            toughness += effect.value[1]

        # layer 7d
        power += self.status.counters["+1/+1"] - self.status.counters["-1/-1"]
        toughness += self.status.counters["+1/+1"] - self.status.counters["-1/-1"]

        for effect in self.effects['switchPT']:  # layer 7e
            power, toughness = toughness, power

        return power, toughness

    def can_attack(self):
        return (self.is_creature and not self.status.tapped and
                (not self.status.summoning_sick or self.has_ability("Haste")))

    def can_block(self, attackers=None):
        if attackers:
            if type(attackers) is not list:
                attackers = [attackers]

            if self.attributes.num_creatures_can_block < len(attackers):
                return False

            for attacker in attackers:
                if (attacker.has_ability('Flying')
                    and not (self.has_ability('Flying')
                             or self.has_ability('Reach'))):
                    return False

                if (attacker.has_ability('Intimidate')
                        and not (self.is_artifact or self.share_color(attacker))):
                    return False
                # TODO: other blocking restrictions (e.g. can't block alone)
                pass

        return self.is_creature and not self.status.tapped

    def attacks(self, player):
        # trigger
        self.status.is_attacking = player

    def blocks(self, creature):
        if self.can_block(creature):
            # trigger
            # if self.status.is_blocking is None:
            #     self.status.is_blocking = []
            self.status.is_blocking.append(creature)
            if type(creature.status.is_attacking) == type(self.controller):
                creature.status.is_attacking = []

            creature.status.is_attacking.append(self)

            return True
        else:
            return False

    @property
    def in_combat(self):
        return self.status.is_attacking or self.status.is_blocking

    def exits_combat(self):
        self.status.is_attacking = []
        self.status.is_blocking = []

    def take_damage(self, source, dmg):
        # trigger based on source
        self.status.damage_taken += dmg
        print("{} takes {} damage from {}\n".format(self, dmg, source))
        if source.has_ability("Deathtouch"):
            self.dies()
        # pdb.set_trace()

    def deals_damage(self, target, dmg):
        """ target could be Player, Creature, or array of creatures"""
        if dmg < 0:
            return

        if isinstance(target, list):
            dmg_to_assign = self.power
            for blocker in target:
                if self.has_ability("Deathtouch"):
                    lethal_dmg = 1
                else:
                    lethal_dmg = blocker.toughness

                if blocker == target[-1]:
                    # all remaining dmg goes to last creature
                    if not self.has_ability("Trample"):
                        lethal_dmg = dmg_to_assign

                if dmg_to_assign < lethal_dmg:
                    blocker.take_damage(self, dmg_to_assign)
                    dmg_to_assign = 0
                else:
                    blocker.take_damage(self, lethal_dmg)
                    dmg_to_assign -= lethal_dmg

            if self.has_ability("Trample"):  # remaining dmg from trample
                self.deals_damage(target[0].controller, dmg_to_assign)

        else:
            # a single creature or a player
            target.take_damage(self, dmg)

        # TODO: check damage actually went through
        if self.has_ability("Lifelink"):
            self.controller.gain_life(dmg)
        # TODO: triggers

    def trigger(self, condition):
        # TODO: more triggers
        if condition == triggers.triggerConditions.onUpkeep:
            self.status.summoning_sick = False
        elif condition == triggers.triggerConditions.onCleanup:
            self.status.damage_taken = 0
            # clear end-of-turn effects

        if condition in self.trigger_listeners:
            print("Trigger to be process at next priority...\n")
            self.controller.pending_triggers.extend(
                [play.Play(lambda: effect(self))
                 for effect in self.trigger_listeners[condition]])

    def dies(self):
        # trigger
        print("{} has died\n".format(self))
        self.zone = zone.ZoneType.GRAVEYARD
        self.controller.battlefield.remove(self)
        c = self.original_card
        c.previousState = self
        self.controller.graveyard.add(c)

    def destroy(self):
        self.dies()

    def add_counter(self, counter, num=1):
        self.status.counters[counter] += num


def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)
