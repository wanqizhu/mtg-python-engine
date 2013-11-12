class Game(object):
    """Represents the visible state of a game and all players"""
    def __init__(self, players):
        self.players = players
        self.stack = []

    def priority_order_players(self, active_player):
        """Returns a list of players in priority order, starting with the
        active player"""
        return players[active_player:] + players[:active_player]

    def priority_loop(self, active_player):
        """Give all players priority in order until all players
        pass consecutively"""
        players = self.priority_order_players(active_player)
        action_taken = True
        while action_taken:
            action_taken = False
            for i in range(len(players)):
                player = players[i]
                action = player.choose_action(self)
                while action is not None:
                    stack.append(action)
                    action = player.choose_action(self)
        return action_taken
                    
            
