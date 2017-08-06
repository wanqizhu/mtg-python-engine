from MTG.gameObject import GameObject
from MTG.zone import ZoneType
import sys

class Status(object):
    def __init__(self):
        self.tapped = False
        self.flipped = False
        self.face_up = True
        self.phased_in = True
        self.summoning_sick = True
        self.damage_taken = 0

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
        self.controller.game.battlefield.add(self)
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
        return CardType.Creature in self.characteristics.types

    def can_attack(self):
        return is_creature and not self.status.summoning_sick

    def take_damage(self, dmg):
        self.status.damage_taken += dmg
        # if self.is_creature() and self.status.damage_taken >= self.characteristics.toughness:
        #     # send state-based action for death
        #     pass

    def trigger(self, condition):
        pass



def make_permanent(card):
    return Permanent(card.characteristics, card.controller, card.owner, card)