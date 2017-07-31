from enum import Enum

from MTG.player import Player
from MTG.zone import *
from MTG.cards import *

global GAME

class Phase(Enum):
    BEGINNING = 0
    PRECOMBAT_MAIN = 1
    COMBAT = 2
    POSTCOMBAT_MAIN = 3
    ENDING = 4

    @property
    def steps(self):
        return {
            Phase.BEGINNING: (Step.UNTAP, Step.UPKEEP, Step.DRAW),
            Phase.PRECOMBAT_MAIN: (Step.PRECOMBAT_MAIN,),
            Phase.COMBAT: (
                Step.BEGINNING_OF_COMBAT,
                Step.DECLARE_ATTACKERS,
                Step.DECLARE_BLOCKERS,
                Step.FIRST_STRIKE_COMBAT_DAMAGE,
                Step.COMBAT_DAMAGE,
                Step.END_OF_COMBAT
            ),
            Phase.POSTCOMBAT_MAIN: (Step.POSTCOMBAT_MAIN,),
            Phase.ENDING: (Step.END, Step.CLEANUP)
        }[self]


class Step(Enum):
    UNTAP = 0
    UPKEEP = 1
    DRAW = 2
    PRECOMBAT_MAIN = 3
    BEGINNING_OF_COMBAT = 4
    DECLARE_ATTACKERS = 5
    DECLARE_BLOCKERS = 6
    FIRST_STRIKE_COMBAT_DAMAGE = 7
    COMBAT_DAMAGE = 8
    END_OF_COMBAT = 9
    POSTCOMBAT_MAIN = 10
    END = 11
    CLEANUP = 12

    @property
    def phase(self):
        return {
            Step.UNTAP: Phase.BEGINNING,
            Step.UPKEEP: Phase.BEGINNING,
            Step.DRAW: Phase.BEGINNING,
            Step.PRECOMBAT_MAIN: Phase.PRECOMBAT_MAIN,
            Step.BEGINNING_OF_COMBAT: Phase.COMBAT,
            Step.DECLARE_ATTACKERS: Phase.COMBAT,
            Step.DECLARE_BLOCKERS: Phase.COMBAT,
            Step.FIRST_STRIKE_COMBAT_DAMAGE: Phase.COMBAT,
            Step.COMBAT_DAMAGE: Phase.COMBAT,
            Step.END_OF_COMBAT: Phase.COMBAT,
            Step.POSTCOMBAT_MAIN: Phase.POSTCOMBAT_MAIN,
            Step.END: Phase.ENDING,
            Step.CLEANUP: Phase.ENDING
        }[self]

class GameOverException(Exception):
    """Indicates that the game is over: that every player has either won, lost, or conceded"""
    pass

