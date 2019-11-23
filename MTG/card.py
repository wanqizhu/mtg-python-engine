import traceback

from MTG import gameobject


class Attributes():
    def __init__(self):
        # attributes goes here
        self.num_creatures_can_block = 1


class Card(gameobject.GameObject):
    triggers = {}

    activated_abilities = []

    static_effects = []
    continuous_effects = ''
    status = None


    def __init__(self, characteristics=None,
                 controller=None, owner=None, zone=None, previousState=None):

        super(Card, self).__init__(characteristics,
                                   controller, owner, zone, previousState)

        self.attributes = Attributes()


    def ID(self):
        pass

    def play_func(self):  # defaults to permanent
        permanent.make_permanent(self)





# need it here to avoid circular imports
from MTG import permanent
