import random

from .. import game

import test_cards
from test_player import TestPlayer

def build_land_deck():
    return [random.choice(test_cards.BASIC_LANDS) for i in range(60)]