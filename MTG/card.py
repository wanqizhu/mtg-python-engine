import traceback

from MTG import gameobject
from MTG import helper_funcs



class Attributes():
    def __init__(self):
        # attributes goes here
        self.num_creatures_can_block = 1



class Card(gameobject.GameObject):
    target_criterias = None  # if targets, this is a list of boolean functions
    target_prompts = None  # list of strings
    targets_chosen = None

    triggers = {}

    activated_abilities = []

    static_effects = []
    continuous_effects = ''
    status = None


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


    ''' Returns a list of booleans, signifying each target's legality '''
    def target_legality(self):
        if (not isinstance(self.targets_chosen, list) or 
            not isinstance(self.target_criterias, list)):
            return []

        return [c(self, t) for c, t in 
                zip(self.target_criterias, self.targets_chosen)]


    def ID(self):
        pass

    def play_func(self):  # defaults to permanent
        permanent.make_permanent(self)





# need it here to avoid circular imports
from MTG import permanent
