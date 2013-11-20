import random

from MTG import phase

turn_phases = (phase.beginning,
               phase.main,
               phase.combat,
               phase.main,
               phase.ending)

class Game(object):
    """Represents the visible state of a game and all players"""
    def __init__(self, players):
        self.players = players
        self.stack = []

    def get_active_player(self):
        """Returns the current active player"""
        return self.players[self.active_player_index]

    def get_opponents(self, player):
        """Returns a list of all opponents of a given player"""
        return [opp for opp in self.players if opp!=player]

    def priority_order_players(self):
        """Returns a list of players in priority order, starting with the
        active player"""
        index = self.active_player_index
        return self.players[index:] + self.players[:index]

    def priority_loop(self, is_main=False):
        """Give all players priority in order until all players
        pass consecutively"""
        players = self.priority_order_players()
        action_taken = True
        while action_taken:
            action_taken = False
            for i in range(len(players)):
                player = players[i]
                action = player.choose_action(self)
                while action is not None:
                    self.stack.push(action)
                    action = player.choose_action(self)
        return action_taken

    def resolve_stack(self, is_main=False):
        """Resolve each item on the stack, giving players priority after each
        resolution"""
        while self.stack:
            self.stack.pop().resolve()
            self.priority_loop(is_main)

    def gain_priority(self, is_main=False):
        """Grant the active player priority, then priority_loop and resolve the
        stack until all players pass priority sequentially when the stack is
        empty"""
        while self.priority_loop():
            self.resolve_stack()

    def play(self):
        """Play through the game until it has ended"""
        for player in self.players:
            player.shuffle_library()
        self.active_player_index = random.choice(range(len(self.players)))
        players = priority_order_players()
        taking_mulligan = [p for p in players if p.choose_mulligan()]
        while taking_mulligan:
            for player in taking_mulligan:
                player.mulligan()
            taking_mulligan = [p for p in players if p.choose_mulligan()]
        # TODO: Add opening hand actions
        while not self.ended():
            for phase in turn_phases:
                phase.run(self)
            self.active_player_index = (self.active_player_index + 1) % len(self.players)
