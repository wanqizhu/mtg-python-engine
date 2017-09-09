import sys
import pdb
import math
import re
from collections import defaultdict, namedtuple
from sortedcontainers import SortedListWithKey
from functools import reduce


from MTG import gameobject
from MTG import zone
from MTG import cardtype
from MTG import triggers
from MTG import play
from MTG import abilities




# class Modifier():
#     def __init__(self, target, modifications=[], to_apply=True):
#         """
#         Modifications is a list of tuples
#             (name-of-method-to-modify, modified-value-or-function,
#                 (optional) add_on=False)

#         If add_on is True and we're modifying a value, then the modification
#          will be added on to the original value

#         So (characteristics.power, 4, True) buffs creature by +4/+0, whereas
#            (characteristics.power, 4) sets base power to 4

#         """
#         self.target = target
#         self.original_methods = {}
#         self.modified_methods = {}
#         self.applied = True

#         self.add(modifications, to_apply)

#     @property
#     def method_names(self):
#         return self.original_methods.keys()

#     def apply(self):
#         """Essentially, what setattr() is doing is:

#             reduce(...) gets to the object
#              which actually contains the attribute/method we want to change

#             so if name is 'tap' or any 1st level method of Permanent, it just return self.target

#             but if name is 'characteristics.power', then it returns self.target[characteristics]

#             Then, it performes 'target.name = modification' through setattr(...)

#              where target is the target returned by reduce(getattr(...)) above
#              and name is only the last part of name -- the actual name of the method

#         This is akin to finding the path-to-file, then changing the file from that directory

#         e.g. we're given a full path, and then we call
#          setattr(path-to-directory, filename, value-to-assign)

#         In the case where name is just a 1st level method, this call is equivalent to
#          setattr(self.target, name, modification)

#         Or: eval('self.target.' + name + ' = ' + modification)

#         """
#         for name, modification in self.modified_methods.items():
#             setattr(
#                 reduce(getattr, name.split('.')[:-1], self.target),
#                 name.split('.')[-1],
#                 modification)

#         self.applied = True

#     def reset(self):
#         for name, original in self.original_methods.items():
#             setattr(
#                 reduce(getattr, name.split('.')[:-1], self.target),
#                 name.split('.')[-1],
#                 original)
#         self.applied = False

#     def add(self, modifications, to_apply=True):
#         for name, modification, *is_add_on in modifications:
#             """The reason why we use reduce is so we can parse names like

#             characteristics.power

#             Essentially, if name refers to a method of Permanent (e.g. 'tap'),
#             then a simple getattr/setattr call will suffice (e.g. getattr(self.target, 'tap'))

#             But that doesn't work with 'characteristics.power'

#             So we need to chain getattr/setattr using reduce
#             """

#             self.original_methods[name] = reduce(getattr, name.split('.'),
#                                                  self.target)

#             if is_add_on and is_add_on[0]:
#                 modification += self.original_methods[name]

#             self.modified_methods[name] = modification

#             if to_apply:
#                 setattr(
#                     reduce(getattr, name.split('.')[:-1], self.target),
#                     name.split('.')[-1],
#                     modification)

#         if to_apply and self.applied:
#             self.applied = True
#         else:
#             self.applied = False



class Status():
    def __init__(self):
        self.tapped = False
        self.not_untap = 0  # 0: untap normally; 1: not untap next turn; math.inf: not untap
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


    def __str__(self):
        s = []
        s.append('tapped' if self.tapped else '')
        s.append('will not untap for %i turns' % self.not_untap if self.not_untap else '')
        s.append('flipped' if self.flipped else '')
        s.append('face down' if not self.face_up else '')
        s.append('phased out' if not self.phased_in else '')
        s.append('is summoning sick' if self.summoning_sick else '')
        s.append('has taken %i damage' % self.damage_taken if self.damage_taken else '')
        s.append('is attacking %s' % str(self.is_attacking) if self.is_attacking else '')
        s.append('is blocking %s' % str(self.is_blocking) if self.is_blocking else '')
        s.extend(['has %i %s counters' % (num, name)
                        for name, num in self.counters.items()
                        if num > 0])

        # remove empty ''
        return 'Status: ' + ', '.join([i for i in s if i])




