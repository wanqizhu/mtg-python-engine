import random

class Player(object):
    """Represents a player in a game"""
    def __init__(self, deck):
        self.library = deck
        self.hand = []
        self.graveyard = []
        self.life = 20
    
    def draw(self):
        """Draw a card from the library to the hand"""
        self.hand.append(self.library.pop())

    def shuffle_library(self):
        """Shuffle the library"""
        random.shuffle(self.library)

    def draw_starting_hand(self):
        for i in range(7):
            self.draw()

    def mulligan(self):
        hand_size = len(self.hand)
        self.library += self.hand
        self.hand = []
        self.shuffle_library()
        for i in range(hand_size-1):
            self.draw()
