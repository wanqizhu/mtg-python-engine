from MTG.mana import *
from MTG.zone import *
from MTG.play import *
from MTG.gamesteps import *
import re, sys, pdb




class EmptyLibraryException(Exception):
    pass

class BadFormatException(Exception):
    pass


class Player(object):
    def __init__(self, deck, name='player', startingLife=20, maxHandSize=7, game=None):
        self.name = name
        # self.ID = None
        self.life = startingLife
        self.maxHandSize = maxHandSize
        self.landPerTurn = 1
        self.landPlayed = 0
        self.passPriorityUntil = None

        self.library = Library(self, deck)
        for card in self.library.elements:
            card.controller = self
            card.owner = self

        self.battlefield = Battlefield(self)
        self.hand = Hand(self)
        self.graveyard = Graveyard(self)
        self.exile = Exile(self)
        self.mana = ManaPool(self)
        self.game = game

    def __repr__(self):
        return self.name


    ## TODO
    def get_action(self):
        """ asks the player to do something

        this gets called whenever a player has priority
        """
        answer = 'placeholder'
        play = None

        while answer and play is None:
            answer = input("What would you like to do? {}, {}\n".format(self.name, self.game.step))
            if answer == '':
                break
            try:
                if answer == 'print':
                    self.game.print_game_state() 

                elif answer == 'hand':
                    print(self.hand)

                elif answer == 'battlefield':
                    print(self.battlefield)

                elif answer == 'debug':
                    pdb.set_trace()


                elif answer[0] == 'p':  # playing card from hand -- 'p3' == plays third card in hand
                    num = int(answer[1:])
                    assert num < self.hand.size()
                    card = self.hand.pop(num)
                    ## pay mana costs
                    can_pay = self.mana.canPay(card.manacost())  # False, or a dict of mana costs
                    ## choose targets
                    can_target = True

                    # timing & restrictions
                    can_play = True
                    if card.is_land() and self.landPlayed >= self.landPerTurn:
                        can_play = False
                    if not (card.is_instant() or card.has_ability('Flash')) and (self.game.stack or self.game.step.phase not in [Phase.PRECOMBAT_MAIN, Phase.POSTCOMBAT_MAIN] or self.game.current_player != self):
                        can_play = False

                    if can_pay and can_target and can_play:
                        self.mana.pay(can_pay)
                        # apply targets

                        play = Play(card.play_func)
                        # special actions
                        if card.is_land():
                            play.is_special_action = True
                            self.landPlayed += 1
                    else:
                        self.hand.add(card)  # illegal casting, revert
                        if not can_pay:
                            print("Cannot pay mana costs\n")
                        if not can_target:
                            print("Cannot target\n")
                        if not can_play:
                            print("Cannot play this right now\n")



                # activate ability from battlefield -- 'a3_1' plays 2nd (index starts at 0) ability from 3rd permanent
                elif answer[0] == 'a':
                    nums = answer[1:].split('_')
                    if len(nums) == 1:
                        nums.append(0)

                    nums[0] = int(nums[0])
                    nums[1] = int(nums[1])

                    assert nums[0] < self.battlefield.size()
                    card = self.battlefield.elements[nums[0]]

                    assert nums[1] <= len(card.activated_abilities)
                    
                    # ability activation
                    if card._activated_abilities_costs_validation[nums[1]](card):
                        play = Play(lambda: card.activate_ability(nums[1]))
                        if card.activated_abilities[nums[1]][2]:  # special action
                            play.is_mana_ability = True

                # skip priority until something happens / certain step
                elif answer[0] == 's':
                    assert answer[1:].upper() in Step._member_names_
                    self.passPriorityUntil = Step[answer[1:].upper()]
                    break

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

    def take_damage(self, damage):
        # trigger
        self.life -= damage



    def print_player_state(self):
        print("\nPLAYER {}\nlife: {}\n".format(self.name, self.life))

        print("mana: {}\n".format(self.mana))

        print("\n\n\n")
        print("battlefield: {}\n".format(self.battlefield.size()))
        print(self.battlefield)

        print("\n\n\n")
        print("hand: {}\n".format(self.hand.size()))
        print(self.hand)

        print("\n\n\n")
        print("library: {}\n".format(self.library.size()))
        print(self.library)

        print("\n\n\n")
        print("graveyard: {}\n".format(self.graveyard.size()))
        print(self.graveyard)

        print("\n\n\n")
        print("exile: {}\n".format(self.exile.size()))
        print(self.exile)