class Effect():
    """ name: name of effct (dict key to self.effects)

    expiration: either a float representing timestamp (usually eot),
                or a function (lambda eff: ...) that when evaluated to True signals expiration

    toggle_func is the function that, while inactive, if evaluated to True toggles on the effct
        while active, the toggle function is negated; thus, it is passed into Effect(...)
        as a boolean dictionary (toggle_funcs)
    """
    def __init__(self, value, timestamp, apply_target=None, source=None, expiration=math.inf, is_active=True,
                 toggle_func=lambda eff: False):
        self.value = value
        self.source = source
        self.expiration = expiration
        self.is_active = is_active
        self.toggle_funcs = {False: toggle_func,
                             True: lambda eff: not toggle_func(eff)}
        self.timestamp = timestamp
        self.apply_target = apply_target



class Permanent(gameobject.GameObject):
    def __init__(self, characteristics, controller, owner=None, original_card=None, status=None, modifications=[]):
        self.characteristics = characteristics
        self.controller = controller
        self.game = controller.game
        self._owner = owner
        self.zone = self.controller.battlefield
        self.original_card = original_card
        # self.modifier = Modifier(self, modifications)
        self.timestamp = self.game.timestamp
        # sort by timestamp
        # each self.effects[name] is a sortedlist of Effect
        # including (..., EXPIRATION_TIME, TIMESTAMP)
        self.effects = defaultdict(lambda: SortedListWithKey(
                                           [], lambda x : x.timestamp))

        for name, value, source, toggle_func in self.controller.static_effects:
            # apply existing static effects
            self.add_effect(name, value, source=source, is_active=False, toggle_func=toggle_func)

        if status is None:
            if original_card and original_card.status:
                self.status = original_card.status
            else:
                self.status = Status()
        else:
            self.status = status

        if original_card:
            self.attributes = original_card.attributes
            self.activated_abilities = [abilities.ActivatedAbility(self, *params)
                                        for params in original_card.activated_abilities]
            # params[0] is the trigger condition
            self.trigger_listeners = {condition: [abilities.TriggeredAbility(self, *params) for params in trigs]
                                      for condition, trigs in original_card.triggers.items()}
            self.continuous_effects = original_card.continuous_effects

            for apply_to, name, value, toggle_func in original_card.static_effects:
                if apply_to == 'self':
                    self.add_effect(name, value, source=self, is_active=False, toggle_func=toggle_func)
                elif apply_to == 'controller':
                    self.controller.add_static_effect(name, value, source=self, toggle_func=toggle_func)
                elif apply_to == 'game':
                    self.game.add_static_effect(name, value, source=self, toggle_func=toggle_func)
                elif apply_to == 'controller -self':  # does not apply ability to self (e.g. 'other creatures ...')
                    self.controller.add_static_effect(name, value, source=self, toggle_func=toggle_func, exempt_source=True)
                elif apply_to == 'game -self':
                    self.game.add_static_effect(name, value, source=self, toggle_func=toggle_func, exempt_source=True)

        else:
            self.attributes = []
            self.activated_abilities = []
            self.trigger_listeners = {}
            self.continuous_effects = ''



        self.controller.battlefield.add(self)
        self.is_token = False
        self.auras = []
        self.equipments = []
        # pdb.set_trace()
        print("making permanent... {}\n".format(self))

    def __repr__(self):
        return (self.__str__() +
                '\nowner: %s\n' % str(self.owner if self.owner else 'None') +
                str(self.status))

    def __str__(self):
        return ('%s controlled by %s (timestamp: %s)' % (
                super(Permanent, self).__repr__(),
                str(self.controller if self.controller else 'None'),
                self.timestamp))

    def __eq__(self, other):
        """ Check equality based on both ID and timestamp"""
        if isinstance(other, self.__class__):
            return id(self) == id(other) and self.timestamp == other.timestamp
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((id(self), self.timestamp))

    def activate_ability(self, num=0):
        print("activating ability... {}".format(self.activated_abilities[num]))
        # pdb.set_trace()
        # self._activated_abilities_effects[num](self)
        name = self.name + ' activated ability #' + str(num)
        return play.Play(
                    lambda: self.activated_abilities[num].resolve(), source=self.activated_abilities[num],
                    name=name, is_mana_ability=self.activated_abilities[num].is_mana_ability)

    # def clear_modifier(self):
    #     """Clears end-of-turn effects"""
    #     self.modifier.reset()

    def add_effect(self, name, value, source=None, expiration=math.inf,
                   is_active=True, toggle_func=lambda eff: True):
        if expiration == math.inf and source:
            # static effect; auto expries if source expires
            t = source.timestamp
            expiration = lambda eff: eff.source.timestamp != t

        eff = Effect(value, self.controller.game.timestamp, self, source,
                     expiration, is_active, toggle_func)
        self.effects[name].add(eff)
        self.check_effect_expiration()

    def get_effect(self, name):
        if name in self.effects:
            return [eff for eff in self.effects[name] if eff.is_active]
        else:
            return []

    def check_effect_expiration(self):
        did_something = False
        time = self.controller.game.timestamp
        for category in self.effects.values():
            for eff in category[:]:
                if eff.toggle_funcs[eff.is_active](eff):
                    eff.is_active = not eff.is_active
                    print("{} active/nonactive toggled".format(eff))

                if isinstance(eff.expiration, (int, float)):
                    if eff.expiration < time:
                        category.remove(eff)
                        print("{} has expired (time)".format(eff))
                        did_something = True

                elif callable(eff.expiration):
                    if eff.expiration(eff):
                        category.remove(eff)
                        print("{} has expired (condition)".format(eff))
                        did_something = True

        return did_something




    def tap(self):
        if not self.status.tapped:
            self.status.tapped = True
            self.trigger("onTap")
            return True
        return False

    def untap(self):
        if (self.status.tapped) and not self.status.not_untap:
            self.status.tapped = False
            self.trigger("onUntap")
            return True

        if self.status.not_untap:
            self.status.not_untap -= 1
        return False

    def freeze(self):
        """ Does not untap next turn """
        if self.status.not_untap == 0:
            self.status.not_untap = 1

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

    def add_counter(self, counter="+1/+1", num=1):
        self.status.counters[counter] += num

    def num_counters(self, counter):
        return self.status.counters[counter]

    def _calculate_pt(self):
        # layer 7a
        power = self.characteristics.power
        toughness = self.characteristics.toughness

        # layer 7b
        for effect in self.get_effect('setPT'):
            if effect.value[0] != '*':  # keep it as is
                power = effect.value[0]
            if effect[1] != '*':
                toughness = effect.value[1]

        # layer 7c
        for effect in self.get_effect('modifyPT'):
            power += effect.value[0]
            toughness += effect.value[1]

        # layer 7d
        power += self.status.counters["+1/+1"] - self.status.counters["-1/-1"]
        toughness += self.status.counters["+1/+1"] - self.status.counters["-1/-1"]

        for effect in self.get_effect('switchPT'):  # layer 7e
            power, toughness = toughness, power

        return power, toughness

    @property
    def is_summoning_sick(self):
        return (self.is_creature and self.status.summoning_sick
                    and not self.has_ability("Haste"))

    def can_attack(self):
        return (self.is_creature and not self.status.tapped
                and not self.is_summoning_sick and not self.has_ability("Defender"))

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

                for landtype in ["Plains", "Island", "Swamp", "Mountain", "Forest"]:
                    if attacker.has_ability(landtype+"walk") and self.controller.controls(subtype=landtype):
                        return False

                # TODO: other blocking restrictions (e.g. can't block alone)
                pass

        return self.is_creature and not self.status.tapped

    def attacks(self, player):
        # trigger
        self.status.is_attacking = player
        if not self.has_ability("Vigilance"):
            self.tap()

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

    def take_damage(self, source, dmg, is_combat=False):
        # trigger based on source
        self.trigger('onTakeDamage', dmg)
        if is_combat:
            self.trigger('onTakeCombatDamage', dmg)

        self.status.damage_taken += dmg
        print("{} takes {} damage from {}\n".format(self, dmg, source))
        if source.has_ability("Deathtouch"):
            self.destroy()
        # pdb.set_trace()

    def deals_damage(self, target, dmg, is_combat=False):
        """ target could be Player, Creature, or array of creatures"""

        ## TODO: deal damage NOT trigger if dmg is prevented
        if dmg < 0:
            return

        self.trigger('onDealDamage', dmg)
        if is_combat:
            self.trigger('onCombatDamage', dmg)

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
                    blocker.take_damage(self, dmg_to_assign, is_combat)
                    dmg_to_assign = 0
                else:
                    blocker.take_damage(self, lethal_dmg, is_combat)
                    dmg_to_assign -= lethal_dmg

            if self.has_ability("Trample"):  # remaining dmg from trample
                self.deals_damage(target[0].controller, dmg_to_assign)

        else:
            # a single creature or a player
            if target.is_player:
                self.trigger('onDealDamageToPlayers', dmg)
                if is_combat:
                    self.trigger('onCombatDamageToPlayers', dmg)
            else:
                self.trigger('onDealDamageToCreature', dmg)
                if is_combat:
                    self.trigger('onCombatDamageToCreatures', dmg)
            target.take_damage(self, dmg, is_combat)

        # TODO: check damage actually went through
        if self.has_ability("Lifelink"):
            self.controller.gain_life(dmg)


    def trigger(self, condition, amount=1):
        """ amount: amount of life gained, damage dealt, etc. """
        # TODO: more triggers
        # technically, these aren't "triggers"; but putting them here suffices

        if isinstance(condition, str):
            condition = triggers.triggerConditions[condition]

        if condition == triggers.triggerConditions.onUpkeep:
            self.status.summoning_sick = False
        elif condition == triggers.triggerConditions.onCleanup:
            self.status.damage_taken = 0
            # clear end-of-turn effects

        if condition in self.trigger_listeners:
            print("Trigger %s to be process at next priority...\n" % condition)

            trigs = [trig for trig in self.trigger_listeners[condition]
                     if trig is not None and trig.condition_satisfied()]
            for trig in trigs:
                trig.trigger_amount = amount

            self.controller.pending_triggers.extend(trigs)

    def change_zone(self, target_zone, from_top=0, shuffle=True):
        for aura in self.auras[:]:
            aura.disenchant()

        return super(Permanent, self).change_zone(target_zone, from_top, shuffle)

    def dies(self):
        # trigger first so we can use last-known state (while it's still a permanent)
        self.trigger('onDeath')
        print("{} has died\n".format(self))
        return self.change_zone(self.owner.graveyard)

    def destroy(self):
        #trigger
        if self.has_ability("Indestructible") and self.toughness > 0:
            print("Indestructible")
            return False

        if self.dies():
            return True

    def sacrifice(self):
        #trigger
        print("Sacrificing")
        if self.dies():
            return True

    def exile(self):
        self.change_zone(self.owner.exile)

    def bounce(self):
        self.change_zone(self.owner.hand)

    def flicker(self):
        self.change_zone(self.owner.exile)
        self.change_zone(self.owner.battlefield)




class Aura(Permanent):
    def __init__(self, enchant_target, characteristics, controller, owner=None, original_card=None):
        super(Aura, self).__init__(characteristics, controller, owner, original_card)

        self.enchant(enchant_target)

        eval(self.continuous_effects)


    def enchant(self, target):
        target.auras.append(self)
        self.enchant_target = target
        pass

    def disenchant(self):
        target.auras.remove(self)
        self.enchant_target = None

    def add_ability(self, ability):
        enchanted_creature = self.enchant_target
        # not sure how to dynamically check this & make sure all associations expire/update correctly
        enchanted_creature.add_effect("gainAbility", ability, self, lambda eff: eff.source.enchant_target != enchanted_creature)

    def add_pt(self, PT):
        enchanted_creature = self.enchant_target
        enchanted_creature.add_effect("modifyPT", PT, self, lambda eff: eff.source.enchant_target != enchanted_creature)




def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)

def make_aura(card, enchant_target):
    return Aura(enchant_target, card.characteristics, card.controller, card.owner, card)