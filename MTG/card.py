# This file is currently a stub representing card objects

from card_type import *
from spell import Spell
from action import LandAction

class Card(object):
    """Superclass for all card classes (which will be generated dynamically)"""
    def __init__(self, owner):
        self.owner = owner
    
    @property
    def text(self):
        raise NotImplementedError()
        
    def get_name(self):
        return self.name
        
    def get_types(self):
        return self.types
    
    def play(self, controller):
        if CardType.LAND in self.get_types():
            if player.can_play_land():
                return LandAction(self, controller)
            else:
                return None
        else:
            if self.is_modal():
                effects = controller.choose_mode(self.effects)
            else:
                effects = self.effects
            # TODO: Optional costs
            mana_cost = controller.choose_cost(self.cost)
            targets = controller.choose_targets(effects)
            divisions = controller.choose_divisions(effects, targets)
            cost = self.get_total_cost(mana_cost, effects, targets, divisions)
            payment = controller.pay_cost(cost)
            if payment:
                return Spell(self, controller, effects, targets, divisions, cost, payment)
            else:
                return None

def gen_card_class(oracle_text):
    """Generates a class for the particular card text"""
    class ThisCard(Card):
        pass
    return ThisCard
