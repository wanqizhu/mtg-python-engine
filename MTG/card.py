# This file is currently a stub representing card objects

class Card(object):
    """Superclass for all card classes (which will be generated dynamically)"""
    def get_text(self):
        raise NotImplementedError()

def gen_card_class(oracle_text):
    """Generates a class for the particular card text"""
    class ThisCard(Card):
        pass
    return ThisCard
