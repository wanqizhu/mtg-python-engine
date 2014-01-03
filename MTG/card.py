# This file is currently a stub representing card objects

from card_type import *
from spell import Spell

class Card(object):
    """Superclass for all card classes (which will be generated dynamically)"""
    def get_text(self):
        raise NotImplementedError()
    
    def play(self, controller):
        if CardType.LAND in self.get_types():
            #I don't like this. Need consistent output
            controller.play_land(self)
        else:
            if self.is_modal():
                actions = controller.choose_mode(self.actions)
            else:
                actions = self.actions
            # TODO: Optional costs
            mana_cost = controller.choose_cost(self.cost)
            targets = controller.choose_targets(actions)
            divisions = controller.choose_divisions(actions, targets)
            cost = self.get_total_cost(mana_cost, actions, targets, divisions)
            payment = controller.pay_cost(cost)
            if payment:
                return Spell(self, controller, actions, targets, divisions, cost, payment)
            else:
                return None

def gen_card_class(oracle_text):
    """Generates a class for the particular card text"""
    class ThisCard(Card):
        pass
    return ThisCard
