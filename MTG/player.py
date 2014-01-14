import random

from .card_type import CardType
from .mana import ManaPool

class Player(object):
    """Represents a player in a game"""
    def __init__(self, deck, name="Player"):
        self.library = deck
        self.hand = []
        self.graveyard = []
        self.permanaents = []
        self.life = 20
        self.name = name
        self.mana_pool = ManaPool()
    
    def __str__(self):
        return name
    
    def draw(self):
        """Draw a card from the library to the hand"""
        self.hand.append(self.library.pop())
    
    def discard(self, index):
        """Discard the chosen card"""
        self.graveyard.append(self.hand[index])
        self.hand = self.hand[:index] + self.hand[index+1:]

    def shuffle_library(self):
        """Shuffle the library"""
        random.shuffle(self.library)

    def draw_starting_hand(self):
        for i in range(7):
            self.draw()
            
    def play_card(self, hand_index):
        card = self.hand[hand_index]
        action = card.play(self)
        if action is not None:
            if action.is_stack_action():
                return action
            else:
                action.resolve()
                
    def zero_lands_played(self):
        self.lands_played = 0
                
    def increment_lands_played(self):
        self.lands_played += 1
        
    def can_play_land(self):
        return self.lands_played < 1
    
    def put_into_play(self, permanent):
        self.permanents.append(permanent)

    def mulligan(self):
        hand_size = len(self.hand)
        self.library += self.hand
        self.hand = []
        self.shuffle_library()
        for i in range(hand_size-1):
            self.draw()

    def get_max_hand_size(self):
        """Returns this player's current maximum hand size"""
        # TODO: Add in other possibilities besides 7
        return 7

    def discard_to_max_hand(self):
        while len(self.hand) > self.get_max_hand_size():
            self.discard(self.choose_hand_card())

    def untap(self):
        """Untaps all permanents that will untap during this untap step"""
        # TODO: Implement this once permanents are implemented
        pass

    def choose_action(self, game):
        """This player chooses what action to take when they have priority.
        Should return an object with a resolve method. Usually an instance of
        the action class"""
        raise NotImplementedError()

    def choose_mulligan(self):
        """Choose whether to mulligan. Returns a boolean"""
        raise NotImplementedError()

    def declare_attackers(self, game):
        """Returns a declaration of attackers"""
        raise NotImplementedError()

    def declare_blockers(self, game, attackers):
        """Returns a declaration of blockers"""
        raise NotImplementedError()

    def choose_hand_card(self):
        """Choose a card in the hand and return the index in the hand
        of that card"""
        raise NotImplementedError()
