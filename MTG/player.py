import pdb
import traceback
import random
from copy import deepcopy
from collections import defaultdict

from MTG import mana
from MTG import zone
from MTG import play
from MTG import gamesteps
from MTG import cards
from MTG import triggers
from MTG import token
from MTG.exceptions import *


class Player():
    is_player = True

    def __init__(self, deck, name='player',
                 startingLife=20, maxHandSize=7, game=None):
        self.name = name
        self.game = game
        self.timestamp = -1
        self.life = startingLife
        self.startingLife = startingLife
        self.maxHandSize = maxHandSize
        self.landPerTurn = 1
        self.landPlayed = 0
        self.passPriorityUntil = None
        self.autoPayMana = False
        self.autoOrderTriggers = True
        self.autoDiscard = False

        self.library = zone.Library(self, deck)
        for card in self.library:
            card.controller = self
            card._owner = self

        self.battlefield = zone.Battlefield(self)
        self.hand = zone.Hand(self)
        self.graveyard = zone.Graveyard(self)
        self.exile = zone.Exile(self)
        self.mana = mana.ManaPool(self)
        self.lost = False
        self.won = False

        self.pending_triggers = []

        # todo: also track "YOUR last turn" rather than just last turn
        self.turn_events = defaultdict(lambda: None)
        self.last_turn_events = defaultdict(lambda: None)

        self.static_effects = []

        # tracks which permanents cares about each player-init triggers
        # trigger_listeners[condition] = list of (permanent, tstamp), where permanent cares about condition
        #       and tstamp is stored to check permanent expiration
        self.trigger_listeners = defaultdict(lambda: [])

        # todo: cost modifier tracker

    def __repr__(self):
        return 'player.Player(name=%r)' % self.name

    def __str__(self):
        return self.name

    def __eq__(x, y):
        return isinstance(y, x.__class__) and x.__repr__() == y.__repr__()

    def __hash__(self):
        return hash(self.__repr__())

    @property
    def is_active(self):
        return self == self.game.current_player

    @property
    def opponent(self):
        return self.game.opponent(self)

    @property
    def creatures(self):
        return self.battlefield.filter(filter_func=lambda p: p.is_creature)

    @property
    def lands(self):
        return self.battlefield.filter(filter_func=lambda p: p.is_land)

    def get_action(self):
        """ asks the player to do something

        this gets called whenever a player has priority
        """
        answer = 'placeholder'
        _play = None

        while answer and _play is None:
            answer = self.make_choice(
                "What would you like to do? {}{}, {}\n".format(
                    self.name,
                    '*' if self.is_active else '',
                    self.game.step))

            if self.game.test:
                print("\t" + self.name + ", " +
                      str(self.game.step) + ": " + answer + "\n")

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

                elif answer == 'stack':
                    print(self.game.stack)

                elif answer == 'mana':
                    print(self.mana)

                elif answer == 'addmana':
                    self.mana.add_str('WWWWWUUUUUBBBBBRRRRRGGGGG11111')

                elif answer == 'debug':
                    # pdb.set_trace()
                    pass

                elif answer[0] == 'p':  # playing card from hand
                    try:
                        # 'p 3' == plays third card in hand
                        num = int(answer[2:])
                        assert num < len(self.hand)
                        card = self.hand[num]
                    except:
                        name = answer[2:]  # 'p Island' == plays 'Island'
                        card = self.hand.get_card_by_name(name)
                        assert card


                    # timing & restrictions
                    can_play = True
                    if card.is_land and self.landPlayed >= self.landPerTurn:
                        can_play = False

                    if not (card.is_instant or card.has_ability('Flash')) and (
                            self.game.stack
                            or self.game.step.phase not in [
                                gamesteps.Phase.PRECOMBAT_MAIN,
                                gamesteps.Phase.POSTCOMBAT_MAIN]
                            or not self.is_active):
                        can_play = False

                    # choose targets
                    if can_play:
                        can_target = card.targets()


                    # pay mana costs
                    if can_play and can_target:
                        cost = card.manacost
                        creatures_to_tap = []

                        if card.has_ability("Convoke"):
                            untapped_creatures = [
                                c for c in self.creatures if not c.status.tapped]
                            print("Your creatures: {}".format(untapped_creatures))
                            ans = self.make_choice("What creatures would you like to tap"
                                                   " to pay for %s? (Convoke) " % card)

                            ans = ans.split(" ")
                            for ind in ans:
                                try:
                                    ind = int(ind)
                                    _creature = untapped_creatures[ind]
                                    if not _creature.status.tapped and _creature not in creatures_to_tap:
                                        color = _creature.characteristics.color
                                        if not color:
                                            color = 'C'
                                        elif len(color) > 1:
                                            color = self.make_choice(
                                                "What color would you like to add? {}".format(color))
                                            assert color in mana.manachr
                                        else:
                                            color = color[0]

                                        color = mana.chr_to_mana(color)
                                        creatures_to_tap.append(_creature)
                                        if cost[color]:
                                            cost[color] -= 1
                                        else:
                                            if cost[mana.Mana.GENERIC]:
                                                cost[mana.Mana.GENERIC] -= 1
                                            else:
                                                raise ValueError

                                except (IndexError, ValueError):
                                    print("error processing creature for convoke")
                                    pass

                        can_pay = self.mana.canPay(cost) 

                    if can_pay and can_target and can_play:
                        self.hand.remove(card)
                        self.mana.pay(can_pay)
                        for _creature in creatures_to_tap:
                            _creature.tap()

                        print("{} playing {} targeting {}\n".format(self, card, card.targets_chosen))
                        _play = play.Play(card.play_func,
                                          card=card)
                        # special actions
                        if card.is_land:
                            _play.is_special_action = True
                            self.landPlayed += 1
                    else:
                        # illegal casting, revert
                        if not can_pay:
                            print("Cannot pay mana costs\n")
                        elif not can_target:
                            print("Cannot target\n")
                        elif not can_play:
                            print("Cannot play this right now\n")

                # activate ability from battlefield -- 'a 3_1' plays 2nd (index starts at 0) ability from 3rd permanent
                # 'a 3' playrs 1st (default) ability of the 3rd permanent
                elif answer[:2] == 'a ':
                    nums = answer[2:].split('_')
                    if len(nums) == 1:
                        nums.append(0)

                    nums[0] = int(nums[0])
                    nums[1] = int(nums[1])

                    assert nums[0] < len(self.battlefield)
                    card = self.battlefield[nums[0]]

                    assert nums[1] <= len(card.activated_abilities)

                    # ability activation

                    # if card._activated_abilities_costs_validation[nums[1]](card):
                    # TODO: target validation
                    PLAYER_PREVIOUS_STATE = deepcopy(self)
                    # if card._activated_abilities_costs[nums[1]](card):
                    if card.activated_abilities[nums[1]].can_activate():
                        # TODO: make each ability have its own description/name for printing
                        _play = card.activate_ability(nums[1])
                    else:
                        raise ResetGameException

                # skip priority until something happens / certain step
                elif answer[:2] == 's ':
                    if answer[2:] == 'main':
                        answer = 's precombat_main'
                    if answer[2:] == 'main2':
                        answer = 's postcombat_main'
                    if answer[2:] == 'combat':
                        answer = 's beginning_of_combat'
                    assert answer[2:].upper() in gamesteps.Step._member_names_
                    self.passPriorityUntil = gamesteps.Step[answer[2:].upper()]
                    break

                elif answer[:2] == '__':  # for dev purposes
                    exec(answer[2:])
                    return '__continue'

                else:
                    raise BadFormatException()

            except ResetGameException:
                print("Illegial action. Resetting...")
                self = PLAYER_PREVIOUS_STATE
                pass

            except:
                traceback.print_exc()
                print("Bad format.\n")
                continue

        return _play

    # separate func for unit testing
    def make_choice(self, prompt_string):
        # if not TEST:
        ans = input(prompt_string)
        if ans == 'debug':
            pdb.set_trace()

        if not self.game or self.game.test:  # for debug
            print(prompt_string[:-1])  # remove ending \n
            print(ans)
        return ans
        # else:
        #     ## TODO: unit tests
        #     pass

    def make_choice_items_in_list(self, items, num=1, up_to=False, repetition=False):
        print(items)
        l = len(items)

        if num == -1:  # any number
            num = l
            up_to = True

        while True:
            chosen = []
            try:
                ans = input("Choose %d items:\n" % num)
                if not ans:
                    break
                ans = ans.split(" ")
                if not up_to:
                    assert len(ans) == num
                else:
                    assert len(ans) <= num

                for i in ans:
                    i = int(i)
                    assert i < l
                    if not repetition:
                        assert items[i] not in chosen

                    chosen.append(items[i])

                break

            except (AssertionError, ValueError):
                print("Bad input")
                pass

        return chosen


    def add_static_effect(self, name, value, source, toggle_func, exempt_source=False):
        """ toggle_func: condition func on which permanents the static effect affects -- lambda eff: True

        e.g. lambda eff: eff.source.is_creature applies to all creatures

        exempt_source: True if the effect only applies to 'other permanents'
        """
        self.static_effects.append((name, value, source, toggle_func))
        for p in self.battlefield:
            p.add_effect(name, value, source=source, is_active=False, toggle_func=toggle_func)

        if not exempt_source:  # when this func is called during permanent.__init__(),
                               # the card isn't on the battlefield yet. 
            source.add_effect(name, value, source=source, is_active=False, toggle_func=toggle_func)

    def remove_static_effect(self, source):
        """ remove all effects from a certain source """
        self.static_effects = [eff for eff in self.static_effects if eff[2] != source]
        # each permanent should auto-remove since source's timestamp has changed


    def trigger(self, condition, source=None, amount=1):
        """Pass player-init triggers to relevant permanents

        e.g. onControllerLifeGain
        """
        if isinstance(condition, str):
            condition = triggers.triggerConditions[condition]

        if condition == triggers.triggerConditions.onUpkeep:
            def f(p):
                p.status.summoning_sick = False
            self.apply_to_battlefield(f)

        elif condition == triggers.triggerConditions.onCleanup:
            def f(p):
                p.status.damage_taken = 0
            self.apply_to_battlefield(f)


        if condition in self.trigger_listeners:
            # make copy so we can remove while iterating
            for p, tstamp in self.trigger_listeners[condition][:]:
                if p.timestamp == tstamp:
                    p.trigger(condition, source, amount)
                else:  # expired
                    print("player-based trigger {} expired".format((p, tstamp)))
                    self.trigger_listeners[condition].remove((p, tstamp))


    def play_card(self, card):
        if isinstance(card, str):  # convert card name to Card object
            card = cards.card_from_name(card)

        _play = play.Play(card.play_func)
        if _play.is_mana_ability or _play.is_special_action:  # applies instantly
            _play.apply()
        else:
            self.game.stack.add(play)  # add to stack

    def draw(self, num=1):
        self.trigger('onControllerDrawCard')
        self.game.trigger('onDrawCard')
        for i in range(num):
            try:
                card = self.library.pop()
                self.hand.add(card)
            except IndexError:
                raise EmptyLibraryException()

    def draw_card(self, card):
        """ draw a specific card

        card is either a string (name of card) or a Card object
        """
        self.hand.add(card)

    def search_lib(self, criteria_funcs, num=1, target_zone='hand', todo_func=None, face_up=True):
        """ criteria_funcs validates the searched set

        If num=1 (searching one card), then that's just the validating function

        If num > 1 and criteria_funcs is a single function, then we're searching
            multiple cards under the same condition (e.g. get 2 lands)

        Else, criteria_funcs is a list
            0: overall validating function lambda items: True if items as a whole is valid
            1..n: individual functions that validate card #1..n being searched

        So if we want to search 2 creatures with total power < 4, we'd have

        [
            lambda creatures: sum(p.power) < 4,
            lambda c: c.is_creature,
            lambda c: c.is_creature
        ]
        """

        if target_zone == 'hand':
            target_zone = self.hand

        if num == 1 or type(criteria_funcs) != list:
            cards = list(self.library.filter(filter_func=criteria_funcs))
            chosen = self.make_choice_items_in_list(cards, num)

            if target_zone:
                for c in chosen:
                    c.change_zone(target_zone)

            if todo_func:
                if len(chosen) == 1:
                    todo_func(chosen[0])
                else:
                    todo_func(chosen)

            self.library.shuffle()

            if face_up:
                print(chosen)
            return chosen

        else:
            pass

    def discard(self, num=1, down_to=None, rand=False):
        """Discarding from hand; prompts user for card choices

        If down_to is specified, number is ignored and set to len(self.hand) - down_to
        """

        self.trigger('onControllerDiscard')
        self.trigger('onPlayerDiscard')

        if num == -1:
            num = len(self.hand)  # -1 to discard whole hand
        if down_to:
            # discard down_to e.g. 3 cards left in hand
            num = len(self.hand) - down_to
        if num > len(self.hand):
            return False
        if num <= 0:
            return True

        if num == len(self.hand):
            cards_to_discard = self.hand[:]

        elif rand or self.autoDiscard:
            print("randomly discarding %i...\n" % num)
            cards_to_discard = random.sample(self.hand.elements, num)

        else:
            # prompt player pick which cards
            answer = self.make_choice(
                "%r\nWhich cards would you like to discard? (discarding %i) \n" % (self.hand, num))
            cards_to_discard = []

            if not answer:  # '' to auto discard
                print("Auto discarding\n")
            else:
                answer = answer.split(" ")
                try:
                    for ind in answer:
                        ind = int(ind)
                        if ind < len(self.hand):
                            cards_to_discard.append(self.hand[ind])
                        else:
                            print("Card #{} is out of bounds\n".format(ind))
                            continue
                except:
                    traceback.print_exc()
                    print("Error processing discard")

            cards_left = num - len(cards_to_discard)
            if cards_left > 0:
                cards_to_discard.extend(self.hand[-cards_left:])

        self.hand.remove(cards_to_discard)
        return self.graveyard.add(cards_to_discard)

    def mill(self, num=1):
        for i in range(min(num, len(self.library))):
            self.graveyard.add(self.library.pop())
        return True

    def create_token(self, attributes, num=1, keyword_abilities=[], activated_abilities=[]):
        token.create_token(attributes, self, num, keyword_abilities, activated_abilities)

    def investigate(self, num=1):
        self.create_token('colorless Clue artifact', num, [], [['2, T, Sacrifice ~', 'self.controller.draw()']])

    def boolster(self, num=1):
        creatures = [(p, p.toughness) for p in self.battlefield if p.is_creature]
        if not creatures:
            return None
        min_toughness = min(creatures, key=lambda i: i[1])
        creatures = [p[0] for p in creatures if p[1] == min_toughness]

        print("Bolster targets avaliable: {}".format(creatures))

        if len(creatures) == 1:
            target = creatures[0]
        else:
            while True:
                ans = self.make_choice("Which creature would you like to bolster?")
                try:
                    ans = int(ans)
                    if ans >= len(creatures):
                        raise ValueError
                    target = creatures[ans]
                    break
                except ValueError:
                    print("wrong format")
                    continue

        print("Bolstering {}".format(target))
        target.add_counter("+1/+1", num)



    def sacrifice(self, num=1, filter_func=lambda p: p.is_creature):
        if num <= 0:
            return True

        avaliable_targets = self.battlefield.filter(filter_func=filter_func)
        if not avaliable_targets or len(avaliable_targets) > num:
            return False

        ans = self.make_choice("Avaliable permanents: %s\nWhat would you like to sacrifice? (need %d)"
                               % (avaliable_targets, num))

        if not ans:
            return False

        sacs = []

        # fetch the chosen indices
        ans = ans.split(" ")
        for ind in ans:
            try:
                ind = int(ind)
                if avaliable_targets[ind] not in sacs:
                    sacs.append(avaliable_targets[ind])

            except ValueError:
                continue

        if len(avaliable_targets) < num:
            print("auto saccing...")
            for p in avaliable_targets:
                if p not in sacs:
                    sacs.append(p)
                if len(avaliable_targets) == num:
                    break

        for p in sacs:
            p.sacrifice()

        return sacs


    # TODO: handle paying X life / X mana
    def pay(self, mana=None, life=0):
        """
        mana: a dict of Mana(Enum)
        """

        # verify we have enough resources
        if self.life - life <= 0:
            return False

        payment = self.mana.canPay(mana)
        if not payment:
            return False

        self.mana.pay(payment)
        self.lose_life(life)
        return True

    def take_damage(self, source, dmg, is_combat=False):
        # trigger
        print("{} takes {} damage from {}\n".format(self, dmg, source))
        self.life -= dmg

    def gain_life(self, amount):
        self.trigger(triggers.triggerConditions.onControllerLifeGain, amount=amount)
        self.game.trigger(triggers.triggerConditions.onLifeGain, amount=amount)

        if self.turn_events['life gain']:
            self.turn_events['life gain'] += amount
        else:
            self.turn_events['life gain'] = amount
        print("%r: gaining %i life\n" % (self, amount))
        self.life += amount

    def lose_life(self, amount):
        self.trigger('onLifeLoss', amount=amount)
        self.game.trigger('onControllerLifeLoss', amount=amount)

        if self.turn_events['life loss']:
            self.turn_events['life loss'] += amount
        else:
            self.turn_events['life loss'] = amount

        self.life -= amount

    def set_life_total(self, value):
        if self.life < value:
            self.gain_life(value - self.life)
        elif self.life > value:
            self.lose_life(self.life - value)

    def end_turn(self):
        self.last_turn_events = self.turn_events
        self.turn_events = defaultdict(lambda: None)

    def controls(self, subtype=None, types=None, supertype=None):
        """ shortcut for checking whether a player controls something (e.g. Island, Goblin) """
        filt = set()
        if subtype:
            f = self.battlefield.filter(
                       filter_func=lambda p: subtype in p.characteristics.subtype)
            if not filt:
                filt = f
            else:
                filt &= f

        if types:
            f = self.battlefield.filter(
                       filter_func=lambda p: types in p.characteristics.types)
            if not filt:
                filt = f
            else:
                filt &= f

        if supertype:
            f = self.battlefield.filter(
                       filter_func=lambda p: supertype in p.characteristics.supertype)
            if not filt:
                filt = f
            else:
                filt &= f

        return filt


    def apply_to_battlefield(self, apply_func, condition=lambda p: True):
        """Apply some function to permanents on the battlefield

        - filter out by a condition function if necessary
        - defaults to all permanents

        return True if at least one object satisfied the condition
        """

        did_something = False

      # use [:] to iterate over a copy of the list in case items get changed
        for perm in self.battlefield[:]:
            if condition(perm):
                apply_func(perm)
                did_something = True

        return did_something

    def lose(self):
        print("{} has lost the game\n".format(self))
        self.lost = True


    def print_player_state(self):
        print("\nPLAYER {}\nlife: {}\n".format(self.name, self.life))

        print("mana: {}\n".format(self.mana))

        print("\n\n\n")
        print("battlefield: {}\n".format(len(self.battlefield)))
        print(self.battlefield)

        print("\n\n\n")
        print("hand: {}\n".format(len(self.hand)))
        print(self.hand)

        print("\n\n\n")
        print("library: {}\n".format(len(self.library)))
        print(self.library)

        print("\n\n\n")
        print("graveyard: {}\n".format(len(self.graveyard)))
        print(self.graveyard)

        print("\n\n\n")
        print("exile: {}\n".format(len(self.exile)))
        print(self.exile)
