__author__ = 'Michael'

from MTG.game_object import GameObject

class Status(object):
    tapped = False
    flipped = False
    face_up = True
    phased_in = True
    summoning_sick = True
    damage_taken = 0

class Permanent(GameObject):
    def __init__(self, characteristics, controller, original_card=None, status=None):
        GameObject.__init__(self, characteristics)
        self.controller = controller
        self.original_card = original_card
        if status is None:
            self.status = Status()
        else:
            self.status = status

    def untap(self):
        if (self.status.tapped):
            self.status.tapped = False
            #self.untapTrigger()

    def is_creature(self):
        return CardType.Creature in self.characteristics.types

    def can_attack(self):
        return is_creature and !self.status.summoning_sick

    def take_damage(self, dmg):
        self.status.damage_taken += dmg
        # if self.is_creature() and self.status.damage_taken >= self.characteristics.toughness:
        #     # send state-based action for death
        #     pass



def make_permanent(card, controller):
    return Permanent(card.characteristics, controller, card)