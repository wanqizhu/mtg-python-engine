import traceback

from MTG import gameobject
from MTG import helper_funcs



class Attributes():
    def __init__(self):
        # attributes goes here
        self.num_creatures_can_block = 1



class Card(gameobject.GameObject):
    target_criterias = None
    target_prompts = None
    targets_chosen = None

    triggers = {}

    activated_abilities = []

    continuous_effects = ''

    def __init__(self, characteristics=gameobject.Characteristics(),
                 controller=None, owner=None, zone=None, previousState=None):

        super(Card, self).__init__(characteristics,
                                   controller, owner, zone, previousState)

        self.attributes = Attributes()

    def targets(self):
        targets_chosen = helper_funcs.choose_targets(self)
        if isinstance(targets_chosen, list):
            self.targets_chosen = targets_chosen
        return targets_chosen

    def ID(self):
        pass

    def play_func(self):  # defaults to permanent
        permanent.make_permanent(self)





# need it here to avoid circular imports
from MTG import permanent
