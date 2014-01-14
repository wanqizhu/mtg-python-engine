class Permanent(object):
    def __init__(self, card):
        self.card = card
        self.tapped = card.comes_into_play_tapped
        
    def get_name(self):
        return card.get_name()

    @property
    def card_type(self):
        return self.card.card_type

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

    @property
    def activated_abilities(self):
        return self.card.activated_abilities
