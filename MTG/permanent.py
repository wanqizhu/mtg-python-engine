import sys, pdb
from enum import Enum

from MTG import gameobject
from MTG import zone
from MTG import cardtype
from MTG import mana



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


class Status():
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



class Permanent(gameobject.GameObject):
    def __init__(self, characteristics, controller, owner=None, original_card=None, status=None):
        self.characteristics = characteristics
        self.controller = controller
        self.owner = owner if owner else controller
        self.zone = zone.ZoneType.BATTLEFIELD
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

    def is_creature(self):
        return cardtype.CardType.CREATURE in self.characteristics.types

    def can_attack(self):
        return (self.is_creature() and not self.status.tapped and 
                    (not self.status.summoning_sick or self.has_ability("Haste")))

    def can_block(self, attacker=None):
        if attacker:
            if (attacker.has_ability('Flying') 
                        and not (self.has_ability('Flying')
                            or self.has_ability('Reach'))):
                return False

            if (attacker.has_ability('Intimidate')
                    and not (self.is_artifact() or self.share_color(attacker))):
                return False
            pass  ## TODO: other blocking restrictions (e.g. can't block alone)
        
        return self.is_creature() and not self.status.tapped



    def attacks(self, player):
        # trigger
        self.status.is_attacking = player

    def blocks(self, creature):
        if self.can_block(creature):
            # trigger
            self.status.is_blocking = creature
            if type(creature.status.is_attacking) == type(self.controller):
                creature.status.is_attacking = []  ## TODO: multi-blocks
            
            creature.status.is_attacking.append(self)

            return True
        else:
            return False

    def in_combat(self):
        return self.status.is_attacking or self.status.is_blocking

    def exits_combat(self):
        self.status.is_attacking = None
        self.status.is_blocking = None

    def take_damage(self, source, dmg):
        ## trigger based on source
        self.status.damage_taken += dmg
        print("{} takes {} damage from {}\n".format(self, dmg, source))
        if source.has_ability("Deathtouch"):
            self.dies()
        # pdb.set_trace()


    def deals_damage(self, target, dmg):
        """ target could be Player, Creature, or array of creatures"""
        if isinstance(target, list):
            dmg_to_assign = self.characteristics.power
            for blocker in target:
                if self.has_ability("Deathtouch"):
                    lethal_dmg = 1
                else:
                    lethal_dmg = blocker.characteristics.toughness
                if dmg_to_assign < lethal_dmg:
                    blocker.take_damage(self, dmg_to_assign)
                    dmg_to_assign = 0
                else:
                    blocker.take_damage(self, lethal_dmg)
                    dmg_to_assign -= lethal_dmg
        else:
            # a single creature or a player
            target.take_damage(self, dmg)
        ## TODO: triggers


    def trigger(self, condition):
        ## TODO: more triggers
        if condition == triggerConditions.onUpkeep:
            self.status.summoning_sick = False
        elif condition == triggerConditions.onCleanup:
            self.status.damage_taken = 0
            # clear end-of-turn effects

    def dies(self):
        ## trigger
        print("{} has died\n".format(self))
        self.zone = zone.ZoneType.GRAVEYARD
        self.controller.battlefield.remove(self)
        self.controller.graveyard.add(self)



def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)