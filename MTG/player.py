from MTG.mana import *
from MTG.zone import *
from MTG.play import *
import re




class EmptyLibraryException(Exception):
    pass


class Player(object):

    def __init__(self, deck, name='player', startingLife=20, maxHandSize=7, game=None):
        self.name = name
        # self.ID = None
        self.life = startingLife
        self.maxHandSize = maxHandSize
        self.library = Library(deck)
        self.hand = Hand()
        self.graveyard = Graveyard()
        self.exile = Exile()
        self.mana = ManaPool()
        self.game = game


    ## TODO
    def get_action(self):
        """ asks the player to do something

        this gets called whenever a player has priority
        """
        answer = input("What would you like to do?\n")
        play = None

        while answer and play is None:
            try:
                if answer[0] == 'h':  # playing card from hand -- 'h3' == plays third card in hand
                    num = int(answer[1:])
                    assert num < self.hand.size()
                    card = self.hand.pop(num)
                    ## pay mana costs
                    ## choose targets
                    if True:
                        play = Play(card.play_func)
                        # special actions
                        if card.is_land():
                            play.is_special_action = True
                    else:
                        self.hand.append(card)  # illegal casting, revert

            except:
                answer = input("Bad format.\nWhat would you like to do?\n")
                continue

        return play






    def draw(self, num=1):
        for i in num:
            try:
                self.hand.add(self.Library.pop())
            except IndexError:
                raise EmptyLibraryException()

    def discard(self, num=1):
        if num > self.hand.size():
            return False
        for i in num:
            self.graveyard.add(self.hand.pop())


    def pay(self, mana, life=0):
        """
        mana: a dict of Mana(Enum)
        """

        # verify we have enough resources
        if self.life - life <= 0:
            return False
        # TODO: smart paying restrictionless mana costs
        for manatype in mana:
            if self.ManaPool[manatype] < mana[manatype]:
                return False

        self.life -= life
        self.ManaPool.pay(mana)
        return True