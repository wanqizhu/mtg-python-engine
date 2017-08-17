import re, sys, pdb, traceback

from MTG import mana
from MTG import zone
from MTG import play
from MTG import gamesteps
from MTG import cards




class Player(object):
    def __init__(self, deck, name='player', startingLife=20, maxHandSize=7, game=None):
        self.name = name
        # self.ID = None
        self.life = startingLife
        self.maxHandSize = maxHandSize
        self.landPerTurn = 1
        self.landPlayed = 0
        self.passPriorityUntil = None

        self.library = zone.Library(self, deck)
        for card in self.library.elements:
            card.controller = self
            card.owner = self

        self.battlefield = zone.Battlefield(self)
        self.hand = zone.Hand(self)
        self.graveyard = zone.Graveyard(self)
        self.exile = zone.Exile(self)
        self.mana = mana.ManaPool(self)
        self.game = game
        self.lost = False
        self.won = False

    def __repr__(self):
        return self.name


    def get_action(self):
        """ asks the player to do something

        this gets called whenever a player has priority
        """
        answer = 'placeholder'
        _play = None

        while answer and _play is None:
            answer = self.make_choice("What would you like to do? {}, {}\n".format(self.name, self.game.step))
            
            if self.game.test:
                print("\t" + self.name + ", " + str(self.game.step) + ": " + answer + "\n")

            if answer == '':
                break

            

            try:
                if answer == 'print':
                    self.game.print_game_state() 

                elif answer == 'hand':
                    print(self.hand)

                elif answer == 'battlefield':
                    print(self.battlefield)

                elif answer == 'graveyard':
                    print(self.graveyard)

                elif answer == 'exile':
                    print(self.exile)

                elif answer == 'debug':
                    pdb.set_trace()


                elif answer[0] == 'p':  # playing card from hand
                    try:
                        num = int(answer[2:])   # 'p 3' == plays third card in hand
                        assert num < self.hand.size()
                        card = self.hand.pop(num)
                    except:
                        name = answer[2:]  # 'p Island' == plays 'Island'
                        card = self.hand.get_card_by_name(name)
                        assert card
                        


                    ## pay mana costs
                    can_pay = self.mana.canPay(card.manacost())  # False, or a dict of mana costs
                    ## choose targets
                    can_target = True

                    # timing & restrictions
                    can_play = True
                    if card.is_land() and self.landPlayed >= self.landPerTurn:
                        can_play = False
                        
                    if not (card.is_instant() or card.has_ability('Flash')) and (
                                self.game.stack 
                                or self.game.step.phase not in [
                                    gamesteps.Phase.PRECOMBAT_MAIN, 
                                    gamesteps.Phase.POSTCOMBAT_MAIN]
                                or self.game.current_player != self):
                        can_play = False

                    if can_pay and can_target and can_play:
                        self.mana.pay(can_pay)
                        # apply targets

                        _play = play.Play(card.play_func)
                        # special actions
                        if card.is_land():
                            _play.is_special_action = True
                            self.landPlayed += 1
                    else:
                        self.hand.add(card)  # illegal casting, revert
                        if not can_pay:
                            print("Cannot pay mana costs\n")
                        if not can_target:
                            print("Cannot target\n")
                        if not can_play:
                            print("Cannot play this right now\n")



                # activate ability from battlefield -- 'a 3_1' plays 2nd (index starts at 0) ability from 3rd permanent
                # 'a 3' playrs 1st (default) ability of the 3rd permanent
                elif answer[:2] == 'a ':
                    nums = answer[2:].split('_')
                    if len(nums) == 1:
                        nums.append(0)

                    nums[0] = int(nums[0])
                    nums[1] = int(nums[1])

                    assert nums[0] < self.battlefield.size()
                    card = self.battlefield.elements[nums[0]]

                    assert nums[1] <= len(card.activated_abilities)
                    
                    # ability activation
                    if card._activated_abilities_costs_validation[nums[1]](card):
                        _play = play.Play(lambda: card.activate_ability(nums[1]))
                        if card.activated_abilities[nums[1]][2]:  # special action
                            _play.is_mana_ability = True

                # skip priority until something happens / certain step
                elif answer[:2] == 's ':
                    if answer[2:] == 'main':
                        answer = 's precombat_main'   
                    assert answer[2:].upper() in gamesteps.Step._member_names_
                    self.passPriorityUntil = gamesteps.Step[answer[2:].upper()]
                    break

                elif answer[:2] == '__':  # for dev purposes
                    exec(answer[2:])

                else:
                    raise BadFormatException()

            except Exception as err:
                traceback.print_tb(err.__traceback__)
                # print(sys.exc_info())
                print("Bad format.\n")
                continue

        return _play


    # separate func for unit testing
    def make_choice(self, prompt_string):
        # if not TEST:
        ans = input(prompt_string)
        if ans == 'debug':
            pdb.set_trace()
        return ans
        # else:
        #     ## TODO: unit tests
        #     pass

    def play_card(self, card):
        if type(card) is str:  # convert card name to Card object
            card = cards.card_from_name(card)

        _play = play.Play(card.play_func)
        if _play.is_mana_ability or _play.is_special_action:  # applies instantly
            _play.apply()
        else:
            self.game.stack.add(play)  # add to stack


    def draw(self, num=1):
        for i in range(num):
            try:
                card = self.library.pop()
                card.zone = zone.ZoneType.HAND
                self.hand.add(card)
            except IndexError:
                raise EmptyLibraryException()

    def draw_card(self, card):
        """ draw a specific card

        card is either a string (name of card) or a Card object
        """
        self.hand.add(card)


    def discard(self, num=1):
        if num > self.hand.size():
            return False

        ## TODO: prompt player pick which cards
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

    def take_damage(self, source, damage):
        # trigger
        self.life -= damage


    def lose(self):
        print("{} has lost the game\n".format(self))
        self.lost = True
        pass


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