from MTG.gameObject import GameObject
from MTG.zone import ZoneType
from MTG.cardType import *
import sys
from enum import Enum


class triggerConditions(Enum):
    # zone changes
    onPlay = 0
    onDraw = 1
    onDiscard = 2
    onEtB = 3
    onPlayfromHand = 4
    onEnterGrave = 5
    onDeath = 6
    onLeaveBattlefield = 7
    # phase (CONTROLLER ONLY or ALL PLAYERS)
    onUpkeep = 10
    onMain1 = 11
    onMain2 = 12
    onEnterCombat = 13
    onDeclareAttackers = 14
    onDeclareBlockers = 15
    onEndofCombat = 16
    onEndstep = 17
    onCleanup = 18
    # events
    onUntap = 8
    onTap = 9
    
    onDealDamageToPlayers = 19
    onDealDamageToCreatures = 20
    onDealDamage = 21
    onTakingDamage = 22
    onAttack = 23
    onBlock = 24
    # global events
    onRevolt = 30 # permanent leaving battlefield
    onControllerLifeLoss = 31
    onLifeLoss = 32
    onControllerLifeGain = 33
    onLifeGain = 34
    onCounterPutOnPermanent = 35


class Status(object):
    def __init__(self):
        self.tapped = False
        self.flipped = False
        self.face_up = True
        self.phased_in = True
        self.summoning_sick = True
        self.damage_taken = 0
        self.is_attacking = None
        self.is_blocking = None

    def __repr__(self):
        return str(self.__dict__)



class Permanent(GameObject):
    def __init__(self, characteristics, controller, owner=None, original_card=None, status=None):
        GameObject.__init__(self, characteristics)
        self.controller = controller
        self.owner = owner if owner else controller
        self.zone = ZoneType.BATTLEFIELD
        self.original_card = original_card
        if status is None:
            self.status = Status()
        else:
            self.status = status

        if original_card:
            self.activated_abilities = original_card.activated_abilities
            self._activated_abilities_costs_validation = original_card._activated_abilities_costs_validation
            self._activated_abilities_costs = original_card._activated_abilities_costs
            self._activated_abilities_effects = original_card._activated_abilities_effects

        # add to battlefield
        self.controller.battlefield.add(self)
        print("making permanent... {}\n".format(self))

    def __repr__(self):
        return super(Permanent, self).__repr__() + ' controlled by ' + str(self.controller if self.controller else 'None')


    def activate_ability(self, num=0):
        try:
            # if self._activated_abilities_costs_validation[num](self):
            print("activating...")
            self._activated_abilities_costs[num](self)
            self._activated_abilities_effects[num](self)
            return True
        except:
            print(sys.exc_info())
            return False


    def tap(self):
        self.status.tapped = True

        
    def untap(self):
        if (self.status.tapped):
            self.status.tapped = False
            #self.untapTrigger()

    def is_creature(self):
        return CardType.CREATURE in self.characteristics.types

    def can_attack(self):
        return self.is_creature() and not self.status.tapped and not self.status.summoning_sick

    def can_block(self):
        return self.is_creature() and not self.status.tapped

    def attacks(self, player):
        # trigger
        self.status.is_attacking = player

    def blocks(self, creature):
        # trigger
        self.status.is_blocking = creature
        creature.status.is_attacking = self  ## TODO: multi-blocks

    def take_damage(self, dmg):
        self.status.damage_taken += dmg
        # if self.is_creature() and self.status.damage_taken >= self.characteristics.toughness:
        #     # send state-based action for death
        #     pass

    def trigger(self, condition):
        if condition == triggerConditions.onUpkeep:
            self.status.summoning_sick = False
        elif condition == triggerConditions.onCleanup:
            self.status.damage_taken = 0
            # clear end-of-turn effects



def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)