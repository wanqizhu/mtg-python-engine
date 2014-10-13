__author__ = 'Michael'

class Characteristics(object):
    def __init__(self,
                 name='',
                 mana_cost=None,
                 color=None,
                 color_indicator=None,
                 card_type=None,
                 subtype=None,
                 supertype=None,
                 text=None,
                 abilities=None,
                 power=None,
                 toughness=None,
                 loyalty=None,
                 hand_modifier=None,
                 life_modifier=None):
        self.name = name
        self.mana_cost = mana_cost
        self.color = color
        self.color_indicator = color_indicator
        self.card_type = card_type
        self.subtype = subtype
        self.supertype = supertype
        self.text = text
        self.abilities = abilities
        self.power = power
        self.toughness = toughness
        self.loyalty = loyalty
        self.hand_modifier = hand_modifier
        self.life_modifier = life_modifier
