import sys, pdb
from collections import defaultdict


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



class Permanent(gameobject.GameObject):
    def __init__(self, characteristics, controller, owner=None, original_card=None, status=None):
        self.characteristics = characteristics
        self.controller = controller
        self.game = controller.game
        self.owner = owner if owner else controller
        self.zone = zone.ZoneType.BATTLEFIELD
        self.original_card = original_card
        self.attributes = original_card.attributes
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
        return super(Permanent, self).__repr__() + ' controlled by ' + str(self.controller if self.controller else 'None')


    def activate_ability(self, num=0):
        if self._activated_abilities_costs_validation[num](self):
            print("activating...")
            self._activated_abilities_costs[num](self)
            self._activated_abilities_effects[num](self)
            return True
        return False


    def tap(self):
        self.status.tapped = True

        
    def untap(self):
        if (self.status.tapped):
            self.status.tapped = False
            #self.untapTrigger()

    @property
    def power(self):
        if self.is_creature:
            return (self.characteristics.power + self.status.counters["+1/+1"]
                                              - self.status.counters["-1/-1"])
        else:
            return None

    @property
    def toughness(self):
        if self.is_creature:
            return (self.characteristics.toughness + self.status.counters["+1/+1"]
                                              - self.status.counters["-1/-1"])
        else:
            return None


    def can_attack(self):
        return (self.is_creature and not self.status.tapped and 
                    (not self.status.summoning_sick or self.has_ability("Haste")))

    def can_block(self, attackers=None):
        if attackers:
            if type(attackers) is not list: attackers = [attackers]

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
                pass  ## TODO: other blocking restrictions (e.g. can't block alone)
        
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
        ## trigger based on source
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
                    if not self.has_ability("Trample"):  # all remaining dmg goes to last creature
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

        ## TODO: check damage actually went through
        if self.has_ability("Lifelink"):
            self.controller.gain_life(dmg)
        ## TODO: triggers


    def trigger(self, condition):
        ## TODO: more triggers
        if condition == triggers.triggerConditions.onUpkeep:
            self.status.summoning_sick = False
        elif condition == triggers.triggerConditions.onCleanup:
            self.status.damage_taken = 0
            # clear end-of-turn effects

        if condition in self.trigger_listeners:
            print("Trigger to be process at next priority...\n")
            self.game.pending_triggers.extend(
                [play.Play(lambda: effect(self))
                 for effect in self.trigger_listeners[condition]])

    def dies(self):
        ## trigger
        print("{} has died\n".format(self))
        self.zone = zone.ZoneType.GRAVEYARD
        self.controller.battlefield.remove(self)
        c = self.original_card
        c.previousState = self
        self.controller.graveyard.add(c)


    def add_counter(self, counter, num=1):
        self.status.counters[counter] += num



def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)