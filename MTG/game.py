import phase

turn_phases = (phase.beginning,
               phase.main,
               phase.combat,
               phase.main,
               phase.ending)

class Game(object):
    """Represents the visible state of a game and all players"""
    def __init__(self, players):
        self.players = players
        self.active_player_index = 0
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
        return players[index:] + players[:index]

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
                    stack.push(action)
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

    def turn_loop(self):
        """Loops through each phase for each player's turn until the game has
        ended"""
        while not self.ended():
            for player in self.players:
                for phase in turn_phases:
                    phase.run(self)
