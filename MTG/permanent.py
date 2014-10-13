__author__ = 'Michael'

from MTG.game_object import GameObject

class Status(object):
    tapped = False
    flipped = False
    face_up = True
    phased_in = True

class Permanent(GameObject):
    def __init__(self, characteristics, controller, status=None):
        GameObject.__init__(self, characteristics)
        self.controller = controller
        if status is None:
            self.status = Status()
        else:
            self.status = status

def make_permanent(card, controller):
    return Permanent(card.characteristics, controller)