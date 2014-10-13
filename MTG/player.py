from MTG.mana import ManaPool
from MTG.zone import Hand

__author__ = 'Michael'




class Player(object):
    won = False
    lost = False

    def __init__(self, interface, life=20):
        self.interface = interface
        self.life = life
        self.hand = Hand()
        self.mana_pool = ManaPool()