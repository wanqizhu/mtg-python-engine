from MTG.mana import *
from MTG.zone import *
from MTG.play import *
import re, sys, pdb




class EmptyLibraryException(Exception):
    pass


class Player(object):

    def __init__(self, deck, name='player', startingLife=20, maxHandSize=7, game=None):
        self.name = name
        # self.ID = None
        self.life = startingLife
        self.maxHandSize = maxHandSize
        self.library = Library(deck)
        for card in self.library.elements:
            card.controller = self
            card.owner = self
        self.hand = Hand()
        self.graveyard = Graveyard()
        self.exile = Exile()
        self.mana = ManaPool()
        self.game = game

    def __repr__(self):
        return self.name


    ## TODO
    def get_action(self):
        """ asks the player to do something

        this gets called whenever a player has priority
        """
        answer = input("\nWhat would you like to do?\n")
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

                elif answer[0] == 'b':  # activate ability from battlefield -- 'b3_1' plays 2nd (index starts at 0) ability from 3rd permanent
                    nums = answer[1:].split('_')
                    if len(nums) == 1:
                        nums.append(0)

                    nums[0] = int(nums[0])
                    nums[1] = int(nums[1])

                    assert nums[0] < self.game.battlefield.size()
                    card = self.game.battlefield.elements[nums[0]]

                    assert nums[1] <= len(card.activated_abilities)
                    
                    # ability activation
                    if card._activated_abilities_costs_validation[nums[1]](card):
                        play = Play(lambda: card.activate_ability(nums[1]))


                elif answer == 'debug':
                    pdb.set_trace()
                    # self.game.print_game_state()
                    answer = input("What would you like to do?\n")

                #elif
                else:
                    raise BadFormatException()

            except BadFormatException:
                print(sys.exc_info())
                answer = input("Bad format.\nWhat would you like to do?\n")
                continue

        return play






    def draw(self, num=1):
        for i in range(num):
            try:
                card = self.library.pop()
                card.zone = ZoneType.HAND
                self.hand.add(card)
            except IndexError:
                raise EmptyLibraryException()

    def discard(self, num=1):
        if num > self.hand.size():
            return False
        for i in range(num):
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



    def print_player_state(self):
        print("\nPLAYER {}\nlife: {}\n".format(self.name, self.life))

        print("mana: {}\n".format(self.mana))

        print("\n\n\n")
        print("hand:\n")
        print(self.hand)

        print("\n\n\n")
        print("library:\n")
        print(self.library)

        print("\n\n\n")
        print("graveyard:\n")
        print(self.graveyard)

        print("\n\n\n")
        print("exile:\n")
        print(self.exile)