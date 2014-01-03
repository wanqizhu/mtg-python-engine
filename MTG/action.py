from card_type import CardType
from permanent import Permanent

class Action(object):
    """Represents an action in the game. Specifically, something that
    goes on the stack"""

    def is_instant_speed(self):
        """Checks whether this action is instant speed, i.e. whether it can
        be played on top of other spells on the stack"""
        raise NotImplementedError()
        
    def is_stack_action(self):
        """Checks whether this action should be put on the stack. If false, it
        instead resolves immediately. Here mainly to support LandAction"""
        return True

    def resolve(self):
        """Does whatever is supposed to happen when the action resolves"""
        raise NotImplementedError()
        
class LandAction(Action):
    def __init__(self, card, controller):
        if not CardType.LAND in card.get_types():
            raise ValueError("Land actions can only be used to play land cards")
        self.card = card
        self.controller = controller
        
    def resolve(self):
        self.controller.put_into_play(Permanent(self.card))
        
    def is_instant_speed(self):
        return False
        
    def is_stack_action(self):
        return False