class Game(object):
    """A game object. This represents the entire state of an in-progress MTG game."""
    passed_priority = 0
    players = []
    priority = 0
    pending_steps = []
    step = None
    pending_turns = []
    current_player = None

    # start a game by giving each player their deck
    def __init__(self, decks):
        self.battlefield = Battlefield()
        self.stack = Stack()
        self.players = [Player(decks[i], 'player'+str(i), game=self) for i in range(len(decks))]

    def get_zone(self, zone_type, owner=None):
        return {
            ZoneType.LIBRARY: owner.library,
            ZoneType.HAND: owner.hand,
            ZoneType.BATTLEFIELD: self.battlefield,
            ZoneType.GRAVEYARD: owner.graveyard,
            ZoneType.STACK: self.stack,
            ZoneType.EXILE: owner.exile,
            # ZoneType.COMMAND: owner.command
        }[zone_type]

    ## TODO
    def apply_state_based_actions(self):
        print("Applying state based actions")
        pass

    ## TODO
    def apply_stack_item(self, stack_item):
        """ resolving a spell/effect from stack"""
        pass

    def handle_priority(self, step):
        while self.passed_priority < len(self.players) or self.stack:  # while not everyone has passed priority
            self.apply_state_based_actions()
            play = self.players[self.priority].get_action()
            if play is None:  # passes priority
                self.passed_priority += 1
                self.priority = (self.priority + 1) % len(self.players)  # who's next to get priority
                if self.passed_priority == len(self.players) and self.stack:  # resolve top stack item
                    self.apply_stack_item(self.stack.pop())
                continue
            else:  # responds with something; must have everyone re-pass priority
                self.passed_priority = 0

            if play.is_mana_ability or play.is_special_action:  # applies instantly
                self.play.apply()
            else:
                self.stack.add(play)  # add to stack



    def handle_beginning_phase(self, step):
        if step is Step.UNTAP:
            for permanent in self.battlefield:
                permanent.untap()

        elif step is Step.UPKEEP:
            self.handle_priority(step)
            pass

        elif step is Step.DRAW:
            self.current_player.draw()

        
    ## TODO
    def handle_main_phase(self, step):
        self.handle_priority(step)
        pass

    ## TODO
    def handle_combat_phase(self, step):
        if step is Step.BEGINNING_OF_COMBAT:
            for permanent in self.battlefield:
                permanent.trigger(triggerConditions.onEnterCombat)
        elif step is Step.DECLARE_ATTACKERS:
            for permanent in self.battlefield:
                permanent.trigger(triggerConditions.onDeclareAttackers)
        elif step is Step.DECLARE_BLOCKERS:
            for permanent in self.battlefield:
                permanent.trigger(triggerConditions.onDeclareBlockers)
        elif step is Step.END_OF_COMBAT:
            for permanent in self.battlefield:
                permanent.trigger(triggerConditions.onEndofCombat)

        if step is Step.DECLARE_ATTACKERS:
            pass
            # declare attackers

        if step is Step.DECLARE_BLOCKERS:
            pass
            # declare blockers

            # resolve damage


        self.handle_priority(step)
        pass



    def handle_end_phase(self, step):
        if step is Step.END:
            self.handle_priority(step)
            pass

        elif step is Step.CLEANUP:
            self.current_player.discard(self.current_player.hand.size() - self.current_player.maxHandSize)



    def handle_turn(self):
        for phase in Phase:
            self.pending_steps.extend(phase.steps)

        while self.pending_steps:
            self.step = self.pending_steps.pop(0)
            {
                Step.UNTAP: lambda step: handle_beginning_phase,
                Step.UPKEEP: lambda step: handle_beginning_phase,
                Step.DRAW: lambda step: handle_beginning_phase,
                Step.PRECOMBAT_MAIN: self.handle_main_phase,
                Step.BEGINNING_OF_COMBAT: lambda step: handle_combat_phase,
                Step.DECLARE_ATTACKERS: lambda step: handle_combat_phase,
                Step.DECLARE_BLOCKERS: lambda step: handle_combat_phase,
                Step.FIRST_STRIKE_COMBAT_DAMAGE: lambda step: handle_combat_phase,
                Step.COMBAT_DAMAGE: lambda step: handle_combat_phase,
                Step.END_OF_COMBAT: lambda step: handle_combat_phase,
                Step.POSTCOMBAT_MAIN: self.handle_main_phase,
                Step.END: lambda step: handle_end_phase,
                Step.CLEANUP: lambda step: handle_end_phase
            }[self.step](self.step)
        self.pending_turns.append(self.current_player)



    ### debug

    ## TODO
    # print each player's states
    # print debug variables
    def print_game_state(self):
        print("\n\n\n")
        print("battlefield:\n")
        print(self.battlefield)

        print("\n\n\n")
        print("stack:\n")
        print(self.stack)

        # for player in players:
        #     player.print_player_state()




## TODO
    def set_up_game(self):
        print("setting up game...")
        pass


    def run_game(self):
        self.set_up_game()
        while len(self.players):
            self.pending_turns.extend(self.players)  # everyone gets a turn queued up, in order
            try:
                self.handle_turn()
            except GameOverException:
                break




def read_deck(filename):
    """ File format:
    NUM CARDNAME

    e.g.
    10 Plains
    10 Oreskos Swiftclaw

    """
    file = open(filename, 'r').read().split("\n")
    deck = []
    for line in file:
        try:
            i = line.index(" ")
            num = int(line[:i])
            for j in range(num):  # add NUM copies of CARDNAME
                card = card_from_name(line[i+1:])
                if card:
                    deck.append(card)
                    print(deck[-1].name())
                else:
                    print("card {} does not exist\n".format(line[i+1:]))
        except:
            raise DecklistFormatError()

    return deck


decks = [read_deck('cards/decks/deck1.txt'), read_deck('cards/decks/deck1.txt')]
GAME = Game(decks)
print(GAME.__dict__)
# GAME.run_game()