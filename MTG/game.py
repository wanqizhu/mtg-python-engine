from enum import Enum

__author__ = 'Michael'

from MTG.player import Player
from MTG.zone import *


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
    players = ()
    priority = 0
    pending_steps = []
    step = None
    pending_turns = []
    current_player = None

    def __init__(self, player_interfaces):
        self.battlefield = Battlefield()
        self.stack = Stack()
        self.players = tuple(Player(interface) for interface in player_interfaces)

    def get_zone(self, zone_type, owner):
        return {
            ZoneType.LIBRARY: owner.library,
            ZoneType.HAND: owner.hand,
            ZoneType.BATTLEFIELD: self.battlefield,
            ZoneType.GRAVEYARD: owner.graveyard,
            ZoneType.STACK: self.stack,
            ZoneType.EXILE: owner.exile,
            ZoneType.COMMAND: owner.command
        }[zone_type]

    def apply_state_based_actions(self):
        print("Applying state based actions")
        pass

    def apply_play(self, play):
        pass

    def apply_stack_item(self, stack_item):
        pass

    def handle_priority(self, step):
        while self.passed_priority < len(self.players) or self.stack:
            self.apply_state_based_actions()
            play = self.players[self.priority].get_action(self.stack, step)
            if play is None:
                self.passed_priority += 1
                self.priority = (self.priority + 1) % len(self.players)
                if self.passed_priority == len(self.players) and self.stack:
                    self.apply_stack_item(self.stack.pop())
                continue
            else:
                self.passed_priority = 0
            if play.is_mana_ability() or play.is_special_action():
                self.apply_play(play)
            else:
                self.stack.add(play)

    def handle_main_phase(self, step):
        self.handle_priority(step)

    def handle_turn(self):
        for phase in Phase:
            self.pending_steps.extend(phase.steps)

        while self.pending_steps:
            self.step = self.pending_steps.pop(0)
            {
                Step.UNTAP: lambda step: None,
                Step.UPKEEP: lambda step: None,
                Step.DRAW: lambda step: None,
                Step.PRECOMBAT_MAIN: self.handle_main_phase,
                Step.BEGINNING_OF_COMBAT: lambda step: None,
                Step.DECLARE_ATTACKERS: lambda step: None,
                Step.DECLARE_BLOCKERS: lambda step: None,
                Step.FIRST_STRIKE_COMBAT_DAMAGE: lambda step: None,
                Step.COMBAT_DAMAGE: lambda step: None,
                Step.END_OF_COMBAT: lambda step: None,
                Step.POSTCOMBAT_MAIN: self.handle_main_phase,
                Step.END: lambda step: None,
                Step.CLEANUP: lambda step: None
            }[self.step](self.step)
        self.pending_turns.append(self.current_player)

    def set_up_game(self):
        pass

    def run_game(self):
        self.set_up_game()
        while not all(player.won or player.lost for player in self.players):
            self.pending_turns.extend(self.players)
            try:
                self.handle_turn()
            except GameOverException:
                break